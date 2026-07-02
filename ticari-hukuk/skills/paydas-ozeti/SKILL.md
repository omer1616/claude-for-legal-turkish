---
name: paydas-ozeti
description: >
  Bir sözleşme incelemesini iş paydaşının gerçekten okuyacağı bir özete çevirir.
  Bir hukuk notu değil — "bunu imzalayabilir miyim ve ne bilmem gerekiyor"
  sorusunun iki dakikalık cevabı. Kullanıcı "iş için özetle", "bunu [paydaş] için
  yaz", "bunu satın almaya açıkla", "hukuki olmayan özet" dediğinde, veya bir
  inceleme bitip hukuk dışına gitmesi gerektiğinde kullan.
---

# Paydaş Özeti

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

Bu sözleşmeyi isteyen iş sahibi bir hukuk notu istemiyor. Şunu bilmek istiyor:
imzalayabilir miyim, kanca nerede ve ne yapmam gerekiyor. Bu skill tamamlanmış bir
incelemeyi alıp bunu haline getirir.

## Hangi taraf?

Alttaki inceleme notu ya satış-tarafı ya da satın alma-tarafı oyun kitabına karşı
çalıştırıldı. Bu çerçevelemeyi taşıyın. Bir satın alma-tarafı özeti iş sahibine "işte
aldığımız şey ve vazgeçtiğimiz şey" der; bir satış-tarafı özeti onlara "işte
sattığımız şey ve sorumlu olduğumuz şey" der. İncelemenin hangi tarafta
çalıştırıldığını kontrol edin (inceleme notunun en üstünde belirtilmiş olmalı) ve
sesle eşleştirin. Notta bariz değilse, özetlemeden önce avukata sorun.

## Kitle kalibrasyonu

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` →
`## Ev tarzı` → paydaş özetlerini kimin okuduğunu, ne kadar uzun olması gerektiğini
okuyun. Belirtilmemişse, şuna varsayılan: satın alma veya bir departman başkanı,
en fazla iki paragraf, hukuki terim yok.

Farklı kitleler farklı özetlere ihtiyaç duyar:

| Kitle | Umursadığı | Umursamadığı |
|---|---|---|
| **Satın alma** | Fiyat, yenileme mekaniği, onay yönlendirmesi | Sorumluluk tavanı yapısı |
| **Departman başkanı (bütçe sahibi)** | Ekipleri kullanabilir mi, bozulursa ne olur, maliyet | Tazminat kapsamı |
| **Mali işler** | Toplam sahiplik maliyeti, yenileme fiyat riski, bilanço-dışı taahhütler | Uygulanacak hukuk |
| **Güvenlik / BT** | Veri işleme, alt işleyenler, sertifikasyonlar, verinin nerede yaşadığı | Geri kalan her şey |
| **Yönetici sponsor** | Bu bizi utandırır mı, hukuk bir engel mi | Detaylar |

Bağlamdan belli değilse bunun kim için olduğunu sorun.

## Özet

### Uzunluk sınırı — zorunlu

Özet şudur:
- **Bir paragraf** sonuç ve bunun ne olduğu için (iş şartları, düz Türkçe)
- **Bir paragraf** kanca için — kimse şimdi söylemezse paydaşın sonra şaşıracağı şey
- **2-3 maddelik bir kontrol listesi** paydaşın gerçekte yapması gereken şey için (en
  fazla üç madde; dördüncüsünü istiyorsanız, ilk üçü yeterince sıkı değil)
- **Onay zamanlamasıyla tek satırlık bir kapanış**

**Toplamda 200 kelimenin altında.** Daha fazla yazıyorsanız, paydaşın ihtiyacı
olmayan detay ekliyorsunuz demektir — bunun için notları var. Bu, paydaş yanıtla
vurmadan önceki hızlı okumadır.

Kapanış üçüncü bir paragraf gerektiriyorsa, bunu kontrol listesine katlayın. Kapanışın
dördüncü bir bloğa büyümesine izin vermeyin.

### Alıntı kapsamı — disiplin

Bir sözleşme maddesi alıntılarken (özette, "kanca" paragrafında veya kontrol
listesinde), **tam koşullu cümleyi** alıntılayın, kısaltılmış bir versiyonu değil.
"Sipariş Formunda açıkça belirtilmedikçe, promosyonel veya tek seferlik fiyatlı
aboneliklerin yenilenmesi liste fiyatına döner" diye okunan bir madde, "yenileme
liste fiyatına döner"den farklı bir şey ifade eder — kısaltma koşulu düşürür ve
şartın ne yaptığını yanlış temsil eder.

Tam koşullu alıntı özetin uzunluk sınırına sığmıyorsa, kısaltmak yerine
parafraz edin. "Promosyonel fiyatlandırma için, yenileme listeye döner" adil bir
parafrazdır; "yenileme listeye döner" değildir — istisnayı kurala yükseltir.

### Format

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
`## Çıktılar`'dan iş-ürünü başlığını ekle (role göre farklılaşır — bkz. `## Bunu
kim kullanıyor`).

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar]
<!-- Meslek sırrı çemberinin dışına (ör. bir iş paydaşına, karşı tarafa veya
tedarikçiye) iletiliyorsa yukarıdaki başlığı kaldırın. İletmeden önce yargı çevreniz
ve dosyanız için doğru işareti teyit edin. -->

**[Karşı taraf] [Sözleşme türü]** — [İMZAYA HAZIR | DEĞİŞİKLİK GEREKİYOR | ENGELLENDİ]

[Bir paragraf: bu sözleşme iş şartlarıyla ne yapıyor. "Bulut tabanlı analitik
sağlanması için Ana Hizmet Sözleşmesi" değil — "bu, pazarlama ekibinin istediği
dashboard aracının sözleşmesi."]

[Bir paragraf: paydaşın bilmesi gereken şey. Varsa kanca. Kimse şimdi söylemezse
sonra şaşıracakları şey. Ör. "Dikkat: bu her yıl otomatik yenileniyor ve 60 gün
önceden iptal etmemiz gerekiyor. Takipçiye ekledim ama bilmenizi istedim." Ya da:
"Temiz sözleşme, sürpriz yok, imzaya açık."]

<!-- Bu sözleşme için yenileme-takibi gerçekten çalıştırılmadıysa "Takipçiye
ekledim" (veya eşdeğeri) demeyin — aşağıdaki Takipçi kayıtlarını iddia etmeden önce
doğrula bölümüne bakın. -->

**Takipçi kayıtlarını iddia etmeden önce doğrulayın.** Özet "Takipçiye ekledim" (veya
eşdeğeri — "takipte," "izleniyor," "hatırlatma kurdum") demeden önce, bu sözleşme
için yenileme-takibi'nin gerçekten çalıştırıldığını doğrulayın. Çıktı klasörünü veya
dosya klasörünü bu karşı taraf/sözleşmeyi adlandıran bir yenileme-takibi çıktısı
için kontrol edin. Yoksa:

- Ya önce bu sözleşme için yenileme-takibi'ni çalıştırın, sonra özeti yazın.
- Ya da takipçi kaydını iddia etmeden özeti yazın ve bir eylem maddesi ekleyin:
  "Yenileme takipçisine ekle — henüz yapılmadı."

Var olmayan bir takipçi kaydı olduğunu iddia etmek, güvenceyi atlamaktan kötüdür.
Paydaş sonra asla çalmayacak hatırlatmaya güvenir. Doğru ifade "takipte"yse, skill
takipçiyi çalıştırır. "Takviminize eklemelisiniz — henüz kaydetmedim"se, bunu söyleyin.

**Ne yapmanız gerekiyor:**
- [ ] [Eylem maddesi, varsa — "ekibin verinin AB'de yaşamasıyla sorunu olmadığını
  teyit et" ya da "hiçbir şey — imza için yönlendireceğim"]

**Onay:** [kim onaylıyor ve beklenen zamanlama]
```

### Neyin çevrileceği

| Hukuki bulgu | İş çevirisi |
|---|---|
| "Sorumluluk 12 aylık ücretle sınırlı" | "Bir şey bozarlarsa, kurtarabileceğimiz en fazla onlara ödediğimiz bir yıllık tutar." |
| "Serbestçe fesih yok" | "İmzaladıktan sonra, tüm süre boyunca kilitliyiz — kullanmayı bırakırsak sadece iptal edemeyiz." |
| "60 gün bildirimle otomatik yenileme" | "Bu her yıl otomatik yenileniyor. İptal etmek için, yenileme tarihinden iki ay önce onlara söylememiz gerekiyor." |
| "Fikri mülkiyet tazminatı yok" | "Biri bu aracın kendi patentlerini ihlal ettiğini iddia ederek bize dava açarsa, satıcı bizi savunmakla yükümlü değil." |
| "Alt işleyen listesi ifşa edilmemiş" | "Verimize hangi başka şirketlerin onlar üzerinden erişimi olacağını bilmiyoruz." |
| "Fesihten sonra 30 gün içinde veri silme" | "İptal ettiğimizde, verimizi bir ay içinde siliyorlar. O zamandan önce ihtiyacınız olan her şeyi dışa aktarın." |
| "SLA kredileri aylık ücretin %10'uyla sınırlı" | "Hizmet çökerse, küçük bir kredi geri alırız. Kesintinin işletmeye maliyetini karşılamaz." |

### NELERİN dahil EDİLMEMESİ gerektiği

- Bölüm numaraları
- Tırnak içinde tanımlanmış terimler
- "Tazminat" kelimesi ("bize karşı korurlarsa" / "onlara karşı korursak" deyin)
- "Şu kadarki" (notwithstanding) kelimesi
- Renkli noktalarla risk matrisleri (bu paydaş özellikle daha önce bunları
  istemedikçe)
- Bunun hukuki tavsiye olmadığına dair çekinceler — paydaş kimin gönderdiğini bilir

## İnceleme sorunlar bulduğunda

İncelemenin 🔴 veya 🟠 sorunları varsa, özet yine de iki paragraf olmalı — ama ikinci
paragraf "işte geri ittiğimiz şey ve neden."

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar]
<!-- Meslek sırrı çemberinin dışına iletiliyorsa yukarıdaki başlığı kaldırın. -->

**[Karşı taraf] [Sözleşme türü]** — DEĞİŞİKLİK GEREKİYOR

[Ne olduğu, bir paragraf.]

Bu hazır olmadan önce [N] şey hakkında onlara geri dönüyoruz. Ana olan: [kritik
sorun düz Türkçe — "verimizi ürünlerini geliştirmek için kullanma hakkı istiyorlar,
bu da rakiplerimizin örneğinin bizim verimizden akıllanacağı anlamına geliyor"]. Bunu
çıkarmalarını istedik. [Gerçekçi değerlendirme: "Muhtemelen kabul edecekler" /
"Bu bir tıkanma noktası olabilir — sizi bilgilendireceğim."]

**Ne yapmanız gerekiyor:**
- [ ] Henüz hiçbir şey — onlardan geri geldiğinde size haber vereceğim.
  YA DA
- [ ] [Yapmaları gereken iş kararı: "X konusunda esnemezlerse, Y'ye razı mısınız,
  yoksa vazgeçiyor muyuz?"]
```

## Devirler

**satici-inceleme / saas-inceleme'den:** Bu skill'ler tam notu üretir. Bu skill
notu okur ve sıkıştırır. Sözleşmeyi yeniden incelemeyin — incelemeyi okuyun.

**Paydaşa:**
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'nin
söylediği kanal üzerinden. Slack ise, 150 kelimenin altında tutun. E-posta ise,
yukarıdaki format olduğu gibi iyidir.

## Eskalasyon-dağılım mutabakatı

Yukarı akış incelemesi bir-den-çoğa üreticidir: farklı bulgular genelinde beş
eskalasyon hedefi adlandırabilir (Yardımcı BHM, Bilgi Güvenliği Sorumlusu, Veri
Koruma Sorumlusu, CFO, iş birimi sahibi). eskalasyon-isaretleyici tek seferde bir
bulguyu yönlendirir. Bir mutabakat adımı olmadan, Yardımcı BHM notu görür ve diğer
dördü asla görmez.

Özeti üretmeden önce, yukarı akış inceleme notunu okuyun ve eskalasyonları sayın:

1. **İncelemenin adlandırdığı eskalasyon hedeflerini sayın.** İncelemenin sonundaki
   yönlendirme/eskalasyon bloğuna, veya bulgu-başına "şuna eskale et: [X]"
   etiketlerine bakın. Onaylayıcı adına göre tekilleştirin — iki bulgu için
   adlandırılan bir onaylayıcı bir kez sayılır.
2. **Gerçekten yönlendirilen eskalasyonları sayın.** İnceleme yazıldıktan sonra
   eskalasyon-isaretleyici tarafından üretilen `eskalasyon-*.md` taslakları için
   inceleme klasörünü (veya dosya klasörünü) okuyun. Her taslak bir onaylayıcıyı
   adlandırır.
3. **Mutabık kıl.** N onaylayıcı adlandırıldıysa ve M taslak varsa, (N − M)
   eskalasyon yönlendirilmemiştir.

Özette — kancanın altında, kontrol listesinin üstünde — kısa bir mutabakat bloğu
dahil edin:

```markdown
**Eskalasyon durumu:** [N]'den [M]'i eskalasyon hedefi yönlendirildi. Şunlar
yönlendirilmedi ve eylem gerektiriyor:
- [Onaylayıcı adı] — [onları adlandıran bulgu hakkında tek satır]
- [Onaylayıcı adı] — [tek satır]
```

Hepsi N yönlendirildiyse:
```markdown
**Eskalasyon durumu:** [N]'den [N]'i eskalasyon hedefi yönlendirildi.
```

Yukarı akış incelemesi hiçbir eskalasyon yüzeye çıkarmadıysa, bloğu atlayın.

**Bir paydaşın adı tanımayacağı için adlandırılmış bir onaylayıcıyı mutabakattan
çıkarmayın.** İş paydaşları genellikle Veri Koruma Sorumlusu'nun veya Bilgi Güvenliği
Sorumlusu'nun kim olduğunu bilmez. Mutabakat iç bakışlıdır — özeti gönderen avukata
tüm yönlendirmenin yapılıp yapılmadığını söyler, paydaşa değil. Paydaşa-dönük özet
dar kalmalıysa, mutabakat bir "yönlendirme durumu" alt bilgisinde veya ekli bir notta
yaşayabilir — ama var olmalıdır. Yönlendirmenin tamamlandığını ima eden bir özet
tamamlanmamışken hiç özetten kötüdür.

**Kelime-sayısı istisnası.** Eskalasyon mutabakat bloğu 200 kelime sınırından
muaftır. Özet gövdesinde uzunluk-sınırı disiplini kalır; mutabakat anlatı değil,
tutarlılık işidir.

**eskalasyon-isaretleyici taslakları mevcut olmadığında.** Yukarı akış incelemesi
onaylayıcıları adlandırdı ve klasörde taslak yoksa, sayımı M = 0 olarak ele alın.
Mutabakat bloğu N'in hepsini yönlendirilmemiş olarak listeler. Bu bulgunun kendisidir.

## Ton üzerine bir not

Paydaşlar hukuk hakkında iki şey hatırlar: beni engelledi mi ve mantıklı mıydı? Bu
skill hukukun mantıklı olma yoludur. Bir dosyaya not yazar gibi değil, akıllı bir
meslektaşa kahve içerken anlatıyormuş gibi yazın.

Dürüst özet "bu iyi, imzala"ysa, bunu söyleyin. Temiz bir incelemeyi kapsamlı
görünmesi için üç paragrafa doldurmayın.
