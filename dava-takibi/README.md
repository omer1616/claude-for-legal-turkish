# Dava Takibi Eklentisi

Dava portföyünü yöneten şirket içi hukuk müşaviri desteği. İlk kurulum görüşmesi risk kalibrasyonunuzu, uyuşmazlık ortamınızı ve kurum içi üslubu yakalar — her yeni dosyanın buna göre sınıflandırıldığı çerçeveyi oluşturur. Tekdüze kayıt sistemi yeni dosyaları yapılandırılmış sicil girişlerine ve dosya bazlı tarihçe dosyalarına dönüştürür. Durum özetleri ve derinlemesine brifingleri sicilin içeriğinden okur.

Aynı anda çok sayıda dosyayı, büyük bölümü dış bürolar tarafından yürütülerek takip eden avukatlar için tasarlanmıştır. Bu eklenti bir düşünce ortağıdır, dava yönetim sistemi değil. SimpleLegal, Onit veya benzeri bir platform kullanıyorsanız bu eklenti onun yerini almaz — yapılandırılmış analiz katmanı olarak yanında durur.

**Her çıktı avukat incelemesi için taslaktır — atıflı, işaretli ve kapılı — hukuki sonuç değil.** Eklenti işi yapar: belgeleri okur, oyun kitabınızı uygular, sorunları bulur, notu taslak haline getirir. Bir avukat inceler, doğrular ve karar verir.

## Ön koşullar

Gmail ve zamanlı görev entegrasyonlarına bazı özellikler değinir. Bunlar ortamınızda yapılandırılmış MCP sunucuları gerektirir — paket içinde gelmez. Olmadığında çıktılar manuel gönderim için dosyaya yazılır:

- **Gmail MCP** — `/dava-takibi:dis-avukat-durum` kimlik doğrulaması varsa Gmail taslakları oluşturur; yoksa `oc-durum/[YYYY-AA-GG]/[slug].md` yoluna markdown taslak yazar.
- **Zamanlı görev MCP** — otomatik zamanlama gönderilmez. Haftalık komutları çalıştırmak için tekrarlayan bir takvim hatırlatıcısı kurun.

Eklenti ikisi olmadan da uçtan uca çalışır; entegrasyonlar isteğe bağlı eklemelerdir.

## Kimler için

| Rol | Birincil kullanım |
|---|---|
| **Şirket içi dava müşaviri** | Tamamı — kayıt, sınıflandırma, durum, tarihçe, brifing |
| **Genel Müdür Yardımcısı / Hukuk Direktörü** | Portföy genel görünümü, yönetim kurulu raporlama özetleri |
| **Genel Müdür / CLO** | Portföyde hızlı durum, herhangi bir dosyada derinlemesine inceleme |

## İlk çalıştırma: ilk-kurulum

İlk kurulum görüşmesi *kurum* pratik profilini yazar — her dosyada kalıcı. Üç temel:

- **Risk kalibrasyonu** — iştah, önemlilik eşikleri, karşılık/açıklama tetikleyicileri, uzlaşma yetkisi, sigorta profili, ciddiyet-olasılık matrisi
- **Ortam** — şirket, coğrafyalar, düzenleyici statü, uyuşmazlık kalıpları, sık karşılaşılan karşı taraflar, dış avukat kadrosu, iç paydaşlar
- **Kurum üslubu** — yönetim kurulu/denetim komitesi not formatı, karşılık not formatı, dış avukat direktifi üslubu, ayrıcalık konvansiyonları, yükseltme normları

Her adımda makul varsayılanlar sunar (örn. 3×3 ciddiyet-olasılık ızgarası) ve her şeyi serbest metin olarak düzenlenebilir tutar.

```
/dava-takibi:ilk-kurulum
```

Yapılandırmanız `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` altında saklanır ve eklenti güncellemelerini atlatarak korunur.

## Komutlar

| Komut | Ne yapar |
|---|---|
| `/dava-takibi:ilk-kurulum` | Kurum profilini yazar → `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` |
| `/dava-takibi:dava-kayit` | Tekdüze kayıt → `matters/[slug]/` yazar + `_log.yaml`'a ekler |
| `/dava-takibi:portfoy-durumu` | Portföy özeti — risk dağılımı, yaklaşan son tarihler, hareketsiz dosyalar |
| `/dava-takibi:dava-ozeti [slug]` | Bir dosyada derinlemesine brifing — GK veya dış avukat görüşmesi öncesi hazır |
| `/dava-takibi:dava-guncelle [slug]` | Dosya tarihçesine tarihli olay ekler; sicildeki `son_guncelleme` alanını yeniler |
| `/dava-takibi:dava-kapat [slug]` | Dosyayı aktif portföyden arşive alır (silinmez, saklanır) |
| `/dava-takibi:talep-giris [baslik]` | Talep mektubu için ön-taslak bağlam toplama (ödeme / ihlal / ihtarname / iş sözleşmesi feshi / delil muhafazası) |
| `/dava-takibi:yasal-saktedbir [slug] [--ver/--yenile/--kaldir/--durum]` | İhtiyati tedbir ver, yenile, kaldır veya raporla — `.docx` yazar + sicili günceller |
| `/dava-takibi:kronoloji [slug]` | Beyan edilen belge kaynaklarından + yüklemelerden kronoloji oluşturur veya günceller |
| `/dava-takibi:dis-avukat-durum` | Portföy genelinde haftalık dış avukat durum-talep e-postalarını taslak oluşturur; Gmail MCP varsa taslak kaydeder |
| `/dava-takibi:ozet-bolumu` | Kurum üslubunda özet bölümü taslağı, dava teorisiyle tutarlı |

## Skill'ler

| Skill | Amaç |
|---|---|
| **ilk-kurulum** | Kurum pratik profili — risk kalibrasyonu, ortam, üslup |
| **dava-kayit** | Tekdüze kayıt soruları; dosya kaydı + sicil satırı yazar |
| **portfoy-durumu** | Sicil genelinde özet — risk, son tarihler, hareketsizlik |
| **dava-ozeti** | Bir dosyanın dosya kaydı + tarihçesinden derin okuma |
| **dava-guncelle** | Yapılandırılmış olay ekleme; sicilin `son_guncelleme` alanını günceller |
| **dava-kapat** | Arşivleme semantiği; sonucu yakalar |
| **talep-giris** | Talep mektubu için uyarlanabilir bağlam toplama — taraflar, olgular, kaldıraç, ayrıcalık filtreleri |
| **yasal-saktedbir** | Tedbir ver / yenile / kaldır / durum raporu; `.docx` bildirimi yazar; sicilin `yasal_saktedbir` alanlarını günceller |
| **kronoloji** | Beyan edilen belge kaynaklarından + yüklemelerden tarihli olayları çıkarır; tekilleştirir; dava teorisine göre önem etiketler |
| **dis-avukat-durum** | Haftalık portföy genelinde dış avukat durum-talep e-posta taslakçısı; markdown + Gmail taslakları |
| **ozet-bolumu** | Kurum üslubunda özet bölümü taslağı, dava teorisiyle tutarlı. Atıflar ve `[İNCELE]` işaretleri dahil |
| **ozellestir** | Pratik profili günceller — yeni pozisyon, üslup değişikliği, eşik yenileme |
| **dava-calisma-alani** | Dosya çalışma alanlarını yönetir (yeni / listele / geç / kapat) |

## Etkileşimli komutlar vs. zamanlanmış ajanlar

Yukarıdaki komutlar siz çağırdığınızda çalışır. Aşağıdaki ajan bir zamanlamayla çalışır:

| Ajan | Neyi izler | Varsayılan sıklık |
|---|---|---|
| **esas-izleyici** | Aktif portföydeki dosyaların mahkeme sicil kayıtları — yeni evrakları çeker, aday son tarihleri hesaplar, her dosyanın tarihçesiyle çapraz referans yapar | Haftalık |

## Verinin organizasyonu

```
dava-takibi/
├── CLAUDE.md                          # KURUM pratik profili — risk, ortam, üslup
├── matters/
│   ├── _log.yaml                      # portföy sicili (dosya başına bir giriş)
│   └── [dava-slug]/
│       ├── matter.md                  # dosyaya özgü kayıt + teori + pozisyon
│       ├── history.md                 # yalnızca ekleme modunda olay günlüğü
│       ├── chronology.md              # savunuculuk odaklı zaman çizelgesi (talep üzerine)
│       └── yasal-saktedbir-v[N].docx  # tedbir bildirimleri (ver, yenile, kaldır)
├── demand-letters/                    # giden talep mektupları
│   └── [slug]/
│       ├── intake.md
│       ├── taslak-v1.docx
│       └── kontrol-listesi.md
├── inbound/                           # gelen talepler, tebligatlar, düzenleyici yazılar
│   └── [slug]/
│       ├── gelen.[uzanti]
│       ├── inceleme.md
│       └── yanit-v1.docx
└── oc-durum/                          # haftalık dış avukat durum-talep taslakları
    └── [YYYY-AA-GG]/
        ├── _ozet.md
        └── [slug].md                  # dosya başına bir e-posta
```

## Bağlayıcılar ve atıf doğrulama

**Önce bir araştırma aracı bağlayın — atıf güvencesi buna bağlıdır.** Olmadığında her atıf `[doğrulanacak]` etiketiyle işaretlenir ve her çıktının üzerindeki gözden geçiren notu kaynakların doğrulanmadığını kaydeder. Eklenti her iki durumda da çalışır; araştırma aracı bağlandığında doğrulamayı sizin için yapar.

Türk hukuku araştırması için önerilen kaynaklar: **mevzuat.gov.tr**, **UYAP**, **Lexpera**, **Kazancı**. Paket içindeki CourtListener ve Trellis ABD odaklıdır.

## Satır içi işaretleyici konvansiyonları

Üç işaretleyici skill çıktılarında ve taslaklar da görünür. Sorumluluk reddi değil, eylem kalemleridir:

- `[ATIF: belirli atıf gerekli]` — hukuki dayanak yer tutucusu. Avukat göndermeden önce doldurur veya doğrular.
- `[DOĞRULA: belirli olgu]` — henüz kaynağa bağlanmamış olgusal iddia. Avukat güvenmeden önce doğrular.
- `[UZM-DOĞRULA: belirli yargı kararı]` — ilgili alanda ehil avukat incelemesi gerektiren yargısal değerlendirme. Bolca kullanılır — yargı ağırlıklı her şey bu işareti taşımalı.

Çözümlenmemiş işaretler içeren bir taslak veya inceleme ne kadar cilalı görünse de nihai değildir.
