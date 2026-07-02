---
name: sorusturma-ozeti
description: >
  Meslek sırrı kapsamındaki soruşturma notundan hedef kitleye özel bir özet
  taslaklar — İK, üst yönetim veya dış avukat versiyonları. Bir soruşturma
  notunun, tam meslek sırrı kapsamındaki iş ürününü görmemesi gereken bir
  hedef kitleye iletilmesi gerektiğinde kullan.
argument-hint: "[dosya adı] [hedef kitle: ik / yonetim / dis-avukat]"
---

# /sorusturma-ozeti

Meslek sırrı kapsamındaki soruşturma notundan sadeleştirilmiş, hedef
kitleye uygun bir özet taslaklar. İK özetleri meslek sırrı analizi içermez.
Yönetim özetleri üst düzeydir. Dış avukat brifingleri tam bağlam içerir.

## Talimatlar

1. `ic-sorusturma` referans skill'ini yükle ve Mod 5'i (Hedef kitle özeti) çalıştır.
2. Henüz bir not yoksa, önce notu taslaklamayı öner.
3. İK özetleri avukatın zihinsel izlenimlerini, güvenilirlik metodolojisini
   veya hukuki risk analizini içermemeli.

## Örnekler

```
/is-hukuku:sorusturma-ozeti [dosya adı] ik
```

```
/is-hukuku:sorusturma-ozeti [dosya adı] yonetim
```

```
/is-hukuku:sorusturma-ozeti [dosya adı] dis-avukat
```

> Ayrıntılı hedef-kitle-sadeleştirme kuralları ve özet şablonları
> `ic-sorusturma` referans skill'inde yaşar — esaslı işe başlamadan önce
> onu yükle.
