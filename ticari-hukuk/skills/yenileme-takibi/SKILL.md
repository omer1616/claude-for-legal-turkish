---
name: yenileme-takibi
description: >
  Yaklaşan fesih-bildirim son tarihleri olan sözleşmeleri gösterin ve bildirim
  pencereleri kapanmadan önce uyarın, tutulan bir yenileme kaydından çalışarak.
  Kullanıcı "yakında ne yenileniyor", "hangi yenilemeler geliyor", "bir iptal
  penceresini kaçırdık mı", "bunu yenileme takipçisine ekle" dediğinde veya
  zamanlanmış bir şekilde kullanın. saas-inceleme'den devirleri alır.
argument-hint: "[pencereyi değiştirmek için --gun N | kaçırılan pencereler için --kacirilan]"
---

# /yenileme-takibi

Ne yenileneceğini ve ne zaman iptal etmeniz gerektiğini yüzeye çıkarır.

## Talimatlar

1. **`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/yenileme-kaydi.yaml`
   dosyasını oku** (yapılandırma dizini — eklenti güncellemelerini atlatır).

2. **Varsayılan mod:** Mod 2 — önümüzdeki 90 günde ne geldiği, her son tarihin tam
   olarak bir bantta yer alması için yarı-açık aralıklar kullanarak aciliyete göre
   gruplanmış: 🔴 0-13 gün, 🟠 14-44 gün, 🟡 45-89 gün. 14, 45 ve 90. günler
   sınırlardır — her biri iki değil tam olarak bir bant'a aittir.

3. **`--gun N`:** Pencereyi değiştir.

4. **`--kacirilan`:** Mod 4 — kaydedilmiş bir iptal olmadan geçen fesih-bildirim son
   tarihleri.

5. **Kayıt boşsa ve CLM bağlıysa:** Mod 3'ü öner — CLM'yi yenileme tarihleri olan
   aktif sözleşmeler için tara ve toplu yükle.

6. **Çıktı önerilen eylemleri içerir:** kime dokunulacağı (kayıttaki her girişten iş
   birimi sahibi), hangilerinin tavansız fiyatlandırması olduğu (pencere
   kapanmadan önce kaldıraç kazanın).

## Örnekler

```
/ticari-hukuk:yenileme-takibi
```

```
/ticari-hukuk:yenileme-takibi --gun 180
```

```
/ticari-hukuk:yenileme-takibi --kacirilan
```

---

## Amaç

Kimse bir sözleşmeyi iki kez okumaz. Yenileme tarihi bir kez, inceleme anında
çıkarılır ve sonra bir yerde yaşar — ideal olarak iptal son tarihinden 45 gün sonra
değil, 45 gün önce size bağıran bir yerde.

Bu skill yenileme kaydını tutar ve neyin geldiğini yüzeye çıkarır.

## Kayıt

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/yenileme-kaydi.yaml`
adresinde yaşar (yapılandırma dizini — eklenti güncellemelerini atlatır). Her kayıt:

```yaml
- karsi_taraf: "Acme SaaS A.Ş."
  sozlesme: "Acme Platform Abonelik Sözleşmesi"
  imza_tarihi: 2025-06-15
  ilk_sure_bitisi: 2026-06-15
  guncel_sure_bitisi: 2026-06-15     # her otomatik yenilemeden sonra ileri sarar; iptal_son_* buradan hesaplanır
  yenileme_mekanizmasi: "otomatik-yenileme yıllık"
  bildirim_suresi_gun: 60
  bildirim_yontemi: "e-posta"        # e-posta / portal / iadeli taahhütlü / KEP / sözleşme §X'e göre
  iletim_tamponu_gun: 0              # elektronik için 0, yurt içi iadeli taahhütlü için 5, uluslararası kayıtlı posta için 10 — veya sözleşmede belirtilmişse ona göre
  iptal_son_takvim: 2026-04-16       # guncel_sure_bitisi eksi bildirim_suresi_gun
  iptal_son_gecerli: 2026-04-16      # gerekirse son iş gününe geri yuvarlanmış
  gonderim_son_gecerli: 2026-04-16   # iptal_son_gecerli eksi iletim_tamponu_gun — bildirimi GÖNDERMENİZ gereken tarih
  iptal_son_yuvarlama_notu: ""       # ör. "2026-11-01 Pazar gününden geri yuvarlandı; sözleşmenin iş günü tanımına karşı doğrula"
  iptal_son_kaynagi: "[model hesaplaması — bildirim maddesine karşı doğrula]"
  yenilemede_fiyat: "o anki liste fiyatı (tavansız)"
  yillik_tutar: 48000
  is_birimi_sahibi: "jane@sirket.com"
  clm_id:        "IC-12345"         # bağlıysa
  docusign_zarfi: "abc-123"         # bağlıysa
  durum: "aktif"                    # aktif | iptal_edildi | yenilendi | suresi_gecti
  notlar: "Fiyat tavansız — yenileme öncesi tekrar gözden geçir. Alternatif satıcılar: X, Y."
```

**Bildirim iletim süresi — `gonderim_son_gecerli`'den uyarın, `iptal_son_gecerli`'den
değil.** İadeli taahhütlü mektup gereksinimi olan 60 günlük bir pencere gerçekte
~55 gündür. Alınacak-tarih üzerinden uyaran takipçi, son tarihi kaçıran takipçidir.
`gonderim_son_gecerli = iptal_son_gecerli - iletim_tamponu_gun` hesaplayın ve
uyarıları (Mod 2'deki 🔴 / 🟠 / 🟡 aciliyet bantları) `gonderim_son_gecerli`'den
tetikleyin. Mod 2'nin aciliyet sütunu `gonderim_son_gecerli`'yi gösterir; bir detay
sütunu `iptal_son_gecerli`, `bildirim_yontemi` ve `iletim_tamponu_gun`'u yüzeye
çıkarır, böylece okuyan farkı görebilir ve tamponu sorgulayabilir.

**Kayan yenilemeler — ileri sarmayan kayıt yalnızca bir kez doğru olan kayıttır.**
Kayıt için `ilk_sure_bitisi`'ni saklayın, ama `iptal_son_*`'ı
`guncel_sure_bitisi`'nden hesaplayın. Bir yenileme tetiklendiğinde (iptal penceresi
geçti ve bildirim verilmedi), sorun:

> Bu sözleşme [tarih]'te otomatik yenilendi. Kaydı güncelleyin: yeni
> `guncel_sure_bitisi` [tarih + yenileme süresi], yeni `iptal_son_gecerli`
> [hesaplanmış], yeni `gonderim_son_gecerli` [hesaplanmış]. Onaylıyor musunuz?

Birinci yıldan sonra, `ilk_sure_bitisi` yanlıştır ve yalnızca `guncel_sure_bitisi`
doğru bir iptal-son-tarihi üretir.

## Her iptal-son-tarihinde iş günü kontrolü

**Kaydın iptal-son tarihi, bildirimin geçerli olduğu son İŞ GÜNÜ olmalıdır, takvim
tarihi değil.** Hafta sonuna denk gelen bir takvim tarihi, bir yenileme son
tarihinin kaçırılmasının en yaygın tek yoludur. Kayıt bunu yakalar.

Bir iptal-son tarihini hesapladığınızda (veya aldığınızda):

1. **Takvim tarihini hesaplayın.** `iptal_son_takvim = ilk_sure_bitisi − bildirim_suresi_gun`
   (veya madde ne belirtiyorsa). Bu ham aritmetiktir.
2. **Uygulanacak hukuka bağlı iş günü geri yuvarlaması.** Sözleşmenin uygulanacak
   hukuku hangi tatillerin sayıldığını belirler. Türkiye: resmi tatiller (dini ve
   milli bayramlar). Yabancı uygulanacak hukuk seçilmişse, o yargı çevresinin tatil
   takvimini kullanın. Cumartesiyse Cuma'ya geri yuvarlayın. Pazarsa Cuma'ya geri
   yuvarlayın. Uygulanacak-hukuk yargı çevresinde bir tatilse, önceki iş gününe geri
   yuvarlayın. Her zaman GERİYE yuvarlayın, asla ileriye — ileri yuvarlama bildirimin
   pencere kapandıktan sonra ulaşması demektir. Tatil takvimini belirleyemiyorsanız,
   işaretleyin: "Uygulanacak hukuk [X] — iş günü geri yuvarlaması bir yer tutucu
   olarak TR resmi tatillerini kullanıyor. Etkin tarihe güvenmeden önce [yargı
   çevresi] tatil takvimine karşı doğrulayın."
3. **Sözleşmenin kendi gün-sayma kuralını kontrol edin.** "İş günü," "alındığında,"
   "alınmış sayılır," "[yerel saat] 17:00" veya bir bildirim-yöntemi maddesi (iadeli
   taahhütlü, okundu bilgili e-posta) arayın. Sözleşme "iş günü"nü tanımlıyorsa veya
   alım mekaniğini belirtiyorsa, o tanım kontrol eder. Varsayılan geri yuvarlama ile
   sözleşmenin kendi kuralı arasındaki herhangi bir uyumsuzluğu işaretleyin.
4. **HER İKİ tarihi de kayda kaydedin.** `iptal_son_takvim` ham aritmetiktir;
   `iptal_son_gecerli` bildirimin geçerli olduğu son iş günüdür;
   `iptal_son_yuvarlama_notu` neden farklı olduklarını kaydeder (ör. "2026-11-01
   Pazar gününden geri yuvarlandı; sözleşmenin iş günü tanımına karşı doğrula").
   Hesaplanan her `iptal_son_gecerli`, doğrula bayrağının çevredeki metinle değil
   tarihle birlikte gezmesi için `[model hesaplaması — bildirim maddesine karşı
   doğrula]` `iptal_son_kaynagi` etiketi taşır.
5. **Uyarıları TAKVİM tarihinden değil ETKİN tarihten tetikleyin.** Aciliyet
   bantları (Mod 2'de 🔴 / 🟠 / 🟡) `iptal_son_gecerli`'yi kullanır. Mod 2 çıktısı
   aciliyet sütununda `iptal_son_gecerli`'yi gösterir ve geri yuvarlamanın olduğu
   yerde bir detay sütununda `iptal_son_takvim` ve `iptal_son_yuvarlama_notu`'nu
   yüzeye çıkarır, böylece okuyan bunu görebilir ve sorgulayabilir.

`iptal_son: 2026-11-01` (bir Pazar) yazdıran, hafta günü ve uyarı olmadan bir Mod 2
raporu, sessizce yanlış bir etkin son tarihtir. Kayıt bunu yakalayacağı yerdir —
bir kez, alım anında — daha sonra pencere zaten hareket ettiğinde değil.

## Modlar

### Mod 1: Bir yenilemeyi al (incelemeden devir)

saas-inceleme veya satici-inceleme bir yenileme maddesi bulduğunda, bir kayıt devreder.
Kayda ekleyin. Karşı tarafın zaten bir girişi varsa, bunun bir yer değiştirme (yenilenen
sözleşme) mi yoksa ek bir sözleşme mi olduğunu sorun.

### Mod 2: Ne geliyor

**Varsayılan geriye bakış penceresi:** önümüzdeki 90 gün.

**Aciliyet bantları yarı-açık aralıklardır — bir son tarih tam olarak bir bant'a
aittir.** Iptal-son-tarihe-kadar-gün-sayısını kullanın (`iptal_son_gecerli - bugün`).
14, 45 ve 90. günlerin her biri iki değil tam olarak bir bant'a aittir; buradaki bir
kayma en acil kalemleri daha az acil kovaya koyar.

- 🔴 **0-13 gün** (14 günden az iptal-son — bugün dahil)
- 🟠 **14-44 gün**
- 🟡 **45-89 gün**
- (90+ gün olan her şey varsayılan geriye bakış penceresinin dışındadır; yalnızca
  kullanıcı 90'ın ötesinde bir `--ufuk` geçtiyse dahil edin)

```markdown
## Yenilemeler — önümüzdeki 90 gün

### 🔴 İptal-son 0-13 gün içinde

| Karşı taraf | İptal-son | Yenileme tarihi | Yıllık TL | Sahip | Notlar |
|---|---|---|---|---|---|
| [isim] | **[tarih]** | [tarih] | [n] TL | [e-posta] | [notlar] |

### 🟠 İptal-son 14-44 gün içinde

[aynı tablo]

### 🟡 İptal-son 45-89 gün içinde

[aynı tablo]

---

**Önerilen eylemler:**
- [ ] [Karşı taraf] — [iş birimi sahibi]'ne dokunun: bunu tutmak istiyor muyuz?
- [ ] [Karşı taraf] — fiyatlandırma tavansız; kaldıracı kaybetmeden önce alternatif
  bir teklif alın
```

Kayıtta penceredeki yenilemeler ~10'dan fazlaysa, veya kullanıcı her istediğinde:
dashboard'u önerin (bkz. CLAUDE.md `## Çıktılar → Veri-yoğun çıktılar için dashboard
önerisi`). Öneriyi bu çıktı için şekillendirin — aciliyet katmanına göre sayımlar
(🔴 / 🟠 / 🟡), bir iptal-son zaman çizelgesi ve karşı taraf, yenileme tarihi, yıllık
TL ve sahiple sıralanabilir bir kayıt.

### Mod 3: CLM / e-imza aracını kaydı doldurmak için tara

MCP'ler bağlıysa ve kayıt boş veya eskiyse:

1. CLM'yi "Aktif" durumu ve bir yenileme tarihi alanı olan tüm sözleşmeler için
   sorgula
2. DocuSign'ı son 24 ayda meta verisinde "abonelik" / "yenileme" / "otomatik-yenileme"
   olan tamamlanmış zarflar için sorgula
3. Her isabet için yenileme mekaniğini çıkar ve kayda ekle
4. Yenileme tarihi meta veriden belirlenemeyen herhangi birini işaretle — bunlar
   sözleşmeyi okuyacak bir insana ihtiyaç duyar

Bu tek seferlik bir toplu yüklemedir. Ondan sonra, alım inceleme anında olur.

### Mod 4: Kaçırılan pencereler (kötü haber raporu)

```markdown
## Kaçırılan iptal pencereleri

Aşağıdaki sözleşmelerin geçmiş iptal-son son tarihleri vardı ve kaydedilmiş bir
iptal yoktu:

| Karşı taraf | İptal-son şuydu | Yenileme tarihi | Durum |
|---|---|---|---|
| [isim] | [tarih] | [tarih] | [tarih]'te otomatik yenilenecek |

**Seçenekler:**
- Geç iptali müzakere edin (nadiren işe yarar ama sormaya değer)
- Yenilemeyi kabul edin, gelecek yılın iptal-son'unu şimdi işaretleyin
- Sözleşmede başka herhangi bir fesih hakkı olup olmadığını kontrol edin (serbestçe,
  haklı sebeple)
```

## Kapı: bir yenilemeyi kabul etmek veya reddetmek

Bir yenileme tarihini takip etmek araştırmadır. Ona göre *hareket etmek* — bir
yenilememe bildirimi göndermek, bir otomatik yenilemenin tetiklenmesine izin vermek
veya bir yenileme formunu karşı-imzalamak — sonuç doğuran bir hukuki adımdır.

**Bir yenilemeyi kabul etmeye veya reddetmeye geçmeden önce (bir yenilememe bildirimi
göndermek veya bir otomatik yenilemenin iptal-son tarihinin ötesinde çalışmasına izin
vermek dahil):**
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
içindeki `## Bunu kim kullanıyor`'u oku. Rol Avukat değilse:

> Bu adımın hukuki sonuçları var (ya başka bir süreye taahhüt ediyorsunuz ya da
> ilişkiyi sonlandırıyorsunuz). Bunu bir avukatla gözden geçirdiniz mi? Evetse,
> devam edin. Hayırsa, onlara getirmeniz için bir brifing:
>
> [1 sayfalık özet üret: karşı taraf, mevcut süre sonu ve iptal-son tarihi, yenileme
> fiyat mekanizması, hiçbir şey yapmazsak ne olacağı, alışveriş yapmak isterseniz
> alternatif satıcılar, ve pencere kapanmadan önce avukata sorulacak üç şey.]
>
> Bir avukat bulmanız gerekirse: bağlı olduğunuz baroya başvurun.
> `[doğrulanacak — TR baro yönlendirme mekanizmaları]`

Açık bir evet olmadan bu kapıdan geçme.

## Entegrasyon: yenileme-ajani agent'ı

Bu eklentideki yenileme-ajani agent'ı bu skill'i bir zamanlamayla (varsayılan
haftalık) çalıştırır ve "geliyor" raporunu
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` →
`## Ev tarzı` → iş ürününün nereye gittiği bölümünde adlandırılan kanala gönderir.
Mod 2, agent'ın birincil çıktısıdır.

## Bu skill'in yapmadıkları

- Sözleşmeleri iptal etmez. Ne zaman karar vereceğinizi söyler.
- Yenilenip yenilenmeyeceğine karar vermez. Son tarihi ve iş birimi sahibini yüzeye
  çıkarır.
- Yenileme tarihlerini bulmak için sözleşme okumaz — bu inceleme anında olur. Bir
  sözleşme kayıtta yenileme tarihi olmadan varsa, elle eklenmiştir ve birinin
  boşluğu doldurması gerekir.
