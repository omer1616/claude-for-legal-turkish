# Geçiş Planı ve Takip (claude-for-legal → claude-for-legal-turkish)

> **Canlı tracker.** Üst düzey kurallar [../CLAUDE.md](../CLAUDE.md)'de. Burası "nerede kaldık".
> Kademe: **A** doğrudan · **B** yeniden yazılmalı · **C** karşılığı yok.
> Durum: ⬜ bekliyor · 🔄 devam · ✅ bitti · ⛔ kapsam dışı.

Son güncelleme: 2026-06-08 · Faz: **Aktif avukat önceliği**

> **Sıralama kararı (2026-05-30):** Altyapı/niş eklentiler (eklenti-merkezi, urun-hukuku,
> yapay-zeka-yonetisimi, hukuk-klinigi, hukuk-ogrencisi) şimdilik beklemeye alındı.
> Aktif avukatın günlük işine dokunan plugin'ler önce taşınır.

---

## Genel ilerleme — YENİ SIRALAMA

| Öncelik | Plugin | TR slug | Kademe | Durum |
|---|---|---|---|---|
| **1** | litigation-legal | **dava-takibi** | Karma (A çekirdek → şimdi) | 🔄 profil ✅, skill'ler ⬜ |
| **2** | commercial-legal | **ticari-hukuk** | A (tamamı) | ⬜ |
| **3** | corporate-legal | **sirketler-hukuku** | A (entity-compliance B) | ⬜ |
| **4** | employment-legal | **is-hukuku** | Karma (A süreç → şimdi) | ⬜ |
| 5 | ip-legal | fikri-mulkiyet | Karma (A süreç → şimdi) | ⬜ |
| 6 | regulatory-legal | mevzuat-takibi | A (comments B) | ⬜ |
| — | privacy-legal | kisisel-veri-kvkk | B (KVKK) | ⬜ |
| bekle | legal-builder-hub | eklenti-merkezi | A | 🔄 kısmi |
| bekle | product-legal | urun-hukuku | A | ⬜ |
| bekle | ai-governance-legal | yapay-zeka-yonetisimi | A | ⬜ |
| bekle | legal-clinic | hukuk-klinigi | A | ⬜ |
| bekle | law-student | hukuk-ogrencisi | Karma | ⬜ |
| ⛔ | cocounsel-legal | — | C (Westlaw) | ⛔ |

---

## Faz 0 — Altyapı (paylaşılan)

- ✅ Yeni repo + git init (main)
- ✅ CLAUDE.md (proje hafızası + konvansiyon)
- ✅ MIGRATION.md (bu dosya — `.claude/` altında)
- ✅ Kaynak referans kopyası `./_kaynak/` (gitignore'lu, salt-okunur)
- ⬜ `.claude-plugin/marketplace.json` — TR plugin kayıtları (TR açıklamalarla)
- ⬜ Kök `README.md` / `QUICKSTART.md` — Türkçe
- ⬜ `references/` paylaşılan şablonlar (dashboard, company-profile) — Türkçe
- ⬜ `scripts/` (validate.py vb.) — büyük ölçüde nötr, gözden geçir
- ✅ Ortak `CLAUDE.md` guardrail bloğu TR çevirisi → kanonik [`references/ortak-guardrail-TR.md`](../references/ortak-guardrail-TR.md)
  (work-product header → Türk meslek sırrı/gizlilik rejimi notu; ABD araştırma araçları →
  TR muadilleri; FLSA örneği → TR zamanaşımı örneği; yollar `claude-for-legal-turkish`'e
  çevrildi; `{EKLENTI}` yer tutucusu). **Plugin profilleri bunu birebir kopyalayacak.**

---

## A GRUBU — önce bunlar

### eklenti-merkezi (legal-builder-hub) — A tamamı 🔄
Hiç hukuk içermez, saf araç/ekosistem. **Pilot — devam ediyor.**

Skill slug eşlemesi: cold-start-interview→`ilk-kurulum` · registry-browser→`kayit-tarayici` ·
skill-installer→`eklenti-kurucu` · related-skills-surfacer→`ilgili-eklentiler` ·
skill-manager→`eklenti-yoneticisi` · skills-qa→`eklenti-kalite-kontrol` ·
auto-updater→`otomatik-guncelleyici` · disable→`devre-disi-birak` · uninstall→`kaldir` ·
customize→`ozellestir` · agent registry-sync→`kayit-esitleme`

- ✅ Kabuk: dizin iskeleti · plugin.json · .mcp.json · hooks.json · .gitignore · README.md
- 🔄 CLAUDE.md profili (+ kanonik `references/ortak-guardrail-TR.md` çıkarımı) — **sıradaki adım**
- ⬜ ilk-kurulum · ozellestir · kayit-tarayici (+references) · ilgili-eklentiler
- ⬜ eklenti-yoneticisi · devre-disi-birak · kaldir · otomatik-guncelleyici · agents/kayit-esitleme · references/allowlist-default.yaml
- ⬜ eklenti-kurucu (+references) · eklenti-kalite-kontrol

### urun-hukuku (product-legal) — A tamamı
Risk kalibrasyonu güdümlü.
- ⬜ cold-start-interview · is-this-a-problem · launch-review
- ⬜ marketing-claims-review · feature-risk-assessment · matter-workspace · customize
- ⬜ agents/launch-watcher · references/currency-watch

### yapay-zeka-yonetisimi (ai-governance-legal) — A tamamı
Çok-yargılı tasarlanmış; kayıt/registry güdümlü.
- ⬜ cold-start-interview · use-case-triage · aia-generation · vendor-ai-review
- ⬜ reg-gap-analysis · policy-monitor · policy-starter · ai-inventory · matter-workspace · customize

### ticari-hukuk (commercial-legal) — A tamamı
Sözleşme incelemesi playbook güdümlü, yargı-nötr.
- ⬜ cold-start-interview · review (vendor/nda/saas) · amendment-history
- ⬜ renewal-tracker · escalation-flagger · stakeholder-summary · review-proposals
- ⬜ matter-workspace · customize · agents (renewal/deal-debrief/playbook-monitor) · hooks

### hukuk-klinigi (legal-clinic) — A tamamı
Klinik süreç akışı. Not: "ABA Formal Op. 512" → TR avukatlık meslek kuralları; research-start
"Westlaw arama terimleri" → TR araştırma (mevzuat.gov.tr/UYAP/Lexpera) — küçük uyarlama.
- ⬜ cold-start-interview · build-guide · ramp · client-intake · client-comms-log
- ⬜ research-start · memo · draft · client-letter · plain-language-letters
- ⬜ status · deadlines · supervisor-review-queue · semester-handoff · form-generation
- ⬜ deadlines.yaml

### sirketler-hukuku (corporate-legal) — A (entity-compliance → B)
- ⬜ cold-start-interview · tabular-review · diligence-issue-extraction
- ⬜ material-contract-schedule · closing-checklist · written-consent · board-minutes
- ⬜ deal-team-summary · ai-tool-handoff · integration-management · matter-workspace · customize
- ⬜ agents/dataroom-watcher
- 🅱️ **entity-compliance** → B: Delaware/eyalet beyanları → TTK + ticaret sicili takvimi

### mevzuat-takibi (regulatory-legal) — A (comments → B)
- ⬜ cold-start-interview (izleme listesi → Resmî Gazete / mevzuat.gov.tr)
- ⬜ reg-feed-watcher (kaynak Resmî Gazete'ye) · policy-diff · gaps · gap-surfacer
- ⬜ policy-redraft · matter-workspace · customize · agents/reg-change-monitor
- 🅱️ **comments** → B: ABD NPRM kamuoyu görüşü dönemi mantığı; TR'de farklı süreç

### dava-takibi (litigation-legal) — A çekirdek 🔄
- ✅ Kabuk: plugin.json · .mcp.json · hooks.json · README.md · matters/_log.yaml · .gitignore
- ✅ **CLAUDE.md profili** (ortak guardrail birebir kopyalandı + dava-takibi'ye uyarlandı;
  litigation'a özel iki paragraf eklendi: kelimesi kelimesine alıntı + pinpoint künye.
  TR uyarlamaları: meslek sırrı, TMS 37/KAP-SPK, ₺, Asliye Ticaret/İş/FSHHM/ISTAC,
  UYAP kaynağı, HMK/discovery-yok notu)

Skill slug eşlemesi: cold-start-interview→`ilk-kurulum` · matter-intake→`dosya-acilis` ·
matter-briefing→`dosya-brifingi` · matter-update→`dosya-guncelleme` ·
matter-close→`dosya-kapatma` · matter-workspace→`dosya-calisma-alani` ·
portfolio-status→`portfoy-durumu` · demand-intake→`talep-alimi` · legal-hold→`delil-saklama` ·
oc-status→`karsi-vekil-durumu` · chronology→`kronoloji` ·
brief-section-drafter→`dilekce-bolumu-taslaklayici` · customize→`ozellestir`
B skill'leri: claim-chart→`iddia-tablosu` · demand-draft→`ihtarname-taslagi` ·
demand-received→`gelen-talep` · subpoena-triage→`mzkr-triaji` `[doğrulanacak — subpoena TR karşılığı]` ·
deposition-prep / privilege-log-review → TR muadili `[doğrulanacak]`

A (taşınacak skill'ler):
- ⬜ ilk-kurulum · dosya-acilis · dosya-brifingi · dosya-guncelleme
- ⬜ dosya-kapatma · dosya-calisma-alani · portfoy-durumu · talep-alimi
- ⬜ delil-saklama · karsi-vekil-durumu · kronoloji · dilekce-bolumu-taslaklayici · ozellestir
B (sonra — usul hukuku farkı):
- 🅱️ iddia-tablosu · ihtarname-taslagi (FRE 408) · gelen-talep · subpoena-triage
- 🅱️ deposition-prep · privilege-log-review → HMK/CMK; discovery/deposition sistemi yok

### is-hukuku (employment-legal) — A süreç
A (taşı):
- ⬜ cold-start-interview · investigation-open/add/memo/query/summary · internal-investigation
- ⬜ leave-tracker · log-leave · international-expansion · expansion-kickoff/update
- ⬜ handbook-updates · hiring-review · policy-drafting · matter-workspace · customize
- ⬜ agents/leave-tracker
B (sonra — TR iş mevzuatı):
- 🅱️ termination-review (FMLA/OWBPA/WARN/eyalet final-pay → 4857, kıdem/ihbar)
- 🅱️ wage-hour-qa (FLSA → İş Kanunu çalışma süreleri) · worker-classification (ABC testi)

### fikri-mulkiyet (ip-legal) — A süreç
A (taşı):
- ⬜ cold-start-interview · clearance · invention-intake · fto-triage
- ⬜ ip-clause-review · oss-review · portfolio · matter-workspace · customize
- ⬜ agents/ip-renewal-watcher
B (sonra):
- 🅱️ takedown (DMCA §512 → 5651 sayılı Kanun) · cease-desist · infringement-triage

### hukuk-ogrencisi (law-student) — A pedagoji
A (taşı — IRAC yöntemi TR'de de öğretilir):
- ⬜ cold-start-interview · socratic-drill · case-brief · outline-builder · irac-practice
- ⬜ legal-writing · cold-call-prep · flashcards · study-plan · session · customize
B (sonra):
- 🅱️ bar-prep-questions (MBE/UBE) · exam-forecast → TR baro/staj sınavı muadili

---

## B GRUBU — Türk hukukçusu eliyle yeniden tasarım

- ⬜ **kisisel-veri-kvkk** (privacy-legal, tüm plugin): GDPR/CCPA/DPIA/DSAR → KVKK, VERBİS,
  Kişisel Verileri Koruma Kurulu, başvuru süreleri.
- ⬜ Yukarıdaki 🅱️ tek tek skill'ler (entity-compliance, comments, litigation usul,
  employment mevzuat, ip ihlal/takedown, law-student baro).

---

## C GRUBU — karşılığı yok

- ⛔ **cocounsel-legal** (Westlaw, ABD-only). TR muadili (Lexpera/Kazancı/UYAP MCP) ayrı iş.

---

## Açık notlar / kararlar

- **Ortak guardrail (2026-06-08):** Kanonik blok `## Outputs` → `## Matter workspaces`
  arasının iki+ plugin'de birebir aynı olan çekirdeğidir. Plugin'e özel paragraflar
  (litigation: kelimesi kelimesine alıntı + pinpoint künye; commercial: çift şiddet
  ekseni) kanonik bloğa GİRMEDİ — ilgili plugin profiline ayrıca eklenecek.
- `[doğrulanacak]` — **work-product → meslek sırrı:** İş-ürünü başlığının Türk
  hukukundaki tam koruma kapsamı (Avukatlık K. m.36 sır saklama, m.58 büro araması;
  şirket içi hukuk biriminin analizlerine uzanır mı; idari/kurul incelemelerinde —
  Rekabet Kurumu, KVKK Kurulu — ibraz muafiyeti var mı). Türk hukukçusu teyit etmeli.
- `[doğrulanacak]` — **TR araştırma araçları:** Kaynak etiketleri Lexpera/Kazancı/UYAP/
  mevzuat.gov.tr/Resmî Gazete olarak konuldu ama hangi araştırma MCP'lerinin gerçekten
  bağlanacağı belli değil; `.mcp.json`'lar netleşince etiket sözlüğü güncellenecek.
- `[doğrulanacak]` — **dashboard-template.md:** Ortak blok bu şablona atıf yapıyor ama
  şablon henüz TR'ye taşınmadı (Faz 0 `references/` kalemi).
