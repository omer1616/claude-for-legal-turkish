---
name: dosya-calisma-alani
description: Çok-müvekkilli pratikler için dosya çalışma alanlarını yönetir — aktif dosyayı oluşturur, listeler, geçiş yapar, kapatır veya ayırır. Kullanıcı yeni bir dosya çalışma alanı oluşturmak, aktif dosyayı değiştirmek, dosyaları listelemek, bir dosyayı arşivlemek veya aktif dosya olmadan yalnızca pratik düzeyinde çalışmak istediğinde kullan.
argument-hint: "<yeni | listele | gecis | kapat | yok> [slug]"
---

# /dosya-calisma-alani

Avukatlar birden fazla müvekkil ve dosyayla çalışır. Bir dosya çalışma alanı, bir müvekkilin veya işin bağlamını diğerlerinden ayrı tutar. Bu komut bu çalışma alanlarını yönetir.

## Alt Komutlar

- `/dava-takibi:dosya-calisma-alani yeni <slug>` — yeni dosya çalışma alanı oluştur, kısa intake çalıştır, `matter.md` yaz
- `/dava-takibi:dosya-calisma-alani listele` — dosyaları durum ve aktif bayrakla listele
- `/dava-takibi:dosya-calisma-alani gecis <slug>` — aktif dosyayı ayarla
- `/dava-takibi:dosya-calisma-alani kapat <slug>` — bir dosyayı arşivle (`~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_arsivlendi/` içine taşı, asla silme)
- `/dava-takibi:dosya-calisma-alani yok` — aktif herhangi bir dosyadan ayır, yalnızca pratik düzeyinde çalış

Not: `/dava-takibi:dosya-brifingi [slug]` (alt komut olmadan) belirli bir dosya hakkında brifing üretir — şirket-içi portföy incelemesi için yararlı. Dosya çalışma alanı yönetimi burada yaşar.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` oku — `## Dosya çalışma alanları` bölümünün dolu olduğunu teyit et. `Etkin` `✗` ise kullanıcıya söyle: "Dosya çalışma alanları kapalı — tek müvekkilli şirket-içi pratik olarak yapılandırılmışsınız, dolayısıyla eklenti pratik düzeyi bağlamıyla otomatik çalışır. Gerçekten birden fazla müvekkilinizle çalışıyorsanız, `/dava-takibi:ilk-kurulum --redo` çalıştırın ve büro avukatı veya bağımsız pratik ayarı seçin. Aksi hâlde `/dosya-calisma-alani`'na hiç ihtiyaç duymazsınız." Hata verme — devre dışı durum şirket-içi kullanıcılar için beklenen durumdur.
2. Aşağıdaki iş akışını ve referansı uygula.
3. `$ARGUMENTS`'ın ilk jetonuna göre yönlendir:
   - `yeni` → intake görüşmesini çalıştır, `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/<slug>/matter.md` yaz, `history.md` ve `notes.md` oluştur.
   - `listele` → `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/*/matter.md`'yi listele, tablo yazdır, aktif dosyayı işaretle.
   - `gecis` → pratik düzeyi CLAUDE.md'deki `Aktif dosya:` satırını güncelle.
   - `kapat` → `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/<slug>/` klasörünü `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_arsivlendi/<slug>/` konumuna taşı, `history.md`'ye kapanma tarihini kaydet.
   - `yok` → `Aktif dosya:`'yı `yok — yalnızca pratik düzeyi bağlam` olarak ayarla.
4. Yazmadan önce kullanıcıya neyin değiştiğini göster ve teyit et.

## Notlar

- Skill, pratik düzeyi CLAUDE.md'deki `Çapraz-dosya bağlamı` `açık` olmadığı sürece dosyalar arasında okuma yapmaz.
- Arşivleme silme değildir — kapatılan dosyalar saklama/çatışma amaçlı okunabilir kalır.
- Slug'lar kısa çizgili küçük harftir. Arşivlenen ve aktif olanlar arasında slug yeniden kullanılıyorsa arşivlenen `_arsivlendi/<slug>/` altında korunur.

---

# Dosya Çalışma Alanı

Çok-müvekkilli avukatlar (büro avukatı — tek kişilik, küçük büro, büyük büro) birçok dosyayla çalışır. Birinden gelen bağlam diğerine sızmamalıdır. Bu skill bunu gerçek kılan ince dosya yönetim katmanıdır.

**Varsayılan durum kapalıdır.** Şirket-içi kullanıcılar bunu hiç görmez — yalnızca pratik düzeyinde çalışırlar. Dosya çalışma alanları, soğuk başlangıçta büro avukatı kullanıcılar için açılır veya pratik düzeyi CLAUDE.md'deki `## Dosya çalışma alanları` bölümü düzenlenerek. `Etkin` `✗` ise bu skill çalışmaz; `/dosya-calisma-alani` skill'i devre dışı durumu açıklar ve gerçekten dosya izolasyonuna ihtiyaç duyan kullanıcılar için `/ilk-kurulum --redo` önerir.

## Depolama Düzeni

Tüm dosya verisi şurada yaşar:

```
~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/
├── CLAUDE.md                       # pratik düzeyi pratik profili
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, dosya türü, kilit olgular, geçersizlemeler
    │   ├── history.md              # olayların, kararların, taslakların, incelemelerin tarihli kaydı
    │   ├── notes.md                # serbest biçim çalışma notları
    │   └── ciktilar/               # bu dosya için skill çıktıları (isteğe bağlı alt klasör)
    └── _arsivlendi/
        └── <slug>/                 # kapatılan dosyalar — okunabilir ama aktif değil
```

Slug'lar kısa çizgili küçük harftir. Örnekler: `acme-alacak-2026`, `zenith-yenileme`, `tedarikci-xyz-nda`.

## Aktif Dosya Pratik CLAUDE.md'dedir

Pratik düzeyi CLAUDE.md'deki `## Dosya çalışma alanları` altındaki `Aktif dosya:` satırı tek doğruluk kaynağıdır. Dosya değiştirmek bu satırı düzenler. Ayrı durum dosyası yok.

## Alt Komut Mantığı

### `yeni <slug>`

1. Slug'ın `matters/<slug>/` veya `matters/_arsivlendi/<slug>/`'da zaten olmadığını teyit et. Yeniden kullanılıyorsa farklı bir slug seçmesi için sor.
2. Intake görüşmesini çalıştır:
   - **Müvekkil** (temsil ettiğimiz taraf, veya şirket-içiyse iç iş birimi)
   - **Karşı taraf** (karşı taraf — birden fazla olabilir)
   - **Dosya türü** (eklentinin pratik profilinden tipik kategorileri oku; dava-takibi için: sözleşme uyuşmazlığı | iş hukuku | fikri mülkiyet | düzenleyici / soruşturma | ürün sorumluluğu | toplu dava | diğer)
   - **Gizlilik düzeyi** (standart | artırılmış | temiz ekip — artırılmış, çapraz-dosya ayarlarında ekstra özen gerektirir)
   - **Kilit olgular** (2–5 cümle: bu dosyanın ne hakkında olduğu, paydaşların kimler olduğu, neler risk altında)
   - **Pratik kılavuza dosyaya özgü geçersizlemeler** (ör. "müvekkil 12 değil 24 aylık sorumluluk sınırı istiyor", "karşı taraf stratejik iş ortağı — ilişkiyi koruyucu ton")
   - **İlgili dosyalar** (bağlantılı dosyaların slug'ları)
3. Aşağıdaki şablonu kullanarak `matters/<slug>/matter.md` yaz.
4. `matters/<slug>/history.md` dosyasını tek "Açıldı" kaydıyla başlat.
5. Boş `matters/<slug>/notes.md` oluştur.
6. Yeni dosyaya **otomatik geçiş yapma**. Sor: "`<slug>`'a şimdi geçmek ister misiniz? (`/dava-takibi:dosya-calisma-alani gecis <slug>`)"

### `listele`

`matters/*/matter.md`'yi listele. Durumu çıkarmak için her dosyanın ön maddesini veya ilk birkaç satırını oku. Tablo yazdır:

| Slug | Müvekkil | Dosya türü | Durum | Açılış | Aktif |
|---|---|---|---|---|---|

Şu anda aktif olan dosyayı `*` ile işaretle. Varsa `_arsivlendi/*`'yi ayrı "Arşivlendi" başlığı altına ekle.

### `gecis <slug>`

1. `matters/<slug>/matter.md`'nin var olduğunu teyit et. Yoksa `/dava-takibi:dosya-calisma-alani yeni <slug>` öner.
2. Pratik düzeyi CLAUDE.md'deki `Aktif dosya:` satırını `Aktif dosya: <slug>` olarak düzenle.
3. Doğru dosyada olduklarını teyit edebilmeleri için matter.md özetini kullanıcıya göster.

### `kapat <slug>`

1. `matters/<slug>/`'un var olduğunu teyit et.
2. Bugünün tarihiyle `matters/<slug>/history.md` dosyasına "Kapatıldı" kaydı ekle.
3. `matters/<slug>/` klasörünü → `matters/_arsivlendi/<slug>/` konumuna taşı.
4. Kapatılan dosya aktif dosyaysa, `Aktif dosya:`'yı `yok — yalnızca pratik düzeyi bağlam` olarak ayarla.

### `yok`

Pratik düzeyi CLAUDE.md'deki `Aktif dosya:`'yı `yok — yalnızca pratik düzeyi bağlam` olarak ayarla. Kullanıcıyla teyit et.

## `matter.md` Şablonu

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar — role göre farklılaşır; bkz. pratik düzeyi CLAUDE.md'de `## Bunu Kim Kullanıyor`]

# Dosya: [Müvekkil] — [kısa açıklama]

**Slug:** [slug]
**Açılış:** [YYYY-AA-GG]
**Durum:** aktif
**Gizlilik:** [standart / artırılmış / temiz-ekip]

---

## Taraflar

**Müvekkil:** [ad]
**Karşı taraf:** [ad(lar)]

## Dosya türü

[sözleşme uyuşmazlığı | iş hukuku | fikri mülkiyet | düzenleyici/soruşturma | ürün sorumluluğu | toplu dava | diğer — tek satır gerekçeyle]

## Kilit Olgular

[2–5 cümle. Bu dosyanın ne hakkında olduğu. Paydaşların kimler olduğu. Neler risk altında. Varsayılan kılavuzdan farklı kılan şey.]

## Dosyaya Özgü Geçersizlemeler

*Pratik düzeyi kılavuzdan yalnızca bu dosyaya uygulanan herhangi bir sapma.*

- [ör. "Sorumluluk sınırı: müvekkil ev standardı 12 değil 24 ay istiyor."]
- [ör. "Ton: ilişkiyi koruyucu — karşı taraf stratejik iş ortağı."]
- [ör. "Uygulanacak hukuk: Türk hukuku olmak zorunda."]

## İlgili Dosyalar

- [slug — neden ilgili tek satır]

## Gizlilik Notları

[Artırılmış veya temiz ekip ise nedenini açıkla. Dosya belgelerini kimler görebilir. Küresel açık olsa bile çapraz-dosya bağlamına izin verilip verilmediği.]
```

## `history.md` Başlangıcı

```markdown
# Geçmiş: [Müvekkil] — [kısa açıklama]

Yalnızca ekleme yapılan olay kaydı. En yenisi en üstte.

---

## [YYYY-AA-GG] — Dosya Açıldı

Intake tamamlandı. Slug: `[slug]`. Durum: aktif.
[matter.md'nin ötesinde korunmaya değer ilk bağlam — ör. "[karşı taraf]'tan gelen ilk taslağa yanıt olarak açıldı."]
```

## Çapraz-Dosya Bağlamı

Pratik düzeyi CLAUDE.md'nin `Çapraz-dosya bağlamı:` bayrağı vardır. `kapalı` (varsayılan) olduğunda, A dosyasında çalışan bir skill **asla** başka herhangi bir `B` için `matters/B/` dosyalarını okumaz. Nokta. Ayarın sağladığı gizlilik güvencesi budur.

`açık` olduğunda, bir skill dosyalar arasında yalnızca kullanıcı açıkça istediğinde okuyabilir (ör. "son beş tedarikçi dosyasındaki sorumluluk sınırı pozisyonumuzu karşılaştır"). `açık` olduğunda bile varsayılan, kullanıcı çapraz-dosya görünümü istemediği sürece yalnızca aktif dosyayı yüklemektir.

## Bu Skill'in Yapmadıkları

- **Çatışma taraması yapmak.** Çatışmalar avukatın/büronun işidir; intake kullanıcının beyan ettiğini kaydeder.
- **Saklama politikasını uygulamak.** Kapatmak arşivler; silmez. Saklama politikası kapsam dışıdır.
- **Çıktıları otomatik yönlendirmek.** Özsel skill nereye yazacağına karar verir; bu skill yalnızca hangi klasörün aktif olduğunu söyler.
- **Çapraz-dosyanın uygun olup olmadığına karar vermek.** Bayrağı okur ve uygular.