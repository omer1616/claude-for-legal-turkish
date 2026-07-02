---
name: uluslararasi-genisletme
description: >
  Referans: uluslararası işe alım için uygulama-planlama çerçevesi — EOR
  (Employer of Record) vs. tüzel kişilik karar çerçevelemesi, vergi/finans/İK
  için fonksiyonlar arası tetikleyiciler, yapılandırılmış dış avukat brifing
  talepleri ve kalıcı bir boşluk izleyicisi. /genisletme-baslangic ve
  /genisletme-guncelleme tarafından yüklenir; doğrudan çağrılmaz.
user-invocable: false
---

# Uluslararası Genişleme Skill'i

## Yön: hangi taraftasınız? `[doğrulanacak]`

Bu skill yargı-çevresi-nötr tasarlanmıştır ve **iki yönde** de çalışır —
intake'te hangisi geçerli olduğunu netleştirin:

1. **Türkiye merkezli bir şirket yurt dışına açılıyor** (ör. Türk bir SaaS
   şirketi Almanya'da ilk çalışanını işe alıyor). Bu durumda "ev sahibi
   ülke" hedef ülkedir ve dış avukat brifingi o ülkenin hukukunu kapsar.
2. **Yabancı bir şirket Türkiye'ye giriyor** (ör. bir ABD şirketi Türkiye'de
   ilk çalışanını işe alıyor). Bu durumda "ev sahibi ülke" Türkiye'dir;
   çalışma izni (Uluslararası İşgücü Kanunu, YU-Kart), SGK işyeri tescili ve
   Çalışma ve Sosyal Güvenlik Bakanlığı bildirimleri gündeme gelir
   `[doğrulanacak]`.

Bu skill'in hangi senaryo(lar)ı birincil olarak kapsaması gerektiği açık bir
sorudur — bkz. `.claude/tasks/is-hukuku/README.md` açık sorular bölümü.
Şimdilik skill her iki yönü de intake'te sorarak ele alır ve dış avukat
brifing talebini buna göre çerçeveler.

## Dosya bağlamı

**Dosya bağlamı.** Pratik düzeyi CLAUDE.md'deki `## Dosya çalışma alanları`
bölümünü kontrol et. `Etkin` `✗` ise (şirket içi kullanıcılar için
varsayılan), bu paragrafın geri kalanını atla — skill'ler pratik düzeyi
bağlamı kullanır ve dosya makinesi görünmez. Etkinse ve aktif bir dosya
yoksa sor: "Bu hangi dosya için? `/is-hukuku:dosya-calisma-alani switch
<slug>` çalıştır veya `pratik-duzeyi` de." Aktif dosyanın `matter.md`'sini
dosyaya özgü bağlam ve geçersizleştirmeler için yükle. Çıktıları dosya
klasörüne yaz:
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/matters/<dosya-slug>/`.
`Çapraz-dosya bağlamı` `on` olmadıkça başka bir dosyanın dosyalarını asla
okuma.

---

## Amaç

Uluslararası işe alım, büyüyen şirketlerde kimse tam resme sahip
olmadığı için baştan savma ele alınır. Hukuk, iş hukuku sorularını bilir
ama daimi işyeri (PE) vergi risklerini bilmez. Finans maliyet modelini
bilir ama çalışan-temsili tetikleyicilerini bilmez. İK ücret
kıyaslamalarını bilir ama 1. gün uyum gereksinimlerini bilmez.

Bu skill bu fonksiyonların hiçbirinin yerini almaz. Araziyi haritalar, her
paydaş için doğru soruları taslaklar, dış avukatı ülkeye özgü konularda
yönlendiren bir brifing talebi üretir ve projeyi oturumlar arasında hareket
halinde tutan bir izleyici oluşturur.

Bu skill genişlemenin karara bağlandığını varsayar. "Genişlemeli miyiz?"
çerçevesi değildir.

Bu skill ülkeye özgü iş hukuku içermez. Esaslı kurallar sık değişir ve
role, kadroya ve sektöre göre değişir — skill her ülkeyi kendi bilgisine
güvenmek yerine bir dış avukat brifinginden geçirir.

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
dosyasını oku → yargı çevresi ayak izi, eskalasyon tablosu, mevcut herhangi
bir genişleme notu.

## Çıktı başlığı

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` →
`## Çıktılar` bölümündeki iş-ürünü başlığını ekle (kullanıcı rolüne göre
değişir — bkz. `## Bunu kim kullanıyor`).

## İş akışı

### Adım 1 — Bilgi toplama

Aşağıdakilerin hepsini tek blokta sor:

> Genişleme planını kurmadan önce bu genişlemenin şeklini anlamam gerekiyor.
> Cevaplayabildiklerinizi cevaplayın — cevaplardaki boşluklar da kendi
> başına faydalı veridir:
>
> **Yön**
> - Bu, Türkiye merkezli şirketinizin yurt dışına açılması mı, yoksa
>   yabancı bir şirketin Türkiye'ye girişi mi?
>
> **Genişleme**
> - Hangi ülke?
> - Hangi rolleri işe alıyorsunuz? (İş fonksiyonu önemlidir — anlaşma
>   kapatan bir satış temsilcisi, kod yazan bir mühendisten farklı hukuki
>   maruziyet yaratır)
> - Önümüzdeki 12 ayda kaç işe alım planlanıyor?
> - İlk kişinin ne zaman başlaması gerekiyor?
>
> **Mevcut durum**
> - Bu ülkede zaten bir tüzel kişiliğiniz var mı?
> - Daha önce bir EOR (Employer of Record) sağlayıcısı kullandınız mı?
>   Zaten bir tanesini mi değerlendiriyorsunuz?
> - Vergi veya finans henüz devreye girdi mi?
> - Bu ülkede dış iş hukuku danışmanınız var mı?
>
> **Stratejik bağlam**
> - Bu uzun vadeli stratejik bir taahhüt mü (gerçek bir ekip kurmak) yoksa
>   piyasayı test etmek mi (bir veya iki işe alım, nasıl gittiğine bakmak)?
> - Yapı kararını veren yönetici sponsoru kim?

Devam etmeden önce cevapları bekle.

### Adım 2 — EOR vs. tüzel kişilik çerçevelemesi

Bu kararı verme. CFO ve vergi danışmanının karar verebileceği kadar hassas
çerçevele.

Aşağıdaki faktörleri intake cevaplarına karşı işle ve yapılandırılmış bir
çerçeveleme belgesi üret:

**Temel değiş tokuş:**

| Faktör | EOR'a işaret eder | Tüzel kişiliğe işaret eder |
|---|---|---|
| 12 ayda kadro | Daha az işe alım | Daha çok işe alım |
| İlk işe alıma kadar süre | Kısa pist | Daha uzun pist mevcut |
| Stratejik taahhüt | Piyasayı test etme | Uzun vadeli varlık |
| Maliyet duyarlılığı | EOR komisyonu kabul edilebilir | Ölçek tüzel kişiliği daha
  verimli kılar |
| Kontrol ihtiyaçları | Düşük — EOR işvereni yerel İK'yı halleder | Yüksek —
  doğrudan işveren ilişkisi isteniyor |
| Fikri mülkiyet hassasiyeti | Daha düşük | Daha yüksek — tüzel kişilik
  sahipliği daha temiz |

Spesifik kadro kırılma noktaları, EOR komisyon aralıkları, kurulum
maliyetleri ve zaman çizelgeleri ülkeye ve sağlayıcıya göre değişir — sabit
kodlama. Bu soruları vergi/finansa ve EOR sağlayıcısına yönlendir.

**Daimi işyeri (PE) vergi riski işareti (vergi danışmanına yönlendir):**
Roller satış, iş geliştirme, müşteri yönetimi veya şirket adına sözleşme
müzakere etme/imzalama yetkisi olan herhangi birini içeriyorsa — bunu açıkça
işaretle:

> PE Riski: [Rol türü], [ülke]'de bir tüzel kişilik olmadan önce bile
> vergilendirilebilir bir daimi işyeri yaratabilir. Bu bir vergi sorunudur,
> bir istihdam sorunu değil. Vergi danışmanı ilk işe alımdan önce
> değerlendirmelidir.

**CFO/vergi için soruyu üret:**

> CFO'nuz ve vergi danışmanınız için sorular:
> - 12 ayda [N] işe alımda, tüzel kişilik kurulumu (EOR komisyonu, kurulum
>   maliyetleri ve devam eden uyum yükü hesaba katılarak) hangi kadroda
>   EOR'dan daha uygun maliyetli hale geliyor?
> - [PE-riski rolleri varsa:] Bu rol türleri [ülke]'de vergilendirilebilir
>   bir daimi işyeri yaratıyor mu? Evetse, bu tüzel kişilik zaman
>   çizelgesini değiştiriyor mu?
> - EOR ile başlayıp sonra tüzel kişiliğe geçersek, EOR'da zaten olan
>   çalışanlar için geçiş riskleri neler?
> - Bu ülke için tercih ettiğimiz EOR sağlayıcısı kim ve yerel uyum geçmişini
>   kontrol ettik mi?

### Adım 3 — Fonksiyonlar arası tetikleyiciler

Devreye girmesi gereken her fonksiyon için şunu belirt: ne yapmaları
gerektiğini ve hukuğun onlara sorması gereken spesifik soruları. Yalnızca
"finansı devreye sok" deme. İsteği taslakla.

**Vergi danışmanı** (ilk işe alımdan önce her zaman gerekli)

Ne yapmaları gerekiyor: PE risk analizi, vergi amaçlı tüzel kişilik gerekip
gerekmediğini belirleme, bu yargı çevresinde hisse senedi vergi
muamelesine danışmanlık.

Hukuğun sormaları gereken sorular:
- [Ülke]'de bir [rol türü] işe almak, tüzel kişiliğimiz olmadan önce bir
  daimi işyeri veya vergilendirilebilir bağlantı yaratıyor mu?
- PE sorunu çözülmeden önce işe almaya başlarsak maruziyet penceremiz ne?
- Pay/opsiyon ödüllerimiz [ülke]'de nasıl vergilendiriliyor? Hibe ve hak
  edişte çalışanlara danışmanlık için yerel vergi danışmanına ihtiyacımız
  var mı?
- Tüzel kişilik kurarsak, yan kuruluş ile ana şirket arasında hangi
  şirketler arası hizmet sözleşmesi gerekiyor?

**Finans / Bordro** (ilk maaş bordrosundan önce gerekli)

Ne yapmaları gerekiyor: yerel bordro sağlayıcısını tespit etme (veya
EOR'un bunu hallettiğini teyit etme), zorunlu işveren katkılarını
bütçeleme, tüzel kişilikse yerel bankacılık kurma.

Hukuğun sormaları gereken sorular:
- Yerel bir bordro sağlayıcısı tespit ettik mi? (EOR ise: EOR'un bordroyu
  yerel sosyal katkılar dahil hallettiğini teyit edin)
- [Ülke]'deki zorunlu işveren katkıları — emeklilik/SGK, sağlık — neler ve
  bunlar ücret modelinde bütçelendi mi?
- [Ülke]'deki çalışanlar için hisse senedi hibeleri nasıl yönetilecek?
  Hak edişte işveren tarafı vergi kesinti yükümlülüklerini modelleyen
  oldu mu?

**İK / Toplam Ödüller** (teklif yapılmadan önce gerekli)

Ne yapmaları gerekiyor: yan hak kıyaslaması, yerel piyasaya karşı ücret
kıyaslaması, zorunlu vs. ek yan hakları teyit etme.

Hukuğun sormaları gereken sorular:
- [Ülke]'de yasal olarak zorunlu olan yan haklar nelerdir, piyasa-standart
  olanlar nelerdir? (Yanlışlıkla gerekenden fazla veya piyasadan az söz
  vermek istemeyiz)
- Standart hisse senedi paketimiz bu piyasada rekabetçi mi, yoksa yerel
  uygulama önemli ölçüde farklı mı?
- Bu kişinin günlük yöneticisi kim olacak — yerel mi yoksa merkezden uzaktan
  mı? (Bazı yargı çevrelerinde çalışan-temsili analizini ve iş sözleşmesi
  şartlarını etkiler)

**Dış avukat** (gerekli — atlama)

Ne yapmaları gerekiyor: bu rol ve kadro için yerel iş hukuku çerçevesini
araştırma ve danışmanlık, yerel iş sözleşmesini gözden geçirme/taslaklama,
önerilen düzenlemede herhangi bir yapısal sorunu işaretleme.

Adım 4'teki dış-avukat brifing talebi bu görevlendirmenin gündemidir. Baştan
gönder — parça parça sorma.

### Adım 4 — Ülkeye özgü brifing talebi

Saklı bir ülke referans tablosu yerine, bu skill yapılandırılmış bir dış
avukat brifing talebi üretir. Esaslı yerel hukuk (tüzel kişilik
gereksinimleri, yasal yan haklar ve katkılar, fesih korumaları, bildirim
süreleri, çalışan-temsili/işyeri konseyi/toplu iş sözleşmesi
yükümlülükleri, zorunlu izin, rekabet yasağı, veri koruma, çalışma izni)
ülkeye *ve* role *ve* kadroya *ve* sektöre göre değişir ve sık değişir. Her
ülkeyi teyit gerektiren bir ülke olarak ele al — skill'in kendi bilgisine
güvenme.

Intake cevaplarına göre uyarlanmış aşağıdaki brifing talebini taslakla:

**Dış avukat brifing talebi — [Ülke]**

> [Tarih]'te başlayarak [Ülke]'de [N] çalışan işe almayı planlıyoruz,
> şu rollerde: [roller]. 12 ay üzerinden hedef kadro: [N]. Tercih edilen
> yapı (danışmanınıza ve vergi danışmanına tabi): [EOR / tüzel kişilik /
> kararsız]. Aşağıdakilerin her birini kapsayan bir brifinge ihtiyacımız
> var. Lütfen bir referans tablosu olarak değil, birincil hukuka atıflı
> sorular olarak cevaplayın — zaman içindeki değişiklikleri takip
> edebilmek istiyoruz.
>
> 1. **Tüzel kişilik ve işe alım yapısı** — seçeneklerimiz neler (tüzel
>    kişilik üzerinden doğrudan işe alım, EOR, taşeron) ve bu kadro ve
>    roller için pratik ve hukuki değiş tokuşlar neler?
>
> 2. **İş sözleşmesi gereksinimleri** — hangi form gerekli veya standart?
>    Neyin dahil edilmesi gerekiyor? Ne dahil edilemez veya uygulanamaz?
>    Hangi dil veya çeviri gereksinimleri geçerli?
>
> 3. **Fesih** — bildirim gereksinimleri ve kıdem tazminatı yükümlülükleri
>    neler? Pratikte fesih ne kadar zor (korumalı-neden standartları,
>    toplu işten çıkarmada sosyal-seçim kuralları, makul-bildirim genel
>    hukuk maruziyeti)? Baştan hangi belgeleme standardını oluşturmalıyız?
>
> 4. **Zorunlu yan haklar ve işveren katkıları** — kanunen ne sağlamamız
>    gerekiyor (emeklilik, sosyal sigorta, sağlık, ücretli izin, ikramiye)?
>    Bütçelememiz gereken güncel işveren katkı oranları neler? Kontrol eden
>    kanunu atıf yapın ve güncelliği doğrulayın.
>
> 5. **Rekabet yasağı hükümleri** — rekabet yasakları uygulanabilir mi?
>    Hangi koşullarda ve hangi tazminat gereksinimleriyle? Hangi gizlilik
>    ve fikri mülkiyet devri dili geçerli oluyor?
>
> 6. **Çalışan temsili** — işyeri konseyi, çalışan temsili, sendika veya
>    toplu iş sözleşmesi gereksinimleri var mı? Hangi kadroda tetikleniyor?
>    Hangi danışma veya ortak-karar hakları geçerli? Sendikalı olmasak
>    bile herhangi bir sektörel toplu sözleşme kapsamında mıyız?
>
> 7. **Veri koruma** — çalışan verisine hangi yükümlülükler uygulanıyor?
>    Çalışan verisinin Türkiye'ye/merkeze akışı için bir veri aktarım
>    mekanizması gerekiyor mu?
>
> 8. **Çalışma izni** — yabancı uyruklular için hangi izinler veya vizeler
>    gerekiyor? İşlem süreleri neler?
>
> 9. **Sektöre özgü kurallar** — sendikalı olmasak bile sektörümüze
>    uygulanan sektör kuralları, ödüller veya toplu sözleşmeler var mı?
>
> 10. **Taşeron/bağımsız yüklenici riski** — ülkenin sınıflandırma testi
>     nedir ve değerlendirebileceğimiz herhangi bir taşeron düzenlemesi
>     için varsayılan-işçilik veya yeniden sınıflandırma riskleri neler?
>
> 11. **Hisse senedi / teşvik ücretlendirmesi** — burada RSU, opsiyon veya
>     diğer hisse senedi ödüllerini nasıl verdiğimizi yöneten yerel vergi,
>     menkul kıymet veya iş hukuku kuralları var mı?
>
> 12. **1. gün uyumu** — ilk çalışan başlamadan önce ne olmalı? Tescil
>     gereksinimleri, bildirimler, başvurular, ilanlar?
>
> 13. **Buraya ilk kez işe alan Türk şirketlerini şaşırtan ilk 2-3 şey** —
>     müvekkillerin size daha erken sormasını dilediğiniz şeyler neler?
>     ABD/Türk ekibinin fark etmemiş olabileceği *son zamanlarda ne
>     değişti*?

Bu brifing talebini genişleme izleyicisine tek bir açık kalem olarak ekle:
sorumlu = Dış Avukat, durum = açık, tam brifing gündemi sorular alanında.
Ekibin daha önce sorduğu bir yargı çevresiyse, brifingi yine de gönder — bu
bir ilk temas değil, bir güncellik kontrolüdür.

### Adım 5 — Genişleme izleyicisini oluştur

Adım 2-4'te tespit edilen tüm açık kalemlerle
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/genisletme-[ulke-slug].yaml`
dosyasına yeni bir dosya yaz. Bu dosya oturumlar arasında kalıcıdır.

Format:

```yaml
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırması ## Çıktılar'a göre — role göre değişir; bkz. `## Bunu kim kullanıyor`]
ulke: [Ülke adı]
ulke_slug: [kucuk-harfli-tireli]
yon: [yurtdisina-acilma / turkiyeye-giris]
baslangic_tarihi: [ISO tarih]
ilk_ise_alim_hedefi: [ISO tarih veya "BELİRSİZ"]
kadro_12ay: [N]
roller: [liste]
stratejik_taahhut: [test / uzun-vadeli]
eor_veya_tuzel_kisilik: [EOR / tüzel kişilik / kararsız]
dis_avukat_devreye_girdi: [true / false]
pe_riski_isaretlendi: [true / false]
son_guncelleme: [ISO tarih]

acik_kalemler:
  - id: 1
    kategori: [yapi / vergi / finans / ik / dis-avukat / uyum]
    kalem: "[ne olması gerekiyor]"
    sorumlu: "[fonksiyon veya kişi]"
    durum: [acik / devam-ediyor / tamamlandi / engellendi]
    son_tarih: [ISO tarih veya null]
    sorular:
      - "[Adım 2-4'te taslaklanan spesifik soru]"
    notlar: ""

  - id: 2
    [vb.]
```

Adım 2-4'te tespit edilen her eylem için bir açık kalem oluştur. Birden
fazla eylemi tek bir kaleme sıkıştırma — her kalem tamamlanabilir olmalı ve
tek bir sorumluya atfedilebilir olmalı.

### Adım 6 — Çıktı

> **Yargı çevresi varsayımı.** Bu plan genişlemeyi intake'te tespit edilen
> tek bir ülkeye çerçeveler. Yerel iş hukuku, vergi kuralları,
> çalışan-temsili yükümlülükleri ve veri koruma gereksinimleri ülkeye,
> bölgeye, sektöre ve kadroya göre maddi olarak değişir ve sık değişir. Her
> esaslı yerel-hukuk cevabı bu skill'den değil, dış avukat brifing
> talebinden gelir. Plan daha sonra başka bir ülke için uyarlanırsa
> brifingi yeniden çalıştırın.

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırması ## Çıktılar'a göre — role göre değişir; bkz. `## Bunu kim kullanıyor`]

## Uluslararası Genişleme: [Ülke] — [Tarih]

**Yön:** [Yurt dışına açılma / Türkiye'ye giriş]
**İlk işe alım hedefi:** [tarih]
**Kadro (12 ay):** [N]
**Roller:** [liste]
**İzleyici:** ~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/genisletme-[slug].yaml

---

### EOR vs. Tüzel Kişilik

[Adım 2'den çerçeveleme — tablo, uygunsa PE risk işareti, CFO/vergi için
sorular]

---

### Kimin devreye girmesi gerekiyor — ve onlara ne sorulacak

**Vergi danışmanı** — [N] soru
[Adım 3'ten sorular]

**Finans / Bordro** — [N] soru
[Adım 3'ten sorular]

**İK / Toplam Ödüller** — [N] soru
[Adım 3'ten sorular]

**Dış avukat** — aşağıdaki brifing talebine bakın
[Adım 4'ten tam brifing talebi]

---

### Açık kalemler ([N] toplam)

| # | Kalem | Sorumlu | Durum |
|---|---|---|---|
| 1 | [kalem] | [sorumlu] | Açık |
[vb.]

---

Kalemler kapandıkça durumu güncellemek için
`/is-hukuku:genisletme-guncelleme [ülke]` çalıştırın.
```

## Bu skill'in YAPMADIKLARI

- Belirli bir ülkenin iş hukuku konusunda danışmanlık yapmak — bu dış
  avukatın işidir.
- EOR vs. tüzel kişilik kararını vermek — doğru karar vericiler için
  çerçeveler.
- Yerel iş sözleşmesini taslaklamak — dış avukatın bunu yapması gerektiğini
  işaretler.
- Kendi bilgisinden ülkeye özgü kuralları belirtmek — her ülke bir dış
  avukat brifinginden geçirilir.
- Dış avukat görevlendirmesinin yerine geçmek — her yeni ülke, istisnasız,
  yerel danışman gerektirir.
