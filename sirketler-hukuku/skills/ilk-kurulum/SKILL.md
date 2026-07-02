---
name: ilk-kurulum
description: >
  Kurum için ilk kurulum mülakatı veya işlem bazında bağlam için --new-deal.
  Modülerdir: Hangi pratik alanlarının (M&A, Kurul & Sekreterya, Halka Açık Şirket,
  Şirket Yönetimi) geçerli olduğunu belirler, ardından her aktif modül için hedefe
  yönelik sorular sorar ve eklenti yapılandırmasına yalnızca ilgili bölümleri yazar.
  İlk kurulumda, CLAUDE.md hâlâ [YER_TUTUCU] işaretleri içerdiğinde, yeni bir işleme
  başlarken veya bir modülü tazelemek/entegrasyonları kontrol etmek için kullanın.
argument-hint: "[--redo | --new-deal | --check-integrations | --module [m&a | kurul | halka-acik | sirket-yonetimi]]"
---

# /ilk-kurulum

1. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` dosyasını kontrol et. `--new-deal` ise doğrudan işleme özel kuruluma (per-deal setup) geç. `--check-integrations` ise mülakatı atla — yalnızca Bölüm 0 "Ne bağlı?" kontrolünü yeniden çalıştır ve `## Mevcut entegrasyonlar` tablosunu yenile. Yoklama yaparken: yalnızca bir MCP araç çağrısı gerçekten başarılı olursa ✓ bildir. Yapılandırılmış-ama-test-edilmemiş bağlayıcılar nasıl doğrulanacağına dair tek satırlık bir açıklamayla ⚪ olarak işaretlenmeli.
2. Aşağıdaki mülakatı çalıştır (önce Bölüm 0 — rol + entegrasyonlar — sonra modüller).
3. Tohum belgeler: due diligence talep listesi + bir önceki sorun/bulgu notu (issues memo).
4. Şunları çıkar: kategoriler, eşikler, not formatı, AI araç konfigürasyonu.
5. Göç: `~/.claude/plugins/cache/claude-for-legal-turkish/sirketler-hukuku/*/CLAUDE.md` yolunda dolu (yer tutucu olmayan) bir CLAUDE.md varsa ve config yolunda yoksa, onu config yoluna kopyala ve kullanıcıya neyin kopyalandığını söyle.
6. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` dosyasını yaz. `--new-deal` (yeni işlem) için `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/deals/[kod]/deal-context.md` dosyasını yaz.

---

## Amaç

Şirketler hukuku rolleri diğer kurum içi işlevlerin çoğundan daha fazla farklılık gösterir. 50 kişilik bir girişimin tek BHM'si (Baş Hukuk Müşaviri) M&A'yi yönetir, pay defterini tutar ve YK sekreteryasını yürütür. BİST 100 şirketindeki bir şirket avukatı yalnızca KAP bildirimlerini ve SPK süreçlerini yürütebilir. Bu mülakat hangi alanların sizin için aktif olduğunu bulur ve yalnızca ilgili pratik profilini oluşturur.

## İlk-kurulum kontrolü

`~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` dosyasını oku:
- **Mevcut değil** → görüşmeyi başlat.
- **`<!-- KURULUM BURADA DURAKLATILDI: -->`** içeriyorsa → kullanıcıyı selamlayıp o bölümden devam etmeyi teklif et.
- **Durdurma yorumu olmadan `[YER_TUTUCU]` işaretleri içeriyorsa** → şablon hiç tamamlanmamış; sıfırdan başlamayı ya da yer tutucuların başladığı yerden devam etmeyi teklif et.
- **Dolu (yer tutucu yok, durdurma yorumu yok)** → zaten yapılandırılmış; `--redo` veya `--module [isim]` yoksa geç.

Şablon yapısı `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`'de bulunur — onu bölüm iskeleti olarak kullan.

- `--redo` — tam yeniden görüşme, tüm bölümlerin üzerine yazar
- `--module [m&a | kurul | halka-acik | sirket-yonetimi]` — tek bir modülü ekler veya tazeler
- `--new-deal` — kurum kurulumunu atlar, doğrudan işleme-özel (per-deal) bağlama geçer (yalnızca M&A modülü)

---

## Paylaşılan şirket profilini kontrol et

`~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasına bak.

- **Mevcutsa:** Oku. Tek satırlık onay göster: "Siz [ad], [çalışma ortamı], [şirket]'te, [sektör]'de, [yargı çevreleri]'nde faaliyet gösteriyorsunuz. Doğru mu? (Değiştirmek için 'güncelle' deyin.)" Onaylanırsa şirket sorularını geç — doğrudan eklentiye özgü sorulara geç.
- **Mevcut değilse:** Bu kullanıcının kurduğu ilk eklenti olacak. Yönlendirmeden sonra şirket sorularını sor, paylaşılan profile yaz (şablon: `references/company-profile-template.md`), sonra devam et. "Şirket profilinizi kaydettim — diğer eklentiler bunu okuyacak" de.

## Kurulum kapsamı kontrolü

Eğer çalışma dizini proje içindeyse (ev dizini değilse), uyar: "Bu eklenti proje kapsamlı kurulmuş görünüyor..." Kullanıcıdan onay al veya duraklat. Çalışma dizini ev diziniyse geç.

## Görüşme başlamadan önce

Aşağıdaki yönlendirmeyi ver (kısa ve öz):

> **`sirketler-hukuku` eklentisi, M&A işlemlerini, yönetim kurulu ve şirket sekreteryasını, halka açık şirket uyumunu ve şirket (TTK/MERSİS) yönetimini destekleyenler içindir.** Senin alanın değil mi? `/eklenti-merkezi:ilgili-eklentiler` kullanabilirsin.
>
> **2 dakika** sana rolünü, çalışma ortamını, modül seçimini ve (M&A, kurul vb.) taslak formatların için çalışan varsayılanları sağlar. **15 dakika** gerçek önemlilik eşiklerini, ev tarzı tutanak ve onay formatlarını tohum belgelerden çeker, yetki merdivenini ve eskalasyon matrisini ekler.
>
> Hızlı mı, tam mı? (İstediğin zaman `--full` ile yükseltilebilir.)

Seçim yapıldıktan sonra eklentinin ne yapacağını anlat:
"Bu kurulum mülakatı, eklentinin genel bir şablon yerine sizin çalıştığınız gibi çalışmasını sağlar. Verdiğiniz yanıtlardan taze bir profesyonel profil oluşturulur."

---

## Görüşme Temposu
- Yazılı belge varsa istemeyi unutma (diligence talep listesi, YK kararı şablonu vb.).
- Alt parçaları sayarak tek seferde 2-3 soru sor.
- Dosya yüklemeleri için bekle. Sessiz boşluklarla profil yazma.

---

## Görüşme

### Bölüm 0: Bunu kim kullanıyor ve ne bağlı?

#### Bunu kim kullanıyor?
- Avukat veya hukuk profesyoneli
- Avukat erişimi olan avukat olmayan
- Avukat erişimi olmayan avukat olmayan (Uyarı yap: Çıktılar araştırma notudur, yasal bir yargı değildir. Avukat bulma referansları ver.)

#### Ne bağlı?
VDR (Box, Intralinks vs.), YK Portalı (Diligent vb.), DYS, Slack. Bağlantıları test et. Yalnızca test başarılıysa ✓ bildir.

#### Çalışma ortamı
- Bağımsız / küçük büro (hiyerarşi yok — kime danışırsın diye sor)
- Orta / büyük büro (eskalasyon zinciri, onay eşikleri)
- Şirket içi (eskalasyon matrisi, BHM kim)
- Kamu / Hukuki yardım / Klinik (gözetim yapısı)
- Hiçbiri (açıklat)

### Bölüm 0.5: Modül seçimi
- 1. M&A
- 2. Kurul & Sekreterya
- 3. Halka Açık Şirket
- 4. Şirket Yönetimi

### Bölüm 1: Şirket profili (Her zaman)
Delegasyon (yetki) matrisi belgesi iste. Yoksa:
- Şirket adı, sektör, aşama, yargı çevresi.
- Ekip büyüklüğü.
- Eskalasyon: Bir bulgu bandın üstündeyse kime gider (BHM, ortak, iş birimi lideri)?

### Bölüm 2M: M&A modülü (Aktifse)
- Alıcı taraf mı, satıcı taraf mı?
- Standart diligence talep listeniz veya geçmiş bir bulgu notunuz (issues memo) var mı? Varsa yüklet.
- Yoksa: Önemlilik eşiğiniz (materiality threshold) nedir? (Örn: Tüm sözleşmeler mi, >₺1M olanlar mı?)
- VDR ne kullanıyorsunuz? AI inceleme aracı kullanıyor musunuz?
- Satıcı taraf iseniz: VDR'a neyin gireceğine kim karar verir?
- Kapanış kontrol listesi (closing checklist) nerede yaşar (Excel, Smartsheet)?
- Ekibe brifing nasıl verilir?

### Bölüm 2B: Kurul & Sekreterya modülü (Aktifse)
- Rolünüz: YK Sekreteri / Raportör / Danışman Avukat?
- Kurul büyüklüğü, komiteler? Toplantı sıklığı?
- TTK m.390 vd. uyarınca tutanak formatı (eylem tutanağı mı, detaylı tartışma mı)?
- TTK m.390/7 kapsamında (oybirliğiyle yazılı karar) onayı ne sıklıkla ve ne için kullanırsınız?
- Tohum belgeler: 5-6 geçmiş toplantı tutanağı yüklet (gerçek taslak formatı çıkarılacak). Yazılı onaylar için emsal deposu var mı? (Gelecekte `/yazili-onay` yeteneği buradan beslenecek.)

> **Önemli (Türk Hukuku):** YK kararları, genel kurul süreçleri TTK çerçevesinde yürür. Belgelerde Delaware referansı çıkarsa, TTK'ya uygun şekilde ayarlanmalıdır.

### Bölüm 2P: Halka Açık Şirket modülü (Aktifse)
- Borsa (örn. BİST), mali yıl sonu.
- Özel durum açıklamaları (KAP) için komite var mı?
- İçeriden öğrenenlerin ticareti kısıtlamaları (karartma dönemleri)? Kimleri kapsar?

### Bölüm 2E: Şirket Yönetimi modülü (Aktifse)
- Organizasyon şeması (org chart) veya şirket listesi yüklet.
- Yoksa: Kaç aktif tüzel kişi? Temel yargı çevreleri? Sicil süreçlerini kim yürütür (iç ekip, dış büro)?

---

## Yazdıktan sonra
Pratik profilini yaz (`CLAUDE.md`). Eksik kalan, yer tutucu olan alanları son kez sor. M&A tohum belgesi alınmadıysa tekrar hatırlat.

Son olarak eklentinin yapabildiklerini göster:
- M&A due diligence sorun çıkarma (`/sirketler-hukuku:due-diligence-sorun-cikartma`)
- Kapanış kontrol listesi (`/sirketler-hukuku:kapani-kontrol-listesi`)
- YK toplantı tutanağı ve yazılı onay (`/sirketler-hukuku:yazili-onay`)
- Şirket uyum takipçisi (`/sirketler-hukuku:entegrasyon-yonetimi`)

Araştırma aracı bağlama uyarısını yap (Lexpera, Kazancı, UYAP).
"Pratik profiliniz öğrenir. Eklentiyi kullandıkça ve düzelttikçe kendi tarzınıza yaklaşacaktır." de.

---

## İşleme Özel Kurulum (Per-deal setup, `--new-deal`)
Yalnızca M&A modülü içindir.
- İşlem kod adı
- Taraf (alıcı / satıcı)
- Hedef/Devralan adı
- VDR konumu
- Anlaşma lideri
- İmza ve Kapanış tarihi beklentisi
- Dış avukat iletişim bilgisi

Bunu `deals/[kod-adi]/deal-context.md` olarak yaz.

---

## Başarısızlık Modları
- **ABD bağlamına düşme:** Yönetim kurulu veya şirket kurulum süreçlerinde Delaware vb. ezberlerini TTK/MERSİS gerçekliğiyle çerçevele.
- **Tüm modülleri aktif varsayma:** Önce sor.
- **Satıcı tarafı alıcı tarafın tersi gibi düşünme:** Satıcı tarafta due diligence defansiftir, bilgi dışarı akışını kontrol eder.
- **Tohum belge istemeyi unutma:** M&A profilinin en değerli kısmı önceki bulgu notundan (issues memo) format çekmektir.
