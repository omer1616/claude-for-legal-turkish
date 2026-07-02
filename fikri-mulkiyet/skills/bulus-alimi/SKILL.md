---
name: bulus-alimi
description: >
  Buluş bildirimi ilk aşama taraması — yenilik (novelty), buluş basamağı 
  (inventive step), patentlenebilir konu (SMK m. 82), hoşgörü/bar süreleri, 
  tespit edilebilirlik ve stratejik değer analizi yapar. 
  Bir buluş bildirimi geldiğinde ve bir önceki teknik (prior-art) araştırmasına, 
  patent vekili incelemesine değip değmeyeceğine karar verilmesi gerektiğinde kullanın.
argument-hint: "[buluş bildirimini yapıştırın veya açıklayın — veya sadece başlığı verin, ben sorarım]"
---

# /bulus-alimi

**Bu, uzman olmayan biri tarafından yapılan ilk aşama bir taramadır, bir patentlenebilirlik görüşü değildir.** Tarama asla bir buluşun kesin olarak patentlenebilir olduğu sonucuna varmaz — sadece ilk taramayı geçtiği (önceki teknik araştırmasına ve vekil incelemesine değdiği), daha fazla bilgiye ihtiyaç duyduğu veya reddedilmesi gerektiği sonucuna varır. Bu yetenek (skill) önceki teknik araştırması (prior-art search) YAPMAZ.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` dosyasını okuyun. Eğer `[YER_TUTUCU]` içeriyorsa, `/fikri-mulkiyet:ilk-kurulum`'a yönlendirin. Patent pratiği yoksa kullanıcıyı uyarın.
2. Aşağıdaki iş akışını izleyin.
3. Girdi alın (Bulşu oku veya 7 temel soruyu sor: ne olduğu / çözülen problem / farkı / buluşçular / kamuya açıklama / kullanım durumu / teknoloji alanı).
4. Altı kriterli taramayı yapın: Yenilik sinyalleri, Buluş basamağı (obviousness) bayrakları, Patentlenebilir konu (SMK m.82 / EPC m.52), Kamuya açıklama/Hoşgörü süresi (SMK m.83), Tespit edilebilirlik, Stratejik değer. Her birine ✓ / 🟡 / 🔴 notu verin.
5. İnceleme notunu (memo) oluşturup uygun klasöre yazın. Role göre başlık ekleyin.
6. Alt çizgi kararı verin: **DEVAM ET (PURSUE)** / **ARAŞTIR (INVESTIGATE)** / **REDDET (DECLINE)**.
7. İlgili karar ağacı (decision tree) ile kapatın. Kamuya açıklama süresi sıkıntılıysa **"Zamana karşı hassas (time-sensitive)"** bayrağını en üste ekleyin.

## Örnekler

```
/fikri-mulkiyet:bulus-alimi "LRU yerine öğrenilmiş bir model kullanan yeni bir önbellek (cache) boşaltma algoritması; bu yıl Q1'de tasarlandı, henüz açıklanmadı, staging ortamında prototipi var."
```

---

## BU BİR ÖN TARAMADIR, PATENTLENEBİLİRLİK GÖRÜŞÜ DEĞİLDİR

> **Bu, uzman olmayan biri tarafından yapılan bir ön taramadır, patentlenebilirlik görüşü değildir.** Patentlenebilirlik görüşü, önceki teknik araştırması, istem (claim) yapılandırması ve kayıtlı bir patent vekilinin (TÜRKPATENT / EPO) değerlendirmesini gerektirir. Bu tarama önceki teknik araştırması (prior art search) yapmaz. Sadece bariz ret nedenlerini (zaten piyasada olma, iki yıl önce yayınlanma, sırf soyut fikir olma vb.) ve bariz olumlu yönleri eler. 

Gereğinden az işaretleme (under-flagging), geri dönülmez hak kayıplarına yol açar (kamuya açıklamadan itibaren SMK'daki 1 yıllık hoşgörü süresi biterse yenilik ortadan kalkar). Şüphe varsa işaretleyin (🟡).

---

## Profil ve Bağlam

CLAUDE.md'den:
- Şirketin patent stratejisi (saldırgan/savunmacı/karma)
- İlgilenilen teknoloji alanları
- Bütçe yaklaşımı (agresif / seçici)
- Onay zinciri

Bilgilerini çekin ve değerlendirmeyi bu stratejiye göre yönlendirin.

## Girdi Alma Soru Listesi

1. **Buluş nedir?** (Basit dille)
2. **Hangi problemi çözüyor?**
3. **Mevcut olanlardan farkı ne?**
4. **Buluşçuları kim ve yaklaşık tasarım tarihi ne?**
5. **Kamuya açıklandı mı?** (Makale, repo, konferans, satış teklifi, NDA'siz müşteri demosu vb. Ne zaman ve nerede?)
6. **Kullanım durumu nedir?** (Satışta, pilot aşamada, kağıt üstünde vb.)
7. **Teknoloji alanı nedir?**

## Altı Aşamalı Tarama (Screens)

### 1. Yenilik Sinyalleri (Novelty - SMK m.82/3)
- 🔴 Sadece bilinen bir tekniğin yeni bir alana uygulanması, var olan ürünün küçük bir ayarı.
- ✓ Yeni bir mekanizma, beklenmeyen bir teknik etki (technical effect), daha önce çözülememiş bir problemin çözümü.

### 2. Buluş Basamağı / Aşikarlık (Inventive Step / Obviousness - SMK m.82/4)
- 🔴 Bilinen elemanların öngörülebilir birleşimi, rutin optimizasyon, estetik tasarım değişikliği.
- ✓ Uzmanın beklediğinin aksine bir sonuç (teaching away), uzun süredir hissedilen ihtiyacın karşılanması.

### 3. Patentlenebilir Konu Hukuki Uygunluğu (SMK m.82/2 - EPC m.52)
- 🔴 Sırf iş yapma yöntemi (business method), soyut matematiksel algoritma, sadece zihni bir faaliyet veya oyun kuralı. (Türkiye ve EPO'da salt yazılımlar "oldukları halleriyle" patentlenemez).
- ✓ Bilgisayara uygulanan buluşlarda (CII) donanıma veya fiziksel dünyaya yansıyan bir "teknik etki" (technical effect), donanımın çalışmasını iyileştirme.
*Not: US §101 Alice/Mayo ile EPO/TÜRKPATENT yaklaşımı farklıdır. Türkiye'de teknik etki varsa yazılım tabanlı patent alınması daha olasıdır. Bunu not düşün.*

### 4. Kamuya Açıklama / Hoşgörü Süresi (Bar Dates - SMK m.83)
- 🔴 Kamuya 12 aydan daha önce açıklanmış (Yenilik mutlak olarak ortadan kalkmıştır).
- 🟡 Son 12 ay içinde açıklanmış (Türkiye'de 1 yıllık hoşgörü süresi işlemekte, hızlı olunmalı; yabancı ülkelerde -örneğin Avrupa dışı bazı yerlerde- mutlak yenilik arandığı için haklar çoktan kaybedilmiş olabilir). Acil bayrağı koyun.
- ✓ Henüz açıklanmamış. (Gizlilik anlaşması / NDA altındaki görüşmeler genel olarak kamuya açıklama sayılmaz).

### 5. Tespit Edilebilirlik (Detectability)
- 🔴 Arka planda sunucuda çalışan algoritma veya iç üretim tekniği. (Bunun **Ticari Sır (Trade Secret)** olarak korunması daha mantıklı olabilir. Patentle ifşa etmek rakibe bedava bilgi vermektir).
- ✓ Tüketici ürünü, açık API/SDK, tersine mühendislikle anlaşılabilecek cihaz.

### 6. Stratejik Değer
- Şirketin IP profiline (savunmacı/saldırgan vs.) ve odaklandığı teknoloji alanlarına uyuyor mu?

## Çıktı Formatı (Memo)

Bkz. orijinal `invention-intake/SKILL.md`. Aynı tablo yapısını kullanın: Sonuç (Pursue / Investigate / Decline), Ekran Sonuçları, Açık Sorular ve Karar Ağacı.

**Sonuç Kararları:**
- **DEVAM ET (PURSUE):** Taramayı geçti, araştırma (prior-art) ve vekil incelemesi ayarlayın. ("Patentlenebilir" demeyin).
- **ARAŞTIR (INVESTIGATE):** Arafta, buluşçudan veya vekilden daha fazla bilgi lazım.
- **REDDET (DECLINE):** 1 yılı geçmiş açıklama, sadece soyut fikir veya şirket alanına girmiyor. Reddetme sebebi açıkça yazılır.

Avukat olmayanlar için bir bilgilendirme notu (Gate) ekleyin: "Bu bir patentlenebilirlik görüşü değildir, kararı patent vekili vermelidir..."
