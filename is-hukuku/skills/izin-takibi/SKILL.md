---
name: izin-takibi
description: >
  Açık izinleri son tarih uyarıları ve gereken kararlar için kontrol eder.
  Yalnızca eylem gerektiren izinleri yüzeye çıkarır ve nedenini açıklar — bir
  durum panosu değildir. Haftalık kullan, veya avukatın hangi izinlerin
  yaklaşan bildirim, rapor veya tükenme son tarihleri olduğunu bilmesi
  gerektiğinde.
argument-hint: "[argüman yok — İK sisteminden veya izin-kaydi.yaml'dan çalışır]"
---

# /izin-takibi

Hukuki son tarihi olan tüm açık izinleri kontrol eder ve yalnızca karar veya
eylem gerektirenleri yüzeye çıkarır. Bir durum panosu değil — ne yapman
gerektiğini ve nedenini söyler.

## Talimatlar

1. `izin-izleyici` agent'ını yükle ve tam iş akışını çalıştır.

2. Bağlı bir İK sistemi yoksa ve
   `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/izin-kaydi.yaml`
   dosyası yoksa, avukata bir izin tablosu yüklemesini veya girdi eklemek için
   `/is-hukuku:izin-kaydi` kullanmasını öner.

3. Yalnızca eylem gerektiren izinler için uyarı. Temiz izinler tek satırda
   özetlenir.

## Örnekler

```
/is-hukuku:izin-takibi
```

Bunu haftalık çalıştır — `/is-hukuku:izin-takibi` çağırmak için Pazartesi
sabahı bir hatırlatıcı ayarla. Otomatik zamanlama ayrı bir entegrasyon
gerektirir (takvim hatırlatıcısı, cron işi vb.); Claude Code agent'ları
kendi kendini zamanlamaz.
