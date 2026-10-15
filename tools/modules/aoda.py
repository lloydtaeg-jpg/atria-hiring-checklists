# AODA Accessible Customer Service Standard
SLUG = "aoda"
TITLE = "Accessible Care"
SUBTITLE = ("Ontario's accessibility law, and what it asks of you in a client's home: dignity, "
            "independence, and asking before assuming.")
COVERS = "AODA customer service · legislated"
TIME = "About 20 minutes"
VERSION = "2026.1"
PASS_MARK = 10
GLYPH = '<circle cx="16" cy="9" r="2.4"/><path d="M16 13v7l-4 5M16 20l4 5M10.5 15h11"/>'
COLOUR = dict(light="#6B4A63", mid="#866080", ink="#593C52",
              dark="#C79BBD", darkbg="#4A3245")
INTRO = ("Ontario requires accessibility training for anyone who deals with the public. Work "
         "through four short sections, then take the check.")
TOC_NOTE = ("Everything here applies in the client's own home, which is both their private space "
            "and your workplace.")

SECTIONS = [
 {"name": "What the law asks", "sops": "Legislated · AODA",
  "lede": "The Accessibility for Ontarians with Disabilities Act sets a goal of an accessible "
          "province. The customer service standard is the part that governs how you deal with "
          "people day to day.",
  "rules": [
   ["Dignity", "Service that respects the person. Nothing that treats them as a problem to manage, and nothing done in a way that draws unnecessary attention.", "AODA"],
   ["Independence", "Let people do what they can do for themselves, even when it takes longer. Doing it for them because it is quicker takes something away.", "AODA", 1],
   ["Integration", "The same service, in the same way, wherever possible — not a separate lesser version.", "AODA"],
   ["Equal opportunity", "The same chance to benefit from the service as anyone else, which sometimes means doing something differently to reach the same result.", "AODA"],
   ["Disability is broad", "Physical, sensory, mental health, intellectual, learning, and conditions that are invisible or that come and go. You will not always know, and you do not need to.", "AODA"],
  ],
  "scene": {"h": "Faster, or independent",
   "t": "Your client with limited hand strength is buttoning her cardigan. It is taking several minutes and you are behind schedule. She has not asked for help.",
   "c": [["Do it for her so you can stay on time", 0, "No. She did not ask, and she can do it. Taking over removes her independence to save your minutes."],
         ["Wait, stay nearby, and offer help if she asks or struggles", 1, "Right. Independence means letting her do what she can, even when it is slower. Offer, do not assume."],
         ["Tell her you will do it today because you are running late", 0, "No. Your schedule is not her problem to absorb, and this is the restorative approach in reverse."]]}},

 {"name": "Communication", "sops": "Legislated · AODA",
  "lede": "Most of accessible service is how you talk to someone. The rule underneath all of it: "
          "ask the person, do not assume.",
  "rules": [
   ["Talk to the person, not the companion", "If someone is with them — family, interpreter, support worker — keep speaking to your client. It is their care.", "AODA", 1],
   ["Ask how to help before helping", "“Would you like a hand with that, and how?” People know what works for them better than you do.", "AODA"],
   ["Plain words, normal voice", "Do not raise your voice at someone who is not hard of hearing, and do not use a sing-song tone with an adult. Speak plainly and give time to answer.", "AODA"],
   ["Hearing", "Face them, let them see your mouth, cut the background noise, and be ready to write it down.", "AODA"],
   ["Vision", "Say who you are when you arrive, say what you are about to do, and tell them when you are leaving the room — do not let them discover it.", "AODA", 1],
   ["Speech", "Give time. Do not finish sentences or pretend to understand. Ask them to repeat, or to write it, and confirm what you heard.", "AODA"],
   ["Cognitive and mental health", "One idea at a time. Simple words, no rush, and check understanding without talking down.", "AODA"],
  ],
  "scene": {"h": "Answering for her",
   "t": "You ask your client whether she would like her shower before or after breakfast. Her daughter, standing beside her, answers immediately: “After, she always has it after.”",
   "c": [["Go with the daughter's answer, she knows the routine", 0, "No. The daughter may be right about the routine, but the question was the client's to answer."],
         ["Thank the daughter and ask the client directly what she would like today", 1, "Right. Keep the conversation with your client. Family knowledge is useful; it does not replace the client's own voice."],
         ["Ask the daughter to leave the room", 0, "Unnecessary and undignified. Just redirect the question warmly."]]}},

 {"name": "Devices, animals and support people", "sops": "Legislated · AODA",
  "lede": "Three things the standard names specifically, and all three are likely in a home.",
  "rules": [
   ["Assistive devices belong to the person", "Walker, wheelchair, cane, hearing aid, magnifier, communication board. Never move one out of reach — a walker across the room is a person stranded.", "AODA", 1],
   ["Ask before you touch a wheelchair", "It is part of someone's personal space. Pushing without asking is the equivalent of picking someone up.", "AODA", 1],
   ["Service animals", "A service animal may stay with the person. Do not pet, feed or distract it — it is working. If you have an allergy or a fear, say so to your supervisor so it can be worked out; it is not a reason to refuse service.", "AODA"],
   ["Support persons", "Someone who comes to help with communication, mobility, personal care or medical needs. If the client wants them present, they stay.", "AODA"],
   ["Equipment you use", "Know how the lift, bed controls or shower chair in that home work before you need them. Fumbling with equipment in front of someone is undignified and unsafe.", "SOP 32"],
  ],
  "scene": {"h": "The walker by the door",
   "t": "You have tidied the living room and put the client's walker neatly by the front door so it is out of the way. She is in her armchair.",
   "c": [["Fine — the room looks better and she knows where it is", 0, "No. She cannot get to it without it. Out of the way means out of reach, and this is a fall waiting to happen."],
         ["Bring it back within her reach and leave it there", 1, "Right. An assistive device is only useful where the person can reach it. Tidiness never outranks access."],
         ["Leave it and tell her to call you when she wants it", 0, "No. That makes her dependent on you for something she can do herself, and she may well try to walk without it."]]}},

 {"name": "When something goes wrong", "sops": "Legislated · SOPs 5, 8, 49",
  "lede": "The standard also covers what happens when the service does not work: a disruption, a "
          "barrier, a complaint.",
  "rules": [
   ["Tell people about a disruption", "If something a client relies on is unavailable — a late visit, a lift out of service — say so, say why, say how long, and say what the alternative is.", "SOP 5"],
   ["Ask when someone is struggling", "If a client cannot access part of the care, ask what would work. The person with the barrier usually knows the way round it.", "AODA"],
   ["Feedback must be easy to give", "Clients can give feedback on their care in whatever way works for them — spoken, written, through family. Pass it to the office the same day.", "SOP 8"],
   ["A complaint is information", "Complaints are acknowledged and answered, not defended against. They go in the quality record (SOP 49).", "SOP 49"],
   ["Never charge someone for access", "A support person's presence, a service animal, a different way of communicating: these are not extras to be billed.", "AODA"],
  ],
  "scene": {"h": "Running late",
   "t": "Traffic means you will reach a client who is blind about forty minutes late. She has no way of knowing why you have not arrived.",
   "c": [["Arrive and apologise when you get there", 0, "Not good enough. Forty minutes of not knowing, with no way to check, is the disruption — not the lateness itself."],
         ["Call as soon as you know, say how late you will be and why, and check whether she needs anything in the meantime", 1, "Right. Tell people about a disruption as it happens, with the reason and an expected time, and ask what they need."],
         ["Ask the office to call her later if you are still delayed", 0, "Too slow. She needs to know now, and you are the one who knows."]]}},
]

QUIZQ = [
 {"s":0,"q":"Which four principles does the AODA customer service standard rest on?","o":["Speed, accuracy, politeness, value","Dignity, independence, integration, equal opportunity","Safety, privacy, consent, documentation","Respect, patience, kindness, honesty"],"a":1,"e":"Dignity, independence, integration and equal opportunity."},
 {"s":0,"q":"Your client can dress herself but it is slow and you are behind schedule. What does independence require?","o":["Do it for her to save time","Let her do it, stay nearby, and offer help if she wants it","Do half and let her finish","Tell her to be quicker"],"a":1,"e":"Independence means letting people do what they can, even when slower. Offer; do not assume."},
 {"s":0,"q":"Which of these counts as a disability under the AODA?","o":["Only physical disabilities","Only disabilities you can see","Physical, sensory, mental health, intellectual and learning disabilities, including invisible ones","Only permanent disabilities"],"a":2,"e":"The definition is broad and includes conditions that are invisible or that come and go."},
 {"s":1,"q":"A client's daughter answers a question you asked the client. What do you do?","o":["Accept the daughter's answer","Thank her and ask the client directly","Ask the daughter to leave","Write it down for later"],"a":1,"e":"Speak to the person whose care it is. Family knowledge helps but does not replace the client's own voice."},
 {"s":1,"q":"You are supporting a client who is blind. What should you always do?","o":["Speak louder","Say who you are when you arrive and tell her when you leave the room","Take her arm and guide her","Keep the room exactly as it is and say nothing"],"a":1,"e":"Announce yourself, say what you are about to do, and say when you leave — do not let her discover it."},
 {"s":1,"q":"A client's speech is difficult to understand. What is the right approach?","o":["Finish his sentences to save him effort","Nod along even when you have not understood","Give time, ask him to repeat or write it, and confirm what you heard","Ask a family member to speak for him"],"a":2,"e":"Give time, never pretend to understand, and check back what you heard."},
 {"s":2,"q":"Where should a client's walker be left?","o":["Tidied out of the way","Within the client's reach","By the front door","Wherever there is space"],"a":1,"e":"An assistive device is only useful where the person can reach it. Out of the way means stranded."},
 {"s":2,"q":"A client has a service animal. Which is correct?","o":["It must stay outside during personal care","It may stay with the person, and you do not pet, feed or distract it","You can ask for proof of certification","It is only allowed if the care plan says so"],"a":1,"e":"The animal stays with the person and is working. An allergy or fear is worked out with your supervisor, not by refusing service."},
 {"s":2,"q":"Before pushing a client's wheelchair, you should:","o":["Just go, it is quicker","Ask first — it is part of their personal space","Ask the family","Push slowly without asking"],"a":1,"e":"Ask. Moving someone's chair without asking is the equivalent of picking them up."},
 {"s":3,"q":"You will be forty minutes late to a client who is blind. When do you tell her?","o":["As soon as you know, with the reason and an expected time","When you arrive","Only if she calls","At the end of the visit"],"a":0,"e":"Tell people about a disruption as it happens: what, why, how long, and what the alternative is."},
 {"s":3,"q":"A client wants a support person present during her care. What is the rule?","o":["Only with the office's permission","Only if the support person has training","If the client wants them present, they stay","Only for medical appointments"],"a":2,"e":"A support person helps with communication, mobility, personal care or medical needs. If the client wants them there, they stay."},
 {"s":3,"q":"A client tells you she found part of her care difficult to access. What do you do?","o":["Note it for her annual review","Ask what would work for her, and pass the feedback to the office the same day","Tell her the care plan cannot change","Suggest she put it in writing"],"a":1,"e":"Ask — the person with the barrier usually knows the way round it — and pass feedback on the same day (SOPs 8, 49)."},
 {"s":3,"q":"Can a client be charged extra because a support person attends?","o":["Yes, it is an extra person","Only if they stay the whole visit","No — access is never an extra to be billed","Only for long visits"],"a":2,"e":"Support persons, service animals and alternative communication are access, not add-ons."},
]
