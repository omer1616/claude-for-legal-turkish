---
name: ilk-kurulum
description: Hukuk Asistanı'nı ilk kez kurar — beş kısa soruyla pratik profilini yazar, çalışma klasörünü oluşturur ve komutları tanıtır. Yeni kurulumda veya profili baştan yapmak istediğinde kullan.
argument-hint: "[--redo]"
---

# /ilk-kurulum

**Bu kurulumun tamamı 3-5 dakika sürmeli.** Beş kısa soru, bir onay, bitti. Uzun
görüşme yok, risk matrisi yok, şablon belge talebi yok — bu eklenti bilinçli olarak
sade. Kullanıcı muhtemelen teknik konulara hâkim olmayan bir avukat: teknik terim
kullanma ("frontmatter", "YAML", "config path" deme), her adımda ne olduğunu bir
cümleyle söyle.

## Adımlar

### 1. Mevcut kurulumu kontrol et

`~/.claude/plugins/config/claude-for-legal-turkish/hukuk-asistani/CLAUDE.md` dosyasına bak:

- **Yoksa** → kuruluma başla (adım 2).
- **Varsa ve doluysa** (`[YER_TUTUCU]` kalmamış) ve `--redo` verilmemişse → "Kurulumun
  zaten tamam. Baştan yapmak istersen `/hukuk-asistani:ilk-kurulum --redo` çalıştır;
  komutları görmek istersen `/hukuk-asistani:yardim`." de ve dur.
- **Varsa ama yarım kalmışsa** → hangi soruların cevaplandığını söyle, kalanlardan devam
  etmeyi teklif et.

Ayrıca `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasına
bak. Varsa (kullanıcı başka bir hukuk eklentisi kurmuş demektir) oradaki cevapları
yeniden sorma — tek cümleyle onaylat: "Diğer eklentiden şu bilgileri buldum: [özet].
Doğru mu?"

### 2. Karşılama

Şöyle bir mesajla aç (kendi sesinle, kısa tut):

> Hoş geldin. Beş kısa soruyla seni tanıyacağım — yaklaşık 3 dakika sürer. Verdiğin
> her cevap sonradan değiştirilebilir. Başlayalım mı?

### 3. Sorular

Soruları **iki grup halinde** sor ve her grupta cevabı bekle. Kullanıcı bir soruyu
geçmek isterse zorla — "atla" geçerli bir cevaptır, yerine `[YER_TUTUCU]` yazılır.

**Grup 1 (kim ve nasıl):**

> 1. **Bunu kim kullanacak?**
>    (a) Avukat / hukukçu (stajyer ve hukuk müşaviri dahil)
>    (b) Hukukçu değilim
>    *(Bu, ürettiğim belgelerin başlığını belirler — avukat çıktıları gizlilik başlığı
>    alır, diğerleri "avukatla incele" notu alır.)*
>
> 2. **Nasıl çalışıyorsun?**
>    (a) Bağımsız avukat  (b) Bir büroda  (c) Şirket içi hukuk  (d) Diğer

Cevap 1(b) ise bir kez şunu söyle (sonra her çıktıda tekrarlama):

> Her özelliği kullanabilirsin. İki şey değişir: çıktıları karar olarak değil,
> avukatla incelenecek araştırma olarak çerçevelerim; ve hukuki sonucu olan adımlarda
> (ihtarname göndermek, dilekçe sunmak, sözleşme imzalamak) bir avukata danışıp
> danışmadığını sorarım. İhtiyacın olursa baronun avukat yönlendirme servisi en hızlı
> başlangıç noktasıdır.

**Grup 2 (ne ve nerede):**

> 3. **Ağırlıklı çalışma alanların neler?** Serbestçe yaz — ör. "ticari davalar ve
>    icra", "iş hukuku ağırlıklı, biraz aile". "Her şeyden geliyor" da geçerli cevap.
>
> 4. **Hangi ilde çalışıyorsun, en sık hangi mahkemelere/mercilere gidiyorsun?**
>    Ör. "Ankara — İş Mahkemesi, İcra Daireleri". Emin değilsen sadece ili yaz.
>
> 5. **Belgelerini nereye kaydedeyim?** Varsayılan önerim: Belgeler klasörünün içinde
>    `Hukuk-Asistani` adlı bir klasör (`~/Documents/Hukuk-Asistani`). "Olur" dersen
>    orayı kullanırım; başka bir yer istersen yolunu yaz.

Kullanıcı bir kanun, süre veya eşik söylerse (ör. "iş davalarında arabuluculuk artık
zorunlu değil" gibi) — profili yazmadan önce bildiklerinle karşılaştır; çelişki varsa
`[öncül işaretlendi — doğrula]` etiketiyle yüzeye çıkar.

### 4. Çalışma klasörünü oluştur

Seçilen kökte şu klasörleri oluştur: `dosyalar/`, `sozlesmeler/`, `dilekceler/`,
`ozetler/`, `arastirmalar/`. Köke kısa bir `BENIOKU.md` yaz: bu klasörün Hukuk
Asistanı tarafından kullanıldığını, hangi alt klasörde ne olduğunu ve dosyaların düz
metin olduğunu (istediği programla açabileceğini) iki paragrafta anlat.

### 5. Profili yaz

`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonunu iskelet olarak kullan;
`~/.claude/plugins/config/claude-for-legal-turkish/hukuk-asistani/CLAUDE.md` yoluna yaz
(gerekirse ara dizinleri oluştur). Cevapları ilgili alanlara doldur, atlanmış alanları
`[YER_TUTUCU]` bırak, `[TARİH]` alanlarına bugünü yaz. Guardrail bölümlerini şablondan
aynen koru — onlar eklentinin çalışma kurallarıdır, kullanıcı cevabı değildir.

### 6. Onaylat ve turu göster

Önce tek paragraf özet: "İşte yakaladıklarım: [rol], [çalışma şekli], [alanlar],
[il/merciler], belgeler [klasör]'de. Yanlış olan var mı?" Cevabı bekle; düzeltme
gelirse profili güncelle.

Sonra kısa tur:

> Hazırsın. Günlük kullanımda işine yarayacaklar:
>
> - **Yeni bir dava/iş geldiğinde:** `/hukuk-asistani:yeni-dosya`
> - **"Dosyalarım ne durumda, bu hafta ne var?":** `/hukuk-asistani:dosyalarim`
> - **Duruşmadan döndün, tebligat geldi:** `/hukuk-asistani:dosya-notu`
> - **Sözleşme geldi, incele:** `/hukuk-asistani:sozlesme-incele`
> - **Sözleşme lazım, hazırla:** `/hukuk-asistani:sozlesme-hazirla`
> - **Dilekçe / ihtarname yaz:** `/hukuk-asistani:dilekce`
> - **Uzun bir karar/rapor geldi, özetle:** `/hukuk-asistani:ozetle`
> - **Hukuki bir sorun araştır:** `/hukuk-asistani:arastir`
>
> Komut ezberlemek zorunda değilsin — derdini normal cümleyle yaz, ben doğru aracı
> seçerim. Bu listeyi tekrar görmek için: `/hukuk-asistani:yardim`
>
> İlk adım önerim: elindeki en güncel dava için `/hukuk-asistani:yeni-dosya` çalıştır.

## Bu skill'in yapmadıkları

- 15 dakikalık görüşme yapmaz; beş sorunun ötesine geçmez. Derinlemesine profil
  isteyen kullanıcıyı `dava-takibi` gibi kapsamlı eklentilere yönlendirebilirsin.
- Kullanıcının kişisel `~/CLAUDE.md` dosyasını veya geçmiş konuşmalarını okumaz;
  profil yalnızca bu görüşmedeki cevaplardan yazılır.
- MCP bağlayıcısı kurmaya çalışmaz — bu eklenti bağlayıcısız çalışacak şekilde
  tasarlandı. Kullanıcı bir araştırma aracı bağlarsa `arastir` skill'i onu kendiliğinden
  kullanır.
- Atlanan sorular için değer uydurmaz — `[YER_TUTUCU]` bırakır.
