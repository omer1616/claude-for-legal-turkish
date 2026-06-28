---
name: talep-alimi
description: İhtarname öncesi bağlam toplama — taraflar, olgular, dayanak, kaldıraç, BATNA ve gizlilik filtreleri — ihtarname taslağının okuyacağı yapılandırılmış bir intake.md'ye yazılır. Kullanıcı ihtarname hazırlamak, taslaklamadan önce intake çalıştırmak veya ödeme talebi, ihtar/ifaya davet, men talebi, iş akdi feshi ya da delil saklama talebi için bağlam yakalamak istediğinde kullan.
argument-hint: "[başlık] [--tam]"
---

# /talep-alimi

1. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` yükle → ihtarname pratiği, manzara, risk kalibrasyonu.
2. Aşağıdaki iş akışını ve referansı uygula.
3. Uyarlanabilir intakei çalıştır (çekirdek 8 her zaman; önemli veya `--tam` ise stratejik blok).
4. Başlık + karşı taraf + yıl-ay'dan slug üret.
5. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/ihtarname/[slug]/intake.md` yaz.
6. Kullanıcıyla teyitle: "Intake kaydedildi. Hazır olduğunuzda `/dava-takibi:ihtarname-taslagi [slug]` çalıştırın."

---

# Talep Alımı (İhtarname Intake)

## Amaç

Taslak yazım aşağı akıştır. Değer ön-yazımdadır — dikkatsiz bir mektubun atladığı soruları zorlar. Kaldıraç, BATNA, olumsuz taraf toleransı, gizlilik filtreleri, gerçek hedef kitle. Bu şeyleri düşünmeden gönderilen ihtarname göndermemekten kötüdür.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` → İhtarname pratiği (sigorta ihbar zamanlaması, dosya oluşturma için önemlilik eşiği, tohum belge şablonları), manzara (karşı taraf türü, tekrarlayan hasım kalıpları), risk kalibrasyonu (önemlilik ön tahmini için), ev tarzı. **Ton, süre, işaretleme, imzalayan pratik düzey varsayılanlar DEĞİLDİR — aşağıdaki `## Bu Dava İçin Duruş` adımında mater başına ayarlanır.**

## Bayraklar

- `--tam` → önemlilik sezgisel kurallarına bakılmaksızın tam intakei çalıştır (her seferinde kapsamlı isteyen avukat için)

## İntake

### Bu Dava İçin Duruş (Çekirdekten ÖNCE sor)

> **Bu dava için duruş.** İhtarname tonu ve koşulları, pratik varsayılanı değil, davaya özeldir. Sor:
> - **Ton:** ölçülü / iddialı / agresif? (ilişkiye, tutara ve davanın olası olup olmadığına bağlı)
> - **Yanıt süresi:** talebi göz önünde bulundurarak makul nedir? (Ödeme talepleri için 7-14 gün yaygın; ifaya davet için 30 gün; men talebi için 7 gün — ama sözleşme veya protokol ayarlamış olabilir)
> - **İşaretleme:** buna "ihtirazi kayıt", "haklarımız saklı kalmak kaydıyla" veya "haksız rekabet sayılmaksızın" işareti gerekiyor mu? (sulh amaçlı yazışmalar; hak iddiası beyanları genellikle gerekmez; yargı çevresi önemlidir — emin değilseniz sorun)
> - **İmzalayan:** siz, müvekkil, BHM, büroya talimat veren avukat?
> Varsayma. Varsa dosya dosyasındaki önceki ihtarname yazışmalarını okuyun — kayıt tarzını ortaya koyar.

Cevapları `## Taraflar`'dan önce `## Duruş` bölümü altında intakee kaydet. Bu cevaplar intakenin geri kalanını ve aşağı akış taslağını yönetir — kullanıcı herhangi birini boş bırakırsa pratik düzey varsayılana dönme; tekrar sor.

### Çekirdek — Her Zaman Sorulur (8 Soru)

**1. Talep Türü**
`odeme | ihlal-ifaya-davet | men-talebi | is-akdi-feshi | delil-saklama | diger`

**2. Taraflar**
- **Gönderen:** bizim şirketimiz (çok tüzel kişilik yapısında varsa belirli tüzel kişi)
- **Alıcı:** karşı taraf — ad, tüzel kişi, adres
- **Alıcı hedef kitle:** gerçekte kim okuyor (BHM? CEO? birey? şirket-içi hukuk?)
- **İlişki:** `musteri | tedarikci | eski-calisan | rakip | ucuncu-taraf | diger`

**3. Tetikleyici Olay**
- Ne oldu ve ne zaman (tarihler önemli — zamanaşımı, ihbar süreleri)
- Mevcut delil (sözleşmeler, e-postalar, kayıtlar, tanıklar)

*Tohum belge fırsatı: "Temel sözleşmeyi, yazışmayı veya delili paylaşabilirseniz, taslak önemli ölçüde daha keskin olur. Yollar çalışır."*

**4. Hukuki / Sözleşmesel Dayanak**
- Hangi maddeler — uygulanabiliyorsa belirli sözleşme bölümleri
- Uygulanacak hukuk (yargı çevresi, hukuk seçimi maddesi)
- Dayandığı kanunlar veya yönetmelikler (yer tutucular tamam — taslak zaten `[ATIF:___]` ile işaretleyecek)

**5. İstenilen Sonuç**
- Spesifik talepler. "Çözüm" değil — Y tarihine kadar X TL ödeme; belirli Z faaliyetinin durdurulması; N gün içinde ifaya davet; belirli mülkün iadesi.
- Birden fazla talep varsa sıralayın (birincil vs. yedek)

**6. Son Tarihler**
- Bunu yönlendiren dış son tarih (zamanaşımı, devam eden zarar penceresi, ticari olay)
- Talep uyum son tarihi — alıcıya ne kadar süre veriyoruz. Yukarıdaki `## Bu Dava İçin Duruş`'ta yakalanan yanıt süresini kullan; pratik düzey varsayılana dönme.

**7. Önceki Ulaşım**
- Bu konu gayri resmi olarak gündeme getirildi mi? Ne zaman, kim tarafından, nasıl?
- Şimdiye kadar herhangi bir yanıt?
- Neden şimdi ihtarnameye tırmanma oluyor?

**8. Dağıtım**
- Teslim yöntemi (sor; pratik düzey varsayılan yok — KEP, iadeli taahhütlü, noter, e-posta)
- İmzalayan — yukarıdaki `## Bu Dava İçin Duruş`'ta yakalandı
- Kopyalar — iç paydaşlar, sigorta şirketi (varsa önceden ihbar için), avukat

### Stratejik — Önemliyse veya `--tam` ise Sorulur

Önemlilik sezgisel kuralı: aşağıdakilerden herhangi biri doğruysa stratejik bloğu sor.

- Talep türü `men-talebi`, `ihlal-ifaya-davet`, `is-akdi-feshi` veya `delil-saklama`
- İstenilen sonucun para değeri ≥ `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` risk kalibrasyonundaki orta şiddet bandı
- Karşı taraf, `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` manzarasına göre müşteri, rakip veya sık hasım
- Kullanıcı `--tam` ile çalıştırdı

**Açık atlama seçeneği.** Stratejik blok tetiklendiğinde, kullanıcı cevaplamayı reddedebilir. Açıkça sor:

> Bu sezgisel kurala göre önemli bir talep. Stratejik blok (kaldıraç, BATNA, ton, gizlilik filtreleri) ön-yazım değerinin çoğunun yaşadığı yerdir. Atlamak daha zayıf bir taslak üretir.
> - **Şimdi cevapla** — stratejik bloğu yürü (5-7 dk)
> - **Kısmi cevapla** — hazır hissettiğiniz alt kümeyi yürü
> - **Atla** — yalnızca çekirdek blokla taslağa geç; intake dosyasında `stratejik_blok: atlandi` olarak işaretlerim

Kullanıcı Atla seçerse, intake dosyası bunu kaydeder:

```yaml
stratejik_blok: cevaplandi | kismi | atlandi
atlama_nedeni: metin | null
```

**9. Kaldıraç ve BATNA**
- Bize müzakere gücü veren şey (sözleşme hakları, olgusal kaldıraç, itibar, ticari)
- Reddederlerse — dava açmaya hazır mıyız? Kamuoyuna mı gidelim? Daha küçük bir sonucu kabul edelim mi?
- Onların muhtemel BATNA'sı — en iyi alternatifleri ne? (Bizi dava açmayacağımızı düşünürlerse, ihtarname zayıftır.)

**10. Olumsuz Taraf Toleransı**
- Bu kamuya açılırsa itibar maruziyeti
- Emsal riski — bu mektup diğer davaları etkileyen bir kalıp oluşturuyor mu?
- Düzenleyici / açıklama sonuçları (bu, SPK/KAP beyanında yer alan türde bir uyuşmazlık mı?)
- Sigorta sonuçları — ihbar etmeden göndermek teminatı ortadan kaldırıyor mu?

**11. Ton Duruşu**
- Yukarıdaki `## Bu Dava İçin Duruş`'ta zaten yakalandı. Burada, kullanıcı olgulardan daha güçlü veya daha zayıf bir ton seçtiyse ödünleşimi araştır.
- Açıkça söylemeye değer: agresif ton ilişkiyi yakar. Ticari ilişkiyi korumak ama hukuki konumu korumak istiyorsanız, `ölçülü` genellikle doğru tercih.

**12. Sulh İletişim Duruşu**
- Forumda geçerli sulh iletişim korumalarını araştır (HMK m.313 vd., CMK karşılıkları). Bu mektup korunan bir sulh iletişimi mi? Yoksa korunmaması gereken bir hak iddiası mı?
- Korunmuşsa: taslak sulh iletişimi işaretini içerecek ve madde (bir uzlaşma tartışması) değil yalnızca etiket bu duruşu destekleyecek şekilde yapılandırılacak.
- Koruma davranış ve bağlamdan yapışır, yalnızca etiketlemeden değil. İşaret bir kemer-askı tercihidir. `[doğrulanacak]`

**13. Gizlilik Filtreleri**
- İç analizimizde mektuba çıkmaması gereken şey? (Doğrulamadığımız olgular, davamız hakkındaki şüphelerimiz, stratejik muhakeme, önceki sulh tartışmaları)
- Tek kötü ifade edilmiş cümle ilgili analiz üzerinde gizliliği ortadan kaldırabilir. Dışarıda ne kalacağı konusunda açık olun.

**14. İkrar ve İbra Riski**
- Mektuptaki karşı tarafın daha sonra olgu veya sorumluluğun ikrarı olarak nitelendirebileceği her şey?
- Bu talep, ayrı bir talepten yanlışlıkla ibra sağlıyor (veya kabul ediyor gibi görünüyor) mu? (İbra riski: "tam ödeme" yazılı çek nakde çevirmek tartışmalı borcu sona erdirebilir.)

## İntake Yazımı

### Slug

`[tur]-[karsi-taraf-kisa]-[yyyy-aa]`. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/ihtarname/`'de benzersizliği teyit et.

### `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/ihtarname/[slug]/intake.md`

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar — role göre farklılaşır; bkz. `## Bunu Kim Kullanıyor`]

# Talep Alımı: [başlık]

**Slug:** [slug]
**Talep türü:** [tür]
**Hazırlayan:** [avukat]
**Açılış:** [YYYY-AA-GG]
**Durum:** intake | taslaga-hazir | taslaklandi | gonderildi | kapandi
**Stratejik blok:** cevaplandi | kismi | atlandi
**Atlama nedeni:** [uygulanabiliyorsa]

---

## Duruş

- **Ton:** [ölçülü / iddialı / agresif — ilişki ve tutara bağlı tek satır gerekçeyle]
- **Yanıt süresi:** [N gün — talebe / sözleşmeye / protokole bağlı]
- **İşaretleme:** [yok / ihtirazi kayıt / haklarımız saklı / diğer — gerekçeyle]
- **İmzalayan:** [ad / rol — siz / müvekkil / BHM / talimat veren avukat]

*Bu, intake'te yakalanan davaya özgü duruştur. Taslak skill buradan okur.*

---

## Taraflar

- **Gönderen:** [bizim tüzel kişimiz]
- **Alıcı:** [karşı taraf, tüzel kişi, adres]
- **Alıcı hedef kitle:** [kim okuyor]
- **İlişki:** [tür]

## Tetikleyici Olay

[Ne oldu, ne zaman, delil]

## Hukuki / Sözleşmesel Dayanak

[Maddeler, uygulanacak hukuk, kanunlar]

## İstenilen Sonuç

[Öncelik sırasında spesifik talepler]

## Son Tarihler

- **Dış:** [zamanaşımı, devam eden zarar penceresi]
- **Uyum:** [onlara ne kadar süre veriyoruz]

## Önceki Ulaşım

[Geçmiş, en yenisi önce]

## Dağıtım

- **Teslim:** [yöntem]
- **İmzalayan:** [ad/rol]
- **Kopyalar:** [liste]

---

## Stratejik (Uygulanabiliyorsa)

### Kaldıraç & BATNA

[Gücümüz, onların muhtemel yanıtı]

### Olumsuz Taraf Toleransı

[İtibar, emsal, düzenleyici, sigorta]

### Ton Duruşu

[ilişkiyi-koruyucu / ölçülü / agresif — gerekçeyle]

### Sulh İletişim Duruşu

[Forumda korumalı mı değil mi — muhakemeyle. `[doğrulanacak — uygulanacak HMK/CMK kuralı]`]

### Gizlilik Filtreleri

[Taslakta ÇIKMAMASI gereken şey]

### İkrar / İbra Riski

[İşaretlenen spesifik riskler]

---

## Tohum Belgeler

| Belge | Yol |
|---|---|
| [temel sözleşme] | [yol veya "paylaşılmadı"] |
| [önceki yazışma] | [yol veya "paylaşılmadı"] |
| [delil] | [yol veya "paylaşılmadı"] |

---

## Önemlilik Değerlendirmesi

**Otomatik sezgisel kural diyor:** [önemli / önemsiz — gerekçeyle]
**Kullanıcı kararı:** [önemli / önemsiz / gönderi sonrası belirlenecek]
```

## Yazmadan Önce Teyit Et

Kullanıcıya taslak intakei göster. İnce noktaları işaretle:

> İşte intake. [İnce nokta]'yı fark ettim. Kaydetmeden önce eklenecek bir şey var mı?

## Taslama'ya El Teslimi

Şununla bitir:
> Intake kaydedildi. Hazır olduğunuzda: `/dava-takibi:ihtarname-taslagi [slug]`

## Sonraki Adımlar Karar Ağacıyla Kapat

CLAUDE.md `## Çıktılar` bölümüne göre sonraki adımlar karar ağacıyla kapat. Bu skill'in ürettiğine seçenekleri uyarla — beş varsayılan dal başlangıç noktasıdır, zorunluluk değil.

## Bu Skill'in Yapmadıkları

- Mektubu taslaklamak. Bu `ihtarname-taslagi` — iki adım kasıtlı olarak ayrılmıştır; böylece avukat taslak yapmadan önce iş girdisi, dış avukat danışması veya sigorta ihbarı için duraksayabilir.
- Mektubu göndermek isteyip istemediğine karar vermek. Bazı intake oturumları "aslında gönderme — doğrudan müzakere edelim" ile sona erer. Bu geçerli bir sonuçtur; intake kaydı yine de değerlidir.
- Çatışma taraması çalıştırmak. Karşı taraf bir müşteri veya bilinen varlıksa, göndermeden önce çatışmaların temizlenmesi gerektiğini işaretle (bkz. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`) — ama taramanın kendisi dosya-acilis iş akışında veya bu skill'in dışında yaşar.