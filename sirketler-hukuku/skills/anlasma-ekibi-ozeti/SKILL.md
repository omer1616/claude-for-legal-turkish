---
name: anlasma-ekibi-ozeti
description: >
  Due diligence bulgularını hedef kitleye uygun seviyede (liderlik için yönetici özeti, 
  ekip için çalışma özeti) bir işlem ekibi bilgilendirme notunda (brief) toplar. 
  Kullanıcı "işlem ekibine bilgi ver", "diligence'ın durumu nedir", 
  "[kitle] için bulguları özetle", "işlem güncellemesi" dediğinde veya düzenli bilgi 
  akışı ritminde kullanın.
---

# /anlasma-ekibi-ozeti

1. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` yükle → İşlem ekibi bilgilendirmesi (ritim, format, kim ne okur).
2. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/deals/[kod]/deal-context.md` yükle → işlem lideri, takvim.
3. `due-diligence-sorun-cikartma` (diligence-issue-extraction) çıktısından güncel bulguları al.

---

## Dosya (Matter) Bağlamı

`CLAUDE.md` içindeki `## Dosya çalışma alanları`nı kontrol et. Eğer etkinse ve aktif dosya yoksa sor. Çıktıları `matters/<dosya-slug>/` klasörüne yaz.

---

## Amaç

İşlem lideri (deal lead) 200 bulguyu okumaz. Nelerin önemli olduğunu, son bilgilendirmeden bu yana nelerin değiştiğini ve neye karar verilmesi gerektiğini okur. Bu yetenek, diligence çıktısını okuyucu için doğru seviyeye sıkıştırır.

## Kitle Seviyeleri

`CLAUDE.md` standardına göre — iş birimi ne okur vs. dosyaya ne girer. Varsayılan seviyeler:

| Kitle | Ne Alır | Ne Almaz |
|---|---|---|
| **Yönetim Kurulu / Sponsor** | İlk 3-5 önemli sorun, fiyat/yapı etkisi, karar kalemleri | Kategori detayı, yeşil (sorunsuz) bulgular, süreç |
| **İşlem Lideri** | Tüm kırmızılar, tüm sarılar, ilerleme, karar kalemleri, sonraki adımlar | Yeşil bulgu detayı |
| **Çalışma Ekibi** | Her şey — tam bulgular, kategori bazında durum, boşluklar | Hiçbir şey saklanmaz |

Eğer kitle seviyesi net değilse sor.

## Özet

### Yönetici (Exec) Seviyesi

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — CLAUDE.md'den]

> Bu özet, imtiyazlı/gizli diligence bulgularını bir araya getirir. Dağıtım listesini onaylamadan göndermeyin.

# [İşlem kodu] — Diligence Bilgi Notu — [tarih]

**Durum:** [Rayında / Sorunlar var / Önemli bulgular var]
**Kapsam:** VDR'ın % [X]'i incelendi

## Önemli bulgular (Material findings)

[En fazla 3-5 adet. Her biri tek paragraf. Sorun nedir, işlem için neden önemli, bununla ilgili ne yapıyoruz.]

## Gereken Kararlar

- [ ] [Belirli karar — fiyat indirimi, tazminat talebi, işlemden çekilme tetikleyicisi]
  — [kim karar verecek] — [ne zamana kadar]

## Son Bilgilendirmeden Bu Yana

[Neler değişti. Yeni bulgular, çözülen bulgular, kapsam ilerlemesi.]
```

### İşlem Lideri Seviyesi

Yukarıdakilere ek olarak:

```markdown
## Kategori Bazında Tüm Açık Sorunlar

### 🔴 Kırmızı
[Bulgu başlığı + tek satır özet — detayı için tam bulguya bağlantı (link)]

### 🟡 Sarı
[aynısı]

## İlerleme

| Kategori | İncelenen Belge | Kapsam | Kırmızılar | Sarılar | Durum |
|---|---|---|---|---|---|
| [isim] | [N/M] | [%] | [N] | [N] | [Tamamlandı / Devam Ediyor / Tıkandı] |

## Boşluklar ve Takipler

- [Bekleyen ek talep kalemleri]
- [Yönetime sorulan sorular]

## Önümüzdeki 72 Saat

[Neler incelenecek, hangi toplantılar planlandı]
```

### Çalışma Ekibi Seviyesi

Tam bulgu detayı. Yukarıdakiyle aynı yapı ama her bulgu tek satır değil, kurum formatındaki tam bloğuyla yer alır.

## Farklar (Deltalar)

Eğer bu düzenli bir bilgilendirme ise (CLAUDE.md ritmine göre), değişenlerle başla:
- Son bilgilendirmeden bu yana yeni bulgular
- Şiddeti artan/azalan bulgular
- Çözülen bulgular (onay alındı, konu açıklığa kavuştu)
- Kapsamdaki hareket

İşlem liderleri durumdan çok harekete (momentuma) önem verir. "Hala 12 sarı var" demek, "2 yeni sarı geldi, 3'ü çözüldü" demekten daha az faydalıdır.

## Devirler (Handoffs)

- **due-diligence-sorun-cikartma'dan:** Bu yetenek birikmiş bulguları oradan okur.
- **kapani-kontrol-listesi'ne:** Kapanış koşuluna (CP) dönüşen herhangi bir "gereken karar" kalemi kontrol listesine gider.

## Kapanış: Sonraki Adımlar Karar Ağacı

CLAUDE.md'deki `## Çıktılar` bölümüne uygun karar ağacıyla bitir.

## Bu yetenek ne yapmaz

- Önemlilik (materiality) kararını vermez — sorun çıkarma yeteneğinin verdiği kararları raporlar.
- İşlem ekibinin bir bulgu hakkında ne yapacağına karar vermez — kararı (ihtiyacı) yüzeye çıkarır.
- Özeti dağıtmaz — taslaklar, insan (avukat) gönderir.
