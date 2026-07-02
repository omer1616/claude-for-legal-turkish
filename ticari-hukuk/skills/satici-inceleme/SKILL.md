---
name: satici-inceleme
description: >
  Referans: gelen bir satıcı sözleşmesinin
  `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
  içindeki ekip oyun kitabına karşı incelenmesi. Sapmaları işaretler, riski
  değerlendirir, spesifik redline dili üretir ve doğru onaylayıcıya yönlendirir.
  Bir satıcı MSA'sı, hizmet sözleşmesi veya benzeri tespit edildiğinde
  /ticari-hukuk:sozlesme-inceleme tarafından yüklenir.
user-invocable: false
---

# Satıcı Sözleşmesi İncelemesi

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

## Hedef kontrolü

Çıktı üretmeden önce nereye gittiğini kontrol et. Kullanıcı bir hedef adlandırdıysa
(bir kanal, dağıtım listesi, karşı taraf, "herkes"), meslek sırrı çemberinin içinde
olup olmadığını sor. Herkese açık kanallar, şirket geneli listeler, karşı taraf/karşı
vekil, tedarikçiler ve (iş ürünü için) müvekkiller korumayı kaldırır. Hedef çemberin
dışında görünüyorsa işaretle ve (a) yalnızca hukuk için gizli sürüm, (b) daha geniş
kanal için arındırılmış sürüm, veya (c) ikisini de öner — sessizce gizli bir başlık
uygulayıp sonra başlığın koruyamayacağı bir yere yapıştırmaya yardım etme. Bu
eklentinin CLAUDE.md'sindeki kanonik `## Paylaşılan guardrail'lar → Hedef kontrolü`
bölümüne bak.

## Amaç

Bir satıcı sözleşmesini bu ekibin gerçekte kullandığı oyun kitabına
(`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` içinde)
karşı oku, sapan her şartı bul ve avukata her biri hakkında ne yapacağını söyle —
belirsiz "revize etmeyi düşünün" değil, spesifik redline diliyle.

Çıktı, avukatın tek geçişte üzerine hareket edebileceği bir inceleme notudur. Her
sorunun bir şiddeti, iş-etkisi açıklaması, önerilen bir düzeltmesi ve gerekiyorsa bir
eskalasyon çağrısı vardır.

## Ön koşul: oyun kitabını yükle

**Sözleşmeyi okumadan önce
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
dosyasını oku.** Eksikse veya hâlâ yer tutucular içeriyorsa, şunu yüzeye çıkar:

> Henüz pratik profilinizi yapılandırmadığınızı fark ettim — bu, oyun kitabı
> pozisyonlarını, eskalasyonu ve ev tarzını pratiğinize göre uyarladığım yöntem.
>
> **İki seçenek:**
> - `/ticari-hukuk:ilk-kurulum` çalıştırın (2 dakika) profilinizi yapılandırmak için,
>   sonra SİZİN oyun kitabınıza uyarlanmış inceleme yaparım.
> - **"geçici"** deyin, genel varsayılanlara karşı (orta risk iştahı, avukat rolü, oyun
>   kitabı yok — temel ilkelerden yaygın satıcı-sözleşmesi risklerini işaretle) inceleme
>   yaparım ve her çıktıyı `[GEÇİCİ — uyarlanmış çıktı için profilinizi yapılandırın]`
>   ile etiketlerim, böylece taahhüt etmeden önce ne yaptığımı görebilirsiniz.

### Geçici mod

Kullanıcı "geçici" derse, incelemeyi normal şekilde şu genel varsayılanları
kullanarak çalıştır: orta risk iştahı, avukat rolü, oyun kitabı yok (sınırsız
sorumluluk, veri-ihlali istisnası yok, tavansız tazminat, bildirimsiz otomatik
yenileme gibi temel ilkelerden satıcı-tarafı yaygın riskleri işaretle —
yapılandırılmış pozisyonlarla eşleştirmek yerine). İnceleyen notunu ve her bulgu
bloğunu `[GEÇİCİ]` ile etiketle. Çıktının sonuna ekle:

> "Bu, varsayılan varsayımlara karşı genel bir çalıştırmaydı. SİZİN pratiğinize —
> oyun kitabınıza, yargı çevrenize, risk iştahınıza — uyarlanmış çıktı almak için
> `/ticari-hukuk:ilk-kurulum` çalıştırın. 2 dakika."

**Hangi taraf?** Oyun kitabını uygulamadan önce, bu sözleşme için şirketin hangi
tarafta olduğunu belirle. Genellikle bellidir: karşı taraf mal veya hizmet sağlayan
bir satıcı/tedarikçiyse, satın alma-tarafındasınız. Karşı taraf ürününüzü/hizmetinizi
satın alan bir müşteriyse, satış-tarafındasınız. Belli değilse (bir bayilik
sözleşmesi, bir ortaklık, bir gelir paylaşımı), sor: "[Şirket] bu sözleşmede hangi
tarafta — satıcı mı müşteri mi?" Eşleşen oyun kitabı bölümünü (`### Satış-tarafı
oyun kitabı` veya `### Satın alma-tarafı oyun kitabı`) yapılandırmadan oku. Çıktıda
hangi tarafın uygulandığını not et, böylece inceleyen hangi oyun kitabının
uygulandığını bilir. Eşleşen taraf `[Yapılandırılmadı]` ise, dur ve kullanıcıya bu
inceleme devam edebilmeden önce `/ticari-hukuk:ilk-kurulum --side <taraf>`
çalıştırmasını söyle.

Bu skill tipik olarak satın alma-tarafı sözleşmeler için kullanılır (size tedarik
eden satıcılar), ama taraf kontrolü yine de geçerlidir — bir "satıcı sözleşmesi"
sizin kendi şablonunuz olup bir bayilik düzenlemesinin parçası olarak bir satıcıya
gönderilmiş olabilir (satış-tarafı).

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
içindeki oyun kitabı gerçek kaynaktır. Size şunu söyler:
- Bu ekibin standart pozisyonları ne (piyasa standardı değil — *onların* standardı)
- Daha önce kabul ettikleri yedekler neler
- Asla kabul etmedikleri neler
- Kim neyi onaylıyor
- Önce kontrol edilecek tek anlaşma bozucu

Sözleşmede anlaşma bozucu varsa, notun en üstünde işaretle ve ayrıntılı incelemeyi
durdur. Satıcıya müşteri verisini eğitim için kullanma hakkı veren bir sözleşmede
sorumluluk tavanlarına 30 dakika harcamanın anlamı yok.

## İş akışı

### Adım 1: Yönelim

Sözleşmenin tamamını bir kez, hızlıca oku. Cevapla:

| Soru | Cevap |
|---|---|
| Bu ne tür bir sözleşme? | MSA / SaaS aboneliği / Profesyonel hizmetler / Lisans / Diğer |
| Biz kimiz? | Müşteri / Satıcı (bu eklenti müşteri varsayar — değilse işaretle) |
| Karşı taraf | İsim, ve BigCo (müzakere etmeyecek) mi yoksa girişim (edecek) mi? |
| Tutar | Belirtilmişse yıllık / toplam sözleşme değeri |
| Süre | Uzunluk, yenileme mekaniği |
| VİS var mı? | Ekli / URL ile referanslı / eksik |
| Sipariş formu var mı? | Ayrı belge mi entegre mi |

**Tutar ele alma.** Ana sözleşme bir tutar belirtmiyorsa (MSA şartları belirler ama
Sipariş Formu fiyatı taşır, ki bu tipiktir), eskalasyon matematiği veya tutar
eşiklerini uygulamadan önce **dur ve sor**:

> MSA'nın kendisi yıllık sözleşme değerini belirtmiyor. Sipariş Formu fiyatı taşıyor.
> Eskalasyon eşiğiniz [matristen X TL]. Bunu yönlendirmeden önce, yıllık tutara
> ihtiyacım var. Seçenekler:
> 1. Sipariş Formu tutarını yapıştırın (tercih edilir — yönlendirme ve not için
>    kullanırım).
> 2. Bunun [eşik]'in üstünde mi altında mı olduğunu söyleyin, buna göre yönlendiririm;
>    not, yönlendirmenin elde tutar olmadan [üstünde/altında] varsaydığını işaretler.
> 3. Ne olursa olsun daha yüksek onaylayıcıya güvenli tarafta yönlendirin — fiyatını
>    bilmediğiniz bir inceleme için daha güvenli.

Sessizce bir tutar varsayıp sonra varsayılan tutarı yönlendirmeyi sürmek için
KULLANMA. Varsayım, skill'in tahmin etmemesi gereken onay çağrısına yayılır.

**Referansla VİS ele alma.** Ana sözleşme bir VİS'i "[URL]'de mevcut" veya "[URL]'de
belirtildiği gibi" veya benzer şekilde referansla birleştiriyorsa, VİS sözleşmenin
parçasıdır ama önünüzde değildir. Bunu Yönelim tablosunda ve inceleme notunda açıkça
belirt:

> Bu sözleşme bir VİS'i URL referansıyla `[URL]` birleştiriyor. VİS gerçek veri
> şartlarını taşır — alt işleyen hakları, ihlal-bildirim zamanlaması, veri-iade
> mekaniği, standart sözleşme maddeleri, denetim hakları. Onu okumadan, aşağıdaki
> veri-koruma analizi kısmidir. VİS'i ayrı bir inceleme için `/kisisel-veri-kvkk`
> kuruluysa oraya yönlendirmeyi öner, ya da Adım 3'ün veri-koruma analizini
> tamamlamadan önce onu getir ve satır içi oku.

Kullanıcıda `kisisel-veri-kvkk` kuruluysa, açıkça öner:

> VİS URL'sini hazır olduğunuzda `/kisisel-veri-kvkk`'ya iletmemi ister misiniz? O
> skill VİS işi için kurulmuştur ve bu skill'in yalnızca kapıda işaretlediği alt
> işleyen / SCC / ihlal-bildirim sorunlarını yakalayacaktır.

VİS referansla birleştirilmişken yokmuş gibi sessizce devam etme. Eksik bir VİS ile
okunmamış bir VİS farklı boşluklardır — farklı etiketleyin.

### Adım 2: Anlaşma bozucu kontrolü

Önce
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
dosyasındaki "tek şeyi" kontrol et. Varsa:

```markdown
## ⛔ ANLAŞMA BOZUCU VAR

**Bölüm [X.X]** [anlaşma bozucuyu] içeriyor. Ekip oyun kitabına göre bu kesin bir
hayırdır. Önerilen:

- [ ] Geri it — [spesifik alternatif dil] öner
- [ ] Vazgeç — karşı taraf esnemezse imzalamayız

Aşağıdaki ayrıntılı inceleme bütünlük için sağlanmıştır ama bu çözülmedikçe
tartışmalıdır.
```

### Adım 3: Madde madde karşılaştırma

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
içindeki her oyun kitabı kategorisi için, sözleşmedeki karşılık gelen bölümü bul ve
karşılaştır.

**Her sapma için üret:**

```markdown
### [Bölüm X.X]: [Sorun adı]

**Oyun kitabı diyor ki:** [standart pozisyonumuz,
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
alıntılanmış]

**Sözleşme diyor ki:**
> "[sözleşmeden tam alıntı]"

**Fark:** [Eksik şart | Standarttan zayıf | Yedekten zayıf | Standart-dışı yapı |
Kabul edilemez]

**Hukuki risk:** 🔴 Kritik | 🟠 Yüksek | 🟡 Orta | 🟢 Düşük
**Ticari sürtünme:** 🔴 Anlaşmayı engeller | 🟠 Anlaşmayı yavaşlatır | 🟡 Müşteriyi
kafa karıştırır | 🟢 Görünmez

**Neden önemli:** [bir veya iki cümle, düz Türkçe — bu şart olduğu gibi kalırsa iş
için ne ters gider]

**Önerilen redline:**
> "[spesifik yerine geçecek dil — bir işaretlemeye yapıştırmaya hazır]"

**Esnemezlerse:** [`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
yedek, veya yedek yoksa "[kişi]'ye eskale et"]
```

**Şiddet kalibrasyonu:**

| Düzey | Anlamı |
|---|---|
| 🔴 Kritik | Düzeltmeden imzalama. Ekibin
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'deki
"asla kabul etme" listesindeki bir şart, veya bir anlaşma bozucu. |
| 🟠 Yüksek | Güçlü şekilde it; esnemezlerse eskale et. Oyun kitabının beyan edilen
yedek aralığının dışında bir şart. |
| 🟡 Orta | İlk turda it; son açık kalem ise kabul et. Yedek aralığının içinde ama
standart pozisyonun gerisinde bir şart. |
| 🟢 Düşük | Not et, sermaye harcama. Oyun kitabının açıkça tolere ettiği bir şart,
veya tamamen biçimsel bir sapma. |

Şiddet her zaman
*`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye karşı*
uygulanır. Bir şart temiz bir şekilde bir oyun kitabı pozisyonuna eşlenmiyorsa,
kullanıcıya hangi kovaya girdiğini sor ve cevabı
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye
kaydetmeyi öner.

#### Sorumluluk tavanı karar prosedürü

**Tavan tutarı, tavanın en az önemli kısmıdır.** Sorumluluk sınırı maddesini
incelerken, tek bir "sorumluluk tavanını oyun kitabına karşı kontrol et" satırı
üretme. Aşağıdaki dört boyutu işle ve her birini bulguda açıkça belirt:

1. **Doğrudan vs. dolaylı/sonuç zararları.** Tavan TÜM sorumluluğa mı, yoksa yalnızca
   doğrudan zararlara mı uygulanır? Doğrudan zararlarda 12 aylık tavan, sınırsız
   sonuç zararlarıyla birlikte, 12 aylık toplu bir tavandan tamamen farklı bir
   pozisyondur. Her iki muameleyi de açıkça belirt.

2. **Tavan tabanı — kelimesi kelimesine alıntıla.** "12 aylık tavan" şu anlama
   gelebilir: (a) talepten önceki 12 ayda ödenen ücretler, (b) mevcut 12 aylık
   dönemde ödenmesi gereken ücretler, (c) son 12 aylık kullanımdaki ücretler, (d)
   mevcut sipariş formu kapsamındaki ücretler, (e) şimdiye kadar ödenen toplam
   ücretler. Bunlar bir büyüklük mertebesi kadar farklılaşabilir. Tam dili alıntıla.
   Belirsizse işaretle: "Tavan tabanı belirsiz — `[alıntılanan dil]` — [X] veya [Y]
   anlamına gelebilir. İmzalamadan önce teyit edin."

3. **Tavan-istisna etkileşimi.** Veri ihlali, fikri mülkiyet ve gizlilik için
   sınırsız tazminatla birlikte 500.000 TL'lik bir tavan, SaaS uyuşmazlıklarında
   gerçekte ortaya çıkan iddialar için fiilen sınırsızdır. Tavanın ÜSTÜNDE (istisnalar)
   olanı, ALTINDA (gerçekte tavanlı) olanı sayın ve tavanlı yüzeyin anlamlı olup
   olmadığını değerlendirin: "Tavan [genel sözleşme ihlalini] kapsıyor. Veri ihlali,
   fikri mülkiyet tazminatı ve gizlilik istisna tutulmuş ve sınırsız. Bu satıcının
   risk profili için, tavanlı yüzey [anlamlı / nominal]."

4. **Boyut başına oyun kitabı pozisyonunuz.** Pratik profilinin şu pozisyonları olmalı:
   doğrudan tavan (ücretin katı), dolaylı zararlar (hariç / tavanlı / sınırsız),
   istisna listesi (tavan üstünde kabul edilebilir olan) ve tavan tabanı (kabul
   edeceğiniz tanım). Oyun kitabının tek bir "standart pozisyon" alanı varsa, not et:
   "Oyun kitabınızın tek bir tavan pozisyonu var — daha kesin bir inceleme için
   doğrudan/dolaylı/istisnalar/taban olarak bölmeyi düşünün."

#### Yargı çevresi farkı kontrolü

**Oyun kitabı tek bir uygulanacak-hukuk tercihini küresel olarak uygular. Uygulanabilirlik
önemli ölçüde değişir.** Oyun kitabı pozisyonlarını yüzeysel kabul etmeden önce
sözleşmenin gerçek uygulanacak hukukunu aşağıdaki başlıca farklara karşı kontrol et.
Bu eklentinin birincil yargı çevresi Türkiye'dir — aşağıdaki liste ABD-merkezli
kaynak eklentiden uyarlanmıştır ve TR muadilleriyle değiştirilmiştir; her madde bir
Türk hukukçusu tarafından teyit edilmelidir:

- **Rekabet yasağı / çalışan devşirmeme maddeleri:** TBK m. 444 vd. rekabet yasağı
  sözleşmesi sınırlamalarına tabidir (süre, yer, konu bakımından sınırlı olmalı; aşırı
  ise kısmen geçersiz sayılabilir). `[doğrulanacak — TBK m.444-447]`
- **Otomatik yenileme:** Tüketici sözleşmeleri için 6502 sayılı TKHK ve ilgili
  yönetmelikler özel bildirim kuralları içerebilir; B2B sözleşmelerde genel sözleşme
  serbestisi geçerlidir ama haksız şart denetimi (TBK m. 20-25, genel işlem koşulları)
  uygulanabilir. `[doğrulanacak]`
- **Sorumluluk istisnaları:** TBK m. 115 uyarınca kasıt ve ağır kusurdan doğan
  sorumluluğu önceden kaldıran veya sınırlayan anlaşmalar kesin hükümsüzdür — bir
  sözleşme "her türlü sorumluluğu" hariç tutmaya çalışıyorsa bu madde onu geçersiz
  kılabilir. `[doğrulanacak — TBK m.115]`
- **Tazminat (indemnification):** Bazı yargı çevrelerinde tazmin edilenin kendi
  kusurundan doğan zararlar için tazminat maddeleri geçersiz sayılır; TR hukukunda
  emsal durum netleştirilmeli. `[doğrulanacak]`
- **Gizlilik süresi:** Süresiz (sonsuz) gizlilik taahhütlerinin makul bir süreyle
  sınırlandırılması gerekip gerekmediği yargı çevresine göre değişir. `[doğrulanacak]`

Oyun kitabı pozisyonu sözleşmenin uygulanacak-hukuk uygulanabilirliğiyle
çelişiyorsa, işaretle: "Oyun kitabınız [X]'i tercih ediyor, ama bu sözleşme [X]'in
[uygulanamaz / kısıtlı / kanuni geçersiz kılmaya tabi] olduğu [Y] hukukuna tabi.
`[yargı çevresi — doğrula]`"

### Adım 4: Olumlu şartlar ve boşluklar

İki kısa liste:

**Standardımızdan daha iyi:** Satıcının bize istediğimizden fazlasını verdiği şartlar.
Bunları not edin — başka yerde bir şeyden vazgeçmeniz gerekirse pazarlık malzemesidir.

**Tamamen eksik:** Sadece orada olmayan standart hükümler. En yaygını: devir
kısıtlamaları, denetim hakları (istiyorsak), mücbir sebep, sigorta gereksinimleri.

### Adım 5: Eskalasyon yönlendirmesi

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
içindeki eskalasyon matrisini şuna karşı kontrol et:
- Sözleşme tutarı
- Herhangi bir 🔴 kritik sorunun varlığı
- Herhangi bir otomatik-eskalasyon tetikleyicisi (sınırsız sorumluluk, fikri mülkiyet
  devri vb.)

Bunu kimin onaylaması gerektiğini açıkça belirt:

```markdown
## Onay yönlendirmesi

[Tutar / sorun şiddetine] göre, bu sözleşme şunu gerektirir:

- [ ] **[İsim/rol]** onayı — [neden]
- [ ] **İş birimi sahibi onayı** [tartmaları gereken spesifik ticari şart] üzerinde

**Önerilen sonraki adım:** [Redline'ları karşı tarafa gönder | Yanıt vermeden önce
BHM'ye eskale et | Hukuk yanıt vermeden önce X ticari şartı hakkında iş girdisi al]
```

**Redline'ları karşı tarafa göndermeye geçmeden önce:**
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
içindeki `## Bunu kim kullanıyor`'u oku. Rol Avukat değilse:

> Redline göndermek hukuki bir eylemdir — karşı taraf her düzenlemeyi
> müzakere pozisyonumuz olarak ele alacaktır. Bunu bir avukatla gözden geçirdiniz mi?
> Evetse, devam edin. Hayırsa, onlara getirmeniz için bir brifing:
>
> [1 sayfalık özet üret: karşı taraf, sözleşme türü, önerilen spesifik redline'lar,
> her birinin ardındaki oyun kitabı pozisyonları, yedekler, ve paket gitmeden önce
> avukata sorulacaklar.]
>
> Bir avukat bulmanız gerekirse: bağlı olduğunuz baroya (il barosu, Türkiye Barolar
> Birliği üzerinden) başvurun, çoğu bir yönlendirme hizmeti sunar.
> `[doğrulanacak — TR baro yönlendirme mekanizmaları]`

Açık bir evet olmadan bu kapıdan geçme.

## Redline ayrıntı düzeyi

**Mümkün olan en küçük ayrıntı düzeyinde düzenle.** Bir redline bir müzakere
aracıdır, bir yeniden yazma değil. Toptan madde değişimi "senin taslağını
çöpe attık" sinyali verir — saldırgandır, karşı tarafı tüm maddeyi yeniden
okumaya zorlar ve iyi olan taslak kısımlarını atar. Cerrahi redline'lar — bir
kelimeyi çiz, bir ifade ekle, bir alt maddeyi yeniden yapılandır — "spesifik
isteklerimiz var" sinyali verir ve okuması, anlaşılması, kabul edilmesi daha
hızlıdır.

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

Şüphedeyken, daha küçük. Cerrahi bir redline alan bir müvekkil, dikkatlice
okuduğunuza güvenir. Toptan bir değişim alan bir müvekkil, gerçekten okuyup
okumadığınızı merak eder.

### Adım 6: Notu birleştir

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
`## Çıktılar`'dan iş-ürünü başlığını ekle (role göre farklılaşır — bkz. `## Bunu
kim kullanıyor`).

Bu not ve altında yatan sözleşme meslek sırrı, gizli veya her ikisi olabilir.
Çıktı bu durumu kaynaktan miras alır. Yalnızca meslek sırrı çemberi içinde dağıt;
gizli materyallerin yaşadığı yerde işaretle ve sakla; herhangi bir dış teslimattan
(ör. karşı taraf redline'ları, paydaş özetleri) önce iş-ürünü başlığını çıkar.

Aşağıda uygulanan oyun kitabı pozisyonları
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` →
`Uygulanacak hukuk ve yetkili merci`'de kaydedilen yargı çevresini yansıtır. Hukuki
kurallar ve uygulanabilirlik yargı çevresine göre önemli ölçüde değişir. Bu anlaşma
farklı bir uygulanacak hukuk veya hukuk seçimi sorunu içeriyorsa, notta işaretle —
analiz yazıldığı gibi aktarılmayabilir.

> **Sessiz tamamlama yok.** Yapılandırılmış hukuki araştırma aracına yapılan bir
> sorgu, notun ihtiyaç duyduğu bir kural için az veya hiç sonuç döndürmezse (bir
> sınırlama maddesinin uygulanabilirliği, tazminat kapsamı, hukuk seçimi sorusu),
> bulunanı raporla ve dur. Boşluğu sormadan web aramasından veya model bilgisinden
> DOLDURMA. Şunu de: "Arama [araç]'tan [N] sonuç döndürdü. [Kural / yargı çevresi]
> için kapsam zayıf görünüyor. Seçenekler: (1) arama sorgusunu genişlet, (2) farklı
> bir araştırma aracı dene, (3) web'de ara — sonuçlar güvenmeden önce birincil
> kaynağa karşı kontrol edilmesi gereken `[web araması — doğrula]` etiketiyle
> gelecek, veya (4) doğrulanmamış olarak işaretle ve dur. Hangisini istersiniz?"
> Daha düşük güvenli kaynakları kabul edip etmeyeceğine avukat karar verir.
>
> **Kaynak atfı.** Not bir kanun, yönetmelik veya içtihat alıntıladığında, atfı
> etiketle: bağlı bir hukuki araştırma bağlayıcısından alınan atıflar için
> `[Lexpera]`, `[Kazancı]`, `[UYAP]`, `[mevzuat.gov.tr]` veya MCP araç adı; web
> araması atıfları için `[web araması — doğrula]`; eğitim verisinden hatırlanan
> atıflar için `[model bilgisi — doğrula]`; karşı taraf taslağından veya kurum
> dosyalarından gelen atıflar için `[kullanıcı verdi]`. `doğrula` etiketli atıflar
> daha yüksek uydurma riski taşır ve önce kontrol edilmelidir. Etiketleri asla
> çıkarma veya birleştirme.

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar]

# Satıcı Sözleşmesi İncelemesi: [Karşı taraf] [Sözleşme türü]

**İncelenme tarihi:** [tarih]
**Sözleşme değeri:** [tutar] TL / [süre]
**Rolümüz:** Müşteri

---

## Sonuç

[İki cümle. Bunu imzalayabilir miyiz? Önce ne değişmeli?]

**Sorunlar (hukuki risk):** [N]🔴 [N]🟠 [N]🟡 [N]🟢
**Sorunlar (ticari sürtünme):** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Onay gereken:** [isim]

---

## Anlaşma bozucu kontrolü

[✅ Temiz | ⛔ Var — yukarıya bak]

---

## Şiddete göre sorunlar

[Adım 3'ten tüm sapma blokları, Kritik → Düşük gruplanmış]

---

## Olumlu şartlar

[liste]

## Eksik hükümler

[liste]

---

## Onay yönlendirmesi

[Adım 5'ten]

---

## Redline paketi

[İstendiyse: tüm önerilen değişiklikler için birleştirilmiş, işaretlemeye hazır dil]
```

## Entegrasyon: CLM

Bir CLM MCP'si bağlıysa, incelemeden sonra:

- Bu karşı tarafın bizimle zaten sözleşmeleri olup olmadığını kontrol et (müzakere
  duruşunu bilgilendirebilir — "son anlaşmada onlara zaten 24 aylık tavan verdik")
- Bu sözleşme türüyle eşleşen iş akışı şablonunu çek
- CLM kaydını inceleme notu ekli ve onaylayıcılar önceden yönlendirilmiş olarak
  oluşturmayı öner

## Entegrasyon: DocuSign

DocuSign MCP'si bağlıysa ve sözleşme imzaya hazırsa (tümü yeşil veya kabul edilmiş
sorunlar), öner:
- Zarfı oluştur
- Eskalasyon matrisine göre doğru sırayla imzacılara yönlendir

Açık talimat olmadan imza için hiçbir şey **gönderme**. "İmzaya hazır" avukatın
çağrısıdır, sizin değil.

**Bir imza zarfı oluşturmadan veya karşı-imza için yönlendirmeden önce:**
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
içindeki `## Bunu kim kullanıyor`'u oku. Rol Avukat değilse:

> Bu adımın hukuki sonuçları var (imzalamak şirketi tüm sözleşmeye bağlar). Bunu
> bir avukatla gözden geçirdiniz mi? Evetse, devam edin. Hayırsa, onlara getirmeniz
> için bir brifing:
>
> [1 sayfalık özet üret: karşı taraf, sözleşme değeri, bulunan sorunlar ve nasıl
> çözüldükleri, avukatın kabul ettiği herhangi bir risk, ve zarf gitmeden önce
> avukata sorulacaklar.]
>
> Bir avukat bulmanız gerekirse: bağlı olduğunuz baroya başvurun.
> `[doğrulanacak — TR baro yönlendirme mekanizmaları]`

Açık bir evet olmadan bu kapıdan geçme.

## Çıktı formatları

**Tam not (varsayılan):** Yukarıdaki gibi. CLM kaydına veya
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` ev-tarzı
bölümündeki Drive klasörüne gider.

**Slack boyutunda özet:** İki satır ve bir bağlantı. Bir kanalda biri "bu uygun mu?"
diye sorduğunda.

```
[Karşı taraf] [tür] — İŞ İSTİYOR. 1🔴 (sınırsız sorumluluk §8.2), 2🟠. Tam inceleme:
[bağlantı]. [BHM] onayı gerekiyor.
```

**Redline belgesi:** Kullanıcı isterse, izlenen değişikliklerle bir .docx çıktısı
üret. docx skill'ini kullan. Her değişiklikteki yorumlar oyun kitabı pozisyonunu
alıntılar.

## Teslim etmeden önce kalite kontrolleri

- [ ] `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
  yüklendi ve alıntılandı — genel piyasa pozisyonları değil
- [ ] Anlaşma bozucu önce kontrol edildi
- [ ] Her sorunun spesifik yerine geçecek dili var
- [ ] Risk düzeyleri kalibre edilmiş (her şey Kritik değil)
- [ ] Onaylayıcı adlandırılmış, "hukuka eskale et" değil
- [ ] Karşı taraf bağlamı düşünüldü (BigCo vs. girişim — neyin uğrunda savaşmaya
  değdiğini etkiler)

## Sonraki-adımlar karar ağacıyla kapat

CLAUDE.md `## Çıktılar`'a göre sonraki-adımlar karar ağacıyla bitir. Seçenekleri bu
skill'in az önce ürettiğine göre uyarla — beş varsayılan dal (X'i taslakla, eskale
et, daha çok olgu al, izle ve bekle, başka bir şey) bir başlangıç noktasıdır, bir
kilitlenme değil. Ağaç çıktının kendisidir; avukat seçer.
