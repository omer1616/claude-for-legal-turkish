---
name: bosluk-cikarici
description: >
  Referans: /bosluk-analizi (gaps) ve yakında eklenecek görüş bildirme yeteneklerini destekleyen ortak boşluk (gap) takip çerçevesi.
  Açık politika boşluklarını takip eder, politika-farki'nden (policy-diff) gelen
  boşlukları alır, açık olanları ve eskiyenleri öne çıkarır, sahiplerine yönlendirir.
  Kullanıcı tarafından doğrudan çağrılmaz; arka planda çalışır.
user-invocable: false
---

# Boşluk Çıkarıcı (Gap Surfacer)

## Her Gönderim Öncesi Onay — İstisna Yok

Slack veya e-posta ile HERHANGİ bir mesaj (atama bildirimi, gecikme hatırlatıcı vb.) göndermeden önce:
1. Kullanıcıya tam olarak ne göndereceğinizi gösterin: "Şunu [N] kişiye göndermek üzereyim: [önizleme]."
2. Açık bir evet onayını bekleyin.

## Dosya Bağlamı (Matter Context)
Eğer profil CLAUDE.md'de "Matter workspaces" `Enabled` ise ilgili dosyanın context'ini yükleyin.

## Takipçi (Tracker)
Konum: `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/gap-tracker.yaml`

Formatı:
```yaml
gaps:
  - id: GAP-001
    requirement: "[mevzuat ne istiyor]"
    regulation: "[isim + atıf]"
    policy_affected: "[politika adı veya 'yeni politika gerekli']"
    gap_type: "partial"  # none | partial | full | new-policy | watch | comment-decision
    owner: "[sorumlu isim]"
    owner_slack: "[biliniyorsa Slack ID]"
    opened: 2026-03-01
    due: 2026-06-01
    status_verified: true
    status: "open"  # open | in-progress | closed | risk-accepted
    notified: false
    resolution: ""
```

**Asla doğrulanmamış bir kuraldaki boşluğu "Gecikmiş" (Overdue) olarak sınıflandırmayın.** `status_verified: false` olanlar "İzleme" (watch) kategorisinde kalmalıdır.

### Mod 1: politika-farki'ndan (policy-diff) Alma
Eğer politika farkı boşluklar (gap) bulursa, onları `gap-tracker.yaml` dosyasına ekleyin.
(Sorumluya bildirme onaylı yapılır.)

### Mod 2: Durum Raporu
Rapor şablonu (Kırmızı: Gecikmiş, Turuncu: 30 günden az kalmış, Sarı: Açık, vb.)
Kullanıcının atıflara güvenmemesi gerektiği uyarısını mutlaka çıktıya ekleyin.

### Mod 3: Bir boşluğu kapatmak
`/mevzuat-takibi:bosluk-analizi --close GAP-001`
Resolution: "Politika v2.3 olarak güncellendi ve onaylandı"

### Mod 4: Riski kabul etmek
`/mevzuat-takibi:bosluk-analizi --accept GAP-002`
Rationale: "X şartı sadece bizi etkilemeyen Y durumunda geçerli. Risk kabul edildi."
Kabul eden kişiyi de kaydedin.
