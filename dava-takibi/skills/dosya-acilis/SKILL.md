---
name: dosya-acilis
description: Yeni dosya intakesi — kimlik tespiti, menfaat çatışması taraması, kaynak, risk triyajı, önemlilik, dış avukat, sahipler, delil saklama ve kilit tarihler dahil tekdüze sorular; matter.md ve history.md oluşturur, _log.yaml'a yapılandırılmış satır ekler. Kullanıcı "yeni dosya", "dosya aç", "intake" dediğinde veya yeni bir davayı portföye almak istediğinde kullan.
argument-hint: "[isteğe bağlı dosya adı]"
---

# /dosya-acilis

1. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` yükle → risk kalibrasyonu (triyaj için), manzara (bağlam, çatışma yöntemi), paydaşlar (kimi dahil edeceğiz).
2. Aşağıdaki iş akışını ve referansı uygula.
3. Tekdüze intakei çalıştır: kimlik tespiti, çatışma taraması, kaynak, risk triyajı, önemlilik, dış avukat, iç sahipler, delil saklama, kilit tarihler, ilk duruş.
4. Dosya adından slug üret (küçük harf, kısa çizgi, yıl).
5. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` oluştur — tam anlatı intake.
6. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` oluştur — intakei ilk kayıt olarak ekle.
7. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` dosyasına yapılandırılmış satır ekle.
8. Kullanıcıyla teyitle: "Şu satırı yazacağım — düzeltme var mı?"

---

# Dosya Açılışı

## Amaç

Her yeni dosya aynı intakeden geçer; bu sayede portföy karşılaştırılabilir kalır. `_log.yaml`'daki tekdüze satırlar durum skill'inin toplu görünüm çıkarmasını sağlar. `matter.md`'deki anlatı, satırın tutamadığı bilgiyi yakalar. Burada oluşturulan geçmiş dosyası, olay kaydı haline gelir.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` — risk kalibrasyonu (triyaj eşikleri, önemlilik, sulh merdiveni), manzara (paydaşlar, dış avukat kadrosu).
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` — slug benzersizliğini teyit etmek için.

## İntake

### 1. Kimlik Tespiti

- Dosya adı (yaygın kullanılan, ör. "Acme - Alacak 2026")
- Karşı taraf
- Dosya türü: `sozlesme | is-hukuku | fikri-mulkiyet | duzenleyici | sorusturma | urun | diger`
- Tarafımızın rolü: `davaci | davali | talep-eden | muhatap | sorusturulan`
  - Pratik profilindeki `## Taraf` varsayılan ayarıysa, rolü oradan önceden doldur ve teyit et. `## Taraf` "dosyaya göre değişir" diyorsa soğuk sor. Pratik profilinin belirlemediği bir duruşu sessizce varsayma.
  - Rol, alt skill'leri etkiler: davacı duruşundaki dosyalar dava değeri / başarı primi ekonomisine yönlendirilir; davalı duruşundakiler maruziyet / karşılıklar / sigorta ihbarına yönlendirilir.
- Yargı çevresi (mahkeme, tahkim kurumu veya düzenleyici kurum)

### 2. Çatışma Taraması

Devam etmeden önce `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` → Menfaat çatışması taramasına göre çatışma adımını çalıştır.

- **Durum:** `temizlendi | beklemede | yapılmadi | feragat-edildi`
- **Yöntem:** `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'nin beyan ettiğiyle eşleş (`sirketler-hukuku-ekibi | dis-avukat | sistem-kontrolu | gayriresmi | diger`). Beyan edilen yöntem `gayriresmi` ise bunu kaydet — kaydın hâlâ avukat kanaatine dayandığını yansıtır.
- **Temizleyen:** ad / ekip / büro
- **Temizlenme tarihi:** YYYY-AA-GG
- **Karşı kontrol edilenler:** kontrol edilen belirli ad/varlıkların kısa listesi (karşı taraf, bilinen iştirakler, karşı vekil [biliniyorsa], önemli tanıklar). Kısa olabilir; "hayır" kabul edilmez.
- **Notlar:** işaretlenen ama temizlenen her şey (ör. "Smith 2019–2021 karşı tarafın yönetim kurulundaydı — bu davayla örtüşmediği için temizlendi").

Duruma göre davranış:

- `temizlendi` → devam et.
- `beklemede` → intakeye devam et; `matter.md`'de ve log satırında çatışmanın beklemede olduğunu belirt; her `/dosya-guncelleme` ve `/portfoy-durumu`'nda çözülene kadar tekrar yüzeye çıkar.
- `feragat-edildi` → nadirdir; çatışma feragati gerekçesi gerektirir (feragat yazmak bu skill'in kapsamı dışında — bir tane olduğunu, kimin imzaladığını ve nerede durduğunu kaydet).
- `yapilmadi` → **DUR. Bu bir kapıdır.** Skill, çatışma durumu çözülene kadar `matter.md`, `history.md` veya `_log.yaml` kaydı oluşturmaz. Kabul edilebilir üç yol:

  **Yol 1 — Şimdi çatışma taraması yap.** Bu intakei durdur. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` Çatışma taramasına göre temizle. `durum: temizlendi` veya `durum: feragat-edildi` (gerekçesiyle) olarak geri dön.

  **Yol 2 — Sahibi ve son tarihi olan "beklemede" olarak işaretle.** Yalnızca `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` Çatışma taraması paralel intakei kabul edilebilir ilan ediyorsa izin verilir. Şunları kaydet: çatışmayı kim yürütüyor, ne zaman sonuç bekleniyor, hangi varlıkları kontrol ediyorlar. İntake devam eder; dosya satırında `catisma.durumu: beklemede` bulunur; `/portfoy-durumu` her çalıştırmada işaretler; `/dosya-guncelleme` çözülene kadar tekrar sorar.

  **Yol 3 — Gerekçeli istisna.** Yalnızca kullanıcı istisnayı açıkça kabul ederse. `catisma.istisna` kısmına kaydet:

  ```yaml
  catisma:
    durum: yapilmadi               # olduğu gibi korunur
    istisna:
      tarafindan: [kullanıcı adı]
      tarih: [YYYY-AA-GG]
      gerekce: [neden çatışma atlandı — kalıcı kayıt; otomatik sona ermez]
  ```

  Bu alan her `/portfoy-durumu`'nda, her `/dosya-acilis` brifinginde ve her `/dosya-guncelleme`'de görünür. Çatışma gerçekten temizlenene kadar skill tarafından kaldırılmaz — yalnızca kullanıcının `_log.yaml`'ı açık şekilde düzenlemesiyle kaldırılabilir.

  **Sessizce devam etme.** "Sonra yaparım" kabul edilebilir bir yanıt değildir. Yol 1/2/3'ten biri seçilmeli ve seçim kayıtta tutulmalıdır.

Bu adım, skill'in bir çatışmanın var olup olmadığına karar verdiği anlamına gelmez — bu kullanıcının/firmanın yargısıdır. Taramanın yapıldığından ve kaydın bunu yansıttığından emin olmakla ilgilidir.

### 3. Kaynak

Bu nasıl geldi?
- `ihtarname | tebligat | celp | duzenleyici-talep | ic-bildirim | dava-oncesi-tehdit`
- *Tohum belge fırsatı:* "Başlatıcı belgeniz varsa (dava dilekçesi, ihtarname, celp), ekleyin veya yolu paylaşın. İntakei keskinleştirir."

### 4. Risk Triyajı — Ev Kalibrasyonuna Karşı

- Şiddet: yüksek | orta | düşük (pratik profilindeki şiddet bantlarını referans al)
- Olasılık: yüksek | orta | düşük (pratik profilindeki olasılık bantlarını referans al)
- Sonuç risk puanı (matrise göre): yüksek | orta | düşük | kritik
- Parasal maruziyet aralığı (en iyi tahmin)
- Parasal olmayan maruziyet (ihtiyati tedbir? idari yaptırım? kamuya duyurum? emsal?)

`~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'deki risk kalibrasyonu zayıfsa hassasiyeti zorlama. Kullanıcının sezgisini kullan ve zayıflığı kaydet.

### 5. Önemlilik

Pratik profilindeki ev eşiklerine göre (`~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`):
- `karsilik | aciklandi | izleniyor | yok`
- `karsilik` ise: karşılık tutarı ve mali işlerin bilgilendirilip bilgilendirilmediği
- `aciklandi` ise: KAP/SPK bildirimi ve dipnot konumu

> **Önemlilik — şirket-içi not:** TMS 37 karşılık eşiği ("olası VE güvenilir tahmin edilebilir") ve KAP/SPK kamuya açıklama yükümlülükleri yalnızca şirket-içi avukatlara uygulanır. Büro avukatı veya bağımsız uygulayıcıysanız bu bölümü boş bırakın veya müvekkile özgü çerçeveyle değiştirin. `[doğrulanacak]`

### 6. Dış Avukat

- Büro
- Sorumlu avukat
- **Sorumlu avukat e-posta** (`/karsi-vekil-durumu` tarafından durum talepleri taslaklamak için kullanılır)
- Vekaletname / ücret sözleşmesi durumu: `imzalandi | beklemede | yok`
- Bütçe yetkisi: tutar ve onaylayan
- *Tohum belge fırsatı:* "İmzalanmışsa vekaletname yolu."

Risk orta veya üstündeyse ve dış avukat atanmamışsa — işaretle.

### 7. İç Sahipler

`~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` manzarasından — hangi iç paydaşlar dahil?
- İş birimi yöneticisi
- İK partneri (iş hukuku dosyasıysa)
- Kurumsal iletişim (itibar riski varsa)
- Bilgi Güvenliği (veri veya siber dosyasıysa)
- Diğer

### 8. Delil Saklama

- Bildirim gönderildi mi? Evet ise: tarih, kapsam, muhafızlar (isim listesi).
- Sonraki tazeleme tarihi (varsayılan: bildirimden altı ay sonra; dosyaya göre ayarla).
- Hayır ise ve bu aktif dava veya makul ölçüde öngörülebilir davayla ilgiliyse: acilen işaretle; intake tamamlandıktan sonra `/dava-takibi:delil-saklama [slug] --ver` çalıştırmayı teklif et.
- *Tohum belge fırsatı:* "Verilmişse saklama bildirimi."

### 9. Kilit Tarihler

- Yanıt son tarihi (cevap, itiraz, karşı dilekçe)
- Sonraki duruşma / ön inceleme
- Zamanaşımı son tarihi (uygulanabiliyorsa)
- Herhangi bir düzenleyici son tarih

### 10. İlk Duruş

Bir paragraf teori:
- Bizim hikayemiz ne?
- Karşı tarafın hikayesi ne?
- Pivot olgu nedir?
- İlk duruş: `mücadele | sulh | soruştur | bekle`

## Çıktı Yazımı

### Slug

Küçük harf, kısa çizgi, sonda yıl. Örnekler: `acme-alacak-2026`, `is-smith-2026`, `rekabet-kurumu-2026`.

`_log.yaml`'da slug'ın benzersiz olduğunu yazmadan önce teyit et.

### `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md`

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar — role göre farklılaşır; bkz. `## Bunu Kim Kullanıyor`]

# [Dosya Adı]

**Slug:** [slug]
**Açılış:** [YYYY-AA-GG]
**Rolümüz:** [davaci/davali/vb.]
**Durum:** [durum]

---

## Kimlik Tespiti

[karşı taraf, yargı çevresi, dosya türü, kaynak]

## Çatışma

**Durum:** [temizlendi / beklemede / yapilmadi / feragat-edildi]
**Yöntem:** [sirketler-hukuku-ekibi / dis-avukat / sistem-kontrolu / gayriresmi / diger]
**Temizleyen:** [ad]
**Temizlenme tarihi:** [YYYY-AA-GG]
**Karşı kontrol edilenler:** [kontrol edilen varlıklar]
**Notlar:** [işaretlenen ama temizlenen her şey, varsa feragat referansı]

## Risk Triyajı

**Şiddet:** [bant] — [neden, ev şiddet tanımlarına referansla]
**Olasılık:** [bant] — [neden]
**Risk puanı:** [yüksek/orta/düşük/kritik]
**Maruziyet:** [para aralığı + parasal olmayan]

## Önemlilik

[karsilik/aciklandi/izleniyor/yok — karşılık tutarı, açıklama konumu veya "yok" ise gerekçe]

## Dış Avukat

[büro, sorumlu, vekaletname durumu, bütçe]

## İç Sahipler

[paydaşlar ve her birinin neden dahil olduğu]

## Delil Saklama

[durum, tarih, kapsam]

## Kilit Tarihler

[liste]

## İlk Teori

[bir paragraf: bizim hikayemiz, karşı tarafın hikayesi, pivot olgu, ilk duruş] `[SME ONAYLA — intake'teki teori çalışma hipotezidir; herhangi bir dilekçe veya bu çerçeveyi varsayan önemli iletişimden önce dış avukatla teyit et]`

## Açık Sorular

[henüz bilinmeyen ama önemli her şey — ör. "sigorta ihbarı beklemede", "X için teminatımız olup olmadığı belirsiz"]

---

## Tohum Belgeler

| Belge | Yol / işaretçi |
|---|---|
| [ör. dava dilekçesi] | [yol veya "henüz paylaşılmadı"] |
```

### `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md`

Geçmiş dosyasını intakeyi sıfır kayıt olarak ekleyerek başlat:

```markdown
# Geçmiş: [Dosya Adı]

Yalnızca ekleme yapılan olay kaydı. En son en üstte.

---

## [YYYY-AA-GG] — Dosya Açıldı

[Kaynak, kim getirdi, ilk triyaj özeti, dış avukat atandı, delil saklama bildirimi gönderildi/gönderilmedi.]
```

### `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` Dosyasına Ekle

Şemaya göre satır ekle. Örnek:

```yaml
- id: acme-alacak-2026
  ad: "Acme A.Ş. - Alacak Davası"
  tur: sozlesme
  rol: davali
  karsi_taraf: "Acme A.Ş."
  yargi_cevresi: "İstanbul Asliye Ticaret Mahkemesi"
  # durum kaynaktan türer:
  #   kaynak: dava-oncesi-tehdit | ihtarname            → durum: tehdit
  #   kaynak: tebligat | celp | duzenleyici-talep       → durum: aktif
  #   kaynak: ic-bildirim                               → durum: tehdit (varsayılan) veya resmi süreç başladıysa aktif
  durum: aktif
  asama: dilekce
  kaynak: tebligat
  dis_avukat:
    buro: "Yılmaz Hukuk Bürosu"
    sorumlu: "Av. A. Yılmaz"
    eposta: "ayilmaz@yilmazhukuk.example.com"
    vekaletname: imzalandi
  catisma:
    durum: temizlendi
    yontem: sirketler-hukuku-ekibi
    temizleyen: "K. Demir"
    temizlenme_tarihi: 2026-04-20
    istisna:                   # yalnızca Yol 3 istisnasında doldurulur
      tarafindan: null
      tarih: null
      gerekce: null
  risk: yuksek
  onemlilik: karsilik
  maruziyet_araligi: "₺500K–₺2M"
  ic_sahipler:
    is_birimi_yoneticisi: "Fatma Şahin"
    ik_partneri: null
    kurumsal_iletisim: null
  delil_saklama:
    gonderildi: true
    tarih: 2026-02-15
    kapsam: "Satış org 2023–2026"
    muhafizlar: ["Fatma Şahin", "R. Çelik", "T. Kaya"]
    son_tazeleme: 2026-02-15
    sonraki_tazeleme: 2026-08-15
    serbest_birakildi: null
  ilgili_dosyalar: []
  acilis: 2026-04-20
  sonraki_son_tarih: 2026-05-15
  son_guncelleme: 2026-04-20
  yol: matters/acme-alacak-2026/
```

## Yazmadan Önce Teyit Et

Kullanıcıya satırı ve matter.md içeriğini göster:

> İşte yazacaklarım. Yanlış veya eksik bir şey görürseniz taahhüt etmeden önce belirtin.

## Sonraki Adımlar Karar Ağacıyla Kapat

CLAUDE.md `## Çıktılar` bölümüne göre sonraki adımlar karar ağacıyla kapat. Bu skill'in ürettiğine seçenekleri uyarla — beş varsayılan dal (X'i taslakla, eskale et, daha fazla olgu topla, izle ve bekle, başka bir şey) başlangıç noktasıdır, zorunluluk değil. Ağaç çıktının kendisidir; avukat seçer.

## Bu Skill'in Yapmadıkları

- **Çatışma taramasını kendisi yapmak.** Sonucu, durumu, yöntemi ve kontrol edilen varlıkları kaydeder. Gerçek temizleme ev pratik profilinin beyan ettiği sistemde (veya yargıda) gerçekleşir. Kullanıcı "temizlendi" derse skill bunu kabul eder ve metaveriyi kaydeder.
- İlk teoriyi belirlemek. Kullanıcının söylediklerini kaydeder; bir tane icat etmez.
- Delil saklama bildirimi göndermek. Eksikse işaretler. Kullanıcı bildirir.