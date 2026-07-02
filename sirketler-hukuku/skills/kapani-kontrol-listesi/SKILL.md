---
name: kapani-kontrol-listesi
description: >
  Kapanışı ne engelliyor — durum, kritik yol ve kapanışa kalan gün sayısı 
  ile kapanış kontrol listesini (closing checklist) sürdürün. Kendini 
  güncelleyen: due diligence bulgularından ve liste (schedule) hazırlıklarından 
  gelen yeni kalemleri yutar, durumu izler, nelerin bloke ettiğini öne çıkarır. 
  Kullanıcı "kapanış kontrol listesi", "kapanış için ne kaldı", "liste durumu", 
  "listeye ekle" dediğinde veya planlı bir durum çekiminde kullanın.
argument-hint: "[isteğe bağlı: kalem ID + durum güncellemesi]"
---

# /kapani-kontrol-listesi

1. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/deals/[kod]/closing-checklist.yaml` dosyasını oku ve aşağıdaki modları kullan.
2. Durum güncellemesi verilmişse: Mod 3 (kalemi güncelle).
3. Aksi takdirde Mod 4: Bloke eden öğeler, kritik yol, kapanışa kalan günler.

---

## Dosya (Matter) Bağlamı

`CLAUDE.md` içindeki `## Dosya çalışma alanları`nı kontrol et. Eğer `Etkin` değilse (şirket-içi kullanıcılar için varsayılan), bu paragrafı atla. Eğer etkinse ve aktif dosya yoksa sor: "Bu hangi dosya (matter) için? `/sirketler-hukuku:dosya-calisma-alani degistir <slug>` çalıştır." Dosyaya özel bağlam için `matter.md` dosyasını yükle. Çıktıları `matters/<dosya-slug>/` klasörüne yaz.

---

## Amaç

İşlemler, kontrol listesi bittiğinde kapanır. Listedeki her şey tamamlanmalıdır. Eksik bir şey kalmamalıdır. Bu yetenek (skill) listeyi sürdürür, due diligence'da yüzeye çıktıkça yeni öğeleri yutar ve ekibe neyin kapanışı engellediğini (blocking) söyler.

## Kontrol Listesi

`~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/deals/[kod]/closing-checklist.yaml` konumunda yaşar. Yapısı:

```yaml
deal_code: "Proje Şahin"
target_close: [TARİH]
signing_date: [TARİH]
last_updated: [TARİH]

conditions_precedent:
  - id: CP-001
    item: "Rekabet Kurumu bekleme süresinin dolması/onayı"
    category: "Düzenleyici (Regulatory)"
    responsible: "Alıcı avukatı"
    due: 2026-04-15
    status: "Başvuru 2026-03-01'de yapıldı, süreç devam ediyor"
    blocking: true
    source: "Satın Alma Sözleşmesi md.7.1(a)"

  - id: CP-002
    item: "Acme Corp devir/kontrol değişikliği onayı"
    category: "Üçüncü taraf onayları (Consents)"
    responsible: "Hedef Şirket — Ahmet Yılmaz"
    due: 2026-04-20
    status: "Talep 2026-03-10'da gönderildi, yanıt yok"
    blocking: true
    source: "Ek 3.12(a)(4); Acme Çerçeve Sözleşmesi md.14.2"

closing_deliverables:
  - id: CD-001
    item: "Faaliyet Belgesi — Hedef Şirket (Ticaret Odası)"
    category: "Kurumsal"
    responsible: "Hedef Şirket avukatı"
    due: 2026-04-28
    status: "Başlamadı"
    blocking: true
    source: "Satın Alma Sözleşmesi md.2.3(b)(iv)"

  # ... vb
```

## Modlar

### Mod 1: Satın alma sözleşmesinden (SPA) başlatma

İmzalanmış (veya son haline yakın) satın alma sözleşmesini oku. Çıkar:

- Tüm ön şartlar / kapanış koşulları (Conditions Precedent / CPs - yerleri sözleşmeye göre değişir, madde başlıklarını okuyun)
- Tüm kapanış teslimatları (Closing Deliverables eki veya ilgili madde)
- Kapanış öncesi bir son tarihi olan tüm taahhütler (covenants)

Her biri sözleşme maddesine kaynak gösterilerek bir kontrol listesi öğesi haline gelir.

**Düzenleyici/onay kalemlerini doldurmadan önce araştırın.** Rekabet (Antitröst), yabancı yatırım ve sektöre özel onaylar (örneğin Rekabet Kurumu, BDDK, EPDK, SPK), değişen mekaniklere, eşiklere ve zaman pencerelerine sahiptir. İlgili düzenleyici koşulunun adını SPA'dan çıkarın, ardından mevcut yürürlükteki mekanikleri (kim başvurur, ne zaman, bekleme süresi nedir) araştırın. Birincil kaynaklara atıf yapın ve güncelliğini doğrulayın. Zamanlama varsayımını hafızadan uydurmayın.

**Önemli Olumsuz Değişiklik (MAC/MAE) kapanış koşulları.** SPA'dan tanımlanmış terimi çekin — MAC/MAE çerçevesi standart değil, müzakere edilmiştir. Bir olayı potansiyel MAC tetikleyicisi olarak işaretlemeden önce, kullanılan dilin tabi olduğu hukukun (TTK, Türk Borçlar Kanunu veya Delaware/NY vb.) istisnaları (carve-outs) ve nicel testleri nasıl ele aldığını araştırın.

**Önemli sözleşmelerden onay gereksiniminin çıkarılması**, tabi olunan hukukun varsayılan kurallarına (örn. TBK devir kuralları) ve her sözleşmedeki belirli devir yasağı diline bağlıdır. Varsayılanı farz etmek yerine sözleşme başına geçerli kuralı analiz edin.

### Mod 2: Due diligence'dan veri yutma ("kendini güncelleyen" kısım)

Mod 2, bir önceki-aşama (upstream) yeteneği kapanış öncesi aksiyon gerektiren bir bulgu ürettiğinde tetiklenir. Yutulan yetenekler ve çıktılar:

- **`due-diligence-sorun-cikartma` bulguları** — kapanış eylemi için işaretlenmiş herhangi bir bulgu (onay, hissedar/genel kurul oyu, yönetim kurulu kararı, düzenleyici bildirim, ibraname, emanet mekanizması, rehin fek yazısı vb.). Yalnızca "onaylar" değil — tam liste için çıkarım yeteneğinin Devirler (Handoffs) bölümüne bakın.
- **`onemli-sozlesme-takvimi` CoC / devir kalemleri** — liste (schedule) oluşturulması sırasında yüzeye çıkan kontrol değişikliği, devir yasağı, MFN tetikleyicileri.
- **`anlasma-ekibi-ozeti` çıktısı** — yönetici özeti, bireysel raporların mekanik okunmasının kaçırabileceği kapanış eylem kalemlerini (örn. birden fazla iş sözleşmesi üzerinden birleştirilmiş toplu ibra, paket onaylar) yüzeye çıkarır. Deal-team-summary'deki eylemleri kontrol listesiyle mutabakatlar.

Handoff şeması (tüm kapanış öncesi eylemleri kapsar):

```yaml
handoff:
  # Gerekli alanlar
  item: "[Karşı taraf veya eylem, tek satır]"
  category: "[Üçüncü taraf onayları | Genel Kurul / YK eylemi | Düzenleyici başvuru | İbraname/Fesih | Emanet(Escrow)/Holdback | Kapanış Teslimatı]"
  source: "[Sözleşme adı / yasal madde / VDR yolu]"
  blocking: true  # sözleşmede bir önemlilik nitelemesi (materiality qualifier) yoksa
  severity: "[🔴 / 🟠 / 🟡 / 🟢 — önceki aşamadan taşınır]"

  # Onay / üçüncü taraf eylem alanları
  counterparty: "[örn., ABC A.Ş.]"
  guarantor: "[örn., Alıcı ana şirket garantisi gerekli veya N/A]"
  conditions: "[karşı tarafın eklediği koşullar — örn. 'onay verilmeden önce kefalet senedi gerekir']"
  notice_deadline: "[örn., kapanıştan 30 gün önce veya belirli bir tarih]"

  # Kurumsal (Şirketler Hukuku) eylem alanları
  approval_body: "[Genel Kurul | Yönetim Kurulu | Komite | Düzenleyici]"
  approval_threshold: "[örn., Birleşme için TTK 136'ya göre oylama, %75 nisap]"
  statutory_or_charter_source: "[örn., TTK m.136; Esas Sözleşme m.4]"

  # Zamanlama
  estimated_time_to_complete: "[örn., 30 gün]"
  must_occur_before: "[örn., kapanış | imza | genel kurul tarihi]"
```

Önceki aşamanın (upstream) doldurduğu HER alanı koruyun. Yinelenen kayıtları engellemek (de-dupe) için eylem tipine + karşı tarafa bakın (sadece isme bakmayın, aynı şirketin onayı ile ibrası farklı şeylerdir). Birleştirirken (merge) alanların üzerine yazmak yerine her iki veriyi de koruyun.

### Mod 3: Durum Güncellemesi

Kullanıcı (veya veri-odasi-izleyici agent'ı) bir durum güncellemesi sağlar. Öğeyi bulun, statüyü ve 'son güncellenme' tarihini güncelleyin.

```
/sirketler-hukuku:kapani-kontrol-listesi
CP-002: Acme yanıt verdi, onay formu eklendi, karşı imza (countersignature) gerekiyor
```

### Mod 4: Neler Bloke Ediyor? (What's blocking)

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — CLAUDE.md'den]

> Bu durum raporu satın alma sözleşmesi, due diligence bulguları ve iç işlem kayıtlarından türetilmiştir. Gizlilik statüsünü miras alır...

## Kapanış Kontrol Listesi Durumu — [İşlem kodu] — [Tarih]

**Hedef kapanış:** [tarih] ([N] gün kaldı)
**Kalemler:** [N] toplam — [N] tamamlandı, [N] devam ediyor, [N] başlamadı

### 🔴 Bloke eden ve risk altında

| ID | Kalem | Teslim/Süre | Durum | Kalan Gün |
|---|---|---|---|---|
| [CP-XXX] | [kalem] | [tarih] | [durum] | **[N]** |

### 🟡 Bloke eden, rayında (on track)

[aynı tablo]

### ✅ Tamamlandı

[N] kalem — [daraltılmış liste]

### Bloke etmeyen (kapanış sonrası, bilgi amaçlı)

[N] kalem

---

**Kritik yol (Critical path):** [Sarkarsa kapanış tarihini geciktirecek kalem(ler)]
```

## Kritik yol (Critical path) analizi

Tüm bloke eden (blocking) öğeler eşit değildir. Alınması 30 gün süren bir onay kritik yoldur. 2 gün süren bir faaliyet belgesi, bloke edici de olsa kritik yol değildir.

Her bloke eden öğe için tamamlanma süresini tahmin edin. `(Son tarih - bugün) < tahmini süre` olanlar risk altındadır. Bunlar her durum raporunun en üstüne yerleşir. 

Liste ~10 kalemden uzunsa veya kullanıcı isterse Dashboard (pano) sunun.

## Sonuç doğuran eylem (Consequential-action) kapısı (Kapanışı onayla)

**"Kapanışa hazır / tüm ön şartlar (CP) karşılandı" sertifikası veya kapanış notu üretmeden önce:** CLAUDE.md'deki `## Bunu kim kullanıyor` bölümünü okuyun. Rol **Avukat değil** ise:

> Kapanış koşullarının karşılandığını onaylamak (veya bunu iddia eden bir kapanış notu üretmek) hukuki sonuçlar doğurur — bu, para transferini (funds flow) ve kapanış sonrası yükümlülükleri tetikleyen sinyaldir. Bunu bir avukatla incelediniz mi? Evet ise ilerleyin. Hayır ise, onlara götüreceğiniz kısa özet:
>
> - Durumuyla birlikte tam CP listesi
> - Kanıtların zayıf veya eksik olduğu yerler
> - Zamanında kapanmayacak öğeler için gereken feragatnameler (waivers) veya yan mektuplar (side letters)
> - Açık sorular (halen bekleyen karşı taraf onayları, MAC/bring-down riski)
> - Avukata ne sorulmalı (bu iş kapandı denebilir mi; atlanmaması gereken şartlar atlanıyor mu; istisna listesine ne eklenmeli)
>
> Bir avukata ihtiyacınız varsa baroların yönlendirme servisleriyle iletişime geçin.

Açık bir "evet" almadan bu kapıyı geçip son bir "kapanışa hazır" sertifikası üretmeyin. Durum takibi ve "neler bloke ediyor" raporları bu kapıyı gerektirmez.

---

## Bu yetenek ne yapmaz

- Onayları kendi almaz, formları doldurmaz veya belgeleri taslaklamaz. Bunların olması gerektiğini takip eder.
- Neyin kapanışı bloke edeceğine karar vermez — bunu satın alma sözleşmesi belirler. Bu yetenek sözleşmeyi okur.
- İşlemi kapatmaz. Size ne zaman kapatabileceğinizi söyler.
