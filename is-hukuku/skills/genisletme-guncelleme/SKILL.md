---
name: genisletme-guncelleme
description: >
  Devam eden bir uluslararası genişleme projesinin durumunu günceller —
  şimdi neyin engeli kalktığını yeniden hesaplar, gecikmiş olan her şeyi
  işaretler ve sıradaki öncelikleri yüzeye çıkarır. Son oturumdan bu yana
  iş yapıldığında ve genişleme izleyicisinin güncel durumu yansıtması
  gerektiğinde kullan.
argument-hint: "[ülke adı]"
---

# /genisletme-guncelleme

Açık bir genişleme izleyicisine döner ve son oturumdan bu yana olanlara
göre kalem durumunu günceller. Şimdi neyin engeli kalktığını yeniden
hesaplar, gecikmiş olan her şeyi işaretler ve sıradaki öncelikleri yüzeye
çıkarır.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
   dosyasını yükle.

2. İzleyici dosyasını tespit et:
   `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/genisletme-[slug].yaml`.
   Yoksa cevapla: "[Ülke] için bir genişleme izleyicisi bulunamadı. Bir
   tane başlatmak için `/is-hukuku:genisletme-baslangic [ülke]` çalıştır."

3. İzleyiciyi oku. Mevcut durumu göster:

```
[Ülke] Genişlemesi — son güncelleme [tarih]
Açık: [N] | Devam ediyor: [N] | Tamamlandı: [N] | Engellendi: [N]

Sıradaki öncelikler (en erken son tarihli veya en yüksek bağımlılıklı açık kalemler):
  [kalem] — sorumlu: [sorumlu]
  [kalem] — sorumlu: [sorumlu]
  [kalem] — sorumlu: [sorumlu]
```

4. Güncellemeleri tek bir istemde sor — her kalemi birer birer sorma:

   > Son baktığımızdan bu yana hangi kalemler ilerledi? Neyin değiştiğini
   > söyleyin (ör. "EOR kararı verildi — Deel ile gidiyoruz", "dış avukat
   > devreye girdi — Perşembe için görüşme planlandı", "PE analizi hâlâ
   > açık, vergiden bekliyoruz"). Yeni kalemler de ekleyebilir veya son
   > tarihleri değiştirebilirsiniz.

5. Güncellemeleri izleyici dosyasına uygula. Yeni `tamamlandi` olarak
   işaretlenen her kalem için, başka kalemlerin engelini kaldırıp
   kaldırmadığını kontrol et ve onları artık eyleme geçirilebilir olarak
   işaretle.

6. Herhangi bir kalemin son tarihi geçmiş ve hâlâ `acik` veya
   `devam-ediyor` ise işaretle:

```
⚠️ Gecikmiş: [kalem] — son tarihi [tarih], sorumlu: [sorumlu]
```

7. Güncellenmiş izleyiciyi yaz. Teyit et:

```
İzleyici güncellendi — [N] kalem kapatıldı, [N] hâlâ açık.
Sıradaki öncelik: [en üstteki açık kalem].
```

## Örnekler

```
/is-hukuku:genisletme-guncelleme Almanya
```

```
/is-hukuku:genisletme-guncelleme
(birden fazla izleyici varsa hangisi olduğunu soracak)
```

> Ayrıntılı izleyici şeması, kalem-durum kuralları ve bağımlılık mantığı
> `uluslararasi-genisletme` referans skill'inde yaşar — esaslı işe
> başlamadan önce onu yükle.
