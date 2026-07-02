---
name: saas-inceleme
description: >
  Referans: SaaS abonelik sözleşmelerinin, abonelik anlaşmalarında en çok önem
  taşıyan şartlara — otomatik yenileme mekaniği, fiyat artışı, veri taşınabilirliği,
  çalışma süresi SLA'ları ve alt işleyen hakları — dikkat ederek incelenmesi. Bir
  SaaS veya abonelik sözleşmesi tespit edildiğinde /ticari-hukuk:sozlesme-inceleme
  tarafından yüklenir.
user-invocable: false
---

# SaaS / Abonelik Sözleşmesi İncelemesi

## Dosya bağlamı

**Dosya bağlamı.** Pratik düzeyi CLAUDE.md'deki `## Dosya çalışma alanları`nı kontrol
et. `Etkin` `✗` ise (şirket-içi kullanıcılar için varsayılan), bu paragrafın geri
kalanını atla — skill'ler pratik düzeyi bağlamı kullanır ve dosya makinesi görünmez.
Etkinse ve aktif bir dosya yoksa sor: "Bu hangi dosya için? `/ticari-hukuk:dosya-
calisma-alani gecis <slug>` çalıştırın ya da `pratik-duzeyi` deyin." Aktif dosyanın
`matter.md`'sini dosyaya özgü bağlam ve geçersizlemeler için yükle. Çıktıları dosya
klasörüne yaz:
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/matters/<dosya-slug>/`.
`Çapraz-dosya bağlamı` `açık` olmadıkça başka bir dosyanın dosyalarını asla okuma.

---

## Amaç

SaaS sözleşmelerinin tek seferlik satıcı sözleşmelerinden farklı bir risk profili
vardır. Paralar yenilemeler boyunca birikir, veri birikir ve geçiş maliyeti her ay
büyür. Bu skill bunu göz önünde bulundurarak inceler.

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
standart oyun kitabı kontrolünü çalıştırır ve abonelik anlaşmalarında en sert
ısıran şartlar üzerine SaaS'a özgü bir katman ekler.

## Yargı çevresi varsayımı

SaaS şartları (otomatik yenileme bildirim gereksinimleri, fiyat artış tavanları,
veri taşınabilirliği zorunlulukları, alt işleyen kuralları) yargı çevresine
duyarlıdır — Türkiye'de tüketici hukuku (TKHK) ve AB kuralları önemli ölçüde
farklılaşır ve bazı yargı çevreleri özel sözleşme şartlarını geçersiz kılan
otomatik-yenileme kanunlarına sahiptir. Bu inceleme,
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
ekibin pozisyonlarını uygular, bunlar orada kayıtlı uygulanacak hukuku varsayar.
Sözleşme farklı bir uygulanacak hukuk seçiyorsa, veya anlaşma kanuni geçersiz
kılmaların olduğu yargı çevrelerine (ör. AB tabanlı kullanıcılar) yayılıyorsa,
işaretleyin — analiz yazıldığı gibi aktarılmayabilir.

> **Sessiz tamamlama yok.** Yapılandırılmış hukuki araştırma aracına (Lexpera,
> Kazancı veya büro platformu) yapılan bir sorgu, anlaşmayı etkileyebilecek kanuni
> bir geçersiz kılma (otomatik-yenileme kanunu, veri-taşınabilirliği zorunluluğu,
> tüketici-koruma kuralı) için az veya hiç sonuç döndürmezse, bulunanı raporla ve
> dur. Boşluğu sormadan web aramasından veya model bilgisinden DOLDURMA. Şunu de:
> "Arama [araç]'tan [N] sonuç döndürdü. [Yargı çevresi / kural] için kapsam zayıf
> görünüyor. Seçenekler: (1) arama sorgusunu genişlet, (2) farklı bir araştırma
> aracı dene, (3) web'de ara — sonuçlar güvenmeden önce birincil kaynağa karşı
> kontrol edilmesi gereken `[web araması — doğrula]` etiketiyle gelecek, veya (4)
> doğrulanmamış olarak işaretle ve dur. Hangisini istersiniz?" Daha düşük güvenli
> kaynakları kabul edip etmeyeceğine avukat karar verir.
>
> **Kaynak atfı.** İnceleme bir kanun, yönetmelik veya içtihat alıntıladığında
> (ör. sözleşme şartlarını geçersiz kılan bir otomatik-yenileme kanunu), atfı
> etiketle: bağlı bir hukuki araştırma bağlayıcısından alınan atıflar için
> `[Lexpera]`, `[Kazancı]`, `[UYAP]`, `[mevzuat.gov.tr]` veya MCP araç adı; web
> araması atıfları için `[web araması — doğrula]`; eğitim verisinden hatırlanan
> atıflar için `[model bilgisi — doğrula]`; karşı taraf taslağından veya kurum
> dosyalarından gelen atıflar için `[kullanıcı verdi]`. `doğrula` etiketli atıflar
> daha yüksek uydurma riski taşır ve önce kontrol edilmelidir. Etiketleri asla
> çıkarma veya birleştirme.

## Oyun kitabını yükle

**Hangi taraf?** Oyun kitabını uygulamadan önce, bu SaaS sözleşmesi için şirketin
hangi tarafta olduğunu belirle. Genellikle bellidir: karşı taraf size platformunu
satan bir SaaS satıcısıysa, satın alma-tarafındasınızdır. Siz SaaS satıcısıysanız ve
karşı taraf müşterinizse, satış-tarafındasınızdır. Belli değilse (bir bayilik
düzenlemesi, beyaz-etiket bir anlaşma), sor: "[Şirket] bu sözleşmede hangi taraf —
satıcı mı müşteri mi?" Eşleşen oyun kitabı bölümünü (`### Satış-tarafı oyun kitabı`
veya `### Satın alma-tarafı oyun kitabı`) yapılandırmadan oku. Çıktıda hangi tarafın
uygulandığını not et. Eşleşen taraf `[Yapılandırılmadı]` ise, dur ve kullanıcıya bu
inceleme devam edebilmeden önce `/ticari-hukuk:ilk-kurulum --side <taraf>`
çalıştırmasını söyle.

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'yi önce
oku. Eşleşen taraf için genel oyun kitabı (sorumluluk, tazminat, fesih, uygulanacak
hukuk) tam olarak uygulanır — satici-inceleme skill'inden tüm standart kontrolleri
çalıştır.

Sonra bir `## Oyun Kitabı` → eşleşen taraf → `SaaS pozisyonları` bölümü ara. Ekibin
otomatik-yenileme bildirim pencereleri, kabul edilebilir fiyat artışları, veri
ihracat hakları, SLA eşikleri, alt işleyen onay hakları ve durdurma (deprecation)
bildirimi üzerindeki pozisyonlarını burada kaydettiği yerdir. Bu skill bu şartlar
için varsayılanlarla gelmez — doğru rakamlar anlaşma büyüklüğüne, satıcı kaldıracına
ve ekibin risk toleransına göre değişir.

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` bu
incelemede ortaya çıkan SaaS'a özgü bir şartı ele almıyorsa, sor:

> Oyun kitabınız [şart — ör. "kabul edilebilir maksimum otomatik-yenileme bildirim
> penceresi" veya "satıcının anonimleştirilmiş türevleri elinde tutmasının kabul
> edilebilir olup olmadığı"]'nı kapsamıyor. Ekibinizin pozisyonu ne? Bunu
> `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye
> eklerim.

Cevabı kaydet ve devam et.

## SaaS'a özgü katman

Aşağıdaki her kategori için, sözleşmede bulduğunuzu listeleyin ve
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'deki
ekibin pozisyonuyla karşılaştırın. Bu skillden sabit-kodlanmış eşikler uygulamayın.

### 1. Otomatik yenileme mekaniği

Bir SaaS anlaşmasının ters gitmesinin en yaygın yolu: kimse yenileme bildirim
penceresini fark etmiyor ve daha yüksek bir fiyatla başka bir yıl için kilitleniyoruz.

Her öğeyi kontrol edin ve
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'deki
ekibin `SaaS pozisyonları`'yla karşılaştırın:

- **Yenileme süre uzunluğu** (ör. ilkiyle aynı, daha uzun, çok yıllı otomatik-dönüşüm)
- **İptal için bildirim penceresi** (yenilemeden önceki gün sayısı)
- **Bildirim yöntemi** (e-posta, hukuka yazılı bildirim, yalnızca portal, iadeli
  taahhütlü mektup)
- **Yenilemede fiyat** (aynı, TÜFE-tavanlı, o anki liste, tavansız takdiri)

**Çıkarın ve kaydedin** herhangi bir kalem işaretlenmemiş olsa bile tam yenileme
tarihini ve bildirim penceresini. Bu, yenileme-takibi skill'ini besler.

### 2. Fiyat artışı

Her öğeyi
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye karşı
kontrol edin:

- **Yıllık artış oranı** (sabit %, TÜFE, tavansız vb.)
- **Kullanım aşım fiyatlandırması** (yayınlanmış fiyat cetveli, prim oran, belirsiz)
- **"Ücret" kapsamı** (yalnızca abonelik vs. geniş tanımlı "ek hizmetler")

### 3. Veri taşınabilirliği ve çıkış

Bu satıcıdan ayrıldığımızda (ayrılırsak değil), verimizi çıkarabilir miyiz? Her
öğeyi
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye karşı
kontrol edin:

- **İhracat formatı** (açık/standart, tescilli-ama-belgeli, "ticari olarak makul")
- **İhracat erişilebilirliği** (kendi kendine her zaman, süre boyunca talep üzerine,
  yalnızca fesihte)
- **Fesih sonrası erişim** (fesihten sonra ihracat için müsait gün sayısı)
- **İhracat maliyeti** (ücretsiz, zaman-malzeme, GB veya kayıt başına)
- **Silme sertifikasyonu** (talep üzerine sertifikalı, yok, satıcı türevleri elinde
  tutuyor)

Satıcının "anonimleştirilmiş" veya "toplulaştırılmış" türevleri elinde tutması
önemli bir pozisyondur —
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'deki
ekip duruşunu teyit edin ve her iki yönde de işaretleyin.

### 4. Çalışma süresi ve SLA

Yalnızca iş gerçekten bu hizmetin çalışır durumda olmasına bağımlıysa önemlidir.
Güzel-olur bir araçsa, bu bölümü atlayın — bir anket aracı için SLA'lar üzerinde
müzakere kapasitesi harcamayın.

Her öğeyi
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye karşı
kontrol edin:

- **Çalışma süresi taahhüdü** (yüzde, veya "ticari olarak makul çaba")
- **Ölçüm periyodu** (aylık, üç aylık, yıllık)
- **Çözüm yolu** (hizmet kredileri — nasıl hesaplandığı, tavanlı olup olmadığı,
  tek çözüm yolu olup olmadığı)
- **Planlı bakım istisnaları** (tanımlı pencere, önceden bildirim, sınırsız)
- **Kredi-tek-çözüm-yolu** etkileşimi sorumluluk tavanıyla

### 5. Alt işleyenler

Bu bir veri koruma sorunudur ama SaaS'a özgüdür çünkü alt işleyen listesi aboneliğin
yaşam süresi boyunca *değişir*.

Her öğeyi
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye karşı
kontrol edin:

- **Mevcut liste** (yayınlanmış, talep üzerine, mevcut değil)
- **Değişiklik bildirimi** (önceden bildirim süresi, veya yok)
- **İtiraz hakları** (engelleyici, bildirim-ve-fesih, yalnızca bildirim, yok)

### 6. Hizmet değişiklikleri ve durdurma (deprecation)

SaaS satıcıları ürünlerini değiştirir. Genellikle sorun yok. Bazen satın aldığınız
şeyi durdururlar.

Her öğeyi
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye karşı
kontrol edin:

- **Esaslı olumsuz değişiklikler** (esaslı bozulmada fesih hakkı, yalnızca bildirim,
  kısıtlanmamış)
- **Ekibin bel bağladığı özellikler için durdurma bildirim süresi**
- **Değiştirmede özellik paritesi** (aynı fiyat kademesi, daha yüksek kademe)

## Yapay zeka ve makine öğrenmesi hakları

**YZ/ML veri hakları karar prosedürü.** Yalnızca bir YZ eğitim maddesi var mı diye
bakmayın. SaaS sözleşmelerindeki #1 yükselen müzakere noktası, yapısal olarak
tek-satırlık bir varlık kontrolünden fazlasıdır. Şunları işleyin:

1. **Açık verilme.** Sözleşme, satıcıya Müşteri Verisini / Müşteri İçeriğini /
   Kullanım Verisini YZ eğitimi, model iyileştirme veya ML geliştirmesi için
   kullanma hakları açıkça veriyor mu? Satın alma-tarafı: bu genellikle bir
   HAYIR'dır — müşteri verisinin satıcının modellerini eğitmesi, müşterinin
   satıcının ürününü sübvanse etmesi ve muhtemelen rekabetçi bilgiyi sızdırması
   anlamına gelir. Satış-tarafı: bu elde ederseniz gelirdir, kötüye kullanırsanız
   itibar riskidir.
2. **Politika yoluyla örtük verilme.** Sözleşme satıcının gizlilik politikasını veya
   hizmet şartlarını atıfla birleştiriyor mu? Satıcı tek taraflı bir politika
   güncellemesiyle eğitim hakları ekleyebilir mi? Kontrol edin: "Taraflar,
   Sağlayıcının zaman zaman güncellenen Gizlilik Politikasını kabul eder" gerçekleşmek
   üzere olan bir eğitim-hakları verilmesidir. Ayrıca "hizmet iyileştirme" veya
   "analitik" her-şeyi-kapsayanları ve günlükleri/telemetriyi Müşteri Verisi
   tanımından çıkaran "kullanım verisi" tanımlarını izleyin, böylece veri-kullanım
   kısıtlamaları uygulanmasın.
3. **Anonimleştirme standardı.** Satıcı yalnızca "anonimleştirilmiş" veya
   "toplulaştırılmış" veri üzerinde eğittiğini iddia ediyorsa, standart nedir?
   Tanımsız "anonimleştirilmiş" zayıftır. KVKK'daki anonimleştirme ölçütlerini veya
   adlandırılmış bir standardı karşılıyor mu `[doğrulanacak]`? Geri döndürülebilir
   mi?
4. **Rekabetçi bulaşma.** Satıcı rakiplerinize hizmet veriyor mu? Öyleyse, verinizde
   eğitim rekabetçi istihbaratı çıktılarda rakiplerinizin görebileceği şekilde
   sızdırabilir. Rekabetçi izolasyon taahhüdü var mı?
5. **Vazgeçme (opt-out) kapsamı ve kalıcılığı.** Bir opt-out varsa, tüm YZ
   kullanımlarını mı kapsıyor yoksa yalnızca bazılarını mı? Yenilemelerden ve TOS
   güncellemelerinden sağ çıkıyor mu? Kullanıcı-başına mı yoksa kuruluş-başına mı?
   Birçok satıcı varsayılan olarak eğitir ve bir yönetici konsoluna gömülü bir
   opt-out sunar — sözleşmenin varsayılanı açık yapıp yapmadığını kontrol edin.
6. **Çıktı sahipliği.** SaaS ürünü kendisi YZ tarafından üretiliyorsa (taslak,
   özetleme, analiz), çıktılara kim sahip? Satıcı çıktılarınızı eğitim örnekleri
   olarak kullanabilir mi? Üçüncü taraf YZ alt işleyenlerini de kontrol edin —
   satıcı müşteri verisini üçüncü taraf bir LLM'ye (OpenAI, Anthropic, Google)
   gönderebilir ve alt işleyen listesi / veri akışı bunun göründüğü yerdir.
7. **Alt akış düzenleyici zincir.** Satıcının verinizi YZ için kullanması SİZİN için
   düzenleyici maruziyet yaratıyor mu? KVKK yükümlülükleri, sektörel düzenleyici
   maruziyet, diğer YZ mevzuatı `[doğrulanacak — TR ve AB YZ düzenlemesi güncel
   durumu]`.

Her birini bir oyun kitabı pozisyonuyla eşleştirin. Pratik profilinin `## Yapay zeka
/ makine öğrenmesi veri hakları` bölümünde her biri için pozisyonlar olmalı. Anlaşma
yedisinde de sessizse, bu yine de bir bulgudur: "Anlaşma YZ/ML eğitim hakları
konusunda sessiz — yukarıdaki yedi boyuta bağlı açık bir yasak veya tanımlı bir
istisna talep edin."

## Sorumluluk tavanı karar prosedürü

**Tavan tutarı, tavanın en az önemli kısmıdır.** Sorumluluk sınırı tek bir
"oyun kitabına karşı kontrol et" kalemi değildir. Şunları işleyin:

1. **Doğrudan vs. dolaylı/sonuç zararları.** Tavan TÜM sorumluluğa mı, yoksa
   yalnızca doğrudan zararlara mı uygulanır? Doğrudan zararlarda 12 aylık tavan,
   sınırsız sonuç zararlarıyla birlikte, 12 aylık toplu bir tavandan tamamen farklı
   bir pozisyondur. Her iki muameleyi de açıkça belirtin.

2. **Tavan tabanı — kelimesi kelimesine alıntılayın.** "12 aylık tavan" şu anlama
   gelebilir: (a) talepten önceki 12 ayda ödenen ücretler, (b) mevcut 12 aylık
   dönemde ödenmesi gereken ücretler, (c) son 12 aylık kullanımdaki ücretler, (d)
   mevcut sipariş formu kapsamındaki ücretler, (e) şimdiye kadar ödenen toplam
   ücretler. Bunlar bir büyüklük mertebesi kadar farklılaşabilir. Tam dili
   alıntılayın. Belirsizse işaretleyin: "Tavan tabanı belirsiz — `[alıntılanan
   dil]` — [X] veya [Y] anlamına gelebilir. İmzalamadan önce teyit edin."

3. **Tavan-istisna etkileşimi.** Veri ihlali, fikri mülkiyet ve gizlilik için
   sınırsız tazminatla birlikte 500.000 TL'lik bir tavan, SaaS uyuşmazlıklarında
   gerçekte ortaya çıkan iddialar için fiilen sınırsızdır. Tavanın ÜSTÜNDE
   (istisnalar) olanı, ALTINDA (gerçekte tavanlı) olanı sayın ve tavanlı yüzeyin
   anlamlı olup olmadığını değerlendirin: "Tavan [genel sözleşme ihlalini]
   kapsıyor. Veri ihlali, fikri mülkiyet tazminatı ve gizlilik istisna tutulmuş ve
   sınırsız. Bu satıcının risk profili için, tavanlı yüzey [anlamlı / nominal]."

4. **Boyut başına oyun kitabı pozisyonunuz.** Pratik profilinin şu pozisyonları
   olmalı: doğrudan tavan (ücretin katı), dolaylı zararlar (hariç / tavanlı /
   sınırsız), istisna listesi (tavan üstünde kabul edilebilir olan) ve tavan tabanı
   (kabul edeceğiniz tanım). Oyun kitabının tek bir "standart pozisyon" alanı
   varsa, not edin: "Oyun kitabınızın tek bir tavan pozisyonu var — daha kesin bir
   inceleme için doğrudan/dolaylı/istisnalar/taban olarak bölmeyi düşünün."

## Yargı çevresi farkı kontrolü

**Oyun kitabı tek bir uygulanacak-hukuk tercihini küresel olarak uygular.
Uygulanabilirlik önemli ölçüde değişir.** SaaS sözleşmesinin gerçek uygulanacak
hukukunu oyun kitabı pozisyonlarını yüzeysel kabul etmeden önce başlıca farklara
karşı kontrol edin. Bu eklentinin birincil yargı çevresi Türkiye'dir — aşağıdaki
liste ABD-merkezli kaynak eklentiden uyarlanmıştır ve TR muadilleriyle
değiştirilmiştir; her madde bir Türk hukukçusu tarafından teyit edilmelidir:

- **Rekabet yasağı / devşirmeme maddeleri:** TBK m. 444 vd. rekabet yasağı
  sözleşmesi sınırlamalarına tabidir. `[doğrulanacak — TBK m.444-447]`
- **Otomatik yenileme:** Tüketici sözleşmeleri için 6502 sayılı TKHK özel bildirim
  kuralları içerebilir; B2B'de haksız şart denetimi (TBK m. 20-25) uygulanabilir.
  `[doğrulanacak]`
- **Sorumluluk istisnaları:** TBK m. 115 uyarınca kasıt ve ağır kusurdan doğan
  sorumluluğu önceden kaldıran anlaşmalar kesin hükümsüzdür. `[doğrulanacak —
  TBK m.115]`
- **Tazminat:** Bazı yargı çevrelerinde tazmin edilenin kendi kusurundan doğan
  zararlar için tazminat maddeleri geçersiz sayılır. `[doğrulanacak]`
- **Gizlilik süresi:** Süresiz gizlilik taahhütlerinin makul bir süreyle
  sınırlandırılması gerekip gerekmediği yargı çevresine göre değişir.
  `[doğrulanacak]`

Oyun kitabı pozisyonu sözleşmenin uygulanacak-hukuk uygulanabilirliğiyle
çelişiyorsa, işaretleyin: "Oyun kitabınız [X]'i tercih ediyor, ama bu sözleşme [X]'in
[uygulanamaz / kısıtlı / kanuni geçersiz kılmaya tabi] olduğu [Y] hukukuna tabi.
`[yargı çevresi — doğrula]`"

## Redline ayrıntı düzeyi

**Mümkün olan en küçük ayrıntı düzeyinde düzenle.** Bir redline bir müzakere
aracıdır, bir yeniden yazma değil. Toptan madde değişimi "senin taslağını çöpe
attık" sinyali verir — saldırgandır, karşı tarafı tüm maddeyi yeniden okumaya
zorlar ve iyi olan taslak kısımlarını atar. Cerrahi redline'lar — bir kelimeyi çiz,
bir ifade ekle, bir alt maddeyi yeniden yapılandır — "spesifik isteklerimiz var"
sinyali verir ve okuması, anlaşılması, kabul edilmesi daha hızlıdır.

Oyun kitabı pozisyonunu sağlayan en küçük düzenlemeyi varsayılan yap:
- Bir **ifadeden** önce bir **kelimeyi** değiştir. ("on iki (12)" → "yirmi dört (24)")
- Bir **cümleden** önce bir **ifadeyi** değiştir. ("Alıcı tarafından ödenen" →
  "Alıcı tarafından ödenen ve ödenmesi gereken")
- Cümleyi değiştirmeden önce bir **alt maddeyi** yeniden yapılandır. (Bileşik bir
  koşulu bölmek için "(a)" ve "(b)" ekle.)
- Maddeyi değiştirmeden önce bir **cümleyi** değiştir.
- Yalnızca karşı tarafın versiyonu pozisyonunuzdan o kadar uzaksa ve cerrahi
  düzenlemeler taze bir taslaktan daha okunması zor olacaksa bir **tüm maddeyi**
  değiştir — ve bunu yaptığınızda iletide söyleyin: "§8.2'yi işaretlemek yerine
  değiştirdik çünkü değişiklikler kapsamlıydı. Farkı sizinle gözden geçirmekten
  memnuniyet duyarız."

Şüphedeyken, daha küçük. Cerrahi bir redline alan bir müvekkil dikkatlice
okuduğunuza güvenir. Toptan bir değişim alan bir müvekkil gerçekten okuyup
okumadığınızı merak eder.

## Çıktı

satici-inceleme not yapısını, standart oyun kitabı kontrollerinden sonra eklenen
SaaS'a özgü bir bölümle kullanın. satici-inceleme notu zaten meslek sırrı başlığını
taşır.

**Çift şiddet.** Her SaaS'a özgü bulgu her iki ekseni de taşır (bkz. CLAUDE.md
`## Çift şiddet ekseni`):
- **Hukuki risk:** 🔴 Kritik | 🟠 Yüksek | 🟡 Orta | 🟢 Düşük
- **Ticari sürtünme:** 🔴 Anlaşmayı engeller | 🟠 Anlaşmayı yavaşlatır | 🟡 Müşteriyi
  kafa karıştırır | 🟢 Görünmez

Veri-çıkışı, otomatik-yenileme ve fiyat-artışı bulguları hukuki 🟢 / ticari 🔴
olması en muhtemel olanlardır — madde uygulanabilir, ama bir müşterinin
ayrılamamasının veya bir yenilemenin finansı şaşırtmasının nedenidir. Bunları
hukuki şiddette değil, ticari-sürtünme şiddetinde yüzeye çıkarın.

```markdown
### Sonuç

[İmzalayabilir misiniz / Önce X için savaşmanız mı gerekiyor / Vazgeçin — tek
cümlelik neden]

### Yapay zeka ve makine öğrenmesi hakları

[#1 yükselen SaaS müzakere noktası. İşaretleyin: açık ML eğitim maddeleri, "hizmet
iyileştirme" her-şeyi-kapsayanları, kullanım verisi tanımları, çıktı sahipliği,
üçüncü taraf YZ alt işleyenleri, opt-out vs opt-in. Anlaşma sessizse: "YZ/ML eğitim
hakları konusunda sessiz — açık bir yasak veya tanımlı bir istisna talep edin."]

## SaaS'a özgü bulgular

### Otomatik yenileme
**Yenileme tarihi:** [tarih]
**Bildirim penceresi:** [yenilemeden [N] gün önce] kadar iptal edin
**Yenileme fiyat mekanizması:** [yazıldığı gibi]
**Oyun kitabı uyumu:** [pozisyon içinde / sapma / ele alınmamış]
**yenileme-takibi için işaretle:** [evet — ve takipçinin ihtiyaç duyduğu kayıt]

### Fiyat artışı
[`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
pozisyonlarına karşı bulgular]

### Veri çıkışı
[bulgular — iş birimi sahibinin okuması gereken kısım budur]

### SLA
[bulgular, veya "Atlandı — hizmet [paydaş]'a göre iş-kritik değil"]

### Alt işleyenler
[`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
pozisyonlarına karşı bulgular]

### Hizmet değişiklikleri
[`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
pozisyonlarına karşı bulgular]
```

## Devirler

**yenileme-takibi'ne:** Yenileme tarihini ve bildirim penceresini bulduğunuzda,
devredin. yenileme-takibi kaydı şu alanları bekler (tam şema için
`skills/yenileme-takibi/references/yenileme-kaydi.yaml`'a bakın):

```yaml
karsi_taraf:          [isim]
sozlesme:             [başlık]
imza_tarihi:          [ISO tarih]
ilk_sure_bitisi:      [ISO tarih]
yenileme_mekanizmasi: [ör. "otomatik-yenileme yıllık"]
bildirim_suresi_gun:  [tamsayı]
iptal_son_gecerli:    [ISO tarih — ilk_sure_bitisi eksi bildirim_suresi_gun]
yenilemede_fiyat:     [yazıldığı gibi mekanizma]
yillik_tutar:         [tamsayı, belirtildiyse]
is_birimi_sahibi:     [e-posta, biliniyorsa]
clm_id:               [mevcutsa kimlik]
durum:                aktif
```

Herhangi bir alan sözleşmeden veya bağlamdan belirlenemiyorsa, atlayın ve hangi
alanların insan tarafından doldurulması gerektiğini not edin. `clm_id`,
`yillik_tutar` ve `is_birimi_sahibi` özellikle insan girdisine ihtiyaç duyma
olasılığı yüksektir.

**eskalasyon-isaretleyici'ye:** SaaS'a özgü kontrollerden herhangi biri ekibin
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'deki
"asla kabul etme" veya eskalasyon-tetikleyici listesine çarparsa,
eskalasyon-isaretleyici skill'i yönlendirir.

## Neyin uğrunda savaşılacağına dair bir not

SaaS satıcıları, özellikle büyük olanlar, kağıtlarını havayolları bilet
şartlarını müzakere ettiği kadar isteyerek müzakere eder. Savaşları *ekibin oyun
kitabına göre* seçin —
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'deki
`SaaS pozisyonları` bölümü, ekibin her zaman ısrar edeceği şartlar, yalnızca önemli
anlaşmalar için savaştığı şartlar ve kaymasına izin verdiği şartlar arasında ayrım
yapmalıdır. Oyun kitabı bu çizgileri çizmiyorsa sorun.

Sözleşme değeri ve geçiş maliyetine göre kalibre edin. Kolay alternatifleri olan
yıllık 50.000 TL'lik bir araç, üzerine inşa edeceğiniz yıllık 5 milyon TL'lik bir
platformdan daha hafif bir dokunuş alır.

## Sonraki-adımlar karar ağacıyla kapat

CLAUDE.md `## Çıktılar`'a göre sonraki-adımlar karar ağacıyla bitir. Seçenekleri bu
skill'in az önce ürettiğine göre uyarla — beş varsayılan dal (X'i taslakla, eskale
et, daha çok olgu al, izle ve bekle, başka bir şey) bir başlangıç noktasıdır, bir
kilitlenme değil. Ağaç çıktının kendisidir; avukat seçer.
