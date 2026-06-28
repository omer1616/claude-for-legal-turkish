---
name: karsi-vekil-durumu
description: Aktif portföy genelinde dış avukatlara haftalık durum talebi e-postası taslakları üretir — dosya başına markdown, Gmail MCP mevcutsa taslak oluşturur. Kullanıcı dış avukat durum talebi, haftalık dış avukat check-in veya portföy günlüğünden dosya başına durum e-postaları taslaklanmasını istediğinde kullan.
argument-hint: "[--hepsi | --slug=foo | --gmail-yok]"
---

# /karsi-vekil-durumu

Haftalık çalıştırmak için `/dava-takibi:karsi-vekil-durumu`'nu başlatmak üzere tekrarlayan bir hatırlatıcı ayarla. Otomatik zamanlama, dahili olmayan bir zamanlanmış görevler entegrasyonu gerektirir.

1. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` yükle, varsayılan kurallara göre (veya bayraklara göre) filtrele.
2. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` yükle → dış avukat talimat tarzı, imzalayan varsayılanları, bütçe duruşu.
3. Aşağıdaki iş akışını ve referansı uygula.
4. Kapsam dahilindeki her dosya için: `matter.md` + `history.md` oku, dosya başına e-posta taslakla.
5. Markdown'u `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/karsi-vekil-durumu/[YYYY-AA-GG]/[slug].md` yaz.
6. Gmail MCP kimlik doğrulaması yapılmışsa: Gmail taslakları oluştur. Aksi hâlde: yalnızca markdown, özette belirt.
7. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/karsi-vekil-durumu/[YYYY-AA-GG]/_ozet.md` yaz — neyin çalıştığını, neyin atlandığını ve nedenini belirt.

---

# Karşı Vekil Durumu

## Amaç

Her hafta 5–15 dosya genelinde dış bürolara aynı durum talebi e-postasını yazmak mekanik bir bilişsel yüktür. İçerik dosya başına tutarlıdır (durum, bekleyen kararlar, bütçe kontrolü). Hedef kitle tutarlıdır (büro sorumlu avukatı). Ton tutarlıdır (ev dışı avukat talimat tarzına göre). Zamanlanmış bir görev hepsini taslaklar; avukat inceler ve gönderir.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/_log.yaml` — filtreleme ve alan kaynağı
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/matter.md` — dosya bağlamı (mevcut duruş, açık sorular)
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/matters/[slug]/history.md` — ne sorulacağını bilgilendirmek için son olaylar
- `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` → dış avukat talimat tarzı, imzalayan adı/e-postası, bütçe duruşu

## Filtreleme — Hangi Dosyalar?

Varsayılan filtre:

- `durum != kapandi`
- `dis_avukat.buro != null` VE `dis_avukat.sorumlu != null`
- Şunlardan biri: son güncellemeden bu yana >10 gün (bir şeylerin olması için zaman) VEYA 21 gün içinde `sonraki_son_tarih` var

Son 10 gün içinde durum güncellemesi olan dosyaları atla (yeniden ping atmaya gerek yok) ve `dis_avukat.eposta`'sı null olan dosyaları atla (Gmail taslağı için e-posta adresleri gerekli; yine de markdown üret).

Bayraklar:
- `--hepsi` → son güncelleme tarihine bakılmaksızın tüm aktif dosyalar için taslakla
- `--slug=[slug]` → yalnızca tek bir dosya için taslakla (anlık talep)
- `--gmail-yok` → MCP mevcut olsa bile Gmail taslağı oluşturmayı atla

## Dosya Başına E-posta Taslağı

Her e-postanın aynı iskeleti var; içerik dosyaya özgü.

**Konu:** ev konvansiyonuna göre (`~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` dış avukat talimat tarzından; yedek: `[Dosya: [dosya adı]] — Haftalık durum güncellemesi`)

**Gövde iskeleti:**

```
[sorumlu avukat adı],

[Tek cümle açılış — doğal, ev tonuyla örtüşür.]

[Dosya adı] hakkında bilgi almak istiyoruz. Birkaç konu:

1. **[Son güncelleme tarihinden] bu yana durum** — ne ilerledi, ne bekliyor? Son görüşmemizden bu yana herhangi bir dilekçe, duruşma, yazışma veya görüşme oldu mu?

2. **Yaklaşan son tarihler** — [günlükteki sonraki_son_tarih + matter.md'deki son tarihler] görüyorum. Kapsam planını ve eklememiz gereken tarihleri teyit edin.

3. **Bekleyen kararlar** — [dış avukat girdisi gerektiren matter.md'deki açık soruları çek; yoksa bu maddeyi çıkar ve yeniden numaralandır]

4. **Bütçe** — [aylık / üç aylık / talep üzerine — `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` bütçe duruşuna göre]. [matter.md'deki bütçe yetkilendirmesine] karşı durumumuz nedir? İşaretlenecek bir sapma var mı?

[Önemliyse ve ilgiliyse: 5. Spesifik talep — ör. "Lütfen itiraz dilekçesinin son taslağını [tarihten] önce gönderin" — matter.md'deki açık sorulardan.]

[İmza — ad, rol, iletişim. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` dış avukat talimatları için imzalayan varsayılanından.]
```

Tonu `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` dış avukat talimat tarzına göre uyarla — bazı bürolar resmi "Sayın avukat" kullanır; diğerleri isim ve maddeler kullanır. Eşleştir.

## Çıktı

### Markdown Taslakları

Şuraya yaz: `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/karsi-vekil-durumu/[YYYY-AA-GG]/[slug].md`

Her dosya bir e-postadır, şu şekilde biçimlendirilir:

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — eklenti yapılandırmasına göre ## Çıktılar — role göre farklılaşır; bkz. `## Bunu Kim Kullanıyor`]

# [Dosya adı] — Dış avukat durum talebi — [YYYY-AA-GG]

**Alıcı:** [günlükteki dis_avukat.eposta] ([dis_avukat.sorumlu], [dis_avukat.buro])
**Gönderen:** [imzalayan adı / e-postası]
**Konu:** [konu satırı]

> Yukarıdaki iş-ürünü başlığı bu iç kaydı korur. Aşağıdaki giden e-posta gövdesi, tutulmuş bir dosyadaki dış avukatlara gider — bu gizlilik niteliği taşıyan bir iletişimdir. Gönderilen e-postanın başına ev gizlilik işaretini (`~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md` gizlilik konvansiyonları) koy, genellikle `GİZLİ — Avukat-Müvekkil İletişimi / Meslek Sırrı`, bu iç iş-ürünü başlığını değil.

---

[iskelete göre gövde]
```

### Gönderme Kapısı (Her Taslakta Kapanış Notu)

Aşağıdakini her markdown taslağına, gövdenin hemen altına ve çalıştırma meta verilerinin üstüne ekle — göndermeden önce çıkar:

> Bu, avukat incelemesinden önce dış avukatlara gönderilmek üzere taslak bir durum e-postasıdır. Gizlilik çemberi dışında paylaşmak istemediğin ayrıcalıklı içeriği, olgusal doğruluğu, tonu ve bütçe duruşunu kontrol et. İncelenmeden gönderme — rutin haftalık check-in'ler bile gönderenin yazmak istemediği teori, strateji veya tavizleri yazıya dökebilir.

### Gmail Taslakları (MCP Mevcutsa)

Gmail taslağı oluşturma MCP'si kimlik doğrulaması yapılmışsa:

- Kullanıcının Gmail'inde `alici`, `gonderen`, `konu`, `govde` dolu hâlde dosya başına taslak oluştur
- Taslak Taslaklar klasörüne gider; kullanıcı Pazartesi sabahı inceler ve gönderir
- Gmail MCP mevcut değilse veya başarısız olursa: yalnızca markdown'a dön ve kullanıcıya bildir

### Çalıştırma Özeti

Tüm dosyaları işledikten sonra `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/karsi-vekil-durumu/[YYYY-AA-GG]/_ozet.md` yaz:

```markdown
# Dış Avukat Durum Çalıştırması — [YYYY-AA-GG]

**İşlenen dosyalar:** [N]
**Oluşturulan taslaklar:** [N]
**Gmail taslakları:** [oluşturuldu / atlandı — neden]

## Taslaklanmış

| Dosya | Sorumlu avukat | Son güncelleme | Dahil etme nedeni |
|---|---|---|---|
| [slug] | [sorumlu] | [tarih] | [eski / yaklaşan son tarih / --hepsi / --slug] |

## Atlananlar

| Dosya | Neden |
|---|---|
| [slug] | yakın güncelleme (son dokunuş [tarih]) |
| [slug] | günlükte dış avukat e-postası yok — `/dava-takibi:dosya-guncelleme [slug]` ile güncelle |

## Anomaliler

- Dış avukat atanmamış dosyalar: [liste — yüksek/kritik risk varsa işaretlendi]
- Dış avukatı olan ama günlükte e-postası olmayan dosyalar: [liste]
```

## Zamanlama

Bu skill haftalık çalışacak şekilde tasarlanmıştır. Otomatik zamanlama, plugin'le birlikte gelmeyen bir zamanlanmış görevler entegrasyonu gerektirir. Haftalık çalıştırmak için `/dava-takibi:karsi-vekil-durumu`'nu başlatmak üzere tekrarlayan bir hatırlatıcı ayarla — ör. takvimine Pazartesi sabahı.

Anlık: istediğin zaman `/karsi-vekil-durumu`. Tek dosya için `/karsi-vekil-durumu --slug=foo`.

## Bu Skill'in Yapmadıkları

- **E-postaları göndermek.** Yalnızca taslaklar. Avukat inceler ve gönderir.
- **Sahip olmadığı içeriği üretmek.** `matter.md` zayıfsa, e-posta kısa ve genel durum soruları sorar. Skill hiçlikten spesifik sorular icat etmez.
- **Başarısızlıkları yeniden denemek.** Gmail taslağı oluşturma çalıştırma ortasında başarısız olursa, skill başarısızlığı kaydeder ve markdown'la devam eder. Kullanıcı kimlik doğrulamayı düzelttikten sonra yeniden deneyebilir.
- **history.md'yi yeniden yazmak.** Bağlam için okur; değiştirmez. (Dış avukatın yanıtı yeni olaylar ortaya çıkarırsa, bunları kaydetmek için `/dava-takibi:dosya-guncelleme [slug]` kullan.)
- **Minimum şablonu zorlamak.** Ev tonu "tek satır, ad, tamam" ise, taslak buna uyar ve madde yapısını atlar. `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`'yi eşleştir.