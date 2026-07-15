---
name: yeni-dosya
description: Yeni bir dava veya iş dosyası açar — temel bilgileri sorar, dosya kaydını oluşturur, kritik tarihleri (duruşma, cevap süresi, zamanaşımı) not eder. Yeni müvekkil, yeni dava, yeni icra takibi veya takip edilecek herhangi bir yeni iş geldiğinde kullan.
argument-hint: "[dosya adı veya müvekkil]"
---

# /yeni-dosya

Amaç: bir dosyayı 2 dakikada kayda geçirmek. Uzun alım görüşmesi yok — iki bilgi
(müvekkil + konu) yeterlidir, gerisi sonradan `dosya-notu` ile tamamlanır.

## Adımlar

### 1. Profili oku

`~/.claude/plugins/config/claude-for-legal-turkish/hukuk-asistani/CLAUDE.md`
profilinden çalışma klasörünü al. Profil yoksa: "Önce 3 dakikalık kurulumu yapalım —
`/hukuk-asistani:ilk-kurulum`" de; kullanıcı yine de devam etmek isterse varsayılan
klasörü (`~/Documents/Hukuk-Asistani`) sorup onaylatarak kullan.

### 2. Bilgileri topla

Tek mesajda sor, cevabı bekle. **Yalnızca ilk iki madde zorunlu** — kullanıcı gerisini
bilmiyorsa/atlıyorsa boş bırak, dosya yine açılır:

> Yeni dosyayı açıyorum. Şunları yazar mısın (bilmediklerini atla):
> 1. **Müvekkil** (dosyayı kimin için tutuyorsun?)
> 2. **Konu** — bir iki cümle (ne davası/işi, ne oldu?)
> 3. Karşı taraf
> 4. Bizim konumumuz (davacı / davalı / alacaklı / borçlu / müşteki / sanık müdafii / danışmanlık…)
> 5. Mahkeme veya merci + esas/dosya numarası (varsa — UYAP'tan kopyalayıp yapıştırabilirsin)
> 6. Aşama (dava açılacak / dilekçeler / ön inceleme / tahkikat / karar / istinaf / icra…)
> 7. Kritik tarihler — duruşma günü, cevap/itiraz süresi, zamanaşımı endişesi

Kullanıcı komutu zaten bilgiyle çağırdıysa ("yeni işçilik davası, müvekkil Ahmet
Yılmaz, işveren X A.Ş.") verilenleri kullan, yalnızca eksik zorunluları sor.

### 3. Süre disiplini

Kullanıcı bir tebliğ tarihi verip süre hesaplamanı isterse (ör. "10 Temmuz'da tebliğ
edildi, cevap süresi ne zaman doluyor?"):

- Hesabı **göster** (başlangıç günü, süre, hafta sonu/resmî tatile denk gelme, adli
  tatil etkisi) ve sonucu `[doğrula — süre hesabı]` etiketiyle ver.
- Sürenin kaynağını söyle ve etiketle (ör. "HMK'daki iki haftalık cevap süresi
  `[model bilgisi — doğrula]`").
- Asla "son gün kesin X'tir" deme — süre kaçırmak telafisiz; hesap her zaman avukat
  teyidine işaretlenir.

### 4. Dosya kaydını yaz

Klasör adı (slug): müvekkil + kısa konu, küçük harf, tire ile, Türkçe karakterleri
sadeleştir (`ş→s ı→i ğ→g ç→c ö→o ü→u`) — ör. `yilmaz-iscilik-alacagi`. Aynı adda
klasör varsa sonuna sayı ekle.

`<çalışma klasörü>/dosyalar/<slug>/dosya.md` dosyasını şu yapıda yaz. Üstteki `---`
arası blok makine tarafından okunur (`dosyalarim` bunu tarar) — alan adlarını değiştirme:

```markdown
---
dosya: Yılmaz / X A.Ş. — işçilik alacağı
muvekkil: Ahmet Yılmaz
karsi_taraf: X A.Ş.
rol: davacı vekili
mahkeme: Ankara 5. İş Mahkemesi
esas_no: 2026/123
asama: dilekçeler
durum: acik
acilis: 2026-07-16
son_islem: 2026-07-16
sonraki_tarih: 2026-09-12
sureler:
  - tarih: 2026-09-12
    ne: Duruşma
  - tarih: 2026-07-24
    ne: "Cevaba cevap son günü [doğrula — süre hesabı]"
---

# Yılmaz / X A.Ş. — işçilik alacağı

## Özet
[Konunun 3-5 cümlelik özeti: ne oldu, ne talep ediliyor, şu an neredeyiz.]

## Taraflar ve konum
[Müvekkil, karşı taraf ve varsa vekilleri; bizim konumumuz.]

## Kritik tarihler
[Sürelerin listesi, her birinin kaynağı/dayanağıyla. Hesaplanan süreler etiketli.]

## Notlar
### 2026-07-16 — Dosya açıldı
[Açılıştaki bilgiler; kullanıcının anlattıklarından önemli ayrıntılar.]
```

Bilinmeyen alanları frontmatter'da boş bırakma — satırı hiç yazma (`esas_no` bilinmiyorsa
satır yok). `sonraki_tarih` = `sureler` içindeki en yakın gelecek tarih; süre yoksa satırı
yazma.

### 5. Onayla ve yol göster

Kullanıcıya sohbette kısaca göster: dosya adı, kayıt yeri (sade dille: "Belgelerinde
`dosyalar/yilmaz-iscilik-alacagi` klasörü"), yakalanan kritik tarihler. Sonra tek
satır yönlendirme: "Gelişme olduğunda 'dosyaya not düş: …' yazman yeterli; tüm
dosyaların görünümü için `/hukuk-asistani:dosyalarim`."

## Kurallar

- Kullanıcının söylediği hukuki olguları (süre, kanun, esas no formatı) kayda geçirmeden
  önce bildiklerinle karşılaştır; çelişkiyi yüzeye çıkar (guardrail: öncül doğrulama).
- Aynı müvekkil/konu için açık bir dosya zaten varsa açmadan önce söyle: "Buna benzeyen
  açık bir dosyan var: [dosya]. Yeni bir dosya mı, ona not mu?"
- Bu bir kayıt aracıdır, hukuki değerlendirme yeri değil — kullanıcı açılışta hukuki
  soru sorarsa cevapla (iskele, gözbağı değil) ama dosya kaydını şişirme; değerlendirme
  Notlar bölümüne tarihli not olarak girer.
