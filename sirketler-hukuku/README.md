# Şirketler Hukuku Eklentisi (sirketler-hukuku)

Şirket içi hukuk müşavirlikleri ve hukuk büroları için dört pratik alanında iş akışları: Şirket Birleşme & Devralma (M&A) işlemleri, yönetim kurulu ve şirket sekreteryası, halka açık şirket yönetişimi ve şirketler hukuku uyumu. Yalnızca rolünüze uygun modülleri etkinleştirin. İlk kurulum görüşmesi modülerdir — her aktif alan için hedefe yönelik sorular sorar ve pratik profilinize yalnızca ilgili bölümleri yazar.

**Her çıktı, avukat incelemesi için bir taslaktır — kaynak gösterilmiş, işaretlenmiş ve denetime tabidir — nihai bir hukuki sonuç değildir.** Eklenti işi yapar: belgeleri okur, standart kurallarınızı uygular, sorunları bulur, notu taslaklar. Avukat inceler, doğrular ve karar verir. Alıntılar kaynağa göre etiketlenir, böylece hangilerinin bir araştırma aracından geldiğini ve hangilerinin kontrol edilmesi gerektiğini bilirsiniz. Kritik eylemler (dosyalama, gönderme, imzalama vb.) her zaman açık onaya tabidir.

## Kimler için

| Rol | Aktif modüller |
|---|---|
| **Şirket içi M&A avukatı** | M&A |
| **Kurul sekreteryası / Avukatı** | Kurul & Sekreterya |
| **Halka açık şirket BHM'si** | M&A + Halka Açık Şirket + Kurul & Sekreterya |
| **Özel şirket BHM'si** | M&A + Kurul & Sekreterya + Şirket Yönetimi |
| **Hukuk bürosu / Bağımsız avukat** | Hangisi uygunsa (seçerek etkinleştirin) |

## İlk Çalıştırma

```
/sirketler-hukuku:ilk-kurulum
```

Modül seçiminden geçer, ardından her aktif alan için kısa ve hedefe yönelik bir mülakat yapar. Sadece ilgili bölümlerle modüler bir `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` yazar. Yapılandırmanız bu yolda saklanır ve eklenti güncellemelerinde kaybolmaz.

İşleme özel kurulum (yalnızca M&A modülü):

```
/sirketler-hukuku:ilk-kurulum --new-deal
```

## Komutlar

| Komut | İşlevi |
|---|---|
| `/sirketler-hukuku:ilk-kurulum` | Modüler ilk kurulum veya `--new-deal` / `--module [m&a \| kurul \| halka-acik \| sirket-uyum]` |
| `/sirketler-hukuku:due-diligence-sorun-cikartma [klasor]` | VDR belgelerini oku, kurum formatında sorunları çıkar |
| `/sirketler-hukuku:tablo-inceleme` | Tablo incelemesi — belge başına bir satır, veri noktası başına bir sütun, her hücre kaynağa atıflı, Excel çıktısı |
| `/sirketler-hukuku:onemli-sozlesme-takvimi` | Due diligence bulgularından önemli sözleşmeler açıklama listesi (disclosure schedule) |
| `/sirketler-hukuku:kapani-kontrol-listesi` | Kapanış kontrol listesi (closing checklist) — eksikler, kritik yol |
| `/sirketler-hukuku:yazili-onay` | Oybirliğiyle yazılı onay (TTK m.390/7) — emsallerden eşleşen taslak + imza takibi |
| `/sirketler-hukuku:yonetim-kurulu-tutanagi` | YK toplantı tutanağı taslağı |
| `/sirketler-hukuku:entegrasyon-yonetimi` | Kapanış sonrası entegrasyon iş planı, onay izleyici, sözleşme devri, durum raporları |
| `/sirketler-hukuku:dosya-calisma-alani` | Çalışma alanı yönetimi (yalnızca çok müvekkilli uygulamalar için) — yeni, listele, değiştir, kapat |

*(Not: `sirket-uyum` yeteneği B kademesinde olup Türk hukuku - TTK/MERSİS için yeniden tasarlanmayı beklemektedir.)*

## Yetenekler (Skills)

| Yetenek | Modül | Amacı |
|---|---|---|
| **ilk-kurulum** | Tümü | Modüler kurulum görüşmesi |
| **due-diligence-sorun-cikartma** | M&A | VDR belgeleri → kategori bazında, kurum formatında sorunlar |
| **tablo-inceleme** | M&A | Belge setini belirli bir yapıya göre inceleme; `.xlsx` / `.csv` / markdown çıktı |
| **anlasma-ekibi-ozeti** | M&A | Kademeli bilgilendirmeler: yönetici / iş lideri / çalışma ekibi |
| **onemli-sozlesme-takvimi** | M&A | Sözleşme tanımlarına göre açıklama listesi (disclosure schedule) |
| **kapani-kontrol-listesi** | M&A | Kendini güncelleyen: due diligence ve sözleşme bulgularından beslenir |
| **yapay-zeka-arac-devri** | M&A | (Opsiyonel) Özel AI belge inceleme araçları entegrasyonu |
| **yonetim-kurulu-tutanagi** | Kurul | Takvimden saptanan toplantılar → kurum formatında tutanak (taslak, TTK m.390 vd.) |
| **yazili-onay** | Kurul | Emsal aramasıyla oybirliğiyle yazılı onaylar; majör kararlar için kapsam uyarısı |
| **entegrasyon-yonetimi** | M&A | Kapanış sonrası izleyici; fazlı iş planı (1/30/90. gün); gerekli onaylar takibi |
| **dosya-calisma-alani** | Tümü | Çok-müvekkilli işler için dosya/çalışma alanı oluşturur ve izole eder. |
| **ozellestir** | Tümü | Eklenti ayarlarına yardımcı olur. |

## Etkileşimli Komutlar ve Zamanlanmış Ajanlar (Agents)

| Ajan | Modül | Ne izler | Varsayılan sıklık |
|---|---|---|---|
| **veri-odasi-izleyici** | M&A | Yeni belge yüklemeleri için VDR; öncelikli yüklemeleri işaretler; kapanış kontrol listesi durumunu günceller | Haftalık |

## Entegrasyonlar

**Öncelikle bir araştırma aracı bağlayın — alıntı kuralları (guardrails) buna bağlıdır.** Bağlamazsanız, her alıntı `[doğrula]` olarak etiketlenir ve her teslimatın üzerindeki inceleyen notunda kaynakların doğrulanmadığı belirtilir. Araştırma aracı (Lexpera, Kazancı, UYAP, mevzuat.gov.tr) sadece doğrulama yükünüzü hafifletir.

Desteklenen bağlantılar:
- **Slack**, **Google Drive**, **Box**

Intralinks, Datasite vb. VDR bağlayıcıları, ortak URL'leri mevcut olduğunda `.mcp.json` dosyasına eklenebilir.

## Nasıl Öğrenir?

Pratik profiliniz (`~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md`) statik değildir — eklentiyi kullandıkça gelişir. Yetenekler, ayarlamanız gereken bir varsayılan kullandıklarında size bildirir. Kurulumu yeniden çalıştırabilir, dosyayı doğrudan düzenleyebilir veya bir yeteneğe yeni bir pozisyon kaydetmesini söyleyebilirsiniz.

## M&A Notları

- Sorun çıkarma (issue extraction), önemlilik eşiklerini (materiality) uygular — eşik "değere göre ilk N" diyorsa her belgeyi okumaz.
- Hem alıcı taraf (buy-side) hem satıcı taraf (sell-side) desteklenir.
- Kapanış kontrol listesi satın alma sözleşmesinden başlar, ardından due diligence gerekli onayları çıkardıkça kendini günceller.
