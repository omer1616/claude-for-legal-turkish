# Hukuk Asistanı

Avukatın günlük işleri için sade bir AI asistanı. Tek eklenti, on komut, beş dakikada kurulum.

---

## Ne işe yarar?

Yeni bir dava aldın, duruşmadan döndün, müvekkil bir sözleşme gönderdi, yarına ihtarname lazım, masanda 40 sayfalık bir bilirkişi raporu var — bu eklenti hepsinde aynı yerde duruyor: **dava ve dosya takibi, sözleşme inceleme ve hazırlama, dilekçe yazımı, hukuki metin özetleme ve genel hukuki araştırma.**

Bu setteki diğer eklentiler (dava-takibi, ticari-hukuk, is-hukuku…) birer uzmanlık alanına derinlemesine iner; kurulumları da ona göre uzundur. Hukuk Asistanı tersini yapar:

- **Kurulum beş kısa soru sürer.** Risk matrisi, şablon belge talebi, 15 dakikalık görüşme yok.
- **Ek bağlantı gerektirmez.** Hiçbir harici sistem (araştırma bağlayıcısı, UYAP entegrasyonu vb.) kurmadan, kutudan çıktığı gibi çalışır.
- **Belgelerin senin bilgisayarında durur.** Her şey `Belgeler/Hukuk-Asistani` klasöründe düz dosya olarak yaşar; istediğin programla açabilirsin.
- **Komut ezberlemek gerekmez.** "Yeni bir işçilik davası aldım" veya "şu sözleşmeye bak" yazman yeterli — asistan doğru aracı kendisi seçer.

Her çıktı senin incelemen için bir **taslaktır** — hukuki tavsiye değil, hukuki sonuç değil. İmzalayan, gönderen, mahkemeye sunan sensin.

---

## Kurulum

Kurulum tek seferliktir, yaklaşık 5 dakika sürer.

**Gereken:** [Claude Code](https://claude.com/claude-code) (terminalde çalışan sürüm) veya Claude Cowork (masaüstü uygulaması). Önünde Claude'un çalıştığı bir pencere varsa hazırsın demektir.

**1. Eklenti kaynağını ekle.** Claude Code'da şunu yaz:

```
/plugin marketplace add omer1616/claude-for-legal-turkish
```

İnternetten erişemiyorsan: `claude-for-legal-turkish` klasörünü bilgisayarına indir, `/plugin marketplace add ` yazıp (sonuna bir boşluk bırakarak) klasörü pencerenin üzerine sürükle — yol kendiliğinden dolar.

**2. Eklentiyi kur:**

```
/plugin install hukuk-asistani@claude-for-legal-turkish
```

**3. Claude Code'u yeniden başlat.** Kapat, tekrar aç. Bu adım zorunlu — atlarsan eklenti komutları çalışmaz.

**4. İlk kurulumu çalıştır:**

```
/hukuk-asistani:ilk-kurulum
```

Beş kısa soru sorar: bunu kim kullanacak, nasıl çalışıyorsun, hangi alanlarda, hangi ilde, belgeler nereye kaydedilsin. Bitti — her cevap sonradan değiştirilebilir (`/hukuk-asistani:ilk-kurulum --redo`).

> **Kurulum kapsamı hakkında:** Kurulum sırasında "bu proje için mi, tüm projeler için mi (kullanıcı kapsamı)" sorusu çıkarsa **kullanıcı kapsamını** seç. Proje kapsamı, eklentinin proje klasörü dışındaki dosyaları (İndirilenler'deki sözleşme, masaüstündeki karar) okumasını engeller.

---

## Kullanım Senaryoları

### "Yeni bir dava aldım"

`/hukuk-asistani:yeni-dosya` — ya da düz cümleyle: *"yeni bir kira davası aldım, müvekkil Ayşe Demir, kiracı çıkmıyor."*

**Adım adım:**

1. Asistan temel bilgileri sorar: müvekkil, konu, karşı taraf, mahkeme/esas no, aşama, kritik tarihler. **Sadece müvekkil ve konu zorunlu** — gerisini bilmiyorsan atla, sonradan tamamlanır.
2. `dosyalar/` altında dosya klasörünü açar, kaydı yazar, kritik tarihleri takvimine işler.
3. Bir tebliğ tarihi verip "süre ne zaman doluyor?" dersen hesabı **gösterir** ve `[doğrula — süre hesabı]` etiketiyle işaretler — son güne asistanın sözüyle güvenilmez, süre kaçırmanın telafisi yoktur.

### "Bu hafta neyim var?"

`/hukuk-asistani:dosyalarim`

Çıktıda göreceklerin:

- En üstte tek satır özet: `7 açık dosya · önümüzdeki 30 günde 4 kritik tarih · 2 dosya 30+ gündür işlem görmedi`
- **⚠️ Yaklaşan tarihler** — tarihe göre sıralı; geçmiş ama kapanmamış tarihler `🔴 GEÇMİŞ` etiketiyle en üstte
- Dosya tablosu: dosya, müvekkil, merci/esas, aşama, sonraki tarih, son işlem
- Uzun süredir el değmemiş dosyaların listesi

### "Duruşmadan döndüm / tebligat geldi"

`/hukuk-asistani:dosya-notu` — ya da: *"bugün Yılmaz dosyasının duruşması vardı, tanıklar dinlendi, yeni duruşma 12 Eylül."*

**Adım adım:**

1. Asistan doğru dosyayı bulur (emin olamazsa sorar).
2. Tarihli notu dosyanın kaydına ekler — eski notlar asla silinmez veya değiştirilmez.
3. Yeni tarihleri takvime işler, aşamayı günceller, ne değiştirdiğini tek satırda söyler.
4. Dava bittiyse *"dosyayı kapat"* de — sonucu sorar, arşivler (silmez), listeden düşürür.

### "Müvekkil bir sözleşme gönderdi, imzalasın mı?"

`/hukuk-asistani:sozlesme-incele sozlesme.pdf` — veya metni doğrudan yapıştır.

**Adım adım:**

1. İki hızlı soru: hangi taraf biziz, özel bir endişe var mı?
2. Sözleşmeyi baştan sona okur (okuyamadığı kısım varsa söyler — asla tamamını okumuş gibi yapmaz).
3. Çıktıda göreceklerin:
   - **Sonuç** — müvekkile telefonda söyleyeceğin paragraf: imzalanabilir mi, en kritik 2-3 nokta ne
   - **Risk tablosu** — 🔴/🟠/🟡/🟢 şiddet sıralı, madde numarası referanslı, her satırda somut değişiklik önerisi
   - **Eksik maddeler** — bu tür sözleşmede olması beklenip de olmayanlar
   - **Müzakere önerileri** — öncelik sırasıyla
4. En altta karar ağacı: redline taslağı mı, karşı tarafa e-posta mı, müvekkile sade özet mi? Birini seçersin, o işi yapar.

### "Sözleşme hazırlamam lazım"

`/hukuk-asistani:sozlesme-hazirla` — ya da: *"ofis için işyeri kira sözleşmesi lazım."*

Türü ve esaslı şartları (taraflar, bedel, süre) sorar; Türk hukukuna uygun, numaralı maddelerle **tam metin** taslak yazar. Bilmediği hiçbir değeri uydurmaz — tarih, tutar, unvan gibi boşluklar `[.........]` olarak kalır, hukuki tercih gerektiren yerler `[incele]` ile işaretlenir. Tür şekil şartına tabiyse (taşınmaz satış vaadi, kefalet gibi) taslaktan önce uyarır.

### "Dilekçe / ihtarname yazmam lazım"

`/hukuk-asistani:dilekce` — ya da: *"kiracıya tahliye ihtarnamesi lazım"* veya *"şu davaya cevap dilekçesi yazalım."*

**Adım adım:**

1. Türü belirler (dava, cevap, istinaf/temyiz, icra itirazı, ihtarname…) — konu kayıtlı bir dosyana aitse taraf ve olay bilgilerini oradan almayı önerir.
2. Olayları, talebi, delilleri toplar; cevap/istinaf yazıyorsan yanıt verilecek dilekçeyi veya kararı ister.
3. Mahkeme formatında taslak çıkarır: başlık, taraflar, KONU, AÇIKLAMALAR, HUKUKİ NEDENLER, HUKUKİ DELİLLER, SONUÇ VE İSTEM.
4. **İçtihat künyesi asla uydurmaz.** Emsal gerekiyorsa `[ATIF: emsal karar eklenecek — Lexpera/Kazancı taraması gerekli]` diye dürüstçe boşluk bırakır. Delile bağlanmamış kritik olgular `[DOĞRULA: …]` işareti taşır.

### "Bu karar / rapor ne diyor?"

`/hukuk-asistani:ozetle karar.pdf` — veya metni yapıştır.

Metnin türünü kendisi tanır ve ona göre özetler: mahkeme kararında künye-uyuşmazlık-gerekçe-hüküm; bilirkişi raporunda tespitler + **itiraza açık noktalar**; mevzuatta yükümlülükler + yürürlük. Alıntılar her zaman kelimesi kelimesine ve sayfa referanslıdır; özet yalnızca metinde olanı söyler.

### "Bunun hukuki durumu ne? / Güncel oran-eşik ne?"

`/hukuk-asistani:arastir` — ya da: *"işe iade davasında arabuluculuk şartı neydi?"*

Kısa cevap önce gelir; dayanak kanun maddeleri her zaman kaynak etiketiyle verilir. Güncel harç, faiz, parasal sınır gibi her yıl değişen konularda **model hafızasına güvenmez** — web'de resmî kaynaklara (mevzuat.gov.tr, resmigazete.gov.tr) bakar ve bulduğunu etiketler.

---

## Komutlar

| Komut | Ne yapar |
|---|---|
| `/hukuk-asistani:ilk-kurulum` | 5 soruluk kurulum; profil + çalışma klasörünü oluşturur |
| `/hukuk-asistani:yeni-dosya` | Yeni dava/iş dosyası açar, kritik tarihleri kaydeder |
| `/hukuk-asistani:dosyalarim` | Tüm dosyaların özeti — yaklaşan duruşma/süreler, hareketsiz dosyalar |
| `/hukuk-asistani:dosya-notu` | Dosyaya tarihli gelişme notu ekler; kapatma da buradan |
| `/hukuk-asistani:sozlesme-incele` | Madde madde risk raporu + müzakere önerileri |
| `/hukuk-asistani:sozlesme-hazirla` | Sıfırdan tam metin sözleşme taslağı |
| `/hukuk-asistani:dilekce` | Dilekçe / ihtarname taslağı, mahkeme formatında |
| `/hukuk-asistani:ozetle` | Karar, rapor, sözleşme, mevzuat özeti |
| `/hukuk-asistani:arastir` | Kaynak etiketli hukuki araştırma |
| `/hukuk-asistani:yardim` | Bu listeyi ve kullanım örneklerini gösterir |

---

## Belgelerin nerede saklanır?

Kurulumda seçtiğin klasörde (varsayılan: `Belgeler/Hukuk-Asistani`):

```
Hukuk-Asistani/
├── dosyalar/          # her dava/iş için bir klasör — kayıt, notlar, o dosyanın belgeleri
│   └── yilmaz-iscilik-alacagi/
│       ├── dosya.md           # dosya kaydı: bilgiler, tarihler, tarihli notlar
│       └── cevap-dilekce-v1.md
├── sozlesmeler/       # dosyaya bağlı olmayan sözleşme taslakları ve incelemeler
├── dilekceler/        # dosyaya bağlı olmayan dilekçe taslakları
├── ozetler/           # belge özetleri
└── arastirmalar/      # kaydedilen araştırma notları
```

Kural basit: çıktı kayıtlı bir dosyaya aitse o dosyanın klasörüne, değilse tür klasörüne yazılır. Hepsi düz metin — Word'e kopyalayabilir, yedekleyebilir, dilediğin gibi taşıyabilirsin. Profilin ise `~/.claude/plugins/config/claude-for-legal-turkish/hukuk-asistani/` altında durur ve eklenti güncellemelerinden etkilenmez.

---

## Çıktılarda göreceğin işaretler

Bu setteki tüm eklentiler aynı işaretleme dilini kullanır — burada öğrendiğin diğerlerinde de geçerli.

| İşaret | Anlamı |
|---|---|
| `GİZLİ — AVUKATIN YÖNLENDİRMESİYLE HAZIRLANMIŞTIR` | İç analiz taslağı; dışarı göndermeden önce meslek sırrı kapsamını teyit et |
| `⚠️ İnceleyen notu` | Çıktının en üstünde: ne okundu, ne doğrulanmadı, güvenmeden önce ne yapman gerekiyor |
| `[doğrula]` | Birincil kaynağa karşı henüz doğrulanmamış olgu/atıf |
| `[doğrula — süre hesabı]` | Asistanın hesapladığı bir son gün — kontrol etmeden güvenme |
| `[incele]` | Burada avukat yargısı gerekiyor; sistem kendi başına karar vermedi |
| `[model bilgisi — doğrula]` | Atıf eğitim verisinden geliyor — araştırma aracından değil |
| `[ATIF: …]` / `[DOĞRULA: …]` | Dilekçelerde: doldurulması/teyit edilmesi gereken boşluk |
| `[.........]` | Sözleşme taslaklarında: senin dolduracağın somut değer (tutar, tarih, unvan) |

Bu işaretlerden biri hâlâ çözümlenmemişse, taslak ne kadar düzgün görünürse görünsün henüz nihai değildir.

---

## Nasıl çalışır?

1. **Kurulum bir kere yapılır.** Sonrasında hangi klasörden çalıştığının önemi yok — `/hukuk-asistani:komut` yazman yeterli.
2. **Profil beş cevaptan oluşur** ve `~/.claude/plugins/config/claude-for-legal-turkish/hukuk-asistani/CLAUDE.md` dosyasında düz Türkçe durur. Elle düzenleyebilir veya `--redo` ile baştan yapabilirsin.
3. **Günlük kullanım doğal dille olur.** Komutlar kısayoldur; "müvekkil şunu sordu", "şu dosyaya not düş" gibi cümleler de aynı yere çıkar.
4. **Dosya kayıtların taşınabilir.** İleride `dava-takibi` gibi kapsamlı bir eklentiye geçersen kayıtların düz metin olduğu için yanında gelir.

---

## Sorun giderme

- **"Komut bulunamadı"** → Kurulum adım 3'ü atlamışsındır; Claude Code'u kapatıp yeniden aç.
- **"Önce kurulum çalıştırın" uyarısı** → `/hukuk-asistani:ilk-kurulum` çalıştırman gerekiyor — 3 dakika.
- **"Bu dosyayı okuyamıyorum"** → muhtemelen eklenti proje kapsamında kurulmuş ve dosya proje klasörü dışında. Kullanıcı kapsamında yeniden kur (yukarıdaki kurulum kapsamı notu) veya dosyayı çalışma klasörüne taşı.
- **Atıflar hep `[model bilgisi — doğrula]` çıkıyor** → Bu bir hata değil, dürüstlük: araştırma aracı bağlı değilken kaynağın eğitim verisi olduğu söylenir. Lexpera/Kazancı gibi bir bağlayıcı eklersen asistan onu kendiliğinden kullanır — ama hiçbiri zorunlu değil.
- **Dosyalarım listesinde bir kayıt görünmüyor** → `dosyalar/<klasör>/dosya.md` dosyasının üst bloğu bozulmuş olabilir; asistan bunu listenin altında bildirir, "düzelt" demen yeterli.

---

## Önemli Notlar

- **Bu bir hukuki tavsiye sistemi değildir.** Son karar her zaman senindir. Sistem sana kayıt, hatırlatma, taslak ve analiz desteği sunar; avukatlık hizmetinin yerini almaz.
- **UYAP'a bağlı değildir.** Duruşma günleri ve süreler sen söyledikçe kaydedilir; kalemin verdiği yeni bir günü asistan kendiliğinden göremez.
- **Süre hesapları daima teyit ister.** Asistan hesabı gösterir ve işaretler; son güne güvenmeden önce kontrol et.
- **İçtihat künyesi uydurmaz.** Emsal karar numarası ancak gerçek bir kaynaktan geldiyse yazılır. Bu bir eksiklik değil, güvenlik özelliğidir.
- **Türk hukukuna göre yapılandırılmıştır.** Yabancılık unsuru taşıyan işlerde asistan bunu fark eder ve çerçeve farkını açıkça söyler.
- **Gizlilik:** belgelerin bilgisayarında durur; ancak Claude ile paylaştığın içerik Anthropic'in hizmetinde işlenir — hassasiyeti yüksek belgelerde büronun/kurumunun politikasına uy.
- **Daha kapsamlı ihtiyaç doğarsa** aynı marketplace'te alan bazlı eklentiler var: `dava-takibi`, `ticari-hukuk`, `is-hukuku`, `fikri-mulkiyet`, `mevzuat-takibi`. Bir çıktı sana yanlış geliyorsa sisteme söyle — profil kendini günceller.
