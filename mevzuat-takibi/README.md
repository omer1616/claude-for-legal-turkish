# Mevzuat Takibi (Regulatory Counsel) Eklentisi

Mevzuat beslemelerini (Resmî Gazete vb.) izler, yeni mevzuatı politika kütüphanenizle karşılaştırır ve uyum boşluklarını çıkarır. Sizin önemlilik (materiality) eşiğinizi öğrenir, böylece her kurum yetkilisinin demecinde alarm vermez. UYAP, mevzuat.gov.tr, Resmî Gazete ve doğrudan düzenleyici kurum beslemeleri için donatılmıştır.

**Her çıktı, avukat incelemesi için bir taslaktır — kaynak gösterilmiş, işaretlenmiş ve geçide (gate) bağlanmıştır — nihai bir hukuki sonuç (legal conclusion) değildir.** Eklenti işi yapar: belgeleri okur, sizin oyun kitabınızı (playbook) uygular, sorunları bulur, bilgi notunu taslaklar. Bir avukat inceler, doğrular ve karar verir. Hangi atıfların bir araştırma aracından geldiğini ve hangilerinin kontrol edilmesi gerektiğini bilmeniz için atıflar kaynaklarına göre etiketlenir. Ayrıcalık (privilege/meslek sırrı) işaretleri muhafazakar bir şekilde uygulanır. Önemli eylemler (dosyalama, gönderme vb.) açık onaya (gate) tabidir.

## Kimler İçin

| Rol | Temel İş Akışları |
|---|---|
| **Uyum / Mevzuat Avukatı** | İzleme listesi (watchlist) bakımı, boşluk (gap) triajı, politika güncellemeleri koordinasyonu |
| **Gizlilik (KVKK) / Ürün Avukatı** | Kendi alanlarıyla ilgili filtrelenmiş alarmları alır |
| **Baş Hukuk Müşaviri (GC)** | Süreli ve önemli uyum boşlukları için eskalasyon (yetki) alıcısı |

## İlk Çalıştırma: İlk Kurulum (Cold-Start)

Hangi düzenleyici kurumları (BDDK, SPK, Rekabet Kurumu, Kişisel Verileri Koruma Kurumu vb.) izlediğinizi sorar, politika belgesi klasörünüzü bağlar ve sizin için "önemli" (material) olanın ne olduğunu öğrenir. Bir izleme listesi oluşturur ve politika kütüphanenizi indeksler.

```
/mevzuat-takibi:ilk-kurulum
```

## Yetenekler (Skills)

| Yetenek | İşlevi |
|---|---|
| `/mevzuat-takibi:ilk-kurulum` | İlk kurulum: izleme listesi + politika indeksi + önemlilik eşiği |
| `/mevzuat-takibi:mevzuat-besleme-izleyici` | Beslemeleri şimdi kontrol et, neyin yeni olduğunu raporla |
| `/mevzuat-takibi:politika-farki [mevzuat]` | Belirli bir mevzuat değişikliğini politika kütüphanesiyle karşılaştır (diff) |
| `/mevzuat-takibi:bosluk-analizi` | Açık boşluklar (gaps) takipçisi — nelerin işaretlendiği ve henüz kapatılmadığı |
| `/mevzuat-takibi:goruş-bildirimi` | *(Yakında - Türk kamuoyu görüşü süreçleri için tasarlanıyor)* |
| `/mevzuat-takibi:politika-taslak-guncelleme` | Bir uyum boşluğunu kapatan işaretli politika taslağı — kaynak belgeye doğrudan müdahale değil, iç inceleme için ilk taslak |
| `/mevzuat-takibi:dosya-calisma-alani` | Dosya çalışma alanlarını yönet (çok müşterili avukatlar için) |
| `/mevzuat-takibi:ozellestir` | Profilinizi yeniden kurulum yapmadan değiştirin |

## Etkileşimli Yetenekler vs. Zamanlanmış Ajanlar (Agents)

Yukarıdaki yetenekler siz çağırdığınızda çalışır. Aşağıdaki ajanlar ise zamanlamaya göre (siz bakmıyorken değişenler için) çalışır:

| Ajan | Neyi İzler | Varsayılan Ritim |
|---|---|---|
| **mevzuat-degisiklik-izleyici** | Mevzuat beslemeleri (Resmî Gazete) — ilk kurulumda öğrenilen önemlilik eşiğine göre filtreler ve gürültü değil sinyal olan bir özet yayınlar | Haftalık (veya mevzuat ortamı hareketliyse günlük) |

## Bağlayıcılar (Connectors) ve Atıf Doğrulama

**Önce bir araştırma aracı bağlayın — atıf koruma kuralları buna dayanır.** Bağlı değilse, her atıf `[doğrulanacak]` (verify) olarak etiketlenir ve her çıktının üzerindeki inceleme notu, kaynakların doğrulanmadığını kaydeder.

Bu eklentideki hukuki araştırma bağlayıcıları sadece veri kaynakları değildir — doğrulanmış bir atıf ile sizin kontrol etmeniz gereken bir atıf arasındaki farktır. Bağlı bir araştırma aracı (örn. Lexpera, Kazancı, UYAP, mevzuat.gov.tr) aracılığıyla alınan bir atıf kaynağıyla etiketlenir ve izlenebilir. Modelin bilgisinden veya web aramasından gelen bir atıf `[doğrulanacak]` olarak etiketlenir ve birincil kaynağa (Resmî Gazete vb.) karşı kontrol edilmelidir.

## Entegrasyonlar (Integrations)

`.mcp.json` içinde standart bağlayıcılarla gelir:
- **Slack** — mesajlarda ara, kanalları oku, tartışmaları bul
- **Google Drive** — belge ara, oku ve getir

## Yapılandırma

Yapılandırmanız `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` adresinde saklanır ve eklenti güncellemelerinden etkilenmez — kurulumu yalnızca bir kez yaparsınız.
