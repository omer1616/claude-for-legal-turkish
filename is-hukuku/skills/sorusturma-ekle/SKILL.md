---
name: sorusturma-ekle
description: >
  Açık bir soruşturmaya veri ekler — belgeler, görüşme notları veya
  gözlemler. Toplu verileri belgelenmiş çekme kriterlerine göre işler, önemli
  kalemleri yüzeye çıkarır ve kapsam doğrulaması için okunan her şeyi
  günlükler. Açık bir soruşturma için yeni kanıt, görüşme notu veya belge
  üretimi geldiğinde kullan.
argument-hint: "[dosya adı veya slug'ı, sonra veriyi yapıştır veya ekle]"
---

# /sorusturma-ekle

Açık bir soruşturma günlüğüne veri ekler. Belgelenmiş çekme kriterlerini
kullanarak belge yığınlarını işler, önemli kalemleri yüzeye çıkarır, kapsam
doğrulaması için okunan her şeyi günlükler.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` dosyasını yükle.
2. `ic-sorusturma` referans skill'ini yükle ve Mod 2'yi (Veri ekleme) çalıştır.
3. İşlemeden sonra yüzeye çıkarma oranını ve yüzeye çıkarılan kalemlerin
   listesini göster.
4. Veri bir kontrol listesi kalemini kapsıyorsa kaynak kontrol listesini
   güncellemeyi öner.

## Örnekler

```
/is-hukuku:sorusturma-ekle [dosya adı]
[görüşme notlarını yapıştır]
```

```
/is-hukuku:sorusturma-ekle [dosya adı]
[e-posta dökümünü ekle]
```

> Ayrıntılı iğne-bulma süreci, günlük kaydı formatı, yüzeye-çıkarma oranı
> kuralları ve kaynak-kontrol-listesi izleme `ic-sorusturma` referans
> skill'inde yaşar — esaslı işe başlamadan önce onu yükle.
