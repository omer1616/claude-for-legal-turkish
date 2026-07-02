---
name: genisletme-baslangic
description: >
  Yeni bir ülke için uluslararası genişleme planlamasını başlatır — intake
  toplar, EOR (Employer of Record) vs. tüzel kişilik çerçevelemesi çalıştırır,
  fonksiyonlar arası sorular taslaklar, ülkeye özgü işaretleri yüzeye çıkarır
  ve kalıcı bir izleyici oluşturur. Biri "[ülke]'de işe alım yapıyoruz",
  "[ülke]'ye genişleme" veya "[ülke]'de ilk işe alım" dediğinde kullan.
argument-hint: "[ülke adı]"
---

# /genisletme-baslangic

Yeni bir ülke için uluslararası genişleme projesi başlatır — intake toplar,
EOR vs. tüzel kişilik çerçevelemesi çalıştırır, fonksiyonlar arası sorular
taslaklar, ülkeye özgü işaretleri yüzeye çıkarır ve kalıcı bir izleyici
oluşturur.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
   dosyasını yükle → yargı çevresi ayak izi, eskalasyon tablosu.
2. `uluslararasi-genisletme` referans skill'ini yükle ve tam iş akışını
   çalıştır.
3. Bu ülke için zaten bir izleyici dosyası varsa
   (`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/genisletme-[slug].yaml`),
   işaretle: "Bir [ülke] genişleme izleyicisi zaten var. Güncellemek için
   `/is-hukuku:genisletme-guncelleme [ülke]` kullan, veya baştan başlamak
   istediğini onayla."
4. Tamamlandığında
   `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/genisletme-[slug].yaml`
   dosyasını oluştur.

## Örnekler

```
/is-hukuku:genisletme-baslangic Almanya
```

```
/is-hukuku:genisletme-baslangic
(skill hangi ülke olduğunu soracak)
```

> Ayrıntılı EOR vs. tüzel kişilik çerçevesi, fonksiyonlar arası sorular,
> brifing şablonları ve izleyici şeması `uluslararasi-genisletme` referans
> skill'inde yaşar — esaslı işe başlamadan önce onu yükle.
