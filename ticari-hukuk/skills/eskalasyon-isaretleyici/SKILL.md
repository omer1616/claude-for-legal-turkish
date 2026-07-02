---
name: eskalasyon-isaretleyici
description: >
  Bir sözleşme sorununu
  `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
  içindeki eskalasyon matrisine göre doğru onaylayıcıya yönlendirin ve talebi
  taslaklayın. Kullanıcı "bunu kim onaylamalı", "bunu eskale et", "bu BHM onayı
  gerektiriyor mu", "bunu onay için yönlendir" dediğinde veya başka bir skill
  inceleyenin yetkisini aşan bir sorun bulduğunda kullan.
argument-hint: "[sorunu tanımlayın, ya da bir inceleme notuna atıfta bulunun]"
---

# /eskalasyon-isaretleyici

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
eskalasyon matrisine göre bir sözleşme sorunu için onaylayıcıyı adlandırır ve
mesajı taslaklar, böylece akşam 5'te "hey bi dakikan var mı" yazmıyorsunuz.

## Talimatlar

1. **`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
   dosyasını yükle** → Eskalasyon bölümü. Eksikse, söyle — pratik profilinin
   düzenlenmesi gerekiyor.

2. **Sorunu karakterize et:** TL eşiği / şart sapması / otomatik tetikleyici / iş
   kararı.

3. **Matrisle eşleştir, onaylayıcıyı adlandır.** Spesifik ol — bir kişi veya rol,
   "hukuk liderliği" değil.

4. **Talebi taslakla** aşağıdaki şablona göre: sözleşme ne diyor, oyun kitabı ne
   diyor, öneriyle seçenekler, karar-tarihi.

5. **Gönderme.** Taslakla, göster, avukatın göndermesine izin ver.

## Örnekler

```
/ticari-hukuk:eskalasyon-isaretleyici
Acme MSA'sında sınırsız sorumluluk var — kim onaylar ve ne söylerim?
```

```
/ticari-hukuk:eskalasyon-isaretleyici
Referans: acme-inceleme-notu.md
Sorun: §8.2 tazminat istisnaları
```

---

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

## Amaç

Her sözleşmeler ekibinin, yazılı olsun olmasın, bir eskalasyon matrisi vardır. Bu
skill yazılı olanı okur
(`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'de), bir
sözleşme sorununu buna karşı eşleştirir, onaylayıcıyı adlandırır ve talebi
taslaklar, böylece avukat akşam 5'te "hey bi dakikan var mı" mesajları yazmaz.

## Matrisi yükle

**Hangi taraf?** Matrisle eşleştirmeden önce, sorunu eskale edilen sözleşme için
şirketin hangi tarafta olduğunu belirle. Genellikle bellidir: karşı taraf mal veya
hizmet sağlayan bir satıcı/tedarikçiyse, satın alma-tarafındasınızdır. Karşı taraf
ürününüzü/hizmetinizi satın alan bir müşteriyse, satış-tarafındasınızdır. Belli
değilse sor. Şartın yedeklerin içinde mi yoksa otomatik eskalasyonu mu tetiklediğini
değerlendirmek için eşleşen oyun kitabı bölümünü (`### Satış-tarafı oyun kitabı`
veya `### Satın alma-tarafı oyun kitabı`) okuyun — bir tarafta uygun olan bir şart
diğer tarafta kesin bir hayır olabilir. Onaylayıcının hangi oyun kitabının
uygulandığını bilmesi için taslak talepte hangi tarafı not edin.

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` →
`## Eskalasyon`'u oku. Eksikse veya belirsizse, söyleyin — ilk-kurulum görüşmesi
bunu yakalamış olmalıydı, yakalamadıysa pratik profilinin düzenlenmesi gerekiyor.

Beklenen yapı:

| Onaylayabilir | Eşik | Eskale eder | Kanal |
|---|---|---|---|
| Paralegal | Standart şartlar, <500.000 TL | Sorumlu avukat | Slack |
| Sorumlu avukat | Standart-dışı ama yedekler içinde, <5.000.000 TL | BHM | Slack veya e-posta |
| BHM | Geri kalan her şey | CFO/Yönetim Kurulu | Toplantı |

Artı **otomatik eskalasyon tetikleyicileri** — tutardan bağımsız eskale eden şeyler.
Tipik olarak: sınırsız sorumluluk, fikri mülkiyet devri, oyun kitabındaki "asla
kabul etme" listelerindeki herhangi bir şey.

## İş akışı

### Adım 1: Sorunu karakterize et

Eskale edilen ne?

- **TL eşiği:** Sözleşme tutarı birinin onay yetkisini aşıyor
- **Şart sapması:** Bir şart oyun kitabı yedeklerinin dışında — daha kıdemli birinin
  kabul edip etmeyeceğine karar vermesi gerekiyor
- **Otomatik tetikleyici:** Her-zaman-eskale-et kalemlerinden biri mevcut
- **İş kararı:** Bir hukuk çağrısı değil — hukuk liderliğine değil, iş sahibine
  ihtiyaç var

Gerçekte sorunsuz olan şeyleri eskale etmeyin. Şart
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
yedekleri içindeyse, yukarı gitmesine gerek yok.

### Adım 2: Matrisle eşleştir

```
Sorun otomatik bir tetikleyici mi?
  → EVET: [o tetikleyici için adlandırılmış kişiye] eskale et
  → HAYIR: devam et

Sözleşme tutarı inceleyenin eşiğinin üstünde mi?
  → EVET: o tutar düzeyinde yetkisi olana eskale et
  → HAYIR: devam et

Şart sapması tüm belgelenmiş yedeklerin dışında mı?
  → EVET: standart-dışı şartları onaylayabilene eskale et
  → HAYIR: inceleyen onaylayabilir — eskalasyon gerekmez
```

### Adım 3: Onaylayıcıyı adlandır

Spesifik olun. "Hukuk liderliğine eskale et" değil —
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
kişiyi veya rolü adlandırın. Matris bu durum için kimseyi adlandırmıyorsa, söyleyin:
"Eskalasyon matrisi [durumu] kapsamıyor. Bunun kime ait olduğunu [BHM adı]'na
sormanızı öneririm."

### Adım 4: Talebi taslakla

Onaylayıcı yalnızca mesajdan karar verebilmelidir — "sözleşmeyi çıkarayım" olmadan.

```markdown
**Eskale edilen:** [isim]
**Kanal:**
[Slack #kanal / e-posta / toplantı —
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye göre]
**Aciliyet:** [varsa son tarih]

---

Merhaba [isim] —

[Karşı taraf] [sözleşme türü] hakkında çağrınıza ihtiyacım var. [Anlaşma bağlamı
hakkında tek cümle.]

**Sorun:** [Düz Türkçe, tek paragraf. Ne istiyorlar, standardımızın dışında neden,
risk gerçekte ne.]

**Sözleşme diyor ki:**
> "[tam alıntı]"

**Oyun kitabımız diyor ki:** [`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'den
alıntı]

**Seçenekler:**
1. **Kabul et** — [bunun neden uygun olabileceği hakkında tek satır]
2. **Şununla geri it:** "[önerilen karşı dil]" — [muhtemel karşı taraf tepkisi
   hakkında tek satır]
3. **Vazgeç** — [iş bağlamı verildiğinde bunun gerçekçi olup olmadığı hakkında tek
   satır]

**Önerim:** [hangi seçenek ve kısaca neden]

**Karar gereken tarih:** [tarih, varsa]

[Tam inceleme notuna bağlantı]
```

### Adım 5: Eskalasyonu kaydet

Bu ekip bir bilet sistemi veya CLM onay iş akışları kullanıyorsa, kaydedin. Değilse,
inceleme notunda eskalasyonun gönderildiğini, kime ve ne zaman olduğunu not edin. Notu
okuyan bir sonraki kişi durumu görmeli.

## Kalibrasyon: şüphedeyken, bir notla eskale et

Gereksiz bir eskalasyonun maliyeti, onaylayıcının ~30 saniyelik zamanıdır — okur,
"tamam, devam et" der, ve kayıt gördüklerini gösterir. Kaçırılan bir eskalasyonun
maliyeti onaylanmamış bir şartı imzalamaktır, ki bu tek yönlü bir kapıdır. Maliyetler
simetrik değildir. **Şüphedeyken, eskale edin.**

Neyin eskalasyonu hak ettiğine dair kalibrasyon
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'de yaşar,
bu skill'de değil. Oyun kitabının beyan edilen pozisyonunu, yedeklerini ve
"tutardan bağımsız otomatik eskalasyon" listesini kontrol edin:

- **Açıkça yedek aralığının içinde:** eskalasyon gerekmez.
- **Açıkça aralığın dışında, veya otomatik-eskalasyon listesinde:** eskale edin.
- **Belirsiz — şart belirsiz, yeni, ya da tartışmalı bir şekilde aralığın içinde ama
  argüman zorlama:** yine de eskale edin ve belirsizliği açıkça not edin. Taslak,
  onaylayıcının karar vermesi gereken spesifik soruyu ve skill'in bunu neden
  güvenle yedek aralığının içine yerleştiremediğini işaretler. Onaylayıcı daraltır;
  skill daraltmaz.

Aşırı-eskalasyon onaylayıcıları göz gezdirmeye eğitebilir diye bir eskalasyonu
bastırmayın. Bu, avukatın oyun kitabındaki eşikleri ayarlayarak çözdüğü bir
onaylayıcı-deneyimi sorunudur, skill'in emin olmadığı bir şart üzerine kendi öznel
çağrısını yaparak çözdüğü bir sorun değil.

Oyun kitabının ele almadığı bir şart geldiğinde, eşiği tahmin etmeyin — inceleyen
avukata bu sınıf sorunun eskale edip etmemesi gerektiğini sorun ve cevabı
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye
kaydetmeyi önerin, böylece gelecekteki incelemeler tutarlı olsun.

## Bu skill'in yapmadıkları

- Hiçbir şeyi onaylamaz. Yönlendirir.
- Seçenekler arasında karar vermez. Taslak bir öneri içerir ama onaylayıcı karar
  verir.
- Eskalasyon mesajını göndermez — taslaklar. Avukat okuduktan sonra gönderir.
