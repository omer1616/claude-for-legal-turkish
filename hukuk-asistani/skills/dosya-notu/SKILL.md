---
name: dosya-notu
description: Bir dosyaya tarihli gelişme notu ekler — duruşma sonucu, gelen tebligat, müvekkil görüşmesi, yeni süre — ve dosyanın aşama/tarih bilgilerini günceller. Dosya kapatma da buradan yapılır. Bir dosyada herhangi bir gelişme olduğunda kullan.
argument-hint: "[dosya] [gelişme]"
---

# /dosya-notu

Amaç: "bugün duruşma vardı, şöyle oldu" cümlesini 30 saniyede kalıcı kayda çevirmek.

## Adımlar

### 1. Dosyayı bul

Kullanıcının verdiği ada/müvekkile göre `dosyalar/` altında eşleştir (klasör adı,
`dosya:` veya `muvekkil:` alanı). Tek eşleşme → devam. Birden çok → kısa liste göster,
seçtir. Hiç yok → "Bu adla kayıtlı dosya bulamadım; yeni dosya mı açalım
(`/hukuk-asistani:yeni-dosya`)?"

### 2. Notu ekle

`dosya.md`'nin `## Notlar` bölümünün **sonuna** ekle:

```markdown
### 2026-07-16 — Duruşma yapıldı
[Kullanıcının anlattığı gelişme — kendi sözlerine sadık, toparlanmış halde.]
```

**Ekleme-esaslı (append-only):** eski notlar asla silinmez, değiştirilmez,
yeniden yazılmaz. Düzeltme gerekiyorsa yeni bir düzeltme notu eklenir.

### 3. Üst bilgiyi güncelle

Notun içeriğine göre `---` arası bloğu güncelle ve **ne değiştirdiğini kullanıcıya tek
satırda söyle**:

- `son_islem` → bugün (her notta).
- Yeni tarih/süre anlatıldıysa (`"yeni duruşma 12 Eylül"`, `"iki haftalık itiraz süresi
  başladı"`) → `sureler` listesine ekle. Süreyi tebliğden kendin hesapladıysan
  `[doğrula — süre hesabı]` etiketiyle ve hesabı göstererek (yeni-dosya'daki süre
  disiplini burada da geçerli).
- Geçmiş bir süre kalemi "yapıldı" ise → `sureler`den çıkar, nota işle.
- `sonraki_tarih` → kalan sürelerin en yakını.
- Aşama değiştiyse (`"karar çıktı"`, `"istinafa taşıdık"`) → `asama` güncelle.

### 4. Kapatma

Kullanıcı dosyanın bittiğini söylüyorsa ("dava sonuçlandı", "dosyayı kapat"):

1. Sonucu sor (tek soru): "Nasıl sonuçlandı? — kabul / red / kısmen kabul / sulh /
   takipsizlik / feragat / başka bir şey + bir cümle."
2. `durum: kapali` yap, `kapanis: [tarih]` ekle, kapanış notunu `## Notlar`a yaz.
3. Bekleyen `sureler` varsa uyar: "Dosyada hâlâ kayıtlı [N] tarih var ([liste]) —
   kapanışla birlikte düşeyim mi? (İstinaf/temyiz süresi gibi kapanış sonrası süreler
   varsa dosyayı kapatmak yerine aşamayı güncellemek daha güvenli olabilir `[incele]`)"
4. Dosya silinmez — klasör yerinde kalır, sadece listeden düşer. Bunu kullanıcıya söyle.

### 5. Kapanış satırı

Kısa onay: ne kaydedildi, ne güncellendi, varsa en yakın yeni tarih. Uzun karar ağacı
gerekmez — bu hızlı bir kayıt işlemidir. Not hukuki bir soru içeriyorsa (ör. "hakim
şunu istedi, ne yapmalıyım?") kaydı yaptıktan sonra soruyu da cevapla (iskele, gözbağı
değil).
