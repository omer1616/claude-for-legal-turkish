---
name: dosya-calisma-alani
description: >
  Dosya çalışma alanlarını yönetir — yeni, listele, geç, kapat veya ayır
  (pratik-düzeyi). Çok-müvekkilli bir uygulayıcı bir dosya oluşturmak, aktif
  dosyayı değiştirmek, dosyaları listelemek, bir dosyayı arşivlemek veya
  pratik-düzeyi bağlama ayrılmak istediğinde, veya başka bir skill hangi
  dosyada çalıştığını bilmesi gerektiğinde kullan.
argument-hint: "<yeni | listele | gecis | kapat | yok> [slug]"
---

# /dosya-calisma-alani

Uygulayıcılar birden fazla müvekkil ve dosya genelinde çalışır. Bir dosya
çalışma alanı bir müvekkilin veya işin bağlamını her diğerinden ayrı tutar.
Bu komut bu çalışma alanlarını yönetir.

## Alt Komutlar

- `/is-hukuku:dosya-calisma-alani yeni <slug>` — yeni bir dosya çalışma
  alanı oluştur, kısa bir intake çalıştır, `matter.md` yaz
- `/is-hukuku:dosya-calisma-alani listele` — dosyaları durum ve aktif
  bayrakla listele
- `/is-hukuku:dosya-calisma-alani gecis <slug>` — aktif dosyayı ayarla
- `/is-hukuku:dosya-calisma-alani kapat <slug>` — bir dosyayı arşivle
  (`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/matters/_arsivlendi/`
  içine taşı, asla silme)
- `/is-hukuku:dosya-calisma-alani yok` — aktif herhangi bir dosyadan ayrıl,
  yalnızca pratik-düzeyinde çalış

## Talimatlar

1. Pratik-düzeyi CLAUDE.md'yi oku — `## Dosya çalışma alanları` bölümünün
   dolu olduğunu teyit et. `Etkin` `✗` ise kullanıcıya söyle: "Dosya çalışma
   alanları kapalı — tek müvekkilli şirket-içi pratik olarak
   yapılandırılmışsınız, dolayısıyla eklenti pratik-düzeyi bağlamıyla
   otomatik çalışır. Gerçekten birden fazla müvekkille (veya birden fazla
   ayrı çalışan durumuyla) çalışıyorsanız, `/is-hukuku:ilk-kurulum --redo`
   çalıştırın ve özel pratik ortamını seçin. Aksi hâlde `/dosya-calisma-
   alani`'na hiç ihtiyaç duymazsınız." Hata verme — devre dışı durum
   şirket-içi kullanıcılar için beklenen durumdur.
2. Aşağıdaki iş akışını ve referansı uygula.
3. `$ARGUMENTS`'ın ilk jetonuna göre yönlendir:
   - `yeni` → intake görüşmesini çalıştır,
     `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/matters/<slug>/matter.md`
     yaz, `history.md` ve `notes.md` oluştur.
   - `listele` →
     `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/matters/*/matter.md`'yi
     listele, tablo yazdır, aktif dosyayı işaretle.
   - `gecis` → pratik-düzeyi CLAUDE.md'deki `Aktif dosya:` satırını
     güncelle.
   - `kapat` →
     `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/matters/<slug>/`
     klasörünü
     `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/matters/_arsivlendi/<slug>/`
     konumuna taşı, `history.md`'ye kapanma tarihini kaydet.
   - `yok` → `Aktif dosya:`'yı `yok — yalnızca pratik-düzeyi bağlam` olarak
     ayarla.
4. Yazmadan önce kullanıcıya neyin değiştiğini göster ve teyit et.

## Notlar

- Skill, pratik-düzeyi CLAUDE.md'deki `Çapraz-dosya bağlamı` `açık`
  olmadığı sürece dosyalar arasında okuma yapmaz.
- Arşivleme silme değildir — kapatılan dosyalar saklama/çatışma amaçlı
  okunabilir kalır.
- Slug'lar kısa çizgili küçük harftir. Arşivlenen ve aktif olanlar arasında
  slug yeniden kullanılıyorsa arşivlenen `_arsivlendi/<slug>/` altında
  korunur.

---

Çok-müvekkilli uygulayıcılar (özel pratik — bağımsız, küçük büro, büyük
büro) birçok dosyayla çalışır. Birinden gelen bağlam diğerine sızmamalıdır.
Bu skill bunu gerçek kılan ince dosya yönetim katmanıdır. Şirket içi iş
hukuku avukatları genellikle bireysel çalışan durumlarını (bir fesih, bir
soruşturma, bir izin, bir işe alım, bir sınıflandırma kararı veya bir ülke
genişleme projesi) izler; bunlar tipik olarak izole müvekkil çalışma
alanlarında değil, eklentinin normal çıktı klasörlerinde tutulur.

**Varsayılan durum kapalıdır.** Şirket-içi kullanıcılar bunu hiç görmez —
yalnızca pratik-düzeyinde çalışırlar. Dosya çalışma alanları, soğuk
başlangıçta özel pratik kullanıcılar için açılır veya pratik-düzeyi
CLAUDE.md'deki `## Dosya çalışma alanları` bölümü düzenlenerek. `Etkin`
`✗` ise bu skill çalışmaz; `/dosya-calisma-alani` skill'i devre dışı
durumu açıklar ve gerçekten dosya izolasyonuna ihtiyaç duyan kullanıcılar
için `/ilk-kurulum --redo` önerir.

## Depolama Düzeni

Tüm dosya verisi şurada yaşar:

```
~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/
├── CLAUDE.md                       # pratik-düzeyi pratik profili
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, dosya türü, kilit olgular, geçersizlemeler
    │   ├── history.md              # olayların, kararların, taslakların, incelemelerin tarihli kaydı
    │   ├── notes.md                # serbest biçim çalışma notları
    │   └── ciktilar/                # bu dosya için skill çıktıları (isteğe bağlı alt klasör)
    └── _arsivlendi/
        └── <slug>/                 # kapatılan dosyalar — okunabilir ama aktif değil
```

Slug'lar kısa çizgili küçük harftir. Örnekler: `ayse-fesih-2026`,
`almanya-genisleme`, `taciz-sorusturma-2026-03`.

## Aktif Dosya Pratik CLAUDE.md'dedir

Pratik-düzeyi CLAUDE.md'deki `## Dosya çalışma alanları` altındaki `Aktif
dosya:` satırı tek doğruluk kaynağıdır. Dosya değiştirmek bu satırı
düzenler. Ayrı bir durum dosyası yoktur.

## Alt Komut Mantığı

### `yeni <slug>`

1. Slug'ın `matters/<slug>/` veya `matters/_arsivlendi/<slug>/`'da zaten
   olmadığını teyit et. Yeniden kullanılıyorsa farklı bir slug seçmesi için
   sor.
2. Intake görüşmesini çalıştır:
   - **Müvekkil** (temsil ettiğimiz taraf, veya şirket-içiyse ilgili iş
     birimi)
   - **Karşı taraf** (çalışan, aday veya karşı taraf — birden fazla olabilir)
   - **Dosya türü** (eklentinin pratik profilinden tipik kategorileri oku;
     is-hukuku için: işe alım | fesih | soruşturma | izin | uyarlama |
     sınıflandırma | ülke genişlemesi | politika projesi | diğer)
   - **Gizlilik düzeyi** (standart | artırılmış | temiz ekip — artırılmış,
     çapraz-dosya ayarlarında ekstra özen gerektirir)
   - **Kilit olgular** (2–5 cümle: bu dosyanın ne hakkında olduğu,
     paydaşların kimler olduğu, neler risk altında)
   - **Pratik kılavuza dosyaya özgü geçersizlemeler** (ör. "bu çalışan için
     ev standardı yerine 3 aylık kıdem tazminatı öngörülüyor", "bu bir
     sendikalı işyeri, ek usul geçerli")
   - **İlgili dosyalar** (bağlantılı dosyaların slug'ları)
3. Aşağıdaki şablonu kullanarak `matters/<slug>/matter.md` yaz.
4. `matters/<slug>/history.md` dosyasını tek "Açıldı" kaydıyla başlat.
5. Boş `matters/<slug>/notes.md` oluştur.
6. Yeni dosyaya **otomatik geçiş yapma**. Sor: "`<slug>`'a şimdi geçmek
   ister misiniz? (`/is-hukuku:dosya-calisma-alani gecis <slug>`)"

### `listele`

`matters/*/matter.md`'yi listele. Durumu çıkarmak için her dosyanın ön
maddesini veya ilk birkaç satırını oku. Tablo yazdır:

| Slug | Müvekkil | Dosya türü | Durum | Açılış | Aktif |
|---|---|---|---|---|---|

Şu anda aktif olan dosyayı `*` ile işaretle. Varsa `_arsivlendi/*`'yi ayrı
"Arşivlendi" başlığı altına ekle.

### `gecis <slug>`

1. `matters/<slug>/matter.md`'nin var olduğunu teyit et. Yoksa
   `/is-hukuku:dosya-calisma-alani yeni <slug>` öner.
2. Pratik-düzeyi CLAUDE.md'deki `Aktif dosya:` satırını `Aktif dosya:
   <slug>` olarak düzenle.
3. Doğru dosyada olduklarını teyit edebilmeleri için matter.md özetini
   kullanıcıya göster.

### `kapat <slug>`

1. `matters/<slug>/`'un var olduğunu teyit et.
2. Bugünün tarihiyle `matters/<slug>/history.md` dosyasına "Kapatıldı"
   kaydı ekle.
3. `matters/<slug>/` klasörünü → `matters/_arsivlendi/<slug>/` konumuna
   taşı.
4. Kapatılan dosya aktif dosyaysa, `Aktif dosya:`'yı `yok — yalnızca
   pratik-düzeyi bağlam` olarak ayarla.

### `yok`

Pratik-düzeyi CLAUDE.md'deki `Aktif dosya:`'yı `yok — yalnızca
pratik-düzeyi bağlam` olarak ayarla. Kullanıcıyla teyit et.

## `matter.md` Şablonu

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar — role göre
farklılaşır; bkz. pratik-düzeyi CLAUDE.md'de `## Bunu kim kullanıyor`]

# Dosya: [Müvekkil/Çalışan] — [kısa açıklama]

**Slug:** [slug]
**Açılış:** [YYYY-AA-GG]
**Durum:** aktif
**Gizlilik:** [standart / artırılmış / temiz-ekip]

---

## Taraflar

**Müvekkil:** [ad]
**İlgili çalışan/aday/karşı taraf:** [ad(lar)]

## Dosya türü

[işe alım | fesih | soruşturma | izin | uyarlama | sınıflandırma | ülke
genişlemesi | politika projesi | diğer — tek satır gerekçeyle]

## Kilit Olgular

[2–5 cümle. Bu dosyanın ne hakkında olduğu. Paydaşların kimler olduğu.
Neler risk altında. Varsayılan kılavuzdan farklı kılan şey.]

## Dosyaya Özgü Geçersizlemeler

*Pratik-düzeyi kılavuzdan yalnızca bu dosyaya uygulanan herhangi bir
sapma.*

- [ör. "Kıdem tazminatı: bu çalışan için ev standardı 30 gün yerine 45 gün
  ücret öngörülüyor."]
- [ör. "Bu bir sendikalı işyeri, ek usul geçerli."]
- [ör. "Uygulanacak hukuk: yurt dışı şubede yerel hukuk geçerli."]

## İlgili Dosyalar

- [slug — neden ilgili tek satır]

## Gizlilik Notları

[Artırılmış veya temiz ekip ise nedenini açıkla. Dosya belgelerini kimler
görebilir. Küresel açık olsa bile çapraz-dosya bağlamına izin verilip
verilmediği.]
```

## `history.md` Başlangıcı

```markdown
# Geçmiş: [Müvekkil/Çalışan] — [kısa açıklama]

Yalnızca ekleme yapılan olay kaydı. En yenisi en üstte.

---

## [YYYY-AA-GG] — Dosya Açıldı

Intake tamamlandı. Slug: `[slug]`. Durum: aktif.
[matter.md'nin ötesinde korunmaya değer ilk bağlam — ör. "[İK]'dan gelen
şikayet üzerine açıldı."]
```

## Çapraz-Dosya Bağlamı

Pratik-düzeyi CLAUDE.md'nin `Çapraz-dosya bağlamı:` bayrağı vardır.
`kapalı` (varsayılan) olduğunda, A dosyasında çalışan bir skill **asla**
başka herhangi bir `B` için `matters/B/` dosyalarını okumaz. Nokta.
Ayarın sağladığı gizlilik güvencesi budur — bir çalışanın soruşturması,
uyarlaması veya feshi başka bir çalışanın işi için sızmamalıdır.

`açık` olduğunda, bir skill dosyalar arasında yalnızca kullanıcı açıkça
istediğinde okuyabilir (ör. "son beş fesih dosyasındaki kıdem tazminatı
uygulamamızı karşılaştır"). `açık` olduğunda bile varsayılan, kullanıcı
çapraz-dosya görünümü istemediği sürece yalnızca aktif dosyayı yüklemektir.

## Bu Skill'in Yapmadıkları

- **Çatışma taraması yapmak.** Çatışmalar avukatın/büronun işidir; intake
  kullanıcının beyan ettiğini kaydeder.
- **Saklama politikasını uygulamak.** Kapatmak arşivler; silmez. Saklama
  politikası kapsam dışıdır.
- **Çıktıları otomatik yönlendirmek.** Özsel skill nereye yazacağına karar
  verir; bu skill yalnızca hangi klasörün aktif olduğunu söyler.
- **Çapraz-dosyanın uygun olup olmadığına karar vermek.** Bayrağı okur ve
  uygular.
