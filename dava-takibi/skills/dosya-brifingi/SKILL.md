---
name: dosya-brifingi
description: Tek bir dosya hakkında derinlemesine brifing — mevcut duruş, değişenler, sonraki son tarih, açık sorular ve risk yeniden değerlendirme kontrolü; BHM güncellemesi veya dış avukat görüşmesinden önce hazır. Kullanıcı "[dosya] hakkında brifing ver", "[dosya] nerede" veya belirli bir dosya hakkında bilgi almak istediğinde kullan.
argument-hint: "[slug]"
---

# /dosya-brifingi

1. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` yükle → risk kalibrasyonu + ilgili paydaşlar.
2. Aşağıdaki iş akışını ve referansı uygula.
3. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` + `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` + `_log.yaml`'daki log satırını oku.
4. Brifing üret: mevcut duruş, son güncellemeden bu yana değişenler, sonraki son tarih, açık sorular, risk yeniden değerlendirme kontrolü ("`risk:` alanı hâlâ gerçeği yansıtıyor mu?").
5. Eskime işareti: `son_guncelleme` > 30 gün ise belirt.

---

# Dosya Brifingi

## Amaç

Avukata toplantı odasına yürüme süresi kadar kısa sürede tek bir dosya hakkında net bir okuma sun. Mevcut duruş, değişenler, sıradaki, yeniden düşünülmesi gerekenler.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` — yapılandırılmış satır
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` — anlatı intake
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` — olay kaydı
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` — risk kalibrasyonu ("risk: yüksek"in genel değil belirli bir anlama gelmesi için)

**Çatışma kapısı — atlanamaz.** Brifingden önce dosya slug'ını `_log.yaml`'da kontrol et. Dosya `_log.yaml`'da yoksa reddet ve yönlendir:

> "[dosya slug'ı]'nı dosya günlüğünde göremiyorum. Önce `/dava-takibi:dosya-acilis` çalıştır; böylece çatışma taraması yapılır ve dosya çalışma alanı kurulur. Intake yapılmamış bir dosya için brifing oluşturmam — çatışma taraması kapıdır."

## Girdi

Slug (zorunlu). Belirsiz veya eksikse, kullanıcıdan aktif dosyalar listesinden seçmesini iste.

## Brifing

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar — role göre farklılaşır; bkz. `## Bunu Kim Kullanıyor`]

# [Dosya Adı] — [bugün]'e Kadar Brifing

**Durum:** [durum / aşama]
**Risk:** [puan] ([şiddet] × [olasılık])
**Önemlilik:** [kategori]
**Dış avukat:** [büro — sorumlu]
**Son güncelleme:** [tarih] [>30 günse ⚠️ ESKİMİŞ işareti]
**Çatışma:** [durum — `beklemede` veya `yapilmadi` ise ⚠️ işareti]

---

## Tek Paragraf Özet

[Mevcut duruş. Ne yapıyoruz ve neden. Kaydedilmişse pivot olguyu adlandır.]

## Son Zamanlarda Değişenler

[history.md'den son 3-5 kayıt, en yenisi önce. Geçmiş zayıfsa belirt.]

## Sıradaki

- **Yakın son tarih:** [sonraki_son_tarih + ne olduğu]
- **Yaklaşan kilometre taşları:** [matter.md'de veya son geçmişte tarihlenmiş her şey]
- **Bekleyen kararlar:** [matter.md'de işaretlenmiş açık sorular]

## Maruziyet

[Aralık + intake'ten bu yana değişiklik. Karşılık ayrıldıysa, mevcut karşılık + yeniden kalibrasyon vakti geçti mi?]

## İç Sahipler

[Kim dahil; dahil edilmesi gereken ama edilmeyen var mı]

## Risk Yeniden Değerlendirme Kontrolü

*Bir soru, yanıt değil.*

- `risk: [puan]` hâlâ doğru mu, yoksa dava mı değişti?
- `onemlilik: [kategori]` hâlâ uyuyor mu? (Yeni olgular karşılık veya açıklama gerektirmeye itebilir mi?)
- Dosyanın artık ihtiyaç duyduğu yeni bir paydaş var mı (ör. delil toplamayla ilgili bir gelişmeden sonra BİLGİ GÜVENLİĞİ devreye giriyor)?

## Açık Sorular

[matter.md'den ve geçmişte çözülmemiş her şey]

## Görüşme İçin

[Kullanıcı bir amaç belirttiyse — "dış avukatla görüşmeden önce brifing ver" — son bölümü buna göre uyarla: sorulacak sorular, alınacak kararlar, çekilecek güncellemeler. Amaç belirtilmemişse bu bölümü atla.]
```

## Eskime

`son_guncelleme > 30 gün önce` ise: başlıkta işaretle VE görüşmede tartışılanları kaydetmek için ardından `/dava-takibi:dosya-guncelleme [slug]` çalıştırmayı öner.

## Ton

Bu pazarlama değil. Bilineni söyle; bilinmeyeni işaretle. Bir dosyanın geçmişi zayıfsa ve yeni açıldıysa, brifing kısa olur — bu doğrudur. Doldurmayın.

## Sonraki Adımlar Karar Ağacıyla Kapat

CLAUDE.md `## Çıktılar` bölümüne göre sonraki adımlar karar ağacıyla kapat. Bu skill'in ürettiğine seçenekleri uyarla — beş varsayılan dal (X'i taslakla, eskale et, daha fazla olgu topla, izle ve bekle, başka bir şey) başlangıç noktasıdır, zorunluluk değil. Ağaç çıktının kendisidir; avukat seçer.

## Bu Skill'in Yapmadıkları

- Sonuçları tahmin etmek. Risk puanı yakalanan bir yargıdır, tahmin değil.
- Strateji tavsiye etmek. Soruları yüzeye çıkarır; avukat cevaplar.
- Yeniden triyaj yapmak. Kullanıcı yeniden triyaj istiyorsa, bu alan değişikliklerini içeren `/dosya-guncelleme` — bu skill okur, yazmaz.