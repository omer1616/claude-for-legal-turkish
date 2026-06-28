---
name: ilk-kurulum
description: Dava takibi eklentisi için pratik profili kurar — şirket-içi, büro avukatı ve bağımsız rollerine ve davacı/davalı tarafına göre dallanır; risk kalibrasyonu, manzara ve ev tarzını yakalar, pratik profili CLAUDE.md'ye yazar. Yeni kurulumda, profili yeniden yapmak istediğinde veya mevcut entegrasyonları yeniden kontrol etmek istediğinde kullan.
argument-hint: "[--redo | --check-integrations]"
---

# /ilk-kurulum

1. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` dosyasını kontrol et. Zaten doluysa ve `--redo` yoksa, üzerine yazmadan önce kullanıcıya sor.
2. Aşağıdaki iş akışını ve referansı takip et.
3. Bölüm 0'ı çalıştır (rol, taraf, entegrasyon kontrolü). Görüşme role ve tarafa göre dallanır.
   - **Rol** pratik profil yapısını yönlendirir: **şirket-içi** (dosya portföyü, dış avukat gözetimi, TMS 37 karşılık metodolojisi, YK/denetim komitesi raporlaması), **büro-avukatı** (dava çalışması — dosya bağlamı, dava teorisi ve dönüm noktası olgu, ev tarzında örnek dilekçe), **bağımsız** (iş yükü + başarı primi ya da peşin ücret ekonomisi + müvekkil beklentileri + zamanaşımı takibi, ardından dava teorisi ve dilekçe bölümleri).
   - **Taraf** kalibrasyon sözlüğünü yönlendirir: **davacı** (iddia eden, dava değeri, başarı primi, zamanaşımı uçurumu), **davalı** (yanıt veren, maruziyet, karşılıklar —yalnızca şirket içi—, sigorta bildirimi), **ikisi de/değişir** (varsayılanı yakalar, dosya başına skill'lerin yeniden sormasına izin verir).

   Bölüm 0'dan sonra seçilen role uyan bölümleri takip et. Büro avukatı için şirket-içi yolu çalıştırma — TMS 37, YK notu ve sulh-yetkisi merdiveni büro pratiğine uygun çerçeve değildir. Varsayılanlar öner; serbest biçimli düzeltmeleri yakala. Her bölümde tohum belge iste (zorlamadan; paylaşmanın aşağı akış skill'lerini nasıl keskinleştirdiğini belirt).
4. Boşlukları yüzeye çıkar. Kullanıcının açıklanmış bir risk çerçevesi veya raporlama eşiği yoksa bunu belirt ve şimdi düşünmeyi ya da `[YER_TUTUCU]` bırakmayı teklif et.
5. Göç: `~/.claude/plugins/cache/claude-for-legal-turkish/dava-takibi/*/CLAUDE.md` yolunda dolu bir CLAUDE.md varsa (herhangi bir sürüm için) ama yapılandırma yolunda yoksa, ilerlemeden önce onu yapılandırma yoluna kopyala ve kullanıcıya neyi göç ettirdiğini göster.
6. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` dosyasını yaz. Alt bölüme tarihi ekle.
7. Sonuçlandırmadan önce kullanıcıyla teyitle: "İşte yakaladıklarım — yanlış olan bir şey var mı?"

## Bayraklar

- `--redo` — tam görüşmeyi yeniden çalıştır ve `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` dosyasının üzerine yaz.
- `--check-integrations` — mevcut MCP bağlayıcılarını yeniden tara ve tam görüşmeyi yeniden çalıştırmadan `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` dosyasındaki `## Mevcut entegrasyonlar` tablosunu yenile. Yeni bir bağlayıcı kurduktan sonra kullan (DYS, belge depolama, Gmail, UYAP, CLM).

Yoklama yaparken: yalnızca bir MCP araç çağrısı gerçekten başarılı olursa ✓ bildir. Yapılandırılmış-ama-test-edilmemiş bağlayıcılar nasıl doğrulanacağına dair tek satırlık bir açıklamayla ⚪ olarak işaretlenmeli. Yalnızca `.mcp.json` bildirimlerine dayanarak asla ✓ bildirme.

---

# İlk Kurulum Görüşmesi: Dava Takibi

## Amaç

Her dosya alımı, her kronoloji yapımı, her dilekçe taslağı, her durum özeti bu dosyadan okur. Çerçeve yakalanmazsa eklenti daha zayıf triyaj çağrıları yapar ve kullanıcı her seferinde sıfırdan düşünmek zorunda kalır. Bu görüşme çerçeveyi bir kez doldurur, böylece aşağı akışta her şey keskinleşir.

Eklenti üç farklı dava rolüne hizmet eder — dosya portföyünü yöneten şirket içi avukat, altta yatan dilekçe/ön inceleme/keşif çalışmasını yapan büro avukatı ve doğrudan iş yükünü yürüten bağımsız avukat. Her biri için sözcük dağarcığı farklıdır ve görüşme buna göre dallanır.

Görüşme aynı zamanda kullanıcının genellikle hangi tarafı temsil ettiğini sorar — davacı, davalı, ikisi de veya dosyaya göre değişir. Risk kalibrasyonu, ihtarname duruşu, delil/savunma hazırlığı ve kronoloji çerçevelemesi tarafa göre farklılık gösterir; pratik profil varsayılanı taşır, böylece aşağı akış skill'lerinin her seferinde sormak zorunda olmaz.

**Ton:** sokratik, kontrol listesi değil. Kullanıcının yazılı bir çerçevesi yoksa, bu çoğu zaman dile getirmeye zorlayan şeydir. Buna yaslan. Boşluklara koşma — adını koy, düşünmeyi teklif et, "sonraya bırak" seçeneğine izin ver.

> **Not (HMK/Türk usul hukuku):** Türk yargısında ABD tarzı *discovery* (kapsamlı belge celbi) ve *deposition* (yeminli sözlü ifade alma) kurumu yoktur. Delil ikamesi HMK m.187 vd. çerçevesinde yürür; belgeler mahkeme aracılığıyla ibraz ettirilir. "Saldırgan/savunmacı" çerçeveleme, dosya hazırlığı ve delil stratejisi için kullanılır — bire-bir ABD prosedürel eşdeğeri olarak değil.

## İlk-kurulum kontrolü

`~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` dosyasını oku:
- **Mevcut değil** → görüşmeyi başlat.
- **`<!-- KURULUM BURADA DURAKLATILDI: -->`** içeriyorsa → kullanıcıyı selamlayıp o bölümden devam etmeyi teklif et.
- **Durdurma yorumu olmadan `[YER_TUTUCU]` işaretleri içeriyorsa** → şablon hiç tamamlanmamış; sıfırdan başlamayı ya da yer tutucuların başladığı yerden devam etmeyi teklif et.
- **Dolu (yer tutucu yok, durdurma yorumu yok)** → zaten yapılandırılmış; `--redo` yoksa geç.

Şablon yapısı `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`'de bulunur — bölüm iskeleti olarak kullan. Tamamlanmış pratik profili yapılandırma yoluna yaz, gerekirse üst dizinleri oluştur.

## Paylaşılan şirket profilini kontrol et

`~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasına bak.

- **Mevcutsa:** Oku. Tek satırlık onay göster: "Siz [ad], [çalışma ortamı], [şirket]'te, [sektör]'de, [yargı çevreleri]'nde faaliyet gösteriyorsunuz. Doğru mu? (Paylaşılan profili değiştirmek için 'güncelle' deyin.)" Onaylanırsa şirket sorularını geç — doğrudan eklentiye özgü sorulara geç.
- **Mevcut değilse:** Bu kullanıcının kurduğu ilk eklenti olacak. Yönlendirme ve dallanmadan sonra şirket sorularını sor, paylaşılan profile yaz (eklenti kökündeki `references/company-profile-template.md` şablonuna göre), ardından eklentiye özgü sorulara devam et. Kullanıcıya şunu söyle: "Şirket profilinizi kaydettim — diğer hukuk eklentileri onu okuyacak ve bu soruları geçecek."

Paylaşılan profile ait olan sorular (mevcutsa **tekrar sorulmamalı**): çalışma ortamı, şirket adı, sektör, ne sattığınız, büyüklük, yargı çevreleri, düzenleyiciler, risk iştahı, eskalasyon isimleri. Eklentiye özgü sorular (playbook tutumları, inceleme çerçevesi, ev tarzı, gözetim modeli, vb.) eklenti başına kalır.

## Kurulum kapsamı kontrolü

Yönlendirmeden önce, çalışma dizini bir projenin içindeyse (kullanıcının ev dizini değil) bir kez işaretle:

> **Dikkat — bu eklenti proje kapsamlı kurulmuş görünüyor; yani yalnızca [mevcut dizin]'deki dosyaları okuyabilirim. Başka yerden (İndirilenler, Belgeler, ağ sürücüsü) belge okumak istersen kullanıcı kapsamlı yeniden kur — bkz. README.md. Proje kapsamıyla devam edebilirsin ama dosyaları bu klasöre taşıman gerekir.**

Devam etmeden önce kullanıcıya sor: proje kapsamıyla devam et ya da kullanıcı kapsamlı yeniden kurmak için duraklat. Çalışma dizini kullanıcının ev diziniyse bu kontrolü sessizce geç.

## Görüşme başlamadan önce

Önce-dallanma girişiyle aç. 3-4 kısa satırda tut. Her şeyden önce hızlı-veya-tam sor.

> **`dava-takibi` davayla çalışan kişiler için — şirket içi portföy yönetimi, büroda dilekçe yazımı ve ön inceleme, ya da bağımsız avukat olarak her ikisi.** Bu senin alanın değil mi? `/eklenti-merkezi:ilgili-eklentiler`.
>
> **2 dakika** sana rolünü (şirket-içi / büro-avukatı / bağımsız), çalışma ortamını, taraf varsayılanını (davacı / davalı) ve aktif dosya sayısını, artı risk kalibrasyonu, ev dilekçe tarzı ve gizlilik konvansiyonları için çalışan varsayılanlar verir. **15 dakika** gerçek şiddet × olasılık bantlarını, sulh yetkisi merdivenini (şirket-içi) ya da ücret ekonomisini (bağımsız), dış avukat kadrosunu, tohum dilekçeden ev tarzını, gizlilik günlüğü formatını, ihtarname şablonlarını ve manzara notlarını ekler.
>
> Hızlı mı, tam mı? (İstediğin zaman `/ilk-kurulum --full` ile yükseltilebilir.)

**Hızlı başlangıç yolu:** yalnızca Bölüm 0'ı (rol, çalışma ortamı, entegrasyonlar) ve yol dallanmasını sor. Konfigürasyonu diğer her şey için `[VARSAYILAN]` işaretleriyle yaz. Şununla kapat: "Tamam. Komutları kullanmaya başlayabilirsin. Risk kalibrasyonu, ev tarzı ve dava teorisi iskeleği için makul varsayılanlar kullandım. Bir skill'in çıktısı yanlış hissettirdiğinde, bu genellikle ayarlamanız gereken bir varsayılandır — hangisi olduğunu söyler. `/dava-takibi:ilk-kurulum --full` ile istediğin zaman tam görüşmeyi yap veya `/dava-takibi:ilk-kurulum --redo <bölüm>` ile bir bölümü yeniden yap."

**Tam kurulum yolu:** aşağıdaki mevcut görüşme akışı. Kullanıcı seçtikten sonra bir sonraki bölümde açıklanan daha derin yönlendirmeyi ver, ardından Bölüm 0'a geç.

## Kullanıcı hızlı veya tam seçtikten sonra

Daha derin yönlendirmeyi ver. Kendi sesinde bir paragraf:

> "Bu eklenti şunları tutar: pratik profilin (risk kalibrasyonu, gizlilik konvansiyonları, ev tarzı), bir dosya defteri (`_log.yaml`), dosya başına dosyalar (kronoloji, delil saklama bildirimleri, geçmişler, gizlilik günlükleri) ve bir iş-ürünü arşivi. İster portföy yöneten şirket içi avukat, ister dilekçe taslağı yapan büro avukatı, ister her ikisini birden yapan bağımsız uygulayıcı ol — dava çalışmasını destekler. Hangi rolde olduğunu, risk kalibrasyonunu ya da dava teorini, uyuşmazlık manzaranı ya da üretim kurulumunu, ev konvansiyonlarını öğrenir ve bunları eklentinin her seferinde okuduğu bir düz metin dosyasına yazar. Cevapladığın her şey sonradan değiştirilebilir."

Ardından taze-profil notu:

> "Kurulum, cevaplarından taze bir profesyonel profil oluşturur. Kişisel Claude geçmişini, diğer konuşmaları veya ev dizinindeki CLAUDE.md'ni okumaz. Konuşma bağlamında ilgili bilgileri fark edersem — ör. daha önce şirketini veya dosyayı belirttiysen — kullanmadan önce sorarım. Yazmadığın veya onaylamadığın hiçbir kişisel şey pratik yapılandırmana dahil edilmez."

Ardından: "Hazır mısın? Önce birkaç hızlı soru."

**Bu neden önemlidir** (kullanıcı zaman maliyetine itiraz ederse sun). Her dosya alımı, her portföy durumu, her dilekçe taslağı bu görüşmenin yazdığı konfigürasyondan okur. Genel bir konfigürasyon genel çıktı verir — varsayılan risk matrisi, varsayılan atıf stili, genel gizlilik günlüğü formatı. Eklentiye gerçek şiddet bantlarını, gerçek sulh yetkisi merdivenini, gerçek dilekçe yapısını söylemek "bir dava yapay zekası aracı" ile "senin gibi triyaj ve taslak yapan bir araç" arasındaki farkı yaratır. Özellikle yük taşıyan: dönüm noktası olgu (büro tarafı ise) ve tohum belgeler.

Pratik profili yalnızca kullanıcının yazılı cevaplarından ve görüşme sırasında yüklediği belgelerden çiz. `~/CLAUDE.md`'yi okuma veya ortam bağlamından pratik olgular çekme. Bu konuşmada ilgili bir şey zaten görünüyorsa, kullanmadan önce sor.

## Görüşme temposu

- **Cevabın bir yerde yazılı olduğunu varsay.** Bir soru muhtemelen bir yerde yazılı olan bilgi istiyorsa — şirket açıklaması, playbook, eskalasyon matrisi, stil kılavuzu, yargı çevresi listesi, dosya portföyü — kullanıcının hafızadan yazmadan önce bir bağlantı ya da yapıştırma iste. "Yapıştır veya kısa versiyonu ver" bir cümleden uzun her şey için varsayılan sorudur.

- **Gerçek cevaplar için bekle.** Bazı sorular hızlı tıklama cevaplarına sahip. Diğerleri kullanıcının bir şey yazmasını, açıklamasını veya bir örnek yüklemesini gerektirir (YK notu, saklama şablonu, ihtarname, risk notu, dava teorisi notu, tohum dilekçe). Bir soru hızlı tıklamadan fazlasını gerektirdiğinde:
  - **Grup boyutu — alt parçaları say.** "Bir turda 2-3'ten fazla soru sorma" demek 2-3 *yanıtlanabilir soru* demek, alt parçaları sayarak.
  - **Soruyu sor ve bekle.** "Bu yazılı bir cevap gerektiriyor — bekliyorum" diyerek açıkça belirt. Kullanıcı yanıtlayana kadar sonraki soruya geçme.
  - **Tohum belge yüklemeleri için:** "İçeriği yapıştır, dosya yolu paylaş veya 'şimdilik atla' de." Gerçekten bekle.
  - **Pratik profili yazmadan önce:** her yakalanan cevabı gözden geçir. Atlanan, yer tutucuyla yanıtlanan veya çelişki üretilen soruları listele. De ki: "Pratik profilinizi yazmadan önce hâlâ açık olanlar: [liste]. Bunlardan herhangi birini şimdi doldurmak ister misiniz?" Bekle.
  - **Asla** sessiz boşluklarla pratik profil yazma. Her `[YER_TUTUCU]` kullanıcının geçmeyi seçtiği bilinçli bir tercih olmalı.
- **Duraklat ve sürdür.** Önceden söyle: "Durmanız gerekirse 'duraklat' (veya 'dur' ya da 'sonraya bırakayım') deyin, ilerlemenizi kaydederim. Daha sonra `/dava-takibi:ilk-kurulum` çalıştırın, kaldığımız yerden devam ederiz." Kullanıcı duraklatınca üstte `<!-- KURULUM BURADA DURAKLATILDI: [bölüm adı] — sürdürmek için /dava-takibi:ilk-kurulum çalıştır -->` yorumu ve yanıtsız alanlarda `[BEKLEMEDE]` işaretçileriyle (ayrı `[YER_TUTUCU]`'dan) kısmi konfigürasyon yaz.

**Kurulumda kullanıcının söylediği hukuki olguları doğrula.** Kullanıcı bir kural atfı, kanun maddesi, içtihat (Yargıtay/Danıştay kararı), süre, sicil numarası, yargı çevresi veya eşikle yanıt verdiğinde — doğrulayabiliyorsan — konfigürasyona yazmadan önce kontrol et. Söyledikleri çelişiyorsa yüzeye çıkar: "₺X'in altında dosya oluşturulmayacağını söylediniz; bu eşiği aklınızda bir karar olarak mı yoksa yazılı bir politika olarak mı düşünüyorsunuz? `[öncül işaretlendi — doğrula]`" CLAUDE.md'ye yazılan yanlış bir olgu her gelecek çıktıya yayılır; burada yakalamak üründeki en yüksek kaldıraçlı anlardan biridir.

## Bölüm 0: Bunu kim kullanıyor + rol yönlendirmesi

### Bunu kim kullanıyor?

> Bunu günlük kim kullanacak? (Bu, her dosya brifinginde, kronolojide, gizlilik günlüğünde ve ihtarname taslağında iş-ürünü başlığını besler — avukat çıktıları gizlilik başlığı alır, avukat olmayanlar "araştırma notları, avukatla incele" başlığı alır.)
>
> 1. **Avukat veya hukuk profesyoneli** — baroya kayıtlı avukat, hukuk müşaviri, avukat gözetiminde çalışan stajyer/paralegal.
> 2. **Avukat erişimi olan avukat olmayan** — kurucu, iş birimi yöneticisi, hukuk departmanı ile iletişim halinde olan yönetici; danışabileceğin iç veya dış bir avukat var.
> 3. **Düzenli avukat erişimi olmayan avukat olmayan** — bunu kendin hallediyorsun.

Cevap 2 veya 3 ise, bunu bir kez söyle (her çıktıda tekrarlama):

> Her özelliği kullanabilirsiniz — araştırma, inceleme, taslak hazırlama, takip. İki şey değişir:
>
> 1. **Çıktıları avukat incelemesi için araştırma olarak çerçeveleyeceğim, kararlar değil.** "YEŞİL — imzalayın" yerine "işte bulduklarım ve imzalamadan önce sorulacak sorular" alırsınız.
> 2. **Hukuki sonuçları olan adımlarda duracağım** — ihtarname göndermek, delil saklama bildirimi yayımlamak veya serbest bırakmak, duruşmaya sunulacak dilekçe, dosyayı kapatmak, sulhe gitmek. Bir avukatla inceleyip incelemediğinizi soracağım.
>
> Bu bir sorumluluk reddi değil. Eklentinin iyi olduğu şeyleri — araştırma, organizasyon, yapı — durumunuz hakkında lisanslı hukuki yargıdan (bir aracın veremeyeceği şey) ayırt etmesi.

Cevap 3 ise ekle:

> Yargı çevrenizdeki lisanslı bir avukat bulmanız gerekiyorsa: baronuzun veya Türkiye Barolar Birliği'nin yönlendirme hizmeti en hızlı başlangıç noktasıdır. Pek çok baro ücretsiz veya düşük maliyetli ilk görüşme imkânı sunar.

### Rol (dallanma sorusu — erken sor)

> **Davayı nasıl yürütüyorsunuz?** (Bu görüşmenin hangi sütunlarının çalışacağını belirler — şirket içi karşılık ve YK notları alır, büro avukatı dava teorisi ve tohum dilekçeler alır, bağımsız her ikisini alır. Ayrıca `/dosya-acilis`, `/portfoy-durumu`, `/karsi-vekil-durumu` ve diğer tüm skill'lerin sözlüğü için varsayılanları ayarlar.)
>
> **(a) Şirket içi portföy yönetimi** — dosyalar, dış avukatlar, son tarihler, ihtarnameler, delil saklamalar. Aynı anda çok sayıda dosyanıza sahipsiniz, çoğunu dış bürolar yürütüyor. Durum özetleri ve YK notları işinizin parçası.
>
> **(b) Büroda dilekçe yazımı, ön inceleme, keşif/delil hazırlığı** — altta yatan iş ürününü gerçekten üretmekten sorumlu avukat veya stajyersiniz. Bir veya birkaç dosya, her birinde derin.
>
> **(c) Bağımsız / küçük büro, iş yükü yönetimi** — alım, triyaj, danışmanlık ve taslak yapıyorsunuz. Üstünüzde ortak yok; şirket içi karşılık / YK notu katmanı yok. Ekonomi başarı primi veya peşin ücret, büyük müvekkile saatlik değil.
>
> **(d) Başka bir şey** — bir cümlede açıklayın.

Cevabı pratik profilin `## Pratik rolü` bölümüne kaydet (`sirket-ici | buro-avukati | bagimsiz | diger`). Aşağı akış skill'leri varsayılanları seçmek için bunu okur.

**Görüşmenin geri kalanı için dallanma kuralları:**

- `sirket-ici` → **Şirket-içi yolu** çalıştır (aşağıdaki Sütun 1–3). Büro avukatı ve bağımsız bölümlerini geç.
- `buro-avukati` → **Büro-avukatı yolunu** çalıştır (aşağıdaki Bölüm A–D). Şirket içi portföy / dış avukat / YK notu sorularını ve bağımsız iş yükü / ekonomi sorularını geç.
- `bagimsiz` → özel **Bağımsız yolu** çalıştır (aşağıdaki Bölüm B1–B3) — iş yükü, müvekkil beklentileri, başarı primi ya da peşin ücret ekonomisi, büro yönetimi — **ardından** Büro-avukatı yolunu (Bölüm A–D) çalıştır çünkü bağımsız avukatlar da dilekçe yazar ve dava çalışır. Şirket-içi yolu ÇALIŞTIIRMA — karşılıklar, TMS 37, YK notları ve BHM'ye kadar uzanan sulh yetkisi merdiveni bağımsız pratik için doğru çerçeve değil.
- `diger` → tek cümlelik açıklama iste, ardından en yakın dala geç.

### Hangi tarafı çoğunlukla temsil ediyorsunuz?

Bunu rol sorusundan hemen sonra sor. Risk kalibrasyon çerçevesi, ihtarname duruşu, delil/savunma hazırlığı ve kronoloji yapım biçimi için yük taşıyan.

> **Hangi tarafı çoğunlukla temsil ediyorsunuz?** (Bu `/ihtarname-taslagi` 🅱️, `/gelen-talep` 🅱️, `/delil-saklama`, `/kronoloji` ve `/iddia-tablosu` 🅱️ besler — davacı çerçevesi ihtarnameleri gönderilen iddialar ve delil ikamesini saldırgan, davalı çerçevesi alınan ve triyaj edilen ve savunmacı olarak ele alır.)
>
> **(a) Davacı / talep eden** — bireyler veya şirketler adına talep açıyorsunuz. İhtarnameler iddialar. Delil/savunma hazırlığı saldırgan. Zamanaşımı karşı çalıştığınız bir uçurumdur. Ekonomi çoğu zaman başarı primidir.
>
> **(b) Davalı / yanıt veren** — taleplere karşı şirketleri veya bireyleri savunuyorsunuz. İhtarnameler alınır ve triyaj edilir. Delil/savunma hazırlığı savunmacı. Maruziyet değerlendirilir, karşılık ayrılır (şirket içi).
>
> **(c) İkisi de** — pratiğiniz düzenli olarak her ikisini de içeriyor. Varsayılan isteyin (davacı veya davalı); tekil skill'ler önemli olduğunda dosya başına soracak.
>
> **(d) Dosyaya göre değişir** — güçlü bir varsayılan yok; her dosya sorulur.

Pratik profilin `## Taraf` bölümüne kaydet (`davaci | davali | ikisi de — varsayılan davacı | ikisi de — varsayılan davalı | dosyaya göre değişir`).

### Çalışma ortamı

> Pratiğinizi en iyi hangisi tanımlıyor?
>
> 1. **Bağımsız avukat**
> 2. **Küçük büro (2–10)**
> 3. **Orta büro**
> 4. **Büyük büro**
> 5. **Şirket içi** (şirket hukuk departmanı)
> 6. **Kamu** (yargı, savcılık, kamu kurumu hukuk birimi)
> 7. **Hukuki yardım / adli yardım**
> 8. **Hukuk kliniği**
> 9. **Başka bir şey**

Bu, pratik profildeki eskalasyon / gözetim dilini inceler:

- **Hiyerarşi olmadan bağımsız / küçük (1, 2):** Yetki merdiveni sorularını "dışarıdan görüş için ne zaman dış avukat veya meslektaş çağırırsın" olarak yeniden çerçevele.
- **Orta / büyük büro / şirket içi / kamu (3, 4, 5, 6):** Tam eskalasyon zincirini, yetki merdivenini ve iç kişiler tablosunu sor.
- **Hukuki yardım / klinik (7, 8):** Gözetim modeline yönlendir — kayıt barosu avukatı, onay zinciri, inceleme kuyruğu mekaniği.
- **Başka bir şey (9):** Tek cümlelik açıklama iste, ardından en yakın dala geç.

### Ne bağlı?

> Bu eklenti şunlarla çalışabilir: DYS (Belge Yönetim Sistemi), belge depolama (Google Drive, SharePoint, Box), Gmail, UYAP / e-Devlet erişimi, zamanlanmış görevler, CLM (Sözleşme Yönetim Sistemi), hukuki araştırma (Lexpera, Kazancı, mevzuat.gov.tr, Resmî Gazete). Hangi bağlayıcıların yapılandırıldığını kontrol edeyim — onlara ihtiyaç duyan özellikler çalışır, ihtiyaç duymayanlar sessizce başarısız olmak yerine zarif biçimde geri döner.

**Gerçekte neyin bağlı olduğunu kontrol et, neyin yapılandırıldığını değil.** `.mcp.json`'da listelenen bir bağlayıcı *mevcut*tur. Gerçekten yanıt veren bir bağlayıcı *bağlı*dır. Bunlar farklıdır. Her bağlayıcı için:

- Bağlantıyı test edebiliyorsan (basit bir MCP araç çağrısı), yalnızca başarılı bir yanıtta ✓ bildir.
- Test edemiyorsan, ⚪ "yapılandırıldı ama doğrulanmadı" olarak işaretle.
- Yalnızca konfigürasyona dayanarak asla ✓ bildirme.

Bulguları şu biçimde raporla:

> - ✓ [Entegrasyon] — bağlı (test edildi)
> - ⚪ [Entegrasyon] — yapılandırıldı ama doğrulanmadı. Onaylamak için MCP ayarlarını aç.
> - ✗ [Entegrasyon] — bulunamadı. [Özellik] [elle alternatife] geri döner. [Nasıl bağlanır.]

Bunların hepsine ihtiyacın yok. Temel özellikler yalnızca dosya erişimiyle çalışır.

Eklenti konfigürasyonuna hemen `## Rol`, `## Bunu kim kullanıyor` ve `## Mevcut entegrasyonlar` bölümünü yaz. CLAUDE.md şablonuna göre iş-ürünü başlık kuralıyla `## Çıktılar`'ı ekle.

---

## Şirket-içi yol (rol == `sirket-ici`)

*Kullanıcının rolü `buro-avukati` veya `bagimsiz` ise bu bölümün tamamını geç.*

> Her dosyanın karşısında triyaj yaptığın çerçeveyi — risk kalibrasyonunu, uyuşmazlık manzarasını ve nasıl yazdığını — yakalamak istiyorum. Bir kez, böylece her dosya alımı bundan okusun. Makul olanlar için varsayılanlar önereceğim. Kabul et, düzenle veya sonraya bırakmak için boş bırak.
>
> Ayrıca yol boyunca tohum belge isteyeceğim — önceki YK notları, karşılık notları, delil saklama şablonları, örnek ihtarnameler. Görüşme boyunca on ile yirmi arası hedefliyoruz. Onun altında pratik profili alt bölüme SINIRLI VERİ olarak işaretleyeceğim — skill'ler çalışmaya devam eder ama çıktılar daha zayıf olur. Şablonlar önce gelir: bir örnek yüklersen okuyacağım ve yapıyı baştan yürümek yerine yalnızca boşlukları soracağım.

### Sütun 0 — Şirket profili

Ekip düzeyi bağlam. Başka bir `-hukuk` eklentisinin `## Şirket profili` bloğu zaten doluysa, yeniden girmek yerine buraya kopyala.

- Kuruluş / tüzel kişi
- Sektör
- Halka açık / özel / iştirak
- Denetim/düzenleme durumu (ör. SPK, BDDK, KVKK, EPDK, yok)
- Temel yargı çevreleri (faaliyet illeri + sık başvurulan mahkemeler/tahkim)
- Çalışan sayısı + hukuk ekibi büyüklüğü
- Kilit iç irtibatlar (BHM, CFO, IK Direktörü, Kurumsal İletişim, CISO, YK/Denetim Komitesi Başkanı) — isimler + ne zaman dahil edilir
- Bu avukatın adı ve bağlı olduğu makam

### Sütun 1 — Risk kalibrasyonu

> Yapılandırılmış sorulardan önce: okuyabileceğim mevcut bir risk-kalibrasyon notu, karşılık politikası belgesi veya dış avukat faturalama yönergeleri var mı? İçerikleri yapıştır, dosya yollarını paylaş veya 'hayır' de, sütunu soru soru yürüyeyim. Biri paylaşırsan şiddet bantlarını, önemlilik eşiklerini ve yetki merdivenini çıkarır ve yalnızca boşlukları sorarım.

Yoksa:

**Risk iştahı (2 dk)** — bir cümlede bu şirket davaya nasıl yaklaşıyor? (Bu `/dosya-brifingi` ve `/portfoy-durumu`'nu besler — her dosya brifinginin bir dosyanın risk kademesini nasıl vurguladığını ayarlar.)

**Şiddet × olasılık (3–5 dk)** — varsayılan 3×3'ü öner. Şiddet bantları (parasal ve parasal olmayan tetikleyiciler). Olasılık bantları. Dile getirilmemişse: "Adil. Pek çok avukat bunu yazmamış. Şimdi taslak çizmek ister misin yoksa varsayılanı bırakalım mı?"

**Önemlilik (materiality) eşikleri (2–3 dk)** — karşılık tetikleyicisi (TMS 37), açıklama tetikleyicisi (KAP/SPK — yalnızca halka açık şirket), YK/denetim komitesi bildirimi, yalnız-BHM eskalasyonu. *Tohum belge fırsatı:* karşılık notu şablonu veya açıklama kontrol listesi.

**Sulh yetkisi (1–2 dk)** — tutar merdiveni, özel saklı hükümler (yapısal tedbir tutardan bağımsız kurul onayı gerektirir).

**Sade Türkçe eskalasyon (1 dk).** Doğrudan sor:

> Bir dosya yetki bandınızın üstünde bir şey gerektirdiğinde — bandınızın üzerinde bir sulh teklifi, tek başına cevaplayamayacağın bir ihtarname, BHM'nin gerektirdiği bir saklama kararı — bu kime gidiyor? Bir isim, bir rol veya "ben karar veriyorum" deyin.

(Bağımsız avukatlar: "Ben karar veriyorum" doğru cevap; soru yine de kayıt için önemli. Dışarıdan görüş için dış avukat çağırıyorsan büronu adlandır.)

**Sigorta profili (1–2 dk)** — yürürlükteki poliçeler (Yönetici Sorumluluk / D&O, İşveren Sorumluluk, Siber, Mesleki Sorumluluk), sigortacılar, limitler, muafiyetler, poliçeye bildirim protokolü.

**Teklif et:** "Bir risk-kalibrasyon notu yüklemediyseniz, risk kalibrasyonunuzu ve yetki merdivenini paylaşabileceğiniz ve tutabileceğiniz bağımsız bir not olarak yazmamı ister misiniz?"

### Sütun 2 — Manzara

*Şirket profili Sütun 0'da. Manzara davaya özgüdür — kalıplar, hasımlar, mahkemeler.*

- İş bağlamı (30 sn) — ne yaptığımıza ve neden dava açtığımıza/aleyhimize dava açıldığına dair bir paragraf.
- Uyuşmazlık kalıpları (2–3 dk) — dosya türleri, sıklık, duruş.
- Sık hasımlar (1–2 dk).
- Dış avukat kadrosu (2–3 dk) — bürolar, sorumlu avukatlar, dosya türü, ücret duruşu, vekalet/ücret sözleşmesi durumu. *Tohum belge:* dış avukat yönergeleri. (Bu `/karsi-vekil-durumu`'nu besler — skill daha sonra bu bürolara haftalık durum talep taslakları hazırlar.)
- Sık başvurulan merciler (30 sn) — Asliye Ticaret, Asliye Hukuk, İş Mahkemesi, Tüketici Mahkemesi, FİŞHHM; ISTAC / ICC / ICSID tahkim.
- Belge depolama (2–3 dk) — dosya belgelerinin nerede yaşadığı (dosya sistemi, Drive, SharePoint, Box, Gmail, CLM, DYS), varsayılan dosya klasörü deseni, belgelerin dış avukatla nasıl paylaşıldığı.
- Menfaat çatışması taraması (1–2 dk) — bu şirket çatışmaları nasıl temizliyor; kim yapıyor; intake'de sert engel mi yoksa paralel mi.

### Sütun 3 — Ev tarzı

> Yapılandırılmış sorulardan önce: okuyabileceğim bir ev stili kılavuzu, şablon YK notu, delil saklama bildirimi şablonu veya örnek ihtarnameler var mı? İçerikleri yapıştır, dosya yollarını paylaş veya 'hayır' de, soruları yürüyeyim.

Yoksa:

- YK / denetim komitesi notu (2 dk) — format, ton, sıklık. *Tohum belge:* yeni YK notu (düzenleme tamam).
- Karşılık notu — format ve onaylayıcı. *Tohum belge:* örnek karşılık notu.
- Dış avukat talimatları — e-posta formatı, sıklık, bütçe duruşu.
- Gizlilik konvansiyonları — damgalama; varsayılan öznel çağrı duruşu (işaretle ve bayrakla); inceleme mekaniği (satır içi / kuyruk / ikisi). (Bu `/delil-saklama`'yı besler.)
- Delil saklama — şablon, yayımlama protokolü, tazeleme sıklığı. *Tohum belge:* saklama şablonu.
- Eskalasyon — kanal normları, konu satırı konvansiyonu.
- İhtarname pratiği — *burada sorulmaz.* Ton, süreler, kayıtlar ve imzalayan dosya başına ayarlanır. `/dava-takibi:talep-alimi` ve `/dava-takibi:ihtarname-taslagi` 🅱️ gerektiğinde sorar. Kurulum görüşmesinin *istediği* pratik-düzeyi parçalar: sigorta bildirimi zamanlaması ve dosya oluşturma önemlilik eşiği.

**Teklif et:** "Bir ev stili kılavuzu veya şablonlar yüklemediyseniz, ev stili kurallarınızı paylaşabileceğiniz bağımsız bir stil notu olarak yazmamı ister misiniz?"

---

## Bağımsız yol (rol == `bagimsiz`)

*Kullanıcının rolü `sirket-ici` veya `buro-avukati` ise bu bölümün tamamını geç. Bağımsız kullanıcılar bu yolu **ve** ardından Büro-avukatı yolunu çalıştırır.*

> Bağımsız pratik kendi çerçevesidir — iş yükü, müvekkil beklentileri, başarı primi ya da peşin ücret ekonomisi, büro yönetimi. Şirket içi dünya (TMS 37 karşılıkları, YK notları, dış avukat gözetimi, BHM'ye kadar sulh yetkisi merdivenileri) burada uygulanmaz ve uygulanıyormuş gibi davranmayacağım. Bana gerçek iş yükünün şeklini ve büroyu nasıl yürüttüğünü söyle.
>
> Birkaç tohum belge yardımcı olur — önceki bir ihtarname, bir sözleşme / vekalet anlaşması, örnek olarak paylaşmak istediğin bir müvekkil güncelleme e-postası.

### Bölüm B1 — Pratik şekli ve iş yükü

- **İş yükü büyüklüğü** — aynı anda yaklaşık kaç aktif dosya taşıyorsunuz? Fazlası ne?
- **Dosya karışımı** — kabaca yüzdeler: davacı vs davalı, pratik alanları (ör. ticari uyuşmazlık, iş hukuku, tüketici, aile, mülkiyet). Kesin olmana gerek yok; bir cümle yeterli.
- **Yargı çevreleri** — ağırlıklı olarak çalıştığın iller ve mahkemeler. İlgili adli varsa dahil et.
- **Tipik dava süresi** — haftalar, aylar, yıllar? Aşağı akış skill'lerinin çaba ve süre ufuklarını ölçeklendirmesi için yararlı.
- **Kapasite bayrakları** — dosya almayı bıraktığın bir nokta var mı? Aşırı kapasitede olduğunu nasıl anlıyorsun?

### Bölüm B2 — Müvekkil beklentileri ve ekonomi

*Bu, şirket içi yolun "risk kalibrasyonu / karşılık metodolojisi / sulh yetkisi merdiveni" dediğini yerine koyar. Bağımsız avukatlar karşılık ayrıp BHM'ye eskalasyon yapmaz; aynı kararlar müvekkile dönük ekonomi olarak görünür.*

**Ücret yapısı (ana etken).** İşinin çoğuna uyanı seç:

- **Başarı primi** (davacı tarafı ağırlıklı pratiğin varsayılan varsayımı): standart oranın ne? Dava öncesi vs dava sonrası? Masraf avansı duruşu — müvekkil, büro, karma? Hangi maruziyette artık başarı primiyle dava almıyorsun? *(Avukatlık K. m.164/3 çerçevesinde)*
- **Saatlik / peşin ücret**: saatlik ücret, standart peşin ücret, emanet hesabı mekaniği.
- **Götürü ücret**: hangi dosya türleri ve ücret aralığı.
- **Karma**: karışımı açıkla.

**Müvekkil beklentileri (2 dk).** Doğrudan sor:

- Müvekkilleri dosyalarında ne sıklıkla güncelliyor musunuz (haftalık, aylık, olay bazlı)?
- Güncellemeler hangi biçimde — telefon, e-posta, mektup, müvekkil portalı?
- Müvekkillerle sulh görüşmelerindeki varsayılan duruşun nedir (agresif sulh yönlendirmesi, müvekkili yönlendirsin, dosyaya bağlı)?

**Maruziyet / dava-değeri okuması (davacı tarafı).** Dava almaya değip değmediğine karar vermek için hızlı zihinsel çerçeven ne?

**Müvekkile rapor etme (1 dk).** *Tohum belge fırsatı:* yeni bir güncelleme mektubu veya e-postası (düzenleme tamam). Bu, şirket içi YK notunun bağımsız karşılığıdır.

### Bölüm B3 — Büro yönetimi ve manzara

- **Zamanaşımı takibi** — iş yükündeki zamanaşımı ve hak düşürücü süreleri nasıl takip ediyorsun? (Takvim, dava yönetim yazılımı, kâğıt tevzi defteri, hafıza — gerçek olan ne.) Bu şirket içi "önemlilik / karşılık tetikleyicisinin" bağımsız karşılığıdır — zamanaşımı kaçırmak bağımsız kariyeri bitiren başarısızlık biçimidir.
- **Dava yönetim yazılımı** — varsa hangi program (ör. UYAP/Avukat Portalı, e-Tebligat, kâğıt dosyalar, elektronik tablolar).
- **Belge depolama** — Google Drive, Dropbox, OneDrive, yerel dosya sistemi. Dosya belgeleri gerçekte nerede yaşıyor?
- **Sık başvurulan merciler** — gerçekten çıktığın mahkemeler.
- **Sık karşı taraflar / avukatlar** — karşı tarafta düzenli gördüğün tekrarlayan oyuncular.
- **Ortak avukat / yönlendirme avukatları kadrosu** — konfor alanın dışındaki dosyalar için kimlerle çalışıyorsun?
- **Menfaat çatışması taraması** — çatışmaları nasıl yürütüyorsun? Bağımsız versiyon genellikle gayriresmidir (hafıza + müvekkil listesi kontrolü) — yakaladığını kaydet.

### Bağımsız ev tarzı

YK notu / karşılık notu / dış avukat yönergesi sorularını tamamen atla. Bağımsız ev tarzı:

- **Müvekkil güncellemesi** — format, ton, sıklık. *Tohum belge:* yeni bir güncelleme mektubu veya e-postası.
- **Vekalet / ücret sözleşmesi** — şablon. *Tohum belge:* örnek (düzenleme tamam).
- **Gizlilik konvansiyonları** — damgalama; inceleme mekaniği.
- **Delil saklama** — bağımsız için de, dava öngörüldüğünde koruma önemlidir. Varsa şablon.
- **İhtarname pratiği** — *burada sorulmaz.* Ton, süreler, kayıtlar ve imzalayan dosya başına ayarlanır.

**Teklif et:** "Bir müvekkil güncelleme örneği veya vekalet sözleşmesi yüklemediyseniz, ev stili kurallarınızı yeniden kullanabileceğiniz bağımsız bir not olarak yazmamı ister misiniz?"

B3'ten sonra aşağıdaki **Büro-avukatı yoluna** devam et. Bağımsız avukatlar da dilekçe yazar, kronoloji oluşturur ve belge incelemesi yapar — dava teorisi ve tohum dilekçe çalışması geçerlidir.

---

## Büro-avukatı yolu (rol == `buro-avukati` veya `bagimsiz`)

> Bir belgeye dokunmadan önce teoriye ihtiyacım var. Bizim hikayemiz ne? Onların hikayesi ne? Dava neye bağlı? Ardından büronun nasıl yazdığını görmem gerekiyor — gurur duyduğun bir dilekçe — ki taslaklar başka yerden gelmiş gibi görünmesin.

### Bölüm A: Dosya (2 dk)

- Dosya adı, müvekkil, esas numarası, mahkeme/tahkim
- Tarafımız (davacı / davalı)
- Sorumlu ortak ve kıdemli avukat (bağımsız / küçük büroysa geç)
- Aşama (dilekçeler, ön inceleme, sözlü yargılama hazırlığı, tahkim duruşması)
- Yaklaşan önemli tarihler

### Bölüm B: Teori — her şey bu (3–4 dk)

> Dava teorinizi söyleyin. Şikâyeti değil — hikayeyi. Jüriye iki cümlede neden kazandığınızı anlatmak zorunda kalsaydınız, bunlar ne olurdu?

- Teorimiz bir paragrafta
- Onların teorisi bir paragrafta (karşı tarafı tanı)
- **Dönüm noktası olgu** — davanın döndüğü olgu
- Bizim için kilit olgular
- Aleyhimize kilit olgular (endişe ettiğin olgular)
- En önemli hukuki mesele

### Bölüm C: Tohum belgeler (3–4 dk)

> İki şey:
>
> 1. **Dava teorisi notu**, varsa. Teori birinin kafasında yaşıyorsa kâğıt üzerinde değil, sorun değil — yukarıda yakaladık.
>
> 2. **Ev tarzında önceki bir dilekçe.** Bu davadan değil — herhangi bir davadan. Elindeki en iyisi. Atıf stilini, yapıyı, tonu, argümanları nasıl düzenlediğini öğreneceğim. (Bu `/dilekce-bolumu-taslaklayici`'yı besler — her gelecek dilekçe bölümü çıkarılan atıf formatında, başlık yapısında ve tonda taslaklanır.)

**Dilekçeden:** atıf formatı (yerel mahkeme kuralları, FSHHM/BAM/Yargıtay atıf gelenekleri), bölüm yapısı, başlık konvansiyonları, ton (agresif / ölçülü), uzunluk normları.

### Bölüm D: Belge inceleme kurulumu (1–2 dk)

> Sorulardan önce: okuyabileceğim bir gizlilik günlüğü formatı, kronoloji formatı veya inceleme protokolü belgesi var mı? İçerikleri yapıştır, dosya yollarını paylaş veya 'hayır' de, tek tek sorayım.

Yoksa:
- E-keşif/belge depolama platformu (Everlaw, Google Drive, DYS, USB/yerel)
- İnceleme protokolü — kodlama kategorileri, kim karar veriyor
- Gizlilik günlüğü formatı
- Kilit muhafızlar ve tarih aralığı

**Teklif et:** "Gizlilik günlüğü veya kronoloji formatı yüklemediyseniz, inceleme protokolünüzü ve gizlilik günlüğü formatınızı bir inceleme ekibiyle paylaşabileceğiniz bağımsız bir referans olarak yazmamı ister misiniz?"

---

## Yazmadan önce — yeniden oku

Eklenti konfigürasyonunu taahhüt etmeden önce her yakalanan cevabı sırayla yeniden oku. Bu üç hata kategorisini yakalar:

1. **Cevaplar arasındaki çelişkiler** — ör. kullanıcı risk iştahında "her şeyle mücadele et" dedi ve ihtarname varsayılanında "hızlıca sulh et" dedi. İkisini de yüzeye çıkar, hangisinin geçerli olduğunu sor.
2. **Bölümler arasında değişen ayrıntılar** — isimler, tarihler, eşikler. Son değeri onayla.
3. **Şimdi tamamlamaya değer atlanan boşluklar** — `--redo` yerine şimdi doldurmak isteyebilecekleri boşluklar.

Ayrıca: rol `buro-avukati` ise dönüm noktası olgunun ve tohum dilekçenin yakalandığını iki kez kontrol et. Bunlar yük taşıyan. İkisi de eksikse, yazmadan önce açıkça adlandır.

## Pratik profili yazma

Tamamlanmış pratik profili eklenti konfigürasyonuna yaz, `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`'deki şablonu bölüm iskeleti olarak kullan. Yakalanan her bölümü doldur; kullanıcının geçtiği bölümlere `[YER_TUTUCU]` bırak. Alt bölüme tarihi ekle.

**Role göre bölüm kapılama:**

- `sirket-ici` → tam şirket içi yapı (Şirket profili, TMS 37 / karşılık / YK notu satırlarıyla Risk kalibrasyonu, Dış avukat kadrosu, YK/denetim komitesi notu). Yalnızca bağımsıza özgü bölümleri atlat veya N/A işaretle (ücret yapısı, vekalet, başarı primi).
- `buro-avukati` → büro dünya yapısı (dava teorisi, dönüm noktası olgu, ortak incelemesi, tohum dilekçe). Karşılık / YK notu / TMS 37 bölümlerini atla; bağımsız ücret / vekalet bölümlerini atla.
- `bagimsiz` → bağımsız yapı (iş yükü, ücret yapısı, müvekkil beklentileri, zamanaşımı takibi, vekalet veya başarı primi, büro yönetimi) **artı** büro-avukatı bölümleri (dava teorisi, tohum dilekçe). Şirket içi TMS 37 / karşılık / YK notu / BHM'ye uzanan sulh-yetkisi merdiveni bölümlerini tamamen atla.

Şablon bölümü yalnızca şirket içi sözcük dağarcığı taşıyorsa (TMS 37 karşılıkları, YK notu), şirket dışı roller için ya bölümü atla ya da sözcük dağarcığını eşdeğer bağımsız veya büro kavramıyla çevir.

**SINIRLI VERİ bayrağı:** görüşme boyunca on'dan az tohum belge paylaşıldıysa alt bölüme bir `> SINIRLI VERİ` notu ekle: "Bu pratik profil [N] tohum belgeden ve görüşme cevaplarından yazıldı. Daha fazla örnek eklenene kadar aşağı akış skill'leri çalışır ama çıktılar daha zayıf olur. Kalibrasyonu keskinleştirmek için daha fazla şablon topladıktan sonra `/dava-takibi:ilk-kurulum --redo` çalıştır."

## Boşluk tespiti

Görüşmeden sonra, yazmadan önce, özetle ve **bir cevap bekle**:

> İşte yakaladıklarım. Fark ettiğim boşluklar:
> - [atlanan bölümleri, boş bırakılan yer tutucuları, kullanıcının "sonraya bırakayım" dediği soruları listele]
>
> Bunlardan herhangi birini şimdi doldurmak ister misin yoksa yer tutucu olarak bırakalım mı? Ayrıca `/dava-takibi:ilk-kurulum --redo` veya konfigürasyon dosyasını doğrudan düzenleyerek sonradan doldurabilirsin. Yazmadan önce bunu düşünmeye değer: [en önemli boşluğu ve nedenini adlandır].

Kullanıcı yanıtlayana kadar yazmaya devam etme.

## Yazdıktan sonra

**Bu eklentinin neler yapabileceğini göster.** Kapatmadan önce teklif et:

> **Ne yardımcı olabileceğimi görmek ister misin?**

Evet ise, bu özelleştirilmiş listeyi göster:

> **Dava pratiğinde iyi olduğum şeyler:**
>
> - **Yeni dosya alımı** — standart sorular, matter.md + history.md yazar, portföy günlüğüne ekler. Dene: `/dava-takibi:dosya-acilis`
> - **Gelen talep triyajı** — seçenekler analizi, portföy çapraz kontrolü, dosyaya dönüşürse alıma geçiş. Dene: `/dava-takibi:gelen-talep` 🅱️
> - **Kronoloji oluşturma** — kaynaklardan ve yüklemelerden kronoloji oluşturur veya günceller. Dene: `/dava-takibi:kronoloji`
> - **Delil saklama** — saklama bildirimini taslakla, günlüğü güncelle, tazeleme zamanla. Dene: `/dava-takibi:delil-saklama`
> - **Portföy özeti** — aktif portföy boyunca risk dağılımı, yaklaşan son tarihler, bayat dosyalar. Dene: `/dava-takibi:portfoy-durumu`
>
> **İlk öneri:** `/dava-takibi:portfoy-durumu` çalıştır — portföyün nerede durduğunu bir bakışta gösterir ve denemesi için sıfır girdi yeterli. Ya da masanda ne var söyle, ben seçeyim.

- `sirket-ici` ise: "Şirket içi pratik profili yazıldı. Her dosya alımı bundan okuyacak. En canlı dosyanda `/dava-takibi:dosya-acilis` çalıştırmak ister misin?"
- `buro-avukati` ise: "İşte yakaladığım teori. Dönüm noktası olguyu oku — doğru aldım mı? Bir sonraki son tarih ne? Oradan başlayalım."
- `bagimsiz` ise: "Bağımsız pratik profilin yazıldı — iş yükü şekli, ücret ekonomisi, büroyu nasıl yürüttüğün — artı canlı bir dosya için dava teorisi ve dilekçe tarzı çalışması. En canlı dosyanda `/dava-takibi:dosya-acilis` çalıştırmak ister misin?"

### "Her şeyi sonradan değiştirebilirsin" notuyla kapat

> "Pratik profilin `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'de — okuyup doğrudan düzenleyebileceğin bir düz metin dosyası. Cevapladığın her şey değiştirilebilir:
>
> - Hızlı değişiklik için dosyayı doğrudan düzenle
> - Tam yeniden görüşme için `/dava-takibi:ilk-kurulum --redo` çalıştır
> - Entegrasyonları yeniden kontrol etmek için `/dava-takibi:ilk-kurulum --check-integrations` çalıştır
>
> İnsanların en çok ayarladığı bölümler: şirket içi için **şiddet × olasılık eşikleri** ve **dış avukat kadrosu**; büro avukatı için **dava teorisi** (özellikle dönüm noktası olgu) ve tohum dilekçeden çıkarılan **ev dilekçe tarzı**; bağımsız için **ücret yapısı** ve **taraf varsayılanı** (davacı / davalı) — burada yanlış bir varsayılan her ihtarname ve kronoloji çıktısını çarpıtır. Bir çıktı yanlış hissettirdiğinde, düzeltme genellikle buradadır."

### İlk dosyandan önce

**Bir araştırma aracı bağla.** Bağlı olmadan her atfı doğrulanmamış olarak işaretlerim — bağlıyken geçerli bir veritabanına karşı doğrularım. Cowork'ta: Ayarlar → Bağlayıcılar. Claude Code'da: bir skill ihtiyaç duyduğunda yetkilendir.

### Pratik profilin öğrenir

Pratik profili yazdıktan sonra bu notla kapat:

> **Pratik profilin öğrenir.** Eklentileri kullandıkça daha iyi olur:
>
> - Bir skill'in çıktısı yanlış hissettirdiğinde, bu genellikle ayarlanacak bir tutumdur. Çıktı hangisi olduğunu söyler.
> - "Playbook'umu X'i tercih edecek şekilde güncelle" veya "eskalasyon eşiğimi Y'ye değiştir" diyebilirsin, ilgili skill değişikliği yazar.
> - Bir bölümü yeniden görüşmek için `/ilk-kurulum --redo <bölüm>` çalıştır veya konfigürasyon dosyasını doğrudan düzenle.
>
> On dakikalık kurulum sana çalışan bir profil verir. Bir aylık kullanım sana sanki kendين yazmış gibi okunacak biri verir.

## Bu skill'in yapmadıkları

- Kullanıcı için çerçeveye karar vermez. Varsayılanlar başlangıç noktalarıdır; kullanıcının yargısı gerçek içeriktir.
- Boşlukların olmadığını iddia etmez. Dürüstçe `[YER_TUTUCU]` bırakmak bir eşik uydurmaktan iyidir.
- Kullanıcıyla tartışmaz. "Henüz elimde yok" derlerse not et ve devam et.
- İzin almadan kişisel `~/CLAUDE.md`'yi veya ortam bağlamını okumaz.