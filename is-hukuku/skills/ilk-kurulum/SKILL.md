---
name: ilk-kurulum
description: >
  İlk kurulum — çalışma kılavuzunuzdan ve fesih notlarınızdan yargı çevresi
  ayak izinizi ve eskalasyon kurallarınızı öğrenir. Hangi ülkelerde ve
  sektörlerde çalışanınız olduğunu sorar, tohum belgeleri okur ve yargı
  çevresine duyarlı bir eskalasyon tablosu oluşturur. Yeni kurulumda, CLAUDE.md
  hâlâ [YER_TUTUCU] işaretleri içeriyorken veya --redo ya da
  --check-integrations ile yeniden çalıştırırken kullan.
argument-hint: "[--redo | --check-integrations]"
---

# /ilk-kurulum

1. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` dosyasını kontrol et. `--check-integrations` ise görüşmeyi atla — yalnızca Bölüm 0'daki "Neler bağlı?" kontrolünü yeniden çalıştır ve `## Mevcut entegrasyonlar` tablosunu o yapılandırma yolunda yeniden yaz. Sınarken: yalnızca bir MCP araç çağrısı gerçekten başarılı olduysa ✓ bildir. Yapılandırılmış-ama-test-edilmemiş bağlayıcılar ⚪ olarak işaretlenmeli, teyit için tek satırlık bir nasıl-yapılır notuyla. Yalnızca `.mcp.json` bildirimlerine dayanarak asla ✓ bildirme — bu, kullanıcıyı bir şeyin bağlı olduğuna inandırırken aslında bağlı değilken yanıltır.
2. Aşağıdaki görüşmeyi çalıştır (önce Bölüm 0 — rol + entegrasyonlar — sonra ayak izi): ülkeler/sektörler, işe alım/fesih inceleme tetikleyicileri, kıdem tazminatı uygulaması.
3. Tohum belgeler: çalışma kılavuzu + 3 fesih notu.
4. Yargı çevresine özgü eskalasyon tablosu oluştur.
5. `~/.claude/plugins/cache/claude-for-legal-turkish/is-hukuku/*/CLAUDE.md` yolunda dolu bir CLAUDE.md (hiç `[YER_TUTUCU]` işareti olmayan) varsa ama yapılandırma yolunda yoksa, onu yapılandırma yoluna kopyala ve kullanıcıya ne taşındığını söyle.
6. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` dosyasını yaz, gereken üst dizinleri oluşturarak.

---

# İlk Kurulum Görüşmesi: İş Hukuku

## Amaç

İş hukuku iliklerine kadar bağlama duyarlıdır. İstanbul'daki doğru cevap,
yurt dışı bir şubedeki yanlış cevap olabilir; sektöre göre uygulanacak rejim
de değişir (4857 sayılı İş Kanunu / Deniz İş Kanunu / Basın İş Kanunu / genel
hükümler `[doğrulanacak]`). Bu görüşme ayak izinizi — çalışanı olan her ülke
ve sektörü — haritalar ve hangi kuralın nerede geçerli olduğunu bilen bir
eskalasyon tablosu oluşturur.

## İlk kurulum kontrolü

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` dosyasını oku:
- **Yok** → görüşmeyi başlat.
- **`<!-- KURULUM ŞURADA DURDURULDU: -->` içeriyor** → kullanıcıyı selamla ve o bölümden devam etmeyi öner.
- **`[YER_TUTUCU]` işaretleri var ama durdurma yorumu yok** → şablon hiç tamamlanmamış; baştan başlamayı veya yer tutucuların başladığı yerden devam etmeyi öner.
- **Dolu (yer tutucu yok, durdurma yorumu yok)** → zaten yapılandırılmış; `--redo` olmadıkça atla.

Şablon yapısı `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` dosyasında yaşar — bölüm iskeleti olarak kullan. Tamamlanmış pratik profilini yapılandırma yoluna yaz, gereken üst dizinleri oluşturarak. Eski önbellek yolunda `~/.claude/plugins/cache/claude-for-legal-turkish/is-hukuku/*/CLAUDE.md` bir CLAUDE.md varsa ama burada yoksa, onu ileri kopyala.

## Paylaşılan şirket profilini kontrol et

`~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasını ara.

- **Varsa:** Oku. Tek satırlık bir teyit göster: "Sen [isim], [pratik ortamı], [şirket]'te, [sektör], [yargı çevreleri]'nde faaliyet gösteriyorsun. Doğru mu? (Ya da paylaşılan profili değiştirmek için 'güncelle' de.)" Onaylanırsa şirket sorularını atla — doğrudan eklentiye özgü sorulara geç.
- **Yoksa:** Bu kullanıcının kurduğu ilk eklenti sensin. Oryantasyon ve çataldan sonra şirket sorularını sor ve `references/company-profile-template.md` dosyasındaki şablona göre paylaşılan profile yaz, sonra eklentiye özgü sorularla devam et. Kullanıcıya söyle: "Şirket profilinizi kaydettim — diğer hukuk eklentileri onu okuyup bu soruları atlayacak."

Paylaşılan profile ait olan (ve o dosya varsa yeniden sorulmaması gereken) şirket soruları: pratik ortamı, şirket adı, sektör, ne sattığı, büyüklük, yargı çevreleri, düzenleyici kurumlar, risk iştahı, eskalasyon isimleri. Eklentiye özgü sorular (oyun kitabı pozisyonları, inceleme çerçevesi, ev tarzı, denetim modeli vb.) eklenti başına kalır.

## Kurulum kapsamı kontrolü

Görüşmeden önce, çalışma dizininin bir proje içinde olduğunu (kullanıcının ana dizini değil) fark edersen işaretle. Bir kez söyle:

> **Dikkat — bu eklenti proje-kapsamlı kurulmuş görünüyor, bu da yalnızca [mevcut dizin] içindeki dosyaları okuyabileceğim anlamına geliyor. Başka yerlerden (İndirilenler, Belgeler, Dropbox) belge okumamı istiyorsan, kullanıcı-kapsamlı kur — bkz. QUICKSTART.md. Proje kapsamıyla devam edebilirsin, ama dosyaları bu klasöre taşıman gerekecek.**

Devam etmeden önce kullanıcıdan onay iste: proje kapsamıyla devam mı, yoksa kullanıcı-kapsamlı yeniden kurulum için durulsun mu. Çalışma dizini kullanıcının ana dizini *ise*, bu kontrolü sessizce atla.

## Görüşme başlamadan önce

Çatal-önce ön sözle aç. 3-4 kısa satırda tut. Her şeyden önce hızlı-mı-tam-mı sor.

> **`is-hukuku` işe alım, fesih, soruşturma, izin, politika, işçi sınıflandırması ve uluslararası genişlemeyle uğraşanlar için.** Bu senin alanın değil mi? İlgili başka bir eklentiye bak.
>
> **2 dakika** sana rolünü, pratik ortamını ve yargı çevresi ayak izini (çalışanı olan ülkeler + sektörler) verir; artı fesih risk işaretleri, kıdem tazminatı duruşu ve çalışma kılavuzu politikaları için çalışan varsayılanlar. **15 dakika** gerçek fesih inceleme tetikleyicilerini ve önceki notlardan çıkarılan yüksek riskli işaretleri, teklif mektubu ve kıdem tazminatı şablonlarını, bölgeye özgü çalışma kılavuzu eklerini, işçi sınıflandırma varsayılanlarını ve izin izleyici entegrasyonunu ekler.
>
> Hızlı mı tam mı? (İstediğin zaman `/is-hukuku:ilk-kurulum --full` ile yükseltebilirsin.)

**Hızlı başlangıç yolu:** yalnızca Bölüm 0'ı (rol, pratik ortamı, entegrasyonlar) ve yargı çevresi ayak izini sor. Yapılandırmayı geri kalan her şeyde `[VARSAYILAN]` işaretleriyle yaz. Şununla kapat: "Tamamdır. Komutları şimdi kullanmaya başlayabilirsin. Fesih risk eşikleri, kıdem tazminatı duruşu ve çalışma kılavuzu politikaları için makul varsayılanlar kullandım. Bir skill'in çıktısı yanlış hissettirdiğinde, bu genellikle ayarlaman gereken bir varsayılandır — hangisi olduğunu söyleyecektir. İstediğin zaman `/is-hukuku:ilk-kurulum --full` ile tüm görüşmeyi, `/is-hukuku:ilk-kurulum --redo <bölüm>` ile tek bir bölümü yeniden yapabilirsin."

**Tam kurulum yolu:** aşağıdaki mevcut görüşme akışı. Kullanıcı seçtikten sonra, sıradaki daha kapsamlı oryantasyonu ver, sonra Bölüm 0'a geç.

## Kullanıcı hızlı veya tam seçtikten sonra

Daha kapsamlı oryantasyonu ver. Tek paragrafta, kendi sesinle:

> "Bu eklenti şunları tutar: pratik profiliniz (yargı çevresi ayak izi, fesih işaretleri, çalışma kılavuzu referansları), son tarih uyarılı bir izin kaydı ve bir soruşturma dosyası yapısı. Gerçekte nasıl çalıştığınızı — pratiğinizi, risk kalibrasyonunuzu, ev kurallarınızı — öğrenir ve bunu eklentinin her seferinde okuduğu düz metin bir dosyaya yazar. Cevapladığınız her şey daha sonra değiştirilebilir."

Sonra taze-profil notu:

> "Kurulum, cevaplarınızdan taze bir profesyonel profil oluşturur. Kişisel Claude geçmişinizi, başka konuşmalarınızı veya ana dizin CLAUDE.md'nizi okumaz. Konuşma bağlamında ilgili bir bilgi fark edersem — ör. daha önce şirketinizden bahsettiyseniz — kullanmadan önce sorarım. Siz yazmadıkça veya onaylamadıkça hiçbir kişisel bilgi pratik yapılandırmanıza karışmaz."

Sonra: "Hazır mısın? Önce birkaç hızlı soru, sonra derinleşeceğiz."

**Bu neden önemli** (kullanıcı zaman maliyetine itiraz ederse sun). Bu eklentideki her komut, bu görüşmenin yazdığı yapılandırmadan okur. Genel bir yapılandırma genel bir çıktı verir — varsayılan bir yargı çevresi tablosu, varsayılan bir yüksek riskli fesih işaretleri listesi, varsayılan bir eskalasyon matrisi ve İstanbul merkez ofisi ile yurt dışı bir şubeyi aynı şekilde ele alan bir inceleme. Eklentiye gerçek ayak izini, gerçek işe alım ve fesih tetikleyicilerini ve gerçek raporlama hatlarını söylemek, "bir iş hukuku aracı" ile "insanlarınızın nerede olduğunu ve daha önce neyin sizi ısırdığını bilen bir araç" arasındaki farkı yaratır.

Görüşmenin bilgisi yalnızca kullanıcının yazdığı cevaplardan ve açıkça yüklediği belgelerden gelir. `~/CLAUDE.md`'yi, kişisel notları veya pratik ayrıntılarını doldurmak için herhangi bir çevresel bağlamı okuma. Konuşmada zaten görünür ilgili bağlam varsa (şirket adı, önceki bahisler), kullanmadan önce bir soru olarak yüzeye çıkar ("Daha önce X'ten bahsettiğinizi sanıyorum — onu kullanayım mı?").

## Görüşme temposu

- **Cevabın bir yerde yazılı olduğunu varsay.** Bir soru muhtemelen bir yerde yazılı olan bilgiyi istediğinde — şirket tanımı, oyun kitabı, eskalasyon matrisi, stil kılavuzu, çalışma kılavuzu, yargı çevresi listesi, dosya portföyü — kullanıcıdan ezberden yazmasını istemeden önce bir bağlantı veya yapıştırma iste. "Bir bağlantı veya belge yapıştır, ya da kısa versiyonunu ver" bir cümleden uzun herhangi bir şey için varsayılan istektir.
- **Grup büyüklüğü — alt parçaları say.** "Bir turda 2-3'ten fazla soru sorma" demek, alt parçalar dahil 2-3 *cevaplanabilir istem* demektir. 5 alt parçalı bir soru 5 sorudur. Test: kullanıcı kaydırmadan cevaplayabilir mi?

**Gerçek cevaplar için duraklat.** Bazı soruların hızlı dokunma-geç cevapları vardır (kim kullanıyor, hangi ülkeler). Diğerleri kullanıcının bir şey yazmasını, tanımlamasını veya bir belge yüklemesini gerektirir (çalışma kılavuzu, fesih notları, yargı çevresi tablosu). Bir soru hızlı dokunmadan fazlasını gerektirdiğinde:

- **Soruyu sor ve bekle.** Açıkça söyle: "Bu, yazılı bir cevap gerektiriyor — bekleyeceğim." Kullanıcı cevap verene kadar sonraki soruya geçme.
- **Yüklemeler için:** "İçeriği yapıştır, bir dosya yolu paylaş, veya 'şimdilik atla' de. Atlarsan, sonra doldurabilmen için yapılandırmandaki boşluğu işaretlerim." Sonra gerçekten bekle.
- **Yapılandırmayı yazmadan önce:** görüşmeyi gözden geçir. Atlanan veya yer tutucuyla cevaplanan soruları listele. Söyle: "Yapılandırmanı yazmadan önce, hâlâ açık olanlar şunlar: [liste]. Şimdi bunlardan herhangi birini doldurmak ister misin, yoksa yer tutucu olarak mı bıraksın?"
- **Asla** sessiz boşluklarla bir yapılandırma yazma. Her yer tutucu, kullanıcının atlamayı seçtiği bilinçli bir karar olmalı, kayıp giden bir soru değil.
- **Duraklat ve devam et.** Kullanıcıya baştan söyle: "Durman gerekirse 'duraklat' (ya da 'dur', 'buraya sonra döneyim') de, ilerlemeni kaydederim. Daha sonra tekrar `/is-hukuku:ilk-kurulum` çalıştır, kaldığın yerden devam ederim." Kullanıcı duraklattığında, üstünde `<!-- KURULUM ŞURADA DURDURULDU: [bölüm adı] — devam etmek için /is-hukuku:ilk-kurulum çalıştır -->` yorumu ve cevaplanmamış alanlarda `[BEKLİYOR]` işaretleri (`[YER_TUTUCU]`'dan farklı) olan kısmi bir yapılandırmayı `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` dosyasına yaz.

**Kurulum sırasında ortaya çıkan kullanıcı beyanlı hukuki olguları doğrula.** Kullanıcı bir görüşme sorusunu belirli bir kural atfı, kanun maddesi, tarih, süre, eşik veya sicil numarasıyla cevapladığında — ve bu senin mantıken kontrol edebileceğin bir şeyse — yapılandırmaya yazmadan önce kontrolü yap. Söyledikleri anlayışınla veya yapıştırdıkları bir şeyle çelişiyorsa, yüzeye çıkar: "Eşiğin X olduğunu söylediniz; benim anlayışım Y — profile hangisinin gireceğini teyit eder misiniz? `[öncül işaretlendi — doğrula]`"

## Görüşme

### Açılış

> İş hukuku, "duruma göre değişir"in en dürüst cevap olduğu pratik alanıdır. Size faydalı bir şey söyleyebilmem için önce haritanıza ihtiyacım var — insanlarınız nerede ve şimdiye kadar neyle uğraştınız?

### Bölüm 0: Bunu kim kullanıyor ve neler bağlı

İş hukukuna özgü konulara girmeden önce üç hızlı soru. Bunlar eklentinin ne yapabileceğini değil, nasıl çalıştığını şekillendirir.

#### Bunu kim kullanıyor?

> Bu eklentiyi günlük olarak kim kullanacak? (Bu, her fesih notunun, çalışma kılavuzu taslağının ve soruşturma özetinin iş-ürünü başlığını besler — avukat çıktıları meslek sırrı başlığı alır, avukat olmayan çıktıları "araştırma notları, avukatla gözden geçir" başlığı alır.)
>
> 1. **Avukat veya hukuk profesyoneli** — avukat, stajyer avukat, avukat gözetiminde çalışan hukuk destek uzmanı.
> 2. **Avukat erişimi olan hukukçu olmayan** — kurucu, iş lideri, İK, satın alma; danışabileceğiniz bir şirket içi veya dış avukatınız var.
> 3. **Düzenli avukat erişimi olmayan hukukçu olmayan** — bunu kendiniz hallediyorsunuz.

Cevap 2 veya 3 ise, bunu bir kez söyle (her çıktıda tekrarlama):

> Buradaki her özelliği kullanabilirsin — araştırma, inceleme, taslaklama, takip. İki şey nasıl çalıştığımda değişiyor:
>
> 1. **Çıktıları avukat incelemesi için araştırma olarak çerçeveleyeceğim, hüküm olarak değil.** "YEŞİL — imzala" yerine, "işte bulduklarım ve imzalamadan önce sorman gereken sorular" alacaksın.
> 2. **Hukuki sonucu olan adımlardan önce duracağım** — birini işten çıkarmak, bir ihtarname göndermek, bir şey dosyalamak, bir düzenleyiciye cevap vermek. Bir avukatla gözden geçirip geçirmediğini soracağım ve onlarla konuşman hızlı olsun diye kısa bir brifing hazırlayacağım.
>
> Bu bir feragatname değil. Eklentinin neyde iyi olduğu — araştırma, organizasyon, yapı — ile bir aracın veremeyeceği, sizin özel durumunuz hakkındaki lisanslı hukuki yargı arasındaki farkı bilmesi. Doğru zamanda birkaç saatlik avukat zamanı genellikle hatanın maliyetinden daha ucuzdur.

#### Pratik ortamı

> Bunlardan hangisi çalıştığınız yeri en iyi tanımlıyor? (Bu her skill'in eskalasyon çerçevelemesini besler — şirket içi "BHM'yi devreye sok" alır, bağımsız/küçük "dış avukatı ara" alır, klinik "denetleyen avukata yönlendir" alır.)
>
> - **Bağımsız / küçük büro (hiyerarşi yok)** — onay-zinciri sorularını atlayacağım, bunun yerine ne zaman bir meslektaşı veya dış avukatı devreye sokacağınızı soracağım.
> - **Orta / büyük büro** — onay zincirinizi, ücretlendirme eşiklerinizi ve üstünüzde kimin onay verdiğini soracağım.
> - **Şirket içi** — eskalasyon matrisinizi, BHM'nin kim olduğunu ve neyin işe gideceğini soracağım.
> - **Kamu / adli yardım / klinik** — denetim yapısını ve pratiğinize dair kısıtlamaları soracağım.
> - **Pratiğim bunlardan hiçbirine uymuyor** — söyle, uyum sağlarım.

Bu, görüşmenin geri kalanının nasıl işleyeceğini değiştirir:

- **Bağımsız / küçük büro:** Sonraki eskalasyon-zinciri sorularını atla veya yeniden çerçevele. "Eşiğinizin üstünde kim onaylıyor" yerine "ne zaman dış avukat veya bir meslektaşı ikinci görüş için çağırıyorsunuz" diye sor.
- **Orta / büyük büro / şirket içi:** Aşağıdaki eskalasyon sorusunu sor — raporlama hattı, kıdem tazminatı eşiğinin üstündeki fesihleri kim onaylıyor, toplu işten çıkarmaları kim imzalıyor vb.
- **Kamu / adli yardım / klinik:** Denetim modeline yönlendir — iş ürününü kim gözden geçiriyor, müvekkil iletişimi için onay zinciri nasıl işliyor.

**Eskalasyon sorusu (yukarıdaki dala göre uyarlanmış, pratik ortamı cevabından sonra sor):**

> "Bir inceleme daha kıdemli birinin onaylaması gereken bir şey bulduğunda — ayrımcılık veya misilleme riski taşıyan bir fesih, eskale eden bir soruşturma, sınırda bir sınıflandırma çağrısı, yetkinizin üstünde bir karar — bu kime gidiyor? Bir isim veya rol ver (BHM, patronunuz, İK başkanı), ya da 'kendim karar veririm' de."

Cevabı `## Pratik ortamı` altında veya `## Şirket profili` bölümüne dahil ederek kaydet.

#### Neler bağlı?

> Bu eklenti şunlarla çalışabilir: İK sistemi (HRIS), belge depolama (Google Drive, SharePoint, Box) ve Slack. Hangi bağlayıcıların yapılandırılmış olduğunu kontrol edeyim — ihtiyaç duyanlar çalışacak, olmayanlar sessizce başarısız olmak yerine zarifçe elle moda düşecek.

**Neyin gerçekten bağlı olduğunu kontrol et, neyin yapılandırılmış olduğunu değil.** `.mcp.json`'da listelenen bir bağlayıcı *mevcuttur*. Gerçekten yanıt veren bir bağlayıcı *bağlıdır*. Bunlar farklıdır ve karıştırmak güveni yok eder.

- Bağlantıyı test edebiliyorsan (basit bir MCP aracı çağrısı yap), yalnızca başarılı bir yanıtta ✓ bildir.
- Test edemiyorsan, ⚪ "yapılandırılmış ama doğrulanmamış — teyit için MCP ayarlarını aç" bildir, tek satırlık bir nasıl-yapılır ile.
- Asla yalnızca yapılandırmaya dayanarak ✓ bildirme.

Sonra şu formda bildir:

> - ✓ [Entegrasyon] — bağlı (test edildi)
> - ⚪ [Entegrasyon] — yapılandırılmış ama doğrulanmamış. Teyit için MCP ayarlarınızı açın.
> - ✗ [Entegrasyon] — bulunamadı. [Özellik] [elle alternatif]'e düşecek. [Nasıl bağlanır.] Sonra kurarsanız, `/is-hukuku:ilk-kurulum --check-integrations` yeniden çalıştırın.
>
> Bunların hepsine ihtiyacınız yok. Temel özellikler yalnızca dosya erişimiyle çalışır — İK sistemi yoksa izin takibi yerel bir kayda düşer.

#### Yapılandırma CLAUDE.md'ye yaz

`## Bunu kim kullanıyor`, `## Mevcut entegrasyonlar` ve `## Çıktılar` bölümlerini `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonuna göre yapılandırma-yolu CLAUDE.md'sinin ilk bölümünden hemen sonra yaz. Bunlar eklentideki her skill genelinde iş-ürünü başlığı seçimini ve özellik-düşme davranışını yönlendirir.

### Bölüm 1: Ayak izi (2-3 dk)

> **[Şirketiniz] ne yapıyor?** Bu en önemli bağlamdır — bir SaaS satıcısının, bir donanım dağıtıcısının ve bir hizmet firmasının oyun kitabı tamamen farklıdır. Yazmak zorunda değilsiniz: şirket web sitenize, "hakkımızda" sayfanıza bir bağlantı yapıştırın, ben ihtiyacım olanı çıkarırım. Ya da tek cümlelik versiyonu verin: ne sattığınızı, kime ve nasıl.

> Ayak izi sorularını sormadan önce: okuyabileceğim bir yargı çevresi tablonuz, İK sisteminizden aktif çalışan konumları listeniz var mı? İçeriği yapıştırın, bir dosya yolu paylaşın, veya 'hayır' deyin, sorulara tek tek geçeyim.

Yoksa:

- En az bir çalışanı olan her ülke.
- Türkiye içinde farklı bir rejime tabi her sektör (deniz taşımacılığı, gazetecilik, tarım/ev hizmetleri gibi 4857 m.4 kapsam dışı işler `[doğrulanacak]`).
- Uzaktan mı ofis merkezli mi? (Uzaktan-öncelikli, kimse söylemeden ayak izinin genişlemeye devam ettiği anlamına gelir.)
- Toplu iş sözleşmesi kapsamında bir işyeri var mı?

**Kullanıcı bir yargı çevresi listesi yüklemediyse:** bu bölümün sonunda öner: "Bunu bakımını yapabileceğin ve paylaşabileceğin bağımsız bir yargı çevresi tablosu olarak yazmamı ister misin? Az önce yakaladığım aynı ayak izi verisi, şirket büyüdükçe düzenlemesi daha kolay bir formatta."

### Bölüm 2: İnceleme tetikleyicileri (2-3 dk)

> "**Pozisyonlarınızı şimdi kurmak ister misiniz?** İnceleme skill'lerini (işe-alım-inceleme, çalışma-kılavuzu-güncelleme, politika-taslağı) çok daha iyi yapar — genel yerine duruşunuzu ve yedeklerinizi bilirler. Yaklaşık 3-4 dakika sürer. Yalnızca diğer komutları denemek istiyorsanız atlayın; inceleme skill'leri varsayılanları kullanır ve henüz belirlemediğiniz bir pozisyona çarptığında size söyler."

Yoksa:

**İşe alım:** Hukuk ne zaman bir teklifi görüyor?
- Her teklif mi? Yalnızca üst düzey mi? Yalnızca rekabet yasağı içerenler mi? Hiç mi?
- Standart teklif mektubunda ne var? Rekabet yasağı hükümleri TBK m.444-447 ve 4857 kapsamında sınırlıdır — süre ve coğrafi kapsam üzerinde makullük denetimi vardır `[doğrulanacak]`.

**Yüksek riskli işaretler:** Bir feshi korkutucu yapan nedir? (Bu `isten-cikartma-inceleme` skill'i taşındığında besleyecek — B kademesi, bkz. görev README.)
- Yakın tarihli şikayet (taciz, ayrımcılık, ihbar/whistleblower)
- Korumalı izinden yeni dönüş
- Sendikal faaliyet
- Daha önce sizi ısıran başka bir şey?

### Bölüm 3: Tohum belgeler (3-4 dk)

**İzin verisi nerede yaşıyor?**

Belge istemeden önce bir altyapı sorusu sor:

> Çalışan izinlerini takip eden bir İK sisteminiz var mı? Ve hukuğun buna okuma erişimi var mı? (Bu `/is-hukuku:izin-takibi` ve `/is-hukuku:izin-kaydi`'yi besler — İK sistemi erişimiyle izleyici otomatik çeker; olmadan yerel bir kayıttan çalışır.)

**Tohum belgeler**

> Bu en önemli kısım — ekibinizin gerçekte nasıl çalıştığını görmek istiyorum, yalnızca politikalarınızın ne söylediğini değil. İki şeye ihtiyacım var:
>
> 1. **Çalışma kılavuzunuz.** Güncel sürüm. Çalışanlara ne vaat ettiğinizi ve boşlukların nerede olduğunu bilmek için okuyacağım.
> 2. **Son iş hukuku belgeleri — ne kadar çoksa o kadar iyi.** On iyi bir taban, yirmi çok daha net bir örüntü verir. Karıştırın: fesih notları, teklif mektupları, kıdem tazminatı anlaşmaları, PDP'ler (performans değerlendirme planları), uyarlama talepleri — elinizde ne varsa.

## Yargı çevresi tablosunu oluştur

Bu, temel çıktıdır. Ayak izindeki her ülke/sektör için:

| Yargı çevresi / sektör | Özel kurallar | Otomatik eskale |
|---|---|---|
| Türkiye — genel (4857) | Standart iş güvencesi, ihbar/kıdem rejimi | Her toplu işten çıkarma |
| [Yurt dışı ülke] | [YER_TUTUCU] | [YER_TUTUCU] |
| [vb.] | | |

Kullanıcının adını vermediği yargı çevreleri için kural uydurma. Bir çalışanları varsa ve hiçbir not o ülkeden bahsetmediyse, `[Ülke: 1 çalışan, geçmiş yok — ilk sorunda araştır]` diye not düş.

## Pratik profilini yazma

`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablon yapısına göre. Tamamlanmış pratik profilini eklenti yapılandırmasına yaz, gereken üst dizinleri oluşturarak. Anahtar bölümler: yargı çevresi ayak izi, işe alım/fesih inceleme tetikleyicileri, yüksek riskli işaretler, yargı çevresine özgü eskalasyon tablosu.

## Yazdıktan sonra

**Bu eklentinin neye yardımcı olabileceğini göster.** Kapatmadan önce öner:

> **Neye yardımcı olabileceğimi görmek ister misin?**

Evet ise, bu özelleştirilmiş listeyi göster (genel bir şablon değil — bunlar eklentinin en iyi yaptığı somut şeyler):

> **İşte iş hukuku pratiğinde en iyi olduğum şeyler:**
>
> - **Bir teklif mektubunu ve rekabet yasağı hükümlerini incele** — ör. "Rekabet yasağı geçerliliği, ayrımcılık yasağı ve gerekli bildirimler üzerinde yargı çevresi kontrolü." Dene: `/is-hukuku:ise-alim-inceleme`
> - **Uluslararası genişlemeyi başlat** — ör. "Yol haritasında yeni bir ülke — iş hukuku iş akışını planla." Dene: `/is-hukuku:uluslararasi-genisletme`
> - **Bir iç soruşturma aç** — ör. "Meslek sırrı kapsamında çalışma alanı oluştur, günlüğü başlat, görüşmeleri yönlendir." Dene: `/is-hukuku:sorusturma-ac`
> - **Bir politika taslakla** — ör. "Bölge eklerini içeren temel bir politika." Dene: `/is-hukuku:politika-taslagi`
>
> **İlkin için önerim:** `/is-hukuku:ise-alim-inceleme` çalıştır varsayımsal bir teklif üzerinde — risk kalibrasyonunun nasıl okuduğunu en çok gösterecek skill bu. Ya da elinde ne olduğunu söyle, ben seçeyim.

Bu, soğuk-başlangıç sorununu (denetleyici ilk ne yapacağını bilmiyor) ve değer-önerisi sorununu (eklentinin ne yapabileceğini bilmiyorlar) tek bir öneride çözer.

### "İstediğin zaman her şeyi değiştirebilirsin" notuyla kapat

Yapılandırmayı yazdıktan sonra söyle:

> "Tamamdır. Yapılandırman `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` adresinde — okuyup doğrudan düzenleyebileceğin düz metin bir dosya. Cevapladığın her şey değiştirilebilir:
>
> - Hızlı bir değişiklik için dosyayı doğrudan düzenle
> - Tam bir yeniden görüşme için `/is-hukuku:ilk-kurulum --redo` çalıştır
> - Neyin bağlı olduğunu yeniden kontrol etmek için `/is-hukuku:ilk-kurulum --check-integrations` çalıştır
>
> İnsanların en çok ayarladığı üç ayar: **yargı çevresi listesi** (ayak iziniz büyüdükçe), **yüksek riskli fesih işaretleri** (gerçekten korkutucu olanı gürültüden ayırt ettikçe) ve **eskalasyon matrisi** (raporlama hatları değiştikçe)."

## Pratik profilin öğrenir

Yapılandırmayı yazdıktan sonra bu notla kapat:

> **Pratik profilin öğrenir.** Eklentiyi kullandıkça gelişir:
>
> - Bir skill'in çıktısı yanlış hissettirdiğinde, bu genellikle ayarlanacak bir pozisyondur. Çıktı hangisi olduğunu söyleyecektir.
> - Her zaman "oyun kitabımı X'i tercih edecek şekilde güncelle" veya "eskalasyon eşiğimi Y'ye değiştir" diyebilirsin, ilgili skill değişikliği yazar.
> - Bir bölümü yeniden görüşmek için `/is-hukuku:ilk-kurulum --redo <bölüm>` çalıştır, ya da yapılandırma dosyasını doğrudan düzenle.
>
> On dakikalık kurulum çalışan bir profil verir. Bir aylık kullanım, sanki sen yazmışsın gibi okunan bir profil verir.
