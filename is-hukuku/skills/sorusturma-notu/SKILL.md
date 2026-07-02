---
name: sorusturma-notu
description: >
  Soruşturma günlüğünden meslek sırrı kapsamındaki soruşturma notunu
  taslaklar veya günceller. Bir soruşturma ilk notu yazacak kadar
  ilerlediğinde, veya yeni veri eklendiğinde ve mevcut taslağın
  güncellenmesi gerektiğinde kullan.
argument-hint: "[dosya adı]"
---

# /sorusturma-notu

Günlükten meslek sırrı kapsamındaki soruşturma notunun ilk taslağını
çıkarır, veya yeni veri eklendiğinde mevcut bir taslağı günceller.

## Talimatlar

1. `ic-sorusturma` referans skill'ini yükle ve Mod 4'ü (Not taslağı/güncelleme) çalıştır.
2. İlk kez taslaklarken, kontrol listesinde hâlâ açık yüksek öncelikli
   kaynaklar varsa uyar.
3. Güncellerken, yeniden yazmadan önce ne değiştiğini göster.
4. Tüm çıktı GİZLİ VE MESLEK SIRRI KAPSAMINDA — AVUKATIN YÖNLENDİRMESİYLE
   HAZIRLANMIŞTIR olarak işaretlenir.

## Örnekler

```
/is-hukuku:sorusturma-notu [dosya adı]
```

```
/is-hukuku:sorusturma-notu [dosya adı]
(mevcut bir not varsa günceller)
```

> Ayrıntılı not yapısı, güvenilirlik değerlendirme çerçevesi ve güncelleme
> kuralları `ic-sorusturma` referans skill'inde yaşar — esaslı işe
> başlamadan önce onu yükle.
