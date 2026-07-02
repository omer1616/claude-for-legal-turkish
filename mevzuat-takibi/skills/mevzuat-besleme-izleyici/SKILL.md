---
name: mevzuat-besleme-izleyici
description: Mevzuat beslemelerini kontrol eder ve son kontrolden bu yana neyin yeni olduğunu, sizin önemlilik (materiality) eşiğinize göre filtreleyerek raporlar. Kullanıcı "beslemeleri kontrol et", "yeni ne var", "mevzuat güncellemesi" dediğinde, zamanlanmış ajan tarafından çalıştırıldığında veya sınıflandırma ve diff için bir mevzuat değişikliği manuel olarak yapıştırıldığında kullanın.
argument-hint: "[opsiyonel: --since TARİH]"
---

# /mevzuat-besleme-izleyici

1. `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` yükle → izleme listesi, önemlilik eşiği, besleme yapılandırması.
2. Aşağıdaki iş akışını kullan.
3. Her bir beslemeyi (feed) çek. Önemlilik (materiality) seviyesine göre filtrele.
4. Çıktı: Önemlilik kademesine göre sınıflandırılmış şekilde nelerin yeni olduğunu ver.

---

## Amaç

Beslemeleri çeker. Önemlilik eşiğine göre filtreler. Geriye kalanı çıktı olarak verir. Filtre, asıl değerdir — filtrelenmemiş beslemeler gürültüdür.

## Bağlam (Context) Yükleme

`~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` → izleme listesi, önemlilik eşiği, besleme yapılandırması, özet (digest) çıktı yolu (eğer ayarlanmışsa).

## İş Akışı

### Adım 0: Kapsam Kontrolü (Çekmeden önce)

Çekim işlemini başlatmadan önce CLAUDE.md'deki izleme listesini kontrol edin. Eksik veya mantıksız bir liste varsa kullanıcıyı `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` veya `/mevzuat-takibi:ilk-kurulum --redo` aracılığıyla uyarmayı düşünün. 

### Adım 1: Çekim (Pull)

**Aşama 1 — Ücretsiz beslemeler (Daima aktif)**

İzleme listesindeki her düzenleyici kurum için:
- **Resmî Gazete** / **mevzuat.gov.tr** → RSS, scraping veya doğrudan arama yeteneklerini kullanarak son kontrol tarihinden bu yana çıkan Kanun, KHK/CBK, Yönetmelik, Tebliğ ve Genelgeleri bulun. (Araç yoksa web araması kullanın, ancak etiketlemelere dikkat edin).
- **Doğrudan kurum RSS'i** — (örn. SPK bülteni, Rekabet Kurumu duyuruları, KVKK ilke kararları).

**Aşama 2 — Ücretli beslemeler (Eğer yapılandırılmışsa)**
Lexpera, Kazancı veya özel MCP'ler üzerinden güncellemeler aranır. Mükerrerleri eleyin.

**Sessiz Tamamlama (No silent supplement) Kuralı:** Eğer çekilen veriler azsa, sessizce modelin bilgisiyle veya onaysız bir web aramasıyla boşluğu doldurmayın. Seçenekleri (web araması vb.) sunun ve kullanıcıya bırakın.

**Kaynak Gösterimi (Source attribution):** Atıfları kaynağıyla etiketleyin: `[Resmî Gazete]`, `[SPK RSS]`, `[Lexpera]`, `[web araması — doğrulayın]`, `[model bilgisi — doğrulayın]`, `[kullanıcı tarafından sağlandı]`.

**Aşama 3 — Manuel Giriş (Manual entry)**
Eğer kullanıcı doğrudan metni yapıştırdıysa, çekimi atlayıp Sınıflandırma aşamasına geçin ve kaynağı "manuel giriş" yapın.

Çekim işleminden sonra zaman damgasını kaydedin. Bir sonraki kontrol buradan itibaren başlayacaktır.

### Adım 2: Sınıflandırma (Classify)

Her bir öğeye `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` dosyasına göre bir önemlilik kademesi atanır:

| Öğenin Türü | Eşiğe Göre Eşleşme |
|---|---|
| Kanun / Yönetmelik / Tebliğ (Nihai kural) | Genelde "daima önemli" (always material) |
| Taslak yönetmelik (NPRM) | Genelde "incelemeye değer" (review-worthy) — varsa görüş (comment) süresini not edin |
| Kurul Kararı / Ceza (Enforcement) | Kendi sektöründeyse → daima önemli; ilgili sektörse → incelemeye değer; hiçbiri → bilgi amaçlı (FYI) veya atla |
| İlke Kararı / Rehber | İncelemeye değer |
| Kurum yetkilisinin konuşması / blog | Eşiğe göre FYI veya atla |

Görüş bildirme süresi (Comment deadline) takibi Türkiye'de (ABD'deki 60 günlük NPRM süreci kadar katı olmasa da) BDDK, SPK, Rekabet taslakları için vardır. Taslak yayımlandıysa görüş süresi varsa not edin.

### Adım 3: Zenginleştirme (Enrich)

FYI seviyesi üzerindeki her öğe için:
- Tek satırlık özet (ne değişti)
- Burada neden önemli olabileceği (ilgi kancası — "bu sizin yaptığınız [X uygulaması] hakkında")
- Kaynağa bağlantı
- Varsa yürürlük tarihi veya görüş/itiraz bildirme son tarihi

FYI öğelerini tek tek özetlemeyin — sadece sayısını verin.

## Çıktı (Output)

Özet varsayılan olarak sohbete gelir. **Aynı zamanda paylaşılabilir bir dosyaya da yazın** (kullanıcı açıkça engellemediyse).
Dosya Yolu: `~/regulatory-legal-digests/mevzuat-ozeti-YYYY-AA-GG.md`. Eğer bugün için varsa üzerine yazmayın, altına yeni zaman damgasıyla ekleyin.

```markdown
[İŞ ÜRÜNÜ BAŞLIĞI — `CLAUDE.md` profilindeki Role göre şekillenir (Gizli-Avukat İş Ürünü veya Araştırma Notu)]

## Mevzuat Besleme Kontrolü — [tarih]

**Dönem:** [son kontrol] ile [şimdi] arası
**Kontrol edilen beslemeler:** [Resmî Gazete, SPK RSS vb.]
**Bulunan öğe:** [N] toplam

### Alt Çizgi (Bottom line)
[N adet boşluk (gap) [tarih]'e kadar işlem gerektiriyor — ilk 3: X, Y, Z]

### 🔴 Daima Önemli
**[Kurum] — [Başlık]**
[Tek satırlık özet]. [İlgi kancası]. Yürürlük tarihi [tarih].
[Bağlantı]
→ Öneri: Etkilenmesi muhtemel olan [ilgili politika] için /mevzuat-takibi:politika-farki çalıştırın.

### 🟡 İncelemeye Değer
**[Kurum] — [Başlık]**
[Özet]. [İlgi]. [Varsa son tarih].
[Bağlantı]

### 📝 Bilgi Amaçlı (FYI)
[N] adet öğe — [başlıklar + bağlantılar, özet yok]

---

**Son kontrol güncellendi:** [zaman damgası]

---

**Atıfları güvenmeden önce doğrulayın.** Buradaki mevzuat atıfları yapay zeka tarafından oluşturulmuş olabilir ve birincil kaynaklardan kontrol edilmemiş olabilir. Harekete geçmeden önce Resmî Gazete veya ilgili kurumun sitesinden teyit edin. Etiketler size kaynağı gösterir (`[web araması — doğrulayın]` gibi).
```

## Yapılandırma Eksikse (Config Fallbacks)

- **İzleme listesi boşsa:** Durun ve `/mevzuat-takibi:ilk-kurulum --redo` isteyin.
- **Önemlilik eşiği boşsa:** Varsayılan kademeleri kullanın ve kullanıcıyı uyarın.

## El Değiştirme (Handoff)

- **policy-diff (politika-farki):** Muhtemel bir politika etkisine sahip "daima önemli" öğe → fark analizi teklif edin.
- **gap-surfacer (bosluk-cikarici):** Bir boşluk bulursa → takip edilir.

## Sonraki Adımlar Karar Ağacı

Çıktıyı oluşturduktan sonra kullanıcıya (Taslakla, Yukarı Taşı, Daha fazla bilgi al, Bekle) şeklindeki standart karar ağacını sunun.
