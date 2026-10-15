# WHMIS 2015 — Atria Private Care
SLUG = "whmis"
TITLE = "WHMIS"
SUBTITLE = ("The hazardous products you actually meet in a client's home — "
            "disinfectants, oxygen, sharps waste — and how to read what is on the label.")
COVERS = "WHMIS 2015 · legislated"
TIME = "About 25 minutes"
VERSION = "2026.1"
PASS_MARK = 11
GLYPH = '<path d="M16 8l8 14H8z"/><path d="M16 14v3"/><path d="M16 19.5v.5"/>'
COLOUR = dict(light="#46617E", mid="#5E7B99", ink="#3A5068",
              dark="#9FBAD4", darkbg="#2F4256")
INTRO = ("WHMIS training is required by law and must cover the products you actually use. "
         "Work through five short sections, then take the check.")
TOC_NOTE = ("This covers WHMIS generally and the products Atria staff meet in homes. Your "
            "supervisor goes through the specific products at your sites during orientation.")

SECTIONS = [
 {"name": "What WHMIS is for", "sops": "Legislated · OHSA",
  "lede": "WHMIS is the system that tells you what is in a container and what it can do to you. "
          "In home care the hazards are ordinary-looking: a spray bottle under a sink, an oxygen "
          "cylinder beside a bed, a sharps container in a bag.",
  "rules": [
   ["You have a right to know", "Your employer must tell you about every hazardous product you may be exposed to at work, and train you on it. That is the law, not a courtesy.", "OHSA"],
   ["Three parts", "WHMIS is labels, safety data sheets, and training. A product is not ready to use until all three are in place.", "WHMIS 2015"],
   ["It follows the product, not the building", "A bottle you carry from your car into a client's home is still a workplace product. The same rules apply there as in an office.", "WHMIS 2015"],
   ["Household products are the grey area", "A consumer product bought at a supermarket may carry a household label instead of a WHMIS one. If you are using it as part of your job, and more often than a householder would, tell your supervisor so it can be assessed.", "WHMIS 2015"],
  ],
  "scene": {"h": "A bottle with no label",
   "t": "Under the client's sink you find a spray bottle of clear liquid with the label torn off. The family thinks it is a disinfectant. You need something to wipe a commode.",
   "c": [["Use it — it is almost certainly the disinfectant", 0, "No. An unlabelled container is an unknown product. It could be anything, including something that makes a toxic gas if mixed."],
         ["Do not use it. Tell your supervisor, and use a product you can identify", 1, "Right. No label means no identification, no hazard information and no safe handling instructions. Set it aside and report it."],
         ["Smell it to work out what it is", 0, "Never. Identifying a chemical by smell is how people get hurt, and some vapours damage you at the first breath."]]}},

 {"name": "Reading a supplier label", "sops": "Legislated · WHMIS 2015",
  "lede": "A supplier label has six things on it. Once you know what to look for, you can read any "
          "product in seconds.",
  "rules": [
   ["Product identifier", "The name of the product, matching the name on its safety data sheet.", "Label"],
   ["Pictogram", "A red diamond with a black symbol. It tells you the kind of harm at a glance.", "Label"],
   ["Signal word", "<strong>Danger</strong> is the more severe hazard; <strong>Warning</strong> is the less severe. There is no third level.", "Label"],
   ["Hazard statement", "What the product does: “causes severe skin burns and eye damage”.", "Label"],
   ["Precautionary statements", "What to do about it: how to handle it, what to wear, what to do for a splash, how to store and dispose of it.", "Label"],
   ["Supplier identifier", "Who made or imported it, so the product can be traced.", "Label"],
   ["A workplace label is different", "If you pour a product into another container, that container needs a workplace label: the product name, how to handle it safely, and a reference to the safety data sheet. A felt pen on tape is acceptable; nothing is not.", "WHMIS 2015", 1],
  ],
  "scene": {"h": "Danger or Warning",
   "t": "Two disinfectants are in the cupboard. One says Danger, the other says Warning. The client has asked you to clean the bathroom.",
   "c": [["Danger means use it only in emergencies", 0, "No. The signal word describes how severe the hazard is, not when to use the product."],
         ["Danger is the more severe hazard, so handle it with more care and the protection the label names", 1, "Right. Both are usable; Danger simply tells you the consequences of getting it wrong are worse. Read the precautionary statements on either one."],
         ["They mean the same thing", 0, "No. Danger is the more severe of the two, and the label will name stronger precautions to match."]]}},

 {"name": "The nine pictograms", "sops": "Legislated · WHMIS 2015",
  "lede": "Each red diamond stands for a family of hazards. You do not need to memorise every class — "
          "you need to recognise the symbol and go and read the label.",
  "rules": [
   ["Flame", "Catches fire easily. Alcohol-based hand rub and some aerosols are in this group. Keep away from heat and open flame, including a client who smokes.", "Pictogram"],
   ["Flame over circle", "Oxidiser — it makes a fire burn harder. <strong>Oxygen cylinders are the one you will meet most</strong>: no smoking, no open flame, no petroleum jelly near the cannula.", "Pictogram", 1],
   ["Corrosion", "Burns skin and eyes, or eats metal. Strong drain and oven cleaners, and some concentrated disinfectants.", "Pictogram"],
   ["Exclamation mark", "Irritates skin, eyes or airways, or is harmful if swallowed. Most ordinary cleaning products sit here.", "Pictogram"],
   ["Health hazard", "Serious longer-term harm: cancer, organ damage, reproductive harm, or asthma caused by the product.", "Pictogram"],
   ["Skull and crossbones", "Acutely toxic — a small amount can kill or seriously harm quickly.", "Pictogram", 1],
   ["Gas cylinder", "Gas under pressure. Oxygen again. A damaged cylinder can become a projectile.", "Pictogram"],
   ["Biohazardous infectious material", "Material containing organisms that cause disease. Relevant when you handle sharps and soiled waste.", "Pictogram"],
   ["Environment", "Harmful to aquatic life. Optional in Canada, so you may or may not see it.", "Pictogram"],
  ],
  "scene": {"h": "Oxygen in the bedroom",
   "t": "Your client uses oxygen through a nasal cannula. Her son steps into the bedroom with a lit cigarette and says he will keep it by the window.",
   "c": [["Ask him to smoke outside, away from the oxygen, and explain why", 1, "Right. Oxygen is an oxidiser: it makes anything that catches fire burn far faster. No smoking and no open flame anywhere near it."],
         ["It is fine if he stays by the window", 0, "No. Oxygen enriches the whole room and soaks into bedding and clothing. Distance within the room is not protection."],
         ["Turn the oxygen off while he smokes", 0, "No. Never interrupt prescribed oxygen. The cigarette leaves, not the therapy."]]}},

 {"name": "Safety data sheets", "sops": "Legislated · WHMIS 2015",
  "lede": "The safety data sheet is the long version of the label. It has 16 sections, always in the "
          "same order, so you can find what you need without reading the whole thing.",
  "rules": [
   ["Where to find them", "Atria keeps a data sheet for every hazardous product staff are asked to use. Ask the office if you cannot find one, and do not use a product with no sheet available.", "WHMIS 2015"],
   ["Section 4, first aid", "The one to go to in an emergency: what to do for skin, eyes, breathing and swallowing. Learn where it is before you need it.", "SDS", 1],
   ["Section 8, protection", "What gloves, eye protection or ventilation the product needs.", "SDS"],
   ["Section 2, hazards", "The pictograms, signal word and hazard statements, in full.", "SDS"],
   ["Section 7, handling and storage", "How to store it so it stays safe, and what it must not be stored beside.", "SDS"],
   ["Never mix products", "Bleach with ammonia or with an acid cleaner makes a toxic gas in seconds, in a small bathroom, with you in it. One product at a time, rinsed between.", "SDS", 1],
  ],
  "scene": {"h": "Splash in the eye",
   "t": "Cleaning a bathroom, a squirt of disinfectant goes into your eye. It stings badly.",
   "c": [["Rinse with water for the time the data sheet says, then get medical advice", 1, "Right. Section 4 of the data sheet gives the first aid, usually a long rinse — 15 minutes or more. Tell your supervisor and report it as an incident."],
         ["Rub it and carry on if it settles", 0, "No. Rubbing grinds the chemical in. Rinse first, for as long as the sheet says, and report it."],
         ["Wait to see whether it gets worse", 0, "No. With a corrosive product the damage happens in the first minutes. Rinse immediately."]]}},

 {"name": "In the client's home", "sops": "Legislated · SOPs 13, 16, 17",
  "lede": "Most of what you handle is ordinary. The risk comes from doing it in someone else's house, "
          "in a small room, often alone.",
  "rules": [
   ["Use the product the care plan or the office names", "Do not substitute something from under the client's sink because it is closer, and do not bring your own.", "SOP 17"],
   ["Ventilate", "Open a window or door when you use a disinfectant. Bathrooms are small, warm and unventilated — the worst case for vapour.", "SOP 17"],
   ["Wear what the label says", "Usually gloves. Sometimes eye protection. The label is the instruction, not a suggestion.", "SOP 13"],
   ["Sharps go in the sharps container, never in household waste", "A needle in a bin bag injures whoever lifts it. Never recap, and report any needlestick within 2 hours.", "SOP 16", 1],
   ["Store out of reach", "Clients with dementia may drink or misuse a cleaning product. Put it back where it belongs, closed, before you move on.", "SOP 29", 1],
   ["Report a spill or exposure", "Tell your supervisor the same shift and complete an incident report, even if you feel fine.", "SOP 47"],
  ],
  "scene": {"h": "Running low",
   "t": "You are nearly out of the disinfectant the office supplies. The client has a large bottle of a different brand under the sink and tells you to use that instead.",
   "c": [["Use the client's product — it is their home", 0, "No. You can only use a product you have been trained on and that Atria has a data sheet for. Their home does not change your training."],
         ["Use it, but only on surfaces", 0, "No. The issue is not where you use it, it is that it has not been assessed and you have not been trained on it."],
         ["Finish with what you have, tell the office you need more, and note the client's product so it can be assessed", 1, "Right. Thank the client, use what you are trained on, and get the supply sorted through the office."]]}},
]

QUIZQ = [
 {"s":0,"q":"What are the three parts of WHMIS?","o":["Labels, safety data sheets and training","Gloves, goggles and masks","Inspection, reporting and discipline","Storage, handling and disposal"],"a":0,"e":"Labels, safety data sheets and worker training. All three must be in place before a product is used."},
 {"s":0,"q":"You find a spray bottle in a client's home with no label. What do you do?","o":["Use it if you are fairly sure what it is","Smell it to identify it","Do not use it; tell your supervisor and use a product you can identify","Pour it away"],"a":2,"e":"An unlabelled container is an unknown product. Never identify a chemical by smell."},
 {"s":1,"q":"Which signal word means the more severe hazard?","o":["Caution","Warning","Danger","Notice"],"a":2,"e":"WHMIS 2015 uses only two signal words. Danger is the more severe; Warning is the less severe."},
 {"s":1,"q":"You pour disinfectant from a large jug into a smaller spray bottle to carry between homes. What does that bottle need?","o":["Nothing, it is the same product","A workplace label: product name, safe handling, and a reference to the data sheet","A copy of the full safety data sheet taped to it","Only the date"],"a":1,"e":"A product decanted into another container needs a workplace label. Handwritten is fine; nothing is not."},
 {"s":1,"q":"Which of these is NOT required on a supplier label?","o":["Pictogram","Signal word","The price of the product","Supplier identifier"],"a":2,"e":"The six required elements are product identifier, pictogram, signal word, hazard statements, precautionary statements and supplier identifier."},
 {"s":2,"q":"Which pictogram appears on an oxygen cylinder, and what does it mean?","o":["Flame — it catches fire","Flame over circle — it makes other things burn harder","Skull and crossbones — it is toxic","Environment — it harms aquatic life"],"a":1,"e":"Oxygen is an oxidiser. It does not burn itself; it makes everything else burn far faster. It also carries the gas cylinder pictogram."},
 {"s":2,"q":"A client on home oxygen has a visitor who wants to smoke by the open window in the same room. What is the right answer?","o":["Fine, as long as the window is open","Fine, if you turn the oxygen off first","Ask them to smoke outside, away from the oxygen","Fine, if they stand more than two metres away"],"a":2,"e":"Oxygen enriches the whole room and soaks into fabric. No smoking or open flame near it, and never interrupt prescribed oxygen."},
 {"s":2,"q":"What does the skull and crossbones pictogram mean?","o":["Irritates skin and eyes","Acutely toxic — a small amount can kill or seriously harm quickly","Causes long-term organ damage","Gas under pressure"],"a":1,"e":"Skull and crossbones is acute toxicity. The health hazard pictogram covers the longer-term harms."},
 {"s":3,"q":"Which section of a safety data sheet gives first aid?","o":["Section 2","Section 4","Section 8","Section 16"],"a":1,"e":"Section 4 is first aid. Section 2 is hazards, section 8 is protection. Find section 4 before you need it."},
 {"s":3,"q":"A colleague suggests mixing bleach with another cleaner to get through a stubborn bathroom. What do you say?","o":["Only in a well-ventilated room","Never mix products — it can make a toxic gas in seconds","Only if you wear gloves","Only a small amount"],"a":1,"e":"Bleach with ammonia or with an acid cleaner produces a toxic gas almost immediately, in a small room, with you in it."},
 {"s":3,"q":"The office asks you to use a product you have not seen before and there is no data sheet available. What do you do?","o":["Use it carefully","Use it with gloves","Do not use it until the data sheet and training are in place","Use it and read the sheet later"],"a":2,"e":"No data sheet, no use. The sheet and the training are part of what makes the product safe to use."},
 {"s":4,"q":"You are disinfecting a small bathroom with no window open. What is the first thing to change?","o":["Work faster","Open the door or window to ventilate","Use more product so it works sooner","Hold your breath"],"a":1,"e":"Bathrooms are the worst case for vapour: small, warm and unventilated. Ventilate before you start."},
 {"s":4,"q":"A used lancet needs disposing of in a client's home. Where does it go?","o":["Wrapped in tissue in the household bin","Recapped and into the household bin","The sharps container","Flushed"],"a":2,"e":"Sharps go in the sharps container, never in household waste, and are never recapped. A needlestick is reported and assessed within 2 hours (SOP 16)."},
 {"s":4,"q":"You spill a cleaning product on your forearm. It stings but you feel fine after rinsing. What do you do?","o":["Nothing, it is minor","Tell your supervisor the same shift and complete an incident report","Mention it at your next supervision","Only report it if a mark appears"],"a":1,"e":"Report exposures the same shift, even when you feel fine. Some effects are delayed (SOP 47)."},
 {"s":4,"q":"Your client has dementia and you have finished cleaning. What do you do with the product?","o":["Leave it out so it is ready for next time","Put it back closed and out of reach before you move on","Leave it in the bathroom","Take it home"],"a":1,"e":"Clients with dementia may drink or misuse a cleaning product. Closed and out of reach, every time."},
]
