---
name: sorusturma-sorgu
description: >
  Açık bir soruşturma günlüğüne karşı sorular sorar — tanıkların ne
  söylediği, hesapların nerede çeliştiği, hangi boşlukların olduğu, her
  konuda en güçlü kanıtın ne olduğu. Avukatın her girişi yeniden okumadan
  soruşturma kaydını sorgulaması gerektiğinde kullan.
argument-hint: "[dosya adı] [soru]"
---

# /sorusturma-sorgu

Soruşturma günlüğüne karşı soruları cevaplar — tanıkların ne söylediği,
hesapların nerede çeliştiği, hangi boşlukların olduğu, her konuda en güçlü
kanıtın ne olduğu.

## Talimatlar

1. `ic-sorusturma` referans skill'ini yükle ve Mod 3'ü (Sorgu) çalıştır.
2. Cevapta her zaman günlük girdi kimliklerini (ID) atıf yap.
3. Günlükte soruyla ilgili hiçbir şey yoksa bunu açıkça söyle — "Bu
   soruşturma günlüğünde [konu] hakkında hiçbir bilgi görmedim ([N] girdi
   incelendi)" — ve bunu bir boşluk olarak işaretlemeyi öner.

## Örnekler

```
/is-hukuku:sorusturma-sorgu [dosya adı]
Davalı Aralık ayındaki ekip yemeği hakkında ne söyledi?
```

```
/is-hukuku:sorusturma-sorgu [dosya adı]
Şikayetçinin ve davalının hesapları nerede çelişiyor?
```

```
/is-hukuku:sorusturma-sorgu [dosya adı]
Hâlâ neye ihtiyacımız var?
```

> Ayrıntılı günlük-sorgu süreci, atıf kuralları ve boşluk-işaretleme
> şablonları `ic-sorusturma` referans skill'inde yaşar — esaslı işe
> başlamadan önce onu yükle.
