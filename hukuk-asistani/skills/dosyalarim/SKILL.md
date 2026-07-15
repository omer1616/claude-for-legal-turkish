---
name: dosyalarim
description: Tüm dosyaların özet görünümü — açık dosyalar, yaklaşan duruşma ve süreler, uzun süredir işlem görmeyen dosyalar. "Dosyalarım ne durumda", "bu hafta ne var", "yaklaşan duruşmalar" diye sorulduğunda kullan.
argument-hint: "[filtre — ör. 'bu hafta' | 'kapali' | müvekkil adı]"
---

# /dosyalarim

Amaç: avukatın güne/haftaya bakışı — 10 saniyede "neyim var, ne yanıyor?"

## Adımlar

### 1. Kayıtları oku

Profildeki çalışma klasöründen `dosyalar/*/dosya.md` dosyalarının üst bloklarını
(`---` arası) oku. Varsayılan görünüm `durum: acik` olanlardır; kullanıcı "kapalılar"
veya bir müvekkil adı verdiyse ona göre filtrele.

Hiç dosya yoksa kısa ve dostça: "Henüz kayıtlı dosyan yok. İlkini açalım mı? —
`/hukuk-asistani:yeni-dosya`" de ve dur.

### 2. Görünümü üret

İş-ürünü başlığı kuralı profilden uygulanır (bkz. eklenti CLAUDE.md `## Çıktılar`).
Format:

**Özet satırı (en üstte):**
`N açık dosya · önümüzdeki 30 günde M kritik tarih · K dosya 30+ gündür işlem görmedi`

**⚠️ Yaklaşan tarihler** — bugünden itibaren 30 gün içindeki tüm `sureler` kalemleri,
tarihe göre sıralı. Geçmiş ama kapanmamış tarihler listenin en üstünde ve `🔴 GEÇMİŞ`
etiketli — bunlar sessizce düşürülmez. Her satırda: tarih, kaç gün kaldığı, dosya adı,
ne olduğu. `[doğrula]` etiketi taşıyan süreler etiketiyle birlikte gösterilir.

**Dosya tablosu:**

| Dosya | Müvekkil | Merci / Esas | Aşama | Sonraki tarih | Son işlem |
|---|---|---|---|---|---|

Sıralama: sonraki tarihi en yakın olan üstte; tarihi olmayanlar sonda, son işleme göre.

**Hareketsiz dosyalar** — `son_islem` 30 günden eskiyse ayrı kısa liste: "şunlara
bakmayalı [N] gün oldu."

### 3. Dürüstlük kuralları

- Bu görünüm **yalnızca kayda geçirdiklerini** bilir. İlk kullanımların birinde (her
  seferinde değil) hatırlat: "Buradaki tarihler senin girdiklerin — UYAP'a bağlı
  değilim, kalemin verdiği yeni bir günü ben göremem."
- Tarih hesaplarını (kaç gün kaldı) bugünün tarihiyle yap; bugünün tarihini uydurma,
  ortamdan al.
- Frontmatter'ı bozuk/eksik bir dosya.md varsa sessizce atlama — "[dosya] kaydını
  okuyamadım, elle düzeltmek ister misin?" diye listenin altında belirt.

### 4. Kapanış

Tablo 10 satırı geçiyorsa dashboard öner (eklenti CLAUDE.md'deki standart öneri
formatıyla). Ardından kısa karar ağacı — en fazla üç seçenek, duruma göre; ör.:

> **Sırada ne var?**
> 1. **Bir dosyaya gir** — adını yaz, son durumunu özetleyeyim.
> 2. **Not düş** — duruşma/tebligat/gelişme varsa söyle, kaydedeyim.
> 3. **Geçmiş tarihi kapat** — 🔴 işaretli kalem yapıldıysa söyle, listeden düşeyim.
