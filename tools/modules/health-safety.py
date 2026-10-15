# Worker Health and Safety Awareness — O. Reg. 297/13
SLUG = "health-safety"
TITLE = "Health & Safety Awareness"
SUBTITLE = ("Your three rights under Ontario law, who is responsible for what, and how hazards "
            "get found and fixed in a workplace that is somebody else's home.")
COVERS = "O. Reg. 297/13 · legislated"
TIME = "About 25 minutes"
VERSION = "2026.1"
PASS_MARK = 11
GLYPH = '<path d="M16 7l8 3.5v6c0 5-3.4 8-8 9.5-4.6-1.5-8-4.5-8-9.5v-6z"/><path d="M12.5 16l2.5 2.5 5-5"/>'
COLOUR = dict(light="#3D6B4F", mid="#55836A", ink="#335942",
              dark="#8FC2A4", darkbg="#284634")
INTRO = ("Ontario requires every worker to complete health and safety awareness training. Work "
         "through five short sections, then take the check.")
TOC_NOTE = ("Supervisors complete a separate supervisor version in addition to this one. Tell the "
            "office if you supervise other staff.")

SECTIONS = [
 {"name": "Your three rights", "sops": "Legislated · OHSA",
  "lede": "Ontario's Occupational Health and Safety Act gives every worker the same three rights. "
          "They are not company policy and nobody can sign them away.",
  "rules": [
   ["The right to know", "To be told about the hazards you may be exposed to, and to be trained on them. WHMIS, safe handling and violence training all come from this right.", "OHSA"],
   ["The right to participate", "To take part in keeping the workplace safe: raising concerns, reporting hazards, and through a health and safety representative or committee where the workplace has one.", "OHSA"],
   ["The right to refuse unsafe work", "To refuse work you believe is likely to endanger you. You report the refusal to your supervisor, who must investigate.", "OHSA", 1],
   ["The health care limit on refusal", "For health care workers the right to refuse does not apply where the refusal would directly endanger the life, health or safety of a client. That never means walking away: it means not doing the unsafe thing, keeping the client safe where they are, and calling your supervisor.", "OHSA", 1],
   ["No reprisal", "An employer may not punish you for using these rights. Discipline, lost shifts or pressure for raising a safety concern is prohibited.", "OHSA"],
  ],
  "scene": {"h": "A transfer that does not look safe",
   "t": "The care plan says a one-person transfer. Today your client is much weaker, sliding in the chair, and you do not think you can do it alone without hurting one of you.",
   "c": [["Attempt it — the care plan says one person", 0, "No. The care plan describes the client on a usual day. A change in condition changes the risk, and following a plan does not make an unsafe lift safe."],
         ["Do not do the transfer. Keep her comfortable and safe where she is, and call your supervisor", 1, "Right. This is the refusal right working properly in health care: you stop the unsafe task, you do not abandon the client, and you get the plan reassessed."],
         ["Ask the family to help you lift her", 0, "No. An untrained family member makes it more dangerous, not less, and it leaves the underlying problem unfixed."]]}},

 {"name": "Who is responsible", "sops": "Legislated · OHSA",
  "lede": "The law gives duties to three groups. They overlap on purpose, so a hazard has to get "
          "past several people before it reaches you.",
  "rules": [
   ["The employer", "Must take every precaution reasonable in the circumstances to protect you. That includes training, equipment, policies and supervision — and acting on what you report.", "OHSA"],
   ["The supervisor", "Must make sure you work the way the law and the employer require, use the protection you have been given, and must tell you about hazards they know of.", "OHSA"],
   ["The worker — you", "Must work safely, use the equipment and protection provided, and report hazards, injuries and near misses. Not using provided equipment is itself a breach.", "OHSA"],
   ["Everyone, every time", "“Every precaution reasonable in the circumstances” is the standard. It is judged after the fact against what a careful employer would have done.", "OHSA"],
  ],
  "scene": {"h": "A step that moves",
   "t": "The back step into a client's home rocks when you stand on it. You have mentioned it to the family twice. Nothing has changed, and it is icy today.",
   "c": [["Keep using it carefully until the family fixes it", 0, "No. You have now identified a hazard that has not been controlled. Carrying on carefully is not a control."],
         ["Use the front door, report it to your supervisor as a hazard, and ask the office to take it up with the family", 1, "Right. Avoid it, report it formally so it is on record, and let the employer carry out its duty to address it."],
         ["Refuse to attend the client at all", 0, "Too far, too early. There is a safe route in. Use it, report the hazard, and let your supervisor assess."]]}},

 {"name": "Finding and fixing hazards", "sops": "Legislated · OHSA",
  "lede": "Hazard control follows an order. Removing a hazard beats guarding against it, and both "
          "beat relying on a person to be careful.",
  "rules": [
   ["1. Get rid of it", "Remove the hazard, or swap it for something safer. A mechanical lift instead of a manual one; a safer cleaning product.", "Hierarchy of control"],
   ["2. Contain or guard it", "If you cannot remove it, put something between it and the worker. A sharps container. A locked cupboard.", "Hierarchy of control"],
   ["3. Change how the work is done", "Procedures, training, scheduling, rest, two-person tasks.", "Hierarchy of control"],
   ["4. Personal protective equipment, last", "Gloves, masks, eye protection. PPE protects one person and only while it is worn correctly — which is why it is last, not first.", "Hierarchy of control", 1],
   ["Four kinds of hazard", "Physical (slips, lifting, noise), chemical (cleaning products, oxygen), biological (infection, sharps) and psychological (violence, harassment, working alone, stress). All four are real in home care.", "OHSA"],
   ["Report the near miss too", "The trip that nearly happened is free information about the fall that would have. Report it the same way.", "SOP 47"],
  ],
  "scene": {"h": "Which control comes first",
   "t": "Staff keep straining their backs repositioning a heavy client up the bed. The office asks what should be done.",
   "c": [["Issue back belts to everyone", 0, "No. That is personal protective equipment, the last resort, and back belts do not prevent these injuries."],
         ["Remind staff to use proper body mechanics", 0, "No. That is relying on the person to be careful, which is near the bottom of the hierarchy. Technique alone cannot make an unsafe load safe."],
         ["Get a slide sheet or mechanical aid so nobody lifts the load by hand", 1, "Right. Remove the hazard — take the manual lift out of the task. That beats guarding against it or training around it."]]}},

 {"name": "Working alone, in someone's home", "sops": "Legislated · SOPs 37, 42",
  "lede": "Home care has a hazard most workplaces do not: you are alone, in a private space you do "
          "not control, with no colleague in the next room.",
  "rules": [
   ["Your car and the route count", "Driving between clients is work. Ice, fatigue and rushing between visits are workplace hazards.", "SOP 37"],
   ["Tell someone where you are", "Keep your schedule current so the office knows where you should be and when. Check in as your schedule requires.", "SOP 37"],
   ["Leave if you feel unsafe", "You do not need permission and you do not need proof. Leave, get somewhere safe, then call your supervisor.", "SOP 37", 1],
   ["Pets, smoking, weapons, other people", "These are workplace hazards and are assessed at intake. If something changes, report it so the assessment changes too.", "SOP 1"],
   ["Fatigue is a hazard", "Back-to-back visits, missed breaks and long drives make mistakes more likely. Raise it before it becomes an incident.", "OHSA"],
  ],
  "scene": {"h": "Something has changed at the house",
   "t": "You arrive for a regular visit. There is a man you have never seen on the porch, shouting into a phone, and he blocks the door when he sees you.",
   "c": [["Try to get past him — the client is expecting you", 0, "No. Your safety comes first, and an unknown agitated person at the door is a reason to stop."],
         ["Leave, get to a safe place, then call your supervisor so the visit and the client's welfare are both handled", 1, "Right. Withdraw first, then report. The office can arrange a welfare check and reassess the visit."],
         ["Wait in the car until he leaves, then go in without mentioning it", 0, "Half right. Waiting somewhere safe is sensible, but not reporting leaves the hazard in place for whoever comes next."]]}},

 {"name": "If something happens", "sops": "Legislated · SOPs 43, 47",
  "lede": "Reporting is how a one-off becomes a fix. It also protects your entitlement if an injury "
          "turns out to be worse than it looked.",
  "rules": [
   ["Tell your supervisor the same shift", "Every injury, exposure and near miss, however small it seems.", "SOP 43"],
   ["Get first aid or medical attention", "Have it recorded. A strain that seems minor on the day can need treatment later, and the record matters then.", "SOP 43"],
   ["WSIB", "Ontario's Workplace Safety and Insurance Board covers workers injured at work. Atria must report an injury needing health care beyond first aid, or causing lost time, within 3 business days.", "SOP 43"],
   ["Critical injuries and the Ministry of Labour", "A critical injury must be reported to the Ministry of Labour immediately, and the scene must not be disturbed except to help the injured person.", "OHSA", 1],
   ["The Ministry of Labour", "Enforces the Act. Inspectors can visit any workplace, including a client's home where work is done, and can order work stopped.", "OHSA"],
   ["No reprisal, again", "Nobody may be penalised for reporting an injury or a hazard.", "OHSA"],
  ],
  "scene": {"h": "A strain that feels minor",
   "t": "Helping a client reposition, you feel a sharp pull in your lower back. By the end of the shift it is an ache you think will pass.",
   "c": [["Say nothing and see how it feels tomorrow", 0, "No. If it worsens you will be reporting an injury with no record from the day it happened, which affects both the investigation and your claim."],
         ["Tell your supervisor before the end of the shift, get it recorded, and seek care if it does not settle", 1, "Right. Report it the same shift. The record protects you, and it tells the office a task needs looking at."],
         ["Mention it at your next supervisory visit", 0, "Too late. Injuries are reported the same shift."]]}},
]

QUIZQ = [
 {"s":0,"q":"What are a worker's three rights under Ontario's OHSA?","o":["To know, to participate, to refuse unsafe work","To know, to be paid, to take breaks","To refuse, to resign, to complain","To train, to supervise, to inspect"],"a":0,"e":"The right to know, the right to participate, and the right to refuse unsafe work."},
 {"s":0,"q":"How does the right to refuse work differ for health care workers?","o":["It does not apply at all","It does not apply where refusing would directly endanger a client's life, health or safety","It applies only with a doctor's note","It applies only to nurses"],"a":1,"e":"The limit is specific. It never means abandoning a client: stop the unsafe task, keep the client safe, call your supervisor."},
 {"s":0,"q":"Your supervisor warns you that raising a safety concern again will cost you shifts. What is that?","o":["Normal management","A prohibited reprisal under the OHSA","Acceptable if the concern was wrong","A performance issue"],"a":1,"e":"Reprisal for using your health and safety rights is prohibited. Report it."},
 {"s":1,"q":"Which is a worker's duty under the OHSA?","o":["To write the health and safety policy","To use the equipment and protection provided, and report hazards","To inspect other workplaces","To decide what training is required"],"a":1,"e":"Work safely, use what you are given, and report hazards, injuries and near misses. Not using provided equipment is itself a breach."},
 {"s":1,"q":"What standard does the law hold the employer to?","o":["Whatever is affordable","Whatever the client agrees to","Every precaution reasonable in the circumstances","Best efforts"],"a":2,"e":"“Every precaution reasonable in the circumstances” — judged against what a careful employer would have done."},
 {"s":2,"q":"In the hierarchy of hazard control, which comes FIRST?","o":["Personal protective equipment","Changing how the work is done","Getting rid of the hazard or swapping it for something safer","Guarding it"],"a":2,"e":"Remove or substitute first. PPE is last because it protects one person, only while worn correctly."},
 {"s":2,"q":"Where does personal protective equipment sit in the hierarchy?","o":["First, it is the most reliable","Last, it is the least reliable","Second","It is not part of the hierarchy"],"a":1,"e":"Last. It does nothing about the hazard itself and depends on a person wearing it properly every time."},
 {"s":2,"q":"Which of these is a psychological hazard?","o":["A wet floor","A cleaning product","Working alone with an aggressive family member","A used lancet"],"a":2,"e":"Violence, harassment, working alone and chronic stress are psychological hazards, and they are as real as the physical ones."},
 {"s":2,"q":"You trip on a rug but catch yourself and are not hurt. What should you do?","o":["Nothing, no one was hurt","Report it as a near miss","Move the rug and say nothing","Mention it only if it happens again"],"a":1,"e":"A near miss is free information about the injury that would have happened. Report it the same way."},
 {"s":3,"q":"You arrive at a visit and feel unsafe because of someone at the property. What do you do?","o":["Go in anyway; the client is expecting you","Leave, get somewhere safe, then call your supervisor","Wait in the car and say nothing afterwards","Call the police before telling anyone at Atria"],"a":1,"e":"Withdraw first, then report. You do not need proof or permission to leave a situation that feels unsafe."},
 {"s":3,"q":"Is driving between client visits part of your workplace?","o":["No, it is personal time","Yes — driving for work is work, and road and weather conditions are workplace hazards","Only if you are paid mileage","Only in winter"],"a":1,"e":"Driving between clients is work. Ice, fatigue and rushing between visits are workplace hazards."},
 {"s":4,"q":"You strain your back during a visit. When do you report it?","o":["The same shift","Within a week","At your next supervisory visit","Only if you need time off"],"a":0,"e":"Same shift, every time. The record from the day matters if it turns out worse than it looked."},
 {"s":4,"q":"Within how long must an employer report an injury that needs health care beyond first aid to the WSIB?","o":["24 hours","3 business days","7 days","30 days"],"a":1,"e":"Three business days for an injury needing health care beyond first aid or causing lost time (SOP 43)."},
 {"s":4,"q":"A critical injury happens at a client's home. What must NOT happen?","o":["Calling 911","Helping the injured person","Disturbing the scene before the Ministry of Labour releases it","Telling the supervisor"],"a":2,"e":"The scene is not disturbed except to help the injured person, and the Ministry of Labour is notified immediately."},
 {"s":4,"q":"Who enforces the Occupational Health and Safety Act?","o":["The WSIB","The Ministry of Labour","The College of Nurses of Ontario","The employer"],"a":1,"e":"The Ministry of Labour enforces the Act and its inspectors can order work stopped. The WSIB handles injury insurance and benefits."},
]
