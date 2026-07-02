---
name: ic-sorusturma
description: >
  Referans: iç soruşturmaların intake'ten nihai nota kadar yönetimi için
  paylaşılan çerçeve — meslek sırrı kapsamında soruşturma günlüğü, iğne-bulma
  ile belge işleme, kaynak kapsama takibi, günlüğe karşı S&C, not taslaklama
  ve hedef kitle özetleri. /sorusturma-ac, /sorusturma-ekle, /sorusturma-sorgu,
  /sorusturma-notu ve /sorusturma-ozeti tarafından yüklenir; doğrudan
  çağrılmaz.
user-invocable: false
---

# İç Soruşturma Skill'i

## Dosya bağlamı

**Dosya bağlamı.** Pratik düzeyi CLAUDE.md'deki `## Dosya çalışma alanları`
bölümünü kontrol et. `Etkin` `✗` ise (şirket içi kullanıcılar için varsayılan),
bu paragrafın geri kalanını atla — skill'ler pratik düzeyi bağlamı kullanır ve
dosya makinesi görünmez. Etkinse ve aktif bir dosya yoksa sor: "Bu hangi dosya
için? `/is-hukuku:dosya-calisma-alani switch <slug>` çalıştır veya
`pratik-duzeyi` de." Aktif dosyanın `matter.md`'sini dosyaya özgü bağlam ve
geçersizleştirmeler için yükle. Çıktıları dosya klasörüne yaz:
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/matters/<dosya-slug>/`.
`Çapraz-dosya bağlamı` `on` olmadıkça başka bir dosyanın dosyalarını asla okuma.

---

## Çıktı başlığı

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` →
`## Çıktılar` bölümündeki iş-ürünü başlığını ekle (kullanıcı rolüne göre
değişir — bkz. `## Bunu kim kullanıyor`). Bu skill'in ürettiği her dosya,
günlük, not ve özet o başlıkla açılır.

> **Dağıtım disiplini.** Bu skill'in oluşturduğu her dosya — günlük girdileri,
> not taslakları, hedef kitle özetleri, belge notları — altındaki
> soruşturmanın meslek sırrı ve gizlilik statüsünü devralır. Meslek sırrı
> çemberinin dışına dağıtım (soruşturma ekibi dışındaki avukat olmayanlara
> yönlendirme, kapsam belirlemeden İK'yı CC'lemek, iş tarafına vermek) tüm
> soruşturma üzerindeki meslek sırrını kaybettirebilir. Bu dosyaları meslek
> sırrı kapsamındaki malzemelerin yaşadığı yerde sakla, iş-ürünü başlığına
> göre etiketle ve her dağıtım kararını bilinçli ver.

## ⚠️ Meslek sırrı uyarısı — devam etmeden önce oku

**Etiketleme meslek sırrı yaratmaz.** Yukarıdaki başlık amaçlanan korumayı
yansıtır ve eklenmesi önemlidir — ama kendisi meslek sırrını oluşturmaz.
Herhangi bir çıktının gerçekten meslek sırrı kapsamında olup olmadığı,
soruşturmanın avukat yönlendirmesinde olup olmadığına, belgelerin hangi
amaçla oluşturulduğuna ve daha sonra nasıl kullanıldığına/ifşa edildiğine
bağlıdır. `[doğrulanacak — Türk hukukunda in-house hukuk biriminin ürettiği
iç soruşturma analizinin meslek sırrı kapsamına ne ölçüde girdiği; Avukatlık
Kanunu m.36/m.58'in kapsamı, bkz. `references/ortak-guardrail-TR.md`]`

**Bir dosya açmadan önce teyit et:** Bu soruşturma avukat yönlendirmeli mi?
Değilse — İK danışman rolündeki hukukla soruşturmayı yürütüyorsa, veya hukuk
danışmanının yönlendirmesiyle hukuki tavsiye almak amacıyla başlatılmadıysa —
meslek sırrı analizi maddi olarak değişir ve bu skill'in varsayılan
etiketlemesi yanıltıcı olabilir. Herhangi bir günlük veya dosya
oluşturulmadan önce bu soruyu avukata yönelt.

Meslek sırrının uygulanabilirliği konusunda herhangi bir şüphe varsa, avukat
soruşturma dosyaları oluşturulmadan önce bunu çözmelidir. Yanlış etiketlenmiş
malzemeler, meslek sırrı daha sonra itiraz edilirse belge ibrazında sorun
yaratabilir.

---

## Amaç

İç soruşturmalar iki şekilde başarısız olur: kapsam boşlukları (hiç
toplanmamış kaynaklar) ve sentez boşlukları (toplanmış ama hiç
bağlanmamış kanıt). Bu skill ikisini de ele alır — toplanan ve toplanmayanı
takip eder, avukatı boğmadan önemli olanı yüzeye çıkarmak için belge
yığınlarını işler ve herhangi bir noktada meslek sırrı kapsamındaki bir nota
dönüştürülebilecek yapılandırılmış bir günlük tutar.

## Meslek sırrı notu

Bu skill tarafından oluşturulan tüm dosyalar yukarıdaki meslek sırrı
etiketini taşır. O etiketin ne yapıp ne yapmadığına dair tam çekince için bu
skill'in en üstündeki uyarıya bakın.

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` →
eskalasyon tablosu, not düşülmüş soruşturma protokolleri.

---

## Mod 1: Yeni bir dosya açma

`/is-hukuku:sorusturma-ac` veya "bir soruşturma aç" ya da "şunun hakkında
soruşturma başlat" ile tetiklenir.

### Adım 1 — Intake

Aşağıdakileri tek blokta sor:

> Soruşturma günlüğünü açmak için birkaç şeye ihtiyacım var:
>
> **Dosya**
> - İddia veya endişe sade terimlerle nedir?
> - Şikayetçi kim (veya bunu ne tetikledi — şikayet, ihbar, denetim, yönetici
>   gözlemi)?
> - Davalı veya konu kim?
> - İddia edilen davranışın yaklaşık zaman aralığı nedir?
> - Bu avukat yönlendirmeli mi? (Evetse: meslek sırrı koruması geçerli.
>   Hayırsa: devam etmeden önce meslek sırrı riskini işaretle.)
>
> **Soruşturma türü** (doğru kaynak kontrol listesini önermeme yardımcı olur)
> - İK: taciz / ayrımcılık / misilleme
> - Mali usulsüzlük: masraf hilesi / satın alma usulsüzlükleri / zimmet
> - Yönetici usulsüzlüğü: menfaat çatışması / açıklanmamış ilişkiler /
>   yönetişim hataları
> - İhbar (whistleblower): korumalı faaliyet nedeniyle misilleme
> - Diğer: kısaca tanımlayın
>
> **Temsil ve işveren statüsü** (görüşme usulünü değiştiren paralel hukuki
> çerçeveleri yüzeye çıkarır)
> - Davalı, şikayetçi veya öngörülen herhangi bir tanık bir sendika tarafından
>   mı temsil ediliyor veya toplu iş sözleşmesi kapsamında mı? (Evetse,
>   soruşturma görüşmelerinde sendikal temsil hakları araştırması için
>   işaretle — Türk hukukunda ABD'deki Weingarten hakları benzeri bir usul
>   olup olmadığı ve 6356 sayılı STİSK kapsamındaki temsil haklarının
>   soruşturma görüşme usulünü nasıl etkilediği `[doğrulanacak]`.)
> - Şirket bir kamu işvereni mi (kamu kurumu, devlet üniversitesi, kamu
>   tüzel kişisi)? (Evetse, kamu görevlisi disiplin soruşturması usulü —
>   657 sayılı Devlet Memurları Kanunu ve ilgili disiplin yönetmeliği —
>   ile ilgili araştırma için işaretle; ABD'deki Garrity doktrini
>   benzeri bir "kullanım bağışıklığı" kavramının Türk kamu personeli
>   hukukunda karşılığı olup olmadığı `[doğrulanacak]`.)

Bu bayraklardan biri tetiklenirse, görüşmeler yapılmadan önce geçerli
kuralları araştır (sendikal temsil için 6356 sayılı STİSK; kamu personeli
için 657 sayılı DMK ve ilgili disiplin mevzuatı). Birincil kaynakları atıf
yap. Güncelliği doğrula. Usul ayarlanana kadar görüşme yapma.

### Adım 2 — Dosya dizinini ve dosyaları oluştur

Aşağıdaki dosyaları oluştur:

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/sorusturma-[dosya-slug]/gunluk.yaml`:

```yaml
# [İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırması ## Çıktılar'a göre — role göre değişir; bkz. `## Bunu kim kullanıyor`]
dosya: "[dosya adı]"
dosya_slug: "[slug]"
acildi: "[ISO tarih]"
avukat_yonlendirmeli: [true/false]
iddia: "[sade dilde özet]"
sikayetci: "[isim/rol veya anonim]"
davali: "[isim/rol]"
davranis_zaman_araligi: "[yaklaşık tarihler]"
sorusturma_turu: "[ik/mali/yonetici/ihbar/diger]"
durum: acik
son_guncelleme: "[ISO tarih]"

konular:
  - "[Konu 1 — iddiadan türetilmiş, ör. 'iddia edilen düşmanca çalışma ortamı']"
  - "[Konu 2 varsa]"

girdiler: []

kanit_bosluklari: []
```

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/sorusturma-[dosya-slug]/kaynak-kontrol-listesi.yaml`:

Soruşturma türünden oluşturulur. Aşağıdaki kaynak kontrol listesi
şablonlarına bakın.

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/sorusturma-[dosya-slug]/incelenen-belgeler.yaml`:

```yaml
# [İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırması ## Çıktılar'a göre — role göre değişir; bkz. `## Bunu kim kullanıyor`]
dosya: "[dosya adı]"
toplam_incelenen: 0
toplam_yuzeye_cikan: 0
son_guncelleme: "[ISO tarih]"
belgeler: []
```

### Adım 3 — Kaynak kontrol listesi

Soruşturma türüne göre uygun kontrol listesini oluştur. Avukata sun ve sor:
"Bu dosyanıza uyuyor mu? Uygulanamayan kalemler varsa (N/A işaretlerim) veya
bu duruma özgü ek kaynaklar varsa bildirin."

**İK soruşturması kaynakları (taciz/ayrımcılık/misilleme):**
```yaml
kaynaklar:
  - id: 1
    kaynak: "Şikayetçi görüşmesi"
    durum: acik
    notlar: ""
  - id: 2
    kaynak: "Davalı görüşmesi"
    durum: acik
    notlar: ""
  - id: 3
    kaynak: "Tanık görüşmeleri — şikayetçi ve davalı hesaplarından tespit et"
    durum: acik
    notlar: ""
  - id: 4
    kaynak: "E-posta/mesajlaşma incelemesi — taraflar, ilgili tarih aralığı"
    durum: acik
    notlar: ""
  - id: 5
    kaynak: "İK kayıtları — davalının performans geçmişi, önceki şikayetler,
             önceki disiplin"
    durum: acik
    notlar: ""
  - id: 6
    kaynak: "Önceki şikayetler — İK sisteminde davalıya karşı önceki
             şikayetler"
    durum: acik
    notlar: ""
  - id: 7
    kaynak: "Karşılaştırma verisi — benzer durumlar nasıl ele alındı"
    durum: acik
    notlar: ""
  - id: 8
    kaynak: "İlgili politikalar — taciz, davranış kuralları, bildirim
             usulleri (iddia edilen davranış zamanında yürürlükte olan
             sürüm)"
    durum: acik
    notlar: ""
  - id: 9
    kaynak: "İddia edilen davranış zamanındaki organizasyon şeması ve
             raporlama ilişkileri"
    durum: acik
    notlar: ""
  - id: 10
    kaynak: "Takvim kayıtları — hesaplarda bahsedilen toplantı veya
             etkinlikler"
    durum: acik
    notlar: ""
  - id: 11
    kaynak: "Şirketi-temsil-eder-uyarısı belgelemesi — görüşmelerden önce
             avukatın şirketi (çalışanı değil) temsil ettiğine dair bir
             uyarı yapıldığının ve belgelendiğinin teyidi (ABD'deki Upjohn
             uyarısı kavramına benzer; Türk hukukunda karşılığı
             `[doğrulanacak]`)"
    durum: acik
    notlar: ""
```

**Mali usulsüzlük kaynakları:**
```yaml
kaynaklar:
  - id: 1
    kaynak: "Masraf raporları — konu, ilgili dönem"
    durum: acik
    notlar: ""
  - id: 2
    kaynak: "Onay kayıtları — masrafları veya işlemleri kim onayladı"
    durum: acik
    notlar: ""
  - id: 3
    kaynak: "Tedarikçi/taşeron kayıtları — sözleşmeler, faturalar, ödeme
             kayıtları"
    durum: acik
    notlar: ""
  - id: 4
    kaynak: "Finansal sistem kayıtları — ilgili hesaplar için muhasebe
             kayıtları"
    durum: acik
    notlar: ""
  - id: 5
    kaynak: "E-posta/mesajlaşma incelemesi — konu, onaylayanlar, karşı
             taraflar"
    durum: acik
    notlar: ""
  - id: 6
    kaynak: "Konu görüşmesi"
    durum: acik
    notlar: ""
  - id: 7
    kaynak: "Onaylayan görüşmeleri"
    durum: acik
    notlar: ""
  - id: 8
    kaynak: "Karşı taraf/tedarikçi görüşmeleri (erişilebilirse)"
    durum: acik
    notlar: ""
  - id: 9
    kaynak: "Denetim günlükleri — ilgili hesap/sistemler için erişim
             günlükleri"
    durum: acik
    notlar: ""
  - id: 10
    kaynak: "İlgili dönemi kapsayan önceki denetimler veya incelemeler"
    durum: acik
    notlar: ""
  - id: 11
    kaynak: "Şirketi-temsil-eder-uyarısı belgelemesi"
    durum: acik
    notlar: ""
```

**Yönetici usulsüzlüğü kaynakları:**
```yaml
kaynaklar:
  - id: 1
    kaynak: "Konu görüşmesi"
    durum: acik
    notlar: ""
  - id: 2
    kaynak: "Yönetim kurulu/ücretlendirme komitesi kayıtları — ilgili
             kararlar, tutanaklar, onaylar"
    durum: acik
    notlar: ""
  - id: 3
    kaynak: "İş sözleşmesi ve tadiller"
    durum: acik
    notlar: ""
  - id: 4
    kaynak: "Pay/opsiyon kayıtları — hibeler, kullanım, hak ediş"
    durum: acik
    notlar: ""
  - id: 5
    kaynak: "Masraf raporları ve onay kayıtları"
    durum: acik
    notlar: ""
  - id: 6
    kaynak: "E-posta/mesajlaşma incelemesi — konu, ilgili karşı taraflar"
    durum: acik
    notlar: ""
  - id: 7
    kaynak: "Menfaat çatışması beyanları (veya bunların yokluğu)"
    durum: acik
    notlar: ""
  - id: 8
    kaynak: "Dış iş faaliyeti kayıtları"
    durum: acik
    notlar: ""
  - id: 9
    kaynak: "Tanık görüşmeleri — doğrudan raporlar, akranlar, yönetim
             kurulu üyeleri"
    durum: acik
    notlar: ""
  - id: 10
    kaynak: "Konu hakkında dile getirilen önceki şikayetler veya endişeler"
    durum: acik
    notlar: ""
  - id: 11
    kaynak: "Şirketi-temsil-eder-uyarısı belgelemesi"
    durum: acik
    notlar: ""
```

**İhbar (whistleblower) kaynakları:**
```yaml
kaynaklar:
  - id: 1
    kaynak: "Şikayetçi görüşmesi"
    durum: acik
    notlar: ""
  - id: 2
    kaynak: "Orijinal şikayet veya ihbar — varsa yazılı form"
    durum: acik
    notlar: ""
  - id: 3
    kaynak: "Altta yatan iddiayla ilgili kayıtlar (şikayetçinin ihbar
             ettiği şey)"
    durum: acik
    notlar: ""
  - id: 4
    kaynak: "Korumalı faaliyetten sonra şikayetçiye karşı alınan herhangi
             bir olumsuz eylemle ilgili kayıtlar"
    durum: acik
    notlar: ""
  - id: 5
    kaynak: "Karar verici görüşmeleri — olumsuz eylem kararını kim verdi"
    durum: acik
    notlar: ""
  - id: 6
    kaynak: "Karşılaştırma verisi — korumalı faaliyete katılmayan benzer
             durumdaki çalışanların muamelesi"
    durum: acik
    notlar: ""
  - id: 7
    kaynak: "E-posta/mesajlaşma incelemesi — karar vericiler, ilgili zaman
             aralığı"
    durum: acik
    notlar: ""
  - id: 8
    kaynak: "Zamanlama analizi — korumalı faaliyetin olumsuz eyleme
             yakınlığı"
    durum: acik
    notlar: ""
  - id: 9
    kaynak: "Davalı/karar verici görüşmeleri"
    durum: acik
    notlar: ""
  - id: 10
    kaynak: "Şirketi-temsil-eder-uyarısı belgelemesi"
    durum: acik
    notlar: ""
```

Kontrol listesini sunduktan sonra
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/sorusturma-[slug]/kaynak-kontrol-listesi.yaml`
dosyasına yaz.

---

## Mod 2: Veri ekleme

`/is-hukuku:sorusturma-ekle` veya "[dosya] soruşturmasına ekle" ya da
avukat belge veya görüşme notu yapıştırdığında tetiklenir.

### Adım 1 — Dosyayı tespit et

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/` altında birden
fazla soruşturma klasörü varsa, bu verinin hangi dosyaya ait olduğunu sor.
Yalnızca biri varsa devam et.

### Adım 2 — Veri türünü tespit et

Bağlamdan net değilse sor:
- Görüşme notları (kimin görüşmesi?)
- Belge yığını (e-postalar, kayıtlar, dosyalar)
- Avukat notları veya gözlemleri
- Şirketi-temsil-eder-uyarısı teyidi

### Adım 3 — Belge çekme kriterleri

Herhangi bir belge yığını için aşağıdaki çekme kriterlerini uygula. Bir belge
AŞAĞIDAKİLERDEN HERHANGİ BİRİNİ karşılıyorsa yüzeye çıkarılır. Kriterler
kasıtlı olarak biraz agresif ayarlanmıştır — önemli bir kalemi kaçırmaktansa
yanlış pozitifi yüzeye çıkarmak daha iyidir.

**Çekme kriterleri:**
1. Soruşturmaya taraf olan herhangi birinin adını içerir (şikayetçi, davalı,
   önceki günlük girdilerinde adı geçen tanıklar)
2. Anahtar davranış zaman aralığında bir taraf tarafından yazılmış veya
   alınmış
3. İddia türüyle ilgili anahtar kelimeler içerir (intake'te ve önceki günlük
   girdilerinde tespit edilmiş — hesaplardan yeni terimler ortaya çıktıkça
   anahtar kelime listesini güncelle)
4. Açık veya örtük itiraflar içerir ("yapmamalıydım," "bunun nasıl
   göründüğünü biliyorum," "bunu yazıya dökme," "bunu sil")
5. Günlükte zaten olan herhangi bir hesapla çelişen dil içerir — spesifik
   çelişkiyi ve çeliştiği günlük girdisini işaretle
6. Yargılamada hassas olacak dil içerir: ayrımcı ifadeler, tehditler,
   korunan özellikler veya faaliyetler hakkında tartışmalar, iddia
   kalıbıyla eşleşen mali usulsüzlükler
7. Önceki hesaplarda bahsedilmiş ama belge setinde henüz görünmemiş bir
   belge türüdür (ör. bir görüşmede bir toplantıdan bahsedildi ama hiçbir
   takvim daveti incelenmedi) → yüzeye çıkarılan bir belge değil, kanıt
   boşluğu olarak günlükle

**İncelenen her belge için nihai durum:**
- `yuzeye_cikti`: bir veya daha fazla çekme kriterini karşılıyor — günlüğe
  girdi olarak eklendi
- `incelendi-onemli-bir-sey-yok`: incelendi, çekme kriterini karşılamıyor —
  yalnızca tek satırlık açıklamayla incelenen-belgeler.yaml'a günlüklendi

**Bir belge yığınını işledikten sonra bildir:**

```
Belge incelemesi tamamlandı.
İncelenen: [N] belge
Yüzeye çıkan: [N] potansiyel olarak önemli
İncelendi/önemli bir şey yok olarak günlüklendi: [N]
Tespit edilen yeni kanıt boşlukları: [N]

Yüzeye çıkan kalemler:
[tek satırlık açıklama ve hangi çekme kriterinin tetiklediğiyle liste]
```

### Adım 4 — Günlük girdilerini yaz

Yüzeye çıkan her kalem için `gunluk.yaml`'a ekle:

```yaml
- girdi_id: [otomatik artan]
  girdi_turu: [gorusme / belge / avukat-notu / bosluk]
  olay_tarihi: "[olayın gerçekleştiği tarih — günlüklendiği değil]"
  gunluklenme_tarihi: "[ISO tarih-saat]"
  kaynak: "[tanık adı/rolü, veya belge dosya adı/açıklaması]"
  kaynak_turu: [sikayetci / davali / tanik / belge / avukat-notu]
  konular: ["[bu girdinin ilişkili olduğu soruşturma konusu/konuları]"]
  onem: [yuksek / orta / arka-plan]
  ozet: "[bu girdinin kayda ne kattığı — 2-5 cümle]"
  alinti: "[önemliyse birebir alıntı — değilse boş]"
  celisen_girdi: [girdi_id veya null]
  destekleyen_girdi: [girdi_id veya null]
  guvenilirlik_notu: ""
  cekme_kriteri: "[hangi kriterin tetiklendiği — belgeler için]"
  meslek_sirri: avukat-is-urunu
```

Kanıt boşlukları için:

```yaml
- bosluk_id: [otomatik artan]
  aciklama: "[hangi belge/kaynağın var olması gerekirken bulunamadığı]"
  tespit_edildigi_yer: "[hangi günlük girdisi veya hesap bunu ortaya
                        çıkardı]"
  edinilecek_kaynak: "[nereden alınacağı]"
  oncelik: [yuksek / orta / dusuk]
  durum: acik
```

### Adım 5 — Kaynak kontrol listesini güncelle

Eklenen veri bir kontrol listesi kalemine karşılık geliyorsa, avukata
tamamlandı veya devam ediyor olarak işaretlenip işaretlenmeyeceğini sor.
Otomatik tamamlandı işaretleme — avukat bir kaynağın yeterince kapsandığına
ne zaman karar verecek.

---

## Mod 3: Günlüğü sorgulama

`/is-hukuku:sorusturma-sorgu` veya soruşturmaya karşı ifade edilen herhangi
bir soru ile tetiklenir (ör. "[tanık] ne dedi", "hangi belgeler doğruluyor",
"hâlâ neye ihtiyacımız var", "her tarafta en güçlü kanıt ne").

Cevap vermeden önce tam günlüğü oku. Cevap türleri:

**Olgusal sorgu** ("X, Y hakkında ne dedi"):
Günlük girdilerinden, girdi kimliklerine atıf yaparak cevapla. Günlükte
konuyla ilgili hiçbir şey yoksa: "Bu soruşturma günlüğünde [konu] hakkında
hiçbir bilgi görmedim ([N] girdi incelendi). Bu bir boşluk olarak
işaretlenmeye değer olabilir."

**Çelişki sorgusu** ("hesaplar nerede çelişiyor"):
Tüm celisen_girdi bağlantılarını yüzeye çıkar. Her çelişki için: çelişkinin
ne olduğunu, hangi girdilerin gerilim içinde olduğunu ve çelişki üzerinde
(varsa) hangi belgesel kanıtın bulunduğunu belirt.

**Kapsama sorgusu** ("hâlâ neye ihtiyacımız var" / "boşluklarımız ne"):
kaynak-kontrol-listesi.yaml ve gunluk.yaml'daki kanit_bosluklari'nı oku.
Bildir:
- Hâlâ açık kontrol listesi kalemleri
- Günlüklenen kanıt boşlukları
- Henüz toplanmamış kaynaklara atıf yapan hesaplar

**Güç sorgusu** ("her konudaki en güçlü kanıt ne"):
Günlükteki her konu için: en yüksek önem düzeyindeki girdileri, herhangi bir
belgesel doğrulamayı ve çözülmemiş çelişkileri tespit et. Konu konu sun.

**Şirketi-temsil-eder-uyarısı sorgusu** ("uyarıları belgeledik mi"):
Kontrol listesi kalemini ve bu belgelemeye etiketlenmiş herhangi bir günlük
girdisini kontrol et. Henüz tamamlanmadıysa işaretle.

---

## Mod 4: Notu taslakla veya güncelle

`/is-hukuku:sorusturma-notu` veya "notu taslakla" ya da "notu güncelle" ile
tetiklenir.

### Not yoksa — ilk taslak

Tam günlüğü oku. Aşağıdakiler tamamlanmadan taslaklama (tamamlanmamışsa
uyar):
- Her açık konu için en az bir girdi
- Şikayetçi ve davalı girdileri mevcut
- Kaynak kontrol listesi gözden geçirildi (açık yüksek öncelikli kalemleri
  işaretle)

Notu, standart iç soruşturma memorandumu pratiğini takip ederek aşağıdaki
yapıda taslakla:

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırması ## Çıktılar'a göre — role göre değişir; bkz. `## Bunu kim kullanıyor`]

---

**MEMORANDUM**

Kime: [Avukat dolduracak]
Kimden: [Avukat dolduracak]
Tarih: [Tarih]
Konu: İç Soruşturma — [Dosya adı]
Durum: ÖN TASLAK

---

## Yönetici Özeti

[2-3 paragraf: iddia sade terimlerle, soruşturma kapsamı ve metodoloji
özeti, madde madde anahtar bulgular (Sabit / Sabit Değil / Sonuçsuz), önerilen
eylemler. En son yazılır ama ilk görünür.]

---

## Arka Plan ve Kapsam

**Tetikleyici olay:** [Soruşturmayı ne başlattı]

**Soruşturulan iddialar:**
[Günlükteki her konu numaralandırılmış bir iddia olarak]

**Kapsam dışı:** [Açıkça soruşturulmayan herhangi bir şey ve nedeni]

**Soruşturma dönemi:** [İddia edilen davranışın tarihleri]
**Soruşturma yürütüldü:** [Açılış tarihi] - [şimdiki veya kapanış tarihi]

---

## Metodoloji

**Yapılan görüşmeler:**
| Tanık | Rol | Tarih | Notlar |
|---|---|---|---|
[kaynak_turu = gorusme olan günlük girdilerinden doldurulur]

**İncelenen belgeler:**
[İncelenen belge kategorilerinin, hacminin, tarih aralığının özeti. Tam
belge günlüğü ayrıca tutulur.]

**Diğer kaynaklar:**
[Kontrol listesinden diğer kaynaklar — politikalar, İK kayıtları, vb.]

**Sınırlamalar:** [İstenen ama elde edilemeyen herhangi bir kaynak, herhangi
bir kısıtlama]

---

## Olgusal Bulgular

*[Konuya göre düzenlenmiş — her iddia için bir bölüm. Tanığa göre değil,
salt kronolojik değil.]*

### Konu 1: [İddia]

[Kanıtın bu konuda ne gösterdiğinin anlatısı. Köşeli parantez içinde günlük
girdi kimliklerine satır içi atıf yap. Hesaplar çeliştiğinde çelişkiyi
doğrudan sun — üstünü örtme. Belgesel kanıt önemliyse alıntılarla sunulur.]

### Konu 2: [İddia]

[Aynı yapı]

[Her konu için devam et]

---

## Güvenilirlik Değerlendirmesi

*[Bağımsız bölüm. Yalnızca güvenilirliği belirleyici olan tanıkları ele al —
yani bir konudaki bulgunun hangi hesabın kabul edildiğine bağlı olduğu
durumlar.]*

### [Tanık adı/rolü]

**İç tutarlılık:** [Tutarlı / Tutarsız — ayrıntıları belirt]
**Doğrulama:** [Hangi belgesel veya başka kanıt hesabı doğruluyor veya
zayıflatıyor]
**Motif:** [Hesaba güvenmek veya güvenmemek için herhangi bir neden]
**Tavır:** [Görüşmeler yüz yüzeyse avukatın gözlemleri — geçerli değilse
veya gözlemlenmediyse boş bırakın]
**Değerlendirme:** [Kabul et / Kabul etme / Kısmen kabul et — dayanağıyla]

---

## İlgili Politikalar

[İddia edilen davranış zamanında yürürlükte olan ve konularla ilgili
politikalar. Sürümü atıf yap. Davranıştan sonra kabul edilen politikalara
atıf yapma.]

---

## Sonuçlar

| Konu | Bulgu | Dayanak |
|---|---|---|
| [Konu 1] | Sabit / Sabit Değil / Sonuçsuz | [Tek cümle] |
| [Konu 2] | ... | ... |

*Bulgular, delillerin üstünlüğü (preponderance) standardına dayanır.*

---

## Öneriler

[Eylem türüne göre düzenlenmiş:]

**Disiplin eylemi:** [Varsa — yalnızca sonucu değil, dayanağını belirt]
**Politika veya süreç değişiklikleri:** [Politikalarda bir boşluk katkıda
bulunduysa]
**Eğitim:** [Belirtilmişse]
**Daha fazla soruşturma:** [Tam çözülmemiş herhangi bir konu]
**İzleme:** [Gereken herhangi bir takip]

---

## Ek A: Olaylar Kronolojisi

[olay_tarihi'ne göre sıralanmış günlük girdilerinden otomatik oluşturulur,
gunluklenme_tarihi'ne göre değil. Format: Tarih | Özet | Kaynak (Girdi Kimliği)]

## Ek B: İncelenen Belgeler

[incelenen-belgeler.yaml'dan özet tablosu]
```

Taslağı
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/sorusturma-[slug]/not.md`
dosyasına yaz.

### Not zaten varsa — güncelleme

Notu ve günlüğü oku. Not son taslaklandığından beri eklenen günlük
girdilerini tespit et (gunluklenme_tarihi'ni notun son güncelleme
tarihiyle karşılaştır).

Neyin değiştiğini bildir:

```
Son not taslağından ([tarih]) bu yana günlüğe şunlar eklendi:

[N] yeni girdi
Yeni konular: [varsa]
Yeni çelişkiler: [varsa]
Çözülen boşluklar: [varsa]

Güncellenmesi gereken bölümler:
  Olgusal bulgular: [hangi konular etkileniyor]
  Güvenilirlik: [herhangi bir yeni güvenilirlikle ilgili girdi]
  Sonuçlar: [yeniden gözden geçirilmesi gereken herhangi bir bulgu]
  Ek A: [N] yeni kronoloji girdisi
```

Sor: "Tüm notu mu güncellememi istersin, yoksa yalnızca etkilenen
bölümleri mi?"

Güncellemeleri uygula. Önceki taslaklamayı koru. Avukat gözden geçirene
kadar değişen bölümleri `[GÜNCELLENDİ: tarih]` ile işaretle.

---

## Mod 5: Hedef kitle özeti taslakla

`/is-hukuku:sorusturma-ozeti` veya "[hedef kitle] için bir özet taslakla"
ile tetiklenir.

Sor: hedef kitle kim ve bu özet hangi karar veya eylemi destekliyor?

**İK özeti** (disiplin eylemi konusunda İK kararı için):
- Ne oldu (olgusal özet, hukuki analiz yok)
- Her iddiadaki bulgu (Sabit/Sabit Değil/Sonuçsuz)
- Önerilen eylem
- Bu özette OLMAYAN: meslek sırrı analizi, güvenilirlik metodolojisi, hukuki
  risk değerlendirmesi, avukatın zihinsel izlenimleri
- Başlık: "Gizli — Yalnızca İK Kullanımı İçin — Dağıtılmaz"
- Girdi kimlikleri veya belge atıfları içerme — bunlar notta kalır

**Yönetim/Yönetim Kurulu özeti** (yönetişim kararı için):
- İddia ve kapsam tek paragrafta
- Anahtar bulgular
- İş etkisi / maruziyet (üst düzey — spesifik hukuki analiz yok)
- Şirketin bu konuda ne yaptığı
- Başlık: "[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırması ## Çıktılar'a göre —
  role göre değişir; bkz. `## Bunu kim kullanıyor`]"

**Dış avukat brifingi** (dava veya daha derin inceleme için devir):
- Hukuki maruziyet analizi dahil tam bağlam
- Açık kanıtsal iplikler
- Hâlâ tartışmalı olan güvenilirlik konuları
- Davada en önemli olacak belgeler
- Başlık: "[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırması ## Çıktılar'a göre —
  role göre değişir; bkz. `## Bunu kim kullanıyor`]"

---

## Sonuç doğuran eylem kapısı (bir talebe veya şikayete cevap verme)

**Bir özet, not veya dış bir cevap için amaçlanan içerik üretmeden önce
(idari başvuru/İŞKUR/Çalışma Bakanlığı cevabı, karşı taraf avukatının
ihtarnamesine cevap, düzenleyici cevabı veya herhangi bir resmi şikayet
yanıtı):** `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
dosyasındaki `## Bunu kim kullanıyor` bölümünü oku. Rol **Avukat olmayan**
ise:

> Bir talebe, başvuruya veya şikayete cevap vermenin hukuki sonuçları vardır
> — burada alınan pozisyonlar sonraki süreçlerde ikrar niteliğinde olabilir,
> savunmalardan feragat kazara olabilir ve altta yatan soruşturma üzerindeki
> meslek sırrı kaybedilebilir. Bu cevabı bir avukatla gözden geçirdiniz mi?
> Evetse devam edin. Hayırsa, onlara götürecek bir brifing:
>
> - İddia, forum ve son tarih
> - Soruşturmanın ne ortaya çıkardığı (iddiaya göre bulgular; incelenen
>   belgeler; görüşülen tanıklar; şirketi-temsil-eder-uyarısı verildi mi
>   verilmedi mi)
> - Çözülmemiş herhangi bir kanıtsal iplik veya güvenilirlik tartışması
> - Önerilen cevabın ne dediği ve zımnen neyi kabul ettiği
> - Açık sorular ve neyin çözülmediği
> - Neyin ters gidebileceği (meslek sırrı feragati, tutarsız olgusal
>   beyanlar, kaçırılmış bir savunma)
> - Avukata ne sorulacağı (bu doğru teori mi; savunmaları koruyor muyuz;
>   dış bir büro bunu devralmalı mı; neyin gizlenmesi veya bir meslek sırrı
>   günlüğü gerektiği)
>
> Bir avukat bulmanız gerekiyorsa: ilgili baroya danışın — baro tarafından
> sunulan avukatlık asgari ücret tarifesi ve avukat yönlendirme hizmetleri
> mevcuttur. İdari başvuru ve ihtarname cevapları, eğitimsiz cevapların
> genellikle altta yatan iddiadan daha fazla maruziyet yarattığı bir
> alandır.

Bu kapının ötesine açık bir "evet" olmadan dış-cevap taslağı üretme. Yalnızca
organizasyon içinde kullanılan iç notlar, İK özetleri ve yönetim brifingleri
bu kapıyı tetiklemez (ama bu skill'in en üstündeki meslek sırrı oluşum
çekincesi hâlâ geçerlidir).

---

## Bu skill'in YAPMADIKLARI

- Disiplin kararları vermek — avukatın bulgularını destekler, İK'nın
  eylemini değil
- Meslek sırrını garanti etmek — meslek sırrı notun nasıl etiketlendiğine
  değil, soruşturmanın nasıl yapılandırıldığına bağlıdır
- Okuyamadığı belgeleri işlemek — dosyalar ayrıştırılamayan formatlardaysa,
  elle inceleme için işaretle
- Görüşme yapmak — görüşme notlarını günlükler, tanıkları görüşmez
- Şirketi-temsil-eder-uyarısının yerini almak — verilip verilmediğini
  takip eder, kendisi vermez

## Sonraki adımlar karar ağacıyla kapat

CLAUDE.md `## Çıktılar` başına sonraki adımlar karar ağacıyla kapat. Seçenekleri
bu skill'in az önce ürettiği şeye göre özelleştir — beş varsayılan dal (X'i
taslakla, eskale et, daha çok olgu topla, izle ve bekle, başka bir şey) bir
başlangıç noktasıdır, bir kilitlenme değil. Ağaç çıktının kendisidir, avukat
seçer.
