---
name: ise-alim-inceleme
description: >
  Bir teklif mektubunu ve herhangi bir rekabet yasağı hükmünü inceler —
  yargı çevresi kontrolü dahil. Esaslı kurallar (rekabet yasağı geçerliliği,
  ilan/bildirim gereksinimleri, sınıflandırma ölçütleri) her işe alım için
  araştırılır, saklanmaz. Kullanıcı "bu teklifi incele", "burada rekabet
  yasağı kullanabilir miyiz", "bu teklif mektubunu kontrol et", "[ülke/şehir]de
  işe alım" dediğinde veya bir teklif eklediğinde kullan.
argument-hint: "[teklif mektubu dosyası, veya işe alımı tanımlayın]"
---

# /ise-alim-inceleme

1. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
   dosyasını yükle → yargı çevresi ayak izi, işe alım inceleme tetikleyicileri,
   rekabet yasağı politikası.
2. Aşağıdaki iş akışını kullan.
3. Kontrol et: yargı çevresi, sınıflandırma, rekabet yasağı hükümleri, arka
   plan kontrolü uyumu.
4. Yargı çevresine özgü eskalasyon tablosuna çarpan herhangi bir şeyi
   işaretle.

---

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

Teklif mektupları, öyle olmayana kadar çoğunlukla standart metindir. Yargı
çevresi kontrolü ve rekabet yasağı kontrolü bu skill'in değer kattığı
yerlerdir. Skill hukuku kendisi ifade etmez — her yargı çevresine özgü
kural inceleme anında araştırılır ve atıf yapılır.

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` →
yargı çevresi ayak izi, işe alım inceleme tetikleyicileri, rekabet yasağı
politikası, teklif mektubu şablonu konumu.

## Çıktı başlığı

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` →
`## Çıktılar` bölümündeki iş-ürünü başlığını ekle (kullanıcı rolüne göre
değişir — bkz. `## Bunu kim kullanıyor`).

## İş akışı

### Adım 1: Yargı çevresi

Bu kişi nerede çalışacak? Merkezin nerede olduğu değil — *onların* nerede
olduğu.

Uzaktansa: kendi ikamet yeri/ülkesi geçerlidir. Hibritse: genellikle ikamet
yeri, ama teklif mektubunun uygulanacak hukuk maddesini kontrol edin (geçerli
olabilir de olmayabilir de).

Bu ülke/bölge için
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
dosyasındaki yargı çevresi tablosunu kontrol edin. Tabloda değilse — yeni
yargı çevresi — işaretleyin: "İlk [ülke] işe alımı. Yargı çevresi tablosu
bunu kapsamıyor. Teklif çıkmadan önce araştırma gerekiyor."

### Adım 2: Sınıflandırma ve çalışma süresi rejimi 🅱️ bağlantılı

*Bu adım kısmen B kademesindeki `ucret-saat-sss` ve `calisan-siniflandirma`
skill'lerine bağlıdır (henüz taşınmadı — bkz. `.claude/MIGRATION.md`).
Skill taşınana kadar bu adımı araştırma bağlayıcısı veya `[doğrulanacak]`
etiketiyle çalıştırın.*

Rol fazla mesaiden muaf mı değil mi? 4857 sayılı Kanun'da ABD'deki
"exempt/non-exempt" ayrımına birebir karşılık gelen bir kavram yoktur;
en yakın konu **üst düzey yönetici** pozisyonlarının çalışma süresi
denetimi kapsamı dışında sayılıp sayılmayacağıdır `[doğrulanacak]`.

| Test | Kontrol |
|---|---|
| Görev tanımı | Rol gerçekten yönetsel/temsil yetkisi kullanımını mı içeriyor? |
| Çalışma süresi denetimi | Rol, işverenin çalışma süresini fiilen denetleyip denetlemediğinden bağımsız mı? |
| Ücret yapısı | Sabit aylık ücret mi, saat başı mı? |

> **Çağırmadan önce araştırın.** Rol için geçerli olan güncel çalışma süresi
> rejimini (4857 m.63-69, varsa toplu iş sözleşmesi hükümleri) tespit edin.
> Birincil kaynaklara atıf yapın. Güncelliği doğrulayın.

Teklif "yönetici muafiyeti" diyor ama rol tanımı bunu desteklemiyorsa —
işaretleyin. Yanlış sınıflandırma maliyetlidir.

### Adım 3: Rekabet yasağı ve gizlilik hükümleri

Teklif bir rekabet yasağı, müşteri/çalışan ayartmama veya
gizlilik/fikri mülkiyet devri hükmü içeriyorsa:

> **Tavsiye vermeden önce uygulanabilirliği araştırın.** Çalışanın yargı
> çevresi için, tekliften geçen her rekabet sınırlamasına ilişkin şu an
> yürürlükte olan kuralları tespit edin. TR hukukunda rekabet yasağı TBK
> m.444-447 kapsamında düzenlenir; süre (azami 2 yıl), coğrafi kapsam ve
> konu bakımından makullük denetimine tabidir ve **tazminat karşılığı
> şart değildir** ancak orantısız sınırlamalar kısmen veya tamamen geçersiz
> sayılabilir `[doğrulanacak]`. Not edin:
> - Hükmün spesifik türü (rekabet yasağı, müşteri ayartmama, çalışan
>   ayartmama, gizlilik/ticari sır, fikri mülkiyet devri) — her birinin
>   kendi kuralları vardır.
> - Süre ve coğrafi kapsam makullük eşiği.
> - Sektöre özgü istisnalar (varsa).
> - Yurt dışı işe alımlarda uygulanacak hukuk ve yetkili merci
>   geçerliliği.
> Birincil kaynaklara atıf yapın. Güncelliği doğrulayın.

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
dosyasındaki rekabet yasağı politikasına göre: bu işe alım hiç böyle bir
hüküm alıyor mu? Bazı şirketler bunları seçici olarak kullanır. Önce ev
politikasını uygulayın, sonra yargı çevresinden gelen araştırma katmanlarını
ekleyin.

> **Sessiz tamamlama yok.** Yapılandırılmış hukuki araştırma aracına bir
> sorgu, yargı çevresinin muafiyet eşikleri, rekabet yasağı kuralları
> veya araştırdığınız başka herhangi bir kalem için az veya hiç sonuç
> döndürmüyorsa, bulunanı bildirin ve durun. Boşluğu web aramasından veya
> model bilgisinden sormadan doldurmayın. Söyleyin: "Arama [araç]'tan [N]
> sonuç döndürdü. [Yargı çevresi / konu] için kapsam yetersiz görünüyor.
> Seçenekler: (1) arama sorgusunu genişlet, (2) farklı bir araştırma aracı
> dene, (3) web'de ara — sonuçlar `[web araması — doğrula]` ile
> etiketlenir ve güvenmeden önce birincil kaynağa karşı kontrol edilmeli,
> veya (4) doğrulanmamış olarak işaretle ve dur. Hangisini istersiniz?"
> Bir avukat düşük güvenilirlikli kaynakları kabul edip etmeyeceğine karar
> verir.
>
> **Kaynak atfı.** İncelemedeki her atfı nereden geldiğiyle etiketleyin:
> bir hukuki araştırma bağlayıcısından alınan atıflar için `[Lexpera]`,
> `[Kazancı]`, `[UYAP]` veya MCP araç adı; web araması atıfları için
> `[web araması — doğrula]`; eğitim verisinden hatırlanan atıflar için
> `[model bilgisi — doğrula]`; kullanıcının sağladığı atıflar için
> `[kullanıcı verdi]`. `doğrula` etiketli atıflar daha yüksek uydurma
> riski taşır ve önce kontrol edilmelidir. Etiketleri asla kaldırma veya
> birleştirme.

### Adım 4: Yargı çevresine özgü gereksinimler

Bu yargı çevresi için
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
tablosunu kontrol edin. Her işe alım için araştırılacak yaygın kategoriler:

- **İlan/bildirim şeffaflığı** — yargı çevresi ilanda ücret aralığı
  gerektiriyor mu? Gerekiyorsa, bu teklif ilan edilen aralık içinde mi?
  Güncel kuralı araştırın (yakın tarihli tadiller veya yeni uygulama
  rehberi dahil). `[doğrulanacak — TR'de böyle bir yasal zorunluluk var
  mı, yoksa yalnızca yurt dışı şubeler için mi geçerli]`
- **Adli sicil sorgusu zamanlaması** — yargı çevresi veya belediye, adli
  sicil sorgusunun zamanlamasını veya kapsamını kısıtlıyor mu?
- **Önceki ücret sorma sınırları** — yargı çevresi önceki ücrete dair
  soru sormayı veya buna güvenmeyi kısıtlıyor mu?
- **Gerekli teklif mektubu veya işe alım bildirimleri** — bazı yargı
  çevreleri teklif veya işe alımda spesifik bildirimler gerektirir
  (ücret bildirimi kanunları, hastalık izni bildirimleri vb.). Şu an ne
  gerektiğini ve bir şablon olup olmadığını araştırın.

Birincil kaynaklara atıf yapın. Güncelliği doğrulayın.

### Adım 5: Teklif mektubu içeriği

Mektubu okuyun. Kontrol edin:

**İşten çıkarma serbestisi ("at-will") büyük ölçüde ABD'ye özgüdür.**
"At-will" tarafların nedensiz ve bildirimsiz fesih yapabileceği anlamına
gelir (yasal istisnalara tabi). Bu kavram Türkiye'de yoktur:

- **Türkiye:** İşten çıkarma serbestisi yoktur. 4857 sayılı Kanun, belirli
  koşullarda iş güvencesi rejimi (m.18-21), ihbar süreleri (m.17) ve
  geçerli/haklı neden ayrımı (m.18, m.25) öngörür. Deneme süresi (m.15)
  azami 2 ay, toplu iş sözleşmesiyle 4 aya kadar uzatılabilir ve bu süre
  içinde bildirimsiz ve tazminatsız fesih mümkündür. Teklif mektubu
  deneme süresini, ihbar süresini ve geçerli olacaksa iş güvencesi
  kapsamını (kıdem/işyeri çalışan sayısı eşiği) açıkça belirtmelidir
  `[doğrulanacak]`.
- **ABD (çoğu eyalet):** At-will varsayılandır.
- **AB/İngiltere ve diğerleri:** At-will yoktur — bildirim, neden ve
  genellikle işyeri konseyi danışması veya toplu işten çıkarma usulü
  gerektirir.

**"At-will" dilini yalnızca ABD yargı çevresiyse kontrol edin.** ABD-dışı
yargı çevreleri için bunun yerine kontrol edin: bildirim süresi (ve yasal
asgariyi karşılayıp karşılamadığı), yargı çevresinin gerektirdiği yazılı
şart bildirimi, deneme süresi şartları ve yargı çevresine özgü zorunlu
hükümler.

**ABD-dışı bir teklif mektubuna asla "at-will" dili eklemeyi önermeyin.**
Hukuken anlamsızdır, zorunlu yasal şartlarla çelişebilir ve çalışanın
avukatına işverenin yargı çevresini anlamadığı sinyalini verir.

- At-will dili mevcut ve başka yerde zayıflatılmamış (yalnızca ABD —
  yukarıya bakın)
- Şartlar açık (arka plan kontrolü, referans, çalışma izni/ikamet izni
  gerekliyse)
- Başlangıç tarihi, unvan, ücret, raporlama yapısı belirtilmiş
- Hisse senedi şartları (varsa) planla tutarlı
- Bütünleştirme maddesi, mektubu anlaşmanın tamamı yapıyor
- ABD-dışı için: bildirim süresi yasal asgariyi karşılıyor, yargı
  çevresinin gerektirdiği yazılı şart bildirimi dahil, deneme süresi
  yerel kurallara uygun

## Çıktı

> **Yargı çevresi varsayımı.** Bu inceleme, Adım 1'de tespit edilen
> çalışanın çalışma yargı çevresinin kurallarını uygular. Rekabet yasağı
> uygulanabilirliği, çalışma süresi rejimi, ilan şeffaflığı yükümlülükleri,
> önceki ücret sınırları ve gerekli bildirimler ülkeye/bölgeye göre maddi
> olarak değişir ve bazıları yakın zamanda değişmiştir. Adayın çalışma
> yeri değişirse, veya rol yargı çevrelerine yayılırsa, bu inceleme
> yazıldığı gibi geçerli olmayabilir.

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırması ## Çıktılar'a göre — role göre değişir; bkz. `## Bunu kim kullanıyor`]

## İşe Alım İncelemesi: [Aday] — [Rol] — [Yargı çevresi]

**Genel:** [Göndermeye hazır | Değişiklik gerekiyor | Eskale et]

### Yargı çevresi: [Ülke/Bölge]
[Yargı çevresi tablosu girdisi. Tetiklenen herhangi bir otomatik-eskale.]

### Sınıflandırma
[Araştırılmış çalışma süresi rejimine dayalı çağrı. Herhangi bir işaret.
🅱️ — tam çerçeve `ucret-saat-sss`/`calisan-siniflandirma` taşınana kadar
`[doğrulanacak]` işaretli.]

### Rekabet yasağı hükümleri
[Varsa. Araştırılmış yargı çevresi kurallarına göre uygulanabilirlik
çağrısı, tam künye atıfları ve güncellik notuyla. Önerilen değişiklikler.]

### Yargı çevresine özgü gereksinimler
[İlan şeffaflığı, bildirimler, önceki ücret kuralları vb. — her biri
araştırılmış ve atıf yapılmış, veya araştırma gerektiği işaretlenmiş.]

### Teklif mektubu
[Mektubun kendisiyle ilgili herhangi bir sorun]

### Eylem kalemleri
- [ ] [gönderilmeden önce gereken spesifik değişiklik]
```

## Sonuç doğuran eylem kapısı (bir teklif yapma)

**"Göndermeye hazır" önerisi veya imza için nihai bir teklif mektubu
üretmeden önce:**
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
dosyasındaki `## Bunu kim kullanıyor` bölümünü oku. Rol **Avukat olmayan**
ise:

> Bir teklif yapmanın hukuki sonuçları vardır — mektup bir sözleşmedir ve
> rekabet yasağı, sınıflandırma ve yargı çevresine özgü şartlar
> gönderildikten sonra sıfırlanması zor olabilir. Bu teklifi bir avukatla
> gözden geçirdiniz mi? Evetse devam edin. Hayırsa, onlara götürecek bir
> brifing:
>
> - Aday, rol, yargı çevresi (gerçekte nerede çalışacakları)
> - Sınıflandırma çağrısı ve nedeni
> - Tekliftteki rekabet yasağı hükümleri ve uygulanabilirlik analizi
> - Geçerli yargı çevresine özgü gereksinimler (ilan şeffaflığı, ücret
>   bildirimleri, önceki ücret kuralları)
> - Açık sorular ve neyin çözülmediği
> - Neyin ters gidebileceği (yanlış sınıflandırma sorumluluğu,
>   uygulanamaz rekabet yasağı, eksik gerekli bildirim, çelişen at-will
>   dili)
> - Avukata ne sorulacağı (bu yargı çevresi için doğru form mu; burada
>   standart rekabet yasağımızı kullanabilir miyiz; mektupla birlikte
>   hangi bildirimlerin gitmesi gerekiyor)
>
> Bir avukat bulmanız gerekiyorsa: ilgili baroya danışın.

Bu kapının ötesine açık bir "evet" olmadan "Göndermeye hazır" çıktısı
üretme. Avukat incelemesi için işaretlenmiş bir TASLAK sorun değil.

---

## Sonraki adımlar karar ağacıyla kapat

CLAUDE.md `## Çıktılar` başına sonraki adımlar karar ağacıyla kapat.
Seçenekleri bu skill'in az önce ürettiği şeye göre özelleştir — beş
varsayılan dal (X'i taslakla, eskale et, daha çok olgu topla, izle ve
bekle, başka bir şey) bir başlangıç noktasıdır, bir kilitlenme değil.

## Bu skill'in yapmadıkları

- Teklif mektubunu taslaklamak — inceler.
- İşe alım kararını vermek — evrakı kontrol eder.
- Rekabet yasağı veya muafiyet kurallarını ezberden belirtmek — her
  yargı çevresine özgü çağrı, güncellik için doğrulanmış araştırılmış,
  atıf yapılmış kaynaklara dayanır.
- Yeni bir yargı çevresini derinlemesine kendi başına araştırmak —
  araştırmanın gerekli olduğunu işaretler, doldurmak için
  `uluslararasi-genisletme` veya dış avukatı kullanır.
