---
name: gizlilik-inceleme
description: >
  Referans: gelen gizlilik sözleşmelerinin (NDA) hızlı YEŞİL / SARI / KIRMIZI
  triyajı, böylece ekip hukuk zamanını yalnızca ihtiyacı olanlara harcar. Satış ve
  iş geliştirmenin hukuka sormadan önce kendi kendine kullanması için kurulmuştur.
  Bir NDA tespit edildiğinde /ticari-hukuk:sozlesme-inceleme tarafından yüklenir.
user-invocable: false
---

# NDA (Gizlilik Sözleşmesi) İncelemesi

## Dosya bağlamı

**Dosya bağlamı.** Pratik düzeyi CLAUDE.md'deki `## Dosya çalışma alanları`nı kontrol
et. `Etkin` `✗` ise (şirket-içi kullanıcılar için varsayılan), bu paragrafın geri
kalanını atla — skill'ler pratik düzeyi bağlamı kullanır ve dosya makinesi görünmez.
Etkinse ve aktif bir dosya yoksa sor: "Bu hangi dosya için? `/ticari-hukuk:dosya-
calisma-alani gecis <slug>` çalıştırın ya da `pratik-duzeyi` deyin." Aktif dosyanın
`matter.md`'sini dosyaya özgü bağlam ve geçersizlemeler için yükle. Çıktıları dosya
klasörüne yaz:
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/matters/<dosya-slug>/`.
`Çapraz-dosya bağlamı` `açık` olmadıkça başka bir dosyanın dosyalarını asla okuma.

---

## Hedef kontrolü

Çıktı üretmeden önce nereye gittiğini kontrol et. Kullanıcı bir hedef adlandırdıysa
(bir kanal, dağıtım listesi, karşı taraf, "herkes"), meslek sırrı çemberinin içinde
olup olmadığını sor. Herkese açık kanallar, şirket geneli listeler, karşı taraf/karşı
vekil, tedarikçiler ve (iş ürünü için) müvekkiller korumayı kaldırır. Hedef çemberin
dışında görünüyorsa işaretle ve (a) yalnızca hukuk için gizli sürüm, (b) daha geniş
kanal için arındırılmış sürüm, veya (c) ikisini de öner — sessizce gizli bir başlık
uygulayıp sonra başlığın koruyamayacağı bir yere yapıştırmaya yardım etme. Bu
eklentinin CLAUDE.md'sindeki kanonik `## Paylaşılan guardrail'lar → Hedef kontrolü`
bölümüne bak.

## Amaç

Gelen NDA'ların çoğu iyidir. Birkaçının mayınları vardır. Bu skill onları bir
dakikanın altında sıralar, böylece hukuk yalnızca önemli olanları okur.

**Amaç:** YEŞİL bir NDA imzadan başka hiçbir şeye ihtiyaç duymamalı. SARI, belirli
bir veya iki şey üzerinde bir avukatın gözüne ihtiyaç duyar. KIRMIZI, kimse zaman
kaybetmeden durur.

## Önce oyun kitabını yükle

**Hangi taraf?** Oyun kitabını uygulamadan önce, bu NDA için şirketin hangi tarafta
olduğunu belirle. Genellikle bağlamdan bellidir: karşı taraf ürününüzü değerlendiren
bir satıcı veya ortaksa satış-tarafındasınız; onlarınkini değerlendiriyorsanız
satın alma-tarafındasınız. Karşılıklı NDA'ların yine de bir tarafı vardır — kağıt
kimin, değerlendirme hangi yönde işliyor. Belli değilse sor. Eşleşen oyun kitabı
bölümünü (`### Satış-tarafı oyun kitabı` veya `### Satın alma-tarafı oyun kitabı`)
yapılandırmadan oku. Çıktıda hangi tarafın uygulandığını not et. Eşleşen taraf
`[Yapılandırılmadı]` ise, dur ve kullanıcıya bu triyaj devam edebilmeden önce
`/ticari-hukuk:ilk-kurulum --side <taraf>` çalıştırmasını söyle.

**Herhangi bir şeyi triyaj etmeden önce
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` →
`## Oyun Kitabı` → eşleşen taraf → `NDA triyaj pozisyonları`'nı oku.** O bölüm, bu
ekip için *bu tarafta* neyin bir NDA'yı YEŞİL, SARI veya KIRMIZI yaptığının gerçek
kaynağıdır. Bu skill NDA şartları üzerinde varsayılan pozisyonlarla gelmez — hukuk,
piyasa ve her ekibin risk toleransı sabit-kodlanmış varsayılanları güvensiz kılacak
kadar değişir.

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` henüz bir
`NDA triyaj pozisyonları` bölümüne sahip değilse, veya incelediğiniz NDA'da ortaya
çıkan bir şart hakkında sessizse, kullanıcıya sor:

> Oyun kitabınız [şart — ör. "kalıntı bilgi (residuals) maddeleri," "hayatta kalma
> süresi," "alıcı olduğunuz tek yönlü NDA'lar"]'ı kapsamıyor. Varsayılan pozisyonunuz
> ne — bu ne zaman YEŞİL, ne zaman SARI, ne zaman KIRMIZI olmalı? Bir sonraki
> inceleme tutarlı olsun diye
> `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye
> eklerim.

Sonra cevabı
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye
kaydet ve yeni pozisyonu kullanarak triyaja devam et.

## Kapsam kontrolü

**NDA'ya özgü hükümleri incelemeden önce, belgenin adının önerdiğinden fazlasını
yapıp yapmadığını kontrol et.** Karşılıklı ticari NDA'lar şunları gizleyebilir:
standstill (bekleme yükümlülüğü), lisans devri, münhasırlık, çalışan/müşteri
devşirmeme, fikri mülkiyet devri, ilk red hakkı, en çok kayrılan müşteri (MFN)
maddeleri ve gizlilik uyuşmazlıklarından çok daha fazlasını yöneten tahkim/yetki
maddeleri.

NDA gizlilik dışında yükümlülükler içeriyorsa: **madde-analizinden bağımsız olarak
otomatik SARI.** NDA-dışı hükümleri işaretle:

> Bu belge bir NDA olarak etiketlenmiş ama [bekleme yükümlülüğü / lisans devri /
> devşirmeme / münhasırlık / fikri mülkiyet devri / ilk red hakkı / MFN / geniş
> tahkim] içeriyor. Bir NDA'dan fazlası. Avukat incelemesine yönlendirin.

Esaslı yükümlülükler bir hizmet sözleşmesi, bir niyet mektubu veya bir taahhüt
paketi olduğunda "NDA" etiketli bir belgeyi sessizce NDA triyajından geçirme.

## Triyaj

NDA'yı,
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
pozisyonlarını uygulayarak üç kovadan birine sınıflandır. Kova tanımları aşağıda
sabittir; her kovayı dolduran *ölçütler* oyun kitabından gelir.

### YEŞİL — imzaya yönlendir

NDA ekibin oyun kitabındaki her pozisyonu karşılıyor ve hiçbir şart oyun kitabına
göre bir KIRMIZI bayrak tetiklemiyor. Oyun kitabının tipik olarak kapsadığı
kontrollere örnekler: karşılıklılık, süre uzunluğu, hayatta kalma süresi, istisnalar,
uygulanacak hukuk, kısıtlayıcı taahhütler, avukatlık ücreti aktarımı. YEŞİL demeden
önce her birini
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye karşı
teyit edin.

**YEŞİL, avukat tarafından incelenmiş oyun kitabı pozisyonları gerektirir.** YEŞİL,
avukat incelemesi olmadan imzaya giden tek yoldur. Varsayılan veya eksik
pozisyonlara karşı verilemez. YEŞİL vermeden önce kontrol edin: pratik profilinde
avukat tarafından incelenmiş bir `## NDA triyaj pozisyonları` bölümü var mı? Yoksa:

> Pratik profilinizde avukat tarafından incelenmiş NDA pozisyonları olmadan YEŞİL
> veremem. Pozisyonları ayarlamak için ticari hukuk müşavirinizle
> `/ticari-hukuk:ilk-kurulum --full` çalıştırın, ya da bu NDA'yı avukat incelemesine
> yönlendirin. Varsayılanlara karşı YEŞİL vermek, bir hukukçu olmayanın bir sonraki
> hukukçu olmayanın güveneceği pozisyonları belirlediği anlamına gelir.

Varsayılanlarda imzaya yönlendirme. Pozisyonlar eksikken doğru çağrı SARI'dır — bunu
kararı verebilecek bir insana yüzeye çıkarır.

**Çıktı:**

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
`## Çıktılar`'dan iş-ürünü başlığını ekle (role göre farklılaşır — bkz. `## Bunu
kim kullanıyor`).

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar]

## NDA Triyajı: [Karşı taraf]

YEŞİL — imzaya yönlendir

### Yönetici Özeti

Oyun kitabına göre kırmızı bayrak tespit edilmedi. Standart sürece göre imzaya
yönlendirin.

| Kontrol | Durum | Oyun kitabı referansı |
|---|---|---|
| [Her oyun kitabı kontrolü] | [geçti/kaldı] | [`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` bölümü] |

**Sonraki adım:** [CLM'nin standart NDA iş akışına gönder | İmza için
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
onaylayıcıya gönder]
```

**YEŞİL'den imzaya geçmeden önce:**
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
içindeki `## Bunu kim kullanıyor`'u oku. Rol Avukat değilse:

> Bu adımın hukuki sonuçları var (bir NDA'yı karşı-imzalamak şirketi bağlar). Bunu
> bir avukatla gözden geçirdiniz mi? Evetse, devam edin. Hayırsa, onlara getirmeniz
> için bir brifing:
>
> [1 sayfalık özet üret: karşı taraf, NDA yönü (karşılıklı / tek yönlü), çalıştırılan
> oyun kitabı kontrolleri, oyun kitabının kapsamadığı herhangi bir şey, olduğu gibi
> imzalanırsa neyin ters gidebileceği, ve avukata sorulacak üç şey.]
>
> Bir avukat bulmanız gerekirse: bağlı olduğunuz baroya başvurun.
> `[doğrulanacak — TR baro yönlendirme mekanizmaları]`

Açık bir evet olmadan bu kapıdan geçme.

### SARI — bir avukatın gözünü spesifik kalemlere gerektirir

Bir veya daha fazla şart oyun kitabından sapıyor ama kategorik anlaşma bozucular
değil, YA DA oyun kitabının ele almadığı bir şart ortaya çıkıyor. Onaylayıcının
çağrıyı yapabilmesi için her kalemi ayrı ayrı yüzeye çıkar.

**Çıktı:**

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
`## Çıktılar`'dan iş-ürünü başlığını ekle (role göre farklılaşır — bkz. `## Bunu
kim kullanıyor`).

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar]

## NDA Triyajı: [Karşı taraf]

SARI — [`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
onaylayıcı isim] için işaretle

### Yönetici Özeti

- [Tek satır uygulanabilir düzenleme, ör. "Devşirmeme maddesini çıkar (Bölüm 6)"]
- [Tek satır uygulanabilir düzenleme]

### İşaretlenen kalemler

**1. [Sorun]** — Bölüm [X]
   Ne: [tek satır]
   Neden işaretlendi: [tek satır — hangi oyun kitabı pozisyonuna çarpıyor, veya
   "oyun kitabı bu konuda sessiz"]
   **Hukuki risk:** [🔴/🟠/🟡/🟢] | **Ticari sürtünme:** [🔴 Anlaşmayı engeller / 🟠
   Anlaşmayı yavaşlatır / 🟡 Müşteriyi kafa karıştırır / 🟢 Görünmez]
   Muhtemel çözüm: [kabul et / X üzerinde geri it / anlaşma bağlamına bağlı]

[her bayrak için tekrarla]

### Geri kalan her şey

| Kontrol | Durum | Oyun kitabı referansı |
|---|---|---|
| [geçen oyun kitabı kontrolleri] | geçti | [`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` bölümü] |

**Sonraki adım:** İşaretlenen kalemler hakkında [onaylayıcı]ya sorun, sonra sorunu
yoksa imzaya yönlendirin.
```

### KIRMIZI — dur, önce hukukla konuş

NDA oyun kitabının "asla kabul etme" listesindeki bir pozisyona çarpıyor, veya
sözleşmenin yapısı ekibin standart duruşuyla uyumsuz (ör. oyun kitabı karşılıklı
gerektirirken tek yönlü bir NDA; oyun kitabı sonlu bir süreyle sınırlarken süresiz
bir süre; "asla" listesindeki uygulanacak hukuk).

**Çıktı:**

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
`## Çıktılar`'dan iş-ürünü başlığını ekle (role göre farklılaşır — bkz. `## Bunu
kim kullanıyor`).

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar]

## NDA Triyajı: [Karşı taraf]

KIRMIZI — önce hukukla konuşmadan gönderme

### Yönetici Özeti

- [Tek satır uygulanabilir düzenleme, ör. "Bölüm 4 — inceleme için Hukuk'a yönlendir"]
- [Tek satır uygulanabilir düzenleme]

### Kritik sorunlar

**1. [Sorun]** — Bölüm [X]
   > "[tam alıntı]"
   Neden bu bir sorun: [spesifik risk; ihlal ettiği oyun kitabı pozisyonunu
   alıntıla]
   **Hukuki risk:** [🔴/🟠/🟡/🟢] | **Ticari sürtünme:** [🔴 Anlaşmayı engeller / 🟠
   Anlaşmayı yavaşlatır / 🟡 Müşteriyi kafa karıştırır / 🟢 Görünmez]
   Önerilen yanıt: [kendi kağıdımızı kullan | spesifik dille geri it | vazgeç]

**Sonraki adım:** Bu triyajı
[`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den BHM
veya adlandırılmış eskalasyon kişisi]'ne gönderin. [CLM veya onay iş akışına]
göndermeyin. Karşı tarafa imzalayacağımızı söylemeyin.
```

## Redline ayrıntı düzeyi

**Mümkün olan en küçük ayrıntı düzeyinde düzenle.** Bir redline bir müzakere
aracıdır, bir yeniden yazma değil. Toptan madde değişimi "senin taslağını çöpe
attık" sinyali verir — saldırgandır, karşı tarafı tüm maddeyi yeniden okumaya
zorlar ve iyi olan taslak kısımlarını atar. Cerrahi redline'lar — bir kelimeyi çiz,
bir ifade ekle, bir alt maddeyi yeniden yapılandır — "spesifik isteklerimiz var"
sinyali verir ve okuması, anlaşılması, kabul edilmesi daha hızlıdır.

Oyun kitabı pozisyonunu sağlayan en küçük düzenlemeyi varsayılan yap:
- Bir **ifadeden** önce bir **kelimeyi** değiştir. ("on iki (12)" → "yirmi dört (24)")
- Bir **cümleden** önce bir **ifadeyi** değiştir. ("Alıcı tarafından ödenen" →
  "Alıcı tarafından ödenen ve ödenmesi gereken")
- Cümleyi değiştirmeden önce bir **alt maddeyi** yeniden yapılandır. (Bileşik bir
  koşulu bölmek için "(a)" ve "(b)" ekle.)
- Maddeyi değiştirmeden önce bir **cümleyi** değiştir.
- Yalnızca karşı tarafın versiyonu pozisyonunuzdan o kadar uzaksa ve cerrahi
  düzenlemeler taze bir taslaktan daha okunması zor olacaksa bir **tüm maddeyi**
  değiştir — ve bunu yaptığınızda iletide söyleyin: "§8.2'yi işaretlemek yerine
  değiştirdik çünkü değişiklikler kapsamlıydı. Farkı sizinle gözden geçirmekten
  memnuniyet duyarız."

Şüphedeyken, daha küçük. Cerrahi bir redline alan bir müvekkil dikkatlice
okuduğunuza güvenir. Toptan bir değişim alan bir müvekkil gerçekten okuyup
okumadığınızı merak eder.

## Yargı çevresi varsayımı

Bu triyaj,
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'de
kaydedilen uygulanacak-hukuk ve kısıtlayıcı-taahhüt pozisyonlarını uygular. Hukuki
kurallar (devşirmeme, rekabet yasağı maddelerinin uygulanabilirliği, ücret aktarımı,
hukuk seçimi) yargı çevresine göre önemli ölçüde değişir. NDA ekibin yapılandırılmış
duruşu dışında bir yargı çevresi içeriyorsa, çıktıda işaretle ve triyajın yazıldığı
gibi aktarılmayabileceğini not et.

## Çıktı kuralları

**Karmaşıklık filtresi:** Bir sorunu ele almak yeni dil taslaklamak, bir maddeyi
yeniden yapılandırmak veya esaslı yeni hükümler eklemek gerektirirse — bunu deneme.
Bunun yerine yaz: "Bölüm [X] — inceleme için Hukuk'a yönlendir." Yönetici Özetine
yalnızca basit, mekanik eylemleri (çiz, sil, bir kelime veya ifadeyi değiştir) dahil
et.

**Temiz NDA kuralı:** NDA hiçbir bayrak olmadan tüm kontrolleri geçerse, Yönetici
Özeti yalnızca şunu söylemeli: "Kırmızı bayrak tespit edilmedi. Standart sürece göre
imzaya yönlendirin."

Temiz bir NDA için uzun bir rapor üretme.

## Ayrıntılı kontrol referansı

Aşağıdaki her kontrol için, kova (YEŞİL/SARI/KIRMIZI)
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
tarafından belirlenir. Bu skill *kategorileri* listeler; eşikleri sabit kodlamaz.

### Karşılıklılık

NDA karşılıklı mı yoksa tek yönlü mü?
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
ekibin pozisyonunu uygulayın. Oyun kitabı bu bağlamda tek yönlü NDA'ları ele
almıyorsa, aşağıdaki tek-yönlü anketini çalıştırın ve sonucu bir insan için yüzeye
çıkarın.

**Tek-yönlü NDA anketi**

NDA tek taraflı olduğunda (bir taraf açıklar, diğeri yalnızca alır), hemen KIRMIZI
işaretlemeyin veya çıkmayın. Sorun:

> Tek yönlü bir NDA bazı durumlarda uygundur. Bunu işaretlemeden önce, birkaç hızlı
> soru sorayım:
>
> 1. Bu ilişkide, gizli bilgiyi açıklayan yalnızca siz misiniz? (yani karşı taraf
>    hiçbir şeyi geri paylaşmıyor)
> 2. Bu sınırlı, spesifik bir ifşa için mi — örneğin teknolojinizi üzerinde
>    çalışacak bir tedarikçiyle paylaşmak, ama onlarınkini sizinle paylaşmamak?
> 3. Bu birleşme/devralma, istihdam veya yatırımla mı ilgili? (Evetse, durun —
>    bu skill yalnızca ticari karşılıklı NDA'lar (MNDA) içindir. Hukuka
>    yönlendirin.)

Cevapları
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
pozisyonuyla birlikte YEŞİL/SARI/KIRMIZI'ya karar vermek için kullanın.
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` bu olgu
kalıbında bir pozisyon almıyorsa, SARI işaretle ve anket cevaplarını onaylayıcı için
yüzeye çıkar.

### Gizli Bilginin Tanımı

Kapsamı (yalnızca-işaretli vs. her-şey-ifşa-edilen), işaretleme gereksinimlerini ve
sözlü-ifşa teyit pencerelerini kontrol edin. Ekibin pozisyonunu
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
uygulayın. Oyun kitabı bunlardan herhangi biri konusunda sessizse sorun.

### İstisnalar

Bir NDA'da tipik olarak bulunan beş istisna:

1. Kamuya açık olan veya (ihlal dışında bir yolla) haline gelen bilgi
2. Alıcı tarafın zaten sahip olduğu bilgi
3. Gizli bilgiye referans olmadan bağımsız geliştirilen bilgi
4. Bir üçüncü taraftan kısıtlama olmadan alınan bilgi
5. Kanun veya mahkeme kararıyla ifşası gereken bilgi (yasal olarak izin verilen
   yerlerde açıklayana bildirimle)

Ekibin hangi istisnaları gerektirdiği ve ne kadar sıkı olduğu bir oyun kitabı
sorusudur. Ekibin gereken istisnalar, kabul edilebilir dil varyasyonları ve biri
eksik olduğunda ne olacağı konusundaki pozisyonu için
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'yi
kontrol edin.

### Kalıntı bilgi (residuals)

Bir kalıntı bilgi maddesi, alıcı tarafın yardımsız hafızada tutulan bilgiyi
kullanmasına izin verir. Bunun kabul edilebilir olup olmadığı — ve hangi koşullar
altında (ör. dar "yardımsız hafıza" dili vs. notları veya kopyaları kapsayan daha
geniş kapsam) —
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'yi
uygulayın. Oyun kitabı kalıntıları ele almıyorsa sorun.

### Süre ve hayatta kalma

İlk süre uzunluğunu, gizlilik yükümlülüklerinin süre-sonrası hayatta kalma süresini
ve ticari sırların daha uzun korumayla istisna tutulup tutulmadığını kontrol edin.
Ekibin pozisyonunu
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
uygulayın. Oyun kitabı bunlardan birini kapsamıyorsa sorun.

### Kısıtlayıcı taahhütler

Devşirmeme (çalışan, müşteri), rekabet yasağı, münhasırlık ve alıcı tarafın kiminle
başka çalışabileceğine dair herhangi bir kısıtlama olup olmadığını kontrol edin.
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'yi
uygulayın. Oyun kitabı sessizse sorun — kısıtlayıcı taahhütler yargı çevresine
duyarlıdır ve ekibin duruşu önemlidir.

### Avukatlık ücreti aktarımı

Ücret aktarım hükümlerini ve karşılıklı, tek taraflı mı, yoksa haklı çıkan-taraf mı
olduğunu kontrol edin.
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'yi
uygulayın.

### Yedekleme ve arşiv istisnası

İmha/iade maddesinin standart yedekleme ve arşiv saklama sistemleri için bir
istisna içerip içermediğini kontrol edin. Ekibin pozisyonunu
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
uygulayın — bazı ekipler bu istisnayı gerektirir ve eklemek için iter; diğerleri
onsuz bir NDA'yı kabul eder. Oyun kitabı bunu ele almıyorsa sorun.

### Uygulanacak hukuk

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
`## Oyun Kitabı` → `Uygulanacak hukuk ve yetkili merci`'ye göre.

## Karşı taraf bağlamı

**BigCo NDA'ları:** Büyük, köklü karşı taraflar genellikle NDA'ları müzakere etmez.
Kalibre edin: KIRMIZI bayrak gerçekten bir anlaşma bozucu mu, yoksa "formumuzdan
farklı" mı? İş ilişkisi önemliyse, çağrı onların kağıdını kabul edip etmemektir —
o kararı eskale edin, siz vermeyin.

**Girişim NDA'ları:** Genellikle bizim kağıdımızı alırlar. Onların NDA'sında sorun
varsa, en hızlı yol genellikle "bizimkini kullanalım"dır, onlarınkini işaretlemek
yerine.

## Entegrasyon: CLM

Bağlıysa:
- YEŞİL → CLM kaydını standart NDA iş akışında oluşturmayı öner
- SARI → işaretlenen kalemleri listeleyen bir not ekli olarak oluşturmayı öner
- KIRMIZI → bir kayıt oluşturma; avukat ne olacağına karar verir

## Bu skill'in YAPMADIKLARI

- Müzakere etmez. Sıralar.
- Bir NDA taslaklamaz. Cevap "kendi kağıdımızı kullanalım"sa, kullanıcı formumuzu
  [CLM veya belge sisteminden] çeker.
- SARI kalemler üzerine çağrıyı yapmaz. Bir insan için yüzeye çıkarır.
- Herhangi bir NDA şartı üzerine pozisyon almaz. Pozisyonlar
  `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'de
  yaşar.

## Kapanış eylemi

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` →
`## NDA triyaj tercihleri` → `closing_action`'ı oku.

Yapılandırılmışsa, kapanış eylemini her çıktının sonunda kelimesi kelimesine ekle.
Örnek yapılandırmalar:

```
closing_action: "Bu analizin tam metnini ve NDA'nın bir kopyasını imzalamadan önce
son teyit için hukuk@[sirketiniz].com adresine gönderin."

closing_action: "Standart NDA iş akışını kullanarak [CLM]'ye gönderin. Hukuk
yönlendirmeden önce teyit edecek."

closing_action: "Bu çıktıyı ve NDA'yı sözleşmeler yöneticinize iletin."
```

`closing_action`
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'de
yapılandırılmadıysa, ekle: "Nihai NDA'yı standart onay sürecinizden geçirin."

İlk-kurulum görüşmesi şunu sorar: "Biri bir NDA triyajını bitirdiğinde, çıktıyla ne
yapmasını istersiniz? Bunu her incelemenin sonunda standart bir talimat olarak
ekleyeceğim."

## Sonraki-adımlar karar ağacıyla kapat

CLAUDE.md `## Çıktılar`'a göre sonraki-adımlar karar ağacıyla bitir. Seçenekleri bu
skill'in az önce ürettiğine göre uyarla — beş varsayılan dal (X'i taslakla, eskale
et, daha çok olgu al, izle ve bekle, başka bir şey) bir başlangıç noktasıdır, bir
kilitlenme değil. Ağaç çıktının kendisidir; avukat seçer.
