---
name: ilk-kurulum
description: >
  Fikri mülkiyet pratiğinizi öğrenmek ve pratik profilinizi oluşturmak için
  ilk kurulum mülakatını yürütün. Pratik profili eksik olduğunda veya hala 
  yer tutucular (placeholders) içerdiğinde ilk kurulumda kullanın. Yeniden 
  başlatmak için --redo ile veya bir MCP bağlantısı ekledikten/kaldırdıktan sonra 
  entegrasyonları yeniden sınamak için --check-integrations ile çalıştırın. 
  Taze bir kurulumda çalışması gereken TEK yetenek budur.
argument-hint: "[--redo ile zaten yapılandırılmış eklentide yeniden çalıştırın] [--check-integrations ile sadece entegrasyonları sınayın]"
---

# /ilk-kurulum

İlk kurulum (cold-start) mülakatını çalıştırır. İlk çalıştırma `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` dosyasını yazar; `--redo` ile yapılan sonraki çalıştırmalar yeniden mülakat yapar ve üzerine yazmadan önce farkı (diff) gösterir.

## Talimatlar

1. **Mevcut durumu kontrol edin:** `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` dosyasını okuyun. Eğer `[YER_TUTUCU]` veya `[Kurum Adınız]` içeriyorsa, yeni mülakatla devam edin. Zaten doluysa ve `--redo` belirtilmemişse şunu sorun: "Görünüşe göre zaten kurulum yapmışsınız. Mülakatı tekrar çalıştırmak ister misiniz? Bu işlem CLAUDE.md'nin üzerine yazacaktır (önce farkları göstereceğim)."

2. **Aşağıdaki mülakat akışını izleyin.**

3. **Pratik belgelerini isteyin:** Portföy listesi (veya FM yönetim dışa aktarımı), marka kılavuzları, ihtarname şablonu(ları), ihlal müdahale rehberi, açık kaynak (OSS) politikası. Dosya yollarını, bulut bağlantılarını veya belge içeriklerini kabul edin.

4. **Paylaşılan belgeleri okuyun** ve fiili pozisyonları çıkarın — ihlal sınırları, onay zinciri, marka izleme ayarları, OSS kuralları. İfade edilen pozisyonlarla şablonların/rehberlerin aslında gerektirdiği arasındaki farkları not edin.

5. **`~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md`** dosyasını yazın (gerekirse ebeveyn dizinleri oluşturun). Mümkün olduğunca avukatın kendi kelimelerini kullanın.

6. **Portföy sicilini tohumlayın:** Kullanıcı bir portföy dışa aktarımı veya FM yönetim sistemi erişimi paylaştıysa `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/portfolio.yaml` dosyasına yazın. Hiçbir şey paylaşılmadıysa, daha sonra doldurulmak üzere boş bırakın.

7. **Özeti gösterin ve sonraki adımları önerin:**
   - "İşte duyduklarım — CLAUDE.md yazıldı. Neleri yanlış anladım?"
   - Test önerin: "Temizlik taramasına (clearance) bir marka atmak veya portföy sicilinde yaklaşan yenilemeleri görmek ister misiniz?"

## `--check-integrations`

Entegrasyon durumu kontrolünü (FM yönetim sistemi, araştırma, belge depolama, Slack vb.) yeniden çalıştırır ve profil dosyasındaki entegrasyonlar bölümünü günceller. Mülakatı yeniden yapmaz.

## Amaç

Bu IP (FM) pratiği ile ilk defa karşılaşıyorsunuz. İşiniz, soyut olarak "Fikri Mülkiyet" işinin nasıl yapıldığını değil, *onların* işi nasıl yaptığını öğrenmek ve bunu canlı bir pratik profiline yazmaktır. Avukat, bu konuşmadan tam olarak doğru soruları soran keskin bir paralegali işe almış gibi hissetmelidir. Hiçbir zaman bir YAML dosyası görmemeliler.

## "İlk kurulum" (Cold start) ne demek?

Eğer CLAUDE.md dosyası yoksa veya yer tutucular içeriyorsa mülakatı başlatın. Varsa ve doluysa atlayın.
Şablon yapısı `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` konumunda yaşar. Profil yazarken şablonu kullanın.

## Ortak Şirket Profili Kontrolü

`~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasına bakın. Varsa okuyun ve "Siz [Şirket/Büro]'dan [Kişi]'siniz, değil mi?" diyerek onay alın. Yoksa, şirkete özgü soruları sorun ve o ortak profile yazın ki diğer eklentiler aynı soruları sormasın.

## Mülakat Akışı

### Açılış

> Sizin Fikri Mülkiyet asistanınız olacağım. Herhangi bir taslak hazırlamadan, tarama (clearance) yapmadan veya portföyünüze dokunmadan önce işlerinizi aslında nasıl yürüttüğünüzü öğrenmek istiyorum — genel geçer en iyi uygulamaları değil, *sizin* uygulama alanlarınızı, ihlal politikanızı, onay zincirinizi ve toleransınızı.
> Hızlı ayar 2 dakika sürer. Tam ayar ise yaklaşık 10-15 dakika alır (belgelerinizi de eklersiniz). Hızlı mı tam mı?

### Bölüm 0: Kim kullanıyor ve Neler bağlı?

- **Kullanıcı Rolü:** Avukat/Hukuk profesyoneli mi? Marka/Patent vekili mi? Avukat erişimi olan uzman mı? Yoksa tek başına mı?
- **Uygulama Alanı Karışımı:** Marka? Patent? Telif? Ticari Sır? Açık Kaynak? Tümü? (Buna göre sonraki soruları filtrele).
- **Mevcut Entegrasyonlar:** Lexpera, Kazancı, Slack, Google Drive, vb. kurulu mu kontrol et.

### Bölüm 1: Çalışma Ortamı
Şirket içi? Özel Hukuk Bürosu? Kurum/Kamu? (Hiyerarşi ve onay zincirini belirler).

### Bölüm 2: Yargı Çevresi ve Coğrafya
- **Tescillerin bulunduğu yerler:** TÜRKPATENT, WIPO/Madrid, EUIPO, USPTO?
- **İhlalleri takip ettiğiniz yerler:** Türkiye, Küresel?

### Bölüm 3: Pratik Belgeleri İsteme
- Portföy listesi
- Marka rehberi
- İhtarname şablonları (Not: 5651 sayılı kanun veya 6769 s. SMK uyarınca)
- Açık kaynak (OSS) politikası
Belgeleri okuyup içindeki kuralları çıkarın.

### Bölüm 4: İhlal ve Yaptırım Yaklaşımı
(Sadece Marka/Patent/Telif uygulayanlara sor)
- Yaklaşım: Agresif (hemen ihtarname), Ölçülü, Muhafazakar (sadece kesin kazanılacaksa).
- Mektup onay süreçleri: 5651 uyarısını (takedown) kim onaylar? İhtarnameyi kim onaylar? Davayı kim onaylar?

### Bölüm 5: Eskalasyon (Tırmandırma)
- Marka taramasında risk çıkarsa kime gider?
- FTO (Serbest kullanım) engelleyici bir patent bulursa kim karar verir?
- OSS lisans ihlali varsa kim çözer?

### Bölüm 6: Marka Koruması
- Özel olarak izlenen markalar var mı? Hangi izleme hizmeti (Corsearch, kurum içi vb.) kullanılıyor?

## Profilin Yazılması
Tüm cevapları toparlayıp `CLAUDE.md` dosyasına Türkçe şablona uygun şekilde yazın.
Yazdıktan sonra kullanıcıya "Bu eklenti ile ne yapmak istersiniz?" diyerek `temizlik-taramasi` veya `portfoy` gibi becerileri önerin.

*Not: DMCA veya İhlal İhtarname yeteneklerinin (B-kademesi) şu an tam aktif olmadığını, ancak taslakların normal prompt gibi oluşturulabileceğini belirtebilirsiniz.*
