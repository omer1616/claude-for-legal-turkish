---
name: sorusturma-ac
description: >
  Yeni bir iç soruşturma dosyası açar — intake çalıştırır, kaynak kontrol
  listesini oluşturur ve kalıcı soruşturma günlüğünü yaratır. Bir şikayet veya
  iddia geldiğinde ve avukatın meslek sırrı kapsamında bir soruşturma çalışma
  alanı kurması gerektiğinde kullan.
argument-hint: "[iddianın kısa açıklaması]"
---

# /sorusturma-ac

Yeni bir soruşturma dosyası açar — intake çalıştırır, kaynak kontrol listesini
oluşturur ve kalıcı soruşturma günlüğünü yaratır.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` dosyasını yükle.
2. `ic-sorusturma` referans skill'ini yükle ve Mod 1'i (Açma) çalıştır.
3. Aynı slug'lı bir dosya zaten varsa, üzerine yazmadan önce uyar.

## Örnekler

```
/is-hukuku:sorusturma-ac
Ankara ofisinde bir yöneticiye karşı taciz şikayeti dosyalandı.
```

```
/is-hukuku:sorusturma-ac
(skill ayrıntıları soracak)
```

> Ayrıntılı intake, meslek sırrı oluşum gereksinimleri, kaynak kontrol listesi
> ve günlük şablonları `ic-sorusturma` referans skill'inde yaşar — esaslı işe
> başlamadan önce onu yükle.
