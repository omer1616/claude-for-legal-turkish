---
name: onemli-sozlesme-takvimi
description: >
  Due diligence bulgularından yola çıkarak, satın alma sözleşmesinin (SPA) 
  "Önemli Sözleşme" (Material Contract) tanımını uygulayıp, sözleşmenin 
  ek/liste formatına göre "önemli sözleşmeler açıklama listesini" (disclosure schedule) 
  oluşturur. Kullanıcı "sözleşme takvimini kur", "açıklama listesi", "ek 3.X", 
  "önemli sözleşmeler listesi" dediğinde veya açıklama listelerini taslaklarken kullanın.
argument-hint: "[satın alma sözleşmesi yolu, veya Önemli Sözleşme tanımını yapıştırın]"
---

# /onemli-sozlesme-takvimi

1. Satın alma sözleşmesini yükle → Önemli Sözleşme tanımı + liste formatı.
2. Aşağıdaki iş akışını kullan.
3. Tanımı due diligence bulgularına uygula. Sınırda (edge case) kalan durumları işaretle.
4. Sözleşmeye göre formatla. İzin/onay (consent) takibi kapanış kontrol listesini (kapani-kontrol-listesi) besler.

---

## Dosya (Matter) Bağlamı

`CLAUDE.md` içindeki `## Dosya çalışma alanları`nı kontrol et. Eğer `Etkin` değilse (şirket-içi kullanıcılar için varsayılan), bu paragrafı atla. Eğer etkinse ve aktif dosya yoksa sor: "Bu hangi dosya (matter) için? `/sirketler-hukuku:dosya-calisma-alani degistir <slug>` çalıştır." Dosyaya özel bağlam için `matter.md` dosyasını yükle. Çıktıları `matters/<dosya-slug>/` klasörüne yaz.

---

## Amaç

Satın alma sözleşmesinde (SPA) şöyle bir tekeffül/beyan bulunur: "Ek 3.X (Açıklama Listesi) tüm Önemli Sözleşmeleri listeler." Bu yetenek (skill), bu listeyi due diligence bulgularından inşa eder — sözleşmenin tanımına göre hangi sözleşmelerin önemli olduğunu belirler ve sözleşmenin gerektirdiği formatta listeler.

## İçerik Yükle

- Satın alma sözleşmesi taslağı — "Önemli Sözleşme" tanımı ve liste formatı için.
- `CLAUDE.md` → önemlilik eşikleri (sözleşmenin tanımından farklı olabilir — daima sözleşmedekini kullanın).
- `due-diligence-sorun-cikartma`'dan gelen due diligence bulguları — sözleşme düzeyinde veriler.

## İş Akışı

### Adım 1: Tanımı al

Satın alma sözleşmesinden "Önemli Sözleşme" tanımını çek — SPA tanımı belirleyicidir. İşlem yapısındaki farklılıklar (hisse vs. varlık devri) veya düzenlenen sektörler (telekom, enerji, BDDK vb.) SPA dışındaki izin gerekliliklerini de ekleyebilir.

SPA tanımında aranacak yaygın kategori başlıkları (bunlar SPA'yı okumanın yerini tutmaz, SPA'nın kullandığı liste geçerlidir):

- Tutar/Değer eşiği (yıllık veya toplam)
- Süre uzunluğu
- Kontrol değişikliği (change of control) veya devir yasağı maddeleri
- Münhasırlık (exclusivity) veya rekabet yasağı
- İlk N müşteri veya tedarikçi sözleşmesi
- Taşınmaz kira sözleşmeleri
- Fikri mülkiyet (IP) lisansları
- İlişkili taraf (related-party) işlemleri
- Kamu/Devlet sözleşmeleri
- Olağan iş akışı dışındaki sözleşmeler

SPA'nın tanımı testin kendisidir. Mekanik olarak uygulayın — SPA tanımındaki herhangi bir başlığa uyan her sözleşme listeye girer.

### Adım 2: Tanımı bulgulara uygula

Due diligence'da incelenen her sözleşme için:

| Sözleşme | Uyduğu Kategori (Prong) | Dahil Mi |
|---|---|---|
| [isim] | [Yıllık 1 Milyon₺+; CoC maddesi var] | Evet |
| [isim] | [hiçbiri] | Hayır |

**İnsan kararı için işaretlenecek sınır durumlar:**
- Sözleşme X-1 değerinde (eşiğin hemen altında) ama iş için kritik.
- Sözleşme bir tanıma uyuyor ama zaten feshediliyor.
- Sözlü anlaşmalar veya yan mektupların (side letters) sayılıp sayılmayacağı.

### Adım 3: Liste verilerini topla

Dahil edilen her sözleşme için listenin genellikle şunlara ihtiyacı vardır:

| Alan | Kaynak |
|---|---|
| Karşı Taraf Adı | Sözleşme |
| Sözleşme başlığı/türü | Sözleşme |
| Tarih | Sözleşme |
| Süre / bitiş | Sözleşme |
| Yıllık/toplam değer | Sözleşme veya yönetim verisi |
| Hangi önemlilik kategorisine uyduğu | Adım 2 analizi |
| İşlem için onay gerekip gerekmediği | Due diligence bulgusu |
| VDR referansı | Diligence envanteri |

Mevcut diligence çıkarımlarından çekin. Bir alan eksikse işaretleyin — tahmin etmeyin.

### Adım 4: Sözleşmeye göre formatla

Açıklama listelerinin (disclosure schedules) bir formatı vardır — genellikle numaralandırılmış bir liste veya tablo, bazen sözleşme türüne göre alt bölümlere ayrılmış. Taslak sözleşmedeki diğer eklerin formatıyla eşleştirin.

```markdown
## Ek 3.[X] — Önemli Sözleşmeler

İmza tarihi itibarıyla Önemli Sözleşmeler aşağıdakilerdir:

### (a) Müşteri Sözleşmeleri

1. [Hedef] ile [Karşı Taraf] arasında [tarih] tarihli [Sözleşme Başlığı].
   [Format gerektiriyorsa kısa açıklama.]
   [VDR: yol/link]

2. [...]

### (b) Tedarikçi Sözleşmeleri

[...]

### (c) Taşınmaz Kiraları

[...]

[vb. — sözleşmenin tanım yapısına göre alt bölümler]
```

### Adım 5: İzin/Onay (Consent) Takibi Yüzeyi

Ayrı olarak (listenin kendisinde değil — bu dahili bir iştir), listelenen hangi sözleşmelerin onay/izin gerektirdiğini takip edin.

> İzin takip yüzeyi ve açıklama listesinin teslimat öncesi taslakları, gizli/imtiyazlı due diligence materyallerinden türetilir ve onların gizlilik statüsünü miras alır. Listenin kendisi, nihai SPA'nın bir eki olarak teslim edildiğinde bir işlem belgesi olur ve gizliliği düşebilir (avukat-müvekkil bağlamında); teslimattan önce iç notları (annotation) temizleyin.

| Liste # | Karşı Taraf | Onay gerekli mi | Durum | Sorumlu | Teslim/Süre |
|---|---|---|---|---|---|
| 3.X(a)(1) | [isim] | Evet — CoC md.12.2 | Talep gönderildi | [isim] | [tarih] |

Bu tablo `kapani-kontrol-listesi`ni besler.

## Çapraz Kontrol (Cross-check)

Teslim etmeden önce:
- Tanıma/Kategoriye uyan her sözleşme listededir (eksiksiz).
- Tanıma uymayan hiçbir sözleşme listede yoktur (aşırı açıklamadan kaçın — bu bir tekeffüldür, veri yığını değil).
- Liste diğer tekeffüllerle tutarlıdır (Ek 3.X'te olup rehin yaratan bir sözleşme, rehinler ekinde de olmalıdır).
- Alıcı avukatının dayanak belgeyi bulabilmesi için her girdinin bir VDR atfı vardır.

## Devirler (Handoffs)

- **due-diligence-sorun-cikartma'dan (nereden):** Sözleşme düzeyindeki bulgular girdidir.
- **kapani-kontrol-listesi'ne (nereye):** İzin/onay (consent) kalemleri kontrol listesine gider.

## Bu yetenek ne yapmaz

- Önemlilik (materiality) tanımına karar vermez — bu satın alma sözleşmesindedir.
- İzin/onayları almaz — hangilerinin gerektiğini takip eder.
- Tekeffül/beyan maddesini (rep) taslaklamaz — tekeffülün atıfta bulunduğu listeyi doldurur.
