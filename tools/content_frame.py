"""Words for the Phnom Penh page that do not come from research/facts.json: titles, nav, toys, pictures. EN / KM / TH."""


def t(en, km, th):
    return {"en": en, "km": km, "th": th}


UI = {
    "title": t("Phnom Penh · Four Faces", "ភ្នំពេញ · ចតុមុខ", "พนมเปญ · จตุมุข"),
    "desc": t("Phnom Penh in one page: Lady Penh's hill, the four rivers, the palace, the years, legends, people, food, a map and what is on.",
              "ភ្នំពេញក្នុងមួយទំព័រ៖ ភ្នំដូនពេញ ទន្លេបួនមុខ ព្រះបរមរាជវាំង ប្រវត្តិ រឿងព្រេង បុគ្គល អាហារ ផែនទី និងព្រឹត្តិការណ៍ខាងមុខ។",
              "พนมเปญในหน้าเดียว เนินของยายเพ็ญ แม่น้ำสี่สาย พระราชวัง ประวัติ ตำนาน ผู้คน อาหาร แผนที่ และงานที่กำลังจะมา"),
    "card_line": t("Phnom Penh in one page: map, holidays, history, legends, people, sites, food and toys",
                   "ភ្នំពេញក្នុងមួយទំព័រ៖ ផែនទី ថ្ងៃបុណ្យ ប្រវត្តិ រឿងព្រេង បុគ្គល ទីកន្លែង អាហារ និងល្បែង",
                   "พนมเปญในหน้าเดียว แผนที่ วันหยุด ประวัติ ตำนาน ผู้คน สถานที่ อาหาร และของเล่น"),
    "card_alt": t("The four rivers meeting at Phnom Penh, drawn", "ទន្លេបួនមុខជួបគ្នានៅភ្នំពេញ គូរដោយដៃ", "แม่น้ำสี่สายบรรจบกันที่พนมเปญ วาดเล่น"),
    "home": t("Mot Dang", "មត់ដែង", "มดแดง"),
    "sections": t("Sections", "ផ្នែក", "หมวด"),
    "h1": t("Phnom Penh", "ភ្នំពេញ", "พนมเปญ"),
    "h1small": t("ភ្នំពេញ · Penh's hill, on the four faces", "Phnom Penh · ភ្នំរបស់ដូនពេញ លើចតុមុខ", "ភ្នំពេញ · เนินของยายเพ็ญ ริมจตุมุข"),
    "lede": t("Cambodia's capital, where the Mekong, the Tonlé Sap and the Bassac meet below a small hill a woman named Penh raised.",
              "រាជធានីនៃកម្ពុជា ជាកន្លែងដែលទន្លេមេគង្គ ទន្លេសាប និងទន្លេបាសាក់ជួបគ្នា នៅជើងភ្នំតូចមួយដែលស្ត្រីម្នាក់ឈ្មោះពេញបានលើក។",
              "เมืองหลวงของกัมพูชา ที่แม่น้ำโขง โตนเลสาบ และบาสัก มาบรรจบกันใต้เนินเล็ก ๆ ที่หญิงชื่อเพ็ญก่อขึ้น"),
    "map_t": t("Phnom Penh, doodled: a hand-drawn map", "ភ្នំពេញ គូរលេង៖ ផែនទីគូរដោយដៃ", "พนมเปญ วาดเล่น แผนที่วาดมือ"),
    "map_open": t("Open the map", "បើកផែនទី", "เปิดแผนที่"),
    "cal_h": t("What's on", "ព្រឹត្តិការណ៍ខាងមុខ", "งานที่จะมา"),
    "soon_h": t("Yearly, next date not out yet", "ប្រចាំឆ្នាំ មិនទាន់ប្រកាសកាលបរិច្ឆេទ", "จัดทุกปี ยังไม่ประกาศวัน"),
    "river_a": t("The four rivers at Chaktomuk. Tap the water to race a boat; tap the palace for fireworks.",
                 "ទន្លេបួនមុខនៅចតុមុខ។ ចុចលើទឹកដើម្បីប្រណាំងទូក ចុចលើវាំងដើម្បីបាញ់កាំជ្រួច។",
                 "แม่น้ำสี่สายที่จตุมุข แตะน้ำเพื่อแข่งเรือ แตะพระราชวังเพื่อจุดพลุ"),
    "river_k": t("Tap the water · tap the palace", "ចុចលើទឹក · ចុចលើវាំង", "แตะน้ำ · แตะพระราชวัง"),
    "river_h": t("Four faces", "ចតុមុខ", "จตุมุข"),
    "river_p": t("Chaktomuk, “four faces”: the Mekong, the Tonlé Sap and the Bassac meet in front of the Royal Palace.",
                 "ចតុមុខ៖ ទន្លេមេគង្គ ទន្លេសាប និងទន្លេបាសាក់ ជួបគ្នានៅមុខព្រះបរមរាជវាំង។",
                 "จตุมุข แปลว่า “สี่หน้า” แม่น้ำโขง โตนเลสาบ และบาสัก มาบรรจบกันหน้าพระบรมราชวัง"),
    "tldr_k": t("TL;DR", "សង្ខេប", "สั้น ๆ"),
    "tldr_h": t("Phnom Penh in a minute", "ភ្នំពេញក្នុងមួយនាទី", "พนมเปญในหนึ่งนาที"),
    "hist_k": t("History", "ប្រវត្តិ", "ประวัติ"),
    "hist_h": t("Hill, capital, protectorate, Year Zero, now", "ភ្នំ រាជធានី អាណាព្យាបាល ឆ្នាំសូន្យ សព្វថ្ងៃ", "เนิน เมืองหลวง อารักขา ปีศูนย์ วันนี้"),
    "leg_k": t("Legends", "រឿងព្រេង", "ตำนาน"),
    "leg_h": t("Stories of the hill and the river", "រឿងរ៉ាវនៃភ្នំ និងទន្លេ", "เรื่องเล่าของเนินและแม่น้ำ"),
    "ppl_k": t("Notable people", "បុគ្គលសំខាន់", "บุคคลสำคัญ"),
    "ppl_h": t("People of Phnom Penh", "អ្នកភ្នំពេញ", "คนพนมเปญ"),
    "ppl_d": t("Tap a face.", "ចុចលើមុខ។", "แตะที่หน้า"),
    "site_k": t("Historic sites", "ទីតាំងប្រវត្តិសាស្ត្រ", "โบราณสถานและที่สำคัญ"),
    "site_h": t("Palace, pagodas, markets, memorials", "វាំង វត្ត ផ្សារ អនុស្សាវរីយ៍", "วัง วัด ตลาด อนุสรณ์"),
    "cul_k": t("Culture", "វប្បធម៌", "วัฒนธรรม"),
    "cul_h": t("Dance, puppets, festivals, songs", "របាំ ស្បែក បុណ្យ ចម្រៀង", "ระบำ หนัง เทศกาล เพลง"),
    "food_k": t("Food", "អាហារ", "อาหาร"),
    "food_h": t("What to eat", "ញ៉ាំអ្វី", "กินอะไรดี"),
    "pic_k": t("Pictures", "រូបភាព", "ภาพ"),
    "pic_h": t("Phnom Penh in pictures", "ភ្នំពេញក្នុងរូបភាព", "พนมเปญในภาพ"),
    "pic_d": t("From Wikimedia Commons, with each photographer's name and licence. Tap to enlarge.",
               "ពីវិគីមេឌាខមម៉ុនស៍ ជាមួយឈ្មោះអ្នកថត និងអាជ្ញាប័ណ្ណ។ ចុចដើម្បីពង្រីក។",
               "จากวิกิมีเดียคอมมอนส์ พร้อมชื่อช่างภาพและสัญญาอนุญาต แตะเพื่อขยาย"),
    "src_k": t("Sources", "ប្រភព", "ที่มา"),
    "src_h": t("Read for this page", "ឯកសារសម្រាប់ទំព័រនេះ", "อ่านประกอบหน้านี้"),
    "src_d": t("Read on 13 October 2026.", "អានថ្ងៃទី១៣ ខែតុលា ឆ្នាំ២០២៦។", "อ่านเมื่อ 13 ตุลาคม 2569"),
    "dir": t("Psar Phnom Penh: places near and now", "ផ្សារភ្នំពេញ៖ ទីកន្លែងជិត និងឥឡូវ", "ตลาดพนมเปญ: ที่ใกล้และตอนนี้"),
    "all": t("All minisites", "គេហទំព័រតូចៗទាំងអស់", "มินิไซต์ทั้งหมด"),
    "source": t("source", "ប្រភព", "ที่มา"),
}

NAV = [("map", t("Map", "ផែនទី", "แผนที่")), ("calendar", t("What's on", "ព្រឹត្តិការណ៍", "งาน")), ("tldr", t("TL;DR", "សង្ខេប", "สั้น ๆ")),
       ("history", t("History", "ប្រវត្តិ", "ประวัติ")), ("legends", t("Legends", "រឿងព្រេង", "ตำนาน")), ("people", t("People", "បុគ្គល", "ผู้คน")),
       ("sites", t("Sites", "ទីកន្លែង", "สถานที่")), ("culture", t("Culture", "វប្បធម៌", "วัฒนธรรม")), ("food", t("Food", "អាហារ", "อาหาร")),
       ("pics", t("Pictures", "រូបភាព", "ภาพ"))]

TOYS = {
    "penh": {"id": "penh", "read": "penhread",
             "h": t("Lady Penh's hill", "ភ្នំដូនពេញ", "เนินของยายเพ็ญ"),
             "p": t("Tap the tree floating in the flood, then tap to carry earth for the hill.",
                    "ចុចលើដើមឈើអណ្តែតក្នុងទឹកជំនន់ រួចចុចដើម្បីលីដីលើកភ្នំ។",
                    "แตะต้นไม้ที่ลอยมากับน้ำหลาก แล้วแตะเพื่อขนดินก่อเนิน"),
             "buttons": [("penhreset", t("Start again", "ចាប់ផ្តើមម្តងទៀត", "เริ่มใหม่"))]},
    "hands": {"id": "hands", "read": "handread",
              "h": t("Royal Ballet hands", "ដៃរបាំព្រះរាជទ្រព្យ", "มือระบำหลวง"),
              "p": t("Tap to move to the next gesture.", "ចុចដើម្បីប្តូរទៅកាយវិការបន្ទាប់។", "แตะเพื่อเปลี่ยนท่ามือ")},
    "bowl": {"id": "bowl", "read": "bowlread",
             "h": t("Kuy teav, built", "គុយទាវ ធ្វើខ្លួនឯង", "ก๋วยเตี๋ยว ทำเอง"),
             "p": t("Tap the bowl to add the next thing. When it is full, tap to eat.",
                    "ចុចលើចានដើម្បីដាក់គ្រឿងបន្ទាប់។ ពេលពេញ ចុចដើម្បីញ៉ាំ។",
                    "แตะชามเพื่อใส่ของถัดไป เต็มแล้วแตะเพื่อกิน")},
}

TOYWORDS = {
    "tonlesap": t("Tonlé Sap", "ទន្លេសាប", "โตนเลสาบ"),
    "mekong": t("Mekong", "ទន្លេមេគង្គ", "แม่น้ำโขง"),
    "lower": t("Lower Mekong", "ទន្លេមេគង្គក្រោម", "แม่น้ำโขงตอนล่าง"),
    "bassac": t("Bassac", "ទន្លេបាសាក់", "แม่น้ำบาสัก"),
    "season_wet": t("Make it rainy season", "ប្តូរទៅរដូវវស្សា", "เปลี่ยนเป็นหน้าฝน"),
    "season_dry": t("Make it dry season", "ប្តូរទៅរដូវប្រាំង", "เปลี่ยนเป็นหน้าแล้ง"),
    "flow_wet": t("Rainy season: the Mekong rises and the Tonlé Sap runs backwards, up to the lake.",
                  "រដូវវស្សា៖ ទឹកទន្លេមេគង្គឡើង ទន្លេសាបហូរបញ្ច្រាស ឡើងទៅបឹងទន្លេសាប។",
                  "หน้าฝน แม่น้ำโขงขึ้น โตนเลสาบไหลย้อนขึ้นไปทะเลสาบ"),
    "flow_dry": t("Dry season: the lake drains, and the Tonlé Sap runs down into the Mekong.",
                  "រដូវប្រាំង៖ បឹងបង្ហូរទឹកចេញ ហើយទន្លេសាបហូរចុះមកទន្លេមេគង្គវិញ។",
                  "หน้าแล้ง ทะเลสาบระบายน้ำ โตนเลสาบไหลลงสู่แม่น้ำโขง"),
    "boat1": t("boat racing", "ទូកកំពុងប្រណាំង", "ลำกำลังแข่ง"),
    "boats": t("boats raced", "ទូកបានប្រណាំង", "ลำแข่งแล้ว"),
    "penh0": t("Tap the tree in the flood.", "ចុចលើដើមឈើក្នុងទឹកជំនន់។", "แตะต้นไม้กลางน้ำหลาก"),
    "penh1": t("Inside the hollow koki tree: four Buddha images and one of Vishnu. Tap to carry earth.",
               "ក្នុងប្រហោងដើមគគី៖ ព្រះពុទ្ធរូបបួនអង្គ និងរូបព្រះនារាយណ៍មួយ។ ចុចដើម្បីលីដី។",
               "ในโพรงต้นตะเคียน พระพุทธรูปสี่องค์และรูปพระนารายณ์หนึ่งองค์ แตะเพื่อขนดิน"),
    "penh2": t("baskets of earth", "ល្អីដី", "กระบุงดิน"),
    "penh3": t("The hill and its shrine: Wat Phnom. The town took its name from it: Phnom Penh, Penh's hill.",
               "ភ្នំ និងវត្តលើភ្នំ៖ វត្តភ្នំ។ ទីក្រុងយកឈ្មោះតាមនេះ៖ ភ្នំពេញ ភ្នំរបស់ដូនពេញ។",
               "เนินและศาลบนยอด คือวัดพนม เมืองได้ชื่อจากที่นี่ พนมเปญ เนินของยายเพ็ญ"),
    "bowl_done": t("Breakfast in Phnom Penh.", "អាហារពេលព្រឹកនៅភ្នំពេញ។", "อาหารเช้าที่พนมเปญ"),
    "bowl_eaten": t("bowls eaten", "ចានបានញ៉ាំ", "ชามแล้ว"),
    "cal_empty": t("Nothing dated in the next weeks yet.", "មិនទាន់មានព្រឹត្តិការណ៍ក្នុងសប្តាហ៍ខាងមុខ។", "ยังไม่มีงานที่ระบุวันในช่วงนี้"),
}

# Kuy teav Phnom Penh, in the order it goes into the bowl. Checked against research/facts.json food.
BOWL = [
    {"k": "noodles", **t("Rice noodles", "គុយទាវ (មីអង្ករ)", "เส้นก๋วยเตี๋ยว")},
    {"k": "broth", **t("Clear pork-bone broth", "ទឹកស៊ុបឆ្អឹងជ្រូក", "น้ำซุปกระดูกหมู")},
    {"k": "mince", **t("Minced pork", "សាច់ជ្រូកចិញ្ច្រាំ", "หมูสับ")},
    {"k": "pork", **t("Sliced pork", "សាច់ជ្រូកចិត", "หมูชิ้น")},
    {"k": "shrimp", **t("Shrimp", "បង្គា", "กุ้ง")},
    {"k": "garlic", **t("Fried garlic", "ខ្ទឹមសចៀន", "กระเทียมเจียว")},
    {"k": "onion", **t("Spring onion", "ស្លឹកខ្ទឹម", "ต้นหอม")},
    {"k": "sprouts", **t("Bean sprouts", "សណ្តែកបណ្តុះ", "ถั่วงอก")},
    {"k": "lime", **t("Lime", "ក្រូចឆ្មារ", "มะนาว")},
    {"k": "chili", **t("Chili", "ម្ទេស", "พริก")},
]

# Royal Ballet hand gestures: 4 fingers × 3 joints, thumb × 3, wrist. Names come from research/facts.json culture.
HANDS = []

SOON = [
    t("Khmer New Year: three days, New Year's Day on 13 or 14 April", "បុណ្យចូលឆ្នាំខ្មែរ៖ បីថ្ងៃ ថ្ងៃចូលឆ្នាំនៅថ្ងៃទី១៣ ឬ ១៤ មេសា", "ปีใหม่เขมร สามวัน วันขึ้นปีใหม่ 13 หรือ 14 เมษายน"),
    t("Pchum Ben: fifteen days, ending on the 15th of the tenth Khmer month, September or October", "ភ្ជុំបិណ្ឌ៖ ដប់ប្រាំថ្ងៃ បញ្ចប់នៅថ្ងៃ ១៥ ខែទី១០ តាមចន្ទគតិ ខែកញ្ញា ឬតុលា", "ประชุมบิณฑ์ สิบห้าวัน สิ้นสุดวันที่ 15 เดือนสิบเขมร ราวกันยายนหรือตุลาคม"),
    t("Bon Om Touk races: the 14th–15th waxing and 1st waning of Kadek. The holiday stays in 2026; the Phnom Penh celebrations are called off", "ប្រណាំងទូកបុណ្យអុំទូក៖ ១៤–១៥ កើត និង ១ រោច ខែកត្តិក។ ឆ្នាំ២០២៦ នៅតែជាថ្ងៃឈប់សម្រាក តែការប្រារព្ធនៅភ្នំពេញត្រូវបានលុបចោល", "แข่งเรือบุญอมตูก ขึ้น 14–15 ค่ำ และแรม 1 ค่ำ เดือนกัตติกะ ปี 2569 ยังเป็นวันหยุด แต่งานที่พนมเปญงดจัด"),
]

EXTRA_DATES = []

BANDS = {
    "history": {"pic": "independence", "cap": t("The Independence Monument, 1958", "វិមានឯករាជ្យ ឆ្នាំ១៩៥៨", "อนุสาวรีย์เอกราช พ.ศ. 2501")},
    "legends": {"pic": "wat-phnom", "cap": t("Wat Phnom, on Penh's hill", "វត្តភ្នំ លើភ្នំដូនពេញ", "วัดพนม บนเนินของยายเพ็ญ")},
    "sites": {"pic": "royal-palace", "cap": t("The Throne Hall of the Royal Palace", "ព្រះទីនាំងទេវាវិនិច្ឆ័យ ក្នុងព្រះបរមរាជវាំង", "พระที่นั่งในพระบรมราชวัง")},
    "culture": {"pic": "water-festival-boats", "cap": t("Racing boats at the Water Festival", "ទូកងក្នុងបុណ្យអុំទូក", "เรือแข่งในบุญอมตูก")},
}

PICS = [
    {"pic": "chaktomuk", "cap": t("Phnom Penh from Chaktomuk", "ភ្នំពេញពីចតុមុខ", "พนมเปญจากจตุมุข")},
    {"pic": "hero-dawn", "cap": t("Sunrise on the Tonlé Sap", "ថ្ងៃរះលើទន្លេសាប", "พระอาทิตย์ขึ้นเหนือโตนเลสาบ")},
    {"pic": "silver-pagoda", "cap": t("The Silver Pagoda", "វត្តព្រះកែវមរកត", "วัดพระแก้วมรกต (เจดีย์เงิน)")},
    {"pic": "wat-phnom-gold", "cap": t("Wat Phnom", "វត្តភ្នំ", "วัดพนม")},
    {"pic": "wat-ounalom", "cap": t("Wat Ounalom", "វត្តឧណ្ណាលោម", "วัดอุณาโลม")},
    {"pic": "wat-langka", "cap": t("Wat Langka", "វត្តលង្កា", "วัดลังกา")},
    {"pic": "wat-botum", "cap": t("Wat Botum", "វត្តបទុមវតី", "วัดปทุมวดี")},
    {"pic": "national-museum", "cap": t("The National Museum", "សារមន្ទីរជាតិ", "พิพิธภัณฑ์แห่งชาติ")},
    {"pic": "central-market", "cap": t("Phsar Thmei, the Central Market", "ផ្សារធំថ្មី", "ตลาดกลาง (ผสารธมทเมย)")},
    {"pic": "russian-market", "cap": t("Phsar Toul Tom Poung, the Russian Market", "ផ្សារទួលទំពូង", "ตลาดรัสเซีย (ผสารตวลทุมปูง)")},
    {"pic": "olympic", "cap": t("The National Olympic Stadium, 1964", "ពហុកីឡដ្ឋានជាតិអូឡាំពិក ឆ្នាំ១៩៦៤", "สนามกีฬาโอลิมปิกแห่งชาติ พ.ศ. 2507")},
    {"pic": "post-office", "cap": t("The Central Post Office", "ប្រៃសណីយ៍កណ្តាល", "ที่ทำการไปรษณีย์กลาง")},
    {"pic": "railway", "cap": t("Phnom Penh railway station", "ស្ថានីយរថភ្លើងភ្នំពេញ", "สถานีรถไฟพนมเปญ")},
    {"pic": "sihanouk-memorial", "cap": t("Statue of King Father Norodom Sihanouk", "ព្រះរូបសំណាក ព្រះបរមរតនកោដ្ឋ នរោត្តម សីហនុ", "อนุสาวรีย์พระบิดา นโรดม สีหนุ")},
    {"pic": "apsara", "cap": t("A dance show in Phnom Penh", "ការសម្តែងរបាំនៅភ្នំពេញ", "การแสดงระบำที่พนมเปญ")},
    {"pic": "monks", "cap": t("Monks on a Phnom Penh street", "ព្រះសង្ឃលើផ្លូវក្នុងភ្នំពេញ", "พระสงฆ์บนถนนในพนมเปญ")},
    {"pic": "tuk-tuk-night", "cap": t("A tuk-tuk at night", "រ៉ឺម៉កពេលយប់", "ตุ๊กตุ๊กยามค่ำ")},
    {"pic": "night-market", "cap": t("The Night Market by the river", "ផ្សាររាត្រីមាត់ទន្លេ", "ตลาดกลางคืนริมแม่น้ำ")},
    {"pic": "amok", "cap": t("Fish amok", "អាម៉ុកត្រី", "ห่อหมกปลาเขมร (อาม็อก)")},
    {"pic": "fruit", "cap": t("Fruit at the Central Market", "ផ្លែឈើនៅផ្សារធំថ្មី", "ผลไม้ในตลาดกลาง")},
    {"pic": "koh-pich", "cap": t("Koh Pich and downtown from a drone", "កោះពេជ្រ និងកណ្តាលក្រុង មើលពីលើ", "เกาะเพชรและใจกลางเมืองจากโดรน")},
    {"pic": "skyline", "cap": t("The palace and the skyline", "វាំង និងទេសភាពទីក្រុង", "พระราชวังกับเส้นขอบฟ้า")},
    {"pic": "sunset-river", "cap": t("Sunset at Boeung Kak", "ថ្ងៃលិចនៅបឹងកក់", "พระอาทิตย์ตกที่บึงกัก")},
    {"pic": "hero-dusk", "cap": t("The naga fountain garden at dusk", "សួនច្បារទឹកក្បាលនាគពេលព្រលប់", "สวนน้ำพุนาคยามเย็น")},
]

WORDS = ["phnom penh", "cambodia", "chaktomuk", "tonle sap", "mekong", "bassac", "wat phnom", "daun penh", "royal palace", "silver pagoda",
         "central market", "russian market", "independence monument", "tuol sleng", "choeung ek", "water festival", "bon om touk",
         "royal ballet", "kuy teav", "amok", "ភ្នំពេញ", "ចតុមុខ", "វត្តភ្នំ", "ដូនពេញ", "พนมเปญ", "จตุมุข", "วัดพนม", "ยายเพ็ญ", "กัมพูชา"]
