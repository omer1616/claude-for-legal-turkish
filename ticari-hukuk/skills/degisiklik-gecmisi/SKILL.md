---
name: degisiklik-gecmisi
description: >
  Bir sözleşmenin ana metni ve tüm zeyilnameleri boyunca nasıl değiştiğini izleyin —
  ya zaman içindeki tüm değişikliklerin bir özeti, ya da belirli bir maddenin izini
  sürme. Kullanıcı "bu sözleşmede zaman içinde ne değişti", "bana değişiklik
  geçmişini göster", "en son [madde] nerede", "[hüküm] nasıl evrildi" dediğinde
  veya bir sözleşmenin birden fazla versiyonunu yüklediğinde kullan.
argument-hint: "[dosya(lar) | [CLM kimliği (yakında)] | [depo bağlantısı (yakında)]] [--madde <hüküm adı>]"
---

# /degisiklik-gecmisi

Bir ana sözleşmeyi ve tüm zeyilnamelerini yükler, sonra ya zaman içinde ne
değiştiğini özetler ya da belirli bir maddeyi güncel kontrol eden diline kadar
izler.

## Talimatlar

1. **Belgeleri al:** Dosya yüklemesinden, [CLM kimliği (yakında)] veya [depo
   bağlantısı (yakında)]'ndan. Bir çağrıda birden fazla dosya kabul edin. Hiçbiri
   verilmediyse sor.

2. **Modu tespit et** aşağıdaki mod tespit kurallarına göre isteği ayrıştırarak.
   Bir madde adı açıkça belirtilmişse, doğrudan Mod 2'ye geç. Madde
   bahsedilmiyorsa Mod 1'i çalıştır. Yalnızca gerçekten belirsizse sor.

3. **Aşağıdaki iş akışını çalıştır.** Tam olarak takip edin.

4. **Çıktıdan sonra devam adımları öner:**
   - "Başka bir madde izlememi ister misiniz?"
   - "Değiştirilmiş haliyle mevcut sözleşmenin tam oyun kitabı incelemesini ister
     misiniz?" (satici-inceleme'ye yönlendirir)
   - "Kilit değişikliklerin bir paydaş özetini ister misiniz?" (paydas-ozeti'ne
     yönlendirir)

## Örnekler

```
/ticari-hukuk:degisiklik-gecmisi acme-msa.pdf zeyilname-1.pdf zeyilname-2.pdf
```

```
/ticari-hukuk:degisiklik-gecmisi --madde tazminat
```

```
/ticari-hukuk:degisiklik-gecmisi
[sözleşme ve zeyilname metnini yapıştır]
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

Sözleşmeler zeyilname biriktirir. Üçüncü zeyilnameye gelindiğinde, kimse orijinalin
ne dediğini veya bir maddenin hangi versiyonunun kontrol ettiğini hatırlamaz. Bu
skill, ana sözleşmeyi ve tüm zeyilnameleri kronolojik sırayla okur ve ya tüm sözleşme
boyunca neyin değiştiğini özetler ya da güncel kontrol eden dili bulmak için belirli
bir maddeyi her versiyon boyunca izler.

## Mod tespiti

Hangi modun çalıştırılacağını belirlemek için kullanıcının isteğini ayrıştırın.
İstek gerçekten belirsiz olmadıkça hangi mod olduğunu sormayın.

**Mod 1 — Özet** (belirli bir madde bahsedilmiyor)
Tetik ifadeleri: "ne değişti", "değişiklik geçmişi", "zaman içindeki değişiklikleri
göster", "zeyilnameleri özetle", "bu sözleşme şu anda nasıl görünüyor"

**Mod 2 — Madde izleme** (belirli bir hüküm veya konu adlandırılmış)
Tetik ifadeleri: "[madde] nerede", "en son [hüküm]", "[terim] nasıl değişti",
"tazminatı bul", "[konu] hakkında şimdi ne diyor"

Yaygın hüküm eşlemeleri:
- "tazminat" → tazminat bölümü
- "sorumluluk" / "sorumluluk tavanı" → sorumluluk sınırı
- "fesih" → süre ve fesih
- "veri" / "gizlilik" / "VİS" → veri koruma hükümleri
- "fikri mülkiyet" → fikri mülkiyet sahipliği ve lisanslar
- "fiyat" / "ücretler" / "ödeme" → ödeme şartları
- "otomatik yenileme" / "yenileme" → yenileme mekaniği

Terim belirsizse ve birden fazla hükme eşleniyorsa, adayları listeleyin ve
hangisi olduğunu sorun:
> "[Terim] ile ilgili [N] hüküm buldum — [listeleyin]. Hangisi?"

Genel istek modlar arasında belirsizse, tek bir soru sorun:
> "Tüm sözleşme boyunca değişikliklerin bir özeti mi, yoksa belirli bir hükmün —
> tazminat, sorumluluk veya fesih gibi — izini mi sürelim?"

---

## Adım 1: Belgeleri yükle ve sırala

Belgeleri aşağıdaki kaynaklardan herhangi birinden kabul edin:

**[CLM entegrasyonu yakında] (bağlıysa):**
Karşı taraf adına veya sözleşme başlığına göre arayın. Ana sözleşmeyi ve tüm
zeyilnameleri çekin. Kayıt meta verisi tipik olarak imza tarihlerini içerir —
kronolojik sırayı belirlemek için bunları kullanın.

**[Belge deposu entegrasyonu yakında] (bağlıysa):**
Karşı taraf adına veya dosya adına göre arayın. "Zeyilname", "Ek", "Zeyilname No.
1", "Birinci Zeyilname" veya numaralandırılmış sonekler gibi kalıplara uyan dosyaları
arayın. Tüm eşleşmeleri çekin ve dosya tarihine veya dosya adı numaralandırmasına
göre sıralayın.

**Doğrudan yükleme:**
Kullanıcı dosyaları doğrudan sağlar. Çoğu durumda sıralama belge başlıklarından
(ör. "Zeyilname No. 1", "İkinci Zeyilname", "Ek A") veya dosya adında veya belge
başlığında görünen tarihlerden kendiliğinden bellidir — sormadan devam edin.

Yalnızca şu durumlarda sırayı teyit etmesini isteyin:
- Dosya adları sıra hakkında hiçbir ipucu vermiyorsa (ör. "sozlesme-final.pdf",
  "sozlesme-v2.pdf", "sozlesme-redline.pdf")
- Hem dosya adlarında hem belge başlıklarında tarihler yoksa
- İki belge aynı zeyilname versiyonu gibi görünüyorsa

Sıra teyit edilmeden çıkarıldıysa, yalnızca belirsiz olan yerde çıktının en üstünde
güveni not edin:
> "Sıra belge başlıklarından çıkarıldı — daha az emin olduğum bir kalem: [spesifik
> belge]. Bu incelemenizi etkiliyorsa teyit edin."

**Sıralama kuralları:**
- İçeriği okumadan önce her zaman kronolojik sırayı belirleyin.
- İmza tarihleri meta veride mevcutsa, bunları kullanın.
- Değilse, belge başlığında veya giriş kısımlarında ("İşbu Zeyilname, [X]
  tarihli...") tarihler arayın.
- Zeyilnameler genellikle değiştirdikleri sözleşmeye atıfta bulunur ("[X] tarihli
  Ana Hizmet Sözleşmesi'ne bu Zeyilname") — zinciri teyit etmek için bu referansları
  kullanın.

---

## Meslek sırrı devri

Bu skill ana sözleşmeyi ve zeyilnameleri okur — genellikle kendi içlerinde meslek
sırrı kapsamında veya gizli ve tipik olarak meslek sırrı analizinde kullanılır.
Çıktı, kaynağın meslek sırrı ve gizlilik durumunu miras alır.
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
`## Çıktılar`'dan iş-ürünü başlığını aşağıdaki her çıktının başına ekleyin, yalnızca
meslek sırrı çemberi içinde dağıtın ve gizli materyallerin yaşadığı yerde saklayın.
Herhangi bir dış teslimattan önce başlığı çıkarın.

## Adım 2: Oku ve indeksle

Her belgeyi kronolojik sırayla okuyun. Her biri için şunu çıkarın:
- Belge türü (ana sözleşme, zeyilname numarası, ek vb.)
- İmza tarihi
- Taraflar (belgeler arasında eşleştiklerini teyit edin — yeni bir taraf eklendiyse
  veya bir taraf adı değiştiyse işaretleyin)
- Açıkça değiştirilen, eklenen veya silinen hükümlerin bir listesi

Çıktı üretmeden önce çalışan bir indeks oluşturun. Çıktıyı yönlendirmek için dahili
olarak kullanın — kullanıcıya göstermeyin.

---

## Mod 1: Tüm değişikliklerin özeti

### Bölüm referansı kuralı

Her bulgu, okuyucunun aramadan kaynak belgeye karşı doğrulayabilmesi için satır içi
bir bölüm referansı içermelidir:

  "Serbestçe fesih (§12.3): Eklendi. Müşteri, ilk süreden sonra ücretsiz olarak
  90 gün yazılı bildirimle fesih edebilir."

Bir hüküm birden fazla bölüme yayılıyorsa veya bölüm numarası zeyilnameler
boyunca değiştiyse, tüm referansları alıntılayın:
  "Tazminat (§9.1 ana; Zeyilname 5'te §9.1 yeniden düzenlendi)"

### Çıktı formatı

```markdown
# Değişiklik Geçmişi: [Karşı taraf] — [Sözleşme türü]

**Ana sözleşme:** [tarih]
**Zeyilnameler:** [N] ([ilkinin tarihi] → [sonuncunun tarihi])
**Son değişiklik:** [tarih]

---

## Ne değişti — kronolojik

### Zeyilname 1 — [tarih]
**Amaç:** [tek cümle — bu zeyilnamenin neden var olduğu, giriş kısımlarından veya
bağlamdan açık. Belirtilmemişse, tahmin etmek yerine atlayın.]

**Esaslı değişiklikler:**
- [Hüküm] (§[X.X]): [öncesinde ne dediği → şimdi ne dediği, düz Türkçe]
- [Eklenen yeni hüküm] (§[X.X]): [ne yaptığı]
- [Silinen hüküm] (§[X.X]): [ne kaldırıldığı ve neden önemli olduğu]

### Zeyilname 2 — [tarih]
[aynı yapı]

[her zeyilname için tekrarlayın]

---

## Net güncel durum

| Hüküm | Güncel pozisyon | §Ref | Son değişiklik |
|---|---|---|---|
| [madde] | [düz Türkçe özet] | §[X.X] | Zeyilname N, [tarih] |
| [madde] | [ana metinden değişmedi] | §[X.X] | Ana sözleşme |

---

## Dikkat edilecek kalemler
[Tutarsız görünen herhangi bir şeyi işaretleyin — ör. zaten silinmiş bir hükmü
değiştiren bir zeyilname, zeyilnameler arasında çelişkili dil, resmi bir devir
olmadan değişen bir taraf adı, veya belgeler arasında bölüm numarasının kaydığı bir
hüküm. Her bayrakta bölüm referansları dahil edin.]
```

---

## Mod 2: Madde izleme

### Çıktı formatı

Yalnızca neyin değiştiğini gösterin. Hükmün dokunulmadığı zeyilnameleri listelemeyin
— tamamen atlayın.

```markdown
# Madde İzi: [Hüküm adı]
## [Karşı taraf] — [Sözleşme türü]

---

### Orijinal — [Ana sözleşme tarihi], §[X.X]
> "[tam alıntı]"

*Düz Türkçe:* [tek cümle]

---

### Zeyilname [N] — [tarih], §[X.X]

**Şuydu:**
> "[önceki dilin tam alıntısı]"

**Şimdi:**
> "[yerine geçen dilin tam alıntısı]"

*Ne değişti:* [tek cümle — taraflar üzerindeki pratik etki]

---

[Yalnızca bu hükme dokunan sonraki zeyilnameler burada görünür. Diğer hepsi
atlanmıştır.]

---

## Güncel kontrol eden dil

**§[X.X] — [kaynak belge, tarih]**
> "[tam alıntı]"

*Düz Türkçe:* [tek cümle]

---

## Dikkat edilecek kalemler
[Bölüm referanslarıyla bayraklar, tutarsızlıklar, açık sorular. Kontrol edilecek
yaygın kalemler: hükmün sorumluluk tavanına tabi olup olmadığı veya istisna
tutulup tutulmadığı; bölüm numarasının zeyilnameler boyunca kayıp kaymadığı;
zeyilname dilinin başka bir hükümle çelişip çelişmediği.]
```

Hüküm ana sözleşmeden sonra hiç değiştirilmediyse:
> "Bu hüküm herhangi bir zeyilname tarafından değiştirilmedi. Orijinal dil
> kontrol ediyor. §[X.X], ana sözleşme, [tarih]."

---

## Sonraki-adımlar karar ağacıyla kapat

CLAUDE.md `## Çıktılar`'a göre sonraki-adımlar karar ağacıyla bitir. Seçenekleri bu
skill'in az önce ürettiğine göre uyarla — beş varsayılan dal (X'i taslakla, eskale
et, daha çok olgu al, izle ve bekle, başka bir şey) bir başlangıç noktasıdır, bir
kilitlenme değil. Ağaç çıktının kendisidir; avukat seçer.

## Bu skill'in yapmadıkları

- Ana sözleşme ile bir zeyilname arasında çelişki durumunda hangi belgenin kontrol
  ettiğine karar vermez — bu bir hukuki yorumlama sorusudur. Çelişkileri işaretler ve
  Hukuk'a yönlendirir.
- Yeni zeyilnameler taslaklamaz.
- `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
  içindeki oyun kitabıyla karşılaştırmaz — bu satici-inceleme skill'inin işidir. Bu
  skill saf olarak tarihseldir.
- Dil belirsizse bir zeyilnamenin ne anlama geldiğini çıkarmaz — tam olarak
  alıntılar ve belirsizliği Hukuk için işaretler.
