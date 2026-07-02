---
name: portfoy
description: >
  Fikri Mülkiyet (FM) portföyünü takip edin — tesciller, yenilemeler, yıllık sicil ücretleri 
  (maintenance fees) ve kullanım kanıtları. Yaklaşan yenilemeleri kontrol etmek, 
  yeni bir varlık eklemek, bir ödemeyi kaydetmek veya sicili boşluklar/düşmeler açısından 
  denetlemek için kullanın.
argument-hint: "[--report [--days N] | --add | --update | --audit]"
---

# /portfoy

Yaklaşan yenilemeleri gösterir, varlık ekler, ödemeleri kaydeder ve sicili denetler.

## Talimatlar

1. **Aşağıdaki iş akışını izleyin** ve `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/portfolio.yaml` dosyasını okuyun.
2. **Varsayılan (parametre yok):** `--report` ile aynıdır. Önümüzdeki 90 gün içindeki son tarihleri aciliyetlerine göre (🔴 düşmüş/hoşgörü süresi, ⏰ yaklaşıyor, 🟡 gelecek, vb.) gösterir.
3. **`--report [--days N]`:** Belirtilen gün (ör. 30/60/90) içindeki vadeleri gösterir.
4. **`--add`:** Etkileşimli olarak yeni bir varlık ekler (TÜRKPATENT, WIPO vb.).
5. **`--update`:** Bir ödemenin yapıldığını veya statünün değiştiğini kaydeder. Avukat onayı teyidi (consequential-action gate) yapmadan statüyü `filed` yapmayın.
6. **`--audit`:** Genel portföy sağlığı denetimi. (Kullanılmayan markalar, 18 aydır bekleyen başvurular vb.)

## Örnekler

```
/fikri-mulkiyet:portfoy
/fikri-mulkiyet:portfoy --report --days 180
/fikri-mulkiyet:portfoy --add
```

---

## Önemli: Süre/Tarih Uyarı Notu

> Bu yeteneğin hesapladığı son tarihler tamamen referans amaçlıdır. TÜRKPATENT, WIPO, EUIPO veya ilgili ofislerin kuralları, harçları ve hoşgörü (grace) süreleri değişebilir. **Hesaplanan tarihleri işlem yapmadan önce MUTLAKA TÜRKPATENT EPATAS / WIPO Madrid Monitor vb. resmi sicillerden veya kendi IP yönetim sisteminizden teyit edin.** Yanlış kaydedilmiş bir son tarih, kaydedilmemiş olandan daha tehlikelidir.

## Türkiye (TÜRKPATENT) ve Küresel Kural Varsayımları

Varlık türüne ve yargı çevresine göre yenileme mekanikleri:

- **Türkiye (TÜRKPATENT) Marka:** Başvuru tarihinden itibaren **10 yılda bir yenilenir** (SMK m. 23). Vadeden itibaren 6 aylık ek (cezalı) hoşgörü süresi vardır. Marka tescilden itibaren 5 yıl içinde ciddi biçimde kullanılmazsa, iptal talebiyle (SMK m. 9) karşılaşabilir (Kullanım ispatı gerekliliği ABD'deki gibi 5-6. yılda resen beyan -§8- olarak değil, iptal talebi geldiğinde savunma/kanıtlama olarak çalışır).
- **Türkiye (TÜRKPATENT) Patent:** Başvuru tarihinden itibaren 3. yıldan başlayarak **HER YIL** yıllık sicil ücreti ödenir (SMK m. 101). Vadesinde ödenmezse 6 aylık ek süre içinde cezalı ödenebilir. Ödenmezse hak düşer (telafi/mücbir sebep istisnaları hariç).
- **Türkiye (TÜRKPATENT) Tasarım:** Başvuru tarihinden itibaren 5 yılda bir yenilenir, toplam koruma süresi 25 yıldır (SMK m. 69).
- **WIPO Madrid Marka:** 10 yıllık periyotlarla WIPO üzerinden yenilenir.
- **Avrupa (EPO) Patent:** Başvuru tarihinden itibaren her yıl yıllık ücret ödenir (ulusal aşamalara geçince ilgili ulusal ofis kuralları geçerlidir).
- **ABD (USPTO):** Markalar için 5-6. yıl §8 kullanım beyanı ve 10 yılda bir yenileme. Patentler için 3.5, 7.5, 11.5. yıllarda bakım harçları.

*Eğer farklı bir ofis/kural varsa `custom_rules` olarak yaml içine ekleyin ve `agent_managed: true` (vekil tarafından yönetiliyor) olarak işaretleyin.*

---

## Sicil Yapısı (portfolio.yaml)

Dosya `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/portfolio.yaml` konumundadır. (Bkz. orijinal SKILL.md formatı).

Status (Durum) değerleri: `upcoming` (90 günden uzak), `due_soon` (90 gün içinde), `overdue` (vadesi geçmiş ama hoşgörü süresinde), `grace` (hoşgörü süresinde - cezalı ödeme), `lapsed` (düşmüş/hakkı yitirilmiş), `filed` (ödendi/tamamlandı).

---

## Mod 1: İlk Kurulum (Initialise)
Dosya yoksa kullanıcıya tek tek sorarak veya sistemden çekerek (varsa) oluşturun. `next_deadlines` kısmını TÜRKPATENT/WIPO/USPTO kurallarına göre hesaplayın. (Ör: TÜRKPATENT Patent için her yılın başvuru ay/gününde yıllık ücret hesapla).

## Mod 2: Raporlama (--report)
Tüm varlıkların son tarihlerini güncelleyip 90 (veya N) gün içindeki vadeleri aciliyet sırasına göre listeleyin:
- 🔴 DÜŞMÜŞ / HOŞGÖRÜ SÜRESİNDE (Cezalı)
- ⏰ [N] GÜN İÇİNDE YAKLAŞANLAR
- 🟡 GELECEKTEKİLER
- 🌐 VEKİL TARAFINDAN YÖNETİLENLER (Agent-managed)
- ❓ BİLİNMEYENLER (Tarihi eksik olanlar)

## Mod 3: Ekleme (--add)
Kullanıcıdan Marka/Patent/Tasarım, TÜRKPATENT/Diğer, Başvuru Tarihi, Belge No, Sınıflar, Mal sahibi gibi verileri isteyip YAML'a ekleyin ve yaklaşan tarihi otomatik hesaplayın.

## Mod 4: Güncelleme (--update)
**Onay Kapısı (Consequential-action gate):** Kullanıcı bir yenilemeyi veya harcı "ödendi/yapıldı" olarak işaretlemek isterse, *"Bunu TÜRKPATENT EPATAS / WIPO veya ilgili sicil üzerinden ya da vekilinizden bizzat teyit ettiniz mi? Buradaki yanlış bir 'ödendi' işareti, sürenin kaçırılıp hakkın düşmesine sebep olabilir."* diye sorun. Evet derse `status: filed` yapın ve bir sonraki dönemin vadesini hesaplayın.

## Mod 5: Denetim (--audit)
Portföy genel sağlığını denetleyin:
- Hoşgörü süresindeki veya düşmüş haklar.
- Uzun süredir "beklemede" (pending) olan başvurular (Ör: TÜRKPATENT'te 18 ayı geçmiş marka başvurusu).
- Tescilden itibaren 5 yılı doldurmuş ama aktif kullanılıp kullanılmadığı bilinmeyen markalar (SMK m. 9 iptal riski).
- Yakın zamanda süresi dolacak 20 yıllık patentler.
- İzlemeye (watch list) alınmamış tescilli markalar.

## Çıktı Formatı
Tüm çıktılarda `CLAUDE.md` içindeki Rol başlığını ekleyin ve **"Resmi sicilden teyit ediniz"** uyarısı ile bitirin. Veri çoksa tablo formatında özet gösterin.
