# Workplace Violence and Harassment — OHSA ss. 32.0.1-32.0.8
SLUG = "violence-harassment"
TITLE = "Violence & Harassment"
SUBTITLE = ("What counts, what to do about it, and how reporting works when the workplace is "
            "somebody's living room and you are there alone.")
COVERS = "OHSA Part III.0.1 · legislated"
TIME = "About 25 minutes"
VERSION = "2026.1"
PASS_MARK = 11
GLYPH = '<path d="M16 7l8 3.5v6c0 5-3.4 8-8 9.5-4.6-1.5-8-4.5-8-9.5v-6z"/><path d="M16 12.5v5M16 20.5v.5"/>'
COLOUR = dict(light="#4F535C", mid="#6B707A", ink="#43464E",
              dark="#B2B8C2", darkbg="#363940")
INTRO = ("Ontario requires training on workplace violence and harassment. Work through five short "
         "sections, then take the check.")
TOC_NOTE = ("Atria's policy and the reporting routes are covered in section 4. Ask your supervisor "
            "for a copy of the written policy if you do not have one.")

SECTIONS = [
 {"name": "What counts", "sops": "Legislated · OHSA",
  "lede": "The law defines these terms, and the definitions are wider than most people expect. "
          "Nothing here requires an injury to have happened.",
  "rules": [
   ["Workplace violence", "The use of physical force, an attempt to use it, or a statement or behaviour that a worker could reasonably interpret as a threat. The threat counts on its own.", "OHSA", 1],
   ["Workplace harassment", "A course of vexatious comment or conduct that is known, or ought reasonably to be known, to be unwelcome. Usually repeated — but one serious incident can be enough.", "OHSA"],
   ["Sexual harassment", "Comment or conduct because of sex, sexual orientation, gender identity or gender expression, or a sexual advance by someone in a position to grant or deny a benefit.", "OHSA", 1],
   ["It is not just colleagues", "In home care it is far more often a client, a family member, a visitor or someone else in the household.", "SOP 42"],
   ["Reasonable management is not harassment", "Assigning work, correcting performance or managing attendance is not harassment, as long as it is done reasonably.", "OHSA"],
  ],
  "scene": {"h": "A joke that is not funny",
   "t": "A client's son makes comments about your body every visit. He laughs each time and says you are too sensitive when you look uncomfortable.",
   "c": [["Ignore it — he is joking and it is his mother's house", 0, "No. Repeated unwelcome comment of a sexual nature is sexual harassment, whoever makes it and wherever it happens. His intent does not decide it."],
         ["Report it to your supervisor — this is sexual harassment and it is covered by the policy", 1, "Right. It is unwelcome, it is repeated, and it is because of sex. Report it; you do not have to tolerate it to keep the client."],
         ["Tell him to stop and handle it yourself", 0, "Telling him is reasonable if you feel able, but it is not instead of reporting. The employer has a duty to act."]]}},

 {"name": "Dementia is not the same thing", "sops": "SOPs 29, 42",
  "lede": "A client with dementia who hits out during personal care is a different situation from a "
          "person who chooses to threaten you. Both still get reported — for different reasons.",
  "rules": [
   ["Responsive behaviour has a cause", "Pain, fear, too much noise, being rushed, not understanding what is about to happen to their body. The behaviour is communication.", "SOP 29"],
   ["Look for the trigger before the behaviour", "Approach from the front, say what you are about to do, go slowly, and stop if they resist. Most of the prevention is in the approach.", "SOP 29"],
   ["Still report it", "Not to blame the client, but so the care plan changes: a different time of day, two staff, a different approach. Unreported, the next person meets the same thing unwarned.", "SOP 42", 1],
   ["Your safety still counts", "Step back, give space, leave the room if you need to. A client who cannot control their behaviour can still injure you.", "SOP 42"],
   ["Flag the risk at intake and after", "History of aggression is assessed before service starts and reassessed when things change (SOP 1). That assessment only works if incidents get reported.", "SOP 1"],
  ],
  "scene": {"h": "Hit during a wash",
   "t": "A client with advanced dementia strikes your arm while you are washing her face. She is frightened and shouting. It is the third time this month.",
   "c": [["Say nothing — she has dementia, she cannot help it", 0, "She may well not be responsible, but that is exactly why it must be reported. Three times in a month is a pattern the care plan should answer."],
         ["Stop, step back, come back to it later, and report it so the care plan and the approach can change", 1, "Right. Stop and give space in the moment, then report — not to blame her, but so the approach changes and the next person is not caught out."],
         ["Carry on quickly to get it over with", 0, "No. Rushing a frightened person is the most likely way to make it worse, for her and for you."]]}},

 {"name": "Seeing it coming", "sops": "SOPs 37, 42",
  "lede": "Most incidents give some warning. Noticing early is what gives you the room to leave.",
  "rules": [
   ["Early signs", "Raised voice, pacing, clenched hands, getting too close, fixed staring, refusing to let you move past.", "SOP 42"],
   ["Keep your exit", "Stay between the person and the door where you can. Never let yourself be backed into a bathroom, a bedroom or a corner.", "SOP 42", 1],
   ["Lower, slower, further back", "Lower your voice, slow down, give more space. Do not match their volume and do not stand over them.", "SOP 42"],
   ["Do not argue or correct", "Winning the point is not the goal. “I can see this isn't right. Let me sort it out” does more than being correct.", "SOP 42"],
   ["Leave before it escalates", "You do not need permission and you do not need to be sure. Leave, get somewhere safe, then call your supervisor.", "SOP 37", 1],
   ["Alcohol, drugs and weapons", "Any of these present changes the situation immediately. Withdraw and call the office; a firearm in the home is reported at once.", "SOP 1"],
  ],
  "scene": {"h": "Between you and the door",
   "t": "A client's partner is angry about the visit schedule. He is standing in the bedroom doorway, voice rising, and you are at the far side of the room.",
   "c": [["Explain the schedule clearly so he understands it is not your fault", 0, "No. You are explaining to someone escalating while they stand between you and the only way out. Position first, explanation later."],
         ["Stay calm, lower your voice, and move so you have a clear route to the door before anything else", 1, "Right. Deal with position first. Keep your exit, lower and slow your voice, and do not argue the point while you are cornered."],
         ["Tell him you are leaving and walk straight past him", 0, "Walking into someone who is escalating is how it becomes physical. Create the route calmly, do not force it."]]}},

 {"name": "Reporting, and what happens next", "sops": "Legislated · SOPs 42, 47",
  "lede": "The law requires Atria to have a policy, a program, and a way for you to report — "
          "including a way that does not go through the person causing the problem.",
  "rules": [
   ["Report every incident", "Including threats, including things said rather than done, and including incidents where you were not hurt.", "SOP 42"],
   ["If your supervisor is the problem", "The program must give you another route. Report to the owner or clinical lead instead. You are never required to report to the person involved.", "OHSA", 1],
   ["It gets investigated", "An incident or complaint must be investigated appropriately in the circumstances, and you must be told the results and any corrective action, in writing.", "OHSA", 1],
   ["Information travels to protect you", "Atria must tell you about a person with a history of violent behaviour you can expect to meet, where the risk is real — enough to protect you, no more than needed.", "OHSA"],
   ["Refusing work over violence", "You may refuse work where violence is likely to endanger you. The health care limit still applies: never abandon a client, but do not walk into danger.", "OHSA"],
   ["No reprisal", "Nobody may be penalised for reporting violence or harassment, or for taking part in an investigation.", "OHSA"],
   ["Domestic violence", "If Atria knows, or ought reasonably to know, that domestic violence may put a worker at risk in the workplace, it must take reasonable precautions. Tell the office if your own situation may follow you to work.", "OHSA"],
  ],
  "scene": {"h": "The person you report to",
   "t": "Your supervisor has been making comments that make you uncomfortable. The policy says to report harassment to your supervisor.",
   "c": [["Report to the supervisor anyway, as the policy says", 0, "No. The law requires an alternative route precisely so you are never made to report to the person involved."],
         ["Report to the owner or clinical lead instead, using the alternative route", 1, "Right. The program must provide another path. Use it."],
         ["Wait and see whether it stops", 0, "No. Waiting leaves it unreported and unaddressed, and the pattern usually continues."]]}},

 {"name": "After an incident", "sops": "SOPs 42, 43, 47",
  "lede": "What happens in the hours after matters, both for you and so the next person is not "
          "caught by the same thing.",
  "rules": [
   ["Get safe first, then call", "Distance before paperwork. Call 911 if anyone is in immediate danger.", "SOP 42"],
   ["Tell your supervisor the same shift", "Before you go home, not at your next shift.", "SOP 47"],
   ["Write facts, not conclusions", "What was said and done, in order, with times. “He raised his fist and said he'd put me through the wall” — not “he got aggressive”.", "SOP 47", 1],
   ["Injury means WSIB too", "A physical injury is reported like any workplace injury. Psychological injury from a traumatic event can also be a claim.", "SOP 43"],
   ["Support is available", "Being threatened at work affects people afterwards. Tell your supervisor what you need; it is not a weakness and it is not held against you.", "SOP 42"],
   ["The plan should change", "Reassessment, a second staff member, a different time, or ending service. If nothing changes after a report, raise it again.", "SOP 42"],
  ],
  "scene": {"h": "Writing it up",
   "t": "After a visit where a family member threatened you, your supervisor asks for an incident report.",
   "c": [["“Client's son became aggressive and threatening during the visit.”", 0, "Too vague. “Aggressive” is a conclusion. An investigation needs what actually happened."],
         ["“At 14:20 the client's son stood in the doorway, raised his voice and said he would put me through the wall if I came back. I left and called the office at 14:25.”", 1, "Right. Times, words as spoken, actions in order, and what you did. That is what an investigation can work with."],
         ["“Difficult visit, will discuss.”", 0, "No. The report is the record. A conversation that is not written down is not a record."]]}},
]

QUIZQ = [
 {"s":0,"q":"Does a threat count as workplace violence if nobody is touched?","o":["No, there must be physical contact","Yes — a statement or behaviour a worker could reasonably take as a threat counts","Only if it is written down","Only if it is repeated"],"a":1,"e":"The definition includes the attempt and the threat, not just the act."},
 {"s":0,"q":"A client's son repeatedly comments on your body and says you are too sensitive. What is this?","o":["Rudeness, but not covered","Sexual harassment under the OHSA","Only harassment if he is an employee","A client relations issue"],"a":1,"e":"Unwelcome comment because of sex is sexual harassment whoever makes it. In home care it is most often a client or family member."},
 {"s":0,"q":"Your supervisor corrects your documentation and sets a deadline to improve. Is that harassment?","o":["Yes, it is unwelcome","No — reasonable management of work and performance is not harassment","Only if done in front of others","Only if you disagree"],"a":1,"e":"Reasonable direction and performance management are excluded, provided they are carried out reasonably."},
 {"s":1,"q":"A client with dementia hits you during personal care. Do you report it?","o":["No, she cannot help it","Yes — so the approach and the care plan can change, and the next person is warned","Only if you are injured","Only if it happens again"],"a":1,"e":"Reporting is not about blame. It is how the care plan changes and how the next staff member is not caught unwarned."},
 {"s":1,"q":"What is the most useful thing to look at after a responsive behaviour during care?","o":["Whether the client should be discharged","What triggered it — pain, fear, noise, being rushed, not understanding","Whether the family was present","Whether anyone saw it"],"a":1,"e":"The behaviour is communication. Most of the prevention sits in the approach: front, slow, explained, stop if they resist."},
 {"s":2,"q":"You are in a bedroom and an angry family member is standing in the doorway. What do you do first?","o":["Explain the schedule so he calms down","Move so you have a clear route to the door","Walk straight past him","Call the office from where you stand"],"a":1,"e":"Position first. Never let yourself be cornered; keep your exit before you try to resolve anything."},
 {"s":2,"q":"Which of these is an early warning sign to act on?","o":["Raised voice, pacing, clenched hands, standing too close","Asking a lot of questions","Being quiet","Disagreeing with the care plan"],"a":0,"e":"These signs usually come before an incident, and noticing them early is what gives you room to leave."},
 {"s":2,"q":"Someone in the home is intoxicated and becoming unpredictable. What do you do?","o":["Finish the visit quickly","Withdraw and call the office","Ask them to leave the room","Carry on and mention it later"],"a":1,"e":"Alcohol, drugs or weapons change the situation immediately. Withdraw and call; do not try to manage it."},
 {"s":3,"q":"The person harassing you is your supervisor. Where do you report?","o":["To that supervisor, as the policy says","Through the alternative route — the owner or clinical lead","Nowhere, until you have proof","To the Ministry of Labour first"],"a":1,"e":"The law requires a reporting route that does not go through the person involved. You are never required to report to them."},
 {"s":3,"q":"After you report a harassment complaint, what must happen?","o":["Nothing until you put it in writing","It is investigated appropriately, and you are told the results and any corrective action in writing","It is discussed at the next staff meeting","It is kept on file in case of a pattern"],"a":1,"e":"An investigation appropriate in the circumstances, and written notice to you of the results and any corrective action."},
 {"s":3,"q":"You are assigned a client whose relative has a known history of violence. What is Atria required to do?","o":["Nothing, it is confidential","Tell you about the risk, enough to protect you","Cancel the service","Send two staff to every visit regardless"],"a":1,"e":"Where the risk is real and you can expect to encounter the person, the employer must share enough information to protect you — no more than needed."},
 {"s":3,"q":"Can you be disciplined for reporting workplace violence?","o":["Yes, if the report turns out to be unfounded","No — reprisal for reporting or taking part in an investigation is prohibited","Only if you reported it late","Only if you told a colleague first"],"a":1,"e":"Reprisal is prohibited, including against people who take part in an investigation."},
 {"s":4,"q":"Which incident report is written correctly?","o":["“Client's son became aggressive during the visit.”","“At 14:20 the son stood in the doorway, raised his voice and said he would put me through the wall. I left and called the office at 14:25.”","“Difficult visit, will discuss.”","“The son has always been a problem.”"],"a":1,"e":"Facts in order, with times and words as spoken. “Aggressive” is a conclusion an investigation cannot work from."},
 {"s":4,"q":"When do you report an incident of violence or harassment?","o":["The same shift, before you go home","Within a week","At your next supervisory visit","Only if you were injured"],"a":0,"e":"Same shift. Get safe first, then report — distance before paperwork, but the report happens that day."},
 {"s":4,"q":"You were not physically hurt but you are shaken after a threat. What is true?","o":["There is nothing to report because there was no injury","Psychological injury from a traumatic event can be a WSIB claim, and support is available","You must take time off","You should wait and see how you feel in a week"],"a":1,"e":"Report it, and tell your supervisor what support you need. Psychological injury from a traumatic workplace event can be a claim."},
]
