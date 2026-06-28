---
name: dilekce-bolumu-taslaklayici
description: Ev tarzında dilekçe bölümü taslaklar — her olgu atıflı, her karar kontrol edilmiş, her argüman teoriye bağlı. Kullanıcı "[bölümü] taslakla", "olgular beyanını yaz", "[konu] hakkında argüman bölümü" dediğinde veya bir dilekçe bölümünün ilk taslağına ihtiyaç duyduğunda kullan.
argument-hint: "[bölüm — ör. 'olgular beyanı', 'argüman II']"
---

# /dilekce-bolumu-taslaklayici

1. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` yükle → dava teorisi, ev tarzı.
2. Aşağıdaki iş akışını ve referansı uygula.
3. Ev formatı/tonunda/atıf tarzında taslakla. Teoriye uygun.
4. Çıktı: taslak bölüm. Doğrulama gereken her olgu ve atfı işaretle.

---

# Dilekçe Bölümü Taslaklayıcı

## İfade Beyanları — Türkiye'ye Özgü Kısıtlamalar

Eğer kullanıcının yargı çevresi bir ifade beyanı taslağı istemeyi gerektiriyorsa (HMK, iş davası, tahkim), Türk mahkemelerinde ifade beyanlarının İngiliz CPR PD 57AC gibi yapı kısıtlamalarına tabi olup olmadığını kontrol et. `[doğrulanacak — Türk hukuku altında yazılı tanık ifadelerinin yapısal gereklilikleri]`

Genel ilke: Tanığın ağzından yazılmış anlatı taslağı çıkarmak ciddi itibar sorunlarına neden olur. Yapabileceğim şey: tanığın gerçek anısını ortaya çıkaracak soru istemleri hazırlamak; tanığın söylediklerini yakalamak ve düzenlemek; gösterildiği belgelerin listesini üretmek; uyum kontrol listesi çalıştırmak. Tanığı yazmak değil, kanıtı ifadeye sokmanıza yardımcı olurum.

## Amaç

İyi bir dilekçe bölümü teoriye uygun, kayda atıflı, ev tarzında yazılmış ve doğrulanabilirdir. Bu skill ilk taslağı üretir — vurgu *taslak* üzerinde. Avukat düzenler.

## Yazılı mı Sözlü mü?

Taslaklamadan önce sor: "Bu yazılı bir sunuş için mi yoksa sözlü argüman için mi?" İkisi farklı zanaatlardır:

- **Yazılı:** kapsamlı. Noktaları kapat, yetkiyi geliştir, yanıtları öngör.
- **Sözlü (itiraz, kapanış, argüman):** stratejik. En önemli 3-4 noktayı seç. Zayıf olanları teslim et veya görmezden gel. En güçlüyle başla. Bir mahkeme ilk iki dakikayı ve son iki dakikayı hatırlar. Çok kapsamlı sözlü savunuculuk odaksız olarak okunur. Çok konulu bir sunuşa yanıt veriyorsanız, hangi konuları vurgulayacağınızı ve hangilerini bırakacağınızı söyleyin — bu kelimelerin değil, stratejinin taslağıdır.

## Kayıt Doğruluğu — Alıntılar ve Pinpoint Atıflar

Her savunuculuk taslağındaki her atfı ve her alıntıyı yöneten iki kural. Kanonik ifade plugin'in CLAUDE.md paylaşılan guardrail'lerinde yaşar; burada tekrarlanıyor çünkü bu skill kuralın sınanmasının en yaygın yeridir.

**Kayıttan kelimesi kelimesine alıntılar kelimesi kelimesine olmalı.** Karşı vekile, tanığa, mahkemeye veya herhangi bir kayıt belgesine atfedilen sözlerin etrafına, tam pasaja sahip değilsen ve atıf yapamıyorsan asla tırnak işareti koyma. Neredeyse doğru bir alıntı, başka kelimelerle ifadeden kötüdür — kaydı yanlış aktarır, sunulursa yaptırıma yol açabilir ve yakalanır. Birinin söylediğini nitelendirmek isteyip tam kelimeleri bulamadığında:

- **Tırnak işareti olmadan açıkla**, açıkça atfederek: "Karşı vekil X'i ileri sürdü `[kayda karşı doğrula — tutanak s. __]`."
- **Yer tutucuyu işaretle:** `[tam alıntı doğrula — kayıt atfı bekliyor]`
- **Boşluğu asla doldurma.** Uydurma bir alıntı, tek kelime bile olsa, bir uydurmadır.

**Pinpoint atıflar bütün önermeyi desteklemeli.** Argüman "karşı taraf X, Y ve Z dedi" ise ve bir tutanak sayfası gösteriyorsan, o sayfanın X VE Y VE Z'yi desteklediğini doğrula. Yalnızca Z'yi destekliyorsa, ya (a) atfı böl ya da (b) önermeyi sayfanın gerçekten desteklediğine daralt.

## Zayıf Argümanlar Hakkında Dürüstlük

Hukuk aleyhindeyken, söyle. Bir argüman zayıfsa — yetki karşı yönde kesiliyor, olgular desteklemiyor, çıkarım zorlama — sarsak bir argüman inşa edip sağlammış gibi sunma. İşaretle:

> "Bu nokta zayıf — [yetki] karşı yönde kesiyor. Bunu mı vurmak istiyorsunuz (nasıl çerçeveleyeceğiniz burada), [daha güçlü noktaya] pivot mi yapıp taviz mi veriyorsunuz, yoksa bırakıyor musunuz? `[incele — stratejik karar]`"

## Atıf Çıkarma Kapsamı

Bu taslak atıf kontrolü yapıldığında — sizin, başka bir skill veya gözden geçirenin — kontrol kapsamlı olmalı:

1. **Birinci geçiş: çıkar.** Tüm belgeyi oku ve her atfın listesini oluştur — davalar, kanunlar, yönetmelikler, kayıt atıfları, ikincil yetki. Sayıyı raporla: "[N] atıf bulundu."
2. **İkinci geçiş: kontrol et.** Her birini kaynağa karşı kontrol et. Örnekleme yapma.
3. **Kapsamı raporla.** Sonunda: "[M] atıftan [N]'i kontrol edildi. [K] alınamadı — manuel doğrula. [J] teyit edildi. [I] potansiyel yanlış atıf olarak işaretlendi. [H] yanlış temellendirilmiş olarak işaretlendi."
4. **Kaynak metin mevcut değilken "kontrol edilemedi" de, asla "teyit edildi" deme.**
5. **Kısmi desteği yakalamak en zor hatadır.** İddianın bir kısmını değil tamamını destekleyen bir atıf.

## Eko vs Tekrar

Kilit çerçevelemelerle eko yap; cümleleri kaldırma. Tutarlılık teorini güçlendirir. Ama sınır var:

- **Eko:** aynı kilit terimleri, merkezi konunun aynı çerçevelemesini, karşı tarafın teorisinin aynı nitelendirmesini kullan.
- **Yapma:** bütün cümleleri kaldırma, aynı dilekçeyi yeniden okuyor gibi gösteren ayırt edici ifadeleri tekrarlama.

## Bağlamı Yükle

`~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` → dava teorisi, ev tarzı (atıf formatı, yapı, ton, uzunluk normları).

**Çatışma kapısı — atlanamaz.** Taslaklamadan önce `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml`'da bu skill'in çağrıldığı dosya slug'ını kontrol et. Dosya `_log.yaml`'da yoksa reddet ve yönlendir:

> "[dosya slug'ı]'nı dosya günlüğünde göremiyorum. Önce `/dava-takibi:dosya-acilis` çalıştır; böylece çatışma taraması yapılır ve dosya çalışma alanı kurulur. Intake yapılmamış bir dosyada esaslı iş ürünü taslaklamam — çatışma taraması kapıdır."

## İş Akışı

### Adım 1: Hangi Bölüm?

| Bölüm | Ne Yapar | Gereken Girdiler |
|---|---|---|
| Olgular beyanı | Hikayeyi, bizim çerçevemizde anlatır, kayda atıflı | Kronoloji, kilit belgeler, tutanak atıfları |
| İnceleme standardı | Mahkemenin uyguladığı çıtayı belirler | Usul duruşu |
| Argüman | Hukuki davayı yapar | Konu, yetki, olgular |
| Sonuç | Tedbir ister | Ne istediğimiz |

### Adım 2: Teori Kontrolü

Yazmadan önce: bu bölüm teori için ne başarması gerekiyor?

- Olgular beyanı: Hikayeyi teorimizin doğal okuma olduğu şekilde çerçevele.
- Argüman: Hukuku teoriye destek verecek şekilde olgulara bağla.

Taslaklamak üzere olduğun bölüm teoriye çelişiyorsa — dur. Ya teori yanlış ya da bölüm yaklaşımı yanlış. İşaretle, üzerini örtme.

### Adım 3: Ev Tarzında Taslakla

**Forumun yerel kurallarını ve hakimin önceki emirlerini araştır; uzunluk, biçimlendirme, atıf ve başvuru gerekliliklerini tercih olarak alma. Birincil kaynakları (yerel kural numarası, emir bölümü) taslak notlarında atıfla. Güncelliği doğrula — yerel kurallar değişir.**

`~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'ye göre:

- **Atıf formatı:** Türk mahkemelerinde kanun/karar atıf kuralları (ilgili Yönetmelik / UYAP kuralları). Yüksek Mahkeme kararları için: `Yargıtay [Daire]. [Tarih]. [Esas No]. [Karar No].` biçimindeki standart Türk atıf formatı. `[doğrulanacak — bulunduğunuz forumun yerel kuralı ve atıf stilini teyit edin]`
- **Yapı:** Bu büro argümanları nasıl düzenliyor? CRAC? Önce başlık cümlesi? Tartışan vs açıklayan başlıklar?
- **Ton:** Agresif ("Davalıların argümanı dayanaksızdır") veya ölçülü ("Delil Davalıların pozisyonunu desteklememektedir")? Tohum dilekçeyle eşleştir.
- **Uzunluk:** Yerel kural / önceki emir başına — "bu hakimin genellikle istediği şey"e güvenmek kuralı kontrol edilebilecekken.

### Adım 4: Her Şeyi Atıfla

Her olgu → kayıt atfı (Bates, tutanak sayfa:satır, sergi).
Her hukuki önerme → kararı atıfla.

**İşaret disiplini — liberalce kullan:**
- `[DOĞRULA: spesifik olgusal iddia]` — kayda karşı teyit edilmemiş her şey
- `[BELİRSİZ: spesifik hukuki önerme]` — mevcut yetkiye karşı teyit edilmemiş her şey
- `[ATI GEREKLİ: spesifik atıf — inanılan olgu/kural ama atıf henüz sabitlenmemiş]`

Çözümlenmemiş işaretlere sahip taslak nihai değildir. İşaretler doğrulama adımını açık kılar.

**Sessiz tamamlama yok.** Yapılandırılmış araştırma aracından (Lexpera, Kazancı, UYAP, mevzuat.gov.tr) bir taslağın ihtiyaç duyduğu yetki için az veya hiç sonuç dönmezse, ne bulunduğunu raporla ve dur. Şunu söyle: "Arama [araç]'tan [N] sonuç döndürdü. Kapsam [konu / karar] için ince görünüyor. Seçenekler: (1) arama sorgusunu genişlet, (2) farklı araştırma aracı dene, (3) web'de ara — sonuçlar `[web araması — doğrula]` olarak etiketlenecek ve güvenmeden önce birincil kaynağa karşı kontrol edilmeli, veya (4) `[ATI GEREKLİ]` işaretini bırak ve burada dur. Hangisini istersiniz?"

**Kaynak atıfı.** Taslaktaki her atfı gerçekte nereden geldiğiyle etiketle: araştırma bağlayıcısından alınan atıflar için `[Lexpera]`, `[Kazancı]`, `[UYAP]`, `[mevzuat.gov.tr]`; web araması atıfları için `[web araması — doğrula]`; eğitim verisinden hatırlanan atıflar için `[model bilgisi — doğrula]`; avukatın sağladığı atıflar için `[kullanıcı verdi]`. `doğrula` ile etiketlenen atıflar araç-alınan atıflardan daha yüksek imalat riski taşır ve önce kontrol edilmeli. Etiketleri asla çıkarma veya daraltma — bunlar gözden geçirecek avukatın dilekçe sunulmadan önce hangi atıfları önce doğrulayacağına dair en hızlı sinyaldir.

### Adım 5: Çıktı

**Dilekçe sunulmadan önce (sonuç doğuran eylem — bu skill taslaklar, ama kapı sunuş adımında çalışır):** `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'deki `## Bunu Kim Kullanıyor` bölümünü oku. Rol Avukat değilse:

> Dilekçe sunmak hukuki sonuçlar doğurur — kayıt hâline gelir, iddia edilen argümanlar ve olgular üzerinde müvekkili bağlar, ve imzaya bir sertifikasyon iliştirilebilir (CMK/HMK kapsamı altında imzalayanın beyanı). Bunu bir avukatla gözden geçirdiniz mi? Evet ise devam edin. Hayır ise, onlara götürmek için kısa bir özet:
>
> [1 sayfalık özet üret: taslak bölüm, teori bağlantısı, kullanılan yetki, çözümlenmemiş `[DOĞRULA]` / `[BELİRSİZ]` / `[ATI GEREKLİ]` işaretleri, yanlış gidebilecekler (olgusal yanlış beyan, desteklenmeyen atıf, teori dışı argüman), sunmadan önce avukata sorulacaklar.]
>
> Yargı çevrenizde lisanslı bir avukat bulmak için: Türkiye Barolar Birliği veya ilgili baronun yönlendirme hizmeti en hızlı başlangıç noktasıdır.

Açık bir "evet" olmadan taslağı sunulmaya hazır olarak değerlendirme. Taslak yazmak kapıyı gerektirmez — sunmak gerektirir.

Ev tarzında bölüm, satır içi işaretlerle.

Gözden geçirecek avukata önceki not (dilekçede değil — dilekçenin önüne bir not):

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar — role göre farklılaşır; bkz. `## Bunu Kim Kullanıyor`]

## Taslak Notları — [Bölüm] — [tarih]

**Teori bağlantısı:** [Bu bölüm dava teorisini nasıl destekliyor]
**Kullanılan yetki:** [liste — hepsinin Shepardize/doğrulama edilmesi gerekiyor]
**Doğrulanacak kayıt atıfları:** [N] satır içi işaretlendi
**Avukat için açık sorular:** [taslağın teyit edilmesi gereken her şeyi varsayar]
**Uzunluk:** [kelime/sayfa vs ev normu]

---

**Sunmadan önce atıf kontrolü.** Bu taslaktaki atıflar bir yapay zeka modeli tarafından üretildi ve birincil kaynağa karşı doğrulanmadı. Dosyaya sunulmadan önce her davayı, kanunu ve yönetmeliği Lexpera, Kazancı, UYAP veya mevzuat.gov.tr üzerinden doğruluk ve yürürlük açısından çalıştırın. Sunulan dilekçelerdeki uydurmalar veya yanlış alıntılar disiplin yaptırımına neden olmuştur.

**Yalnızca taslak — sunum değil.** Bu bölümü sunmak bir yargılamaya katılır (veya devam eder) ve HMK/meslek etiği maruziyeti taşır. Lisanslı bir avukat denetleyip düzenler ve dava dosyasına girmeden önce mesleki sorumluluk üstlenir. İncelenmeden sunma.
```

## Olgular Beyanı Özellikleri

Olgular beyanı, seçim ve sıralama yoluyla savunuculuktur, argüman değil.

- Aksi için bir neden yoksa kronolojik
- **Olgular beyanındaki her olgu kayda atıfla — bir sayfa ve satır referansı, bir dava kaydı, bir sergi.** "Veya kabul edildi" kayıt atfının yerine geçmez.
- Seçim yoluyla çerçevele: hangi olgular öne çıkar, hangisi bir satır alır, hangisi çıkarılır (gerekli değilse ve yararlı değilse)
- Argüman yok. "Sözleşme açıkça X gerektiriyordu" argümandır. "Sözleşmede 'X' yazdı." olgudur.

## Argüman Bölümü Özellikleri

- Olgularla değil kuralla başla (genellikle — ev tarzı farklı olabilir)
- Bölüm başına bir argüman. Gerçekten iki argümansa, iki bölümdür.
- Karşı tarafın en iyi karşı argümanına değin. Ondan saklanma — bariz karşı argümanı görmezden gelen dilekçe, hakimin güvenmediği dilekçedir.

## Bu Skill'in Yapmadıkları

- Nihai dilekçe üretmek. Taslak üretir. Her atfın doğrulanması, her argümanın avukat gözü gereklidir.
- Strateji kararı vermek. Konuyu iki şekilde argüman etme seçeneği varsa, her ikisini de işaretle ve avukatın seçmesine izin ver.
- Herhangi bir şeyi sunmak. Hiçbir zaman.
