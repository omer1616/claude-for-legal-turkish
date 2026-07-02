# Fikri Mülkiyet (IP) Hukuku Eklentisi (Plugin)

Fikri mülkiyet pratiği: marka, patent, telif hakkı, ticari sır ve açık kaynak (open source). Sözleşmelerdeki FM maddelerini inceler, marka temizlik (clearance) ve serbest kullanım (FTO) ilk triyajını yapar, tescil ve yenileme tarihlerini takip eder ve açık kaynak lisans uyumluluğunu denetler. (Not: DMCA/5651 içerik kaldırma ve ihlal ihtarname yetenekleri şu an beklemededir).

Her çıktı, nihai bir hukuki sonuç değil, **avukat incelemesi için bir ilk taslaktır.** 

## Kimler İçin

| Rol | Ana İş Akışları |
|---|---|
| **Şirket İçi FM Müşaviri** | FM madde incelemesi, portföy gözetimi, FTO triyajı |
| **FM Uzmanı / Paralegal** | Portföy ve yenileme takibi, marka temizlik ilk taraması |
| **Hukuk Bürosu FM Avukatı** | Müvekkil bazlı dosya alanları, temizlik ve FTO triyajı, madde incelemesi |

Bu eklenti **patent istemi (claim) taslağı hazırlamaz.** Fikri mülkiyet eklentisi bir patent vekilinin yerine geçmez, sadece ön değerlendirme, FTO triyajı ve yenileme takibi gibi süreçlere yardımcı olur.

## İlk Çalıştırma: İlk Kurulum Görüşmesi

Kurulum için:
```
/fikri-mulkiyet:ilk-kurulum
```
Bu görüşme sonrası profiliniz `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` konumuna kaydedilir. Eklenti, ABD (USPTO) odaklı değil, sizin belirttiğiniz yargı çerçevesinde (örn. TÜRKPATENT, EPO, WIPO vb.) çalışacak şekilde kendini ayarlar.

## Komutlar (Yetenekler - Skills)

| Komut | Ne Yapar |
|---|---|
| `/fikri-mulkiyet:ilk-kurulum` | İlk kurulum (veya yeniden kurulum) mülakatını başlatır |
| `/fikri-mulkiyet:temizlik-taramasi [marka]` | İlk geçiş marka temizlik araştırması (TÜRKPATENT vb.) |
| `/fikri-mulkiyet:bulus-alimi [bildirim]` | Buluş bildirimleri için patentlenebilirlik ön taraması |
| `/fikri-mulkiyet:serbest-kullanim-triaji [ürün/kapsam]` | Freedom-to-operate (FTO) triyajı |
| `/fikri-mulkiyet:fm-madde-inceleme [dosya]` | Sözleşmelerdeki FM maddelerinin incelemesi |
| `/fikri-mulkiyet:acik-kaynak-inceleme [repo]` | Açık kaynak lisans uyumluluk denetimi |
| `/fikri-mulkiyet:portfoy` | Tescil ve yenileme takibi — yaklaşan yenilemeler |
| `/fikri-mulkiyet:dosya-calisma-alani` | Müşteri bazlı dosya yönetimi |
| `/fikri-mulkiyet:ozellestir` | Profildeki özel bir ayarı değiştirme |

*(İçerik kaldırma ve İhlal ihtarı gibi B kademesi yetenekler Türk hukukuna uyarlanmak üzere beklemededir.)*

## Ajanlar (Agents)

| Ajan | Ne İzler | Varsayılan Ritim |
|---|---|---|
| **fm-yenileme-izleyici** | Portföy sicilini kontrol ederek önümüzdeki 90 gün içinde yapılması gereken yenileme/harç ödemesi bildirimlerini yapar | Haftalık |

## Dosya Yapısı

```
fikri-mulkiyet/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Şablon
├── README.md
├── agents/
│   └── fm-yenileme-izleyici.md
├── skills/
│   ├── ilk-kurulum/
│   ├── temizlik-taramasi/
│   ├── bulus-alimi/
│   ├── serbest-kullanim-triaji/
│   ├── fm-madde-inceleme/
│   ├── acik-kaynak-inceleme/
│   ├── portfoy/
│   ├── dosya-calisma-alani/
│   └── ozellestir/
└── hooks/hooks.json
```
