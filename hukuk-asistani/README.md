# Hukuk Asistanı

Avukatın günlük işleri için sade bir yapay zekâ asistanı: **dava ve dosya takibi,
sözleşme inceleme ve hazırlama, dilekçe yazımı, hukuki metin özetleme ve genel hukuki
araştırma** — hepsi tek eklentide.

Bu eklenti, teknik konulara hâkim olması gerekmeyen avukatlar için tasarlandı:

- **Kurulum 5 dakika** — beş kısa soru, bitti. Uzun görüşme yok, risk matrisi yok.
- **Ek bağlantı gerektirmez** — hiçbir harici sistem (MCP bağlayıcısı, UYAP entegrasyonu
  vb.) kurmadan, kutudan çıktığı gibi çalışır.
- **Belgelerin senin bilgisayarında** — her şey `Belgeler/Hukuk-Asistani` klasöründe
  düz dosya olarak durur; istediğin programla açabilirsin, kilitli bir sisteme bağımlı
  değilsin.
- **Komut ezberlemek gerekmez** — "yeni bir işçilik davası aldım" veya "şu sözleşmeye
  bak" yazman yeterli; asistan doğru aracı kendisi seçer.

> **Önemli:** Asistanın ürettiği her belge, senin incelemen için bir **taslaktır** —
> hukuki tavsiye veya hukuki sonuç değildir. Kritik noktalar (atıflar, süre hesapları,
> yargı gerektiren tercihler) `[doğrula]` ve `[incele]` etiketleriyle işaretlenir.
> İmzalayan, gönderen, mahkemeye sunan sensin.

---

## Kurulum

Tek seferliktir, yaklaşık 5 dakika sürer.

**1. Claude Code'u edin** *(zaten kuruluysa geç)*

[claude.com/claude-code](https://claude.com/claude-code) adresinden indir. Önünde
Claude'un çalıştığı bir pencere varsa hazırsın demektir.

**2. Eklenti kaynağını tanıt** — Claude'a şunu yaz:

```
/plugin marketplace add omer1616/claude-for-legal-turkish
```

*(İnternetten erişemiyorsan: `claude-for-legal-turkish` klasörünü bilgisayarına indir,
`/plugin marketplace add ` yazıp klasörü pencerenin üzerine sürükle — yol kendiliğinden
dolar.)*

**3. Eklentiyi kur, sonra Claude Code'u kapatıp yeniden aç:**

```
/plugin install hukuk-asistani@claude-for-legal-turkish
```

**4. Kurulumu tamamla:**

```
/hukuk-asistani:ilk-kurulum
```

Beş kısa soru sorar (kim kullanacak, nasıl çalışıyorsun, hangi alanlarda, hangi ilde,
belgeler nereye kaydedilsin) ve hazırsın. Her cevap sonradan değiştirilebilir.

---

## Neler yapar?

| Günlük ihtiyaç | Komut |
|---|---|
| Yeni dava/iş kaydı aç | `/hukuk-asistani:yeni-dosya` |
| Dosyalarım ne durumda? Yaklaşan duruşma ve süreler | `/hukuk-asistani:dosyalarim` |
| Dosyaya gelişme notu ekle (duruşma, tebligat, görüşme) | `/hukuk-asistani:dosya-notu` |
| Sözleşme incele — riskler, eksikler, müzakere önerileri | `/hukuk-asistani:sozlesme-incele` |
| Sıfırdan sözleşme taslağı hazırla | `/hukuk-asistani:sozlesme-hazirla` |
| Dilekçe veya ihtarname taslağı yaz | `/hukuk-asistani:dilekce` |
| Karar, rapor veya sözleşmeyi özetle | `/hukuk-asistani:ozetle` |
| Hukuki soru araştır — mevzuat, içtihat, güncel eşikler | `/hukuk-asistani:arastir` |
| Bu listeyi tekrar göster | `/hukuk-asistani:yardim` |

### Günlük kullanım örnekleri

Komutlarla uğraşmak istemiyorsan doğal cümle yeterli:

- *"Yeni bir kira davası aldım, müvekkil Ayşe Demir, kiracı çıkmıyor"* → dosya açılır
- *"Bugün Yılmaz dosyasının duruşması vardı, tanıklar dinlendi, yeni duruşma 12 Eylül"* → dosyaya not düşülür, tarih takvime işlenir
- *"Bu hafta neyim var?"* → yaklaşan duruşma ve sürelerin listesi
- *"Müvekkil şu hizmet sözleşmesini gönderdi, imzalasın mı?"* → madde madde risk raporu
- *"Kiracıya tahliye ihtarnamesi lazım"* → noter formatında taslak
- *"Şu Yargıtay kararı bizim dosyayı etkiler mi?"* → özet + değerlendirme
- *"İşe iade davasında arabuluculuk şartı neydi?"* → kaynak etiketli araştırma cevabı

---

## Belgelerin nerede saklanır?

Kurulumda seçtiğin klasörde (varsayılan: `Belgeler/Hukuk-Asistani`):

```
Hukuk-Asistani/
├── dosyalar/          # her dava/iş için bir klasör — kayıt, notlar, o dosyanın belgeleri
├── sozlesmeler/       # sözleşme taslakları ve incelemeler
├── dilekceler/        # dilekçe taslakları
├── ozetler/           # belge özetleri
└── arastirmalar/      # kaydedilen araştırma notları
```

Hepsi düz metin dosyasıdır — Word'e kopyalayabilir, yedekleyebilir, dilediğin gibi
taşıyabilirsin. Asistan hiçbir veriyi bu klasörün ve Claude oturumunun dışına
göndermez; Claude ile paylaştığın içeriğin Anthropic'in hizmetinde işlendiğini
unutma — gizlilik hassasiyeti yüksek belgelerde büronun/kurumunun politikasına uy.

---

## Bilmen gerekenler (dürüst sınırlar)

- **UYAP'a bağlı değildir.** Duruşma günleri ve süreler sen söyledikçe kaydedilir;
  kalemin verdiği yeni bir günü asistan kendiliğinden göremez.
- **Süre hesapları daima teyit ister.** Asistan hesabı gösterir ve `[doğrula — süre
  hesabı]` diye işaretler; son güne güvenmeden önce kontrol et. Süre kaçırmanın
  telafisi yoktur.
- **İçtihat künyesi uydurmaz.** Emsal karar numarası ancak gerçek bir kaynaktan
  geldiyse yazılır; aksi halde "emsal için Lexpera/Kazancı taraması gerekir" der. Bu
  bir eksiklik değil, güvenlik özelliğidir.
- **Güncel oranlar ve eşikler** (harçlar, parasal sınırlar, faiz) için asistan web
  araması yapar ve kaynağını etiketler; yine de resmî kaynaktan doğrulamadan işlem
  yapma.
- Lexpera/Kazancı gibi bir araştırma aracını Claude'a bağlarsan asistan onu
  kendiliğinden kullanır — ama hiçbiri kurulum için gerekli değildir.

## Sık sorulanlar

**Daha kapsamlı bir şeye ihtiyacım olursa?**
Bu marketplace'te alan bazlı gelişmiş eklentiler de var (`dava-takibi`,
`ticari-hukuk`, `is-hukuku`…). Hukuk Asistanı'ndan onlara geçiş kolaydır; dosya
kayıtların düz metin olduğu için taşınabilir.

**Yanlış cevap verirse?**
Her çıktı taslaktır ve işaretli yerler ("`[doğrula]`", "`[incele]`") tam da bu yüzden
vardır. Bir çıktı sürekli yanlış hissettiriyorsa `/hukuk-asistani:ilk-kurulum --redo`
ile profili güncelle veya asistan içinde ne istediğini tarif et — düzeltir.

**Ekipçe kullanabilir miyiz?**
Her kullanıcı kendi bilgisayarında kurar. Çalışma klasörünü ortak bir dizine (ör.
büro ağ sürücüsü) yönlendirerek dosya kayıtlarını paylaşabilirsiniz — eşzamanlı
düzenlemede çakışmaya dikkat edin.
