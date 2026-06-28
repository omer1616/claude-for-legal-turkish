---
name: dosya-kapatma
description: Bir dosyayı kapatır — sonucu, nihai maruziyeti ve öğrenilen dersleri yakalar, ardından kaydı silmeden aktif portföyden arşivler. Kullanıcı bir dosyayı kapatmak istediğinde, "[dosya] bitti" dediğinde veya sulh, ret, karar, geri çekme ya da birleştirme sonucunu kaydetmesi gerektiğinde kullan.
argument-hint: "[slug]"
---

# /dosya-kapatma

1. Aşağıdaki iş akışını ve referansı uygula.
2. Slug'ı ve mevcut durumu teyit et.
3. Sonucu yakala: çözüm türü (sulh, ret, lehimize karar, aleyhimize karar, geri çekme, birleştirme), tarih, nihai maruziyet/maliyet, dersler.
4. `_log.yaml`'ı güncelle: `durum: kapandi`, `kapanma: YYYY-AA-GG` ve `sonuc:` alanları ekle.
5. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` dosyasına son kayıt ekle.
6. Dosya `_log.yaml`'da ve `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/`'da kalır — silinmez. `/portfoy-durumu` onu aktif özetlerden filtreler.

---

# Dosya Kapatma

## Amaç

Dosyalar sona erer. Sonuç, portföyün ürettiği tek en değerli veri noktasıdır — gelecekteki dosyalar için risk çerçevesini kalibre eder. Bir dosyayı kapatmak, kaydın salt arşiv değil yararlı olması için sonucu yapısal olarak yakalar.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` — satırı bul
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` — referans (intake bağlamı)
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` — ekleme hedefi

**Çatışma kapısı — atlanamaz.** Kapatmadan önce dosya slug'ını `_log.yaml`'da kontrol et. Dosya `_log.yaml`'da yoksa reddet ve yönlendir:

> "[dosya slug'ı]'nı dosya günlüğünde göremiyorum. Kapatılacak bir şey yok — ya slug yanlış ya da dosya hiç `/dava-takibi:dosya-acilis` yoluyla intake yapılmamış. Önce slug'ı kontrol et; gerçekten hiç intake yapılmadıysa, güncellenecek satır ve kapatılacak dosya yapısı yok."

## Girdi

Slug (zorunlu).

## Kapatma

### 1. Çözüm Türü

- `sulh` — karşı tarafla, para tutarı, yapısal koşullar
- `ret` — kesin veya kesin olmayan, hangi mekanizmayla
- `lehimize-karar` — hangi aşamada, temyiz maruziyeti
- `aleyhimize-karar` — hangi aşamada, temyiz durumu, kristalize maruziyet
- `geri-cekme` — karşı tarafça, koşullar
- `birlestirme` — başka bir dosyayla birleştirildi (ana dosyanın slug'ını ver)
- `diger` — açıklamayla

### 2. Çözüm Tarihi

Davanın gerçekten sona erdiği tarih (sulh imzalandı, karar çıktı, geri çekme dilekçesi verildi).

### 3. Nihai Maruziyet

- Şirkete gerçek maliyet (sulh tutarı + avukatlık ücretleri + ihtiyati tedbir/yapısal maliyet)
- Intake'teki ilk maruziyet aralığına karşı (beklentimiz doğru çıktı mı?)
- Karşılık doğruluğu (karşılık ayrıldıysa): ayrılan vs. gerçek

### 4. Dersler

İki veya üç cümle. Neyi doğru yaptık? Neyi yanlış değerlendirdik? İntakede daha erken işaretlenmesi gereken bir şey var mıydı?

Bu, gelecekteki avukatın yeniden okuyacağı kısım. Dürüst olun. "Olasılığı yanlış değerlendirdik — karşı taraf beklentiden agresif davrandı" "lehimize sonuçlandı"dan çok daha değerlidir.

### 5. Tohum Belge Sorusu

Sulh sözleşmesi, nihai karar, geri çekme dilekçesi — varsa yol. Zorunlu değil.

## Yazım

**Dosyayı kapatmadan önce (sonuç doğuran eylem — dosya arşivlenir ve aktif takip sona erer):** `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'deki `## Bunu Kim Kullanıyor` bölümünü oku. Rol Avukat değilse:

> Bir dosyayı kapatmak hukuki sonuçlar doğurur — aktif takibi sona erdirir, ilgili delil saklama bildirimini etkileyebilir (uygunsa ayrıca `/dava-takibi:delil-saklama --serbest-birak` çalıştırın), ve şirketin güveneceği nihai kaydı oluşturur. Bunu bir avukatla gözden geçirdiniz mi? Evet ise devam edin. Hayır ise, onlara götürmek için kısa bir özet:
>
> [1 sayfalık özet üret: dava, çözüm türü ve koşullar, nihai maruziyet vs. ilk, karşılık doğruluğu, hâlâ aktif olan ilgili dosyalar veya temyizler, erken kapatmanın yanlış gitebilecekleri, avukata sorulacaklar.]
>
> Yargı çevrenizde lisanslı bir avukat bulmak için: Türkiye Barolar Birliği veya ilgili baronun yönlendirme hizmeti en hızlı başlangıç noktasıdır.

Açık bir "evet" olmadan kapatma alanlarını yazma veya kapatma kaydını ekleme.

### `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` Güncelle

```yaml
durum: kapandi
kapanma: [YYYY-AA-GG]
sonuc: [cozum-turu]
nihai_maliyet: [para tutarı]
son_guncelleme: [bugün]   # kapatma son dokunuştur; kaydet
```

Mevcut tüm alanları koru. Satırı silme.

### `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` Dosyasına Son Kayıt Ekle

```markdown
## [YYYY-AA-GG] — Dosya Kapatıldı: [cozum-turu]

**Çözüm:** [anlatı — ne oldu, hangi koşullarda]
**Nihai maliyet:** [tutar + varsa yapısal koşullar]
**İlk maruziyete karşı:** [matter.md intake aralığıyla karşılaştır]
**Karşılık doğruluğu:** [uygulanabiliyorsa]

**Dersler:**
[2-3 cümle — dürüst retrospektif]

**İlgili belge:** [sulh sözleşmesi / nihai karar / vb., sağlandıysa]
```

### `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` Dosyasına Dokunuş

Sonuna kapatma bloğu ekle (önceki bölümleri değiştirme — bunlar tarihi intake'tir):

```markdown
---

## Kapatıldı [YYYY-AA-GG]

[Tek paragraf çözüm özeti. Ayrıntı için nihai geçmiş kaydına işaretçi.]
```

## Teyit Et

Yazmadan önce kullanıcıya tam kapatma kaydını ve yaml değişikliklerini göster.

## Bu Skill'in Yapmadıkları

- Dosyaları silmek. Kapatılan dosyalar `_log.yaml`'da ve diskte kalır — portföy yargısının eğitim setidir.
- Yeniden açmak. Kapatılan bir dosya geri gelirse (temyiz, ilgili dava), kapatılana `matter.md`'de atıfta bulunan yeni bir dosya aç.
- Kullanıcının söylemediği dersleri özetlemek. Kullanıcı dersler bölümünü atlarsa, icat etmek yerine boş bırak.