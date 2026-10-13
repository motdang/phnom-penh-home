"""Phnom Penh page words, EN / KM / TH. Facts from research/facts.json (each with its source, read 2026-10-13); the frame is in content_frame.py."""
from content_frame import BANDS, BOWL, EXTRA_DATES, NAV, PICS, SOON, TOYS, TOYWORDS, UI, WORDS, t  # noqa: F401

ENW = "https://en.wikipedia.org/wiki/"
PP = ENW + "Phnom_Penh"
TS = ENW + "Tonl%C3%A9_Sap"
NIS = "https://www.nis.gov.kh/nis/Census2019/Final%20General%20Population%20Census%202019-English.pdf"
NIS_N = "National Institute of Statistics: 2019 census, final results"
UNESCO = "https://ich.unesco.org/en/"
KD = str.maketrans("0123456789", "០១២៣៤៥៦៧៨៩")


def km(s):
    return s.translate(KD)


def Y(ce, be=None):
    """A year in each calendar: CE in English, Khmer digits in Khmer, Buddhist Era in Thai."""
    return {"en": ce, "km": km(ce), "th": be or ce}


TLDR = [
    t("<b>Where:</b> Cambodia's capital, on the Chaktomuk, where the Mekong, the Tonlé Sap and the Bassac meet. 2.28 million people in the 2019 census, in 14 khans.",
      "<b>ទីតាំង៖</b> រាជធានីនៃកម្ពុជា នៅចតុមុខ ជាកន្លែងទន្លេមេគង្គ ទន្លេសាប និងទន្លេបាសាក់ជួបគ្នា។ ប្រជាជន ២,២៨ លាននាក់ តាមជំរឿនឆ្នាំ២០១៩ ក្នុង ១៤ ខណ្ឌ។",
      "<b>อยู่ไหน:</b> เมืองหลวงของกัมพูชา ริมจตุมุขที่แม่น้ำโขง โตนเลสาบ และบาสักบรรจบกัน ประชากร 2.28 ล้านคนตามสำมะโน 2562 แบ่งเป็น 14 เขต"),
    t("<b>The name:</b> “Penh's hill”. Tradition says that in 1372 a woman named Penh pulled a floating koki tree from the river, found Buddha images inside, and raised a hill for them. The hill is Wat Phnom.",
      "<b>ឈ្មោះ៖</b> “ភ្នំរបស់ដូនពេញ”។ តាមដំណាលថា នៅឆ្នាំ១៣៧២ ស្ត្រីម្នាក់ឈ្មោះពេញ បានទាញដើមគគីអណ្តែតទឹកឡើងពីទន្លេ ឃើញព្រះពុទ្ធរូបនៅខាងក្នុង ហើយលើកភ្នំដើម្បីតម្កល់។ ភ្នំនោះគឺវត្តភ្នំ។",
      "<b>ชื่อ:</b> “เนินของยายเพ็ญ” ตำนานว่า พ.ศ. 1915 (ค.ศ. 1372) หญิงชื่อเพ็ญดึงต้นตะเคียนที่ลอยน้ำขึ้นฝั่ง พบพระพุทธรูปข้างใน จึงก่อเนินประดิษฐาน เนินนั้นคือวัดพนม"),
    t("<b>Capital twice:</b> King Ponhea Yat moved the court here from Angkor in the 1430s. King Norodom brought it back in the 1860s and built the Royal Palace, under a French protectorate that lasted until 1953.",
      "<b>រាជធានីពីរដង៖</b> ព្រះបាទពញាយ៉ាតបានផ្លាស់រាជធានីពីអង្គរមកទីនេះ ក្នុងទសវត្សរ៍ឆ្នាំ១៤៣០។ ព្រះបាទនរោត្តមបាននាំរាជធានីត្រឡប់មកវិញ ក្នុងទសវត្សរ៍ឆ្នាំ១៨៦០ ហើយសាងសង់ព្រះបរមរាជវាំង ក្រោមអាណាព្យាបាលបារាំង រហូតដល់ឆ្នាំ១៩៥៣។",
      "<b>เป็นเมืองหลวงสองครั้ง:</b> พญายาตย้ายราชสำนักจากนครวัดมาที่นี่ราว พ.ศ. 1977 พระนโรดมนำเมืองหลวงกลับมาราว พ.ศ. 2409 และสร้างพระบรมราชวัง ใต้อารักขาฝรั่งเศสจนถึง พ.ศ. 2496"),
    t("<b>1975–1979:</b> the Khmer Rouge emptied the city on 17 April 1975. Tuol Sleng, the S-21 prison, and the killing field at Choeung Ek are memorials now.",
      "<b>១៩៧៥–១៩៧៩៖</b> ខ្មែរក្រហមបានជម្លៀសប្រជាជនចេញពីទីក្រុង នៅថ្ងៃទី១៧ មេសា ១៩៧៥។ ទួលស្លែង (គុក ស-២១) និងវាលពិឃាតជើងឯក ឥឡូវជាទីរំលឹក។",
      "<b>2518–2522:</b> เขมรแดงกวาดต้อนผู้คนออกจากเมืองเมื่อ 17 เมษายน 2518 วันนี้คุกตวลสแลง (S-21) และทุ่งสังหารเจิงเอกเป็นอนุสรณ์สถาน"),
    t("<b>Built:</b> the Central Market's 26-metre dome (1937), then Vann Molyvann's Independence Monument (1958), Chaktomuk Conference Hall (1961) and Olympic Stadium (1964).",
      "<b>សំណង់៖</b> លំហដំបូលផ្សារធំថ្មី កម្ពស់ ២៦ ម៉ែត្រ (១៩៣៧) បន្ទាប់មកស្នាដៃរបស់លោក វណ្ណ មូលីវណ្ណ៖ វិមានឯករាជ្យ (១៩៥៨) សាលសន្និសីទចតុមុខ (១៩៦១) និងពហុកីឡដ្ឋានជាតិអូឡាំពិក (១៩៦៤)។",
      "<b>สิ่งก่อสร้าง:</b> โดมสูง 26 เมตรของตลาดกลาง (2480) แล้วงานของวัณณ์ โมลีวัณณ์ อนุสาวรีย์เอกราช (2501) หอประชุมจตุมุข (2504) และสนามกีฬาโอลิมปิก (2507)"),
    t("<b>The river turns:</b> for about half the year the Tonlé Sap runs up to its lake, then back down. Bon Om Touk marks the turn with boat races in front of the palace.",
      "<b>ទន្លេបង្វិល៖</b> ប្រហែលកន្លះឆ្នាំ ទន្លេសាបហូរឡើងទៅបឹង រួចហូរចុះវិញ។ បុណ្យអុំទូកអបអរការប្តូរនេះ ដោយប្រណាំងទូកនៅមុខព្រះបរមរាជវាំង។",
      "<b>แม่น้ำไหลกลับ:</b> ราวครึ่งปีโตนเลสาบไหลขึ้นไปทะเลสาบ แล้วไหลกลับลงมา บุญอมตูกฉลองการเปลี่ยนนี้ด้วยการแข่งเรือหน้าพระราชวัง"),
    t("<b>Eat:</b> kuy teav for breakfast, bai sach chrouk, fish amok, num pang from the corner cart.",
      "<b>ញ៉ាំ៖</b> គុយទាវពេលព្រឹក បាយសាច់ជ្រូក អាម៉ុកត្រី នំបុ័ងពីរទេះកែងផ្លូវ។",
      "<b>กิน:</b> ก๋วยเตี๋ยวตอนเช้า ข้าวหมูย่าง (บายซัจจรูก) อาม็อกปลา ขนมปังนมปังจากรถเข็นหัวมุม"),
]

NUMBERS = [
    {"v": "2,281,951", "l": t("people, 2019 census", "នាក់ ជំរឿនឆ្នាំ២០១៩", "คน สำมะโน 2562"), "src": NIS, "src_name": NIS_N},
    {"v": "679 km²", "l": t("area", "ផ្ទៃដី", "พื้นที่"), "src": NIS, "src_name": NIS_N},
    {"v": "14 · 105", "l": t("khans · sangkats", "ខណ្ឌ · សង្កាត់", "เขต · แขวง"), "src": NIS, "src_name": NIS_N},
    {"v": "1372", "l": t("Lady Penh's hill, in tradition", "ភ្នំដូនពេញ តាមដំណាល", "เนินยายเพ็ญ ตามตำนาน"), "src": PP, "src_name": "Wikipedia: Phnom Penh"},
    {"v": "115 km", "l": t("the Tonlé Sap river, both ways", "ទន្លេសាប ហូរទាំងពីរទិស", "โตนเลสาบ ไหลได้สองทาง"), "src": TS, "src_name": "Wikipedia: Tonlé Sap"},
    {"v": "26 m", "l": t("Central Market dome, 1937", "លំហផ្សារធំថ្មី ១៩៣៧", "โดมตลาดกลาง 2480"), "src": ENW + "Central_Market,_Phnom_Penh", "src_name": "Wikipedia: Central Market, Phnom Penh"},
    {"v": "37 m", "l": t("Independence Monument, 1958", "វិមានឯករាជ្យ ១៩៥៨", "อนุสาวรีย์เอกราช 2501"), "src": ENW + "Independence_Monument,_Phnom_Penh", "src_name": "Wikipedia: Independence Monument"},
    {"v": "15,000–20,000", "l": t("people held at S-21, 1975–79", "នាក់ត្រូវឃុំនៅ ស-២១", "คนถูกคุมขังที่ S-21"), "src": "https://tuolsleng.gov.kh/en/museum/building/", "src_name": "Tuol Sleng Genocide Museum"},
]

TIMELINE = [
    {"y": Y("1372", "1915"), "text": t("In tradition, Penh finds a floating koki tree holding four Buddha images and one of Vishnu, and has a hill raised for them. The legend was first written down about a century later.",
                                         "តាមដំណាល ដូនពេញរកឃើញដើមគគីអណ្តែតទឹក មានព្រះពុទ្ធរូបបួនអង្គ និងរូបព្រះនារាយណ៍មួយ ហើយឲ្យគេលើកភ្នំតម្កល់។ រឿងនេះត្រូវបានកត់ត្រាប្រហែលមួយសតវត្សក្រោយមក។",
                                         "ตามตำนาน ยายเพ็ญพบต้นตะเคียนลอยน้ำ ข้างในมีพระพุทธรูปสี่องค์และรูปพระนารายณ์หนึ่งองค์ จึงให้ก่อเนินประดิษฐาน ตำนานนี้บันทึกไว้ราวร้อยปีต่อมา"),
     "src": ENW + "Wat_Phnom", "src_name": "Wikipedia: Wat Phnom"},
    {"y": Y("1434", "1977"), "text": t("King Ponhea Yat leaves Angkor and settles at Chaktomuk. Sources give dates from 1397 to 1434.",
                                         "ព្រះបាទពញាយ៉ាតចាកចេញពីអង្គរ មកតាំងនៅចតុមុខ។ ប្រភពផ្សេងៗផ្តល់កាលបរិច្ឆេទពីឆ្នាំ១៣៩៧ ដល់ ១៤៣៤។",
                                         "พญายาตออกจากนครวัดมาตั้งที่จตุมุข แหล่งต่าง ๆ ให้ปีตั้งแต่ 1940 ถึง 1977"),
     "src": PP, "src_name": "Wikipedia: Phnom Penh"},
    {"y": Y("1529", "2072"), "text": t("King Ang Chan I moves the capital to Longvek; Oudong follows from 1618 until 1866.",
                                         "ព្រះបាទអង្គចន្ទទី១ ផ្លាស់រាជធានីទៅលង្វែក បន្ទាប់មកឧដុង្គ ពីឆ្នាំ១៦១៨ ដល់ ១៨៦៦។",
                                         "พระองค์จันท์ที่ 1 ย้ายเมืองหลวงไปละแวก ต่อมาเป็นอุดงตั้งแต่ 2161 ถึง 2409"),
     "src": ENW + "Lovek", "src_name": "Wikipedia: Lovek"},
    {"y": Y("1863", "2406"), "text": t("King Norodom signs the treaty that puts Cambodia under a French protectorate, on 11 August.",
                                         "ព្រះបាទនរោត្តមចុះហត្ថលេខាលើសន្ធិសញ្ញាដាក់កម្ពុជាក្រោមអាណាព្យាបាលបារាំង នៅថ្ងៃទី១១ សីហា។",
                                         "พระนโรดมลงนามสนธิสัญญาให้กัมพูชาอยู่ใต้อารักขาฝรั่งเศส 11 สิงหาคม"),
     "src": ENW + "French_protectorate_of_Cambodia", "src_name": "Wikipedia: French protectorate of Cambodia"},
    {"y": Y("1866", "2409"), "text": t("Norodom moves his court from Oudong to Phnom Penh; the Royal Palace goes up between 1866 and 1870.",
                                         "ព្រះបាទនរោត្តមផ្លាស់ព្រះរាជវាំងពីឧដុង្គមកភ្នំពេញ។ ព្រះបរមរាជវាំងត្រូវបានសាងសង់ពីឆ្នាំ១៨៦៦ ដល់ ១៨៧០។",
                                         "พระนโรดมย้ายราชสำนักจากอุดงมาพนมเปญ สร้างพระบรมราชวังระหว่าง 2409–2413"),
     "src": ENW + "Oudong", "src_name": "Wikipedia: Oudong"},
    {"y": Y("1937", "2480"), "text": t("King Sisowath Monivong opens the Central Market, Jean Desbois's art deco hall with a 26-metre dome.",
                                         "ព្រះបាទស៊ីសុវត្ថិ មុនីវង្ស សម្ពោធផ្សារធំថ្មី ដែលលោក ហ្សង់ ដេប៊ួ រចនាបែបអាតដេកូ មានលំហដំបូលកម្ពស់ ២៦ ម៉ែត្រ។",
                                         "พระสีสุวัตถิ์ มุนีวงศ์ เปิดตลาดกลาง อาคารอาร์ตเดโคของฌอง เดอบัว โดมสูง 26 เมตร"),
     "src": ENW + "Central_Market,_Phnom_Penh", "src_name": "Wikipedia: Central Market, Phnom Penh"},
    {"y": Y("1953", "2496"), "text": t("Independence from France, celebrated on 9 November.", "ឯករាជ្យពីបារាំង អបអរនៅថ្ងៃទី៩ វិច្ឆិកា។", "ได้เอกราชจากฝรั่งเศส ฉลอง 9 พฤศจิกายน"),
     "src": ENW + "French_protectorate_of_Cambodia", "src_name": "Wikipedia: French protectorate of Cambodia"},
    {"y": Y("1958", "2501"), "text": t("The Independence Monument, 37 metres, by Vann Molyvann, rises at Norodom and Sihanouk boulevards.",
                                         "វិមានឯករាជ្យ កម្ពស់ ៣៧ ម៉ែត្រ ស្នាដៃលោក វណ្ណ មូលីវណ្ណ ត្រូវបានសាងសង់នៅផ្លូវប្រសព្វមហាវិថីនរោត្តម និងសីហនុ។",
                                         "อนุสาวรีย์เอกราช สูง 37 เมตร งานของวัณณ์ โมลีวัณณ์ ตั้งที่ทางแยกถนนนโรดมกับสีหนุ"),
     "src": ENW + "Independence_Monument,_Phnom_Penh", "src_name": "Wikipedia: Independence Monument"},
    {"y": Y("1964", "2507"), "text": t("Molyvann's National Sports Complex and Olympic Stadium are finished. No Olympic Games has been held there.",
                                         "មជ្ឈមណ្ឌលកីឡាជាតិ និងពហុកីឡដ្ឋានអូឡាំពិក ស្នាដៃលោក មូលីវណ្ណ ត្រូវបានបញ្ចប់។ មិនដែលមានការប្រកួតអូឡាំពិកនៅទីនោះទេ។",
                                         "ศูนย์กีฬาแห่งชาติและสนามกีฬาโอลิมปิกของโมลีวัณณ์สร้างเสร็จ ยังไม่เคยจัดโอลิมปิกที่นี่"),
     "src": ENW + "Olympic_Stadium_(Phnom_Penh)", "src_name": "Wikipedia: Olympic Stadium (Phnom Penh)"},
    {"y": Y("1975", "2518"), "text": t("17 April: the Khmer Rouge take Phnom Penh and order everyone out. The city held 2 to 3 million people, most of them refugees from the war.",
                                         "ថ្ងៃទី១៧ មេសា៖ ខ្មែរក្រហមចូលកាន់កាប់ភ្នំពេញ ហើយបញ្ជាឲ្យប្រជាជនទាំងអស់ចេញ។ ទីក្រុងមានប្រជាជន ២ ទៅ ៣ លាននាក់ ភាគច្រើនជាជនភៀសខ្លួនពីសង្គ្រាម។",
                                         "17 เมษายน เขมรแดงยึดพนมเปญและสั่งให้ทุกคนออกจากเมือง ขณะนั้นมีคน 2–3 ล้านคน ส่วนใหญ่ลี้ภัยสงครามมา"),
     "src": ENW + "Fall_of_Phnom_Penh", "src_name": "Wikipedia: Fall of Phnom Penh"},
    {"y": Y("1975–79", "2518–22"), "text": t("A school at Tuol Svay Prey becomes Security Prison 21. The museum counts 15,000 to 20,000 people held there; 12 were found alive in January 1979. The ECCC states over a million people died under Democratic Kampuchea.",
                                         "សាលារៀនទួលស្វាយព្រៃក្លាយជាគុកសន្តិសុខ ស-២១។ សារមន្ទីររាប់អ្នកជាប់ឃុំ ១៥.០០០ ទៅ ២០.០០០ នាក់ នៅខែមករា ១៩៧៩ រកឃើញអ្នករស់រានមានជីវិតតែ ១២ នាក់។ អ.វ.ត.ក ថ្លែងថា មនុស្សជាងមួយលាននាក់បានស្លាប់ក្រោមរបបកម្ពុជាប្រជាធិបតេយ្យ។",
                                         "โรงเรียนตวลสวายไพรกลายเป็นคุกความมั่นคง S-21 พิพิธภัณฑ์นับผู้ถูกคุมขัง 15,000–20,000 คน พบผู้รอดชีวิต 12 คนในเดือนมกราคม 2522 ศาลพิเศษ ECCC ระบุว่ามีผู้เสียชีวิตกว่าหนึ่งล้านคนในยุคกัมพูชาประชาธิปไตย"),
     "src": "https://tuolsleng.gov.kh/en/museum/building/", "src_name": "Tuol Sleng Genocide Museum"},
    {"y": Y("1979", "2522"), "text": t("7 January: Vietnamese forces with the Cambodian front enter Phnom Penh.", "ថ្ងៃទី៧ មករា៖ កងទ័ពវៀតណាមរួមជាមួយរណសិរ្សកម្ពុជា ចូលភ្នំពេញ។", "7 มกราคม กองทัพเวียดนามพร้อมแนวร่วมกัมพูชาเข้าพนมเปญ"),
     "src": ENW + "Cambodian%E2%80%93Vietnamese_War", "src_name": "Wikipedia: Cambodian–Vietnamese War"},
    {"y": Y("1991–93", "2534–36"), "text": t("The Paris Peace Agreements are signed on 23 October 1991; UNTAC runs the country and the elections in 1992–93.",
                                              "កិច្ចព្រមព្រៀងសន្តិភាពទីក្រុងប៉ារីស ចុះហត្ថលេខានៅថ្ងៃទី២៣ តុលា ១៩៩១។ អ៊ុនតាក់គ្រប់គ្រងប្រទេស និងរៀបចំការបោះឆ្នោតក្នុងឆ្នាំ១៩៩២–៩៣។",
                                              "ลงนามความตกลงสันติภาพปารีส 23 ตุลาคม 2534 อันแทคบริหารประเทศและจัดเลือกตั้ง 2535–36"),
     "src": ENW + "Paris_Peace_Agreements", "src_name": "Wikipedia: Paris Peace Agreements"},
    {"y": Y("2010", "2553"), "text": t("The ECCC, a court of Cambodia and the UN sitting in Phnom Penh, convicts Duch, head of S-21, on 26 July. It closes in December 2022 after three convictions.",
                                         "អ.វ.ត.ក ជាតុលាការរវាងកម្ពុជា និងអង្គការសហប្រជាជាតិ នៅភ្នំពេញ ផ្តន្ទាទោស ឌុច ប្រធានគុក ស-២១ នៅថ្ងៃទី២៦ កក្កដា។ តុលាការបិទនៅខែធ្នូ ២០២២ ក្រោយការផ្តន្ទាទោសបីសំណុំរឿង។",
                                         "ศาลพิเศษ ECCC ของกัมพูชาและสหประชาชาติที่พนมเปญ ตัดสินลงโทษดุช ผู้คุมคุก S-21 เมื่อ 26 กรกฎาคม ปิดศาลธันวาคม 2565 หลังตัดสินลงโทษสามคดี"),
     "src": "https://www.eccc.gov.kh/en", "src_name": "ECCC"},
    {"y": Y("2025", "2568"), "text": t("Techo International Airport, 19 km south in Kandal, opens on 9 September and takes over from the old airport.",
                                         "អាកាសយានដ្ឋានអន្តរជាតិតេជោ ចម្ងាយ ១៩ គីឡូម៉ែត្រ ខាងត្បូង ក្នុងខេត្តកណ្តាល ចាប់ដំណើរការនៅថ្ងៃទី៩ កញ្ញា ជំនួសអាកាសយានដ្ឋានចាស់។",
                                         "ท่าอากาศยานนานาชาติเตโช ห่างไปทางใต้ 19 กม. ในจังหวัดกันดาล เปิด 9 กันยายน แทนสนามบินเดิม"),
     "src": ENW + "Techo_International_Airport", "src_name": "Wikipedia: Techo International Airport"},
]

LEGENDS = [
    {"tag": t("Wat Phnom", "វត្តភ្នំ", "วัดพนม"), "name": t("Lady Penh and the koki tree", "ដូនពេញ និងដើមគគី", "ยายเพ็ญกับต้นตะเคียน"),
     "text": t("Penh, a wealthy woman at Chaktomuk, saw a koki tree floating in the flood and had it pulled ashore. Inside were four Buddha images and one of Vishnu. She had a hill raised on the west bank and a shrine built on top. The hill is Wat Phnom; the city is Phnom Penh, Penh's hill.",
               "ដូនពេញ ជាស្ត្រីអ្នកមាននៅចតុមុខ បានឃើញដើមគគីអណ្តែតក្នុងទឹកជំនន់ ហើយឲ្យគេទាញឡើងគោក។ នៅខាងក្នុងមានព្រះពុទ្ធរូបបួនអង្គ និងរូបព្រះនារាយណ៍មួយ។ គាត់ឲ្យគេលើកភ្នំនៅច្រាំងខាងលិច ហើយសាងវិហារនៅលើកំពូល។ ភ្នំនោះគឺវត្តភ្នំ ទីក្រុងគឺភ្នំពេញ។",
               "ยายเพ็ญ หญิงมั่งมีที่จตุมุข เห็นต้นตะเคียนลอยมากับน้ำหลาก จึงให้ลากขึ้นฝั่ง ข้างในมีพระพุทธรูปสี่องค์และรูปพระนารายณ์หนึ่งองค์ นางให้ก่อเนินทางฝั่งตะวันตกและสร้างศาลบนยอด เนินนั้นคือวัดพนม เมืองนั้นคือพนมเปญ"),
     "src": PP, "src_name": "Wikipedia: Phnom Penh"},
    {"tag": t("Chaktomuk", "ចតុមុខ", "จตุมุข"), "name": t("Four faces", "ចតុមុខ", "สี่หน้า"),
     "text": t("Chaktomuk, “four faces”, names the place where the upper and lower Mekong, the Tonlé Sap and the Bassac meet. The name recalls four-faced Brahma. Ponhea Yat called his city Krong Chaktomuk.",
               "ចតុមុខ គឺជាឈ្មោះកន្លែងដែលទន្លេមេគង្គលើ មេគង្គក្រោម ទន្លេសាប និងទន្លេបាសាក់ជួបគ្នា។ ឈ្មោះនេះរំលឹកដល់ព្រះព្រហ្មមុខបួន។ ព្រះបាទពញាយ៉ាតហៅទីក្រុងថា ក្រុងចតុមុខ។",
               "จตุมุข แปลว่าสี่หน้า คือที่แม่น้ำโขงตอนบน โขงตอนล่าง โตนเลสาบ และบาสัก มาบรรจบกัน ชื่อนี้ชวนนึกถึงพระพรหมสี่หน้า พญายาตเรียกเมืองว่ากรุงจตุมุข"),
     "src": PP, "src_name": "Wikipedia: Phnom Penh"},
    {"tag": t("Tonlé Sap", "ទន្លេសាប", "โตนเลสาบ"), "name": t("The river that turns back", "ទន្លេដែលហូរបញ្ច្រាស", "แม่น้ำที่ไหลย้อน"),
     "text": t("The 115-km Tonlé Sap river runs about six months toward its lake and six months back. Inflow starts in May or June and ends in October or November. Bon Om Touk marks the turn.",
               "ទន្លេសាប ប្រវែង ១១៥ គីឡូម៉ែត្រ ហូរទៅបឹងប្រហែលប្រាំមួយខែ ហើយហូរត្រឡប់វិញប្រាំមួយខែ។ ទឹកចាប់ផ្តើមហូរចូលបឹងនៅខែឧសភា ឬមិថុនា ហើយឈប់នៅខែតុលា ឬវិច្ឆិកា។ បុណ្យអុំទូកអបអរការប្តូរទិសនេះ។",
               "โตนเลสาบยาว 115 กม. ไหลเข้าทะเลสาบราวหกเดือน แล้วไหลกลับอีกหกเดือน น้ำเริ่มไหลเข้าราวพฤษภาคมหรือมิถุนายน และหยุดราวตุลาคมหรือพฤศจิกายน บุญอมตูกฉลองการเปลี่ยนทิศนี้"),
     "src": TS, "src_name": "Wikipedia: Tonlé Sap"},
    {"tag": t("Bon Om Touk", "បុណ្យអុំទូក", "บุญอมตูก"), "name": t("The nāga's tooth", "ធ្មេញនាគ", "เขี้ยวพญานาค"),
     "text": t("One account says the water festival honours a tooth lost in the deep by a nāga whose daughter married an Indian prince and founded Cambodia. After the races, the boats gather to urge the nāga to send the swollen waters to the sea.",
               "តាមរឿងមួយ បុណ្យទឹកនេះគោរពដល់ធ្មេញមួយ ដែលនាគបាត់បង់នៅបាតទឹកជ្រៅ។ បុត្រីនាគរៀបការជាមួយព្រះរាជបុត្រឥណ្ឌា ហើយបង្កើតកម្ពុជា។ ក្រោយការប្រណាំង ទូកជួបជុំគ្នាអង្វរនាគឲ្យបញ្ជូនទឹកជំនន់ទៅសមុទ្រ។",
               "เรื่องหนึ่งว่าเทศกาลน้ำนี้บูชาเขี้ยวที่พญานาคทำหล่นในน้ำลึก ธิดานาคแต่งงานกับเจ้าชายอินเดียและสร้างกัมพูชา หลังแข่งเรือ เรือทั้งหมดมารวมกันขอให้พญานาคส่งน้ำหลากลงทะเล"),
     "src": TS, "src_name": "Wikipedia: Tonlé Sap"},
    {"tag": t("Origin", "ដើមកំណើត", "กำเนิด"), "name": t("Preah Thong and Neang Neak", "ព្រះថោង និងនាងនាគ", "พระทองกับนางนาค"),
     "text": t("A foreign prince, Preah Thong, marries the nāga princess Neang Neak, and together they found Funan, the first Cambodian kingdom. Much of the Khmer wedding is traced to this marriage.",
               "ព្រះថោង ជាព្រះរាជបុត្របរទេស រៀបអភិសេកជាមួយនាងនាគ ជាបុត្រីស្តេចនាគ ហើយបង្កើតនគរហ្វូណន ជានគរដំបូងនៃកម្ពុជា។ ពិធីរៀបការខ្មែរជាច្រើនមានដើមកំណើតពីរឿងនេះ។",
               "พระทอง เจ้าชายต่างแดน แต่งงานกับนางนาค ธิดาพญานาค แล้วสร้างอาณาจักรฟูนัน อาณาจักรแรกของกัมพูชา พิธีแต่งงานเขมรหลายอย่างสืบมาจากเรื่องนี้"),
     "src": ENW + "Preah_Thong_and_Neang_Neak", "src_name": "Wikipedia: Preah Thong and Neang Neak"},
    {"tag": t("Folk tale", "រឿងព្រេង", "นิทาน"), "name": t("Preah Ko Preah Keo", "ព្រះគោ ព្រះកែវ", "พระโค พระแก้ว"),
     "text": t("Two brothers: Preah Ko, an ox with divine power and treasure in his belly, and Preah Keo, a man. They bring peace wherever they live. One reading takes the tale as the treasure lost when Longvek fell in 1594.",
               "បងប្អូនពីរនាក់៖ ព្រះគោ ជាគោមានឫទ្ធិ មានកំណប់ក្នុងពោះ និងព្រះកែវ ជាមនុស្ស។ ពួកគេនាំសន្តិភាពទៅគ្រប់ទីដែលពួកគេរស់នៅ។ ការបកស្រាយមួយថា រឿងនេះនិយាយពីកំណប់ដែលបាត់ពេលលង្វែកដួលរលំ ឆ្នាំ១៥៩៤។",
               "พี่น้องสองคน พระโคเป็นวัวมีฤทธิ์ มีของมีค่าอยู่ในท้อง และพระแก้วเป็นคน ทั้งสองนำความสงบมาทุกที่ที่อยู่ การตีความหนึ่งว่าเป็นเรื่องของสมบัติที่หายไปเมื่อละแวกแตก ปี 2137"),
     "src": ENW + "Preah_Ko_Preah_Keo", "src_name": "Wikipedia: Preah Ko Preah Keo"},
    {"tag": t("Wat Phnom", "វត្តភ្នំ", "วัดพนม"), "name": t("Neak ta, the guardian spirits", "អ្នកតា", "เนียะตา ผีอารักษ์"),
     "text": t("A neak ta watches over people, places and things while they are shown respect. The cult is older than Hinduism and Buddhism in Cambodia and has no priests. At Wat Phnom a small shrine to Lady Penh stands at the southwest corner.",
               "អ្នកតា ថែរក្សាមនុស្ស ទីកន្លែង និងវត្ថុ ដរាបណាគេគោរព។ ជំនឿនេះមានមុនព្រហ្មញ្ញសាសនា និងព្រះពុទ្ធសាសនានៅកម្ពុជា ហើយគ្មានបូជាចារ្យ។ នៅវត្តភ្នំ មានខ្ទមតូចមួយសម្រាប់ដូនពេញ នៅជ្រុងនិរតី។",
               "เนียะตาคุ้มครองคน สถานที่ และสิ่งของ ตราบที่ได้รับความเคารพ ความเชื่อนี้มีมาก่อนศาสนาพราหมณ์และพุทธในกัมพูชา และไม่มีนักบวช ที่วัดพนมมีศาลเล็กของยายเพ็ญอยู่มุมตะวันตกเฉียงใต้"),
     "src": ENW + "Neak_ta", "src_name": "Wikipedia: Neak ta"},
]


def P(en, km_, th, years, text, src, src_name):
    return {"tag": years, "name": t(en, km_, th), "text": text, "src": src, "src_name": src_name}


PEOPLE = [
    P("Lady Penh", "ដូនពេញ", "ยายเพ็ญ", t("1372", "១៣៧២", "1915"), t("In tradition, the founder of Phnom Penh and its hill.", "តាមដំណាល ជាអ្នកបង្កើតភ្នំពេញ និងភ្នំ។", "ตามตำนาน ผู้ก่อตั้งพนมเปญและเนินนั้น"), ENW + "Penh", "Wikipedia: Penh"),
    P("Ponhea Yat", "ពញាយ៉ាត", "พญายาต", t("c. 1394–1463", "ប្រហែល ១៣៩៤–១៤៦៣", "ราว 1937–2006"), t("King who moved the court from Angkor to Chaktomuk and ordered monasteries built around the city.", "ព្រះមហាក្សត្រដែលផ្លាស់រាជធានីពីអង្គរមកចតុមុខ ហើយបញ្ជាឲ្យសាងសង់វត្តជុំវិញទីក្រុង។", "กษัตริย์ผู้ย้ายราชสำนักจากนครวัดมาจตุมุข และให้สร้างวัดรอบเมือง"), ENW + "Ponhea_Yat", "Wikipedia: Ponhea Yat"),
    P("King Norodom", "ព្រះបាទនរោត្តម", "พระนโรดม", t("1834–1904", "១៨៣៤–១៩០៤", "2377–2447"), t("Signed the 1863 protectorate treaty and moved the court to Phnom Penh, where he built the Royal Palace.", "ចុះហត្ថលេខាលើសន្ធិសញ្ញាអាណាព្យាបាល ឆ្នាំ១៨៦៣ ហើយផ្លាស់ព្រះរាជវាំងមកភ្នំពេញ ជាកន្លែងសាងសង់ព្រះបរមរាជវាំង។", "ลงนามสนธิสัญญาอารักขา 2406 และย้ายราชสำนักมาพนมเปญ สร้างพระบรมราชวัง"), ENW + "Norodom_of_Cambodia", "Wikipedia: Norodom"),
    P("King Norodom Sihanouk", "ព្រះបាទនរោត្តម សីហនុ", "พระนโรดม สีหนุ", t("1922–2012", "១៩២២–២០១២", "2465–2555"), t("King, head of state and prime minister; won independence from France in 1953 and wanted a new architecture for Phnom Penh.", "ព្រះមហាក្សត្រ ប្រមុខរដ្ឋ និងនាយករដ្ឋមន្ត្រី ទទួលបានឯករាជ្យពីបារាំងឆ្នាំ១៩៥៣ ហើយចង់បានស្ថាបត្យកម្មថ្មីសម្រាប់ភ្នំពេញ។", "กษัตริย์ ประมุขรัฐ และนายกรัฐมนตรี ได้เอกราชจากฝรั่งเศสปี 2496 และอยากได้สถาปัตยกรรมใหม่ให้พนมเปญ"), ENW + "Norodom_Sihanouk", "Wikipedia: Norodom Sihanouk"),
    P("Vann Molyvann", "វណ្ណ មូលីវណ្ណ", "วัณณ์ โมลีวัณณ์", t("1926–2017", "១៩២៦–២០១៧", "2469–2560"), t("Architect of New Khmer Architecture: the Independence Monument, Chaktomuk Conference Hall and Olympic Stadium.", "ស្ថាបត្យករនៃស្ថាបត្យកម្មខ្មែរថ្មី៖ វិមានឯករាជ្យ សាលសន្និសីទចតុមុខ និងពហុកីឡដ្ឋានអូឡាំពិក។", "สถาปนิกแห่งสถาปัตยกรรมเขมรใหม่ อนุสาวรีย์เอกราช หอประชุมจตุมุข และสนามกีฬาโอลิมปิก"), ENW + "Vann_Molyvann", "Wikipedia: Vann Molyvann"),
    P("Sinn Sisamouth", "ស៊ីន ស៊ីសាមុត", "สิน ศรีสมุทร", t("c. 1933–1976", "ប្រហែល ១៩៣៣–១៩៧៦", "ราว 2476–2519"), t("Singer-songwriter of Phnom Penh's music scene from the 1950s to the 1970s; died under the Khmer Rouge.", "អ្នកនិពន្ធ និងចម្រៀងនៃវិស័យតន្ត្រីភ្នំពេញ ពីទសវត្សរ៍ ១៩៥០ ដល់ ១៩៧០ បានស្លាប់ក្រោមរបបខ្មែរក្រហម។", "นักร้องนักแต่งเพลงของวงการดนตรีพนมเปญ ทศวรรษ 2490–2510 เสียชีวิตในยุคเขมรแดง"), ENW + "Sinn_Sisamouth", "Wikipedia: Sinn Sisamouth"),
    P("Ros Serey Sothea", "រស់ សេរីសុទ្ធា", "รส สิริสุทธา", t("c. 1948–1978", "ប្រហែល ១៩៤៨–១៩៧៨", "ราว 2491–2521"), t("Singer; Sihanouk called her the “Queen with the Golden Voice”. She disappeared under the Khmer Rouge.", "អ្នកចម្រៀង សម្តេចសីហនុហៅនាងថា “មហាក្សត្រីសំឡេងមាស”។ នាងបាត់ខ្លួនក្រោមរបបខ្មែរក្រហម។", "นักร้อง สีหนุขนานนามว่า “ราชินีเสียงทอง” หายตัวไปในยุคเขมรแดง"), ENW + "Ros_Serey_Sothea", "Wikipedia: Ros Serey Sothea"),
    P("Pen Ran", "ប៉ែន រ៉ន", "แปน รอน", t("c. 1944–1979", "ប្រហែល ១៩៤៤–១៩៧៩", "ราว 2487–2522"), t("Singer and songwriter with rock and soul in her sound; recorded with Sinn Sisamouth from 1966.", "អ្នកចម្រៀង និងនិពន្ធបទ មានសំឡេងរ៉ុក និងសូល ថតជាមួយ ស៊ីន ស៊ីសាមុត ចាប់ពីឆ្នាំ១៩៦៦។", "นักร้องนักแต่งเพลงที่มีกลิ่นร็อกและโซล บันทึกเสียงกับสิน ศรีสมุทร ตั้งแต่ 2509"), ENW + "Pen_Ran", "Wikipedia: Pen Ran"),
    P("Princess Norodom Buppha Devi", "សម្តេចរាជបុត្រី នរោត្តម បុប្ផាទេវី", "นโรดม บุปผาเทวี", t("1943–2019", "១៩៤៣–២០១៩", "2486–2562"), t("Prima ballerina and director of the Royal Ballet; later Minister of Culture and Fine Arts.", "តារារបាំឯក និងនាយិការបាំព្រះរាជទ្រព្យ ក្រោយមកជារដ្ឋមន្ត្រីក្រសួងវប្បធម៌ និងវិចិត្រសិល្បៈ។", "นางระบำเอกและผู้อำนวยการระบำหลวง ต่อมาเป็นรัฐมนตรีวัฒนธรรมและวิจิตรศิลป์"), ENW + "Norodom_Buppha_Devi", "Wikipedia: Norodom Buppha Devi"),
    P("Dith Pran", "ឌិត ប្រន", "ดิธ ปราน", t("1942–2008", "១៩៤២–២០០៨", "2485–2551"), t("Photojournalist who stayed in Phnom Penh in 1975, survived four years under the Khmer Rouge and coined the phrase “killing fields”.", "អ្នកកាសែតថតរូប ដែលនៅភ្នំពេញឆ្នាំ១៩៧៥ រស់រានពីរបបខ្មែរក្រហមបួនឆ្នាំ ហើយបង្កើតពាក្យ “វាលពិឃាត”។", "ช่างภาพข่าวที่อยู่พนมเปญปี 2518 รอดชีวิตสี่ปีในยุคเขมรแดง และเป็นผู้คิดคำว่า “ทุ่งสังหาร”"), ENW + "Dith_Pran", "Wikipedia: Dith Pran"),
    P("Rithy Panh", "រិទ្ធី ប៉ាន់", "ฤทธี ปาณห์", t("born 1964", "កើត ១៩៦៤", "เกิด 2507"), t("Documentary director born in Phnom Penh; his films, among them S-21: The Khmer Rouge Killing Machine (2003), concern the Khmer Rouge years.", "អ្នកដឹកនាំខ្សែភាពយន្តឯកសារ កើតនៅភ្នំពេញ ខ្សែភាពយន្តរបស់លោក រួមទាំង ស-២១ (២០០៣) និយាយពីសម័យខ្មែរក្រហម។", "ผู้กำกับสารคดี เกิดที่พนมเปญ ผลงานรวมถึง S-21 (2546) ว่าด้วยยุคเขมรแดง"), ENW + "Rithy_Panh", "Wikipedia: Rithy Panh"),
    P("Chum Mey", "ជុំ ម៉ី", "จุม เม็ย", t("born c. 1930", "កើតប្រហែល ១៩៣០", "เกิดราว 2473"), t("Mechanic, sent out of the city on 17 April 1975, held at S-21 from October 1978, one of very few to survive it; testified at the ECCC in 2009.", "ជាងម៉ាស៊ីន ត្រូវជម្លៀសចេញពីទីក្រុងថ្ងៃទី១៧ មេសា ១៩៧៥ ជាប់ឃុំនៅ ស-២១ ពីខែតុលា ១៩៧៨ ជាអ្នករស់រានមានជីវិតម្នាក់ក្នុងចំណោមមួយចំនួនតូច ហើយផ្តល់សក្ខីកម្មនៅ អ.វ.ត.ក ឆ្នាំ២០០៩។", "ช่างเครื่อง ถูกต้อนออกจากเมือง 17 เมษายน 2518 ถูกคุมขังที่ S-21 ตั้งแต่ตุลาคม 2521 หนึ่งในไม่กี่คนที่รอด ให้การต่อศาล ECCC ปี 2552"), "https://www.eccc.gov.kh/en/directory/witness-profile/chum-mey", "ECCC: Chum Mey"),
    P("Youk Chhang", "ឆាំង យុ", "ยุก ชาง", t("born 1961", "កើត ១៩៦១", "เกิด 2504"), t("Director of the Documentation Center of Cambodia since 1995; born in Phnom Penh and separated from his family in the 1975 evacuation.", "នាយកមជ្ឈមណ្ឌលឯកសារកម្ពុជា តាំងពីឆ្នាំ១៩៩៥ កើតនៅភ្នំពេញ ហើយបែកពីគ្រួសារក្នុងការជម្លៀសឆ្នាំ១៩៧៥។", "ผู้อำนวยการศูนย์เอกสารกัมพูชาตั้งแต่ 2538 เกิดที่พนมเปญ พลัดจากครอบครัวเมื่อถูกต้อนออกจากเมืองปี 2518"), ENW + "Youk_Chhang", "Wikipedia: Youk Chhang"),
]


def S(tag, en, km_, th, text, src, src_name):
    return {"tag": tag, "name": t(en, km_, th), "text": text, "src": src, "src_name": src_name}


SITES = [
    S(t("1866–70", "១៨៦៦–៧០", "2409–13"), "Royal Palace", "ព្រះបរមរាជវាំង", "พระบรมราชวัง", t("The King's residence, on the west bank at Chaktomuk; built by Norodom, rebuilt 1912–1932.", "ព្រះរាជដំណាក់របស់ព្រះមហាក្សត្រ នៅច្រាំងខាងលិចចតុមុខ សាងសង់ដោយព្រះបាទនរោត្តម សាងសង់ឡើងវិញ ១៩១២–១៩៣២។", "ที่ประทับของพระมหากษัตริย์ ริมฝั่งตะวันตกของจตุมุข พระนโรดมสร้าง สร้างใหม่ 2455–2475"), ENW + "Royal_Palace,_Phnom_Penh", "Wikipedia: Royal Palace, Phnom Penh"),
    S(t("Palace", "វាំង", "ในวัง"), "Silver Pagoda", "វត្តព្រះកែវមរកត", "วัดพระแก้วมรกต", t("South side of the palace: a small green crystal Buddha and a gold Maitreya ordered by King Sisowath.", "ខាងត្បូងព្រះបរមរាជវាំង៖ ព្រះពុទ្ធរូបកែវពណ៌បៃតងតូចមួយ និងព្រះសិអារ្យមេត្រីយមាស ដែលព្រះបាទស៊ីសុវត្ថិបញ្ជាឲ្យធ្វើ។", "ด้านใต้ของพระราชวัง มีพระพุทธรูปแก้วสีเขียวองค์เล็ก และพระศรีอาริยเมตไตรยทองคำที่พระสีสุวัตถิ์โปรดให้สร้าง"), ENW + "Silver_Pagoda", "Wikipedia: Silver Pagoda"),
    S(t("1920", "១៩២០", "2463"), "National Museum", "សារមន្ទីរជាតិ", "พิพิธภัณฑสถานแห่งชาติ", t("Cambodia's largest museum of cultural history, over 14,000 objects, in red buildings of 1917–1924.", "សារមន្ទីរប្រវត្តិវប្បធម៌ធំបំផុតនៃកម្ពុជា មានវត្ថុជាង ១៤.០០០ ក្នុងអគារពណ៌ក្រហម ១៩១៧–១៩២៤។", "พิพิธภัณฑ์ประวัติศาสตร์วัฒนธรรมใหญ่ที่สุดของกัมพูชา วัตถุกว่า 14,000 ชิ้น ในอาคารสีแดงปี 2460–2467"), ENW + "National_Museum_of_Cambodia", "Wikipedia: National Museum of Cambodia"),
    S(t("46 m", "៤៦ ម៉ែត្រ", "46 ม."), "Wat Phnom", "វត្តភ្នំ", "วัดพนม", t("The hill that names the city, with Lady Penh's shrine at the southwest corner.", "ភ្នំដែលផ្តល់ឈ្មោះដល់ទីក្រុង មានខ្ទមដូនពេញនៅជ្រុងនិរតី។", "เนินที่เป็นชื่อเมือง มีศาลยายเพ็ญที่มุมตะวันตกเฉียงใต้"), ENW + "Wat_Phnom", "Wikipedia: Wat Phnom"),
    S(t("1443", "១៤៤៣", "1986"), "Wat Ounalom", "វត្តឧណ្ណាលោម", "วัดอุณาโลม", t("Former seat of the Mahanikaya order; keeps what is held to be a hair from between the Buddha's eyebrows.", "អតីតទីស្នាក់ការគណៈមហានិកាយ រក្សាទុកព្រះលោមដែលគេជឿថាជារោមចិញ្ចើមរបស់ព្រះពុទ្ធ។", "อดีตที่ตั้งคณะมหานิกาย เก็บพระอุณาโลมที่เชื่อว่าเป็นขนระหว่างพระขนงของพระพุทธเจ้า"), ENW + "Wat_Ounalom", "Wikipedia: Wat Ounalom"),
    S(t("15th c.", "សតវត្សទី១៥", "พุทธศตวรรษที่ 20"), "Wat Botum", "វត្តបទុមវតី", "วัดปทุมวดี", t("One of Ponhea Yat's pagodas, south of the palace; Norodom rebuilt and renamed it from 1865.", "វត្តមួយក្នុងចំណោមវត្តរបស់ព្រះបាទពញាយ៉ាត ខាងត្បូងវាំង ព្រះបាទនរោត្តមសាងសង់ឡើងវិញ និងប្តូរឈ្មោះ ចាប់ពីឆ្នាំ១៨៦៥។", "หนึ่งในวัดของพญายาต ทางใต้ของวัง พระนโรดมบูรณะและเปลี่ยนชื่อตั้งแต่ 2408"), ENW + "Wat_Botum", "Wikipedia: Wat Botum"),
    S(t("1442", "១៤៤២", "1985"), "Wat Langka", "វត្តលង្កា", "วัดลังกา", t("Built to keep the Tripitaka and as a meeting place for Khmer and Sri Lankan monks, which gave it its name.", "សាងសង់ដើម្បីរក្សាព្រះត្រៃបិដក និងជាកន្លែងជួបជុំព្រះសង្ឃខ្មែរ និងស្រីលង្កា ដែលជាប្រភពឈ្មោះ។", "สร้างเพื่อเก็บพระไตรปิฎก และเป็นที่พบของพระเขมรกับพระลังกา จึงได้ชื่อนี้"), ENW + "Wat_Langka", "Wikipedia: Wat Langka"),
    S(t("1937", "១៩៣៧", "2480"), "Central Market", "ផ្សារធំថ្មី", "ตลาดกลาง (ผสารธมทเมย)", t("Art deco market: a 26-metre dome and four arms of stalls.", "ផ្សារបែបអាតដេកូ៖ លំហដំបូលកម្ពស់ ២៦ ម៉ែត្រ និងស្លាបតូបបួន។", "ตลาดอาร์ตเดโค โดมสูง 26 เมตร กับปีกแผงค้าสี่ด้าน"), ENW + "Central_Market,_Phnom_Penh", "Wikipedia: Central Market, Phnom Penh"),
    S(t("Toul Tom Poung", "ទួលទំពូង", "ตวลทุมปูง"), "Russian Market", "ផ្សារទួលទំពូង", "ตลาดรัสเซีย (ผสารตวลทุมปูง)", t("Souvenirs, jewellery, gold, clothes. Named for the Russian goods it once sold.", "វត្ថុអនុស្សាវរីយ៍ គ្រឿងអលង្ការ មាស សម្លៀកបំពាក់។ ហៅថាផ្សាររុស្ស៊ី ព្រោះធ្លាប់លក់ទំនិញពីរុស្ស៊ី។", "ของที่ระลึก เครื่องประดับ ทอง เสื้อผ้า ได้ชื่อตามสินค้ารัสเซียที่เคยขาย"), "https://km.wikipedia.org/wiki/%E1%9E%95%E1%9F%92%E1%9E%9F%E1%9E%B6%E1%9E%9A%E1%9E%91%E1%9E%BD%E1%9E%9B%E1%9E%91%E1%9F%86%E1%9E%96%E1%9E%BC%E1%9E%84", "វិគីភីឌា៖ ផ្សារទួលទំពូង"),
    S(t("1958", "១៩៥៨", "2501"), "Independence Monument", "វិមានឯករាជ្យ", "อนุสาวรีย์เอกราช", t("A 37-metre lotus-shaped stupa by Vann Molyvann, centre of national celebrations.", "ស្តូបរាងផ្កាឈូក កម្ពស់ ៣៧ ម៉ែត្រ ស្នាដៃលោក វណ្ណ មូលីវណ្ណ ជាកណ្តាលនៃពិធីបុណ្យជាតិ។", "สถูปรูปดอกบัวสูง 37 เมตร ของวัณณ์ โมลีวัณณ์ ศูนย์กลางงานฉลองของชาติ"), ENW + "Independence_Monument,_Phnom_Penh", "Wikipedia: Independence Monument"),
    S(t("1961", "១៩៦១", "2504"), "Chaktomuk Conference Hall", "សាលសន្និសីទចតុមុខ", "หอประชุมจตุมุข", t("Molyvann's fan-shaped hall on the quay. After 1979 a tribunal tried Pol Pot there in his absence.", "សាលរាងផ្លិតរបស់លោក មូលីវណ្ណ នៅមាត់ទន្លេ។ ក្រោយឆ្នាំ១៩៧៩ សាលាក្តីមួយបានជំនុំជម្រះ ប៉ុល ពត កំបាំងមុខនៅទីនោះ។", "หอรูปพัดของโมลีวัณณ์ริมแม่น้ำ หลัง 2522 มีศาลพิจารณาคดีพล พตลับหลังที่นี่"), ENW + "Chaktomuk_Conference_Hall", "Wikipedia: Chaktomuk Conference Hall"),
    S(t("1964", "១៩៦៤", "2507"), "National Olympic Stadium", "ពហុកីឡដ្ឋានជាតិអូឡាំពិក", "สนามกีฬาโอลิมปิกแห่งชาติ", t("Seats 30,000; Molyvann shaped it from 500,000 cubic metres of earth.", "ចំណុះ ៣០.០០០ កៅអី លោក មូលីវណ្ណ បានរចនាវាពីដី ៥០០.០០០ ម៉ែត្រគូប។", "จุ 30,000 ที่นั่ง โมลีวัณณ์ปั้นรูปจากดิน 500,000 ลูกบาศก์เมตร"), ENW + "Olympic_Stadium_(Phnom_Penh)", "Wikipedia: Olympic Stadium (Phnom Penh)"),
    S(t("Memorial", "ទីរំលឹក", "อนุสรณ์"), "Tuol Sleng Genocide Museum", "សារមន្ទីរឧក្រិដ្ឋកម្មប្រល័យពូជសាសន៍ទួលស្លែង", "พิพิธภัณฑ์ตวลสแลง", t("The S-21 prison in a former school; 15,000 to 20,000 people were held there, 1975–1979.", "គុក ស-២១ ក្នុងអតីតសាលារៀន មនុស្ស ១៥.០០០ ទៅ ២០.០០០ នាក់ ត្រូវឃុំនៅទីនោះ ១៩៧៥–១៩៧៩។", "คุก S-21 ในโรงเรียนเก่า มีผู้ถูกคุมขัง 15,000–20,000 คน ระหว่าง 2518–2522"), "https://tuolsleng.gov.kh/en/", "Tuol Sleng Genocide Museum"),
    S(t("Memorial", "ទីរំលឹក", "อนุสรณ์"), "Choeung Ek", "ជើងឯក", "เจิงเอก", t("A killing field 17 km south of the centre; 8,895 bodies were exhumed there.", "វាលពិឃាតចម្ងាយ ១៧ គីឡូម៉ែត្រ ខាងត្បូងទីក្រុង សាកសព ៨.៨៩៥ ត្រូវបានគាស់ចេញពីទីនោះ។", "ทุ่งสังหารห่างใจกลางเมือง 17 กม. ทางใต้ ขุดพบศพ 8,895 ศพ"), ENW + "Choeung_Ek", "Wikipedia: Choeung Ek"),
    S(t("Riverfront", "មាត់ទន្លេ", "ริมน้ำ"), "Sisowath Quay", "តីរវិថីព្រះស៊ីសុវត្ថិ", "ถนนริมน้ำสีสุวัตถิ์", t("The Tonlé Sap riverfront of hotels, cafés and shops; the stretch before the palace is where crowds watch the boat races.", "មាត់ទន្លេសាប មានសណ្ឋាគារ ហាងកាហ្វេ និងហាង ផ្នែកមុខវាំងជាកន្លែងមហាជនមើលប្រណាំងទូក។", "ริมโตนเลสาบที่มีโรงแรม คาเฟ่ ร้านค้า ช่วงหน้าพระราชวังคือที่ผู้คนชมแข่งเรือ"), ENW + "Sisowath_Quay", "Wikipedia: Sisowath Quay"),
]

CULTURE = [
    S(t("UNESCO 2008", "យូណេស្កូ ២០០៨", "ยูเนสโก 2551"), "Royal Ballet of Cambodia", "របាំព្រះរាជទ្រព្យ", "ระบำหลวงกัมพูชา", t("Court dance of over a thousand years with four roles: woman, man, giant and monkey. The Khmer Rouge killed nearly all the masters; troupes came back after 1979. Four basic hand gestures: sprout, leaf, flower, falling flower.", "របាំរាជវាំងជាងមួយពាន់ឆ្នាំ មានតួបួន៖ នាង នាយរោង យក្ស និងស្វា។ ខ្មែរក្រហមបានសម្លាប់គ្រូស្ទើរតែទាំងអស់ ក្រុមរបាំបានរស់ឡើងវិញក្រោយឆ្នាំ១៩៧៩។ ក្បាច់ដៃមូលដ្ឋានបួន៖ ត្រួយ ស្លឹក ផ្កា ផ្លែ។", "ระบำราชสำนักกว่าพันปี มีสี่บทบาท นาง พระ ยักษ์ ลิง เขมรแดงสังหารครูเกือบทั้งหมด คณะระบำกลับมาหลัง 2522 ท่ามือพื้นฐานสี่ท่า หน่อ ใบ ดอก ผล"), UNESCO + "RL/royal-ballet-of-cambodia-00060", "UNESCO: Royal Ballet of Cambodia"),
    S(t("UNESCO 2008", "យូណេស្កូ ២០០៨", "ยูเนสโก 2551"), "Sbek Thom", "ល្ខោនស្បែកធំ", "หนังใหญ่เขมร (สแบกธม)", t("Shadow theatre with two-metre leather puppets before a white screen and a fire; stories from the Reamker, up to 160 puppets, over several nights.", "ល្ខោនស្រមោល ប្រើស្បែកកម្ពស់ពីរម៉ែត្រ នៅមុខវាំងននស និងភ្លើង រឿងពីរាមកេរ្តិ៍ ប្រើស្បែករហូតដល់ ១៦០ សម្តែងច្រើនយប់។", "การแสดงเงา ตัวหนังสูงสองเมตร หน้าจอขาวกับกองไฟ เรื่องจากเรียมเกร์ ใช้ตัวหนังถึง 160 ตัว แสดงหลายคืน"), UNESCO + "RL/sbek-thom-khmer-shadow-theatre-00108", "UNESCO: Sbek Thom"),
    S(t("UNESCO 2016", "យូណេស្កូ ២០១៦", "ยูเนสโก 2559"), "Chapei Dang Veng", "ចាប៉ីដងវែង", "จาปีดองแวง", t("A singer plays the long-necked chapei lute; the words run from teaching to satire.", "អ្នកចម្រៀងលេងចាប៉ីដងវែង បទចម្រៀងមានចាប់ពីការអប់រំ ដល់ការរិះគន់បែបកំប្លែង។", "นักร้องดีดจาปีคอยาว เนื้อร้องมีตั้งแต่สั่งสอนจนถึงเสียดสี"), UNESCO + "USL/chapei-dang-veng-01165", "UNESCO: Chapei Dang Veng"),
    S(t("UNESCO 2018", "យូណេស្កូ ២០១៨", "ยูเนสโก 2561"), "Lakhon Khol", "ល្ខោនខោល", "ละโคนโขล", t("Masked dance drama by men. The Wat Svay Andet troupe, 10 km east on the Mekong, performs it for the neak ta.", "ល្ខោនពាក់មុខ សម្តែងដោយបុរស។ ក្រុមវត្តស្វាយអណ្តែត ចម្ងាយ ១០ គីឡូម៉ែត្រ ខាងកើត លើទន្លេមេគង្គ សម្តែងថ្វាយអ្នកតា។", "ละครสวมหน้ากากที่ผู้ชายแสดง คณะวัดสวายอันแดต ห่างไปทางตะวันออก 10 กม. ริมแม่น้ำโขง แสดงถวายเนียะตา"), UNESCO + "USL/lkhon-khol-wat-svay-andet-01374", "UNESCO: Lkhon Khol Wat Svay Andet"),
    S(t("Kadek", "កត្តិក", "กัตติกะ"), "Bon Om Touk", "បុណ្យអុំទូក", "บุญอมตูก", t("Three days, the 14th and 15th waxing and 1st waning of Kadek, at the end of the rains: boat races on the quay, fireworks, concerts.", "បីថ្ងៃ ១៤ និង ១៥ កើត និង ១ រោច ខែកត្តិក ចុងរដូវវស្សា៖ ប្រណាំងទូកនៅមាត់ទន្លេ កាំជ្រួច និងការប្រគុំតន្ត្រី។", "สามวัน ขึ้น 14–15 ค่ำ และแรม 1 ค่ำ เดือนกัตติกะ ปลายหน้าฝน แข่งเรือริมน้ำ พลุ คอนเสิร์ต"), "https://intocambodia.org/content/water-and-moon-festival-bon-om-tuk-bondet-protit-sam-peah-preah-khae", "Into Cambodia: Bon Om Tuk"),
    S(t("15 days", "១៥ ថ្ងៃ", "15 วัน"), "Pchum Ben", "បុណ្យភ្ជុំបិណ្ឌ", "ประชุมบิณฑ์", t("Fifteen days ending on the 15th of the tenth Khmer month; families feed the dead of seven generations through the monks.", "ដប់ប្រាំថ្ងៃ បញ្ចប់នៅថ្ងៃ ១៥ ខែទី១០ តាមចន្ទគតិខ្មែរ។ គ្រួសារឧទ្ទិសម្ហូបដល់ដូនតាប្រាំពីរជំនាន់ តាមរយៈព្រះសង្ឃ។", "สิบห้าวัน สิ้นสุดวันที่ 15 ของเดือนสิบเขมร ครอบครัวทำบุญถึงบรรพบุรุษเจ็ดชั่วคนผ่านพระสงฆ์"), ENW + "Pchum_Ben", "Wikipedia: Pchum Ben"),
    S(t("April", "មេសា", "เมษายน"), "Khmer New Year", "បុណ្យចូលឆ្នាំខ្មែរ", "ปีใหม่เขมร", t("Three days at the end of the harvest; New Year's Day usually falls on 13 or 14 April.", "បីថ្ងៃ នៅចុងរដូវប្រមូលផល ថ្ងៃចូលឆ្នាំជាធម្មតាត្រូវនឹងថ្ងៃទី១៣ ឬ ១៤ មេសា។", "สามวันหลังฤดูเก็บเกี่ยว วันขึ้นปีใหม่มักตรงกับ 13 หรือ 14 เมษายน"), ENW + "Cambodian_New_Year", "Wikipedia: Cambodian New Year"),
    S(t("1960s", "ទសវត្សរ៍ ៦០", "ทศวรรษ 2500"), "Phnom Penh rock", "តន្ត្រីរ៉ុកខ្មែរ", "ร็อกพนมเปญ", t("Khmer music met rock and pop from imported records. It ended in 1975; many of its singers disappeared.", "តន្ត្រីខ្មែរជួបរ៉ុក និងប៉ុបពីថាសនាំចូល។ វាបានបញ្ចប់នៅឆ្នាំ១៩៧៥ អ្នកចម្រៀងជាច្រើនបានបាត់ខ្លួន។", "ดนตรีเขมรผสมร็อกและป๊อปจากแผ่นเสียงนำเข้า จบลงปี 2518 นักร้องหลายคนหายสาบสูญ"), ENW + "Cambodian_rock_(1960s%E2%80%931970s)", "Wikipedia: Cambodian rock"),
    S(t("Article 5", "មាត្រា ៥", "มาตรา 5"), "Khmer script", "អក្សរខ្មែរ", "อักษรเขมร", t("The official language and script under the constitution. Modern Khmer uses 33 of 35 original consonants; the script also writes Pali.", "ភាសា និងអក្សរផ្លូវការ តាមរដ្ឋធម្មនុញ្ញ។ ភាសាខ្មែរសម័យថ្មីប្រើព្យញ្ជនៈ ៣៣ ក្នុងចំណោម ៣៥ ដើម ហើយអក្សរនេះក៏សរសេរភាសាបាលីដែរ។", "ภาษาและอักษรราชการตามรัฐธรรมนูญ ภาษาเขมรปัจจุบันใช้พยัญชนะ 33 จาก 35 ตัวเดิม อักษรนี้ยังใช้เขียนภาษาบาลี"), "https://www.constituteproject.org/constitution/Cambodia_2008", "Constitution of Cambodia"),
    S(t("Article 43", "មាត្រា ៤៣", "มาตรา 43"), "Theravada Buddhism", "ព្រះពុទ្ធសាសនា", "พุทธศาสนาเถรวาท", t("The constitution makes Buddhism the state religion.", "រដ្ឋធម្មនុញ្ញកំណត់ព្រះពុទ្ធសាសនាជាសាសនារបស់រដ្ឋ។", "รัฐธรรมนูญกำหนดให้พุทธศาสนาเป็นศาสนาประจำชาติ"), "https://www.constituteproject.org/constitution/Cambodia_2008", "Constitution of Cambodia"),
]

FOOD = [
    S(t("Phnom Penh", "ភ្នំពេញ", "พนมเปญ"), "Kuy teav Phnom Penh", "គុយទាវភ្នំពេញ", "ก๋วยเตี๋ยวพนมเปญ", t("Rice-noodle soup in clear pork-bone broth, eaten at breakfast. The Phnom Penh bowl carries the most: minced and sliced pork, ribs, liver, shrimp.", "គុយទាវក្នុងទឹកស៊ុបឆ្អឹងជ្រូកថ្លា ញ៉ាំពេលព្រឹក។ គុយទាវភ្នំពេញមានគ្រឿងច្រើនជាងគេ៖ សាច់ជ្រូកចិញ្ច្រាំ សាច់ចិត ឆ្អឹងជំនីរ ថ្លើម បង្គា។", "ก๋วยเตี๋ยวเส้นข้าวในน้ำซุปกระดูกหมูใส กินตอนเช้า แบบพนมเปญใส่เครื่องมากที่สุด หมูสับ หมูชิ้น ซี่โครง ตับ กุ้ง"), ENW + "Kuy_teav", "Wikipedia: Kuy teav"),
    S(t("Breakfast", "ពេលព្រឹក", "อาหารเช้า"), "Bai sach chrouk", "បាយសាច់ជ្រូក", "บายซัจจรูก (ข้าวหมูย่าง)", t("Rice with thin pork marinated in palm sugar, garlic, coconut milk and fish sauce, grilled over coals.", "បាយជាមួយសាច់ជ្រូកស្តើង ប្រឡាក់ស្ករត្នោត ខ្ទឹមស ខ្ទិះ និងទឹកត្រី អាំងលើរងើក។", "ข้าวกับหมูหั่นบางหมักน้ำตาลโตนด กระเทียม กะทิ น้ำปลา ย่างบนถ่าน"), ENW + "Bai_sach_chrouk", "Wikipedia: Bai sach chrouk"),
    S(t("Breakfast", "ពេលព្រឹក", "อาหารเช้า"), "Num banhchok", "នំបញ្ចុក", "นมบัญเจาะ (ขนมจีนเขมร)", t("Lightly fermented rice noodles with a fish or coconut gravy.", "នំបញ្ចុកមេប្រហុកស្រាលៗ ជាមួយសម្លត្រី ឬសម្លខ្ទិះ។", "เส้นขนมจีนหมักอ่อน ราดน้ำยาปลาหรือกะทิ"), ENW + "Num_banhchok", "Wikipedia: Num banhchok"),
    S(t("Banana leaf", "ស្លឹកចេក", "ใบตอง"), "Fish amok", "អាម៉ុកត្រី", "อาม็อกปลา", t("Fish steamed in a banana-leaf cup with kroeung, coconut cream and egg; one of Cambodia's national dishes.", "ត្រីចំហុយក្នុងកន្ទោងស្លឹកចេក ជាមួយគ្រឿង ខ្ទិះ និងស៊ុត ជាម្ហូបជាតិមួយរបស់កម្ពុជា។", "ปลานึ่งในกระทงใบตองกับเครื่องแกงเกรือง กะทิ และไข่ หนึ่งในอาหารประจำชาติกัมพูชา"), ENW + "Fish_amok", "Wikipedia: Fish amok"),
    S(t("Beef", "សាច់គោ", "เนื้อ"), "Lok lak", "ឡុកឡាក់", "ลกลัก", t("Cubed beef in fish, soy and oyster sauce, tossed with onion and pepper, on lettuce and tomato.", "សាច់គោកាត់ជាដុំតូច ប្រឡាក់ទឹកត្រី ស៊ីអ៊ីវ និងប្រេងខ្យង ឆាជាមួយខ្ទឹមបារាំង និងម្រេច លើសាឡាត់ និងប៉េងប៉ោះ។", "เนื้อหั่นเต๋าในน้ำปลา ซีอิ๊ว ซอสหอยนางรม ผัดหอมใหญ่และพริกไทย วางบนผักกาดกับมะเขือเทศ"), ENW + "Shaking_beef", "Wikipedia: Shaking beef"),
    S(t("Cart", "រទេះ", "รถเข็น"), "Num pang", "នំបុ័ង", "นมปัง (ขนมปังเขมร)", t("A short crisp baguette with pâté, pork or meatballs, pickled carrot and herbs; the bread came with the French.", "នំបុ័ងខ្លីស្រួយ ញាត់ប៉ាតេ សាច់ជ្រូក ឬប្រហិត ការ៉ុតជ្រក់ និងជីរ នំបុ័ងមកជាមួយបារាំង។", "บาแก็ตสั้นกรอบ ใส่ปาเต้ หมู หรือลูกชิ้น แครอทดอง และผัก ขนมปังมากับฝรั่งเศส"), ENW + "Num_pang", "Wikipedia: Num pang"),
    S(t("Paste", "ប្រហុក", "ปลาร้า"), "Prahok", "ប្រហុក", "ปรอฮก", t("Salted, fermented fish paste, about a month in the making, for soups and dips.", "ត្រីប្រឡាក់អំបិល ផ្អាប់ប្រហែលមួយខែ សម្រាប់ស៊ុប និងទឹកជ្រលក់។", "ปลาหมักเกลือราวหนึ่งเดือน ใช้ในแกงและน้ำจิ้ม"), ENW + "Prahok", "Wikipedia: Prahok"),
    S(t("New Year", "ចូលឆ្នាំ", "ปีใหม่"), "Kralan", "ក្រឡាន", "ข้าวหลาม", t("Sticky rice, beans, coconut and palm sugar roasted in bamboo for about 90 minutes.", "បាយដំណើប សណ្តែក ដូង និងស្ករត្នោត ដុតក្នុងបំពង់ឫស្សីប្រហែល ៩០ នាទី។", "ข้าวเหนียว ถั่ว มะพร้าว น้ำตาลโตนด เผาในกระบอกไม้ไผ่ราว 90 นาที"), ENW + "Sticky_rice_in_bamboo", "Wikipedia: Sticky rice in bamboo"),
    S(t("GI 2010", "GI ២០១០", "GI 2553"), "Kampot pepper", "ម្រេចកំពត", "พริกไทยกำปอต", t("Black pepper from Kampot, cracked over kuy teav.", "ម្រេចខ្មៅពីកំពត បុកលើគុយទាវ។", "พริกไทยดำจากกำปอต บดโรยก๋วยเตี๋ยว"), ENW + "Kampot_pepper", "Wikipedia: Kampot pepper"),
    S(t("Sweet", "ផ្អែម", "หวาน"), "Palm sugar", "ស្ករត្នោត", "น้ำตาลโตนด", t("From palm sap: in the bai sach chrouk marinade, in kralan, in stir-fries.", "ពីទឹកត្នោត៖ ក្នុងគ្រឿងប្រឡាក់បាយសាច់ជ្រូក ក្នុងក្រឡាន និងម្ហូបឆា។", "จากน้ำตาลต้นตาล ใช้หมักบายซัจจรูก ใส่ข้าวหลาม และของผัด"), ENW + "Khmer_cuisine", "Wikipedia: Khmer cuisine"),
]

# The four basic hand gestures, as the Ministry of Culture and Fine Arts names them (mcfa.gov.kh/?p=5593).
# Angles: little, ring, middle, index (three joints each), thumb (three), wrist. Negative arches the finger back.
HANDS = [
    {"name": t("Sprout · birth", "ត្រួយ · កំណើត", "หน่อ · การเกิด"), "a": [0.15, 0.3, 0.3, 0.1, 0.3, 0.3, 0.05, 0.3, 0.3, 0.0, 0.3, 0.3, -0.5, -0.3, -0.2, 0.0]},
    {"name": t("Leaf · change", "ស្លឹក · ការវិវត្ត", "ใบ · การเปลี่ยนแปลง"), "a": [-0.3, -0.2, -0.28, -0.16, -0.2, -0.28, -0.04, -0.2, -0.28, 0.08, -0.2, -0.28, 0.25, 0.2, 0.15, -0.15]},
    {"name": t("Flower · growth", "ផ្កា · ការលូតលាស់", "ดอก · การเติบโต"), "a": [-0.3, -0.18, -0.25, -0.15, -0.18, -0.25, -0.02, -0.18, -0.25, 0.45, 0.85, 0.7, -0.55, -0.55, -0.4, -0.1]},
    {"name": t("Falling flower · vanishing, and the seed begins again", "ផ្កាចាស់ទុំជ្រុះ · ការរលត់ ហើយគ្រាប់ចាប់ផ្តើមម្តងទៀត", "ดอกร่วง · การดับสูญ แล้วเมล็ดเริ่มใหม่"), "a": [0.1, 0.2, 0.2, 0.15, 0.2, 0.2, 0.2, 0.25, 0.2, 0.6, 0.9, 0.7, -0.6, -0.6, -0.4, 0.55]},
]
