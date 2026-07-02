---
name: sozlesme-inceleme
description: >
  Bir satıcı sözleşmesini, NDA'yı veya SaaS aboneliğini oyun kitabınıza karşı
  inceleyin. Sözleşme yapısını başlıklardan tespit eder, doğru inceleme skill'ine
  (satici-inceleme, gizlilik-inceleme, saas-inceleme) yönlendirir ve çıktıyı tek bir
  notta bütünleştirir. Kullanıcı "bu sözleşmeyi incele", "bu MSA'yı kontrol et", "bu
  NDA uygun mu", "bu SaaS sözleşmesine bak" dediğinde veya incelenmek üzere gelen bir
  sözleşme eklediğinde kullan.
argument-hint: '[dosya yolu | Drive bağlantısı | [CLM kimliği] | metin yapıştır]'
---

# /sozlesme-inceleme

Gelen bir sözleşmeyi
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
içindeki oyun kitabına karşı inceler. Sözleşme yapısını başlıklardan tespit eder,
uygun skill(ler)i seçer ve — confirm_routing etkinse — devam etmeden önce
kullanıcıyla kontrol eder.

## Talimatlar

1. **`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
   dosyasını yükle.** Yer tutucular varsa dur ve iste: "Önce `/ticari-hukuk:ilk-kurulum`
   çalıştırın — oyun kitabınıza karşı inceleyebilmem için önce onu öğrenmem gerekiyor."

   Ayrıca
   `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` →
   `## İnceleme tercihleri` → `confirm_routing`'i oku. Alan yoksa `true` say.

2. **Sözleşmeyi al:** Dosya yolundan, Drive bağlantısından, [CLM kimliği]nden veya
   yapıştırılmış metinden. Hiçbiri verilmediyse sor.

3. **Belge yapısını oku — önce başlıklar.**

   Gövdeyi okumadan önce şunu çıkar:
   - Ana sözleşme başlığı (ör. "Ana Hizmet Sözleşmesi", "Gizlilik Sözleşmesi (NDA)")
   - Tüm ek (exhibit), cetvel (schedule), zeyilname ve ek belge başlıkları (ör. "Ek A —
     Veri İşleme Sözleşmesi", "Cetvel 1 — Abonelik Sipariş Formu", "Ek B — Hizmet
     Seviyesi Sözleşmesi")

   Bu yönlendirme sinyalidir. Yalnızca gövde anahtar kelimelerine güvenme — baştan
   sona "gizli" geçen 40 sayfalık bir MSA bir NDA değildir.

4. **Belge yapısına göre skill(ler)i seç.**

   Her tanımlanan belgeyi veya bölümü bir skill'e eşle:

   | Belge / bölüm başlığı şunu içeriyor | Skill |
   |---|---|
   | Gizlilik Sözleşmesi, NDA, Gizlilik Anlaşması (*ana* sözleşme olarak) | **gizlilik-inceleme** |
   | Ana Hizmet Sözleşmesi (MSA), Profesyonel Hizmetler, İş Tanımı (SOW), Danışmanlık Sözleşmesi | **satici-inceleme** |
   | Abonelik, SaaS, Bulut Hizmetleri, otomatik yenilemeli Sipariş Formu, tekrarlayan ücretli Yazılım Lisansı | **saas-inceleme** (satici-inceleme üzerine katman) |
   | Veri İşleme Sözleşmesi (VİS), DPA (ek veya bağımsız olarak) | **satici-inceleme** için not → veri koruma bölümü |
   | Hizmet Seviyesi Sözleşmesi, SLA (ek olarak) | **saas-inceleme** için not → SLA bölümü |

   Birden fazla skill geçerli olabilir. Yaygın kombinasyonlar:
   - MSA + VİS eki → satici-inceleme, VİS notuyla
   - SaaS aboneliği + Sipariş Formu + SLA eki → saas-inceleme (üçünü de kapsar)
   - MSA + otomatik yenilemeli Sipariş Formu → satici-inceleme + saas-inceleme katmanı

   Yapı başlıkları okuduktan sonra gerçekten belirsizse (ör. eki listelenmemiş
   "Sözleşme" başlıklı bir belge), belirsizliği çözmek için gövdenin ilk iki
   sayfasını oku — sonra dur ve yönlendir.

5. **Etkinse yönlendirmeyi onayla.**

   `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
   içinde `confirm_routing` `true` ise (veya alan yoksa):

   ```
   Bunu şu şekilde inceleyeceğim: [sözleşme türü/leri].

   Tanımlanan belgeler:
   - [Ana sözleşme başlığı] → [skill]
   - [Ek A başlığı] → [nasıl ele alınacağı]
   - [Ek B başlığı] → [nasıl ele alınacağı]

   Doğru mu? (evet / hayır — ya da neyi yanlış anladığımı söyle)
   ```

   Devam etmeden önce teyidi bekle. Kullanıcı yönlendirmeyi düzeltirse, talimatını
   uygula ve devam et.

   `confirm_routing` `false` ise: sessizce devam et. Yönlendirme kararını inceleme
   notunun en üstüne kaydet, böylece kullanıcı neyin uygulandığını görebilir.

6. **Skill(ler)i çalıştır.** Her skill'in iş akışını tam olarak takip et. Birden fazla
   skill geçerliyse, sırayla çalıştır ve çıktıyı tek bir notta bütünleştir — ayrı
   notlar üretme.

7. **Eskalasyonları kontrol et:** Herhangi bir sorun,
   `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
   matrisine göre inceleyenin yetkisini aşıyorsa, yönlendirmek ve talebi taslaklamak
   için **eskalasyon-isaretleyici**'yi çağır.

8. **Devam adımları öner:**
   - İş birimi sahibi için paydaş özeti
   - İzlenen değişikliklerle bir redline .docx
   - CLM kaydı oluşturma (bağlıysa)
   - Otomatik yenileme bulunduysa yenileme kaydına ekleme

## confirm_routing'i yapılandırma

`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` →
`## İnceleme tercihleri`'ne ekle:

```markdown
## İnceleme tercihleri

confirm_routing: true   # Yönlendirme onayını atlayıp otomatik devam etmek için false yap
```

İlk-kurulum görüşmesi bu tercihi sormalıdır. Varsayılan `true`'dur — onay açık.
Güven arttıkça kullanıcı `false` yapabilir.

## Örnekler

```
/ticari-hukuk:sozlesme-inceleme satici-msa.pdf
```

```
/ticari-hukuk:sozlesme-inceleme https://drive.google.com/file/d/ABC123
```

```
/ticari-hukuk:sozlesme-inceleme
[sözleşme metnini yapıştır]
```

## Çıktı

Skill'in formatına göre tam inceleme notu. Yönlendirme kararı en üstte kaydedilmiş.
Sapma-sapma, spesifik redline dili, adlandırılmış onaylayıcı. Nereye kaydedileceği
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md` → Ev
tarzının "iş ürünü nereye gider" dediği yerdir.
