---
name: delil-saklama
description: Delil saklama bildirimlerini verir, tazeler, serbest bırakır veya raporlar — bildirimi markdown olarak hazırlar, _log.yaml'daki delil_saklama alanlarını günceller ve sonraki tazelemeyi takvime ekler. Kullanıcı "saklama ver", "saklamayı tazele", "saklamayı serbest bırak" dediğinde veya portföy genelinde saklama durum raporu istediğinde kullan.
argument-hint: "[slug] [--ver | --tazele | --serbest-birak | --durum]"
---

# /delil-saklama

1. `--durum` (slug olmadan): `_log.yaml` oku, portföy genelinde saklama raporu üret.
2. Aksi hâlde: `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` + log satırını yükle.
3. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` yükle → gizlilik işaretleri, saklama şablonu işaretçisi, eskalasyon normları.
4. Aşağıdaki iş akışını ve referansı uygula.
5. Bayrağa göre yönlendir:
   - `--ver`: kapsam, muhafızlar, tarih aralığı, sistemler yakala. `delil-saklama-v1.md` taslakla. `delil_saklama` alanlarını güncelle. Geçmiş kaydı ekle. `sonraki_tazeleme` ayarla (varsayılan +6 ay).
   - `--tazele`: kapsam/muhafız değişikliklerini yakala. Sonraki sürümü taslakla. `son_tazeleme` + `sonraki_tazeleme` güncelle. Ayrılan muhafızları işaretle.
   - `--serbest-birak`: serbest bırakma tarihini, saklama talimatını yakala. Serbest bırakma bildirimini taslakla. `serbest_birakildi:` alanını ayarla.
6. Yazmadan önce teyit et. Kullanıcıya taslak bildirimi ve log farkını göster.

---

# Delil Saklama

## Amaç

Delil saklama bildirimi, şirket-içi avukatın yazdığı en mekanik yüksek-riskli belgedir. Bildirimin kendisi şablonludur. Hata modları operasyoneldir: çok geç verilmiş, çok dar kapsamlı, hiç tazeletilmemiş, hiç serbest bırakılmamış. Bu skill dört aşamanın tamamına sahiptir: **ver → tazele → (serbest bırak) → takip et**.

Portföy eksik saklamaları zaten işaretler; bu skill onları yazar.

## Yargı Çevresi Varsayımı

Saklama yükümlülükleri yargı çevresine göre önemli ölçüde farklılık gösterir. **Türk hukukunda:**

- HMK (m.220 vd.) belge ibrazı ve saklama yükümlülüklerini düzenler; CMK ceza davalarında delil muhafazasını kapsar.
- Hukuki saklama yükümlülüğünün ne zaman başladığı (dava ikamesi, tebligat, makul öngörü) ve kapsamı Türk mahkemelerinde daha dar yorumlanabilir; ABD federal mahkemelerinden (Zubulake / FRCP 37(e)) farklıdır.
- KVKK, sektöre özgü mevzuat (Bankacılık K., SPK mevzuatı) ve sözleşmesel yükümlülükler sivil kurallara ek saklama yükümlülükleri getirebilir.
- Saklama yükümlülüğünün zamanlaması, kapsamı ve yaptırım maruziyeti verilen dava için Türk hukuku ve foruma göre birincil kaynakla teyit edilmelidir; kaydedilen tetik standardı, kapsam standardı ve yaptırım maruziyeti çıkarmadan/tazeletmeden/serbest bırakmadan önce avukat onayıyla doğrulanmalıdır. `[doğrulanacak]`

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` — log satırı (delil_saklama alanları + durum)
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` — dava bağlamı (karşı taraf, olgular, ic_sahiplerden kilit muhafızlar)
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` — dava tutanma şablonu işaretçisi, gizlilik işaretlemesi, eskalasyon normları için ev tarzı

**Çatışma kapısı — atlanamaz.** Saklama vermeden, tazeletmeden veya serbest bırakmadan önce dosya slug'ını `_log.yaml`'da kontrol et. Dosya `_log.yaml`'da yoksa reddet ve yönlendir:

> "[dosya slug'ı]'nı dosya günlüğünde göremiyorum. Önce `/dava-takibi:dosya-acilis` çalıştır; böylece çatışma taraması yapılır ve dosya çalışma alanı kurulur. Intake yapılmamış bir dosyada delil saklama vermem, tazeletmem veya serbest bırakmam — çatışma taraması kapıdır ve `--tazele` / `--serbest-birak` / `--durum` bayraklarının işlediği `_log.yaml` satırı yoktur."

## Modlar

Komut bir bayrak alır: `--ver | --tazele | --serbest-birak | --durum`. Varsayılan (bayrak yok) → sor.

### `--ver` — İlk Saklama

`delil_saklama.gonderildi == false` olduğunda ve dava aktifse veya makul ölçüde öngörülüyorsa gereklidir.

**Saklama bildirimini muhafızlara göndermeden önce (sonuç doğuran eylem):** `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'deki `## Bunu Kim Kullanıyor` bölümünü oku. Rol Avukat değilse:

> Delil saklama bildirimi vermek hukuki sonuçlar doğurur — kapsam, muhafız listesi ve zamanlama, daha sonra delil imhası iddia edilirse şirketin yargılanacağı saklama kaydını oluşturur. Bunu bir avukatla gözden geçirdiniz mi? Evet ise devam edin. Hayır ise, onlara götürmek için kısa bir özet:
>
> [1 sayfalık özet üret: dava ve tetikleyici, önerilen kapsam ve muhafızlar, araştırılan Türk hukuku/HMK saklama kuralı, bilinen delil imhası riski, yanlış gidebilecekler (çok geniş / çok dar), avukata sormadan önce ne sorulacak.]
>
> Lisanslı bir avukat bulmak için: Türkiye Barolar Birliği veya ilgili baronun yönlendirme hizmeti en hızlı başlangıç noktasıdır.

Açık bir "evet" olmadan bildirimi gönderme. Taslak yazmak ve kapsam belirlemek kapıyı gerektirmez — vermek gerektirir.

**Vermeden önce geçerli saklama kuralını araştır.** Yargı çevresini ve saklama yükümlülüğünün kaynağını (Türk mahkemesi için HMK, CMK, sektöre özgü mevzuat, sözleşme) belirle. Şu anki işletilen tetik standardını (yükümlülük ne zaman başlıyor), kapsam standardını (neyin saklanması gerekiyor) ve yaptırım maruziyetini teyit et. Birincil kaynakları aktar. `[doğrulanacak]`

> **Dış teslimat:** aşağıdaki bildirim muhafızlara gönderilir. Giden bildirime avukat-müvekkil gizlilik başlığı EKLEME; şablondaki avukat-müvekkil işaretlemesini kullan. Yargı çevreniz ve davanız için doğru işaretlemeyi teyit edin.

**Girdiler:**
1. **Kapsam** — belge, veri, iletişim kategorileri. Spesifikten başla: karşı tarafla sözleşmeler, [proje/konu]'ya atıfta bulunan tüm iletişimler, ilgili mali kayıtlar, takvim girişleri. `[SME ONAYLA — kapsam çok geniş = operasyonel yük; çok dar = delil imhası riski]`
2. **Muhafızlar** — duyarlı materyale sahip olması muhtemel adlandırılmış kişiler. Önerileri matter.md ic_sahiplerinden ve yaygın rollerden çek (iş birimi yöneticisi, İK partneri, BİLGİ GÜVENLİĞİ). `[SME ONAYLA — muhafız listesi savunulabilir saklama ile boşluk iddiası arasındaki farktır]`
3. **Tarih aralığı** — saklamanın ne zaman başlayacağı (genellikle: tetikleyici olay veya daha önce), bugünden itibaren devam edecek.
4. **Sistemler** — e-posta, anlık mesajlaşma (Teams, Slack vb.), dosya sunucuları, kişisel cihazlar (BYOD dahilse), proje yönetimi araçları, CRM, eski sistemler.
5. **Aciliyet** — dava zaten tebliğ edildiyse veya talep dava tehdidiyle alındıysa, bu bugün çıkar.
6. **Yürürlük tarihi** — saklamanın tarihi.

**Varsayılan saklama bildirimi şablonu:**

```
[GİZLİ — AVUKAT-MÜVEKKİL İLETİŞİMİ]

TARİH: [yürürlük tarihi]
ALICI: [muhafız adı]
GÖNDEREN: [imzalayan — `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` varsayılanına göre]
KONU: DELİL SAKLAMA BİLDİRİMİ — [dava kısa adı]

Bu bildirimi alıyorsunuz; zira [şirket], [uyuşmazlık / soruşturmanın bir cümlelik açıklaması, önyargılı ayrıntıdan kaçınarak] ile ilgili bir durumla karşı karşıya kaldığını belirlemiştir. Hukuk, bu davayla potansiyel olarak ilgili belge ve iletişimlerin saklanmasını gerektirmektedir.

HEMEN ETKİLİ OLARAK, şunları saklamanız gerekmektedir:

1. [Kapsam maddesi 1] ile ilgili tüm belgeler, e-postalar, mesajlar ve diğer iletişimler.
2. [Kapsam maddesi 2]
3. [Kapsam maddesi 3]
...

Bu saklama yükümlülüğü şunlar için geçerlidir:
- E-posta (gönderilen, arşivlenen, silinen klasörler dahil)
- Anlık mesajlaşma platformları (Teams, Slack vb.)
- Paylaşılan sürücüler ve bulut depolama
- İş amaçlı kullanılan kişisel cihazlar (BYOD)
- Kâğıt belgeler
- Sesli mesajlar
- Takvim girişleri ve toplantı notları

YAPMAYIN:
- Potansiyel olarak duyarlı materyali silmeyin, değiştirmeyin, imha etmeyin veya elden çıkarmayın
- E-posta veya mesajları otomatik silmeyin

Bu bildirimi doğrudan raporlarınız veya BT ile paylaşmadan önce [hukuk irtibatı] ile koordinasyon sağlayın.

Bu bildirim veya saklama yükümlülüklerinizle ilgili sorularınızı [imzalayan]'a yöneltin. Çalışmanız için gerektiğinde meslektaşlarınızla ilgili ticari konuyu tartışmaya devam edebilirsiniz, ancak bu hukuki bildirimi, davayı veya hukuki stratejiyi tartışmayın.

Bir şeyin kapsama girip girmediğinden EMİN DEĞİLSENİZ, SAKLAMAK YÖNÜNDE HAREKET EDİN.

Lütfen bu bildirimin alındığını [üç iş günü içinde yanıt / bağlantı / form ile] teyit edin. Sorularınız için [imzalayan e-posta] ile iletişime geçin.

Bu bildirim yazılı serbest bırakma bildirimi alana kadar yürürlükte kalır. Belirli aralıklarla uyumu yeniden teyit etmeniz istenebilir.

[İmzalayan imza bloğu]
```

**Gönderme kapısı (taslaktaki kapanış notu):** Bildirimin sohbetteki önizlemesinin ardına ekle — muhafızlara gitmeden önce çıkar:

> Bu, avukat incelemesi için bir taslak delil saklama bildirimidir, vermeye hazır bir bildirim değildir. Saklama bildirimi vermek, şirketin daha sonraki bir delil imhası tartışmasında yargılanacağı saklama yükümlülükleri başlatır ve bildirimin kendisi gizlilik bağlamında dikkate alınabilir. Lisanslı bir avukat, dağıtılmadan önce inceler, onaylar ve verir. Bu taslağı incelenmeden dağıtmayın.

**Yazmalar:**
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/delil-saklama-v1.md` (markdown formatında)
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` dosyasına ekle:
  ```
  ## [YYYY-AA-GG] — Delil Saklama Verildi

  [N] muhafıza saklama verildi: [liste].
  Kapsam: [tek satır özet].
  Sonraki tazeleme: [YYYY-AA-GG (varsayılan verilmeden 6 ay sonra)].
  ```
- `_log.yaml` satırını güncelle:
  ```yaml
  delil_saklama:
    gonderildi: true
    tarih: [YYYY-AA-GG]
    kapsam: "[tek satır özet]"
    muhafizlar: [liste]
    son_tazeleme: [YYYY-AA-GG]   # ilk vermede tarih ile aynı
    sonraki_tazeleme: [YYYY-AA-GG]   # varsayılan: tarih + 6 ay
    serbest_birakildi: null
  ```

### `--tazele` — Periyodik Yeniden Teyit

Tazeleme sıklığı: varsayılan 6 ay; davaya göre ayarlanabilir. `sonraki_tazeleme < bugün` olduğunda (veya kullanıcı manuel olarak tetiklediğinde), skill bir tazeleme bildirimi hazırlar.

**Girdiler:**
1. Son tazeletmeden bu yana **kapsam değişiklikleri** (delil toplama sürecinde ortaya çıkan yeni konular, yeni muhafızlar, yeni sistemler).
2. **Eklenecek veya çıkarılacak muhafızlar** (ayrılanlar — aşağıya bakın).
3. Yeniden teyit dili.

**Tazeleme bildirimi şablonu:** ilk vermeye benzer; "[tarih]'te verilen delil saklama bildiriminin yeniden teyididir" ile açılır. Mevcut kapsamı listeler (değiştirilmişse). Yeniden teyit ister.

**Ayrılan muhafızlar:** son tazeletmeden bu yana bir muhafız şirketten ayrıldıysa, skill bunu bir saklama eylem kalemi olarak işaretler — ayrılan çalışanın dosyaları ve e-posta arşivi BT düzeyinde saklanması gerekir, yalnızca kişiye bildirim değil. history.md'ye eylem gerektiren ayrı bir kayıt olarak kaydeder.

**Yazmalar:**
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/delil-saklama-v[N].md` (sonraki sürüm numarası)
- `history.md` kaydı
- `_log.yaml`: `son_tazeleme` ve `sonraki_tazeleme` alanlarını günceller; değiştiyse `muhafizlar` listesini değiştirir

### `--serbest-birak` — Saklamayı Kapat

Genellikle dosya kapatmada. Davanın gerçekten sona erdiğini teyit et (temyizde değil, yeniden açılması muhtemel değil, ilgili taleplerde zamanaşımı geçmiş).

**Saklamayı serbest bırakmadan önce (sonuç doğuran eylem — saklama yükümlülükleri normal saklama politikasına döner):** `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'deki `## Bunu Kim Kullanıyor` bölümünü oku. Rol Avukat değilse:

> Saklama bildirimi serbest bırakmanın hukuki sonuçları vardır — serbest bırakıldıktan sonra muhafızlar materyali silmeye başlayabilir. Yanlış zamanda serbest bırakmak delil imhası riski yaratır. Bunu bir avukatla gözden geçirdiniz mi? Evet ise devam edin. Hayır ise, onlara götürmek için kısa bir özet üret.

Açık bir "evet" olmadan serbest bırakma bildirimini gönderme.

**Girdiler:**
1. Serbest bırakma yetkisinin teyidi (genellikle imzalayan veya BHM).
2. Serbest bırakma tarihi.
3. Saklama talimatı — saklama altındaki materyal ne olacak? (Normal saklama politikasına dön? Belirli bir süre daha saklama? Arşive transfer?)

**Serbest bırakma bildirimi şablonu:** tek paragraf, resmi. "[Tarih]'te [dava] ile ilgili verilen delil saklama bildirimi [tarih] itibarıyla serbest bırakılmıştır. Normal saklama politikası yeniden geçerlidir."

**Yazmalar:**
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/delil-saklama-serbest.md`
- `history.md` kaydı
- `_log.yaml`: `serbest_birakildi: [YYYY-AA-GG]` ayarlar

### `--durum` — Portföy Genelinde Rapor

`_log.yaml` oku. Bir rapor üret:

```markdown
# Delil Saklama Durumu — [bugün]

## Aktif Saklama Bildirimleri

| Dava | Verildi | Son Tazeleme | Sonraki Tazeleme | Muhafız Sayısı | Durum |
|---|---|---|---|---|---|
| [slug] | [tarih] | [tarih] | [tarih] | [N] | [tamam / ⚠️ tazeleme yaklaşıyor / ❌ gecikmiş] |

## ⚠️ Dikkat

- **Gecikmiş tazeleme:** [`sonraki_tazeleme` geçmiş olan slug'lar]
- **30 gün içinde tazeleme:** [liste]
- **Aktif saklama bildirimi olmayan dosyalar:** [liste — önce yüksek/kritik risk]
- **Saklama aktifken kapatılan dosyalar:** [liste — serbest bırakmayı değerlendir]

## Son Serbest Bırakılanlar

[Tarihli son 5 serbest bırakılan saklama]
```

Bu, ayrı bir komut çağrısıdır (`/dava-takibi:delil-saklama --durum`, slug olmadan) VEYA portföy özetinin bir bölümü olarak `/portfoy-durumu` tarafından çağrılır.

## Bu Skill'in Yapmadıkları

- **Saklamayı uygulamak.** Bildirimi verir; BT/muhafızlar saklar. Skill bir muhafız ayrıldığında işaretler (böylece BT sistem düzeyinde saklayabilir) ama sistemlere ulaşmaz.
- **Tek başına kapsam kararları vermek.** Skill, dava bağlamından kapsam önerir; kullanıcı teyit eder. Kapsam çok geniş = operasyonel yük. Kapsam çok dar = delil imhası riski. Kullanıcının yargısı.
- **İncelemeden otomatik tazeletmek.** `sonraki_tazeleme` geldiğinde bile, tazeleme bildirimi çıkmadan önce kullanıcı kapsam değişikliklerini inceler.
- **Bildirimi göndermek.** Markdown taslak yazar; kullanıcı ev konvansiyonuna göre e-posta / KEP ile gönderir.