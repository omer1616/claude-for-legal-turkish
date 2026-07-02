---
name: due-diligence-sorun-cikartma
description: >
  VDR belgelerini okur ve kurum kategorilerine ve önemlilik eşiklerine göre 
  sorunları çıkararak, bulguları kurum içi formatta üretir. Kullanıcı 
  "veri odasını (data room) incele", "[klasör] içindeki sorunları çıkar", 
  "due diligence incelemesi", "VDR'da ne var" dediğinde veya VDR belgelerini 
  işaret ettiğinde kullanın.
argument-hint: "[VDR klasör yolu veya kategori adı]"
---

# /due-diligence-sorun-cikartma

1. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` + `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/deals/[kod]/deal-context.md` dosyalarını yükle.
2. Aşağıdaki iş akışını kullan.
3. `yapay-zeka-arac-devri` (ai-tool-handoff) yeteneğini kontrol et — kategori toplu ise ve araç yapılandırılmışsa, önce oraya devret.
4. Belgeleri oku, önemlilik filtresi uygula, kategori bazında çıkarım yap.
5. Bulguları kurum (house) formatında üret. İzin/onay gerekliliklerini kapanış kontrol listesine (kapani-kontrol-listesi) devret.

---

## Dosya (Matter) Bağlamı

`CLAUDE.md` içindeki `## Dosya çalışma alanları`nı kontrol et. Eğer `Etkin` değilse (şirket-içi kullanıcılar için varsayılan), bu paragrafı atla. Eğer etkinse ve aktif dosya yoksa sor: "Bu hangi dosya (matter) için? `/sirketler-hukuku:dosya-calisma-alani degistir <slug>` çalıştır." Dosyaya özel bağlam için `matter.md` dosyasını yükle. Çıktıları `matters/<dosya-slug>/` klasörüne yaz.

---

## Amaç

VDR'da 2.000 belge var. Bir yerlerde bu işlem için önemli olan 30 belge var. Bu yetenek, `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` dosyasındaki due diligence kategorilerine ve önemlilik eşiklerine (materiality threshold) göre belgeleri okur, sorunları çıkarır ve bunları kurumun sorun/bulgu notu formatında yazar.

## İçerik Yükle

- `CLAUDE.md` → Due diligence yapısı (kategoriler, önemlilik eşikleri)
- `CLAUDE.md` → Sorun notu formatı (bulguların nasıl ifade edildiği)
- `deal-context.md` → İşleme özel eşikler, VDR konumu

`deal-context.md` yoksa, bunun hangi işlem için olduğunu sor.

## İş Akışı

### Adım 1: VDR Envanterini Çıkar

VDR MCP'si (Box/Intralinks vb.) bağlıysa, indeksi çek. VDR klasörlerini due diligence talep listesi kategorileriyle eşleştir. Boşlukları not et (VDR içeriği olmayan talep kategorileri).

```markdown
## VDR Envanteri: [İşlem kodu]

| Talep kategorisi | VDR klasörü | Belge Sayısı | Durum |
|---|---|---|---|
| Kurumsal ve Organizasyonel | /01-Kurumsal | 45 | İncendi |
| Önemli Sözleşmeler | /02-Sozlesmeler | 312 | Devam ediyor |
| Fikri Mülkiyet (IP) | /03-IP | 89 | Başlamadı |

**Boşluklar:** [VDR'da karşılığı olmayan talep kategorileri — takip talebi gerekir]
```

### Adım 2: Önemlilik filtresini uygula

Kurum (CLAUDE.md) veya işleme özel eşiklere (deal-context.md) göre çalış. Eğer eşik ">1 Milyon ₺ tutarındaki sözleşmeler" diyorsa her şeyi inceleme.

Özellikle sözleşmeler için: Belirtilen değere (dosya adında/meta verisinde varsa) veya karşı tarafın önemine göre sırala. Eşiğe ulaşana veya kategori tükenene kadar yukarıdan aşağıya incele.

### Adım 3: Sorunları çıkar

Okunan her belgeyi kendi kategorisi için standart due diligence endişelerine karşı kontrol et:

**Önemli sözleşmeler — standart çıkarım seti:**
- Kontrol değişikliği (change of control) (bu işlem tetikler mi? onay gerekli mi?)
- Devir kısıtlaması (sözleşme alıcıya devredilebilir mi?)
- Münhasırlık / rekabet yasağı (alıcının işini kısıtlar mı?)
- MFN (en çok kayrılan müşteri — fiyatlama kısıtlamaları)
- Fesih hakları (karşı taraf işlem nedeniyle sözleşmeden dönebilir mi?)
- Olağandışı tazminatlar veya sorumluluk maruziyeti

**Kurumsal (Şirketler Hukuku / TTK) — standart çıkarım seti:**
- Pay defteri (cap table) doğruluğu, opsiyonlar
- İşlem için yönetim kurulu ve genel kurul onay gereklilikleri (TTK m.390, m.408 vb.)
- Pay sahipleri sözleşmesi kısıtlamaları (birlikte satma, ön alım vb.)
- Grup şirketi yapısı ve şirketler arası düzenlemeler (TTK m.195 vd. bağlı şirket ilişkileri)

**Fikri Mülkiyet (IP) — standart çıkarım seti:**
- Mülkiyet zinciri (kuruculardan/çalışanlardan devirler yapılmış mı?)
- Üründe açık kaynak kullanımı
- Lisanslanan ve sahip olunan kritik IP
- Derdest veya tehdit aşamasındaki IP davaları

**İş Hukuku / İstihdam — standart çıkarım seti:**
- Kontrol değişikliğine bağlı kıdem/ihbar tetikleyicileri
- Kritik çalışanları elde tutma riski
- Derdest iş davaları (işe iade, alacak vb.)
- Statü riski (çalışan gibi görünen bağımsız yükleniciler)

**Dava / İhtilaf — standart çıkarım seti:**
- Derdest davalar ve ayrılan karşılıklar (TMS 37)
- İhtarnameler / olası davalar
- Düzenleyici kurum incelemeleri (Rekabet, KVKK vb.)
- Kalıpsal uyuşmazlıklar (tüketici sınıf davaları vb.)

### Adım 4: Her bulguyu formüle et

> **Kaynak Atfı.** Bir bulgu kanuna, yönetmeliğe, içtihada veya kurum kararına atıfta bulunuyorsa (örn. uygulanabilir hukuka göre analiz edilmiş bir kontrol değişikliği, doktrine dayalı bir IP mülkiyet açığı, esas numaralı bir dava) geldiği yeri etiketle: `[Lexpera]`, `[Kazancı]`, `[UYAP]` veya yasal araştırma aracından çekilen MCP araç adı; web aramaları için `[web araması — doğrula]`; eğitim verisi için `[model bilgisi — doğrula]`. VDR'dan (belge adı) gelenler kendi orijinal referansını korur. Asla etiketleri silme.
>
> **Sessiz tamamlama yok.** Hukuki araştırma aracı boş dönüyorsa uydurma. Kullanıcıya seçenek sun: 1) aramayı genişlet, 2) web'de ara, 3) işaretsiz bırak.

Bulgu şablonunu `CLAUDE.md` içinden çek. Varsa tohum belgedeki (seed memo) yapıyı harfiyen kullan:

```
Sorun #N: [Başlık]
Kategori: [talep listesi kategorisi]
Şiddet: [kurum şemasına göre seviye]
Belgeler: [VDR yolu + belge adı]
Bulgu: [belge ne diyor ve neden önemli]
Öneri/Aksiyon: [fiyat ayarlaması / tazminat / onay gerekli / beyan & tekeffül / vazgeç]
```

**Şiddet kalibrasyonu (🔴 / 🟡 / 🟢 kullanılıyorsa):**
- 🔴 **Kırmızı (Engelleyici):** İşlem değerini etkiler. Önemli müşteri onayı gereken kontrol değişikliği. Açıklanmamış ciddi dava.
- 🟡 **Sarı (Riskli):** Dikkat gerektirir, çözülebilir. Onay gerekli ama muhtemelen alınabilir. İşçi statüsü sınıflandırma riski.
- 🟢 **Yeşil (Temiz/Düşük):** Dosyaya not edildi. Sorun yok, temsil ve tekeffüllerle uyumlu.

### Adım 5: Kategori bazında birleştir

Bulguları talep kategorisine göre grupla. Kategori içinde şiddete göre sırala.

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — CLAUDE.md'den]

> Bu çıktı ayrıcalıklı veya gizli materyallerden türetilmiştir... (Meslek sırrı notu)

# Due Diligence Sorunları: [İşlem kodu] — [Kategori]

**İncelenen Belgeler:** [M] belgeden [N] tanesi
**Kapsam:** [Tümü | >X₺ eşiği | İlk N]
**Bulgular:** [N]🔴 [N]🟡 [N]🟢

---

### Alt çizgi (Bottom line)
[🔴 N engelleyici · 🟠 N yüksek · 🟡 N orta] — [işlem ekibinin bilmesi gereken tek şey]

---

[Her bulgu kurum formatında]

---

## Boşluklar
- [Yanıt veren belge bulunmayan talep maddesi]
```

## Devirler (Handoffs)

- **yapay-zeka-arac-devri'ne (Luminance/Kira vs):** Büyük sözleşme yığınları için devret.
- **anlasma-ekibi-ozeti'ne:** Birleştirilmiş bulgular işlem ekibi özetini besler.
- **onemli-sozlesme-takvimi'ne:** Sözleşme çıkarımları sözleşme açıklama listesini (disclosure schedule) besler.
- **kapani-kontrol-listesi'ne:** Kapanış öncesi bir işlemi işaret eden HER bulgu kontrol listesi maddesi olur. Sadece üçüncü taraf onayları değil:
  - Yönetim Kurulu/Genel Kurul kararları (TTK m.390, m.408)
  - Rekabet Kurumu, BDDK/SPK, Yabancı Yatırım onayları
  - Karşı taraftan alınacak "kontrol değişikliği" onayları
  - İbraname, ipotek/rehin fekki yazıları.

**Sorumluluğun geçişi (Successor Liability):**
Derdest çevre/vergi cezalarını, hileli devir risklerini, "İşletmenin devri (TBK m.202)" kuralları gereği satıcının borçlarının geçişini kontrol et. Satın alma sözleşmesi bu riskleri dışlasa bile kanundan doğan müteselsil sorumluluklar vardır (TBK m.202 iki yıl müteselsil sorumluluk öngörür).

## Toplu İşleme
Büyük kategoriler için parçalar halinde işle. 🔴 seviyesinde bir şey bulduğunda hemen kullanıcıya bildir, tüm yığının bitmesini bekleme.

## Kapanış: Sonraki Adımlar Karar Ağacı
CLAUDE.md'deki `## Çıktılar` bölümüne uygun karar ağacıyla bitir (Örn: sözleşme listesini taslakla, BHM'ye rapor et vb.). 10'dan fazla bulgu varsa dashboard öner.

## Bu yetenek (skill) ne yapmaz
- Sınırda kalan vakalarda önemlilik kararını vermez (insana bırakır).
- Temsil ve tekeffülleri (reps and warranties) müzakere etmez, sadece onları besleyecek bulguları üretir.
