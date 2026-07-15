# MIGRATION / Durum İzleyici

*CLAUDE.md'nin işaret ettiği granüler ilerleme izleyicisi. Her oturum sonunda güncellenir.*

## Plugin durumu

| Plugin (TR slug) | Kaynak | Kademe | Durum |
|---|---|---|---|
| **hukuk-asistani** | — (yeni, kaynaktan çeviri değil) | — | **bitti** (v1.0.0, 2026-07-16) |
| dava-takibi | litigation-legal | A | bitti |
| ticari-hukuk | commercial-legal | A | kısmen (skill'ler mevcut, gözden geçirilecek) |
| sirketler-hukuku | corporate-legal | A | kısmen |
| is-hukuku | employment-legal | B | kısmen |
| fikri-mulkiyet | ip-legal | B | kısmen |
| mevzuat-takibi | regulatory-legal | A | kısmen |
| eklenti-merkezi | legal-builder-hub | A | kısmen |
| kisisel-veri-kvkk | privacy-legal | B | beklemede |
| urun-hukuku / yapay-zeka-yonetisimi / hukuk-klinigi / hukuk-ogrencisi | — | — | beklemede (altyapı) |

## hukuk-asistani (yeni — 2026-07-16)

**Ne:** Kaynak setin çevirisi değil; teknik bilgisi sınırlı avukatlar için sıfırdan
tasarlanmış sade, genel amaçlı günlük asistan. Kapsam: dava/dosya takibi, sözleşme
inceleme + hazırlama, dilekçe/ihtarname, özetleme, genel araştırma.

**Skill'ler (10):** `ilk-kurulum` (5 soru, ~3 dk), `yardim`, `yeni-dosya`,
`dosyalarim`, `dosya-notu`, `sozlesme-incele`, `sozlesme-hazirla`, `dilekce`,
`ozetle`, `arastir`.

**Bilinçli tasarım kararları:**

- **`.mcp.json` yok** — eklenti bağlayıcısız çalışacak şekilde tasarlandı; araştırma
  web araması + kaynak etiketleriyle yürür. Kullanıcı bir TR araştırma MCP'si
  bağlarsa `arastir` onu kullanır.
- **Sicil dosyası yok** — `_log.yaml` benzeri ayrı kayıt tutulmaz; her dosya tek
  `dosya.md` (YAML frontmatter + notlar), `dosyalarim` frontmatter'ları tarar. Tek
  kayıt kaynağı ilkesi.
- **Veriler kullanıcının görebildiği klasörde** — varsayılan
  `~/Documents/Hukuk-Asistani/` (kurulumda değiştirilebilir); config yolunda yalnızca
  profil (`~/.claude/plugins/config/claude-for-legal-turkish/hukuk-asistani/CLAUDE.md`)
  ve verification-log durur.
- **Guardrail bloğu** `references/ortak-guardrail-TR.md`'den kopyalandı
  (`{EKLENTI}` → `hukuk-asistani`) — tek sapma: kanonik bloğun son bölümü
  **"Dosya çalışma alanları" alınmadı** (bu eklentide `dosya-calisma-alani` skill'i
  yok; dosya bağlamı çalışma klasörü kuralıyla yönetiliyor). Kanonik blok değişirse
  bu profil de güncellenmeli.
- Standart slug sözlüğüne uyum: kurulum skill'i `ilk-kurulum` (tüm plugin'lerle aynı).

**Açık işler:**
- [ ] Gerçek kullanıcı testi: kurulum akışı teknik olmayan bir avukatla denenmeli.
- [ ] `dilekce` iskeletlerinin (özellikle istinaf/temyiz ve icra itiraz formatları)
      bir Türk avukat tarafından gözden geçirilmesi `[doğrulanacak]`.
- [ ] `dosyalarim` süre/adli tatil mantığının örnek dosyalarla smoke testi.

## Proje geneli açık notlar

- `references/dashboard-template.md` hâlâ TR'ye taşınmadı (guardrail bloğu buna
  `[doğrulanacak]` etiketiyle atıf yapıyor).
- Meslek sırrı kapsamı (Av. K. m.36/m.58) ve TR araştırma MCP mevcudiyeti — Türk
  hukukçusuyla teyit bekliyor (bkz. üst dizin CLAUDE.md "Open items").
