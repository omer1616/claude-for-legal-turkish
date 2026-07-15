---
name: sozlesme-hazirla
description: Sıfırdan sözleşme taslağı hazırlar — türü ve esaslı şartları sorar, Türk hukukuna uygun tam metin taslak yazar. Kira, hizmet, satış, eser, gizlilik (NDA), iş sözleşmesi, vekâlet ücret sözleşmesi vb. gerektiğinde kullan.
argument-hint: "[sözleşme türü — ör. 'işyeri kira sözleşmesi']"
---

# /sozlesme-hazirla

Amaç: kullanılabilir, tam metin bir sözleşme taslağı — bilinmeyen yerleri dürüstçe boş
bırakan, hukuki yargı noktalarını işaretleyen, imza öncesi avukat incelemesine hazır.

## Adımlar

### 1. Esasları topla

Tek mesajda sor (verilenleri atlayarak):

> 1. **Sözleşme türü** (kira, hizmet, satış, eser, gizlilik, iş, vekâlet ücreti…)
> 2. **Taraflar** — ad/unvan; bilmiyorsan yer tutucu bırakırım
> 3. **Esaslı şartlar** — konu, bedel, süre (bir iki cümle yeter)
> 4. **Hangi taraf için kaleme alıyoruz?** (dengeli mi, müvekkil lehine mi?)
> 5. **Özel istekler** — cezai şart, teminat, rekabet yasağı, gizlilik, özel fesih
>    hakları… ("yok" geçerli cevap)

Sadece tür verilse bile makul varsayılanlarla ilerleyebilirsin — ama bedel, süre ve
taraflar gibi esaslı boşlukları `[.........]` yer tutucusuyla bırak, uydurma.

### 2. Şekil ve geçerlilik kontrolü (yazmadan önce)

Tür şekil şartına veya özel geçerlilik koşuluna tabiyse **taslaktan önce** söyle ve
taslakta uyarı notu bırak. Örnekler: taşınmaz satışı/satış vaadi (resmî şekil),
kefalet (el yazısı unsurları ve eş rızası), işçiden alınan rekabet yasağının sınırları,
tüketici işlemlerinde emredici hükümler — hepsi `[model bilgisi — doğrula]` etiketiyle.
Emredici hükümlere aykırı istek gelirse (ör. kiracı aleyhine kanuna aykırı hüküm)
sessizce yazma — riski söyle, `[incele]` işaretiyle yine de isterlerse alternatifiyle
birlikte yaz.

### 3. Taslağı yaz

Numaralı maddelerle tam metin. Standart iskelet (türe göre uyarla, gereksiz başlığı
atla):

1. Taraflar · 2. Tanımlar (gerekliyse) · 3. Sözleşmenin konusu · 4. Tarafların hak ve
yükümlülükleri · 5. Bedel ve ödeme koşulları · 6. Süre, yenileme ve fesih · 7. Cezai
şart / teminat (istendiyse) · 8. Gizlilik · 9. Kişisel verilerin korunması
(gerekliyse) · 10. Devir ve temlik yasağı · 11. Mücbir sebep · 12. Tebligat ·
13. Uyuşmazlıkların çözümü, uygulanacak hukuk ve yetkili mahkeme · 14. Yürürlük —
ardından imza blokları.

Kurallar:

- Bilinmeyen her somut değer `[.........]` — tarih, tutar, adres, unvan uydurulmaz.
- Hukuki yargı gerektiren tercihler satır içinde `[incele]` (ör. cezai şart tutarının
  orantılılığı, yetkili mahkeme seçimi).
- Kanun maddesi anılıyorsa kaynak etiketi kuralları geçerli; taslağın hukuki dayanak
  gerektirmeyen yerine gereksiz atıf koyma.
- Damga vergisi yükümlülüğü paylaşımını bir maddede düzenle ve `[doğrula]` notu düş.
- Dil: sade, güncel sözleşme Türkçesi — arkaik kalıplara ("işbu mezkûr") boğma, ama
  yerleşik terimleri de değiştirme.

### 4. Teslim

Taslak **dışa dönük belge adayıdır**: gövdeye iş-ürünü başlığı koyma; inceleyen notu
taslağın ÜSTÜNDE ayrı blok olarak verilir (sessiz mod kuralı). İnceleyen notunda en
az: doldurulacak `[.........]` sayısı, `[incele]` sayısı, şekil şartı uyarısı varsa o.

Kaydet: dosyaya bağlıysa `dosyalar/<slug>/`, değilse `sozlesmeler/` altına
`<tur>-taslak-v1.md`. Kullanıcıya söyle: "Word'e aktarmak için dosyayı açıp
kopyalayabilirsin; istersen ben de gözden geçirilmiş v2 çıkarırım."

Rol profilde **hukukçu değil** ise kapanışta bir kez: "Bu taslak imzalanmadan önce bir
avukat tarafından incelenmeli — özellikle `[incele]` işaretli yerler senin durumuna
göre karar gerektiriyor."

Karar ağacıyla kapat — tipik: (1) boşlukları birlikte dolduralım, (2) karşı taraf
gözüyle risk okuması yapayım, (3) müvekkile açıklama e-postası taslaklayayım.
