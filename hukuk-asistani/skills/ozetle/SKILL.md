---
name: ozetle
description: Hukuki bir metni özetler — mahkeme kararı, bilirkişi raporu, sözleşme, mevzuat veya uzun dilekçe. "Şunu özetle", "bu karar ne diyor", "bu rapora hızlı bakayım" dendiğinde kullan.
argument-hint: "[dosya yolu — veya metni yapıştır]"
---

# /ozetle

Amaç: uzun hukuki metni, avukatın 2 dakikada okuyacağı güvenilir bir özete çevirmek.
Özetin değeri doğruluğundadır — özet yanlışsa hiç olmamasından kötüdür.

## Adımlar

### 1. Metni al ve türünü tanı

Dosya yolu → oku (okuyamazsan dosya-erişim protokolü). Yapıştırma → doğrudan.
Türü kendin tanı (mahkeme/tahkim kararı · bilirkişi raporu · sözleşme · mevzuat ·
dilekçe · diğer); emin değilsen sor. >50 sayfa ise büyük-girdi kuralı: ne okuduğunu
inceleyen notuna yaz.

### 2. Uzunluk

Varsayılan **kısa özet** (~yarım sayfa). Metin çok katmanlıysa veya kullanıcı isterse
ayrıntılı sürüm; sorup bekletme — kısa yaz, sonunda "ayrıntılı ister misin?" seçeneği sun.

### 3. Tür bazlı format

İş-ürünü başlığı + inceleyen notu üstte. Sonra:

**Mahkeme kararı:**
- Künye — mahkeme/daire, tarih, esas/karar no (belgede yazdığı gibi, `[kullanıcı verdi]`)
- Uyuşmazlık — tek cümle
- Tarafların iddiaları — ikişer cümle
- Gerekçe — kararın asıl mantığı (en önemli bölüm; kısaltırken hukuki testi kaybetme)
- Hüküm — ne karar verildi (kabul/red/bozma/onama, tazminat tutarları)
- Bizim için önemi `[incele]` — kullanıcının bağlamı biliniyorsa
- Önemli pasajlar — kelimesi kelimesine, sayfa/paragraf referanslı (kanonik alıntı kuralı)

**Bilirkişi raporu:**
- Bilirkişiye sorulan sorular · Tespitler (madde madde) · Sonuç/kanaat ·
  **İtiraza açık noktalar** `[incele]` — yöntem eleştirisi, atlanmış belge, çelişki

**Sözleşme:**
- Taraflar, konu, bedel, süre/fesih tek blokta · dikkat çeken maddeler
- Not: kullanıcı risk analizi istiyorsa özet formatına zorlamak yerine
  `/hukuk-asistani:sozlesme-incele` öner (yanlış skill'e zorlamama kuralı) — ama
  önce istediği özeti ver.

**Mevzuat:**
- Ne düzenliyor · kimi kapsıyor · temel yükümlülükler · yaptırımlar ·
  yürürlük/geçiş hükümleri `[doğrula — yürürlük tarihleri değişebilir]`

**Dilekçe/diğer:** iddia-talep-dayanak üçlüsünü çıkar; format serbest ama başlıklı.

### 4. Doğruluk kuralları

- Özet YALNIZCA metinde olanı söyler. Metnin dışından hukuki bağlam eklersen ayrı
  "Bağlam" başlığı altında ve etiketli (`[model bilgisi — doğrula]`) ver — metnin
  içeriğiyle harmanlanmaz.
- Alıntı = kelimesi kelimesine + konum. Yaklaşık alıntı yok.
- Metin okumadığın atıflara/eklere gönderme yapıyorsa bunu belirt: "Karar, elimde
  olmayan bilirkişi raporuna atıf yapıyor — özet o rapor okunmadan eksiktir."

### 5. Kaydet ve kapat

Kullanıcı isterse (veya belge kayıtlı bir dosyaya aitse) `ozetler/` ya da
`dosyalar/<slug>/` altına `<konu>-ozet-YYYY-AA-GG.md` kaydet; her özet için sormadan
diske yazma — sohbette vermek çoğu zaman yeterli. Diske yazarsan eklenti CLAUDE.md'deki
**Word (.docx) ikizi** kuralına göre aynı adla `.docx` de üret (müvekkile/yönetime
iletilecekse Word kopyası işini kolaylaştırır).

Kapanışta kısa seçenekler: (1) ayrıntılı sürüm, (2) belirli bölümü derinleştir,
(3) [karara itiraz noktaları çıkar / sözleşme için tam inceleme / rapora itiraz
dilekçesi] — türe uygun olanı öner.
