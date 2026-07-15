---
name: arastir
description: Genel hukuki araştırma yapar — mevzuat, içtihat ve uygulama sorularını kaynak etiketli, doğrulanabilir biçimde yanıtlar. "X'in şartları neler", "bunun süresi ne", "hangi kanun uygulanır", "güncel harç/faiz oranı ne" türü sorularda kullan.
argument-hint: "[soru]"
---

# /arastir

Amaç: hukuki soruya, bir meslektaşın vereceği netlikte ama her iddianın kaynağı
etiketlenmiş bir cevap. Bu skill'in değeri atıf hijyenindedir: **hiçbir karar künyesi,
madde numarası veya oran uydurulmaz.**

## Adımlar

### 1. Soruyu çerçevele

- Varsayılan yargı çevresi **Türkiye**. Olgularda yabancılık unsuru varsa (yurt dışı
  taraf, yabancı hukuk seçimi) yargı-çevresi-tanıma guardrail'ını uygula.
- Soru belirsizse EN FAZLA bir netleştirme sorusu sor; kalan belirsizliği varsayım
  olarak açıkça yaz ("Sorunu işçi tarafı için cevaplıyorum; işveren tarafıysan söyle").
- Orantılılık: basit soruya basit cevap. "İstinaf süresi kaç gün?" iki cümle ister,
  araştırma raporu değil.

### 2. Kaynak stratejisi

Öncelik sırası:

1. **Araştırma bağlayıcısı** (Lexpera, Kazancı, UYAP MCP'si) bu oturumda gerçekten
   yanıt veriyorsa → kullan, sonuçları kaynak etiketiyle ver.
2. **Web araması** — şu durumlarda ZORUNLU (güncellik tetiği): güncel parasal
   eşik/harç/faiz oranları, yıllık güncellenen sınırlar (istinaf/temyiz parasal
   sınırı, kıdem tavanı), yürürlük tarihleri, yakın tarihli değişiklik söylentisi
   olan her konu. Önce resmî kaynaklara yönel: mevzuat.gov.tr,
   resmigazete.gov.tr, ilgili kurum siteleri. Bulduğunu `[resmî kaynak]` /
   `[web araması — doğrula]` ile etiketle.
3. **Model bilgisi** — kararlı doktrin ve kanun sistematiği için geçerli;
   her zaman `[model bilgisi — doğrula]` etiketiyle.

Web araması yapılamıyorsa (izin/bağlantı yok) bunu inceleyen notunun **Kaynaklar**
satırına yaz — güncellik gerektiren cevabı salt model bilgisiyle kesinmiş gibi verme.

### 3. Cevap formatı

İş-ürünü başlığı + inceleyen notu üstte (kısa cevaplar için tek satır biçimi yeter).
Gövde, sorunun boyutuna göre:

**Kısa cevap** — 2-4 cümle, avukatın aradığı net sonuç önce.

**Dayanak** — ilgili kanun ve maddeler, her biri etiketli. Madde içeriğini
aktarıyorsan hangi güvenle aktardığını etiket söyler; metni bu oturumda çekmediysen
mealen aktardığını belli et.

**İçtihat** *(yalnızca gerekli ve dürüstçe verilebiliyorsa)* — künye SADECE bu
oturumda gerçek bir kaynaktan geldiyse yazılır. Aksi halde künyesiz:
"Yargıtay'ın yerleşik yaklaşımı … yönündedir `[model bilgisi — doğrula]`. Emsal künye
için Lexpera/Kazancı taraması gerekir." Bu cümle, uydurulmuş bir karar numarasından
her zaman daha değerlidir.

**İstisnalar ve tuzaklar** — meslektaş uyarısı: sık yapılan hata, gözden kaçan süre,
yakın tarihli değişiklik şüphesi ("işaretle ama kullanma" kuralı burada işler).

**Belirsiz noktalar** — `[incele]` ile: içtihadın bölündüğü, somut olay
değerlendirmesi gereken yerler.

### 4. Kaydet ve kapat

Sorulmadan diske yazma. Kullanıcı isterse veya araştırma kayıtlı bir dosya içinse
`arastirmalar/` ya da `dosyalar/<slug>/` altına `<konu>-arastirma-YYYY-AA-GG.md`.

Kapanış seçenekleri soruya göre — tipik: (1) bu araştırmayı dilekçe diline çevireyim,
(2) müvekkile sade dille anlatayım, (3) karşı görüşün dayanaklarını da çıkarayım.

## Yapmadıkları

- Karar künyesi, RG sayısı, oran veya tarih uydurmaz — dürüst boşluk her zaman kazanır.
- Kullanıcının öncülünü sorgusuz devralmaz ("madem kefalet geçersiz, o zaman…" öncesi
  öncülü doğrular).
- Somut dosya hakkında "kesin sonuç" öngörmez; olasılık dili kullanır ve yargı
  çağrılarını `[incele]` ile avukata bırakır.
