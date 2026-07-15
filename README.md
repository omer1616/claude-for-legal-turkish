# claude-for-legal-turkish

Avukatlar için yapılmış bir AI asistan seti. Türk hukuku ve yargı sistemine göre uyarlanmış.

---

## Ne işe yarar?

Sözleşme inceliyorsun, dava dosyası hazırlıyorsun, bir çalışanla ilgili soruşturma açıyorsun ya da mevzuat takibi yapıyorsun — bu sistem her seferinde sıfırdan başlaman yerine sana yapılandırılmış bir iş akışı sunar: neye bakman gerektiğini hatırlatır, takip listeni tutar, taslak hazırlar.

Her çıktı senin incelemen için bir **taslaktır** — hukuki tavsiye değil, hukuki sonuç değil. İmzalayan, gönderen, mahkemeye sunan sensin.

> **Yeni mi başlıyorsun?** Alan bazlı eklentiler kapsamlıdır ama kurulumları daha uzundur.
> Sade ve hızlı bir başlangıç için **`hukuk-asistani`** eklentisini kur: dava/dosya takibi,
> sözleşme inceleme ve hazırlama, dilekçe yazımı, özetleme ve araştırma tek eklentide —
> kurulum 5 dakika, ek bağlantı gerekmez. Detaylar: [hukuk-asistani/README.md](hukuk-asistani/README.md)

---

## Kurulum

Kurulum tek seferliktir.

**Gereken:** [Claude Code](https://claude.com/claude-code) (terminalde çalışan sürüm) veya Claude Cowork (masaüstü uygulaması). Önünde Claude'un çalıştığı bir terminal penceresi varsa Claude Code'a sahipsin demektir.

**1. Bu klasörü indir.** `claude-for-legal-turkish` klasörünün tamamını bilgisayarına indir veya klonla. Aşağıdaki adımda tam yoluna ihtiyacın olacak (ör. `/Users/adiniz/Downloads/claude-for-legal-turkish`).

**2. Eklenti kaynağını ekle.** Claude Code'da şunu yaz (sonuna bir boşluk bırakarak):

```
/plugin marketplace add
```

Sonra indirdiğin klasörü terminal penceresinin üzerine sürükle — yol otomatik dolar. Sürükleyemiyorsan tam yolu elle yazabilirsin: `/plugin marketplace add /Users/adiniz/Downloads/claude-for-legal-turkish`

**3. Kendi alanındaki eklentiyi kur.** Aşağıdaki tablodan seç, sonra:

```
/plugin install ticari-hukuk@claude-for-legal-turkish
```

(Örnekte ticari hukuk gösterildi — kendi alanının slug'ını yaz: `hukuk-asistani` (genel/başlangıç), `dava-takibi`, `sirketler-hukuku`, `is-hukuku`, `fikri-mulkiyet`, `mevzuat-takibi`, `eklenti-merkezi`. Birden fazla alanla ilgileniyorsan hepsini kurabilirsin, birbirine karışmazlar. Hangisinden başlayacağını bilmiyorsan `hukuk-asistani` ile başla.)

**4. Claude Code'u yeniden başlat.** Kapat, tekrar aç. Bu adım zorunlu — atlarsan eklenti komutları çalışmaz.

**5. İlk kurulum görüşmesini çalıştır.** Her eklenti işe başlamadan önce seni tanır:

```
/ticari-hukuk:ilk-kurulum
```

Risk toleransını, ekip yapını, kurum üslubunu sorar — sohbet havasında, 2-15 dakika. Öğrendikleri `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` dosyasına düz Türkçe yazılır. Bu bir ayar dosyası değil, senin de açıp düzenleyebileceğin bir belge.

**6. (Önerilir) Bir araştırma aracı bağla.** Lexpera, Kazancı veya mevzuat.gov.tr gibi bir bağlayıcı yoksa her hukuki atıf `[model bilgisi — doğrula]` etiketiyle işaretlenir — yani kaynağın eğitim verisi olduğu ve doğrulanmadığı belirtilir. Bağlarsan doğrulamayı senin yerine yapar. İkisinde de sistem çalışır, bağlı olan daha güvenilir atıf üretir.

> **Kurulum kapsamı hakkında:** Kurulum sırasında "bu proje için mi, tüm projeler için mi (kullanıcı kapsamı)" sorusu çıkarsa **kullanıcı kapsamını** seç. Proje kapsamı kulağa daha güvenli gelse de, eklentinin proje klasörü dışındaki dosyaları (İndirilenler'deki taslak, Dropbox'taki müvekkil dosyası) okumasını engeller. Kullanıcı kapsamı eklentiye ekstra erişim vermez, sadece hangi klasörden çalıştığının önemini kaldırır.

---

## Kullanım Senaryoları

### "Karmaşık yapı istemiyorum — günlük işlerim için sade bir asistan lazım"

`hukuk-asistani` eklentisi. Bir avukatın günlük ihtiyaçlarını tek eklentide toplar:
dava/dosya takibi, sözleşme inceleme ve hazırlama, dilekçe ve ihtarname taslağı,
karar/rapor özetleme, hukuki araştırma. Kurulumu beş soru sürer; belgelerin
`Belgeler/Hukuk-Asistani` klasöründe düz dosya olarak durur.

**Adım adım:**

1. İlk kullanımda bir kere: `/hukuk-asistani:ilk-kurulum` — 5 kısa soru, ~3 dakika
2. Yeni dava geldiğinde: `/hukuk-asistani:yeni-dosya`
3. "Bu hafta neyim var?": `/hukuk-asistani:dosyalarim`
4. Duruşmadan döndüğünde: `/hukuk-asistani:dosya-notu`
5. Sözleşme, dilekçe, özet, araştırma: `/hukuk-asistani:sozlesme-incele`, `:sozlesme-hazirla`, `:dilekce`, `:ozetle`, `:arastir`

Komut ezberlemek gerekmez — "kiracıya tahliye ihtarnamesi lazım" gibi normal bir cümle
yeterli. Tüm liste için: `/hukuk-asistani:yardim`

---

### "Karşı taraf bana bir sözleşme gönderdi, bakabilir misin?"

`ticari-hukuk` eklentisi. Sözleşme türünü kendisi tanır (NDA, SaaS aboneliği, tedarikçi anlaşması) ve doğru inceleme akışına yönlenir. Müvekkile gönderilecek özeti, itiraz edilmesi gereken maddeleri ve eskalasyon gerektiren noktaları tek bir çıktıda verir.

**Adım adım — bir SaaS sözleşmesi örneği:**

1. İlk kullanımda bir kere: `/ticari-hukuk:ilk-kurulum` — satış mı satın alma tarafındasın, hangi maddelerde ne kadar esnek olduğun (sorumluluk sınırı, otomatik yenileme, veri işleme şartları), eskalasyon zincirin sorulur. Elindeki son birkaç imzalı sözleşmeyi de isteyebilir, gerçek pozisyonlarını örüntüden çıkarmak için.

2. Sözleşmeyi ver: `/ticari-hukuk:sozlesme-inceleme saas-sozlesmesi.pdf`

3. Çıktıda göreceklerin:
   - Üstte gizlilik başlığı: `GİZLİ — AVUKATIN YÖNLENDİRMESİYLE HAZIRLANMIŞTIR`
   - Playbook'undan sapan maddelerin listesi, her biri için somut redline önerisi
   - Otomatik yenileme, fiyat artışı, veri taşınabilirliği gibi SaaS'a özgü riskli maddeler, işaretlenmiş
   - En üstte bir **⚠️ İnceleyen notu**: hangi sayfaların okunduğu, hangi kalemlerin senin yargını beklediği, atıfların doğrulanıp doğrulanmadığı — tek bakışta
   - En altta bir karar ağacı:
     > **Sırada ne var?**
     > 1. Redline'lı bir yanıt taslağı hazırlayayım
     > 2. Bunu eskalasyon eşiğindeki onaylayıcıya yönlendireyim
     > 3. Karşı tarafa sorulacak 2-3 soru hazırlayayım
     > 4. Bekletip izleyeyim

   Bir seçenek söylersin, o işi yapar — analizi tekrar anlatmaz.

Diğer komutlar: `/ticari-hukuk:yenileme-takibi` (önümüzdeki 90 günde ne yenileniyor), `/ticari-hukuk:eskalasyon-isaretleyici` (bir sorunu doğru onaylayıcıya yönlendir), `/ticari-hukuk:degisiklik-gecmisi` (bir sözleşmenin zeyilnamelerle nasıl değiştiğini izle).

---

### "Bu davayı devraldım, nerede kaldığımızı anlamam lazım"

`dava-takibi` eklentisi. Yeni bir dosyaysa açar, devraldığın bir dosyaysa kaydından ve tarihçesinden okunmuş bir brifing hazırlar: kim kim, ne iddia ediliyor, hangi tarihler kritik, süre aşımı riski var mı.

**Adım adım:**

1. İlk kullanımda: `/dava-takibi:ilk-kurulum` — risk iştahını, önemlilik eşiklerini (ne zaman karşılık ayrılır, ne zaman yönetim kuruluna gider), sulh yetki merdivenini ve sık karşılaştığın uyuşmazlık türlerini öğrenir.

2. Yeni bir dosyaysa: `/dava-takibi:dava-kayit` — taraflar, olgular, talep tutarı, dava ihtimali sorulur; hem dosya klasörünü hem de portföy sicilindeki satırı oluşturur.

3. Derinlemesine brifing istersen (bir duruşma veya yönetim kurulu toplantısı öncesi): `/dava-takibi:dava-ozeti [dosya-adi]` — dosyanın kaydı ve tarihçesinden okunmuş, atıflı bir brifing, kurumunun yönetim kurulu notu formatında.

4. Portföyünün genel durumuna her an bakmak için: `/dava-takibi:portfoy-durumu` — risk dağılımı, yaklaşan son tarihler, uzun süredir hareket görmemiş dosyalar.

5. Yeni bir gelişme olduğunda: `/dava-takibi:dava-guncelle [dosya-adi]` — tarihli olayı dosya tarihçesine ekler.

Diğer komutlar: `/dava-takibi:kronoloji [dosya-adi]` (belge kaynaklarından tarihli olay çizelgesi), `/dava-takibi:yasal-saktedbir` (ihtiyati tedbir ver/yenile/kaldır/durum raporu), `/dava-takibi:dis-avukat-durum` (dış avukatlardan haftalık durum e-postası taslağı).

---

### "Bir çalışanımız hakkında şikayet geldi, disiplin soruşturması açmam gerekiyor"

`is-hukuku` eklentisi. Soruşturmayı adım adım götürür, notları düzenli tutar, kimin ne zaman bilgilendirileceğini işaretler.

**Adım adım:**

1. İlk kullanımda: `/is-hukuku:ilk-kurulum`
2. Soruşturmayı aç: `/is-hukuku:sorusturma-ac` — intake, kaynak kontrol listesi, kalıcı günlük oluşturur
3. Her tanık ifadesi veya belge geldikçe: `/is-hukuku:sorusturma-ekle`
4. Not yazman gerektiğinde: `/is-hukuku:sorusturma-notu` — meslek sırrı kapsamında soruşturma notu taslağı
5. İK'ya veya yönetime özet gerektiğinde: `/is-hukuku:sorusturma-ozeti` — hedef kitleye göre uyarlanmış özet

> **Kademe durumu — önemli:** İşten çıkarma incelemesi, ücret/saat SSS ve çalışan sınıflandırması gibi doğrudan 4857 sayılı Kanun'a dayanan bazı yetenekler bilinçli olarak bu sürümde yok — bir Türk iş hukukçusunun tasarımını bekliyor. Geri kalan her şey (soruşturma, izin takibi, işe alım incelemesi, uluslararası genişleme) çalışır durumda.

---

### "Müvekkilimin bir buluşu var, ne yapabiliriz?"

`fikri-mulkiyet` eklentisi. Önce bir ön temizlik taraması yapar, sonra 6769 sayılı Sınai Mülkiyet Kanunu çerçevesinde sonraki adımları seninle planlar.

**Adım adım:**

1. `/fikri-mulkiyet:ilk-kurulum`
2. Buluşu kayıt altına al: `/fikri-mulkiyet:bulus-alimi [bildirim]`
3. Benzer marka/patentleri tara: `/fikri-mulkiyet:temizlik-taramasi [marka]`
4. Ürünün serbestçe kullanılıp kullanılamayacağını (freedom-to-operate) kontrol et: `/fikri-mulkiyet:serbest-kullanim-triaji [ürün/kapsam]`
5. Portföy takibi için: `/fikri-mulkiyet:portfoy` — yaklaşan yenileme/harç son tarihleri

> **Not:** İçerik kaldırma bildirimi ve ihlal ihtarı/triyajı (5651 ve 6769'a göre yeniden tasarlanması gereken kısımlar) henüz bu sürümde yok.

---

### "Şirket birleşmesi var, due diligence başladı"

`sirketler-hukuku` eklentisi. Veri odası takibinden önemli sözleşme takvimine, kapanış kontrol listesine kadar tüm süreci organize eder.

**Adım adım:**

1. `/sirketler-hukuku:ilk-kurulum` (`--module m&a` ile M&A'ya özel modülü seçebilirsin)
2. Veri odası belgelerini incelet: `/sirketler-hukuku:due-diligence-sorun-cikartma [klasor]` — bulguları kurum kategorilerine göre çıkarır
3. Yapılandırılmış tablo incelemesi istersen: `/sirketler-hukuku:tablo-inceleme` — belge başına satır, veri noktası başına sütun, her hücre kaynağa atıflı, Excel çıktısı
4. Kapanışa yaklaşırken: `/sirketler-hukuku:kapani-kontrol-listesi` — eksikler, kritik yol
5. Yönetim kurulu kararı gerektiğinde: `/sirketler-hukuku:yazili-onay` (TTK m.390/7) veya `/sirketler-hukuku:yonetim-kurulu-tutanagi`

---

### "Yeni bir düzenleme çıktı, müvekkilimi nasıl etkiliyor?"

`mevzuat-takibi` eklentisi. Belirlediğin düzenleyici alanları (BDDK, SPK, EPDK, Rekabet Kurumu, KVKK gibi) izler, yeni bir mevzuat değişikliği çıktığında fark analizi çıkarır.

**Adım adım:**

1. `/mevzuat-takibi:ilk-kurulum` — izleme listeni, politika indeksini, önemlilik eşiğini tanımlar
2. Beslemeleri şimdi kontrol et: `/mevzuat-takibi:mevzuat-besleme-izleyici`
3. Belirli bir değişikliği politikanla karşılaştır: `/mevzuat-takibi:politika-farki [mevzuat]`
4. Açık uyum boşluklarını gör: `/mevzuat-takibi:bosluk-analizi`

---

### "Yeni bir hukuki araç var mı, onu kurmak istiyorum"

`eklenti-merkezi`. Topluluk tarafından yapılmış yeni hukuki eklentileri bulur, güvenlik taramasından geçirir (kötü niyetli kod var mı diye bakar), onayınla kurar.

**Adım adım:**

1. Ara: `/eklenti-merkezi:kayit-tarayici [sorgu]`
2. Güvenli olduğunu doğrula: `/eklenti-merkezi:eklenti-kalite-kontrol [eklenti]` — Hukuk Eklentisi Tasarım Çerçevesi'ne göre değerlendirir, prompt-enjeksiyon taraması içerir
3. Kur: `/eklenti-merkezi:eklenti-kurucu [eklenti]`

---

## Çıktılarda göreceğin işaretler

Her eklenti aynı işaretleme dilini kullanır — birinde öğrendiğin diğerinde de geçerli.

| İşaret | Anlamı |
|---|---|
| `GİZLİ — AVUKATIN YÖNLENDİRMESİYLE HAZIRLANMIŞTIR` | Bu iç bir analiz taslağı; dışarı göndermeden önce meslek sırrı kapsamını teyit et |
| `[doğrulanacak]` | Bir olgu veya atıf birincil kaynağa karşı henüz doğrulanmadı |
| `[incele]` | Burada bir avukat yargısı gerekiyor, sistem kendi başına karar vermedi |
| `[UZMAN DOĞRULA]` | Alandan bir uzmanın onayı olmadan güvenilmemeli |
| `⚠️ İnceleyen notu` | Çıktının en üstünde: ne okundu, ne doğrulandı, güvenmeden önce ne yapman gerekiyor — tek bakışta |
| `[Lexpera]` / `[Kazancı]` / `[mevzuat.gov.tr]` | Atıf, bağlı bir araştırma aracından bu oturumda gerçekten geldi |
| `[model bilgisi — doğrula]` | Atıf eğitim verisinden — araştırma aracından değil, güvenmeden önce kontrol et |

Bu işaretlerden biri hâlâ çözümlenmemişse, taslak ne kadar düzgün görünürse görünsün henüz nihai değildir.

---

## Mevcut Eklentiler

| Eklenti | Ne için | Durum |
|---|---|---|
| `hukuk-asistani` | Günlük genel kullanım — dosya takibi, sözleşme, dilekçe, özet, araştırma. **Başlangıç için önerilir** | Hazır |
| `dava-takibi` | Dava yönetimi, dosya takibi, dilekçe desteği | Hazır |
| `ticari-hukuk` | Sözleşme inceleme ve müzakere desteği | Hazır |
| `sirketler-hukuku` | Şirket işlemleri, M&A, genel kurul | Hazır |
| `is-hukuku` | İş hukuku, soruşturma, izin takibi | Hazır (kısmi*) |
| `fikri-mulkiyet` | Patent, marka, telif, sınai mülkiyet | Hazır (kısmi*) |
| `mevzuat-takibi` | Düzenleyici değişiklik izleme ve uyum | Hazır (kısmi*) |
| `eklenti-merkezi` | Yeni araçları bul, kur, yönet | Hazır |
| `kisisel-veri-kvkk` | KVKK uyumu, VERBİS, veri sahibi hakları | Hazırlanıyor |
| `urun-hukuku` | Ürün lansmanı, pazarlama, tüketici hukuku | Bekliyor |
| `yapay-zeka-yonetisimi` | YZ risk ve uyum | Bekliyor |

**\*Kısmi ne demek?** Bu üç eklentide, kaynağında doğrudan ABD/AB mevzuatına dayanan birkaç tekil yetenek bilinçli olarak eklenmedi — geri kalan her şey çalışır durumda. Detaylar ilgili eklentinin kendi README'sinde. Bir Türk hukukçusunun tasarımını beklemeden hiçbir şey "yaklaşık" olarak eklenmez; ilgili komut basitçe mevcut değildir.

---

## Nasıl çalışır?

1. **Kurulum** (yukarıdaki adımlar) bir kere yapılır. Sonrasında hangi klasörden çalıştığının önemi yok — Claude Code'da nerede olursan ol `/eklenti-adı:komut` yazman yeterli.

2. **İlk kurulum görüşmesi** seni tanır ve `~/.claude/plugins/config/claude-for-legal-turkish/<eklenti-adı>/CLAUDE.md` dosyasına yazar. Bunu istediğin zaman elle de düzenleyebilirsin, ya da ilgili eklentinin `ozellestir` komutuyla tek bir şeyi (bir eşiği, bir onaylayıcıyı) tüm görüşmeyi tekrarlamadan güncelleyebilirsin.

3. **Günlük kullanım** slash komutlarıyla (`/`) olur. Her eklentinin kendi komutları var, yukarıdaki senaryolarda örnekleri gösterildi.

4. **Profil gelişir.** Ne kadar kullanırsan sistem o kadar sana özel hale gelir — playbook pozisyonların, eskalasyon eşiklerin zamanla netleşir.

---

## Sorun giderme

- **"Komut bulunamadı"** → Kurulum adım 4'ü atlamışsındır, Claude Code'u yeniden başlat.
- **"Önce kurulum çalıştırın" uyarısı** → herhangi bir komuttan önce `/<eklenti-adı>:ilk-kurulum` çalıştırman gerekiyor.
- **Atıflar hep `[doğrulanacak]` çıkıyor** → bir araştırma aracı bağlı değil (Kurulum adım 6). Bağlı olmadan her atıf eğitim verisinden gelir.
- **"Bu dosyayı okuyamıyorum"** → muhtemelen eklenti proje kapsamında kurulmuş ve dosya proje klasörü dışında. "Kurulum kapsamı" notuna bak, kullanıcı kapsamında yeniden kur.
- **Aradığın işlev yok** → önce eklentinin kendi README'sindeki kademe notuna bak (yukarıdaki "kısmi" eklentiler). Değilse `/eklenti-merkezi:ilgili-eklentiler` ile daha uygun bir öneri alabilirsin.

---

## Önemli Notlar

- **Bu bir hukuki tavsiye sistemi değildir.** Son karar her zaman senindir. Sistem sana iş akışı, hatırlatma ve analiz desteği sunar; avukatlık hizmetinin yerini almaz.
- **Türk hukukuna göre yapılandırılmıştır.** Referanslar TBK, HMK, CMK, 4857, 6769, FSEK ve ilgili mevzuata göre düzenlenmiştir.
- **Verilerin bilgisayarında kalır.** Pratik profilin ve dosya kayıtların `~/.claude/plugins/config/claude-for-legal-turkish/` altında yerel olarak tutulur, eklenti güncellemelerinden etkilenmez.
- Bir çıktı sana yanlış geliyorsa sisteme söyle — profil kendini günceller.
