/* Atria PDF round-trip, shared by every fillable template.
   The printed PDF carries the form's own answers as text, so uploading that
   same PDF back into the template restores every field.

   A template supplies two hooks:
     window.atriaCollect()      -> a plain object holding the form's answers
     window.atriaApply(obj)     -> writes that object back into the form
   Templates with no state model of their own use atriaGenericCollect/Apply.

   Source of truth: tools/pdf-roundtrip.js. Injected inline by
   tools/add_roundtrip.py; edit it there and re-run, never in the template. */
(function(){
  var MARK='ATRIA-DATA-V1', END='ATRIA-DATA-END', WIDTH=100;

  function enc(s){ var b=new TextEncoder().encode(s), o='';
    for(var i=0;i<b.length;i++){ o+=String.fromCharCode(b[i]); } return btoa(o); }
  function dec(s){ var b=atob(s), a=new Uint8Array(b.length);
    for(var i=0;i<b.length;i++){ a[i]=b.charCodeAt(i); } return new TextDecoder().decode(a); }
  var SKIP='.import-panel,.atria-import,.import-wrap,[data-atria-skip]';
  function list(root,sel){
    /* the upload panels are part of the page, not the form */
    return Array.prototype.slice.call((root||document).querySelectorAll(sel))
      .filter(function(el){ return !el.closest(SKIP); });
  }

  /* ---------- the block that rides along in the PDF ---------- */
  function build(){
    var el=document.getElementById('atriaData');
    if(!el || typeof window.atriaCollect!=='function'){ return; }
    el.textContent='';
    var payload;
    try{ payload=enc(JSON.stringify(window.atriaCollect())); }
    catch(e){ return; }
    function ln(text, cls){
      var d=document.createElement('div'); d.className=cls||'adl';
      d.textContent=text; el.appendChild(d);
    }
    ln(MARK,'adl adl-mark');
    /* Each chunk is short enough that it cannot wrap at the printed size.
       A wrapped line would put its closing ~ on the next row, and the reader
       would pair that tilde with the wrong chunk. */
    /* Base64 only, and each line is framed with ~, so a browser's own print
       header or page number landing on these pages cannot be read as payload.
       One element per line: a single wrapped paragraph gets reflowed on print
       and the lines run together. */
    for(var i=0;i<payload.length;i+=WIDTH){ ln('~'+payload.substr(i,WIDTH)+'~'); }
    ln(END,'adl adl-mark');
  }
  window.atriaBuildData=build;
  window.addEventListener('beforeprint', build);

  window.atriaReadData=function(text){
    var a=text.indexOf(MARK); if(a<0){ return null; }
    var b=text.indexOf(END,a); if(b<0){ b=text.length; }
    var seg=text.slice(a+MARK.length,b), chunks=[], re=/~([A-Za-z0-9+\/=\s]+?)~/g, m;
    while((m=re.exec(seg))){ chunks.push(m[1].replace(/\s+/g,'')); }
    if(!chunks.length){ return null; }
    /* every chunk but the last is a full line; a short one means the text came
       back broken, and a half-restored form is worse than none */
    for(var i=0;i<chunks.length-1;i++){
      if(chunks[i].length!==WIDTH){ return null; }
    }
    var out=chunks.join('');
    try{ return JSON.parse(dec(out)); }catch(e){ return null; }
  };

  /* ---------- reading a PDF ---------- */
  function itemsToText(items){
    var lines={}, order=[];
    items.forEach(function(it){
      if(!it.str) return;
      var y=Math.round(it.transform[5]);
      if(!lines[y]){ lines[y]=[]; order.push(y); }
      lines[y].push({x:it.transform[4], w:it.width||0, h:it.height||0, s:it.str});
    });
    order.sort(function(a,b){ return b-a; });
    return order.map(function(y){
      var parts=lines[y].sort(function(a,b){ return a.x-b.x; }), line='', prev=null;
      parts.forEach(function(p){
        if(prev){
          /* PDFs carry their own space items; adding one between every pair
             doubles them and splits hyphenated words. */
          var gap=p.x-(prev.x+prev.w);
          if(gap > Math.max(1,(p.h||prev.h||10)*0.22) && !/\s$/.test(line) && !/^\s/.test(p.s)){ line+=' '; }
        }
        line+=p.s; prev=p;
      });
      return line.replace(/[ \t]+/g,' ').trim();
    }).filter(Boolean).join('\n');
  }

  var V='3.11.174', CDN='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/'+V+'/', pending=null;
  function script(src){
    return new Promise(function(res,rej){
      var sc=document.createElement('script'); sc.src=src;
      sc.onload=function(){ res(); };
      sc.onerror=function(){ rej(new Error('Could not download the PDF reader. Check your connection and try again.')); };
      document.head.appendChild(sc);
    });
  }
  function ensureLib(){
    /* PDF.js normally starts a Worker from the CDN, and a Worker cannot be
       created from another origin: that path hangs for ever instead of
       failing. Loading the worker file as a page script lets it parse on this
       thread instead, which costs a brief pause and always works. */
    if(window.pdfjsLib && window.pdfjsWorker){ return Promise.resolve(window.pdfjsLib); }
    if(pending){ return pending; }
    var first=window.pdfjsLib ? Promise.resolve() : script(CDN+'pdf.min.js');
    pending=first.then(function(){
      return window.pdfjsWorker ? null : script(CDN+'pdf.worker.min.js');
    }).then(function(){
      if(!window.pdfjsLib){ throw new Error('The PDF reader did not load.'); }
      window.pdfjsLib.GlobalWorkerOptions.workerSrc=CDN+'pdf.worker.min.js';
      return window.pdfjsLib;
    });
    return pending;
  }

  /* A browser prints its own header and footer into the page margin: the page
     title and time at the top, the address and "Page 3 of 18" at the bottom.
     They are ordinary text to a PDF reader, so without this they get read as
     part of the record and end up inside a findings or contact field. */
  var RUNNING=[
    /\bPage\s+\d+\s+of\s+\d+\b/i,
    /\d{4}-\d{2}-\d{2},?\s+\d{1,2}:\d{2}(:\d{2})?\s*(AM|PM)?$/i,
    /\d{1,2}\/\d{1,2}\/\d{2,4},?\s+\d{1,2}:\d{2}(:\d{2})?\s*(AM|PM)?$/i,
    /^\S*:\/\/\S+(\s+\d+\s*\/\s*\d+)?$/i,   /* an address, with or without Chrome's 3/12 */
    /^\d+\s*\/\s*\d+$/                      /* a bare page counter */
  ];
  function looksRunning(line){
    if(!line) return false;
    for(var i=0;i<RUNNING.length;i++){ if(RUNNING[i].test(line)) return true; }
    return false;
  }
  window.atriaStripRunningHeads=function(pages){
    function edge(page, top){
      var lines=page.split('\n');
      while(lines.length && looksRunning(top ? lines[0] : lines[lines.length-1])){
        if(top){ lines.shift(); } else { lines.pop(); }
      }
      return lines.join('\n');
    }
    pages=pages.map(function(p){ return edge(edge(p,true),false); });
    if(pages.length<2){ return pages; }
    /* whatever is left and still repeats, word for word bar the numbers, at the
       same edge of most pages is also furniture */
    function norm(s){ return String(s||'').replace(/\d+/g,'#').replace(/\s+/g,' ').trim(); }
    [true,false].forEach(function(top){
      var keys=pages.map(function(p){
        var l=p.split('\n'); if(!l.length) return '';
        return norm(top ? l[0] : l[l.length-1]);
      });
      var counts={};
      keys.forEach(function(k){ if(k){ counts[k]=(counts[k]||0)+1; } });
      var need=Math.max(2, Math.ceil(pages.length*0.6));
      pages=pages.map(function(p,i){
        if(!keys[i] || counts[keys[i]]<need) return p;
        var l=p.split('\n'), line=top ? l[0] : l[l.length-1];
        /* never drop something that looks like a record row */
        if(line.indexOf('|')>-1 || /^[A-Z][A-Z &/]{4,}$/.test(line.trim())) return p;
        if(top){ l.shift(); } else { l.pop(); }
        return l.join('\n');
      });
    });
    return pages;
  };

  window.atriaPdfText=function(file){
    return ensureLib().then(function(lib){
      return file.arrayBuffer().then(function(buf){
        return lib.getDocument({data:buf, disableWorker:true}).promise;
      });
    }).then(function(pdf){
      var out=[], chain=Promise.resolve();
      for(var n=1;n<=pdf.numPages;n++){
        (function(page){
          chain=chain.then(function(){
            return pdf.getPage(page)
              .then(function(pg){ return pg.getTextContent(); })
              .then(function(tc){ out.push(itemsToText(tc.items)); });
          });
        })(n);
      }
      return chain.then(function(){ return window.atriaStripRunningHeads(out).join('\n'); });
    });
  };

  /* ---------- a generic form, for templates with no state model ---------- */
  function ceText(node){
    var parts=[];
    (function walk(n){
      for(var i=0;i<n.childNodes.length;i++){
        var c=n.childNodes[i];
        if(c.nodeType===3){ parts.push(c.nodeValue); continue; }
        if(c.nodeType!==1) continue;
        if(c.tagName==='BR'){ parts.push('\n'); continue; }
        if(/^(DIV|P|LI)$/.test(c.tagName) && parts.length){ parts.push('\n'); }
        walk(c);
      }
    })(node);
    return parts.join('').replace(/ /g,' ').replace(/\n{3,}/g,'\n\n').trim();
  }
  function setCe(node, text){
    node.textContent='';
    String(text==null?'':text).split('\n').forEach(function(part,i){
      if(i){ node.appendChild(document.createElement('br')); }
      node.appendChild(document.createTextNode(part));
    });
  }
  var TEXTIN='input[type="text"],input[type="date"],input[type="number"],input[type="tel"],input[type="email"],input:not([type])';

  window.atriaGenericCollect=function(){
    return {
      t:'atria-form', v:1, id:window.atriaFormId||document.title,
      ce:list(document,'[contenteditable]').map(ceText),
      inp:list(document,TEXTIN).map(function(e){ return e.value; }),
      ta:list(document,'textarea').map(function(e){ return e.value; }),
      cb:list(document,'input[type="checkbox"]').map(function(e){ return e.checked?1:0; }),
      bx:list(document,'.box').map(function(e){ return e.classList.contains('checked')?1:0; })
    };
  };
  window.atriaGenericApply=function(d){
    var n=0;
    function pour(nodes, vals, set){
      if(!vals) return;
      nodes.forEach(function(el,i){ if(i<vals.length){ set(el,vals[i]); if(vals[i]) n++; } });
    }
    pour(list(document,'[contenteditable]'), d.ce, setCe);
    pour(list(document,TEXTIN), d.inp, function(e,v){ e.value=v==null?'':v; });
    pour(list(document,'textarea'), d.ta, function(e,v){ e.value=v==null?'':v; });
    pour(list(document,'input[type="checkbox"]'), d.cb, function(e,v){ e.checked=!!v; });
    pour(list(document,'.box'), d.bx, function(e,v){ e.classList.toggle('checked', !!v); });
    return n;
  };

  /* ---------- the upload panel ---------- */
  window.atriaMountImport=function(){
    var pick=document.getElementById('atriaPick'),
        file=document.getElementById('atriaFile'),
        drop=document.getElementById('atriaDrop'),
        stat=document.getElementById('atriaStatus');
    if(!pick||!file||!drop){ return; }
    function say(msg,kind){
      if(!stat) return;
      stat.textContent=msg||'';
      stat.className='atria-status'+(kind?' '+kind:'');
    }
    function take(files){
      var f=Array.prototype.slice.call(files).filter(function(x){
        return /\.pdf$/i.test(x.name)||x.type==='application/pdf'; })[0];
      if(!f){ say('Choose the PDF this template saved.','warn'); return; }
      say('Reading '+f.name+'…');
      window.atriaPdfText(f).then(function(text){
        if(!text || !text.replace(/\s/g,'')){
          say('That PDF has no text in it — it is a scan or a photo. Save the form again with Download / Save as PDF, and upload that file.','warn');
          return;
        }
        var data=window.atriaReadData(text);
        if(!data){
          say('That PDF has text, but none of this form’s saved answers. Upload a PDF that this template produced.','warn');
          return;
        }
        var filled=window.atriaApply(data);
        say('Restored '+filled+' filled field'+(filled===1?'':'s')+' from '+f.name+'. Check each section before saving.','ok');
      }).catch(function(err){
        say(String(err&&err.message||err),'warn');
      });
    }
    pick.addEventListener('click', function(){ file.click(); });
    file.addEventListener('change', function(){ if(file.files.length){ take(file.files); } file.value=''; });
    drop.addEventListener('dragover', function(e){ e.preventDefault(); drop.classList.add('over'); });
    drop.addEventListener('dragleave', function(){ drop.classList.remove('over'); });
    drop.addEventListener('drop', function(e){
      e.preventDefault(); drop.classList.remove('over');
      if(e.dataTransfer.files.length){ take(e.dataTransfer.files); }
    });
  };
  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded', function(){ window.atriaMountImport(); });
  } else { window.atriaMountImport(); }
})();
