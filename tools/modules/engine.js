
(function(){
const MODULE_VERSION = "1.2";
const LOGO = document.querySelector(".logo-mark img").getAttribute("src");
const PASS_MARK = 52;

__SECTIONS__


const __QUIZQ__;

const steps = ["Welcome", ...SECTIONS.map(s=>s.name), "The check"];

/* build sections */
const ICON_CHECK='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>';
const ICON_ALERT='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>';
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}

const secWrap=document.getElementById("sections");
const toc=document.getElementById("toc");
SECTIONS.forEach((s,i)=>{
  const li=document.createElement("li"); li.textContent=`${s.name} (${s.sops})`; toc.appendChild(li);
  const el=document.createElement("section"); el.className="step"; el.dataset.name=s.name;
  el.innerHTML=`<p class="eyebrow">Section ${i+1} of ${SECTIONS.length} · ${s.sops}</p><h2></h2><div class="context lede-s"></div><div class="rules"></div>
  <div class="scene"><h3></h3><p class="t"></p><div class="choices"></div><div class="feedback" role="status"></div></div>`;
  el.querySelector("h2").textContent=s.name;
  el.querySelector(".lede-s").textContent=s.lede;
  const rules=el.querySelector(".rules");
  s.rules.forEach(r=>{ const d=document.createElement("div"); d.className="rule"+(r[3]?" red":"");
    d.innerHTML="<div class='rule-hd'><span class='ic'>"+(r[3]?ICON_ALERT:ICON_CHECK)+"</span><div class='rule-info'><h3></h3><div class='ref'></div></div></div><p></p>";
    d.querySelector("h3").textContent=r[0]; d.querySelector("p").textContent=r[1]; d.querySelector(".ref").textContent=r[2];
    rules.appendChild(d); });
  const sc=el.querySelector(".scene");
  sc.querySelector("h3").textContent="Try it: "+s.scene.h; sc.querySelector(".t").textContent=s.scene.t;
  const ch=sc.querySelector(".choices"), fb=sc.querySelector(".feedback");
  shuffle(s.scene.c.slice()).forEach(c=>{ const b=document.createElement("button"); b.className="choice"; b.textContent=c[0];
    b.onclick=()=>{ ch.querySelectorAll(".choice").forEach(x=>x.classList.remove("best","no"));
      b.classList.add(c[1]?"best":"no"); fb.className="feedback show "+(c[1]?"good":"bad"); fb.textContent=c[2]; };
    ch.appendChild(b); });
  secWrap.appendChild(el);
});

/* quiz */
const qEl=document.getElementById("quiz");
let lastS=-1;
QUIZQ.forEach((q,i)=>{
  if(q.s!==lastS){ const h=document.createElement("div"); h.className="qhead"; h.textContent=SECTIONS[q.s].name; qEl.appendChild(h); lastS=q.s; }
  const d=document.createElement("fieldset"); d.className="qq"; d.style.border="0"; d.style.padding="0";
  d.innerHTML=`<legend><strong>${i+1}. ${q.q}</strong></legend><div class="opts">${shuffle(q.o.map((o,j)=>j)).map(j=>`<label class="opt"><input type="radio" name="q${i}" value="${j}"><span>${q.o[j]}</span></label>`).join("")}</div><div class="ex">${q.e}</div>`;
  qEl.appendChild(d);
});

/* navigation */
const allSteps=[...document.querySelectorAll("section.step")];
const stopsEl=document.getElementById("stops");
allSteps.forEach(()=>stopsEl.appendChild(document.createElement("span")));
let cur=0, staffName="", passed=false;
const back=document.getElementById("backBtn"), next=document.getElementById("nextBtn");
const nameInput=document.getElementById("staffName"), startBtn=document.getElementById("startBtn");
function checkName(){ staffName=nameInput.value.trim(); startBtn.disabled = staffName.length<2; render(); }
nameInput.addEventListener("input",checkName);
startBtn.onclick=()=>go(1);
function go(n){ cur=Math.max(0,Math.min(allSteps.length-1,n)); render(); window.scrollTo({top:0}); }
function render(){
  allSteps.forEach((s,i)=>s.classList.toggle("on",i===cur));
  [...stopsEl.children].forEach((s,i)=>{ s.className = i<cur?"done":(i===cur?"now":""); });
  document.getElementById("stepName").textContent=allSteps[cur].dataset.name;
  document.getElementById("stepCount").textContent=`${cur+1} of ${allSteps.length}`;
  back.disabled = cur===0;
  const last = cur===allSteps.length-1;
  next.classList.toggle("hidden", last);
  next.disabled = cur===0 && staffName.length<2;
  next.textContent = cur===allSteps.length-2 ? "Go to the check" : "Next";
}
back.onclick=()=>go(cur-1);
next.onclick=()=>go(cur+1);

/* grading */
let dbRef=null, userRef=null, dlRef=null, myId=null;
document.getElementById("gradeBtn").onclick = async ()=>{
  const answers=QUIZQ.map((q,i)=>{ const sel=document.querySelector(`input[name=q${i}]:checked`); return sel? +sel.value : null; });
  const unanswered=answers.filter(a=>a===null).length;
  const res=document.getElementById("result");
  document.querySelectorAll("#quiz .opt").forEach(l=>l.classList.remove("right","wrong"));
  qEl.classList.remove("graded");
  if(unanswered){ res.innerHTML=`<div class="result fail"><strong>Answer every question to submit.</strong> ${unanswered} left.</div>`; return; }
  const score=answers.filter((a,i)=>a===QUIZQ[i].a).length;
  passed = score>=PASS_MARK;
  QUIZQ.forEach((q,i)=>{
    const lab=v=>document.querySelector(`input[name=q${i}][value="${v}"]`).closest(".opt");
    if(answers[i]!==q.a) lab(answers[i]).classList.add("wrong");
    if(passed) lab(q.a).classList.add("right");
  });
  const date=new Date().toLocaleDateString("en-CA",{year:"numeric",month:"long",day:"numeric"});
  if(passed){
    qEl.classList.add("graded");
    res.innerHTML=`<div class="result pass"><h3>You passed: ${score}/${QUIZQ.length}</h3><p style="margin:0">Read the explanations above for anything you missed.</p><p id="saveStatus" class="hint" style="margin:8px 0 0"></p></div>
    <div class="cert"><div class="logo-mark"><img src="${LOGO}" alt=""></div><div class="hint">Atria Private Care · Certificate of completion</div><div class="who"></div><div>has completed <strong>Care by the Book: Atria Client Care Procedures</strong></div><div class="hint" style="margin-top:8px">Score ${score}/${QUIZQ.length} · ${date} · Module v${MODULE_VERSION}</div></div>
    <div class="certActions"><button class="btn hidden" id="mailBtn" style="width:100%;margin-top:12px">Email my certificate</button>
    <button class="btn ghost hidden" id="printBtn" style="width:100%;margin-top:10px">Print or save as PDF</button>
    <button class="btn ghost hidden" id="dlBtn" style="width:100%;margin-top:10px">Download certificate</button></div>`;
    res.querySelector(".who").textContent=staffName;
  } else {
    const missed={}; QUIZQ.forEach((q,i)=>{ if(answers[i]!==q.a) missed[q.s]=(missed[q.s]||0)+1; });
    const list=Object.keys(missed).map(k=>`<li>${SECTIONS[k].name} (${missed[k]} wrong)</li>`).join("");
    res.innerHTML=`<div class="result fail"><h3>${score}/${QUIZQ.length}: not quite yet</h3><p>You need ${PASS_MARK} to pass. Answers marked in red are wrong. Sections to review:</p><ul class="clean">${list}</ul><p style="margin:0">Go back to those sections, then change your answers and submit again.</p><p id="saveStatus" class="hint" style="margin:8px 0 0"></p></div>`;
  }
  res.scrollIntoView({behavior:"smooth",block:"start"});
  await saveRecord(score,passed);
  const mail=document.getElementById("mailBtn"), pr=document.getElementById("printBtn"), dl=document.getElementById("dlBtn");
  if(mail){ mail.classList.remove("hidden"); mail.onclick=()=>emailCert(score,date); }
  if(pr){ pr.classList.remove("hidden"); pr.onclick=()=>window.print(); }
  if(dl){ dl.classList.remove("hidden"); dl.onclick=()=>saveCert(score,date); }
};

async function saveRecord(score,didPass){
  const st=document.getElementById("saveStatus");
  if(!dbRef || !myId){
    try{ localStorage.setItem("cbtb_record", JSON.stringify({name:staffName, score:score, passed:didPass,
      total:QUIZQ.length, completedAt:new Date().toISOString(), version:MODULE_VERSION})); }catch(e){}
    if(st) st.textContent = didPass
      ? "Send your certificate to the office using the buttons below, so it can be filed in your training record."
      : "Review the answers marked above, then submit again. Nothing is sent to the office until you pass and send your certificate.";
    return; }
  try{
    const ref=dbRef.doc("records/"+myId);
    let prev=null; try{ const s=await ref.get(); prev=s.exists?s.data():null; }catch(e){}
    const attempts=((prev&&prev.attempts)||0)+1;
    const rec=(prev && prev.passed && prev.version===MODULE_VERSION && !didPass) ? {...prev, attempts}
      : {name:staffName, score, total:QUIZQ.length, passed:didPass, completedAt:new Date().toISOString(), version:MODULE_VERSION, attempts};
    await ref.set(rec);
    if(st) st.textContent = didPass ? "Your completion has been recorded for your employer." : "This attempt has been recorded.";
  }catch(e){ if(st) st.textContent="Your result couldn't be recorded. Show your certificate to your supervisor."; }
}

const RETURN_EMAIL = "tlloyd@whtalife.com";

function certLines(score,date){
  return `Name: ${staffName}\nModule: Care by the Book: Atria Client Care Procedures (v${MODULE_VERSION})\nResult: Passed, ${score}/${QUIZQ.length}\nDate completed: ${date}`;
}
function emailCert(score,date){
  const subj=`Care by the Book certificate - ${staffName}`;
  const body=`Hello,\n\nI have completed the Care by the Book training module.\n\n${certLines(score,date)}\n\nThank you,\n${staffName}`;
  location.href=`mailto:${RETURN_EMAIL}?subject=${encodeURIComponent(subj)}&body=${encodeURIComponent(body)}`;
}

async function saveCert(score,date){
  const safe=staffName.replace(/[<>&"]/g,"");
  const html=`<!DOCTYPE html><html><head><meta charset="utf-8"><title>Care by the Book certificate - ${safe}</title></head><body style="font-family:Georgia,'Times New Roman',serif;color:#2C3E3E;background:#FAFAF8;text-align:center;margin:30px;padding:50px;border:6px double #6F9797"><div style="width:90px;height:90px;border-radius:50%;overflow:hidden;background:#FAF8F2;margin:0 auto 14px;display:flex;align-items:center;justify-content:center"><img src="${LOGO}" style="width:130%;height:130%;object-fit:contain" alt=""></div><p style="color:#5A8282;letter-spacing:1px;font-size:14px">ATRIA PRIVATE CARE</p><p>Certificate of completion</p><h1 style="font-size:40px;color:#5A8282;margin:10px 0">${safe}</h1><p>has completed</p><h2>Care by the Book: Atria Client Care Procedures</h2><p style="color:#4A6060">Score ${score}/${QUIZQ.length} &middot; ${date} &middot; Module v${MODULE_VERSION}</p></body></html>`;
  const fname=`CareByTheBook-certificate-${safe.replace(/\s+/g,"-")}.html`;
  if(dlRef){ try{ await dlRef.save({filename:fname, data:html}); return; }catch(e){} }
  try{
    const blob=new Blob([html],{type:"text/html;charset=utf-8"});
    const url=URL.createObjectURL(blob);
    const a=document.createElement("a");
    a.href=url; a.download=fname; a.style.display="none";
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(()=>URL.revokeObjectURL(url),2000);
  }catch(e){
    const w=window.open("","_blank"); if(w){ w.document.write(html); w.document.close(); }
  }
}

async function loadRecords(){
  const box=document.getElementById("records");
  try{
    const snap=await dbRef.collection("records").get();
    const rows=snap.docs.map(d=>d.data()).sort((a,b)=>(b.completedAt||"").localeCompare(a.completedAt||""));
    if(!rows.length){ box.innerHTML='<p class="hint">No completions yet. Share this page with staff as Contributors so their results record here.</p>'; return; }
    const t=document.createElement("table");
    t.innerHTML="<thead><tr><th>Name</th><th>Result</th><th>Score</th><th>Date</th><th>Version</th><th>Attempts</th></tr></thead><tbody></tbody>";
    const tb=t.querySelector("tbody");
    rows.forEach(r=>{ const tr=document.createElement("tr");
      const cells=[r.name||"—",null,`${r.score}/${r.total||37}`, r.completedAt?new Date(r.completedAt).toLocaleDateString("en-CA"):"—", (r.version||"—")+(r.version===MODULE_VERSION?"":" (old)"), r.attempts||1];
      cells.forEach((c,i)=>{ const td=document.createElement("td");
        if(i===1) td.innerHTML=r.passed?'<span class="pill p">Passed</span>':'<span class="pill f">Not passed</span>'; else td.textContent=c;
        tr.appendChild(td); });
      tb.appendChild(tr); });
    box.innerHTML=""; box.appendChild(t);
  }catch(e){ box.innerHTML='<p class="hint">Records couldn\'t be loaded right now. Reopen the page to try again.</p>'; }
}

(async()=>{
  if(!window.claude || !window.claude.use) return;
  try{ userRef=await window.claude.use("user"); }catch(e){}
  try{ dbRef=await window.claude.use("db"); }catch(e){}
  try{ dlRef=await window.claude.use("downloads"); }catch(e){}
  if(userRef){ try{ myId=await userRef.id(); }catch(e){} }
  if(dbRef && myId){
    try{ const s=await dbRef.doc("records/"+myId).get();
      if(s.exists){ const r=s.data(); const p=document.getElementById("priorRecord");
        p.textContent = r.version!==MODULE_VERSION ? "This module has been updated since your last completion. Please complete it again."
          : r.passed ? `You passed this module on ${new Date(r.completedAt).toLocaleDateString("en-CA",{year:"numeric",month:"long",day:"numeric"})} with ${r.score}/${r.total||37}. You're welcome to review it again.`
          : `Your last attempt scored ${r.score}/${r.total||37}. You need ${PASS_MARK} to pass.`;
        p.classList.remove("hidden");
        if(r.name && !nameInput.value){ nameInput.value=r.name; checkName(); } } }catch(e){}
  }
  let admin=false; if(userRef){ try{ admin=(await userRef.isOwner()) || (await userRef.canEdit()); }catch(e){} }
  if(admin && dbRef){ document.getElementById("adminPanel").classList.remove("hidden"); loadRecords(); }
})();

(function(){
  if(window.claude && window.claude.use) return;   /* on claude.ai the records panel handles this */
  try{
    const raw=localStorage.getItem("cbtb_record"); if(!raw) return;
    const r=JSON.parse(raw); const p=document.getElementById("priorRecord"); if(!p) return;
    p.textContent = r.version!==MODULE_VERSION
      ? "This module has been updated since you last completed it. Please work through it again."
      : r.passed
        ? `You passed this module on ${new Date(r.completedAt).toLocaleDateString("en-CA",{year:"numeric",month:"long",day:"numeric"})} with ${r.score}/${r.total}. This is saved on this device only.`
        : `Your last attempt on this device scored ${r.score}/${r.total}. You need ${PASS_MARK} to pass.`;
    p.classList.remove("hidden");
    if(r.name && nameInput && !nameInput.value){ nameInput.value=r.name; checkName(); }
  }catch(e){}
})();

render();
})();
