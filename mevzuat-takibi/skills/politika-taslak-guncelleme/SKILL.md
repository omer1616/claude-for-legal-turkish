---
name: politika-taslak-guncelleme
description: bosluk-analizi (gaps) veya politika-farki (policy-diff) tarafından bulunan bir boşluğu kapatan, işaretli (marked-up) bir politika taslağı (önerisi) üretir. Bu, iç inceleme için bir ilk taslaktır — doğrudan onaylı politika belgelerine uygulanmaz. Kullanıcı "politikayı yeniden yaz", "düzeltmeyi taslakla" dediğinde veya bosluk-cikarici taslak hazırlamak için devrettiğinde kullanın.
argument-hint: "[GAP-ID veya boşluk açıklaması]"
---

# /politika-taslak-guncelleme

1. `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` yükle → politika kütüphanesi indeksi.
2. Aşağıdaki iş akışını kullan.
3. Girdileri topla: boşluk, güncel onaylı politika metni, kural (mevzuat) metni.
4. Kuralın güncel olduğunu doğrula. Doğrulayamazsan uyar: `⚠️ KURAL DURUMU DOĞRULANAMADI`
5. Etkilenen politika bölümlerinin işaretli (redline) bir taslağını oluştur — mümkün olan en küçük değişiklik, `[doğrula]` etiketleri dahil.
6. Çıktı: Politika Taslak Güncelleme Notu. Bunu `[politika-adi]-taslak-guncelleme-[YYYY-AA-GG].md` adlı YENİ bir dosyaya yaz — asla kaynak politika belgesine yazma.
7. Takipçideki boşluğu KAPATMA. Boşluk ancak politika sahibi taslağı onaylayıp uyguladığında kapanır.

---

> Bu yetenek bir **öneri (proposal)** üretir, bir düzenleme yapmaz.

## Adım 1: Girdileri Topla

Aşağıdaki 3 girdi şarttır. Biri eksikse, tahmin etmeyin, isteyin.
1. Boşluk (Gap-ID veya kullanıcı açıklaması)
2. Güncel Politika Metni (dosya yolu veya yapıştırılmış metin — son onaylı sürüm mü teyit et)
3. Kural/Mevzuat Metni

## Adım 2: Kuralın Durumunu Doğrula

Kuralın yürürlükte (veya iptal edilmemiş/ertelenmemiş) olduğunu doğrula. Edemiyorsan başa uyarı koy ve tarihlere `[yayınlanan kurala göre yürürlük tarihi — durum doğrulanamadı]` etiketini ekle.

## Adım 3: Taslağı Üret (Redraft)

- Mümkün olan en küçük değişiklik (Bütün bölüm yerine paragraf, paragraf yerine cümle).
- Çıkarılan metin: `~~çıkarılan metin~~`
- Eklenen metin: **eklenen metin**
- Her değişikliğin nedenine dair satır içi açıklama ekle: `[Değişiklik: ... eklendi [doğrula]]`

## Adım 4: Çıktı

Dosya adında "taslak" ifadesi mutlaka olmalıdır. Format:
```markdown
[İŞ ÜRÜNÜ BAŞLIĞI]

> **⚠️ İnceleyen Notu**
> - **Kaynaklar:** [✓ doğrulandı | bağlı değil — model bilgisi, doğrulayın]
> - **Okundu:** [okunan politika bölümleri]
> - **Güncellik:** [kural durumu onaylandı | doğrulanamadı - uyarı]
> - **Güvenmeden Önce:** bunun son onaylı sürüm olduğunu onaylayın; kural durumunu teyit edin; boşluk takipçisini (gap tracker) sadece onaylanıp uygulandıktan sonra güncelleyin.

## Politika Taslak Güncelleme: [Politika Adı]

**Boşluk:** [GAP-ID]
**Mevzuat:** [isim, atıf]
**Politika:** [isim, son güncelleme tarihi]
**Durum:** TASLAK / ÖNERİ — henüz incelenmedi veya onaylanmadı

### Alt Çizgi
[Değişikliğin ne yaptığına dair tek cümle.]

### İşaretli Politika Bölümleri
[Değişen metinler, satır içi yorumlarla]

### Değişiklik Özeti
| # | Madde | Mevcut | Önerilen | Neden | Doğrulama |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

### Uygulamadan Önce - Kontrol Listesi
- [ ] Bu taslağın son onaylı politikaya uygulandığını onaylayın.
- [ ] Kural durumunu doğrulayın (örn. iptal davası yok).
- [ ] Politika sahibinin incelemesini alın.
- [ ] Şirket içi politika onay sürecinizi izleyin.
- [ ] Yalnızca uygulandıktan ve onaylandıktan sonra takipçiyi güncelleyin.

---
**Sırada ne var? Seçin:**
1. **Uygula ve Onay Al**
2. **[X] hakkında daha fazla bilgi al**
3. **Eskalasyon (Yukarı taşı)**
4. **İzle ve bekle**
```
