---
name: dosya-calisma-alani
description: >
  Dosya (matter) çalışma alanlarını yönetin — aktif dosyayı oluşturun, 
  listeleyin, değiştirin, kapatın (arşivleyin) veya bağlantısını kesin. 
  Böylece çok müşterili çalışan avukatlar bir müşterinin bağlamını diğerinden ayrı tutabilir. 
  Kullanıcı "yeni dosya", "dosya değiştir", "dosyaları listele", "dosyayı kapat" dediğinde 
  veya sadece genel pratik düzeyinde çalışmak istediğinde kullanın.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /dosya-calisma-alani

Avukatlar birden fazla müşteri ve dosya (matter) üzerinde çalışırlar. Bir dosya çalışma alanı, bir müşteri veya işin bağlamını diğerinden ayrı tutar. Bu yetenek bu alanları yönetir.

## Alt Komutlar (Subcommands)

- `/mevzuat-takibi:dosya-calisma-alani new <slug>` — yeni bir dosya oluştur, kısa bir ön görüşme (intake) yap, `matter.md` yaz.
- `/mevzuat-takibi:dosya-calisma-alani list` — dosyaları durumları ve aktif bayraklarıyla listele.
- `/mevzuat-takibi:dosya-calisma-alani switch <slug>` — aktif dosyayı belirle.
- `/mevzuat-takibi:dosya-calisma-alani close <slug>` — dosyayı arşivle (`_archived/` klasörüne taşı, asla silme).
- `/mevzuat-takibi:dosya-calisma-alani none` — aktif dosyadan ayrıl, sadece genel pratik seviyesinde çalış.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` dosyasını oku — `## Dosya çalışma alanları` (Matter workspaces) bölümünü kontrol et. Eğer `Etkin` (Enabled) değilse (`✗`), kullanıcıya söyle: "Dosya çalışma alanları kapalı — tek müşterili bir şirket-içi (in-house) pratik olarak yapılandırılmışsınız. Eğer birden fazla müşteriyle çalışıyorsanız `/mevzuat-takibi:ilk-kurulum --redo` çalıştırıp özel pratik (büro) ayarını seçin. Aksi takdirde bu yeteneğe ihtiyacınız yok." Hata verme — şirket-içi kullanıcılar için kapalı olması beklenen durumdur.
2. Aşağıdaki iş akışını kullan.
3. `$ARGUMENTS`'in ilk kelimesine göre yönlendir:
   - `new` → ön görüşme yap, `matters/<slug>/matter.md` dosyasını yaz, `history.md` ve `notes.md` oluştur.
   - `list` → `matters/*/matter.md` dosyalarını listele, tablo yaz, aktif dosyayı işaretle.
   - `switch` → CLAUDE.md'deki `Aktif dosya:` (Active matter) satırını güncelle.
   - `close` → `matters/<slug>/` klasörünü `matters/_archived/<slug>/` konumuna taşı, kapanış tarihini `history.md`'ye kaydet.
   - `none` → `Aktif dosya:` ayarını `yok — sadece pratik-seviyesi bağlam` olarak ayarla.
4. Kullanıcıya nelerin değiştiğini göster ve yazmadan önce onayla.

## Notlar

- Bu yetenek, CLAUDE.md'de `Çapraz-dosya bağlamı` (Cross-matter context) `açık` (on) olmadığı sürece ASLA dosyalar arası (cross-matter) okuma yapmaz.
- Arşivlemek silmek demek değildir — kapanan dosyalar çıkar çatışması kontrolü vb. için okunabilir kalır.
- Slug'lar küçük harfli ve tireli olmalıdır.

---

## Depolama Düzeni

Tüm dosya verileri şurada yaşar:

```
~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/
├── CLAUDE.md                       # pratik seviyesindeki profil
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müşteri, karşı taraf, dosya türü, kilit olaylar, özel kurallar
    │   ├── history.md              # olayların, kararların, taslakların kronolojik kaydı
    │   ├── notes.md                # serbest form çalışma notları
    │   └── outputs/                # bu dosya için yetenek çıktıları
    └── _archived/
        └── <slug>/                 # kapalı dosyalar — okunabilir ama aktif değil
```

Örnek slug'lar: `abc-kvkk-uyum`, `xyz-spk-sorusturma`, `tedarikci-denetim`.

## Aktif dosya CLAUDE.md'dedir

CLAUDE.md içindeki `Aktif dosya:` satırı tek doğru kaynaktır (single source of truth). Bir dosyayı değiştirmek bu satırı düzenler.

## Alt Komut Mantığı

### `new <slug>`

1. Slug'ın mevcut olmadığını onayla.
2. Ön görüşme (intake) yap:
   - **Müşteri (Client)** (kimi temsil ediyoruz?)
   - **Karşı taraf / Kurum (Counterparty / Regulator)**
   - **Dosya türü (Matter type)** (Mevzuat Uyum | Danışmanlık | İnceleme | Soruşturma | vb.)
   - **Gizlilik seviyesi** (standart | yüksek | clean-team)
   - **Kilit olaylar (Key facts)** (2-5 cümle: Bu dosya ne hakkında?)
   - **Dosyaya özel geçersiz kılmalar (Overrides)** (Örn: "Öncelikli mevzuat: SPK Tebliği", "Kuruma karşı ılımlı dil kullanılmalı")
   - **İlgili dosyalar** (varsa bağlantılı dosyaların slug'ları)
3. `matters/<slug>/matter.md` dosyasını oluştur (aşağıdaki şablonla).
4. `history.md` içine "Açıldı" kaydı düş.
5. Boş bir `notes.md` oluştur.
6. Otomatik geçiş (switch) yapma. Sor: "Şimdi `<slug>` dosyasına geçmek ister misiniz?"

### `list`

`matters/*/matter.md` listesini çek ve tablo oluştur:
| Slug | Müşteri | Dosya türü | Durum | Açılış | Aktif |
Aktif dosyayı `*` ile işaretle.

### `switch <slug>`

1. `matters/<slug>/matter.md` dosyasının varlığını onayla. Yoksa `new` teklif et.
2. CLAUDE.md'deki `Aktif dosya:` satırını `Aktif dosya: <slug>` yap.
3. Doğru dosyada olduklarını teyit etmek için `matter.md` özetini göster.

### `close <slug>`

1. Klasörün varlığını onayla.
2. `history.md`'ye "Kapatıldı" kaydı ekle.
3. Klasörü `_archived/` içine taşı.
4. Kapatılan dosya aktif dosyaydı ise `Aktif dosya:` ayarını `yok` yap.

### `none`

CLAUDE.md'de `Aktif dosya:` satırını `yok — sadece pratik-seviyesi bağlam` yap. Onayla.

## `matter.md` şablonu

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI]

# Dosya: [Müşteri] — [kısa açıklama]

**Slug:** [slug]
**Açılış:** [YYYY-MM-DD]
**Durum:** aktif
**Gizlilik:** [standart / yüksek / clean-team]

---

## Taraflar
**Müşteri:** [isim]
**İlgili Kurum / Karşı Taraf:** [isim(ler)]

## Dosya türü
[Mevzuat Uyum | Soruşturma | Danışmanlık | ...]

## Kilit olaylar
[2-5 cümle. Dosyanın konusu ve önemi.]

## Dosyaya özel geçersiz kılmalar (Overrides)
[Örn: "İlgili Mevzuat: KVKK ve ilgili alt mevzuat"]
```

## Bu yetenek ne yapmaz
- **Çıkar çatışması (conflicts check) yapmaz.** Çatışma avukatın işidir; bu sadece kullanıcının beyanını kaydeder.
- **Saklama süresini (retention) uygulamaz.** Kapatmak arşivler, silmez.
- **Çıktıları otomatik yönlendirmez.** Çıktının nereye yazılacağına ana yetenek karar verir, bu yetenek sadece hangi dosyanın aktif olduğunu söyler.
