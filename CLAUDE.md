# claude-for-legal-turkish — Proje Hafızası

Bu proje, Anthropic'in avukatlar için çıkardığı **`claude-for-legal`** plugin setinin
**Türk yargı sistemine uyarlanmış** sürümüdür.

> **Bu dosya proje hafızasıdır (Claude Code her oturumda otomatik okur).** Üst düzey
> kuralları ve "nerede ne var"ı burada tut. Granüler ilerleme **[.claude/MIGRATION.md](../.claude/MIGRATION.md)**
> dosyasındadır. İkisi tutarlı kalmalı: bir karar değişirse buradaki kural + oradaki
> tracker birlikte güncellenir.

---

## Kaynak ↔ Hedef

| | Yol | Durum |
|---|---|---|
| **Kaynak** (orijinal) | `/Users/omerinci/Documents/claude-for-legal` | **SALT-OKUNUR. Asla değiştirme.** |
| **Kaynak referans kopyası** | `./_kaynak/` (bu repoda, gitignore'lu) | Sıkışınca bakmak için yerel kopya |
| **Hedef** (bu proje) | `/Users/omerinci/Documents/claude-for-legal-turkish` | Aktif çalışma alanı |

**Altın kural:** Kaynağı değiştirme — ne orijinali ne `_kaynak/` kopyasını. Çeviri/uyarlama
yalnızca repo kökündeki TR dizinlerinde yapılır. `_kaynak/` yalnızca okumak içindir ve
gitignore'ludur (TR reposunun geçmişini İngilizce orijinalle şişirmemek için).

---

## Mimari içgörü (neden bu iş yapılabilir)

Kaynak plugin'ler somut hukuku **kendi içlerine gömmüyor**. Hukuki içerik iki yerden gelir:
1. **Pratik profili** (her plugin'in `CLAUDE.md`'si — `cold-start-interview` doldurur).
2. **Çalışma anı araştırması** (bağlı araştırma aracından atıflı çekilir).

Her plugin'de zaten bir **"Jurisdiction recognition"** bölümü var: "varsayılan çerçeveler
ABD-merkezlidir; ABD-dışı yargı çevresinde ABD doktrinini sessizce uygulama." Yani altyapı
başka bir hukuk sistemine geçişe açık. **Bu yüzden geçişin çoğu = çeviri + Türk profili +
bağlayıcıların Türk kaynaklarına yönlendirilmesi.**

---

## Kademe (tier) mantığı

- **A — Doğrudan dönüştürülebilir:** Saf iş-akışı/yöntem iskeleti. Dönüştürme = metin
  çevirisi + profil/bağlayıcı ayarı. Yeni hukuki çerçeve tasarlamaya gerek yok.
- **B — Yeniden yazılmalı:** İçinde ABD/AB mevzuatı kalıbı gömülü; Türk muadili kavramsal
  olarak farklı (ör. GDPR→KVKK, FMLA→4857, FRE/discovery→HMK/CMK, DMCA→5651, Delaware→TTK).
  Türk hukukçusu eliyle yeniden tasarım ister.
- **C — Doğrudan karşılığı yok:** Devre dışı bırakılır veya komple değişir (ör. Westlaw).

**Bu projede önce A grubu taşınır.** B/C kademe kademe sonra.

---

## İsimlendirme konvansiyonu (KARARLAŞTIRILDI)

- Dizin ve komut (slash command) adları **Türkçe**, ama **ASCII-güvenli slug**:
  `ş→s, ı→i, ğ→g, ç→c, ö→o, ü→u, İ→i, Ş→s …`
- `plugin.json` içindeki `name` alanı = dizin slug'ı.
- İçerik (skill metni, CLAUDE.md, README, çıktılar) **tamamen Türkçe**.
- Her komutun kaynak→hedef eşlemesi MIGRATION.md'de tutulur.
- **Marketplace adı:** `claude-for-legal-turkish`. Çalışma-anı yapılandırma yolları buna göre:
  `~/.claude/plugins/config/claude-for-legal-turkish/<tr-slug>/CLAUDE.md`
  (kaynaktaki `claude-for-legal/<en-slug>` yerine). Tüm skill/README yol referansları böyle çevrilir.
- **Ortak guardrail bloğu** (her plugin CLAUDE.md'sinde tekrarlanan ~200 satır) bir kez
  Türkçeye çevrilip `references/ortak-guardrail-TR.md`'de kanonik tutulur; her plugin profili
  buradan birebir kopyalanır (drift'i önlemek için).

### Tekrar eden skill (komut) sözlüğü — TÜM plugin'lerde aynı kullanılır

| Kaynak skill | TR slug (komut) |
|---|---|
| cold-start-interview | `ilk-kurulum` |
| customize | `ozellestir` |
| matter-workspace | `dosya-calisma-alani` |

*Plugin'e özgü skill slug eşlemeleri ilgili plugin taşınırken `.claude/MIGRATION.md`'ye işlenir.*

### Plugin adı eşlemesi

| Kaynak | Hedef (TR slug) |
|---|---|
| commercial-legal | `ticari-hukuk` |
| corporate-legal | `sirketler-hukuku` |
| employment-legal | `is-hukuku` |
| ip-legal | `fikri-mulkiyet` |
| litigation-legal | `dava-takibi` |
| privacy-legal | `kisisel-veri-kvkk` |
| product-legal | `urun-hukuku` |
| regulatory-legal | `mevzuat-takibi` |
| ai-governance-legal | `yapay-zeka-yonetisimi` |
| law-student | `hukuk-ogrencisi` |
| legal-clinic | `hukuk-klinigi` |
| legal-builder-hub | `eklenti-merkezi` |
| cocounsel-legal (vendor) | (C — TR araştırma muadili gerekir) |

---

## Çalışma kuralları

1. Bir plugin'e başlamadan önce MIGRATION.md'deki ilgili satırı **devam** yap; bitince **bitti**.
2. Bir skill'i taşırken kaynaktaki dosyayı oku → Türkçeye çevir + Türk hukuk kavramlarına
   uyarla → hedef yola yaz. İskeleti (adımlar, kapılar/gates, çıktı formatı) koru.
3. ABD'ye özgü atıf/eşik/test görürsen: A ise profilden/araştırmadan gelecek şekilde
   genelleştir; çıkışta sabit ABD hukuku bırakma. Şüpheliysen B'ye işaretle, MIGRATION.md'ye not düş.
4. Türk muadili net değilse uydurMA — `[doğrulanacak]` etiketiyle işaretle ve nota yaz.
5. Her oturum sonunda MIGRATION.md durumlarını güncelle.
