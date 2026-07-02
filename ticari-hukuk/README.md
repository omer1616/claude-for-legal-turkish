# Ticari Hukuk Eklentisi

Şirket içi ticari sözleşme iş akışları: satıcı sözleşmesi incelemesi, NDA (gizlilik
sözleşmesi) triyajı, SaaS abonelik incelemesi, yenileme takibi, eskalasyon yönlendirmesi
ve iş birimi paydaşlarına dönük özetler. İlk-kurulum görüşmesinin yazdığı bir ekip
pratik profili etrafında kurulmuştur — eklenti *sizin* oyun kitabınızı öğrenir, genel
bir şablonu değil.

**Her çıktı avukat incelemesi için taslaktır — atıflı, işaretli ve kapılı — hukuki
sonuç değil.** Eklenti işi yapar: belgeleri okur, oyun kitabınızı uygular, sorunları
bulur, notu taslak haline getirir. Bir avukat inceler, doğrular ve karar verir. Atıflar
kaynağına göre etiketlenir, böylece hangisinin bir araştırma aracından geldiğini ve
hangisinin kontrol edilmesi gerektiğini bilirsiniz. Meslek sırrı/gizlilik işaretleri
temkinli uygulanır ki hiçbir şey yanlışlıkla feragat edilmesin. Sonuç doğuran eylemler —
gönderme, imzalama, yürürlüğe koyma — açık onay arkasında kapılıdır.

## Kimler için

| Rol | Birincil iş akışları |
|---|---|
| **Ticari hukuk müşaviri** | Satıcı sözleşmesi incelemesi, eskalasyon yönlendirmesi, paydaş özetleri |
| **Sözleşme yöneticisi / hukuk destek uzmanı** | NDA triyajı, yenileme takibi, ilk-geçiş incelemesi |
| **Satın alma** | Yenileme farkındalığı, alıcı olarak paydaş özetleri |
| **Satış / iş geliştirme** | Hukuka sormadan önce NDA'yı kendi kendine triyaj etme |

## İlk çalıştırma: ilk-kurulum

İlk kullanımda eklenti sizi görüşür — on dakika, sohbet havasında — ekibinizin gerçekte
nasıl çalıştığını öğrenmek için. Oyun kitabı pozisyonlarınızı, eskalasyon kurallarınızı
ve masanıza düştüğünde içinizi sıkan şeyi sorar. Sonra son imzalanmış 5-10 sözleşmeyi
(daha fazlası daha iyi, 20 tanesi daha net bir örüntü verir) ister, ki pozisyonlarınızı
doğada görebilsin.

Öğrendiklerini `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
dosyasına yazar — ekibiniz hakkında düz Türkçe bir belge, her başka skill bir şey
yapmadan önce bunu okur. Belgeyi siz düzenlersiniz, bir yapılandırma dosyasını değil.

```
/ticari-hukuk:ilk-kurulum
```

**Oyun kitabı tarafı.** Kurulumun erken bir adımında, bir **satış-tarafı** oyun
kitabı (ürününüzü/hizmetinizi satıyorsunuz; siz satıcısınız; genellikle kendi
kağıdınız), bir **satın alma-tarafı** oyun kitabı (satıcılardan alım yapıyorsunuz; siz
müşterisiniz; genellikle onların kağıdı) veya ikisini de kurup kurmayacağınız
sorulacak. Cevap neredeyse her oyun kitabı pozisyonunu tersine çevirir — sorumluluk
tavanları, tazminat yönü, fesih hakları, fikri mülkiyet sahipliği — bu yüzden en
başta önemlidir. İkisini de seçerseniz, kurulum önce satış-tarafını kurar; ardından
`/ticari-hukuk:ilk-kurulum --side purchasing` çalıştırarak diğerini kurun.
Yapılandırmanız ikisini de paralel tutar, inceleme skill'leri hangi tarafın geçerli
olduğunu oyun kitabını okumadan önce kontrol eder.

## Komutlar

| Komut | Ne yapar |
|---|---|
| `/ticari-hukuk:ilk-kurulum` | İlk-kurulum görüşmesini çalıştır (veya yeniden çalıştır) |
| `/ticari-hukuk:sozlesme-inceleme [dosya]` | Bir satıcı sözleşmesini, NDA'yı veya SaaS aboneliğini oyun kitabınıza göre incele |
| `/ticari-hukuk:yenileme-takibi` | Önümüzdeki 90 günde ne yenileniyor ve fesih-bildirim son tarihleri ne zaman |
| `/ticari-hukuk:eskalasyon-isaretleyici` | Bir sorunu doğru onaylayıcıya yönlendir ve talebi taslakla |
| `/ticari-hukuk:degisiklik-gecmisi [dosya(lar)]` | Bir sözleşmenin ana metni ve tüm değişiklikleri (zeyilname) boyunca nasıl değiştiğini izle |
| `/ticari-hukuk:teklif-inceleme` | İzleyici agent'ından gelen bekleyen oyun kitabı güncelleme tekliflerini adım adım gözden geçir |
| `/ticari-hukuk:dosya-calisma-alani` | Dosya çalışma alanlarını yönet (yalnızca çok-müvekkilli özel pratik) — yeni, listele, geç, kapat, yok |
| `/ticari-hukuk:ozellestir` | Pratik profilinizde tek bir şeyi değiştirin — tüm görüşmeyi yeniden çalıştırmadan |

## Skill'ler

| Skill | Amaç |
|---|---|
| **ilk-kurulum** | İlk çalıştırma görüşmesi — `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` dosyasını yazar |
| **sozlesme-inceleme** | Router — sözleşme yapısını tespit eder, uygun alt-skill'e (satici-inceleme / gizlilik-inceleme / saas-inceleme) yönlendirir ve çıktıyı tek bir notta birleştirir |
| **satici-inceleme** | Redline'larla birlikte tam oyun kitabı-sözleşme sapma analizi |
| **gizlilik-inceleme** | Hızlı YEŞİL/SARI/KIRMIZI triyaj — hukuk yalnızca ihtiyacı olan NDA'ları okusun |
| **saas-inceleme** | Aboneliğe özgü katman: otomatik yenileme, fiyat artışı, veri çıkışı, SLA'lar |
| **yenileme-takibi** | Fesih-bildirim son tarihleri kaydı, ne geldiğini yüzeye çıkarır |
| **eskalasyon-isaretleyici** | Sorunları eskalasyon matrisiyle eşleştirir, onaylayıcı talebini taslaklar |
| **paydas-ozeti** | Bir hukuki incelemenin iki paragraflık iş çevirisi |
| **degisiklik-gecmisi** | Ana sözleşme ve zeyilnameleri boyunca değişiklikleri özetler, veya belirli bir maddeyi güncel kontrol eden diline kadar izler |
| **teklif-inceleme** | Oyun kitabı izleyicisinden gelen bekleyen tekliflerin gözden geçirilmesi ve onaylanması/reddi |
| **dosya-calisma-alani** | Çok-müvekkilli pratikler için dosya çalışma alanları oluşturur, listeler, değiştirir ve kapatır; bağlamın dosyalar arasında sızmamasını sağlar |
| **ozellestir** | Pratik profilinin rehberli özelleştirmesi — tüm görüşmeyi yeniden çalıştırmadan tek bir şeyi değiştirir |

## Etkileşimli komutlar vs. zamanlanmış ajanlar

Yukarıdaki komutlar siz çağırdığınızda çalışır — bir dosya üzerinde çalışırken. Aşağıdaki
agent'lar bir zamanlamayla çalışır — siz bakmazken hareket eden şey için:

| Agent | Neyi izler | Varsayılan sıklık |
|---|---|---|
| **yenileme-ajani** | Yenileme kaydı — önümüzdeki 90 günde geleni paylaşır, 0-13 günlük fesih-bildirim pencereleri için kırmızı bayrak eskalasyonuyla | Haftalık (Pazartesi) |
| **anlasma-degerlendirme** | Son imzalanan sözleşmelerdeki oyun kitabı sapmalarını yüzeye çıkarır; hafıza tazeyken avukatı bağlamı kaydetmeye teşvik eder | Haftalık (Pazartesi) |
| **oyun-kitabi-izleyici** | Sapma günlüğü — bir madde 12 aylık kayan bir pencerede 5+ kez geçersiz kılındığında oyun kitabı güncellemeleri önerir | Veri-tetiklemeli (her anlasma-degerlendirme sonrası) |

## Entegrasyonlar

**Önce bir araştırma aracı bağlayın — atıf güvencesi buna bağlıdır.** Olmadığında her
atıf `[doğrulanacak]` etiketiyle işaretlenir ve her çıktının üzerindeki inceleyen notu
kaynakların doğrulanmadığını kaydeder. Eklenti her iki durumda da çalışır; bir araştırma
aracı bağlandığında doğrulamayı sizin için yapar.

`.mcp.json` içinde yapılandırılmış bağlayıcılarla gelir:

- **Ironclad** — sözleşme yaşam döngüsü yönetimi (CLM)
- **DocuSign** — imza durumu ve zarf takibi
- **iManage** — yönetilen belge deposu
- **Definely** — sözleşme yapısına canlı erişim (tanımlar, çapraz referanslar)
- **TopCounsel** — dış avukat önerileri (ABD-ağırlıklı topluluk; TR için Lexpera/Kazancı
  veya baro listeleri değerlendirin)
- **Slack** — mesajları arar, kanalları okur, tartışmaları bulur (genel kova)
- **Google Drive** — belgeleri arar, okur ve getirir (genel kova)

Türk hukuku araştırması için önerilen kaynaklar: **mevzuat.gov.tr**, **UYAP**,
**Lexpera**, **Kazancı**. Paket içindeki bağlayıcılar genel sözleşme yönetimi
araçlarıdır — mevzuat/içtihat araştırması için değildir.

Bir CLM bağlıysa: incelemeler aynı karşı tarafla önceki sözleşmeleri kontrol eder,
yenileme kaydını toplu yükler, inceleme notları eklenmiş kayıtlar oluşturur.

DocuSign bağlıysa: imza durumunu izler, zarfları onaylayıcı sırasına göre yönlendirir.

## Hızlı başlangıç

### 1. Görüşülün

```
/ticari-hukuk:ilk-kurulum
```

On dakika. Paylaşmaya hazır 5-10 son imzalanmış sözleşme bulundurun (daha fazlası
daha iyi, 20 tanesi daha net bir örüntü verir).

Yapılandırmanız `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
dosyasında saklanır ve eklenti güncellemelerini atlatarak korunur.

### 2. Bir sözleşmeyi incele

```
/ticari-hukuk:sozlesme-inceleme satici-msa.pdf
```

Çıktı: oyun kitabınıza karşı madde madde sapma notu, spesifik redline diliyle ve
adlandırılmış onaylayıcıyla.

### 3. Ne yenileneceğini gör

```
/ticari-hukuk:yenileme-takibi
```

Çıktı: önümüzdeki 90 günde fesih-bildirim son tarihi olan her şey, aciliyete göre
gruplanmış.

## Nasıl öğrenir

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` adresindeki
pratik profiliniz statik değildir — eklentiyi kullandıkça gelişir. Skill'ler bir çıktı
ayarlaman gereken bir varsayılan kullandığında size söyler. `oyun-kitabi-izleyici`
agent'ı pratiğiniz oyun kitabınızdan saptığında güncellemeler önerir. Kurulumu yeniden
çalıştırabilir, dosyayı doğrudan düzenleyebilir veya bir skill'e yeni bir pozisyon
kaydetmesini söyleyebilirsiniz.

## Dosya yapısı

```
ticari-hukuk/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Ekip pratik profiliniz — ilk-kurulum tarafından yazılır, sizin tarafınızdan düzenlenir
├── README.md
├── agents/
│   ├── yenileme-ajani.md
│   ├── anlasma-degerlendirme.md
│   └── oyun-kitabi-izleyici.md
├── skills/
│   ├── ilk-kurulum/
│   ├── sozlesme-inceleme/
│   ├── teklif-inceleme/
│   ├── satici-inceleme/
│   ├── gizlilik-inceleme/
│   ├── saas-inceleme/
│   ├── yenileme-takibi/
│   │   └── references/yenileme-kaydi.yaml
│   ├── eskalasyon-isaretleyici/
│   ├── degisiklik-gecmisi/
│   ├── dosya-calisma-alani/
│   └── paydas-ozeti/
└── hooks/hooks.json
```

## Notlar

- Eklenti çoğu incelemede sizin **müşteri** olduğunuzu varsayar. Siz satıcıysanız,
  işaretleyin — inceleme oyun kitabı kutbunu tersine çevirir.
- NDA triyajı hukukçu olmayanların kendi kendine kullanması için kurulmuştur. YEŞİL
  "imzaya yönlendir" demektir. Müzakere etmez.
- Yenileme takibi yalnızca bu eklenti üzerinden incelenmiş veya CLM'den toplu
  yüklenmiş sözleşmeleri bilir. Bu eklentiyi kurmadan önce imzalanan sözleşmelerin
  tek seferlik bir taramaya ihtiyacı vardır.
- Bu eklenti neredeyse tamamen A kademesidir (saf iş akışı iskeleti) — sözleşme
  hukuku büyük ölçüde yargı-nötrdür. "Yargı çevresi farkı kontrolü" gibi bazı
  alt bölümlerdeki spesifik kanun atıfları `[doğrulanacak]` ile işaretlenmiştir;
  bir Türk hukukçusu tarafından teyit edilmelidir.
