---
name: dosya-guncelleme
description: Dosyanın geçmiş dosyasına tarihli olay ekler ve log satırını günceller — yeni gelişmeler, durum değişiklikleri, risk yeniden değerlendirmeleri, son tarih kaymaları ve sulh yetkisi değişikliklerini yakalar. Kullanıcı bir dosya güncellemesi kaydetmek, bir gelişmeyi not etmek veya portföye karşı durum değişikliği kaydetmek istediğinde kullan.
argument-hint: "[slug] [kısa olay açıklaması]"
---

# /dosya-guncelleme

1. Aşağıdaki iş akışını ve referansı uygula.
2. Slug'ın `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/` ve `_log.yaml`'da olduğunu teyit et.
3. Olay türü, tarih (varsayılan bugün), özet ve log alan güncellemelerini sor (risk değişikliği, durum değişikliği, sonraki son tarih kayması, önemlilik yeniden sınıflandırması).
4. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` dosyasına tarihli kayıt ekle.
5. `_log.yaml`'ı güncelle — `son_guncelleme`'yi bugüne ayarla, alan güncellemelerini uygula.
6. Teyit et.

---

# Dosya Güncelleme

## Amaç

Portföy ancak güncel kalırsa yararlı kalır. Bu skill bir güncellemeyi kaydetmeyi ucuz hale getirir — iki dakika yapılandırılmış yakalama, serbest biçim savrulması yok.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` — satırı bul
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` — ekleme hedefi
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` — referans (yeniden yazma)
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` — risk kalibrasyonu (risk yeniden değerlendiriyorsa)

**Çatışma kapısı — atlanamaz.** Güncellemeyi kaydetmeden önce dosya slug'ını `_log.yaml`'da kontrol et. Dosya `_log.yaml`'da yoksa reddet ve yönlendir:

> "[dosya slug'ı]'nı dosya günlüğünde göremiyorum. Önce `/dava-takibi:dosya-acilis` çalıştır; böylece çatışma taraması yapılır ve dosya çalışma alanı kurulur. Yönetilmeyen bir dosyaya geçmiş eklemem — çatışma taraması kapıdır ve dosya intake yapılana kadar eklenecek `history.md` yok."

## Girdi

Slug (zorunlu). Sağlanmamışsa sor — seçilebilecek kısa son güncellenen dosyalar listesiyle.

## Güncelleme

### 1. Olay Türü

Kategoriler sun:

- **Usul** — dilekçe verildi/alındı, karar çıktı, duruşma yapıldı, son tarih belirlendi
- **Delil/Belge** — belge üretimi yapıldı/alındı, bilirkişi atandı, celp tebliğ edildi
  *(Not: Türk usul hukukunda (HMK/CMK) ABD tarzı discovery/deposition sistemi yoktur. Delil ikamesi mahkeme eliyle yürür. Bu kategori Türk yargısına özgü belge süreçlerini kapsar.)*
- **Esasa İlişkin** — yeni olgular, kilit belge ortaya çıktı, esasa ilişkin karar
- **Strateji** — duruş değişikliği, sulh teklifi yapıldı/alındı, yetki güncellemesi
- **Risk Yeniden Değerlendirme** — şiddet veya olasılık değişti
- **Paydaş** — yeni kişi dahil edildi, dış avukat değişikliği
- **İdari** — vekaletname imzalandı, bütçe ayarlandı, saklama tazeletildi

Hiçbiri uymuyorsa serbest biçim.

### 2. Tarih

Varsayılan bugün. Geçersizleme kabul et (ör. geçen haftaki bir olayı kaydediyorsa).

### 3. Özet

Tek paragraf anlatı. Ne oldu, ne anlama geliyor, varsa anlık sonuç.

### 4. Log Alan Değişiklikleri

Potansiyel olarak etkilenen alanlarda yürü:

- `durum:` — aşama değişti mi (ör. dilekce → tahkikat)?
- `asama:` — alt aşama güncellemesi
- `risk:` — yeniden değerlendirme gerekiyor mu?
- `onemlilik:` — değişiklik var mı (yeni olgular karşılık veya açıklama tetikleyebilir mi)?
- `maruziyet_araligi:` — yeni bilgi varsa revize et
- `sonraki_son_tarih:` — varsa yeni yaklaşan tarih
- `dis_avukat:` — değişiklik?
- `ic_sahipler:` — yeni veya çıkarılan var mı?
- `delil_saklama:` — tazeletildi, genişletildi, serbest bırakıldı?

Yalnızca olay türünden etkilenmesi muhtemel alanlar için sor. Usul güncellemeleri genellikle yalnızca `asama` ve `sonraki_son_tarih`'i etkiler; bir sulh teklifi `onemlilik`, `maruziyet_araligi`, `durum`'u etkileyebilir.

### 4ön. Sulh Kabulü Kapısı

Strateji güncellemesi bir **sulh kabulüyse** (şirket bir sulh teklifini kabul ediyor, sulh sözleşmesini imzalıyor veya prensipte kabulü yetkilendiriyorsa — yalnızca yapılan veya alınan teklifi kaydetmiyorsa): `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'deki `## Bunu Kim Kullanıyor` bölümünü oku. Rol Avukat değilse:

> Sulh kabulünün hukuki sonuçları vardır — talepleri çözer, genellikle ibraname gerektirir ve sigorta, vergi ve ilgili konuları etkileyebilir. Bunu bir avukatla gözden geçirdiniz mi? Evet ise devam edin. Hayır ise, onlara götürmek için kısa bir özet:
>
> [1 sayfalık özet üret: dava, önerilen sulh koşulları (tutar, yapısal, ibraname kapsamı, gizlilik, olumsuz yorum yasağı), risk altındaki maruziyet, yetki merdiveni durumu (bkz. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` sulh yetkisi), yanlış gidebilecekler, kabul etmeden önce avukata sorulacaklar.]
>
> Yargı çevrenizde lisanslı bir avukat, noterlik hizmetleri veya hukuki danışmanlık bulmak için: Türkiye Barolar Birliği veya ilgili baronun yönlendirme hizmeti en hızlı başlangıç noktasıdır.

Açık bir "evet" olmadan kabulü kaydetme veya kabul esasında önemliliği değiştirme. Teklifleri veya karşı teklifleri kaydetmek kapıyı gerektirmez — kabul gerektirir.

### 4a. Önemlilik Tetikleyici — Açık Soru

Belirli olay türleri bir önemlilik yeniden kontrolünü zorlar. Olay türü bu listededeyse, **her zaman sor** — kullanıcının açık bir cevap vermeden devam etmesine izin verme:

| Olay türü | Önemlilik tetikleyici sorusu |
|---|---|
| Esasa ilişkin (yeni olgular, kilit belge, esasa ilişkin karar) | "Bu olay esasa ilişkin. `önemlilik`'i etkiler mi? Mevcut: `[mevcut]`. Seçenekler: `karsilik / aciklandi / izleniyor / yok`. Değişiklik?" |
| Strateji (duruş değişikliği, sulh teklifi yapıldı veya alındı) | "Sulh faaliyeti genellikle önemlilik yeniden sınıflandırmasını tetikler. Mevcut: `[mevcut]`. Teklif, karşı teklif veya kabul maruziyeti değiştiriyorsa veya tartışmalı'dan muhtemel-ve-tahmin-edilebilir'e geçiyorsa yeniden sınıflandır." |
| Risk yeniden değerlendirme (şiddet veya olasılık değişti) | "Risk değişti. Önemlilik takip etmeli. Mevcut: `[mevcut]`. Yeniden sınıflandır?" |
| Düzenleyici / icra gelişmesi | "Düzenleyici işlem (celp, inceleme, icra bildirimi) genellikle açıklama analizini tetikler. Mevcut: `[mevcut]`. Değişiklik?" |

Kabul edilebilir yanıtlar `değişiklik yok`'u içerir — ama `değişiklik yok` açık olmalı, sessizlikle ima edilmemeli. Geçmiş kaydında şunu yakala:

```markdown
**Önemlilik kontrolü:** [değişiklik yok / X'ten Y'ye değişti]
**Gerekçe:** [bir cümle]
```

Önemlilik `karsilik` veya `aciklandi`'ya geçiyorsa ve dosya önceden karşılık veya açıklama taşımıyorsa, olayı `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` önemlilik eşiklerine göre mali işler / denetim komitesi bildirimi gerektiriyor olarak işaretle.

### 5. Tohum Belge Sorusu (İsteğe Bağlı)

Güncelleme bir belgeye (karar, dilekçe, yazışma) atıfta bulunuyorsa, bağlanacak bir yol olup olmadığını sor. Baskı yapma.

## Yazım

### `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` Dosyasına Ekle

En yenisi en üstte, başlığın ardındaki `---`'ın hemen altında.

```markdown
## [YYYY-AA-GG] — [Olay türü]: [kısa başlık]

[Paragraf özeti.]

**Değiştirilen alanlar:**
- [alan]: [eski → yeni]
- [alan]: [eski → yeni]

**İlgili belge:** [yol, sağlandıysa]
```

Alan değişmemişse "Değiştirilen alanlar" bloğunu atla.

### `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` Güncelle

- Alan değişikliklerini uygula.
- `son_guncelleme: [bugün]` ayarla (veya kullanıcı geçersiz kıldıysa olay tarihi — log kaydın en son ne zaman dokunulduğunu izler).

## Teyit Et

Yazmadan önce kullanıcıya geçmiş kaydını ve yaml farkını göster:

> İşte ekleyeceğim ve güncelleyeceğim. Taahhüt edilsin mi?

## Bu Skill'in Yapmadıkları

- Geçmiş kayıtları düzenlemek. Düzeltmeler önceki kayıtlara atıfta bulunup düzelten yeni kayıtlardır.
- Günlüğü sessizce değiştirmek. Her alan değişikliği yazılmadan önce kullanıcıya gösterilir.
- Yeni gelişmenin karşılık/açıklama gerektirip gerektirmediğine karar vermek. Soruyu yüzeye çıkarır ("bu önemliliği itebilir — yeniden sınıflandır?"), kullanıcı yanıtlar.