---
name: ilk-kurulum
description: İlk kurulum görüşmesi — izleme listenizi oluşturur, politika kütüphanesini indeksler ve önemlilik (materiality) eşiğinizi öğrenir, böylece izleyici sistem gürültü yerine sinyal üretir. Temiz kurulumda, yeniden yapılandırmada (--redo) veya bağlantıların çalışıp çalışmadığını kontrol ederken (--check-integrations) kullanın.
argument-hint: "[--redo | --check-integrations]"
---

# /ilk-kurulum

1. `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` dosyasını kontrol edin. Eğer yapılandırılmış bir CLAUDE.md (içinde `[YER_TUTUCU]` olmayan) varsa ancak sadece eski önbellek yolunda bulunuyorsa, yapılandırma yoluna kopyalayın. `--check-integrations` kullanılmışsa, görüşmeyi atlayın ve sadece Bölüm 0 entegrasyon kontrolünü yeniden çalıştırıp tabloyu güncelleyin.
2. Aşağıdaki görüşme iş akışını kullanın. Görüşme (Önce Bölüm 0 — rol + entegrasyonlar — ardından izleme listesi): Hangi kurumlar, politikaların nerede tutulduğu, neyin önemli olduğu.
3. Politika klasörünü bağlayın. Politikaları indeksleyin.
4. `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` dosyasına (gerekirse üst dizinleri oluşturarak) izleme listesi + önemlilik eşiğini yazın.

Entegrasyonları kontrol ederken: sadece MCP araç çağrısı gerçekten başarılı olursa ✓ verin. Yapılandırılmış ama test edilmemiş bağlayıcılar ⚪ ile işaretlenmeli ve onaylama için kısa bir yönerge içermelidir.

---

## Amaç

Kurumlar sürekli yayın yapar (Resmî Gazete, kurum duyuruları vb.). Ancak bunların çoğu sizin için önemli değildir. Bu görüşme, hangi kurumları izleyeceğini ve sizin için "önemli" (material) olanın ne anlama geldiğini öğrenir.

## İlk Kurulum Kontrolü

`~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` oku:
- **Yoksa** → görüşmeyi başlat.
- **`<!-- KURULUM BURADA DURAKLATILDI: -->` içeriyorsa** → kullanıcıyı selamla ve kaldığı bölümden devam etmeyi teklif et.
- **`[YER_TUTUCU]` içeriyorsa** → şablon tamamlanmamıştır; sıfırdan başlama teklif et.
- **Doluysa** → zaten yapılandırılmıştır; `--redo` değilse atla.

## Ortak Şirket Profili Kontrolü

`~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasını arayın. Varsa okuyun. Yoksa şirket hakkında temel soruları sorarak oluşturun.

## Kurulum Kapsamı (Install Scope)

Mevcut dizinin kullanıcı ana dizini (home directory) dışında olduğunu fark ederseniz (proje odaklıysa) uyarı verin ve yerel dosyaları göremeyebileceğinizi hatırlatın.

## Görüşme Başlamadan Önce

Kısa ön bilgi (3-4 satır):
> **`mevzuat-takibi`, mevzuat değişikliklerini izleyen, boşlukları değerlendiren ve uyum yükümlülüklerini yöneten kişiler içindir.**
> **2 dakika** içinde rolünüz, pratik ayarınız ve temel mevzuat rejiminiz alınır. **15 dakika** içinde tam izleme listesi, önemlilik eşikleri, besleme ritmi ve politika kütüphanesi yapılandırılır. Hızlı mı, tam kurulum mu istersiniz? (Sonradan `--full` diyerek yükseltebilirsiniz.)

## Görüşme Akışı

**Adım 1: Rol ve Entegrasyonlar (Part 0)**
Kimin kullanacağını sorun (Avukat, avukat olmayan vb.). Entegrasyonları kontrol edin (Resmî Gazete/mevzuat.gov.tr varsayılan kabul edilir). Pratik ayarını (şirket-içi, hukuk bürosu vb.) sorun.

**Adım 2: İzleme Listesi (Watchlist - Part 1)**
Hangi düzenleyici kurumlar izlenecek? (SPK, BDDK, Rekabet Kurumu, Kişisel Verileri Koruma Kurumu (KVKK), Ticaret Bakanlığı, Merkez Bankası vb.) Neden izleniyor? 

**Adım 3: Önemlilik Eşiği (Materiality - Part 2)**
Neyin acil (hemen haber ver), neyin haftalık bültenlik, neyin bilgi amaçlı (FYI) olduğunu sorun:
- Taslak yönetmelik, yeni kanun yayımlanması.
- Kurul cezaları (Sektörünüzde veya başka sektörde).
- Rehber veya ilke kararları yayınlanması vb.

**Adım 4: Politika Kütüphanesi (Part 3)**
Politikalar nerede tutuluyor? Hangi mevzuatın hangi politikanızı etkilediğini bulabilmemiz için bağlantı veya klasör yolu isteyin. Kimin sorumlu olduğunu sorun.

**Adım 5: Besleme (Feed) Kaynakları (Part 4)**
Resmî Gazete günlük kontrol edilir. İlgili kurumların siteleri veya Lexpera, Kazancı gibi entegrasyonlar varsa öğrenilir. 
Görüş (comment) dönemi: Taslak mevzuata itiraz veya görüş bildirme süreci (örn. ilgili kamu kurumuna taslak görüşü) takip edilecek mi?

## Profilin Yazılması

Şablona göre `CLAUDE.md` dosyasını oluşturun. İzleme listesi, önemlilik eşikleri, besleme yapılandırması bloklarını oluşturun.
Kurulum bittikten sonra kullanıcının deneyebileceği bazı komutları (örn. `/mevzuat-takibi:mevzuat-besleme-izleyici`) önerin.
