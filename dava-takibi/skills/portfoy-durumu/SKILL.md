---
name: portfoy-durumu
description: _log.yaml'dan portföy özetler — risk dağılımı, yaklaşan son tarihler, eski dosyalar, önemlilik toplamları, aşama dağılımı ve işaretlenmiş anomaliler. Kullanıcı "nerede duruyoruz", "kaç açık dosya var" dediğinde veya tüm aktif dosyalar genelinde portföy özeti ya da durum istediğinde kullan.
argument-hint: "[--hepsi | --risk=yuksek | --eski]"
---

# /portfoy-durumu

1. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` yükle → risk kalibrasyonu (`risk:` alanının nasıl okunacağını tanımlar).
2. Aşağıdaki iş akışını ve referansı uygula.
3. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml`'ı ayrıştır. Varsayılan olarak kapatılan dosyaları filtrele (`--hepsi` ile dahil et).
4. Özet üret: risk dağılımı, sonraki 14/30/60 gün içindeki son tarihler, >30 gündür güncelleme olmayan dosyalar, önemlilik toplamları, aşama dağılımı.
5. Anomalileri işaretle — kritik olarak işaretlenen her şey, geçmiş `sonraki_son_tarih`, risk orta veya yüksek olan ve dış avukat atanmamış dosyalar.

---

# Portföy Durumu

## Amaç

Tek okuma şu soruları yanıtlar: şu anda neyim var, neye dikkat etmek gerekiyor ve ne kayıyor? Çıktı taranabilir — bir sonraki aramasından önce üç dakikası olan avukat için tasarlanmış.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` — doğruluk kaynağı
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` — risk kalibrasyonu (risk/önemlilik alanlarını doğru yorumlamak için)

## Bayraklar ve Filtreler

Varsayılan: yalnızca aktif dosyalar (`durum: kapandi`'yı hariç tut).

Bayraklar:
- `--hepsi` — kapatılanları dahil et
- `--risk=yuksek` (veya `kritik` / `orta` / `dusuk`) — risk bandına göre filtrele
- `--eski` — yalnızca `son_guncelleme` > 30 gün olan dosyalar
- `--tur=is-hukuku` — dosya türüne göre filtrele
- `--sahip=[ad]` — iş birimi / İK / kurumsal iletişim sahibine göre filtrele

## Özet

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar — role göre farklılaşır; bkz. `## Bunu Kim Kullanıyor`]

# Portföy Durumu — [bugün]

**Aktif dosyalar:** [N]
**Kapatılan (yılbaşından bu yana):** [N] *(yalnızca --hepsi ile görünür)*

---

## Riske Göre

| Risk | Sayı | Dosyalar |
|---|---|---|
| Kritik | [N] | [slug'lar] |
| Yüksek | [N] | [slug'lar] |
| Orta | [N] | [yalnızca sayı — `--risk=orta` ile genişlet] |
| Düşük | [N] | [yalnızca sayı] |

## Yaklaşan Son Tarihler

| Süre | Dosyalar |
|---|---|
| 14 gün | [slug — son tarih — kısa açıklama] |
| 15–30 gün | [...] |
| 31–60 gün | [...] |

*Geçmiş `sonraki_son_tarih` aşağıda ayrıca işaretlendi.*

## Önemlilik

| Kategori | Sayı | Toplam maruziyet (orta nokta) |
|---|---|---|
| Karşılık | [N] | [₺X] |
| Açıklandı | [N] | [₺X] |
| İzleniyor | [N] | — |
| Yok | [N] | — |

## Aşamaya Göre

[tablo: dilekce / tahkikat / ön karar / yargılama hazırlığı / sulh / temyiz]

---

## ⚠️ Anomaliler ve İşaretler

- **Geçmiş son tarihler:** [`sonraki_son_tarih` geçmiş olan slug'lar]
- **Eski (>30g güncelleme yok):** [liste]
- **Çözülmemiş çatışmalar:** [`catisma.durumu`'nun [beklemede, yapilmadi] olduğu slug'lar]
- **Çatışma istisnası aktif:** [`catisma.istisna.tarafindan`'ın dolu olduğu slug'lar — elle temizlenene kadar kalıcı işaret]
- **Yüksek/kritik risk, dış avukatsız:** [liste]
- **Karşılık, >60g güncellemesiz:** [liste] — karşılık yeniden kalibrasyonu muhtemelen gecikmiş
- **Aktif davada delil saklama bildirilmemiş:** [liste]
- **Eksik alanlar:** [slug → alan]

---

## Kapanış Tavsiyesi

[Öne çıkan bir şey varsa önce neye bakılacağına dair bir iki cümle. Kalıp değil — yalnızca gerçekten öne çıkan bir şey varsa.]
```

## Anomali Kuralları

Bunlar skill'i süslü olmaktan çok yararlı kılan kontrollerdir:

1. **Geçmiş son tarih:** `sonraki_son_tarih < bugün` ve `durum != kapandi`
2. **Eski:** `son_guncelleme < bugün - 30g` ve `durum != kapandi`
3. **Çözülmemiş çatışma:** `catisma.durumu in [beklemede, yapilmadi]` ve `durum != kapandi`
3b. **Çatışma istisnası aktif:** `catisma.istisna.tarafindan != null` (hiç otomatik temizlenmez)
4. **Yüksek riskli, sigortasız:** `risk in [yuksek, kritik]` ve `dis_avukat.buro == null`
5. **Eski karşılık:** `onemlilik == karsilik` ve `son_guncelleme < bugün - 60g`
6. **Saklama boşluğu:** `durum in [tehdit, aktif, tahkikat, yargılama, temyiz]` ve `delil_saklama.gonderildi == false` — saklama yükümlülüğü makul öngörüde başlar, dolayısıyla `tehdit` dosyaları kapsam içindedir.
7. **Eksik alanlar:** herhangi bir zorunlu alan null — `risk`, `onemlilik`, `durum`, `acilis`, `catisma.durumu`

## Sonraki Adımlar Karar Ağacıyla Kapat

CLAUDE.md `## Çıktılar` bölümüne göre sonraki adımlar karar ağacıyla kapat. Bu skill'in ürettiğine seçenekleri uyarla — beş varsayılan dal (X'i taslakla, eskale et, daha fazla olgu topla, izle ve bekle, başka bir şey) başlangıç noktasıdır, zorunluluk değil.

Portföyde ~10'dan fazla dosya varsa veya kullanıcı istediğinde: dashboard sun (bkz. CLAUDE.md `## Çıktılar → Veri-yoğun çıktılar için dashboard önerisi`). Teklifi bu çıktıya göre şekillendir — risk kademesine göre sayılar, yaklaşan son tarihlerin zaman çizelgesi ve durum, çatışma kontrolü ve son dokunulma tarihli sıralanabilir dosya defteri.

## Bu Skill'in Yapmadıkları

- Kararlar almak. Dikkat edilmesi gerekenleri yüzeye çıkarır; kullanıcı önceliği belirler.
- Sahip olmadığı kesinliği taklit etmek. Maruziyet orta noktaları kabataslak ve bu şekilde etiketlenmelidir.
- Gerçek bir dava yönetim sisteminin yerini almak. Bu bir çalışma-belleği özeti, kayıt sistemi değil.