---
name: entegrasyon-yonetimi
description: >
  Kapanış sonrası (Post-closing) M&A entegrasyon takipçisi — aşamalı iş planı, 
  onay/izin (consent) takibi, sözleşme devirleri ve haftalık durum raporları. 
  Mevcut işlem belgelerinden (satın alma sözleşmesi, işlem özeti, kapanış kontrol listesi) 
  başlatılır. Kullanıcı "entegrasyon", "kapanış sonrası", "bekleyen onaylar", 
  "sözleşme devirleri", "entegrasyon durumu" veya "işlemde ne kaldı" dediğinde kullanın.
argument-hint: "[--init | --contracts | --report | --update | --export [--format csv|table] [--section all|consents|contracts|workplan]] [--deal [code]]"
---

# /entegrasyon-yonetimi

1. `deal-context.md` dosyasını (işlem kodu, hedef şirket, kapanış tarihi, işlem lideri) yükle.
2. Varsa `integration-tracker.yaml` dosyasını yükle (veya `--init` ise oluştur).
3. Bayrağa (flag) göre yönlendir:
   - `--init`: Mod 1 — PA'yı oku, aşamalı iş planı ve onay takipçisi oluştur
   - `--contracts`: Mod 2 — Sözleşme listesini içe aktar, kademelendir (tier) ve sınıflandır
   - `--report`: Mod 3 — Durum raporu oluştur
   - `--update`: Mod 4 — Manuel güncelleme yap veya yüklenen durum belgesini ayrıştır
   - `--export`: Mod 5 — CSV veya tablo dışa aktar
4. Sonuçları `integration-tracker.yaml` dosyasına kaydet. Her yazımdan sonra değişiklik özetini göster.

---

## Dosya (Matter) Bağlamı

`CLAUDE.md` içindeki `## Dosya çalışma alanları`nı kontrol et. Eğer etkinse ve aktif dosya yoksa sor. Çıktıları `matters/<dosya-slug>/` klasörüne yaz.

---

## Amaç

Dış avukat işlemi kapatır. Hukuk departmanı karmaşayı miras alır. Bu yetenek, kapanış sonrası entegrasyon için program yönetimi katmanıdır — ticari entegrasyon, IT sistemleri veya İK organizasyon tasarımı değil. Hukuki iş akışı: İzinler/onaylar, sözleşme devirleri, tüzel kişilik rasyonalizasyonu (birleştirme/tasfiye), Fikri Mülkiyet (IP) devir tescilleri ve SPA (Satın Alma Sözleşmesi) yükümlülükleri.
Neyin yapıldığını, neyin vadesinin geldiğini, neyin tıkandığını ve neyin karar gerektirdiğini takip eder.

---

## Takip (Tracker) Dosyası

`~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/deals/[kod]/integration-tracker.yaml` konumunda yaşar. `deal-context.md` ve `closing-checklist.yaml` (varsa) dosyalarından kapanış sonrası kalemleri miras alır.

(Tracker şeması (YAML) İngilizce orijinalindeki yapıdadır, örneğin `workplan`, `required_consents`, `contracts`, `pa_dates` alanlarını içerir. Format aynen korunur.)

---

## Mod 1: Başlatma (Init)

```
/sirketler-hukuku:entegrasyon-yonetimi --init [--deal [kod]]
```

### Adım 1: İşlem bağlamını yükle
`deal-context.md` yoksa bilgileri sorup oluştur. `closing-checklist.yaml` (kapani-kontrol-listesi) varsa kapanış sonrası öğelerini miras al.

### Adım 2: İşlem girdilerini oku
**Tam bir satın alma sözleşmesi (SPA) en eksiksiz takipçiyi üretir.** SPA'daki "Zorunlu İzinler" (Required Consents) listesi ve "Kapanış Sonrası Taahhütler" (post-closing covenants) bölümü kesin tarihler için yetkili kaynaktır. Ancak hiçbir belge yoksa bile standart (varsayılan) iş planı oluşturulabilir.

SPA'dan şunları çek:
- **Zorunlu İzinler Listesi:** Karşı taraf, sözleşme tipi ve SPA'daki son tarih (`pa_deadline`).
- **Kapanış sonrası yükümlülükler:** İş planı kalemlerine dönüştür (`pa-obligation` olarak etiketle).
- **Önemli Tarihler:** Zorunlu izinler son tarihi, Tekeffül (rep&warranty) ayakta kalma süresi (survival period) bitişi, emanet (escrow) serbest kalma tarihi, varsa ek ödeme (earn-out) ölçüm tarihleri.

### Adım 3: Aşamalı iş planını oluştur

**1. Gün — Hukuk Departmanı'nın (legal-owns) Sorumlulukları:**
- Unvan değişikliği tescili (Ticaret Sicili/MERSİS) [Kritik]
- Banka hesap imza sirküleri güncellemesi [Kritik]
- Önemli IP devirleri icrası (kapanışta ertelenmişse) [Kritik]
- Alan adı (domain) devri [Yüksek]
- Yönetici sorumluluk (D&O) sigortası uzatma poliçesi onayı [Kritik]

**30. Gün — Hukuk Departmanı'nın Sorumlulukları:**
- Zorunlu İzinler (Required Consents) için ilk temas [Kritik]
- IP (Patent/Marka) devir tescilleri (TÜRKPATENT/WIPO) [Yüksek]
- Önemli Sözleşmeler - Kademe 1 ve 2 devir analizi [Yüksek]

**90. Gün — Hukuk Departmanı'nın Sorumlulukları:**
- Zorunlu İzinler son tarihi — Alınmalı veya dış avukata/yönetime raporlanmalı [Kritik]
- Tüzel Kişilik Rasyonalizasyonu kararı (ayrı tut / birleştir (TTK m.136) / tasfiye et) [Yüksek]
- Kademe 3 kontrol değişikliği sözleşmelerinin çözümü [Kritik]

**180. Gün — Hukuk Departmanı'nın Sorumlulukları:**
- Şirket birleşme veya tasfiye tescil başvurusu (rasyonalizasyon kararına göre) [Yüksek]
- Tam sözleşme yenilemesi (novation) (TBK m.205) gerektiren sözleşmeler [Yüksek]
- Tekeffül (rep) süre takibi — yaklaşan bitiş [Orta]

(Not: "legal-supports" yani Hukuk'un İK/IT'ye destek verdiği roller de eklenir).

---

## Mod 2: Sözleşme Devri (Contract Assignment)

```
/sirketler-hukuku:entegrasyon-yonetimi --contracts [--deal [kod]]
```

### Adım 1: Sözleşme listesini al
- A) Bağlı bir VDR/havuz klasöründen tarama yap.
- B) Manuel yüklenen listeyi (CSV/Excel) oku.
- C) Hiçbiri yoksa SPA Eklerinden (Disclosure Schedules / Önemli Sözleşmeler) oku.

### Adım 2: Devir mekanizmasını belirle
Sözleşmeleri TBK/TTK ve sözleşme dillerine göre sınıflandır:
- `consent-required` (İzin Gerekli): Açık devir yasağı (Kademe 1 veya 2)
- `coc-provision` (Kontrol Değişikliği): Kapanışla tetiklenen fesih/onay hakkı (Kademe 3)
- `auto-assign` (Otomatik/Serbest): Devir serbest veya bağlı şirkete devir hakkı var (Kademe 4)
- `silent` (Sessiz): Sözleşmede devir hükmü yok — TBK m.205 uyarınca sözleşmenin devri karşı tarafın onayına tabidir. Avukat incelemesi için işaretle (Kademe 2)

SPA'da "Zorunlu İzinler" listesinde olanlar daima Kademe 1'dir.

### Adım 3: Kademelendirme (Tiering)
- **Kademe 1 (Zorunlu İzinler):** SPA'da listelenmiş, kesin son tarihi var.
- **Kademe 2 (Önemli, izin gerekli):** Sözleşmede kısıtlama var ama SPA'da listelenmemiş (90. gün hedefi).
- **Kademe 3 (Kontrol Değişikliği):** ⚠️ Harekete geç — Karşı tarafın fesih hakkı çoktan başlamış olabilir.
- **Kademe 4 (Otomatik):** Sadece takip.

---

## Mod 3: Durum Raporu

```
/sirketler-hukuku:entegrasyon-yonetimi --report [--deal [kod]]
```
Zorunlu izinlerin tamamlanma yüzdesi, sözleşme devirlerinin kademe bazında durumu, gecikmiş (🔴) veya bu hafta vadesi gelen (⏰) iş planı kalemleri ve engeller (blockers) ile birlikte bir durum raporu (markdown formatında) oluşturur.

---

## Mod 4: Güncelleme

```
/sirketler-hukuku:entegrasyon-yonetimi --update [--deal [kod]]
```
Manuel ("Salesforce onayını aldık, durumu güncelle") veya belge yüklemesi yoluyla tracker'ı (YAML) günceller. Değişiklikleri ve oluşan yeni riskleri (örn: "Onay reddedildi -> SPA tazminat riski, dış avukata sor") kullanıcıya bildirir.

---

## Mod 5: Dışa Aktar (Export)

```
/sirketler-hukuku:entegrasyon-yonetimi --export [--format csv|table] [--section all|consents|contracts|workplan]
```
Verileri tablo veya CSV olarak dışa aktarır.

> **Formül Enjeksiyonu Savunması:** Excel/CSV çıktıları üretirken, karşı taraftan veya belgelerden alınan metinlerin (isimler, sözleşme maddeleri) "=", "+", "-", "@" vb. formül tetikleyicilerle başlamadığından emin olun (başına tek tırnak `'` ekleyin).

---

## Bu yetenek ne yapmaz
- Ticari entegrasyonu (IT, İK, Finans) yönetmez.
- İbraname, onay talebi veya devir (novation) sözleşmelerini kendi taslaklamaz (bunlar `yazili-onay` veya dış avukat işidir).
- Onay reddedildiğinde SPA ihlali/tazminat analizini yapmaz — durumu işaretler, analiz avukatındır.
- Ek ödeme (earn-out) performansını takip etmez (bunu finans yapar, bu sadece tarihi not eder).
