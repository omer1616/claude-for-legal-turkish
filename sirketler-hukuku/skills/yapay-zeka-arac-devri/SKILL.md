---
name: yapay-zeka-arac-devri
description: >
  Luminance, Kira veya benzeri bir toplu inceleme (bulk-review) aracının kullanımda 
  olduğunu tespit eder, yüksek hacimli madde (clause) çıkarım işini ona devreder ve 
  çıktısını `CLAUDE.md`'deki güven (trust) seviyesine göre kalite kontrolünden (QA) geçirir. 
  Kullanıcı "Luminance'a gönder", "toplu inceleme", "yapay zeka çıkarımı" dediğinde veya 
  due-diligence-sorun-cikartma yüksek hacimli bir kategoriye çarptığında kullanın.
---

# /yapay-zeka-arac-devri

1. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` yükle → Yapay zeka destekli inceleme.
2. Eğer araç yoksa → doğrudan `due-diligence-sorun-cikartma`'ya geç.
3. Eğer araç varsa → hacim ve madde tiplerini kontrol et, devret.
4. Sonuç geldiğinde güven seviyesine göre (as-is, spot-check, full re-review) kalite kontrolü yap.
5. Hukuki değerlendirme (judgment layer) uygula ve sonuçları diligence bulgularına gönder.

---

## Dosya (Matter) Bağlamı

`CLAUDE.md` içindeki `## Dosya çalışma alanları`nı kontrol et. Çıktıları `matters/<dosya-slug>/` klasörüne yaz.

---

## Amaç

Luminance ve Kira bir şeyde çok iyidir: 500 sözleşmeyi okuyup her kontrol değişikliği (CoC) maddesini bulmak. Yargıda (hukuki değerlendirmede) o kadar iyi değillerdir — örneğin, belirli bir CoC hükmünün bu işlem yapısıyla tetiklenip tetiklenmediğine karar vermek.

Bu yetenek, toplu çıkarımı doğru araca devreder, ardından geri gelenler üzerinde kalite kontrol (QA) ve hukuki değerlendirme (judgment) katmanını çalıştırır.

**Devretmeden önce:** İlk olarak `tablo-inceleme` (`/sirketler-hukuku:tablo-inceleme`) yeteneğini deneyin. Birkaç yüz belge gibi yönetilebilir hacimler için, yerel bir tablo incelemesi (tabular review) kurmak daha hızlıdır, belge başına maliyeti yoktur ve iş ürününü yerel tutar. Araç (Luminance/Kira) devrini; veri seti gerçekten çok büyük olduğunda, ekibin zaten bir lisansı/süreci olduğunda veya dosya onaylanmış bir kaynak zinciri (provenance) gerektirdiğinde yapın.

## İçerik Yükle

`CLAUDE.md` → Yapay zeka destekli inceleme (AI-assisted review):
- Kullanılan araç (Luminance / Kira / Hiçbiri)
- Ne için kullanıldığı (hangi madde tipleri)
- Güven seviyesi (olduğu gibi kullan / nokta kontrol (spot-check) yap / yeniden tam incele)
- Devir süreci (kim yüklüyor, kim QA yapıyor)

## Ne Zaman Devredilmeli (Handoff)

Şunların tümü geçerliyse devret:
- Kategori >50 belgeye sahipse (daha azsa, okumak/tablo incelemesi yapmak daha hızlıdır).
- Çıkarım hedefi, aracın iyi olduğu bir madde türüyse (CoC, devir (assignment), münhasırlık, MFN, fesih, otomatik yenileme).
- Belgeler makul ölçüde tek tipse (hepsi müşteri sözleşmesi vb. - karmaşık sözleşme/tutanak/yan mektup karışımı değil).

Şunlarda devretme:
- Özel (bespoke) veya ağır müzakere edilmiş belgeler.
- Yan mektuplar ve zeyilnameler/ek protokoller (araçlar ana sözleşmeyle etkileşimi kaçırır).
- Sorunun "bu madde var mı" değil, "bunun işlem için anlamı ne" olduğu herhangi bir şey.

## Devir İşlemi

### Adım 1: Yığını Hazırla
- VDR envanterinden belgeleri belirle.
- `CLAUDE.md`'ye göre çıkarım hedeflerini belirt.
- Aracın çıktısının filtrelenebilmesi için önemlilik eşiğini not et.

### Adım 2: Yükle (Veya yükleyiciye talimat ver)
Eğer sen (Claude) yüklüyorsan, yükleme talimatlarını oluştur. Eğer başka biriyse, talebi (request) oluştur:

```markdown
## [Araç] Yükleme Talebi — [İşlem kodu] — [Kategori]

**Belgeler:** VDR klasörü [yol]'dan [N] belge
**Yükleme yeri:** [Araç çalışma alanı/matter]
**Çıkarım hedefleri:**
- Kontrol değişikliği / Devir (Assignment)
- Münhasırlık (Exclusivity)
- [CLAUDE.md'deki diğer hedefler]

**Çıktıyı filtrele:** Sadece çıkarım hedefinin MECUT olduğu yerleri işaretle ("CoC bulunamadı"ya gerek yok).
**Teslim tarihi:** [tarih]
```

### Adım 3: Çıktıyı Kalite Kontrolünden (QA) Geçir
Araç sonuçları döndürdüğünde güven seviyesini uygula:
- **"Olduğu gibi kullan (Use as-is)":** Doğrudan diligence bulgularına al (sadece `CLAUDE.md` söylüyorsa - ki bu nadirdir).
- **"Nokta kontrolü yap (Spot-check) %X":** İşaretlenmiş belgelerin %X'ini rastgele örnekle. Maddeyi gerçekte oku ve aracın çıkarımıyla karşılaştır. Hata oranı düşükse kabul et. Hataysa, örneklemi genişlet.
- **"İşaretlilerin tam insan incelemesi":** Araç evreni daraltır (500 belge → CoC içeren 80 belge). İnsan (veya Claude) 80 belgenin tamamını okur. Araç, temiz 420 belgeyi okuma zamanından tasarruf sağlamıştır.

### Adım 4: Hukuki Değerlendirme (Judgment) Katmanı
Araç maddeleri buldu. Şimdi hukuki yargı uygulayın:

İşaretlenmiş her CoC/Devir hükmü için: *Bu işlemle (deal) gerçekten tetikleniyor mu?*
- Hisse devri vs. varlık devri vs. birleşme — farklı tetikleyiciler vardır. (Örn: TTK/TBK kurallarına göre hisse devrinde CoC tetiklenmiyorsa ama sözleşmede açıkça "pay sahipliği değişikliği" yazıyorsa tetiklenir).
- Sözleşmede "Kontrol değişikliği" nasıl tanımlanmış — çoğunluk mülkiyeti? yönetim kurulu kontrolü?
- Bu tür bir işlem için istisna (carve-out) var mı?

Bu aracın (Luminance/Kira) yapamayacağı kısımdır. Çıktı, kurum formatında diligence bulgularına gider.

## Çıktı

```markdown
## Yapay Zeka Araç Devri Özeti — [Kategori]

**Araç:** [Luminance / Kira]
**İşlenen belge:** [N]
**Çıkarım hedefleri:** [madde tipleri]

### Kalite Kontrol (QA)
**Güven seviyesi:** [`CLAUDE.md`'ye göre]
**Örneklem boyutu:** [N] belge nokta-kontrol edildi
**Hata oranı:** % [X] — [Kabul Edildi / Örneklem Genişletildi / Yeniden Tam İnceleme Tetiklendi]

### Sonuçlar
| Madde tipi | İşaretlenen Belge | Hukuki Değerlendirme Sonrası | Önemli (Material) |
|---|---|---|---|
| Kontrol Değişikliği | [N] | [İşlem yapısıyla tetiklenen N] | [Eşik üzerindeki N] |
| Devir (Assignment) | [N] | [N] | [N] |

**→ Diligence sorunlarına [N] bulgu eklendi**
**→ Kapanış kontrol listesine [N] onay eklendi**
```

## Bu yetenek ne yapmaz
- Luminance veya Kira'yı *kendi çalıştırmaz* — devri ve QA'yi yönetir. Çıkarımı bir insan (veya aracın kendi arayüzü) çalıştırır.
- Aracın çıktısını tamamen kendi yargısıyla değiştirmez — eğer spot-check %10 diyorsa, %10'unu kontrol eder, %100'ünü değil.
- Güven seviyesine karar vermez — bu, ilk kurulumda belirlenmiş `CLAUDE.md` kuralıdır.
