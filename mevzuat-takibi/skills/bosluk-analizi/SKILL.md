---
name: bosluk-analizi
description: Açık boşluk takipçisi — nelerin işaretlendiği ve henüz kapatılmadığı. Kullanıcı "hangi boşluklar açık", "boşluk takipçisi", "iyileştirme durumu" sorduğunda veya bir boşluğu kapatmak (--close GAP-ID) veya riski kabul etmek (--accept GAP-ID) istediğinde kullanın.
argument-hint: "[opsiyonel: --close GAP-ID | --accept GAP-ID]"
---

# /bosluk-analizi

1. `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/gap-tracker.yaml` adresindeki boşluk takipçisini (gap tracker) okuyun.
2. Eğer `--close`: boşluğu çözüm notuyla birlikte kapatıldı (closed) olarak işaretleyin.
3. Eğer `--accept`: risk kabul etme gerekçesini ve kabul edeni kaydedin, durumu -> risk-kabul-edildi (risk-accepted) yapın.
4. Aksi takdirde: açık boşlukları yaş ve önemlilik seviyesine göre raporlayın.

> Detaylı takipçi şeması, durum raporu formatı, yönetici bildirim mantığı, hatırlatıcı ritmi, kapatma/risk kabul modları ve önemli eylem onayı (gate), **bosluk-cikarici** (gap-surfacer) referans yeteneğinde bulunur — esaslı bir işlem yapmadan önce onu yükleyin.
