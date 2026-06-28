---
name: kronoloji
description: Beyan edilen belge kaynaklarından ve yüklemelerden kronoloji oluşturur veya günceller — tarihli olaylar çıkarılır, tekilleştirilir ve dava teorisine göre önem derecesiyle etiketlenir. Kullanıcı bir üretim veya dosya setinden kronoloji veya zaman çizelgesi oluşturmasını istediğinde, "kayıt kronolojisi", "ne zaman ne oldu" dediğinde veya çalışma amaçlı, olgular beyanı veya tanığa özgü zaman çizelgesi istediğinde kullan.
argument-hint: "[slug] [--format=calisma|olgular-beyani|tanik-[ad]]"
---

# /kronoloji

1. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` yükle → teori, pivot olgu, kilit olgular.
2. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` yükle → belge depolama kaynakları, varsayılan dosya klasörü deseni.
3. Aşağıdaki iş akışını ve referansı uygula.
4. Kaynakları sırayla belirle: bu oturumda kullanıcı tarafından sağlanan yollar, varsayılan dosya klasörü, `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'den beyan edilen kaynaklar.
5. Okunabilir kaynaklar için: tarihli olayları çıkar. Erişilemeyen kaynaklar için: Boşluklarda not et.
6. Tekilleştir, olay başına kaynak listesiyle birleştir.
7. Dava teorisine göre önem derecesini etiketle (🔴/🟡/⚪).
8. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/kronoloji.md` yaz (veya bayrak başına format çeşidi).
9. Önceki sürüm varsa: sürüm numarası artar, fark özeti kullanıcıya sunulur.
10. Sonuçlandırmadan önce teyit et: "İşte oluşturduğum. 🔴 girdileri tara — yanlış değerlendirdiğim bir şey var mı?"

---

# Kronoloji

## Açıklanan Belge Kullanım Kısıtlamaları

Bir dava belgesi setiyle çalışmadan önce sor: "Bu belgelerden herhangi biri hukuki işlemlerdeki ifşa veya keşif yoluyla elde edildi mi?" Evet ise:

- **Türk hukukunda (HMK m.220 vd.):** Mahkeme kararıyla ibraz ettirilen belgeler, ilgili yargılama sona erdiğinde veya dışında başka amaçlarla kullanılamaz. Kamuya açık hâle gelen belgeler bu kısıtlamadan muaftır. `[doğrulanacak — HMK'da İngiliz CPR 31.22 gibi kesin bir "örtülü taahhüt" kuralı var mı?]`
- **Diğer yargı çevreleri:** Benzer kısıtlamalar yaygındır. Yerel kuralı kontrol et.
- **ABD belgelerinde (CPR/FRCP):** Koruyucu emirler ve Federal Hukuk Muhakemeleri Usulü Kuralları (FRCP Kural 26(c)) benzer kısıtlamalar getirebilir.

Teyit et: "Bu kullanım, belgelerin ifşa edildiği yargılamalar kapsamındadır, veya izin/onay sahibim, veya belgeler artık kamuya açıktır." Teyit edilmezse işaretle: "⚠️ İfşa edilen belgeler kullanım kısıtlamalarına tabi olabilir. Devam etmeden önce bu kullanımın izinli olduğunu teyit edin."

## Amaç

Olgular sırayla gerçekleşir. Kronoloji, her anlatının asıldığı omurgadır — dilekçedeki olgular beyanı, karşılık notları, sulh notları, tanık hazırlığı. Kronoloji elle oluşturmak yavaştır; yapay zeka yapılandırılmış çıkarımda iyidir. Sorun: çöp girince çöp çıkar. Bu skill, yapılandırmanın beyan ettiği kaynaklardan ve kullanıcının yüklediği her şeyden çeker.

## Modlar

Bu skill iki pratik ortama hizmet eder. Varsayılanı plugin yapılandırma CLAUDE.md'sindeki kullanıcının `## Pratik rolü`nden seç; kullanıcı bayrakla çalıştırma başına geçersiz kılabilir.

- **`--dosya` modu (şirket-içi dava avukatı için varsayılan).** Dosya-geçmişi odaklı. Dosyanın dava teorisini ve kilit olgularını `matter.md`'den okur, beyan edilen belge depolama kaynaklarından çeker ve `history.md`'yi çalışan iç günlük olarak ele alır (kararlar, saklamalar, karşılık notları — kasıtlı olarak kronolojide değil). Çıktı dosya-merkezlidir: uyuşmazlık genelinde ne oldu, savunuculuk kullanımı için etiketlendi.
- **`--belgeler` modu (büro avukatı / paralegal için varsayılan).** Üretim belgesi odaklı. Yapılandırmadan dava teorisini okur, ardından e-keşif çıktısından, bir muhafız dosya setinden veya Bates numaralı bir üretimden çıkarır. Çıktı üretim merkezlidir: belgeler ne gösteriyor, Bates atıflarıyla, dava teorisine göre etiketlenmiş.

Her iki mod da aynı çıktı yapısında birleşir (zaman çizelgesi, 🔴/🟡/⚪ önem etiketleri, boşluklar, SoF çeşidi). Fark kaynak profili ve önem çerçevesidir.

`## Pratik rolü` `bagimsiz` veya `diger` ise, varsayılan olarak `--dosya` al ama ilk çalıştırmada her iki modu da belirt ve kullanıcının seçmesine izin ver.

## Taraf Çerçeveleme (Önem Etiketleri)

Aynı olay, uygulayıcının bir iddiayı ispat etmesine veya çürütmesine bağlı olarak farklı şekillerde önem taşır. Pratik profilindeki `## Taraf` bölümünü oku (ve dosya varsayılanı geçersiz kılıyorsa dosya bazı duruşu):

- **Davacı (saldırgan çerçeveleme)** — 🔴, iddianın unsurlarını *oluşturan* (sorumluluk, nedensellik, zarar, ihbar), savunmanın açmaya çalışacağı boşlukları *kapatan* veya davacı lehine zamanaşımı sürelerini *başlatan* olayları işaretler. 🟡, iddiayı destekleyen ama itirazlara açık olayları işaretler. ⚪ arka plan bağlamıdır.
- **Davalı (savunmacı çerçeveleme)** — 🔴, iddianın unsurlarını *kıran* (nedensellik, ihbar, güven, itimat başarısızlığı), zamanaşımı veya yetki itirazlarını *açan* veya ek savunmaları *destekleyen* (ibra, feragat, kusur ağırlığı) olayları işaretler. 🟡, davacının anlatısını zayıflatan olayları işaretler. ⚪ arka plandır.
- **Her ikisi / değişiyor** — önem etiketleri için hangi tarafın çerçevelemesinin uygulanacağını kronoloji başına kullanıcıya sor. Temel zaman çizelgesi tarafsızdır; yalnızca önem okuması değişir.

Uygulanan çerçevelemeyi çıktının başında not et: `Önem etiketleri [davacı / davalı] perspektifinden uygulandı.` Olgular beyanı çeşidi üretirken, kullanıcı aksi belirtmedikçe taraf varsayılanını kullan.

## Bağlamı Yükle

Ortak:
- Plugin yapılandırma CLAUDE.md → dava teorisi bağlamı (şirket-içi: belge kaynakları için `## Manzara`; büro avukatı: platform + muhafızlar için `## Dava teorisi` ve `## Belge incelemesi`), iş-ürünü başlığı için `## Çıktılar`, ayrıcalık işaretleme kuralı için `## Karar duruşu`.
- Bu dosya için önceki `kronoloji.md`, varsa.
- Kullanıcının bu oturumda yüklediği veya sağladığı yollar.

`--dosya` modu ayrıca okur:
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` → dava teorisi, kilit olgular, pivot olgu (önem etiketleme için), kilit tarihler.
- CLAUDE.md'den varsayılan dosya klasörü deseni → bu slug için belgelerin nerede olduğu.

`--belgeler` modu ayrıca okur:
- Bağlayıcı mevcutsa e-keşif platform meta verisi — muhafız + tarih aralığına göre.
- Kullanıcı işaret ediyorsa Bates aralığı bildirimi veya üretim indeksi.

**Çatışma kapısı — atlanamaz (`--dosya` modu).** Kronoloji oluşturmadan önce `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml`'da dosya slug'ını kontrol et. Dosya `_log.yaml`'da yoksa reddet ve yönlendir:

> "[dosya slug'ı]'nı dosya günlüğünde göremiyorum. Önce `/dava-takibi:dosya-acilis` çalıştır; böylece çatışma taraması yapılır ve dosya çalışma alanı kurulur. Intake yapılmamış bir dosyada kronoloji oluşturmam — çatışma taraması kapıdır."

Intake yapılmamış dosyada devam etme. `--belgeler` modu (dosya slug'ı olmadan geçici bir belge seti üzerinde çalışma) kapıdan muaftır, ancak çıktıları dosya-öncesi araştırma olarak ele alınmalı ve sanki iş ürünüymüş gibi dosyalanmamalı.

## İş Akışı

### Adım 0: Gizlilik Kapısı (Her Seferinde İlk Çalışır)

Kronoloji çalışması belgelerden çeker. Belgeler genellikle gizlidir (avukat-müvekkil, iş ürünü, ortak çıkar, ortak savunma) — şirket-içi dosya belgeleri genellikle varsayılan olarak gizlidir; e-keşif üretimleri, özellikle süregelen veya ortak çıkar üretimleri, genellikle gizli veya incelenmemiş materyal içerir. Ayrıcalıklı bir belgeden içerik çıkarıp daha sonra paylaşılan bir kronolojiye koymak, kime ve hangi doktrin altında alındığına bağlı olarak feragat riskini *yaratabilir* (ortak çıkar, ortak savunma, iş ürünü korumaları geçerli olabilir). Feragat analizi olgulara özgüdür — dağıtmadan önce avukat onayı alın.

Skill, kullanıcı bir gizlilik duruşu seçene kadar çıkarmayacak:

> Çıkarmadan önce: kaynaklar gizlilik açısından nasıl tarandı?
>
> - **A. Tüm kaynaklar temizlendi** — bunları zaten taradınız. Gizlilik bayrakları olmadan çıkarırım. Çıktı keşfe hazır duruştur; yine de iş ürünü olarak işaretlendi.
>
> - **B. Karışık veya henüz taranmadı** — çıkarırım ve her girdiyi bir `gizlilik` bayrağıyla etiketlerim: `tamam` (açıkça gizli olmayan materyalden alınan), `bayrak` (potansiyel gizli materyalden alınan — A/M, İÜ, ortak çıkar), veya `incele` (kaynak belirsiz). İşaretlenmiş girdiler çıktıda görsel olarak belirtilir ve Olgular Beyanı çeşidi bunları varsayılan olarak filtreler.
>
> - **C. İptal et — önce tara** — skill'i durdur. Kaynakları tara. Geri dön ve yeniden çalıştır.

Seçimi kronoloji başlığında `gizlilik_durusu: A-temiz | B-karisik | C-iptal` olarak kaydet. B veya C ise gerekçeyi kısaca kaydet.

**Neden uyarı değil kapı:** Bir uyarı bir kez okunur ve unutulur. Bir kapı, duruş kararını kayda zorlar; bu da her kronoloji dosyasının kendi provenance'ını taşıdığı anlamına gelir — sonraki okuyan girdilerin gizlilik taramasından geçmiş materyalden elde edilip edilmediğini bilir.

### Adım 1: Belge Kaynaklarını Belirle

**`--dosya` modu:**

1. **Kullanıcı tarafından sağlanan yollar** — bu oturumda bırakılan her şey (dosya yolları, sürücü bağlantıları, e-posta çıktıları).
2. **Varsayılan dosya klasörü** — CLAUDE.md'nin belge depolama deseninden, bu slug için genişletilmiş (ör. `G:/Hukuk/Dosyalar/acme-alacak-2026`).
3. **Beyan edilen kaynaklar** — CLAUDE.md'deki `Belge depolama` tablosu, bu dosyanın dokunabileceği olanlarla filtrelenmiş.
4. **Sor** — kaynaklar yetersiz görünüyorsa, sor: "Şimdilik elimdekilerden oluşturabilirim, ancak kronoloji eksik olacak. Başka bir şey işaret etmek ister misiniz? Kilit e-postalar, sözleşmeler, iç yazışmalar, üretim mektupları?"

**`--belgeler` modu:**

1. **Üretim çıktısı / Bates seti** — kullanıcı üretim dizinini veya bir bildirimi işaret eder; skill Bates aralığı + tarihle okur.
2. **E-keşif bağlayıcısı** — MCP bağlayıcısı mevcutsa, muhafız + tarih aralığına göre çek.
3. **Muhafız dosyaları** — kullanıcı ham muhafız posta kutuları veya sürücü çıktıları sağlarsa, bunları da oku.
4. **Sor** — kilit bir muhafız veya tarih aralığı için kapsam ince görünüyorsa, sor.

### Adım 2: Çek + Oku

Her okunabilir dosyaya sahip kaynak için:

- **PDF'ler, e-postalar (.eml), .docx, .txt** — doğrudan oku.
- **E-posta arşivleri (Gmail, Outlook)** — MCP bağlayıcısı doğrulandıysa, tarih aralığı + karşı taraf / anahtar terimlerle sorgu yap; aksi hâlde kullanıcı ilgili konuları bir klasöre çıktı alır.
- **E-keşif platformları** — bağlayıcı mevcutsa, muhafız + tarih aralığına göre çek; aksi hâlde kullanıcı bir çıktı sağlar.

Skill beyan edilen bir kaynağa erişemiyorsa, sessizce devam etmek yerine çıktının Boşluklar bölümünde bunu açıkça belirt.

**Sessiz tamamlama yok.** Bir dönem için kaynak kapsamı ince görünüyorsa — iddia edilen zaman penceresinden beklenenden az belge, erişilemeyen bir muhafız posta kutusu, henüz gelmemiş bir üretim — ne bulunduğunu raporla ve dur. Sormadan web aramasından, kamuya açık kayıt aramasından veya model bilgisinden boşlukları doldurma. Şunu söyle: "Kaynaklar [dönem / muhafız] için [N] olay döndürdü. Kapsam ince görünüyor. Seçenekler: (1) ek kaynaklara (Bates, klasör, posta kutusu) işaret et, (2) yapılandırıldıysa farklı bir MCP bağlayıcısı dene, (3) bu penceredeki kamuya açık kayıt olayları için web'i ara — sonuçlar `[web araması — doğrula]` olarak etiketlenecek ve güvenmeden önce birincil kaynağa karşı kontrol edilmeli, veya (4) burada dur ve boşluğu not et. Hangisini istersiniz?" Avukat, daha düşük güvenilirlikli kaynakları kabul edip etmemeye karar verir; skill karar vermez.

**Kaynak atıfı.** Her kronoloji girdisini olayın gerçekte nereden geldiğiyle etiketle: alınan belgelerden çıkarılan olaylar için dosya yolu, Bates numarası, MCP bağlayıcısı veya beyan edilen belge depolama kaynağı (Kaynaklar sütununda zaten yakalandı). Alınan belgeden izlenemeyen herhangi bir olay veya tarih için — ör. model eğitim verisinden hatırlanan bir olgu, web aramasıyla bulunan bir kamuya açık kayıt olayı — satır içi etiketle: `[web araması — doğrula]`, `[model bilgisi — doğrula]` veya `[kullanıcı verdi]`. `doğrula` ile etiketlenen girdiler, araçla alınan girdilerden daha yüksek imalat riski taşır ve önce kontrol edilmeli. Etiketleri asla çıkarma veya birleştirme — bunlar avukatın dilekçeye çekmeden önce hangi girdileri doğrulayacağına dair en hızlı sinyalidir.

**Etiketleme, yalnızca zaman çizelgesi girdilerini değil, bir hukuki sonuç, son tarih veya hesaplanmış tarih belirten her bölümü kapsar.** Zaman çizelgesi belgelerden kaynaklıdır. Boşluklar bölümü, Kilit olaylar bölümü, Teori bağlantı satırları ve zamanaşımı, tolling olayı, başvuru son tarihi, keşif son tarihi veya ayrıcalık tespiti ifadeleri, skill'in kaynak olmadıkça model bilgisinden yazdığı hukuki analizdir. Her bu tür ifade bir provenance etiketi taşır: `[hesaplandı: <etiketli kural atfı>]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]` veya bu oturumda alındıysa bir araştırma bağlayıcısı etiketi.

### Adım 3: Olayları Çıkar

Her belge için tarihli olayları belirle:

- **E-posta:** `[tarih] [gönderen] [alıcıya] [konu/içerik] söyledi`
- **Toplantı:** `[tarih] [katılımcılar] [konu] hakkında görüştü` (takvim girişi veya notlara göre)
- **Karar:** `[tarih] [karar verici] [ne] kararı verdi` (belgeleyen belgeye göre)
- **Dilekçe / tutanak:** `[tarih] [taraf] [dilekçe/dava/yanıt] verdi`
- **Dış olay:** `[tarih] [bir şey oldu]` (sözleşme imzalandı, ürün piyasaya çıktı, düzenleyici davrandı, bir olay eşiği aştı)

Belge başına genellikle bir olay. Ara sıra sıfır (tarihsiz veya olay saptanmamış). Bazen birden fazla (birkaç kararı kapsayan toplantı özeti).

**Girdi başına gizlilik bayrağı (yalnızca gizlilik_durusu == B-karisik olduğunda). Üç durumlu kural — öznel bir ayrıcalık testinin karşılanmadığına sessizce karar verme:**

- `gizlilik: tamam` — kaynak **güvenle** ayrıcalıklı olmayan (dilekçeler, düzenleyici yazışma, kamuya açık belgeler, avukatımız olmadan karşı taraf iletişimi). Yalnızca makul bir ayrıcalık teorisi yoksa kullan.
- `gizlilik: bayrak` — kaynak güvenle veya muhtemelen ayrıcalıklı (avukatla iletişim, iş ürünü notları, ayrıcalıklı taslaklar, ortak savunma materyali). **Belirsiz her şey için varsayılan** — baskın amaç değerlendirmesi yakınsa, dava ihtimali sınırdaysa veya içerik karışıksa, buraya gider, `tamam`a değil.
- `gizlilik: incele` — yüzeysel olarak belirsiz kaynak, skill hiç karar veremedi (gönderen/alıcı meta verisi yok, okunamaz, vb.).

`gizlilik: bayrak` veya `gizlilik: incele` olduğunda, avukat inceleme sırasında görsün diye satır içi `[UZM DOĞRULA: gizlilik durumu]` ekle. Az-işaretleme gizliliği kaldırır (tek yönlü kapı); fazla-işaretleme avukat tarafından incelemede düzeltilir (çift yönlü kapı). Geri alınabilir hatayı tercih et.

### Adım 4: Tekilleştir

Aynı olay birden fazla belgede yüzeye çıkar: bir toplantı üç takvimde ve özet bir e-postada bulunuyor — bu **dört kaynaklı bir olay**, dört olay değil. Birleştir. Birleştirilmiş girdi tüm kaynakları atıflar.

### Adım 5: Önem Derecesini Etiketle — Dava Teorisine Göre

`matter.md`'den (`--dosya` modu) veya yapılandırmanın `## Dava teorisi` bölümünden (`--belgeler` modu) pivot olguyu ve kilit olguları oku. Her olayı etiketle:

- 🔴 **Kilit** — olay pivot olgunun veya aleyhimize/lehimize kilit bir olgunun parçası
- 🟡 **İlgili** — bağlam, kalıp delil, ikincil argümanı destekler
- ⚪ **Arka plan** — eksiksizlik için yararlı, dilekçeye girmeyecek

**Disiplin:** 300 🔴 etiketiyle 300 girdili bir kronoloji etiket taşımaz. 🔴'yü gerçekten bir gerçeği bulanı hareket ettirecek olaylar için sakla. Şüpheliysen, 🟡.

**Sınır etiketleme:** Bir girdi 🔴 ile 🟡 arasında (veya 🟡 ile ⚪ arasında) kaldığında, daha düşük önem derecesinde etiketle ve satır içi `[UZM DOĞRULA — sınır önem derecesi değerlendirmesi]` ekle. Avukatın yargısı skill'in değerlendirmesini geçersiz kılacak. Güvenle fazla etiketleyen bir kronoloji, belirsizliğini yüzeye çıkaran birinden daha az kullanışlıdır.

### Adım 6: Yaz

Varsayılan çıktı çalışma kronolojisidir. İstek üzerine çeşitler.

## Çıktı Formatları

### Çalışma Kronolojisi (Varsayılan)

Konum: `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/kronoloji.md`. Eksiksiz, etiketli, dipnotlu. Avukatın üzerinde çalıştığı referans belgesi.

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar — role göre farklılaşır; bkz. `## Bunu Kim Kullanıyor`]

> **Gizlilik devrimi.** Bu kronoloji, avukat-müvekkil ayrıcalığı, iş ürünü koruması, ortak çıkar / ortak savunma materyali içerebilen veya bunların karışımından oluşan dosya belgelerinden türetilmiştir. Kaynakların koruma statüsünü devralar. Ayrıcalık çemberinin ötesinde dağıtmak — nişanlılık dışındaki iş paydaşlarına, karşı vekile, bir düzenleyiciye — hem kronoloji hem de temel kaynaklar üzerinde feragat yaratabilir. Ayrıcalıklı dosya materyaliyle birlikte sakla, ev gizlilik konvansiyonlarıyla tutarlı şekilde işaretle ve dağıtım kararlarını kasıtlı olarak ver. Aşağıda yakalanan gizlilik duruşu seçimi, sonraki herhangi bir dağıtım değerlendirmesi için provenance damgasıdır.

# Kronoloji — [Dosya Adı]

> Önem etiketleri (🔴/🟡/⚪) ve gizlilik bayrakları (🔒) herhangi bir dış iş ürününde (dilekçeler, olgular beyanı, yönetim kurulu notu, dış avukat teslimatı) kullanımdan önce `[UZM DOĞRULA]` gerektiren ilk geçiş okumalardır.

**Dosya:** [slug]
**Mod:** dosya | belgeler
**Oluşturuldu:** [YYYY-AA-GG]
**Kaynaklar:** [kaynak türleri genelinde N belge]
**Girdiler:** [N] ([N] 🔴 / [N] 🟡 / [N] ⚪)
**Pivot olgu:** [tek cümle]
**Gizlilik duruşu:** A-temiz | B-karisik | C-iptal
**İşaretlenmiş girdiler:** [N] 🔒 *(yalnızca duruş == B-karisik olduğunda mevcut)*

---

## Zaman Çizelgesi

| Tarih | Olay | Etiket | 🔒 | Kaynaklar |
|---|---|---|---|---|
| [YYYY-AA-GG] | [ne oldu, tek cümle] | 🔴/🟡/⚪ | [boş / 🔒-bayrak / 🔒-incele] | [dosya yolları veya Bates] |

---

## Kilit Olaylar (Yalnızca 🔴)

[Çıkarıldı, her biri teoriye neden önem taşıdığına dair bir satırla.]

### [tarih] — [olay başlığı]
- Ne: [tek satır]
- Teori bağlantısı: [bu neden önem taşıyor]
- Kaynaklar: [liste]

---

## Boşluklar

**Olaysız tarih aralıkları:**
[aralıklar — bu dönem için belgeler nerede?]

**Beklenen ama eksik:**
[belgelenmesini bekleyeceğimiz ama göremediğimiz olaylar — ör. "2024-06 ile 2025-03 arasındaki sözleşme değişiklikleri — üretilmedi"]

**Okunamayan kaynaklar:**
[bu çalıştırmada CLAUDE.md'de beyan edilen ama erişilemeyen kaynaklar — ör. "UYAP — MCP bağlayıcısı yok; çıktı gerekli"]

---

## İşaret Disiplini

- `[DOĞRULA: olgusal iddia — tarih, katılımcılar, içerik]` — temel belgeye karşı henüz teyit edilmedi
- `[BELİRSİZ: hukuki nitelendirme — ör. bir olayın düzenleyici tetikleyici oluşturduğu]`
- `[ATI GEREKLİ: Bates / sergi / tutanak sayfa:satır]`
- `[UZM DOĞRULA: gizlilik durumu | sınır önem derecesi değerlendirmesi]` — avukat yargısı gerekli

---

## Sürüm
- v[N] [tarih]'te [kaynak özeti]nden oluşturuldu
- v[N-1] [tarih]'te oluşturuldu (önceki, aşıldı)
```

### Olgular Beyanı Kronolojisi (İstek Üzerine)

Yalnızca 🔴 ve ilgili 🟡'ye filtrele. Kronolojik anlatım sırasında düz metin olarak sun — dilekçenin olgu bölümünün iskeleti, kayıt atıflarıyla.

**Gizlilik filtresi varsayılanı:** `gizlilik_durusu == B-karisik` olduğunda, 🔒-bayrak ve 🔒-incele girdiler varsayılan olarak **hariç tutulur**. Olgular beyanı çeşidi nihai dış kullanım için tasarlanmıştır (dilekçeler, açıklamalar, müzakere eden karşı taraf) — 🔒 girdiler avukat gizlilik durumunu teyit edene kadar oraya gitmez. Kullanıcı yine de 🔒 girdileri dahil etmek isterse, açık `--bayraklilari-dahil-et` onayı gerekir; onay çıktı başlığında kalıcı kayıt olarak yakalanır.

### Tanığa Özgü Kronoloji (İstek Üzerine)

Adlandırılmış bir tanığın gönderici, alıcı, katılımcı veya konu olduğu olaylara filtrele. Tanık hazırlığını besler ve tanığın ne zaman ne bildiğini yeniden yapılandırmaya yardımcı olur.

## Artımlı Oluşturmalar

`kronoloji.md` mevcutsa:

- Önceki sürümü oku
- Mevcut kaynaklardan yeni kronoloji oluştur
- Fark: yeni olaylar (son oluşturmadan bu yana), değiştirilmiş girdiler (mevcut olaylara yeni kaynaklar eklendi), kaldırılan girdiler (nadir; nedenini not et)
- Önceki sürüm numarasını koru; `v[N+1]` ile yeni sürüm yaz
- Neyin değiştiğinin özetini çıktıla

## matter.md / history.md ile Entegrasyon

**Kasıtlı olarak ayrı** (şirket-içi `--dosya` modu). `history.md`, avukatın çalışan günlüğüdür — kararlar, güncellemeler, usul dönüm noktaları, iç strateji notları. `kronoloji.md`, olguların savunuculuk yönlü zaman çizelgesidir. Örtüşürler ama birleşmezler:

- Saklama verildi → history.md'ye gider (iç eylem). Genellikle kronolojide değil (uyuşmazlığın olgusu değil).
- Karşı taraf 14 Mart'ta ihlal bildirimi gönderdi → kronoloji.md'ye gider (🟡 — bilgilerini oluşturur). Ayrıca intake'te bahsedildiyse history.md'ye de.
- Karşılık tavsiye notumuz taslaklandı → yalnızca history.md.

Avukat kronolojide geçmiş olayları istediğinde, yapıştırabilir. Varsayılan, ayrı kalmaları.

## Bu Skill'in Yapmadıkları

- **Çelişkileri çözmek.** İki belge bir olayın ne zaman gerçekleştiği hakkında farklı şeyler söylediğinde, her iki girdi de bayrakla birlikte girer. Çözüm avukatın kararıdır; tanık görüşmesi veya ek keşif gerekebilir.
- **Kaynaklarda olmayan olayları icat etmek.** Belgelerde değilse (ve matter.md veya yapılandırmada yakalanmış bir olgu olarak değilse), kronolojide değildir — ama "Boşluklar" bunu eksik olarak işaret edebilir.
- **Tamlığı garanti etmek.** Kronoloji kaynaklar kadar iyidir. E-keşif üretimi devam ediyorsa ve yalnızca %20'si geldiyse, kronoloji bunu yansıtır. Sınırlamanın adını koy.
- **Kullanıcı adına ayrıcalık durumuna karar vermek.** Adım 0 kapısı duruş seçimini zorlar; girdi başına `gizlilik` bayrağı ilk geçiş sınıflandırmasını yakalar. Gerçek ayrıcalık tespitleri avukatın kararıdır, `[UZM DOĞRULA]` bayraklarına göre.