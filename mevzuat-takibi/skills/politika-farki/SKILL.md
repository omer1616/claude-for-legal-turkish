---
name: politika-farki
description: Belirli bir mevzuat değişikliğini indekslenmiş politika kütüphanesiyle karşılaştırın (diff). Mevzuat değiştiğinde ve neleri etkilediğini bulmak gerektiğinde kullanın.
argument-hint: "[mevzuat adı, veya metin/özeti yapıştırın]"
---

# /politika-farki

1. `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` yükle → politika kütüphanesi indeksi.
2. İş akışını uygulayın.
3. Mevzuattaki yeni gereksinimleri çıkarın ve politikalara eşleştirin.
4. Çıktı: gereksinim bazında boşluk analizi ve değişim ihtiyacı.

## Kapsam Bütünlüğü
Eğer kullanıcı bir bölümü hariç tutmanızı isterse, bunu en üste büyük harflerle `⚠️ KAPSAM SINIRLAMASI` olarak ekleyin ve eksik kısımları aramayın.

## İş Akışı

### Adım 0: Karşılaştırmadan önce Kuralın Durumunu Doğrula
Eğer mevzuat yürürlükte değilse (iptal edilmişse, ertelenmişse vb.), bunu bir araştırma aracı (örn. mevzuat.gov.tr, Anayasa Mahkemesi iptal kararları) üzerinden teyit edin. Doğrulayamazsanız başa uyarı ekleyin: `⚠️ KURAL DURUMU DOĞRULANAMADI`

### Adım 1: Yeni gereksinimleri çıkar
Web araştırması veya metin içerisinden gereksinimleri madde madde çıkarın:
| # | Gereksinim | Yürürlük | Atıf |
|---|---|---|---|
| 1 | [Ne gerektiriyor] | [tarih] | [madde] |

### Adım 2: Politikalarla Eşleştir
Her bir gereksinim için: Doğrudan eşleşme, dolaylı eşleşme veya eşleşme yok.

### Adım 3: Karşılaştırma (Diff)
Eşleşenler için:
- **Yeni kural ne diyor:**
- **Politikamız ne diyor:**
- **Boşluk:** Yok / Kısmi / Tam
- **Değişim ihtiyacı:** [spesifik detay]
- **Politika sahibi:** [kişi]

### Adım 4: Eşleşmeyenler
Eğer hiçbir politika karşılamıyorsa, "Yeni politika gerekli" olarak listeleyin.

## El Değiştirme (Handoff)
bosluk-cikarici (gap-surfacer): Kısmi veya Tam boşluklar, sahip ve son tarih ile izlenen bir öğe haline gelir.
