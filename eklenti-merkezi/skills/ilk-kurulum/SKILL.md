---
name: ilk-kurulum
description: >
  Topluluk (community) hukuki eklentilerinin başlangıç paketini öneren ve kuran pratik profili görüşmesi. Bu, tüm ekosistem için GERÇEK ilk kurulumdur — ne tür bir hukukçu olduğunuzu sorar ve önce neleri kuracağınızı önerir. Yeni kurulumda, kullanıcı "beni başlat" veya "ne kurmalıyım" dediğinde veya bir MCP bağlayıcısı ekleyip çıkardıktan sonra entegrasyon-kullanılabilirlik kontrolünü yeniden çalıştırmak için kullanın.
argument-hint: "[--yeniden] [--entegrasyon-kontrolu]"
---

# /ilk-kurulum

1. `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` dosyasını kontrol edin. Eğer yapılandırma yolunda değil de `~/.claude/plugins/cache/claude-for-legal-turkish/eklenti-merkezi/*/CLAUDE.md` yolunda dolu bir CLAUDE.md (hiç `[YER TUTUCU]` işareti olmayan) varsa, onu yapılandırma yoluna kopyalayın ve kullanıcıya neyin taşındığını söyleyin.
2. Aşağıdaki iş akışına göre Bölüm 0'ı (rol + entegrasyon kontrolü), ardından beş soruyu (pratik türü, sektör, ekip, araç konforu) çalıştırın.
3. Profili kayıt (registry) eklentileriyle eşleştirin. Başlangıç paketi önerin.
4. Önerilen her eklentinin SKILL.md özetini gösterin. Kullanıcı seçsin.
5. Seçilen eklentileri kurun. `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` dosyasını (gerektikçe üst dizinleri oluşturarak) `## Bunu kim kullanıyor`, `## Kullanılabilir entegrasyonlar`, profil + kurulu listesi ile YAZIN.

**`--entegrasyon-kontrolu`:** Sadece Bölüm 0 entegrasyon-kullanılabilirlik kontrolünü yeniden çalıştırır. Rolü veya pratik profilini dokunmadan `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` içindeki `## Kullanılabilir entegrasyonlar` tablosunu günceller. Bir MCP bağlayıcısı ekledikten veya çıkardıktan sonra kullanın.

Sorgularken: sadece bir MCP araç çağrısı gerçekten başarılı olduysa ✓ bildirin. Yapılandırılmış ama test edilmemiş bağlayıcılar, onaylamak için tek satırlık bir "nasıl yapılır" açıklamasıyla ⚪ olarak işaretlenmelidir. Asla sadece `.mcp.json` beyanlarına dayanarak ✓ bildirmeyin — bu, kullanıcıları bir şeyin bağlı olmadığı halde bağlı olduğunu düşünmeye sevk eder.

---

## İlk-kurulum kontrolü

Şurayı okuyun: `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md`:
- **Yoksa** → görüşmeyi başlatın.
- **`<!-- KURULUM ŞURADA DURAKLATILDI: -->` içeriyorsa** → kullanıcıyı selamlayın ve o bölümden devam etmeyi teklif edin.
- **`[YER TUTUCU]` işaretleri içeriyor ancak duraklatma yorumu yoksa** → şablon hiçbir zaman tamamlanmamıştır; sıfırdan başlamayı veya yer tutucuların başladığı yerden devam etmeyi teklif edin.
- **Dolu (yer tutucu yok, duraklatma yorumu yok)** → zaten yapılandırılmış; `--yeniden` (redo) denilmedikçe atlayın.

Şablon yapısı `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`'de yaşar — bunu bölüm iskelesi olarak kullanın. Tamamlanan pratik profilini yapılandırma yoluna yazın, gerektiğinde üst dizinleri oluşturun. Eğer eski önbellek yolunda `~/.claude/plugins/cache/claude-for-legal-turkish/eklenti-merkezi/*/CLAUDE.md` bir CLAUDE.md varsa ama burada yoksa, öne doğru kopyalayın.

## Paylaşılan şirket profili için kontrol

Şunu arayın: `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md`.

- **Mevcutsa:** Okuyun. Tek satırlık bir onay gösterin: "Siz [şirket]'te, [sektör]'de, [yargı çevresi]'nde faaliyet gösteren [isim]'siniz, [pratik ortamı]. Doğru mu? (Veya paylaşılan profili değiştirmek için 'güncelle' deyin.)" Onaylanırsa şirket sorularını atlayın — doğrudan eklentiye özel sorulara geçin.
- **Yoksa:** Bu kullanıcının kurduğu ilk eklenti siz olacaksınız. Yönlendirme ve ayrımdan sonra, şirket sorularını sorun ve bunları paylaşılan profile (eklenti kökündeki `references/company-profile-template.md` şablonuna göre) yazın, ardından eklentiye özel sorularla devam edin. Kullanıcıya şunu söyleyin: "Şirket profilinizi kaydettim — diğer hukuki eklentiler bunu okuyacak ve bu soruları atlayacaktır."

Paylaşılan profile ait (ve varsa YENİDEN SORULMAMASI GEREKEN) şirket soruları: pratik ortamı, şirket adı, sektör, ne-satıyorsunuz, boyut, yargı çevreleri, düzenleyiciler, risk iştahı, eskalasyon isimleri. Eklentiye özel sorular (playbook pozisyonları, inceleme çerçevesi, ev tarzı, gözetim modeli vb.) eklenti bazında kalır.

## Amaç

Bu eklenti uygulama mağazasıdır. İlk-kurulum görüşmesi ise devreye alma öneri motorudur — ne yaptığınızı sorar, bir başlangıç paketi önerir, seçtiğinizi kurar.

Diğer ilk-kurulumların aksine, bu kısadır. Beş soru, bir öneri, bitti.

## Kurulum kapsamı kontrolü

Oryantasyondan önce, çalışma dizininin bir proje içinde (kullanıcının ana dizini değil) olduğunu fark ederseniz, işaretleyin. Bir kez söyleyin:

> **Dikkat — bu eklenti proje kapsamlı olabilir, bu da sadece [mevcut dizin] içindeki dosyaları okuyabileceğim anlamına gelir. Başka yerlerden (İndirilenler, Belgeler, Dropbox) belge okumamı isterseniz, bunun yerine kullanıcı kapsamlı kurun. Proje kapsamıyla devam edebilirsiniz, ancak dosyaları bu klasöre taşımanız gerekir.**

Kullanıcıdan devam etmeden önce onaylamasını isteyin: proje kapsamıyla devam et, veya kullanıcı kapsamlı yeniden kurmak için durakla. Çalışma dizini kullanıcının ana diziniyse, bu kontrolü sessizce atlayın.

## Görüşme başlamadan önce

Önce bu girişi gösterin (3-4 kısa satır, daha fazla değil):

> **`eklenti-merkezi`, topluluk katkılı hukuki eklentileri (skills) bulmak, kurmak ve yönetmek içindir.** Bir pratik alanı iş akışı mı arıyorsunuz? Doğrudan `dava-takibi`, `ticari-hukuk` gibi eklentilerden birini kurun; ne olduğunu görmek için `/eklenti-merkezi:kayit-tarayici` çalıştırın.
>
> **2 dakika** ile rol ve pratik alanı belirlenir — kayıt izleme listesi, güncelleme temposu ve varsayılan izin verilenler (allowlist) listesi ayarlanır. **15 dakika** ile pratiğinize uygun hale getirilmiş bir başlangıç paketi, güvenilen kaynaklar politikası (dağıtım bağlamınızdan tohumlanmış) ve öneriler için sektör/ekip büyüklüğü sinyali eklenir.
>
> Hızlı mı yoksa tam mı? (İstediğiniz zaman `/eklenti-merkezi:ilk-kurulum --tam` ile yükseltebilirsiniz.)

## Kullanıcı hızlı veya tam olanı seçtikten sonra

Kullanıcı seçtikten sonra onları yönlendirin. Kendi sesinizle şunları kapsayın:

- **Bu eklentinin koruduğu şeyler:** pratik profiliniz (güvenilen kaynaklar, güncelleme tercihleri, dağıtım bağlamı), kurulumları denetleyen bir `allowlist.yaml` ve kurulum günlüğü.
- **Bu kurulumun yaptığı şey:** kullanıcının hukuki eklentileri keşfetmesine, kurmasına ve değerlendirmesine yardımcı olur — herhangi bir şeyin iş akışına dokunmasından önce pratik profili odaklı bir başlangıç paketi ve kalite kontrolü. Pratik profilini ve güncelleme tercihlerini öğrenir ve eklentinin her defasında okuduğu düz metin dosyasına yazar. Her şey daha sonra değiştirilebilir.
- **Veri kaynakları:** kurulum, sadece kullanıcının cevaplarından taze bir pratik profili oluşturur. Kişisel Claude geçmişini veya diğer konuşmaları okumaz. Eğer bu konuşmada daha önce ilgili bir şey gündeme geldiyse (örneğin kullanıcı ekibinden bahsettiyse), profil içine katmadan önce sorun.

### Hızlı başlangıç veya tam kurulum — dallanma

**Hızlı başlangıç yolu:** sadece rolü ve pratik alan(lar)ını sorun. Diğer her şeye `[VARSAYILAN]` işaretleri koyarak config'i yazın. Şununla kapatın: "Tamam. Şimdi göz atıp kurmaya başlayabilirsiniz. Kayıt izleme listesi ve güncelleme temposu için makul varsayılanlar kullandım. İstediğiniz zaman tam görüşmeyi yapmak için `/eklenti-merkezi:ilk-kurulum --tam`, veya bir bölümü yeniden yapmak için `/eklenti-merkezi:ilk-kurulum --yeniden <bölüm>` komutunu çalıştırabilirsiniz."

**Tam kurulum yolu:** aşağıdaki mevcut görüşme akışı.

## Görüşme temposu

- **Cevabın bir yerlerde var olduğunu varsayın.** Şirket açıklaması, playbook vb. varsa doğrudan yazdırın veya link isteyin.
- Soruyu sorun ve bekleyin. Birden çok soruyu aynı anda sormayın (bir defada maks. 2-3 soru).
- Dilediği zaman "duraklat" diyerek ilerlemeyi kaydetmesine olanak tanıyın.

### Bölüm 0: Bunu kim kullanıyor ve neler bağlı

#### Bunu kim kullanıyor?

> Bu eklentiyi günden güne kim kullanacak? (Bu, kuracağınız her eklentide taşınan Rol sinyalini besler)
>
> 1. **Avukat veya hukuk profesyoneli** — avukat, stajyer avukat, hukuk bürosu çalışanı.
> 2. **Avukat erişimi olan avukat-olmayan** — kurucu, iş lideri, sözleşme yöneticisi, İK; danışabileceğiniz iç veya dış bir avukatınız var.
> 3. **Düzenli avukat erişimi olmayan avukat-olmayan** — bunu kendiniz hallediyorsunuz.

2 veya 3 ise, ekleyin: "Bu eklenti, eklentileri keşfeder ve kurar. Kurduğunuz eklentilerin rolünüze göre kendi guardrail'ları olacaktır."
3 ise Türkiye koşullarına uygun bir avukat/baro tavsiyesi ekleyin.

#### Neler bağlı?

MCP araçlarını kontrol edin (Slack vb.) ve `## Kullanılabilir entegrasyonlar` altına yazın. Yalnızca test edilebilenlere ✓ koyun.

#### Güvenilen kaynaklar (allowlist.yaml)

- Kullanıcıdan güvenilen registry (kayıt) kaynakları listesi isteyin.
- Dağıtım bağlamını sorun: Kişisel / Firma-içi / Ürün-gömülü. (Buna göre lisans izinleri belirlenecektir).
- `allowlist.yaml` dosyasına yazın. (Kısıtlayıcı/İzin verici mod onayı alın).

#### Tazelik hatırlatıcıları (Freshness)

> "Bir topluluk eklentisi referans materyali (mevzuat, usul şablonları vb.) paketlediğinde, hala güncel olduğunu teyit etmenizi hatırlatmadan önce ne kadar süre güvenilmelidir? (Düzenleyici içerik için genelde 6 ay varsayılandır.)"

`## Tazelik hatırlatıcıları` tablosunu profile yazın.

### Beş Soru

1. **Pratik alanı** — Şirket içi mi yoksa büro mu? Ticari, KVKK, ürün, dava, M&A vb.
2. **Sektör** — Teknoloji, sağlık, finans, diğer vb.
3. **Ekip boyutu** — Tek, küçük ekip (2-5), büyük departman.
4. **En çok yaptığınız şey nedir?** — Sözleşme inceleme, uyum, lansman incelemeleri, dilekçe yazımı vb.
5. **Araç konforu** — Kurucu (kendi skill'ini yazan), kurcalayan (var olanı düzenleyen), sadece-çalışsın.

### Öner (Recommend)

Profili kayıt (registry) eklentileriyle eşleştirin:
- Şirket içi ticari, teknoloji -> `ticari-hukuk` eklentisi
- Dava -> `dava-takibi` eklentisi
- Bilişim / Ürün -> `fikri-mulkiyet` eklentisi

Önerilenleri kullanıcının onayıyla kurun.

## Pratik Profilini Yazma

`~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` şablonuna göre yazın.

## Yazdıktan Sonra

Kapanışta merkezin neler yapabildiğini (`kayit-tarayici`, `eklenti-kurucu`, `otomatik-guncelleyici`, vb.) gösterin ve "Pratik profiliniz kullandıkça öğrenir" diyerek tamamlayın.
