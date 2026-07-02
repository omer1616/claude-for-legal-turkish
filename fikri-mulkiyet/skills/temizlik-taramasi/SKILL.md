---
name: temizlik-taramasi
description: >
  Marka temizlik (clearance) ilk taraması — kesin ret nedenleri (knockout) ve 
  karıştırılma ihtimali kontrolü yaparak bir araştırma notu (memo) üretir; 
  kesin bir marka temizlik onayı (clearance opinion) DEĞİLDİR. Yeni bir marka 
  önerildiğinde, "bu marka müsait mi?" diye sorulduğunda veya tam kapsamlı 
  profesyonel bir araştırmadan önce ön risk analizi yapmak için kullanın.
argument-hint: "[önerilen markayı, mal/hizmetleri ve yargı çevrelerini açıklayın — veya sadece markayı verin, ben sorarım]"
---

# /temizlik-taramasi

**Bu bir ön triyajdır, hukuki bir marka temizlik onayı (clearance opinion) değildir.** Bir markanın temiz (clear) olduğuna dair hukuki görüş, tam kapsamlı profesyonel bir araştırmayı ve marka vekilinin/avukatının değerlendirmesini gerektirir. "Açık bir çakışma yok" sonucu sadece *bu taramanın* bir şey bulmadığını gösterir — markanın sorunsuz olduğu anlamına gelmez.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` dosyasını okuyun. Eğer `[YER_TUTUCU]` içeriyorsa, durun ve `/fikri-mulkiyet:ilk-kurulum`'a yönlendirin.
2. Aşağıdaki iş akışını izleyin.
3. Girdi alın (marka, mal/hizmetler, sınıflar, yargı çevreleri, görsel özellikler).
4. Mutlak Ret Nedenleri (Knockout / SMK m.5) kontrolü yapın — ayırt edici nitelikten yoksun, tanımlayıcı, yanıltıcı, coğrafi işaret, kamu düzenine aykırı, vb.
5. Benzer marka araştırmasını (Nispi ret nedenleri / SMK m.8 potansiyeli) bağlı olan araçlarla yapın (Lexpera, Kazancı, Web araması veya TÜRKPATENT MCP'si varsa). Hiçbiri bağlı değilse, bunu çıktıda belirtin ve sadece faktör analizine geçin.
6. Karıştırılma ihtimali faktörlerini (benzerlik, mal/hizmet yakınlığı, hedef kitle vb.) değerlendirin. Her birini işaretleyin; ASLA kesin sonuç bildirmeyin.
7. Çıktıyı (triage memo) aktif dosya klasörüne (eğer dosya modu açıksa) veya genel çıktılar klasörüne yazın. Başlığı role göre ekleyin.
8. Önerilen sonraki adımlar ile bitirin.

## Örnekler

```
/fikri-mulkiyet:temizlik-taramasi "APEXLEAF outdoor giyim için, Türkiye ve AB pazarı"
```

```
/fikri-mulkiyet:temizlik-taramasi
```
(Marka, mal/hizmet ve ülke bilgilerini siz sorarsınız.)

---

## BU BİR ÖN TARAMADIR, HUKUKİ GÖRÜŞ DEĞİLDİR

**Bunu her çıktının en üstünde belirtin. Yumuşatmayın.**

> **Bu bir ön taramadır (first pass), hukuki marka temizlik görüşü değildir.** Kapsamlı bir temizlik görüşü, tam bir profesyonel araştırma (TÜRKPATENT sicili, WIPO/Madrid, ticaret sicilleri, alan adları, sosyal medya ve kullanıma dayalı haklar) ve karıştırılma ihtimaline ilişkin vekil/avukat değerlendirmesi gerektirir. "Açık bir çakışma bulunamadı" sonucu sadece bu sınırlı taramanın bir engel bulmadığı anlamına gelir. Herhangi bir kullanım, tescil başvurusu veya yatırımdan önce tescilli bir marka vekili veya uzman avukat değerlendirmelidir.

---

## İlk Kurulum (Pratik Profili) Kontrolü

Tarama yapmadan önce `CLAUDE.md` içindeki:
- **Rolü** (iş ürünü başlığını belirler)
- **Kayıtlı olunan ve izlenen yargı çevrelerini** (ör. Türkiye / AB)
- **Karar Alma Yaklaşımını** çekin.

Geçici (Provisional) Mod: Profil kurulmamışsa kullanıcıya sorarak jenerik ayarlarla çalışabilir ve bunu açıkça belirtebilirsiniz.

## Girdi Alma (Intake)

> Taramaya başlamadan önce:
> 1. **Önerilen marka** (tam yazılışı, varsa şekil/logo)
> 2. **Mal veya hizmetler** (neler sunulacak, 1-2 cümle)
> 3. **Sınıflar** (biliyorsanız Nice sınıfları, yoksa ben tahmin edeceğim)
> 4. **Yargı Çevreleri** (Türkiye, AB (EUIPO), WIPO vb. - belirtmezseniz profilinizdekileri kullanacağım)
> 5. **Kullanım şekli** (varsa eşlik edecek slogan, vb.)

## Mutlak Ret / Knockout Kontrolü (SMK m. 5 odaklı)

Şunları kontrol edin:
- **Jenerik (Cins İsim)** / **Tanımlayıcı (Tasviri)**: Marka doğrudan malı/hizmeti veya bir özelliğini tanımlıyor mu?
- **Yanıltıcı (Deceptive)**: Tüketiciyi nitelik veya coğrafi kaynak konusunda aldatır mı?
- **Coğrafi Kaynak**: Ürünün menşei ile ilgili yanıltıcı veya tescilli bir coğrafi işaret mi?
- **Kamu Düzeni / Genel Ahlak**
- **Şekli veya İşlevsel Zorunluluk**: Ürünün doğası gereği olan bir şekil mi?

*Çıktı:* Her biri için "Sorun yok" veya "İşaretlendi (sebep)" belirtin.

## Benzer Marka Kontrolü (Nispi Ret / SMK m. 8 potansiyeli)

Bağlı araçlarla ön tarama yapın. Eğer araç yoksa şunu ekleyin:
> **Veritabanı araştırması yapılamadı.** Bu tarama TÜRKPATENT, EUIPO veya WIPO veritabanlarını doğrudan taramadı. Analiz, sadece yapısal engeller (mutlak ret) ve varsa bahsedilen markalar üzerindeki karıştırılma ihtimali analizinden ibarettir.

**Yanal Aileler (Adjacent families):** "NEXUS HOME" için "HUB, CONNECT, CASA, SMART, NEXIS" gibi kategorik eşanlamlılar veya fonetik benzerleri de listeleyin ve arama yapın (veya yapılmasını önerin). Ayrıca özellikle yabancı dillerin Türkiye'de ortalama tüketici tarafından bilinirliği (ör. İngilizce kelimelerin Türkçe çevirileri) de SMK kapsamında dikkate alınır.

## Karıştırılma İhtimali Faktörleri

Türkiye'de (SMK m.8) Yargıtay ve TÜRKPATENT uygulaması Avrupa (EUIPO) uygulamasıyla yüksek paralellik gösterir (Global Appreciation - Bütüncül Değerlendirme).
Faktörler:
- Markaların görsel, işitsel (fonetik) ve anlamsal benzerliği
- Mal ve hizmetlerin benzerliği / tamamlayıcılığı (Nice sınıfları yetmez, fiili pazar dikkate alınır)
- İlgili tüketici kesiminin dikkat seviyesi (ör. sakız vs. tıbbi cihaz)
- Önceki markanın ayırt edicilik gücü ve tanınmışlığı
- Bütünsel izlenim (ortak unsurun baskınlığı)

Her faktör için bir bayrak (işaret) üretin. **ASLA "karıştırılma ihtimali yoktur" demeyin.**

## Sonraki Adımlar

- Mutlak ret riski varsa: Markayı revize etme veya ayırt edicilik kazandırma (secondary meaning / SMK m.5/2) stratejisi.
- Benzer marka bulunduysa: Uzman avukat görüşü, rıza beyanı (muvafakatname) alınması (SMK m.5/3) veya itiraz riskinin analizi.
- Kapsamlı profesyonel araştırma gerekliliği (her zaman).

## Çıktı Formatı

Bkz. orijinal kaynak `clearance/SKILL.md` - aynı şablonu (Başlık, Mutlak Ret Tablosu, Benzer Markalar Tablosu, Faktörler Tablosu) Türkçe olarak kullanın.
Avukat olmayan kullanıcılar için mülakat sonunda "Avukata/Vekile Sunulacak Özet" (Non-lawyer gate) kısmını ekleyin.
