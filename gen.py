# -*- coding: utf-8 -*-
# BAZA — yekun generator. python3 gen.py → bütün sayt yenidən yaranır.
#
# ┌─────────────────────────────────────────────────────────────┐
# │ VACİB: aşağıdakı SITE_URL-i öz GitHub Pages ünvanınla əvəz  │
# │ et (sonda / OLMASIN), sonra python3 gen.py işə sal.         │
# └─────────────────────────────────────────────────────────────┘
SITE_URL = "https://elgarzynlv.github.io/baza"

import os, html

OUT = "/Users/elgar/Desktop/baza/output"

CSS = """
  body{max-width:680px;margin:0 auto;padding:40px 20px 80px;
    font-family:Georgia,'Times New Roman',serif;font-size:17px;
    line-height:1.65;color:#1a1a1a;background:#fff;}
  @media (prefers-color-scheme: dark){
    body{background:#111;color:#ddd}
    a{color:#9cc}.dim,.def{color:#999}
    input{background:#111;color:#ddd;border-color:#444}
  }
  .site{font-size:1.4em;font-weight:bold;margin-bottom:4px}
  .site a{color:inherit}
  h1{font-size:1.3em;margin-bottom:2px}
  h2{font-size:1.3em;margin-bottom:2px}
  h3{font-size:1.05em;margin:22px 0 8px}
  .dim{color:#666;font-size:.85em}
  a{color:#0645ad;text-decoration:none}
  a:hover{text-decoration:underline}
  .nav{margin:14px 0 28px;font-size:.9em}
  .nav a{margin-right:14px}
  input{width:100%;font:inherit;font-size:.95em;padding:6px 8px;
    border:1px solid #bbb;margin-bottom:16px;}
  .cats{font-size:.9em;margin-bottom:20px}
  .cats a{margin-right:12px}
  .entry-link{display:block;margin-bottom:10px}
  .def{color:#555;font-size:.9em}
  .letter{font-weight:bold;margin:20px 0 8px;font-size:.9em;color:#888}
  .tdef{font-style:italic;margin:14px 0 20px}
  p{margin-bottom:14px}
  .section-label{font-weight:bold;font-size:.85em;margin-top:26px;
    margin-bottom:6px;text-transform:uppercase;letter-spacing:.05em;color:#888}
  .back{display:inline-block;margin-bottom:20px}
  ul{margin:0 0 14px 22px}
  li{margin-bottom:8px}
  .book{margin-bottom:16px}
  .book .def{display:block}
"""

NAV = """<div class="nav">
  <a href="index.html">Məqalələr</a>
  <a href="yollar.html">Oxu yolları</a>
  <a href="kitabxana.html">Kitabxana</a>
  <a href="luget.html">Lüğət</a>
  <a href="manifest.html">Manifest</a>
  <a href="#" id="random">Təsadüfi</a>
</div>"""

def page(title, body, desc, path, h1=None):
    canonical = f"{SITE_URL}/{path}"
    head_title = f'<h1>{h1}</h1>' if h1 else ''
    return f"""<!DOCTYPE html>
<html lang="az">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="az_AZ">
<style>{CSS}</style>
</head>
<body>
<div class="site"><a href="index.html">Baza</a></div>
<div class="dim">Anlayışlar arxivi · fəlsəfə, psixologiya, elm, cəmiyyət</div>
{NAV}
{head_title}{body}
<script>
document.getElementById('random').addEventListener('click',function(ev){{
  ev.preventDefault();
  var P={slugs_js};
  location.href=P[Math.floor(Math.random()*P.length)]+'.html';
}});
</script>
</body>
</html>"""

# ═══════════════════ MƏQALƏLƏR (22) ═══════════════════
A = [
# ─── FƏLSƏFƏ ───
dict(slug="amor-fati", t="Amor Fati", cat="Fəlsəfə",
  d="Taleyini sadəcə qəbul etmək yox — onu sevmək: heç nəyin başqa cür olmasını istəməmək.",
  p=["Nitsşe üçün amor fati (“taleyə məhəbbət”) insanın böyüklüyünün düsturudur. Bu, passiv təslimçilik deyil: stoiklərin “dözümündən” fərqli olaraq, Nitsşe olanı yalnız daşımağı yox, ona “hə” deməyi tələb edir. Ağrı, itki, uğursuzluq — bunlar həyatın xətası deyil, onun mətnidir.",
     "Konsepti sınamaq üçün Nitsşe “əbədi qayıdış” fikir eksperimentini təklif edir: bu həyatı, hər detalı ilə, sonsuz dəfə təkrar yaşamalı olsaydın — dəhşətə gələrdin, yoxsa sevinərdin? Amor fati məhz ikinci cavabın halıdır.",
     "Müasir psixologiyada bu ideyanın əks-sədası “radikal qəbul” anlayışında görünür. Fərq bundadır: qəbul terapevtik texnikadır, amor fati isə ekzistensial mövqedir — həyata verilən estetik qiymət."],
  s="Fridrix Nitsşe — Ecce Homo (1888); Şən Elm, §276",
  r=["nezaret-dixotomiyasi","ressentiment","ustinsan"]),

dict(slug="ressentiment", t="Ressentiment", cat="Fəlsəfə",
  d="Gücsüzlüyün gizli qisası: əldə edə bilmədiyini dəyərsizləşdirərək özünü yüksəltmək.",
  p=["Ressentiment Nitsşenin “Əxlaqın Genealogiyası”nda mərkəzi anlayışdır. Zəif olan, güclüdən açıq qisas ala bilməyəndə, qisası daxilə köçürür: dəyərlər cədvəlini tərsinə çevirir. Güc “pislik”, acizlik “fəzilət” adlanır — və beləcə məğlubiyyət mənəvi qələbə kimi yenidən paketlənir.",
     "Bu, sadə paxıllıqdan dərindir: paxıllıq obyekti istəyir, ressentiment isə obyekti istəməyi özünə qadağan edib onu ləkələyir. “Onsuz da o üzümlər turş idi” — Ezopun tülküsü ressentimentin ilk portretidir.",
     "Maks Şeler sonradan göstərdi ki, ressentiment fərdi hiss deyil, bütöv mədəniyyətlərin əxlaq sistemini formalaşdıra bilən sosial mexanizmdir. Öz mühakimələrimizdə onu tanımaq — intellektual dürüstlüyün ilk imtahanıdır."],
  s="Fridrix Nitsşe — Əxlaqın Genealogiyası (1887); Maks Şeler — Ressentiment (1912)",
  r=["amor-fati","ustinsan","koqnitiv-dissonans"]),

dict(slug="ustinsan", t="Üstinsan", cat="Fəlsəfə",
  d="Tanrının ölümündən sonra insanın qarşısına qoyulan hədəf: öz dəyərlərini özü yaradan varlıq.",
  p=["“Tanrı öldü” — Nitsşenin bu məşhur cümləsi zəfər nidası deyil, diaqnozdur: Avropa öz dəyərlərinin təməlinə inamı itirib, amma hələ bunun nəticələri ilə üzləşməyib. Boşluğu nə ilə doldurmalı? Nitsşenin cavabı Übermensch — üstinsandır: hazır dəyərləri miras almayan, onları özü yaradan insan.",
     "Üstinsan bioloji və ya irqi anlayış deyil — bu, Nitsşenin ən çox təhrif olunmuş fikridir. “Zərdüşt”də üstinsan üç çevrilmənin sonuncusudur: dəvə (daşıyan), şir (rədd edən) və uşaq (yaradan). Yəni yol itaətdən üsyana, üsyandan yaradıcılığa gedir — dağıtmaq yalnız aralıq mərhələdir.",
     "Əks qütbdə “son insan” durur: rahatlıqdan başqa heç nə istəməyən, riskdən, ehtirasdan, böyük məqsəddən qaçan varlıq. Nitsşenin qorxusu üstinsanın gəlməməsi deyildi — son insanın qələbəsi idi. Bu qarşıdurma bu gün də aktualdır: komfort əsrində böyüklük hələ də mümkündürmü?"],
  s="Fridrix Nitsşe — Belə Buyurdu Zərdüşt (1883–85)",
  r=["amor-fati","ressentiment","menaya-irade"]),

dict(slug="absurd", t="Absurd", cat="Fəlsəfə",
  d="İnsanın məna tələbi ilə kainatın susqunluğu arasındakı barışmaz toqquşma.",
  p=["Kamyu üçün absurd nə insandadır, nə dünyada — ikisinin qarşılaşmasındadır. İnsan “niyə?” deyə soruşur; kainat cavab vermir. Absurd məhz bu dialoqsuzluğun adıdır.",
     "Kamyu üç mümkün cavab görür: fiziki intihar (səhnəni tərk etmək), fəlsəfi intihar (dinə və ya ideologiyaya sığınıb sualı boğmaq) və üsyan — absurdu görə-görə yaşamaq. Sizif dağa daşı bilə-bilə qaldırır; Kamyunun məşhur hökmü budur ki, Sizifi xoşbəxt təsəvvür etmək lazımdır.",
     "Absurdizm nihilizmlə qarışdırılmamalıdır: nihilizm “məna yoxdur, deməli heç nə dəyərsizdir” deyir; absurdizm “məna verilməyib — deməli yaşamağın özü etiraz aktıdır” deyir."],
  s="Alber Kamyu — Sizif Mifi (1942)",
  r=["amor-fati","menaya-irade","entropiya"]),

dict(slug="nezaret-dixotomiyasi", t="Nəzarət Dixotomiyası", cat="Fəlsəfə",
  d="Bəzi şeylər bizim əlimizdədir, bəziləri deyil — və müdriklik bu sərhədi düzgün çəkməkdən başlayır.",
  p=["Epiktetin “Əl Kitabçası” bu cümlə ilə açılır: bəzi şeylər bizdən asılıdır (mühakimə, niyyət, istək), bəziləri asılı deyil (bədən, mülk, şöhrət, başqalarının rəyi). Stoisizmin bütün binası bu bir bölgünün üstündə durur.",
     "Qayda sadədir, tətbiqi çətin: enerji yalnız birinci qrupa xərclənməlidir. Asılı olmayanı dəyişməyə çalışmaq — əzabın resepti; asılı olanı laqeyd buraxmaq — məsuliyyətdən qaçış. Epiktet qul idi, sonra sürgün edildi — bu bölgünü nəzəriyyədə yox, təcrübədə yazıb.",
     "Müasir dövrdə bu ideya idrak-davranış terapiyasının (KDT) təməllərindən birinə çevrildi: bizi hadisələr yox, hadisələr haqqında mühakimələrimiz sarsıdır. Amma stoik orijinal daha radikaldır — o, texnika yox, həyat tərzi təklif edir."],
  s="Epiktet — Əl Kitabçası (Enchiridion), §1; Marcus Aurelius — Özümlə Söhbətlər",
  r=["amor-fati","oyrenilmis-acizlik","koqnitiv-dissonans"]),

dict(slug="magara-alleqoriyasi", t="Mağara Alleqoriyası", cat="Fəlsəfə",
  d="Divardakı kölgələri reallıq sanan məhbuslar: bilik — mağaradan çıxmağın ağrısıdır.",
  p=["Platonun “Dövlət”inin VII kitabında insanlar uşaqlıqdan mağarada zəncirlənib: yalnız qarşı divarı görürlər, arxalarındakı ocağın işığında keçən əşyaların kölgələri onların bütün reallığıdır. Kölgələri adlandırırlar, kölgələr üzərində elm qururlar, kölgə bilicilərinə hörmət edirlər.",
     "Biri zəncirdən azad olub çölə çıxanda əvvəl işıq gözünü kor edir — həqiqət ilk təmasda ağrılıdır. Amma alleqoriyanın ən dərin hissəsi sondadır: geri qayıdıb o birilərini azad etmək istəyəndə, məhbuslar ona gülür və Platon əlavə edir — imkan olsa, öldürərlər. Bu sətirlər Sokratın edamına işarədir.",
     "Alleqoriya iki min ildən çoxdur hər dövrün öz mağarasına tətbiq olunur: dünən ideologiya, bu gün alqoritmik lent. Sual dəyişmir: kölgə ilə əşyanı ayırmağın meyarı nədir — və mağaradan çıxdığını haradan bilirsən, bəlkə sadəcə daha böyük mağaradasan?"],
  s="Platon — Dövlət, VII kitab (e.ə. ~375)",
  r=["tesdiq-qerezi","falsifikasiya","overton-penceresi"]),

# ─── PSİXOLOGİYA ───
dict(slug="koqnitiv-dissonans", t="Koqnitiv Dissonans", cat="Psixologiya",
  d="İnancla davranış toqquşanda beynin faktı yox, çox vaxt inancı 'təmir etməsi'.",
  p=["Leon Festinqer 1950-ci illərdə dünyanın sonunu gözləyən bir sektanı müşahidə etdi. Peyğəmbərlik boşa çıxanda üzvlər inancdan əl çəkmədilər — əksinə, daha da fanatikləşdilər: “bizim imanımız dünyanı xilas etdi”. Festinqer bunun adını qoydu: koqnitiv dissonans.",
     "İki uyğunsuz idrak (“siqaret zərərlidir” + “mən siqaret çəkirəm”) psixi gərginlik yaradır. Beyin bu gərginliyi üç yolla azaldır: davranışı dəyişir (nadir hal), inancı dəyişir (“o qədər də zərərli deyil”) və ya yeni bəraət idrakı əlavə edir (“babam 90 il yaşadı”).",
     "Ən vacib nəticə: dissonans azaltma şüursuz baş verir. İnsan özünü rasional hesab edərkən çox vaxt rasionallaşdırır. Öz arqumentlərinə şübhə ilə baxmaq bacarığı buna qarşı yeganə peyvənddir."],
  s="Leon Festinqer — A Theory of Cognitive Dissonance (1957)",
  r=["tesdiq-qerezi","dunning-kruger","ressentiment"]),

dict(slug="tesdiq-qerezi", t="Təsdiq Qərəzi", cat="Psixologiya",
  d="Zehin vəkil kimi işləyir: əvvəl hökm verir, sonra ona sübut yığır.",
  p=["Təsdiq qərəzi — mövcud inancımızı dəstəkləyən məlumatı axtarmaq, yadda saxlamaq və inandırıcı saymaq; ona zidd olanı isə görməzdən gəlmək və ya “şübhəli mənbə” adlandırmaq meylidir. Bu, koqnitiv qərəzlərin bəlkə də ən universalı və ən təhlükəlisidir, çünki özünü tədqiqat kimi göstərir: qərəzli adam da axtarır, oxuyur, “faktlar yığır”.",
     "Klassik nümayiş Uosonun seçmə tapşırığıdır (1960): iştirakçılara “2-4-6” ardıcıllığı verilir və qaydanı tapmaq üçün öz ardıcıllıqlarını sınamağa dəvət olunurlar. Demək olar hamı öz fərziyyəsini təsdiq edəcək misallar sınayır — təkzib edəcək misalları yox. Halbuki qaydanı yalnız təkzib cəhdi aça bilərdi.",
     "Praktik nəticə acıdır: daha çox məlumat qərəzli adamı düzəltmir, əksinə silahlandırır. Yeganə işləyən üsul prosedurdur — öz mövqeyinə qarşı ən güclü arqumenti tapıb ona cavab verməyi vərdiş etmək. Elm bunu institutlaşdırıb: buna falsifikasiya deyilir."],
  s="Peter Wason — On the failure to eliminate hypotheses (1960); Raymond Nickerson — Confirmation Bias (1998)",
  r=["falsifikasiya","koqnitiv-dissonans","magara-alleqoriyasi"]),

dict(slug="dunning-kruger", t="Dunning-Kruger Effekti", cat="Psixologiya",
  d="Bacarıqsızlıq ikiqat lənətdir: insan həm bilmir, həm də bilmədiyini bilmir.",
  p=["1999-cu ildə Devid Danninq və Castin Kruger göstərdilər ki, testlərdə ən aşağı nəticə göstərənlər öz performanslarını ən çox şişirdənlərdir. Səbəb təkəbbür deyil: bir sahədə səriştəni qiymətləndirmək üçün lazım olan bilik, elə həmin sahənin öz biliyidir. Bilmirsənsə — nə qədər bilmədiyini görə bilmirsən.",
     "Effektin ikinci, az xatırlanan tərəfi: həqiqi ekspertlər özlərini bir qədər aşağı qiymətləndirirlər, çünki sahənin nəhəngliyini görürlər və “hamı bunu bilir” deyə düşünürlər.",
     "Populyar mədəniyyətdə effekt çox vaxt “axmaqlar özünə arxayındır” kimi kobudlaşdırılır — bu, tədqiqatın dediyindən dayazdır. Əsl dərs özümüz haqqındadır: hər birimizin xəritədə “bilmədiyimizi bilmədiyimiz” zonalar var."],
  s="Kruger & Dunning — Unskilled and Unaware of It (1999)",
  r=["koqnitiv-dissonans","tesdiq-qerezi"]),

dict(slug="konformizm", t="Konformizm", cat="Psixologiya",
  d="Qrup səhv deyəndə gözünə yox, qrupa inanmaq: sosial təzyiq qavrayışın özünü əyir.",
  p=["Solomon Aşın 1951-ci il eksperimenti sadə idi: iştirakçıya iki kart göstərilir — birində bir xətt, digərində üç; hansı xəttin bərabər olduğunu demək lazımdır. Cavab göz qabağındadır. Amma otaqdakı digər “iştirakçılar” (əslində aktyorlar) növbə ilə eyni yanlış cavabı verirlər. Nəticə: insanların təxminən 75%-i ən azı bir dəfə qrupa qoşulub açıq-aşkar səhvi təkrarladı.",
     "Maraqlısı səbəblərin bölgüsüdür: bəziləri qrupdan seçilməmək üçün bilə-bilə yalan dedi (normativ konformizm), bəziləri isə həqiqətən öz gözünə şübhə etdi (informasion konformizm). İkincisi daha dərindir — təzyiq davranışı yox, qavrayışın özünü dəyişir.",
     "Bir detal ümid verir: qrupda tək bircə nəfər düz cavab verəndə, konformizm dörd dəfə azalırdı. Yəni azlıqda qalan bir səs, sistemin bütün riyaziyyatını dəyişir — susan hər kəs isə təzyiqin bir hissəsinə çevrilir."],
  s="Solomon Asch — Opinions and Social Pressure (1955)",
  r=["koqnitiv-dissonans","serin-banalligi","mehbus-dilemmasi"]),

dict(slug="oyrenilmis-acizlik", t="Öyrənilmiş Acizlik", cat="Psixologiya",
  d="Çıxış yolunun olmadığını öyrənən orqanizm, yol açılanda da onu axtarmır.",
  p=["Martin Seliqmanın 1967-ci il təcrübələrində qaça bilməyəcəyi elektrik təsirinə məruz qalan itlər sonradan — qaçış mümkün olanda belə — cəhd etmirdilər: uzanıb dözürdülər. Nəzarət qrupundakı itlər isə dərhal çıxışı tapırdı. Fərq ağrıda deyildi — ağrının idarəolunmazlığı təcrübəsində idi.",
     "İnsanlarda mexanizm eynidir, amma bir əlavə ilə: biz acizliyi izah edirik. Seliqmanın sonrakı işləri göstərdi ki, həlledici olan izah üslubudur — uğursuzluğu daimi (“həmişə belədir”), universal (“hər şeydə belədir”) və şəxsi (“səbəb mənəm”) sayan adam acizliyi öyrənir; müvəqqəti, lokal və situativ sayan isə yox.",
     "Anlayışın ironik tərəfi sonradan üzə çıxdı: neyrobioloji tədqiqatlar göstərdi ki, beyin üçün ilkin vəziyyət elə passivlikdir — öyrənilən əslində acizlik yox, nəzarətdir. Bu, nəticəni tərsinə çevirir: çarəsizlik defolt haldır, təsir edə bilmək isə qazanılan bacarıq. Deməli sual “niyə təslim oluruq?” deyil — “nəzarəti necə öyrənirik?” olmalıdır."],
  s="Martin Seligman — Helplessness (1975); Maier & Seligman — Learned Helplessness at Fifty (2016)",
  r=["nezaret-dixotomiyasi","menaya-irade","axin"]),

dict(slug="menaya-irade", t="Mənaya İradə", cat="Psixologiya",
  d="İnsanın əsas hərəkətverici qüvvəsi həzz və ya güc deyil — məna axtarışıdır.",
  p=["Viktor Frankl Vyana psixiatrı idi və konslagerlərdən sağ çıxdı. Orada müşahidə etdiyi şey nəzəriyyəsinin təməli oldu: eyni şəraitdə bəziləri sınır, bəziləri dözürdü — və fərq çox vaxt fiziki gücdə yox, insanın nəyinsə və ya kiminsə naminə yaşamasında idi. Nitsşenin sözünü tez-tez təkrarlayırdı: yaşamaq üçün “niyə”si olan, demək olar hər “necə”yə dözər.",
     "Frankl Freydin həzz iradəsinə və Adlerin güc iradəsinə üçüncü yolu qarşı qoydu: mənaya iradə. Buradan logoterapiya doğuldu — mənasızlıq hissini (“ekzistensial boşluq”) nevrozların ayrıca mənbəyi sayan yanaşma. Onun müşahidəsi bu gün daha aktualdır: rifah artdıqca boşluq azalmır, çox vaxt dərinləşir.",
     "Franklın ən sərt tezisi budur: məna verilmir və icad edilmir — tapılır, və məsuliyyət bizdədir. Sual qoyan biz deyilik; həyat bizdən soruşur və hər vəziyyət konkret cavab tələb edir. Xoşbəxtlik isə hədəf kimi qovulanda qaçır — o, mənalı işin kölgəsi kimi öz-özünə gəlir."],
  s="Viktor Frankl — İnsanın Məna Axtarışı (1946)",
  r=["absurd","ustinsan","oyrenilmis-acizlik"]),

dict(slug="axin", t="Axın", cat="Psixologiya",
  d="İnsanın ən yaxşı anları: bacarıqla çətinliyin tarazlaşdığı, mənliyin əridiyi tam qapılma halı.",
  p=["Mihay Çiksentmihayi minlərlə insandan ən xoşbəxt anlarını soruşdu və gözlənilməz nəticə aldı: bu anlar istirahətdə yox, işin içində idi — dağa dırmaşarkən, cərrahiyyə edərkən, şahmat oynayarkən. Ortaq cəhət: fəaliyyətə elə qapılma ki, zaman itir, mənlik unudulur, hərəkət düşüncədən ayrılmır. O, bu hala flow — axın adını verdi.",
     "Axının resepti dəqiqdir: aydın məqsəd, dərhal əks-əlaqə və ən vacibi — çətinliklə bacarığın tarazlığı. Çətinlik bacarıqdan çox olanda narahatlıq, az olanda darıxma yaranır; axın ikisinin arasındakı dar dəhlizdədir. Buradan böyümənin mexanikası çıxır: bacarıq artdıqca dəhliz yuxarı sürüşür — axında qalmaq üçün daim daha çətinə getməlisən.",
     "Fəlsəfi nəticə gözlənilməzdir: xoşbəxtliyin ən dərin forması hedonizmin tam əksidir. Axın rahatlıq deyil — nizamlanmış gərginlikdir; və Çiksentmihayinin qənaəti budur ki, həyatın keyfiyyəti təsadüfə yox, diqqətin hara yönəldilməsinə bağlıdır. Diqqət — psixi enerjidir və onu idarə edən, təcrübəsini idarə edir."],
  s="Mihaly Csikszentmihalyi — Flow: The Psychology of Optimal Experience (1990)",
  r=["oyrenilmis-acizlik","menaya-irade"]),

# ─── ELM ───
dict(slug="entropiya", t="Entropiya", cat="Elm",
  d="Nizamsızlığın ölçüsü — və kainatın yeganə istiqamətli saatı.",
  p=["Termodinamikanın ikinci qanunu deyir: qapalı sistemdə entropiya azalmır. Qırılan fincan öz-özünə bərpa olunmur, soyuyan çay geri qaynamır. Fizikanın demək olar bütün qanunları zamanda geriyə də işləyir — entropiyadan başqa. Zamanın oxunu bizə məhz o verir.",
     "Boltsmanın dərin ideyası: entropiya mistik qüvvə deyil, sadəcə statistikadır. Nizamsız halların sayı nizamlı hallardan astronomik dərəcədə çoxdur; sistem sadəcə ən ehtimallı hala doğru sürüşür.",
     "Həyat isə paradoks kimi görünür: orqanizm lokal nizam yaradır. Ziddiyyət yoxdur — biz açıq sistemik, öz nizamımızı ətrafın entropiyasını artırmaq hesabına alırıq. Şrödingerin ifadəsi ilə, canlı “neqativ entropiya ilə qidalanır”. Yəni nizam — həmişə kiminsə ödədiyi borcdur."],
  s="Ervin Şrödinger — Həyat Nədir? (1944); Karlo Rovelli — Zamanın Nizamı (2017)",
  r=["emergentlik","kepenek-effekti","absurd"]),

dict(slug="emergentlik", t="Emergentlik", cat="Elm",
  d="Bütövün hissələrdə olmayan xassələr qazanması: bir neyron düşünmür, milyardı düşünür.",
  p=["Bir su molekulu “yaş” deyil; yaşlıq trilyonlarla molekulun qarşılıqlı təsirindən doğur. Bir qarışqa demək olar heç nə bilmir; koloniya körpülər qurur, təsərrüfat aparır, müharibə edir. Emergentlik — mürəkkəb sistemlərdə aşağı səviyyədə mövcud olmayan keyfiyyətlərin yuxarı səviyyədə peyda olmasıdır.",
     "Fəlsəfi tərəfi kəskindir: şüur beynin emergent xassəsidirsə, onu neyronlara qədər “parçalayıb” izah etmək mümkündürmü? Reduksionizm ilə emergentizm arasındakı mübahisə müasir şüur fəlsəfəsinin mərkəzindədir.",
     "Praktik dərs: mürəkkəb sistemləri (iqtisadiyyat, cəmiyyət, internet) hissələrinin niyyətləri ilə izah etmək çox vaxt xətadır. Sistem öz məntiqini yaradır — və o məntiq heç kimin planı deyil."],
  s="Filip Anderson — More Is Different (1972)",
  r=["entropiya","kepenek-effekti","mehbus-dilemmasi"]),

dict(slug="falsifikasiya", t="Falsifikasiya", cat="Elm",
  d="Nəzəriyyəni elmi edən sübut oluna bilməsi deyil — təkzib oluna bilməsidir.",
  p=["Karl Popperi narahat edən sual bu idi: niyə Eynşteynin nəzəriyyəsi elmdir, amma astrologiya deyil — axı hər ikisinin “təsdiqləri” var? Cavabı tapdı: fərq təsdiqdə yox, riskdədir. Eynşteyn dedi — işıq Günəşin yanında bu qədər əyilməlidir; əyilməsəydi, nəzəriyyə ölərdi. Astrologiya isə elə qurulub ki, heç nə onu təkzib edə bilmir: hər nəticə “uyğunlaşdırılır”.",
     "Buradan meyar doğur: bir iddia yalnız o halda elmidir ki, onu yanlış çıxara biləcək müşahidəni əvvəlcədən göstərmək mümkün olsun. Təkzibedilməz nəzəriyyə güclü deyil — boşdur; heç nəyi qadağan etmir, deməli heç nə demir.",
     "Bunun fərdi düşüncəyə tətbiqi bəlkə elmə tətbiqindən də qiymətlidir: öz inancına Popper sualını ver — “hansı fakt məni fikrimdən daşındırardı?” Cavab yoxdursa, o inanc bilik deyil, iman rejimində işləyir. Təsdiq qərəzinə qarşı ən güclü intizam məhz budur."],
  s="Karl Popper — Fərziyyələr və Təkziblər (1963); Elmi Kəşfin Məntiqi (1934)",
  r=["tesdiq-qerezi","okkam-ulgucu","magara-alleqoriyasi"]),

dict(slug="okkam-ulgucu", t="Okkam Ülgücü", cat="Elm",
  d="İki izah eyni şeyi açıqlayırsa — sadəsi seçilməlidir: fərziyyələri ehtiyacsız artırma.",
  p=["XIV əsr sxolastı Uilyam Okkamlının adı ilə bağlanan prinsip belə səslənir: varlıqları zərurətdən artıq çoxaltmaq olmaz. Praktikada bu o deməkdir ki, müşahidəni izah edən iki nəzəriyyədən daha az fərziyyəyə söykənəni üstündür — hər əlavə fərziyyə səhv üçün əlavə qapıdır.",
     "Ülgüc gücünü ehtimal nəzəriyyəsindən alır: hər müstəqil fərziyyənin doğru olma ehtimalı vahiddən kiçikdir, deməli fərziyyələr çoxaldıqca izahın ümumi ehtimalı vurula-vurula əriyir. “Açar itib” ilə “açarı gizli təşkilat oğurlayıb, izləri silib, qonşunu da ələ alıb” — ikincisi mümkündür, amma hər halqası ehtimalı bir az da öldürür. Konspiroloji təfəkkürün riyazi diaqnozu budur.",
     "Bir xəbərdarlıq vacibdir: ülgüc həqiqət maşını deyil, seçim qaydasıdır — təbiət bəzən mürəkkəb çıxır və sadə izah səhv olur. Eynşteynə aid edilən düstur tarazlığı düzgün qoyur: hər şey mümkün qədər sadə olmalıdır, amma lazım olandan sadə yox."],
  s="William of Ockham — Summa Logicae (~1323); David Deutsch — The Fabric of Reality (1997)",
  r=["falsifikasiya","tesdiq-qerezi"]),

dict(slug="kepenek-effekti", t="Kəpənək Effekti", cat="Elm",
  d="Determinist sistem belə proqnozlaşdırılmaz ola bilər: kiçik fərq, nəhəng nəticə doğurur.",
  p=["1961-ci ildə meteoroloq Edvard Lorens kompüter simulyasiyasını yarıdan davam etdirmək üçün rəqəmi 0.506127 əvəzinə 0.506 daxil etdi — və tamam başqa hava mənzərəsi aldı. Milyonda bir fərq həftələr içində sistemin bütün gedişatını dəyişmişdi. Sonralar bu, məşhur sualda ifadə olundu: Braziliyada kəpənəyin qanad çalması Texasda qasırğa yarada bilərmi?",
     "Kəşfin dərinliyi bundadır: söhbət təsadüfdən getmir. Lorensin sistemi tam determinist idi — hər addım əvvəlkindən qanunla doğulur. Amma başlanğıc şərtlərə həssaslıq elə güclüdür ki, sonsuz dəqiq ölçmə mümkün olmadığından, uzunmüddətli proqnoz prinsipcə qeyri-mümkün olur. Determinizm və proqnozlaşdırıla bilənlik — sən demə, ayrı şeylərdir.",
     "Bu, elmin özünüdərkində dönüş nöqtəsi idi: Laplasın “hər şeyi bilən ağıl gələcəyi hesablayar” xəyalı dəfn olundu. Hava, iqtisadiyyat, tarix — xaotik sistemlərdə uzaq gələcək qapalıdır, və bu, biliyimizin azlığından yox, reallığın quruluşundandır. Təvazökarlıq burada əxlaqi tövsiyə deyil — riyazi nəticədir."],
  s="Edward Lorenz — Deterministic Nonperiodic Flow (1963); James Gleick — Chaos (1987)",
  r=["entropiya","emergentlik"]),

# ─── CƏMİYYƏT ───
dict(slug="mehbus-dilemmasi", t="Məhbus Dilemması", cat="Cəmiyyət",
  d="Hər kəsin rasional hərəkəti hamının uduzması ilə bitəndə: fərdi ağıl kollektiv axmaqlıq doğura bilir.",
  p=["İki məhbus ayrı-ayrı otaqlarda dindirilir. Hər ikisi sussa — yüngül cəza. Biri o birini satsa — satan azad, susan ağır cəza alır. İkisi də satsa — hər ikisinə orta cəza. Riyazi soyuqluqla baxanda hər biri üçün satmaq “rasionaldır” — nəticədə ikisi də satır və ikisi də sussalar alacaqlarından pis nəticə alırlar.",
     "Bu, sadəcə tapmaca deyil — cəmiyyətin skeletidir: silahlanma yarışı, ekoloji böhran, tıxacda zolaq dəyişmək, vergi ödəməmək. Hər yerdə eyni struktur: fərdi maraq kollektiv marağı yeyir, çünki əməkdaşlığa etibar lazımdır, etibara isə zəmanət yoxdur.",
     "Akselrodun turnirləri bir çıxış göstərdi: oyun təkrarlananda vəziyyət dəyişir. Ən uğurlu strategiya sadə “Tit for Tat” oldu — əməkdaşlıqla başla, sonra qarşındakının hərəkətini güzgülə. Yəni əməkdaşlıq sadəlövhlük deyil — yaddaşı olan sistemlərdə ən rasional seçimdir. Etibar, təkrar görüşəcəyini bilən adamların ixtirasıdır."],
  s="Robert Akselrod — Əməkdaşlığın Təkamülü (1984)",
  r=["emergentlik","konformizm"]),

dict(slug="panoptikon", t="Panoptikon", cat="Cəmiyyət",
  d="İzlənildiyini bilmək — nəzarətçini içəri köçürür: cəza yox, baxış idarə edir.",
  p=["Ceremi Bentam XVIII əsrdə ideal həbsxana layihəsi çəkdi: mərkəzdə qüllə, ətrafda kameralar. Məhbus nəzarətçini görmür, amma hər an görülə biləcəyini bilir. Nəticə: nəzarətçiyə ehtiyac azalır — məhbus özü özünü izləyir.",
     "Mişel Fuko “Nəzarət və Cəza”da göstərdi ki, panoptikon bina deyil, müasir hakimiyyətin sxemidir: məktəb, xəstəxana, ofis — hamısı görünmə vasitəsilə intizam yaradan qurumlardır. Hakimiyyət artıq bədəni cəzalandırmır, davranışı normallaşdırır.",
     "Rəqəmsal dövrdə sxem tərsinə də işləyir: sosial şəbəkələrdə insan izlənməkdən qaçmır — izlənmək üçün yarışır. Şoşana Zuboff bunun adını “nəzarət kapitalizmi” qoydu: baxış artıq intizam yox, xammal istehsal edir."],
  s="Mişel Fuko — Nəzarət və Cəza (1975); Şoşana Zuboff — Nəzarət Kapitalizmi Dövrü (2019)",
  r=["konformizm","overton-penceresi","emergentlik"]),

dict(slug="serin-banalligi", t="Şərin Banallığı", cat="Cəmiyyət",
  d="Ən böyük fəlakətləri çox vaxt canavarlar yox — düşünməkdən imtina etmiş adi adamlar törədir.",
  p=["1961-ci ildə Hanna Arendt Holokostun logistikasını idarə etmiş Adolf Ayxmanın Yerusəlimdəki məhkəməsini izləməyə getdi və gözlədiyi iblisi tapmadı. Qarşısında karyera düşünən, ştamplarla danışan, əmri icra etməyi fəzilət sayan bürokrat vardı. Arendtin qənaəti qalmaqal yaratdı: bu miqyasda şər üçün nifrət belə lazım deyil — düşünməmək kifayətdir.",
     "“Banallıq” şərin kiçikliyi demək deyil — mənbəyinin adiliyidir. Ayxmanda Arendtin gördüyü əsas qüsur təfəkkürsüzlük idi: özgənin yerindən baxa bilməmək, öz hərəkətinin nə olduğunu özündən soruşmamaq. Sistem məsuliyyəti elə xırdalayır ki, hər kəs yalnız “öz işini görür” — və nəticənin sahibi itir.",
     "Arendtin dərsi ittihamnamə yox, güzgüdür: “mən sadəcə vəzifəmi icra edirəm” cümləsi harada başlayırsa, orada ayıq olmaq lazımdır. Aş və Milqram eksperimentləri onun müşahidəsinə laboratoriya təsdiqi verdi — adi insanların əksəriyyəti təzyiq altında vicdanı yox, konteksti dinləyir. Düşünmək, Arendtə görə, əxlaqın son sədd xəttidir."],
  s="Hannah Arendt — Eichmann in Jerusalem: A Report on the Banality of Evil (1963)",
  r=["konformizm","panoptikon","mehbus-dilemmasi"]),

dict(slug="overton-penceresi", t="Overton Pəncərəsi", cat="Cəmiyyət",
  d="İctimai müzakirədə 'normal' sayılanın sərhədləri sabit deyil — və o sərhədlər hərəkət etdirilə bilir.",
  p=["Siyasətşünas Cozef Overtonun sadə müşahidəsi: hər cəmiyyətdə ideyaların yalnız dar bir zolağı “ağlabatan” sayılır — pəncərə. Pəncərədən kənar fikirlər radikaldan ağlasığmaza qədər dərəcələnir. Siyasətçilər adətən pəncərənin içində danışır; pəncərəni isə ideyaların uzunmüddətli dövriyyəsi hərəkət etdirir.",
     "Mexanizm iki istiqamətdə işləyir. Dünən ağlasığmaz sayılan (məsələn, qadınların səsvermə hüququ) mərhələ-mərhələ radikala, mübahisəliyə, məqbula və nəhayət normaya çevrilə bilir — bu, azadlıqların tarixidir. Amma eyni mexanizmlə qəddarlıq da normallaşdırıla bilir: hər addım əvvəlkinə görə “bir az” fərqli olduğundan, cəmiyyət sürüşməni hiss etmir.",
     "Anlayışın praktik dəyəri diaqnostikadır: “bu, on il əvvəl deyilə bilərdimi?” sualı pəncərənin hara sürüşdüyünü göstərir. Pəncərə özü nə yaxşıdır, nə pis — o, sadəcə alətdir. Sual həmişə eynidır: onu kim, hansı istiqamətə və nəyin hesabına hərəkət etdirir — və sən bunu görürsənmi?"],
  s="Joseph Overton / Mackinac Center (1990-cı illər); Joshua Treviño-nun dərəcələndirməsi",
  r=["konformizm","magara-alleqoriyasi","panoptikon"]),
]

slugs_js = "[" + ",".join(f"'{a['slug']}'" for a in A) + "]"
by_slug = {a["slug"]: a for a in A}
CATS = ["Fəlsəfə","Psixologiya","Elm","Cəmiyyət"]

os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    if f.endswith((".html",".xml",".txt")): os.remove(os.path.join(OUT,f))

# ── Məqalə səhifələri ──
for a in A:
    rel = " · ".join(f'<a href="{r}.html">{by_slug[r]["t"]}</a>' for r in a["r"] if r in by_slug)
    body = f"""<a class="back" href="index.html">← Bütün məqalələr</a>
<h1>{a['t']}</h1>
<div class="dim">{a['cat']}</div>
<div class="tdef">{a['d']}</div>
{''.join(f'<p>{p}</p>' for p in a['p'])}
<div class="section-label">Mənbə</div>
<p>{a['s']}</p>
<div class="section-label">Əlaqəli</div>
<p>{rel}</p>"""
    with open(f"{OUT}/{a['slug']}.html","w",encoding="utf-8") as f:
        f.write(page(f"{a['t']} nədir? — Baza", body, a["d"], f"{a['slug']}.html"))

# ── İndeks ──
items_html = ""
letter = ""
for a in sorted(A, key=lambda x: x["t"]):
    L = a["t"][0].upper()
    if L != letter:
        letter = L
        items_html += f'<div class="letter">{L}</div>\n'
    items_html += (f'<a class="entry-link" data-cat="{a["cat"]}" data-text="{html.escape((a["t"]+" "+a["d"]).lower())}" '
                   f'href="{a["slug"]}.html">{a["t"]} <span class="def">— {a["d"]}</span></a>\n')

index_body = f"""<input id="q" type="text" placeholder="axtar..." aria-label="Axtarış">
<div class="cats">
  <a href="#" data-f="">Hamısı ({len(A)})</a>
  {' '.join(f'<a href="#" data-f="{c}">{c} ({sum(1 for a in A if a["cat"]==c)})</a>' for c in CATS)}
</div>
<div id="list">
{items_html}</div>
<script>
(function(){{
  var q=document.getElementById('q'),cat='';
  function apply(){{
    var f=q.value.trim().toLowerCase();
    document.querySelectorAll('.entry-link').forEach(function(a){{
      var ok=(!cat||a.dataset.cat===cat)&&(!f||a.dataset.text.indexOf(f)>-1);
      a.style.display=ok?'':'none';
    }});
    document.querySelectorAll('.letter').forEach(function(h){{
      var n=h.nextElementSibling,show=false;
      while(n&&!n.classList.contains('letter')){{
        if(n.style.display!=='none')show=true;
        n=n.nextElementSibling;
      }}
      h.style.display=show?'':'none';
    }});
  }}
  q.addEventListener('input',apply);
  document.querySelectorAll('.cats a').forEach(function(a){{
    a.addEventListener('click',function(ev){{ev.preventDefault();cat=a.dataset.f;apply();}});
  }});
}})();
</script>"""
with open(f"{OUT}/index.html","w",encoding="utf-8") as f:
    f.write(page("Baza — fəlsəfə, psixologiya və elm anlayışları azərbaycanca",
                 index_body,
                 "Fəlsəfə, psixologiya, elm və cəmiyyət anlayışlarının Azərbaycan dilində arxivi: entropiya, absurd, ressentiment, koqnitiv dissonans və s.",
                 "index.html"))

# ── Manifest ──
manifest = """<a class="back" href="index.html">← Məqalələr</a>
<h1>Manifest</h1>
<div class="dim" style="margin-bottom:18px">Niyə bu baza var</div>
<p>Bu səhifələr sənin yerinə düşünmək üçün deyil — sənin düşünməyinə başlanğıc olmaq üçün yazılıb.</p>
<p>Azərbaycan dilində ciddi fikrə gedən yol həmişə başqa dillərdən keçib: fəlsəfəni rusca, psixologiyanı ingiliscə, dərinliyi tərcümədə axtarmışıq. Bu baza kiçik bir etirazdır — sübut ki, entropiya haqqında, ressentiment haqqında, absurd haqqında öz dilimizdə dərin danışmaq mümkündür.</p>
<p>Burada üç qayda var. <b>Birincisi:</b> hər məqalə mənbəyə söykənir — burda fikir yox, fikrin ünvanı satılır; oxu, sonra get orijinalı tap. <b>İkincisi:</b> heç bir məqalə son söz iddiasında deyil. <b>Üçüncüsü:</b> burda bəzək yoxdur — mətn və mənbə. Diqqətini alan hər şey düşüncəndən oğurlanıb.</p>
<p>Bu baza reklam olunmayacaq. Səni bura alqoritm gətirməyib — sual gətirib. Deməli, düzgün yerdəsən.</p>
<p>Əgər bu sətirləri illər sonra oxuyursansa: bunlar yazılanda müəllif hardan başlayacağını bilməyən bir tələbə idi. Başlamaq — davam etməyin yeganə şərtidir. Sən də öz bazanı qur.</p>
<p class="dim">— Baza, Bakı</p>"""
with open(f"{OUT}/manifest.html","w",encoding="utf-8") as f:
    f.write(page("Manifest — Baza", manifest, "Bu bazanın niyə mövcud olduğu haqqında.", "manifest.html"))

# ── Oxu yolları ──
def yol(n, ad, tesvir, maddeler):
    lis = "".join(f'<li><a href="{s}.html">{by_slug[s]["t"]}</a> — {izah}</li>' for s, izah in maddeler)
    return f'<h3>{n}. {ad}</h3><p class="def">{tesvir}</p><ul>{lis}</ul>'

yollar = f"""<a class="back" href="index.html">← Məqalələr</a>
<h1>Oxu yolları</h1>
<div class="dim" style="margin-bottom:18px">Hardan başlamalı bilmirsənsə — hazır marşrutlar. Hər yol 3-4 məqalədir, ardıcıllıq qəsdəndir.</div>
{yol(1,"Başlanğıc nöqtəsi","Bazaya ilk dəfə gələnlər üçün: üç sahədən üç fundamental fikir.",
  [("magara-alleqoriyasi","gördüyün, olan deyil"),
   ("koqnitiv-dissonans","beynin öz-özünü aldatması"),
   ("nezaret-dixotomiyasi","nəyin sənin əlində olduğu")])}
{yol(2,"Öz zehnini tanı","Beyin həqiqət üçün yox, sağ qalmaq üçün optimallaşıb. Sübutlar:",
  [("koqnitiv-dissonans","inanc faktı necə əzir"),
   ("tesdiq-qerezi","niyə həmişə haqlı çıxırsan"),
   ("dunning-kruger","bilməməyin ikiqat lənəti"),
   ("konformizm","qrupun gözü ilə görmək")])}
{yol(3,"Necə yaşamalı","Fəlsəfənin ən qədim sualına dörd cavab — stoiklərdən ekzistensialistlərə:",
  [("nezaret-dixotomiyasi","Epiktetin xəritəsi"),
   ("amor-fati","Nitsşenin cavabı"),
   ("absurd","Kamyunun üsyanı"),
   ("menaya-irade","Franklın sübutu")])}
{yol(4,"Həqiqəti necə axtarmalı","Bilik nədir, nə deyil və özünü aldatmadan necə yoxlamalı:",
  [("magara-alleqoriyasi","problemin qoyuluşu"),
   ("tesdiq-qerezi","daxili maneə"),
   ("okkam-ulgucu","seçim qaydası"),
   ("falsifikasiya","Popperin həll üsulu")])}
{yol(5,"Fərd, sistem, cəmiyyət","Milyonlarla fərdi qərar bir yerə gələndə nə baş verir:",
  [("emergentlik","bütöv hissələrdən böyükdür"),
   ("mehbus-dilemmasi","rasionallıq niyə əməkdaşlığı öldürür"),
   ("konformizm","qrup fərdi necə əridir"),
   ("serin-banalligi","düşünməməyin qiyməti")])}
{yol(6,"Nizam və xaos","Kainatın ən böyük mövzusu — üç pəncərədən:",
  [("entropiya","niyə hər şey dağılır"),
   ("kepenek-effekti","niyə gələcək qapalıdır"),
   ("emergentlik","xaosdan nizam necə doğur")])}
{yol(7,"Nitsşe xətti","Bir filosofun daxili məntiqi — diaqnozdan üfüqə:",
  [("ressentiment","xəstəliyin diaqnozu"),
   ("amor-fati","dərman"),
   ("ustinsan","üfüq")])}"""
with open(f"{OUT}/yollar.html","w",encoding="utf-8") as f:
    f.write(page("Oxu yolları — Baza", yollar, "Hazır oxu marşrutları: hardan başlamalı.", "yollar.html"))

# ── Kitabxana ──
books = [
("Platon — Dövlət (e.ə. ~375)","Mağara alleqoriyası VII kitabdadır. Hamısını oxumaq şərt deyil — VI-VII kitablar özü ayrıca əsər kimi işləyir. Fəlsəfə tarixinin ən çox istinad olunan mətni."),
("Epiktet — Əl Kitabçası / Enchiridion (~125)","Cəmi 30-40 səhifə. Fəlsəfəyə girişin bəlkə də ən qısa yolu: birinci abzas nəzarət dixotomiyasıdır və ondan sonra hər şey nəticədir."),
("Fridrix Nitsşe — Əxlaqın Genealogiyası (1887)","Nitsşeyə buradan başla, “Zərdüşt”dən yox: üç oçerk, aydın arqument. Ressentiment anlayışının doğulduğu yer."),
("Fridrix Nitsşe — Belə Buyurdu Zərdüşt (1883–85)","Nitsşenin ən məşhur və ən çətin kitabı — ona görə də son oxunmalıdır, ilk yox. Üç çevrilmə (dəvə-şir-uşaq) birinci hissədədir."),
("Fridrix Nitsşe — Şən Elm (1882)","Fraqmentar üslub: hər gün 2-3 fraqment oxumaq üçün ideal. §341 (əbədi qayıdış) və §276 (amor fati) bu bazanın mənbələrindəndir."),
("Alber Kamyu — Sizif Mifi (1942)","İncə kitabdır, amma tez oxunmur. Fəlsəfi hazırlıq tələb etmir — dürüstlük tələb edir."),
("Viktor Frankl — İnsanın Məna Axtarışı (1946)","İki hissə: lager xatirələri və logoterapiyanın icmalı. Bir oturuma oxunur, illərlə işləyir. Bazadakı ən 'praktik' kitab bəlkə də budur."),
("Karl Popper — Fərziyyələr və Təkziblər (1963)","Elm-qeyri-elm sərhədi haqqında əsas mətn. Birinci fəsil müstəqil oxuna bilir və falsifikasiya məqaləsinin mənbəyidir."),
("Leon Festinqer — A Theory of Cognitive Dissonance (1957)","Akademik mətndir; hazır deyilsənsə, “When Prophecy Fails” kitabından başla — sekta hekayəsi oradadır və roman kimi oxunur."),
("Daniel Kahneman — Sürətli və Yavaş Düşünmə (2011)","Koqnitiv qərəzlər sahəsinin ensiklopediyası. Uzundur — bölmə-bölmə oxu, yoxsa hamısı qarışacaq."),
("Mihaly Csikszentmihalyi — Flow (1990)","Axın anlayışının mənbəyi. İlk üç fəsil əsas ideyanı verir; qalanı tətbiqlərdir. Populyar psixologiyanın nadir hallarda ciddi qalan nümunəsi."),
("Martin Seligman — Helplessness (1975)","Öyrənilmiş acizliyin ilk sistemli izahı. Müasir baxış üçün Maier & Seligman-ın 2016 məqaləsi (Learned Helplessness at Fifty) ilə birlikdə oxu."),
("Ervin Şrödinger — Həyat Nədir? (1944)","Fizikin bioloqlara mühazirəsi; DNT kəşfindən əvvəl genetik kodu proqnozlaşdıran kitab. Qısadır."),
("Karlo Rovelli — Zamanın Nizamı (2017)","Müasir fizikanın zaman haqqında bildiklərini şeir kimi yazır. Entropiya məqaləsindən sonra buradan davam et."),
("James Gleick — Chaos (1987)","Xaos nəzəriyyəsinin doğulma hekayəsi — Lorensdən Mandelbrota. Elmi-populyar janrın klassiki, riyaziyyat tələb etmir."),
("Robert Akselrod — Əməkdaşlığın Təkamülü (1984)","Məhbus dilemmasının davamı: eqoistlər dünyasında əməkdaşlıq necə yaranır? Oyun nəzəriyyəsinin ən oxunaqlı kitabı."),
("Hannah Arendt — Eichmann in Jerusalem (1963)","Reportaj kimi başlayır, fəlsəfə kimi bitir. Oxumazdan əvvəl bil: kitab ətrafındakı mübahisə hələ də davam edir — bu, onun gücünün əlamətidir."),
("Mişel Fuko — Nəzarət və Cəza (1975)","Çətin müəllifin nisbətən oxunaqlı kitabı. İlk fəsildəki edam səhnəsindən qorxma — kitab məhz o dəhşətin niyə yoxa çıxdığını izah edir."),
]
kitabxana = f"""<a class="back" href="index.html">← Məqalələr</a>
<h1>Kitabxana</h1>
<div class="dim" style="margin-bottom:18px">Bazadakı bütün mənbələr — şəxsi qeydlərlə</div>
{''.join(f'<div class="book"><b>{b}</b><span class="def">{n}</span></div>' for b,n in books)}"""
with open(f"{OUT}/kitabxana.html","w",encoding="utf-8") as f:
    f.write(page("Kitabxana — Baza", kitabxana, "Bazadakı bütün mənbə kitablar, oxu qeydləri ilə.", "kitabxana.html"))

# ── Lüğət ──
terms = [
("axın","ing. flow","“Cərəyan” fiziki, “transa girmə” mistik çalar daşıyır. “Axın” həm hərfi tərcümədir, həm hadisənin hissini verir — zamanın axıb getməsi."),
("emergentlik","ing. emergence","“Meydanaçıxma” süni səslənir, “yaranma” isə mənanı itirir — yeni keyfiyyətin gözlənilməzliyini vermir. Beynəlxalq kök saxlanılıb."),
("falsifikasiya","ing. falsifiability","“Təkzibolunma” mümkün qarşılıqdır və mətn içində işlədilir, amma termin kimi beynəlxalq forma saxlanılıb — Popper ədəbiyyatında axtarışı asanlaşdırmaq üçün."),
("konformizm","ing. conformity","“Uyğunlaşma” neytraldır və təkamüli adaptasiya ilə qarışır; konformizm konkret hadisədir — qrup təzyiqi altında mühakimənin əyilməsi."),
("koqnitiv qərəz","ing. cognitive bias","“Meyillilik” çox yumşaqdır, “xəta” isə çox sərt — bias sistematikdir, amma həmişə səhv nəticə vermir. “Qərəz” ikisinin arasını tutur."),
("öyrənilmiş acizlik","ing. learned helplessness","“Çarəsizlik” də mümkündür, amma “acizlik” subyektin daxili halını daha dəqiq verir — çarə yox deyil, çarə axtarışı sönüb."),
("ressentiment","fr./alm.","Tərcümə edilmir — Nitsşe özü də almancada fransız sözünü saxlayıb, çünki “küskünlük” və ya “kin” anlayışın yalnız yarısını verir."),
("təslimçilik","ing. resignation","“Təslim olma” hərbi çalar daşıyır; burada ekzistensial mövqe nəzərdə tutulur — mübarizədən daxili imtina."),
("üstinsan","alm. Übermensch","“Superinsan” komiks çaları daşıyır, “fövqəlinsan” ağır kalkadır. “Üstinsan” türk dilləri ənənəsinə uyğundur və orijinalın quruluşunu saxlayır."),
("üsyan","fr. révolte, Kamyuda","“Qiyam” siyasi, “etiraz” zəifdir. Kamyunun révolte-u metafizik aktdır — “üsyan” bu ağırlığı daşıyır."),
]
luget = f"""<a class="back" href="index.html">← Məqalələr</a>
<h1>Lüğət</h1>
<div class="dim" style="margin-bottom:18px">Bu bazada işlədilən terminlər və seçimlərin əsaslandırması. Azərbaycan dilində bu terminlərin çoxunun oturuşmuş qarşılığı yoxdur — burada seçim edilir və səbəbi yazılır.</div>
{''.join(f'<div class="book"><b>{t}</b> <span class="dim">({e})</span><span class="def">{n}</span></div>' for t,e,n in terms)}"""
with open(f"{OUT}/luget.html","w",encoding="utf-8") as f:
    f.write(page("Lüğət — Baza", luget, "Fəlsəfi-psixoloji terminlərin Azərbaycan dilində qarşılıqları və əsaslandırmalar.", "luget.html"))

# ── sitemap.xml + robots.txt ──
pages = ["index.html","manifest.html","yollar.html","kitabxana.html","luget.html"] + [a["slug"]+".html" for a in A]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for pth in pages:
    sm += f"  <url><loc>{SITE_URL}/{pth}</loc></url>\n"
sm += "</urlset>\n"
with open(f"{OUT}/sitemap.xml","w",encoding="utf-8") as f: f.write(sm)
with open(f"{OUT}/robots.txt","w",encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

print(f"Hazır: {len(A)} məqalə, {len(pages)} səhifə + sitemap.xml + robots.txt")
