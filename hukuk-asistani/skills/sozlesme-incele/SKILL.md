---
name: sozlesme-incele
description: Bir sözleşmeyi baştan sona inceler — riskleri, tek taraflı ve eksik maddeleri sade Türkçe raporlar, müzakere önerileri verir. Müvekkil veya karşı taraf bir sözleşme taslağı gönderdiğinde, imza öncesi kontrol istendiğinde kullan.
argument-hint: "[dosya yolu — veya metni yapıştır]"
---

# /sozlesme-incele

Amaç: avukatın masasındaki sözleşmeyi, madde referanslı ve önceliklendirilmiş bir risk
raporuna çevirmek. Rapor sade Türkçe yazılır — müvekkile okunabilecek netlikte, ama
avukat incelemesi için işaretlenmiş.

## Adımlar

### 1. Metni al

Dosya yolu verildiyse oku; okuyamazsan guardrail'daki dosya-erişim protokolünü uygula
(ne olduğunu söyle, yapıştırmayı öner). Metin yapıştırıldıysa doğrudan kullan.

### 2. İki hızlı soru (okumaya başlamadan)

> 1. **Hangi taraf biziz?** (İnceleme perspektifi buna göre döner — kiracı için risk
>    olan madde kiraya veren için güvencedir.)
> 2. **Özel bir endişen veya amacın var mı?** ("fesih koşullarına özellikle bak",
>    "müvekkil ödeme planından endişeli" — yoksa "yok" de, standart geçiş yaparım.)

Kullanıcı taraf bilgisini vermeden ısrarla devam etmek isterse her iki taraf için de
işaretleyerek incele ama bunu raporda belirt.

### 3. Tamamını oku

Sözleşmeyi **baştan sona** oku. >50 sayfa ise büyük-girdi kuralı geçerli (eklenti
CLAUDE.md): önceliklendir, ne okuduğunu inceleyen notuna yaz, asla tamamını okumuş
gibi yapma.

### 4. Kontrol tabanı

Aşağıdaki başlıklar **taban**dır (tavan değil — sözleşme türüne göre ekle):

taraflar ve temsil yetkisi · konu ve kapsam · bedel, ödeme koşulları ve gecikme
sonuçları · süre, yenileme, fesih (haklı/süreli fesih, cayma) · ifa ve teslim ·
ayıp ve muayene yükümlülükleri · cezai şart ve götürü tazminat · sorumluluğun
sınırlandırılması · gizlilik · kişisel veriler (KVKK'ya uyum gerekip gerekmediği) ·
fikri mülkiyet · devir ve temlik yasağı · mücbir sebep · tebligat adresleri ·
uygulanacak hukuk ve yetkili mahkeme/tahkim · imza ve şekil (şekil şartına tabi
sözleşme türü mü?) · damga vergisi yükü `[doğrula]`

Hukuki dayanağa bağladığın her tespit kaynak etiketi taşır (çoğu zaman
`[model bilgisi — doğrula]`); sözleşmeden alıntı yapıyorsan **kelimesi kelimesine**
alıntıla ve madde numarası ver.

### 5. Raporu yaz

İş-ürünü başlığı + inceleyen notu üstte (eklenti CLAUDE.md `## Çıktılar`). Gövde:

**Sonuç** — 3-5 cümle: bu sözleşme bizim taraf için imzalanabilir mi, en kritik 2-3
nokta ne, genel dengesi nasıl. Avukatın müvekkile telefonda söyleyeceği paragraf.

**Risk tablosu** — şiddet sıralı (🔴 Engelleyici / 🟠 Yüksek / 🟡 Orta / 🟢 Düşük):

| | Madde | Sorun | Öneri |
|---|---|---|---|
| 🔴 | m.7.2 | [sorunun bir cümlelik özeti, gerekiyorsa kısa alıntıyla] | [somut değişiklik önerisi] |

**Eksik maddeler** — bu tür bir sözleşmede beklenen ama metinde olmayanlar, her biri
için neden önemli olduğu tek cümleyle.

**Müzakere önerileri** — öncelik sırasıyla: hangi maddede ne istenecek, geri çekilme
hattı ne olabilir `[incele]`.

Öznel yargı gerektiren her karar `[incele]` etiketli — sessizce "sorun değil" deme
(karar duruşu guardrail'ı).

### 6. Kaydet ve kapat

Sözleşme kayıtlı bir dosyaya aitse raporu `dosyalar/<slug>/` altına, değilse
`sozlesmeler/` altına `<konu>-inceleme-YYYY-AA-GG.md` adıyla kaydet. Ardından eklenti
CLAUDE.md'deki **Word (.docx) ikizi** kuralına göre aynı adla `.docx` üret ve
kullanıcıya ikisini de (Word dosyası + düzenlenebilir .md) söyle.

Karar ağacıyla kapat — tipik seçenekler: (1) değişiklik önerilerini madde metni olarak
taslakla (redline), (2) karşı tarafa e-posta taslağı, (3) müvekkile sade özet,
(4) belirli bir maddeyi derinlemesine analiz et.
