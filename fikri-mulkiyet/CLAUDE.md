<!--
YAPILANDIRMA (CONFIG) KONUMU

Bu eklenti için kullanıcıya özel yapılandırma (config), eklenti güncellemelerinden etkilenmeyen şu yolda bulunur:

  ~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md

Bu eklentideki her yetenek (skill), komut ve ajan için kurallar:
1. Yapılandırmayı BU DOSYADAN DEĞİL, o yoldan OKU.
2. Eğer o dosya yoksa veya hala [YER_TUTUCU] işaretleri içeriyorsa, esaslı bir iş yapmadan önce DUR. Şöyle de: "Bu eklentinin size faydalı çıktılar verebilmesi için önce kuruluma ihtiyacı var. Lütfen `/fikri-mulkiyet:ilk-kurulum` komutunu çalıştırın."
3. İlk kurulum komutu (ilk-kurulum) bu yapılandırmayı o yola YAZAR, gerekirse üst dizinleri oluşturur.
4. Bu dosya (şu an okuduğunuz) ŞABLON'dur. Asla kullanıcı verisini buraya yazmayın.

**Ortak şirket profili.** (Kim olduğunuz, ne yaptığınız, risk yaklaşımınız) tüm 12 eklentinin paylaştığı `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasında bulunur.
-->

# Fikri Mülkiyet (IP) Pratik Profili
*Bu dosya ilk çalıştırmadaki mülakat ile yazılır. O zamana kadar bir şablondur.*

---

## Şirket / Müvekkil Profili

**Kurum adı:** [YER_TUTUCU — tam hukuki ünvan] *(company-profile.md'den)*
**Sektör:** [YER_TUTUCU — örn. tüketici SaaS, tıbbi cihaz, moda, fintech]
**Aşama:** [YER_TUTUCU — girişim / büyüme / halka açık / köklü / hukuk bürosu]
**Ana Yargı Çevresi:** [YER_TUTUCU — kuruluş yeri / ana faaliyet yargı çevresi (örn. Türkiye)]

**En büyük sorun / Acı noktası:** [YER_TUTUCU — ekibin kendi kelimeleriyle neyin zor olduğu]

**Çalışma ortamı:** [YER_TUTUCU — Tek/Küçük büro | Orta/Büyük büro | Şirket-içi (In-house) | Kamu]

---

## Kim Kullanıyor

**Rol:** [YER_TUTUCU — Avukat / Hukuk profesyoneli | Marka/Patent vekili | Avukat erişimi olan uzman | Avukat erişimi olmayan uzman]
**Avukat İletişim:** [YER_TUTUCU — İsim / ekip / dış büro]

---

## Mevcut Entegrasyonlar

| Entegrasyon | Durum | Yoksa Ne Yapılır |
|---|---|---|
| FM Yönetim Sistemi (Anaqua, PatSnap, vb.) | [YER_TUTUCU ✓/✗] | Portföy `portfolio.yaml` dosyasında manuel tutulur. |
| Hukuki Araştırma (Lexpera, Kazancı, vb.) | [YER_TUTUCU ✓/✗] | Manuel araştırma — yetenek, hangi davaların çekileceğini söyler. |
| Patent Araştırması (Solve Intelligence vb.) | [YER_TUTUCU ✓/✗] | FTO ve önceki teknik becerileri manuel girilen referanslardan çalışır. |
| Doküman Depolama (Drive vb.) | [YER_TUTUCU ✓/✗] | Kullanıcı belgeleri her inceleme için manuel yükler. |
| Slack | [YER_TUTUCU ✓/✗] | Bildirimler kanala gönderilmek yerine sohbet ekranında verilir. |

---

## Çıktılar

**İş-Ürünü Başlığı** (Bu eklentinin ürettiği her analiz veya incelemenin en üstüne eklenir). Başlık Role göre değişir:

- Rol "Avukat / Hukuk profesyoneli" ise: `GİZLİ — AVUKAT İŞ ÜRÜNÜ / MESLEK SIRRI — MÜVEKKİL-AVUKAT GİZLİLİĞİ KAPSAMINDADIR`
- Rol "Marka/Patent Vekili" ise: `GİZLİ — VEKİL-MÜVEKKİL İLİŞKİSİ / TÜRKPATENT / WIPO UYGULAMASI`
- Rol Avukat olmayan biri ise: `ARAŞTIRMA NOTLARI — HUKUKİ TAVSİYE DEĞİLDİR — HAREKETE GEÇMEDEN ÖNCE BİR AVUKATLA İNCELEYİN`

Başlığı dışa dönük belgelerden çıkarın (karşı tarafa gönderilen ihtarlar vb.).

**⚠️ İnceleyen notu — çıktının hemen üstünde.** 
> **⚠️ İnceleyen Notu**
> - **Kaynaklar:** [Araştırma aracı: Lexpera ✓ doğrulandı | model bilgisi, güvenmeden önce doğrulayın]
> - **Okundu:** [200 sayfanın 1-50. sayfaları | tüm belgeler]
> - **İncelenmesi İçin İşaretlenenler:** [satır içinde `[incele]` ile işaretlenmiş N öğe]
> - **Güvenmeden önce:** [inceleyenin gerçekten yapması gereken 1-2 şey]

**Veri Ağır Çıktılar İçin Pano (Dashboard) Teklifi.** Eğer çıktı çok fazla veri içeriyorsa (~10'dan fazla satır, uzun bir liste vb.) bir görsel pano (dashboard) teklif edin.

---

## Kaynak Etiketleri (Source Tags)

- `[Lexpera]` / `[Kazanci]` / `[TÜRKPATENT]` — SADECE bu oturumda o kaynaktan açıkça çekildiyse.
- `[mevzuat / kurum sitesi]` — İlgili web sitesinden bu oturumda metin çekildiyse.
- `[kullanıcı sağladı]` — Kullanıcı yapıştırdıysa.
- `[model bilgisi — doğrula]` — Geri kalan her şey. (Eğer kendiniz çekmediyseniz, ne kadar emin olursanız olun bu model bilgisidir.)

Etiketleri kaynağına göre kullanın, "doğru göründüğü" için daha güvenilir bir etikete yükseltmeyin.

---

## FM Pratik Profili

**Uygulama Alanları:** [YER_TUTUCU — marka / patent / telif / ticari sır / açık kaynak / tümü]

**Tescil Olunan Yargı Çevreleri:** [YER_TUTUCU — Türkiye (TÜRKPATENT), WIPO/Madrid, EPO vb.]

**FM Yönetim Sistemi:** [YER_TUTUCU — Anaqua / PatSnap / e-tablo / yok]

**Uygulama Alanı Sahipliği:**
- Marka: [YER_TUTUCU — isim/ekip veya dış büro]
- Patent: [YER_TUTUCU — isim/ekip veya dış büro]
- Açık Kaynak: [YER_TUTUCU — isim/ekip]

---

## FM Portföyü

**Sicil Dosyası:** `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/portfolio.yaml`

---

## Marka Koruması (Brand Protection)

**İzlenen Markalar:** [YER_TUTUCU — ihlal için izlenen markaların listesi]
**İzleme Alanı (Jurisdictions):** [YER_TUTUCU — TR / Küresel]

---

## Yaptırım ve İhlal Yaklaşımı (Enforcement Posture)

**Varsayılan Yaklaşım:** [YER_TUTUCU — agresif / ölçülü / muhafazakar]
*Agresif = hemen ihtarname gönder, dava açmaya istekli. Ölçülü = önce yumuşak bir iletişim, ticari etki varsa tırmandır. Muhafazakar = sadece dava kesinse ve işletme onayladıysa harekete geç.*

**Mektup Gönderme Onayı:**
- İhtarname (Cease-and-desist): [YER_TUTUCU]
- Dava Açma: [YER_TUTUCU]

---

## Dosya Çalışma Alanları (Matter Workspaces)

**Etkin:** ✗ (özel büro için ilk kurulumda ayarlanır)
**Aktif dosya:** yok
**Çapraz-dosya bağlamı:** kapalı

Etkinleştirildiğinde yetenekler aktif dosyanın (matter.md) bağlamında çalışır.
