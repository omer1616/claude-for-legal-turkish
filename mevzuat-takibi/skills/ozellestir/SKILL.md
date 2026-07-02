---
name: ozellestir
description: >
  Mevzuat takibi pratik profilinizi rehberli olarak özelleştirin — tüm ilk-kurulum 
  (cold-start) mülakatını yeniden yapmadan tek bir şeyi değiştirin. İzleme listesini, 
  önemlilik (materiality) eşiklerini, besleme ritmini veya dosya çalışma alanı yollarını ayarlayın. 
  Kullanıcı "benim [şu ayarı] değiştir", "profilimi güncelle", "konfigürasyonumu düzenle" 
  veya "özelleştir" dediğinde kullanın.
argument-hint: "[bölüm adı, veya neyi değiştirmek istediğinizi açıklayın]"
---

# /ozellestir

## Ne zaman çalışır

Kullanıcı `/mevzuat-takibi:ozellestir` yazdı. Pratik profilinde bir şeyi değiştirmek istiyorlar — ve tüm ilk kurulumu (`ilk-kurulum`) yeniden yapmak veya yapılandırma dosyalarını elle düzenlemek istemiyorlar.

## Ne yapılmalı

1. **Konfigürasyonu oku.** `~/.claude/plugins/config/claude-for-legal-turkish/mevzuat-takibi/CLAUDE.md` dosyasını (ve bir üst seviyedeki `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasını) oku. Eğer eklenti konfigürasyonu yoksa veya hala `[YER_TUTUCU]` değerleri içeriyorsa şöyle de:

   > Henüz kurulumu yapmamışsınız. Önce `/mevzuat-takibi:ilk-kurulum` (cold-start) çalıştırın — özelleştirme yeteneği halihazırda var olan bir profili ayarlamak içindir.

2. **Özelleştirilebilir haritayı göster.** Profilde neler olduğunu, mevcut değerin tek satırlık özetiyle gruplandırarak listele:

   - **Şirket / kim olduğunuz** — isim, sektör, yargı çevreleri, aşama, halka açık / özel, çalışma ortamı *(Tüm eklentilerde ortaktır — değişiklikler `company-profile.md`'ye yansır)*
   - **İzlenen Kurumlar** — SPK, BDDK, Rekabet Kurumu, Ticaret Bakanlığı vb. hangileri izleme listesinde.
   - **Rol ve İletişim** — Avukat, uyum yöneticisi, Hukuk Müşavirliği iletişim bilgisi.
   - **Önemlilik Eşiği** — Acil (always material), İncelemeye Değer (review-worthy), Bilgi Amaçlı (FYI) neleri kapsıyor.
   - **Politika Kütüphanesi** — Hangi politikalar nerede, sahibi kim.
   - **Boşluk Yanıt Süreci** — Triaj kimde, eskalasyon kimde.
   - **Besleme Konfigürasyonu** — Ücretsiz API'ler, RSS adresleri, özel MCP'ler.
   - **İş Akışı** — dosya çalışma alanları (matter workspaces).

3. **Neyi değiştirmek istediklerini sor.**

   > Neyi ayarlamak istersiniz? Bir bölüm seçin veya değişikliği kendi kelimelerinizle açıklayın.

4. **Değişikliği yap.** Mevcut değeri göster, yeni değeri iste, değişikliğin alt süreçleri (downstream) nasıl etkileyeceğini açıkla, onayla ve konfigürasyona yaz.

   Örnekler:
   - *Yeni bir kurum eklemek:* "Rekabet Kurumu'nu izleme listesine ekliyorum. Artık `/mevzuat-besleme-izleyici` Rekabet Kurulu kararlarını ve bültenlerini de kontrol edecek."
   - *Önemlilik eşiğini değiştirmek:* "Taslak yönetmelikleri (NPRM) 'Hemen haber ver' seviyesinden 'Haftalık incelemeye değer' seviyesine indiriyorum."

5. **Ortak-profil (shared-profile) değişiklikleri için** (şirket adı, sektör, yargı çevresi vb.): Değişikliği `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasına yaz ve şunu belirt:

   > Bu değişiklik tüm kurulu hukuk eklentilerini (plugins) etkiler — yargı çevrenizi veya şirketinizi okuyan herhangi bir eklenti artık [yeni değeri] görecektir.

6. **Kapat.**

   > Tamamlandı. Sonraki çıktılarınız bu değişikliği yansıtacak. Başka bir şey var mı? `/mevzuat-takibi:ozellestir` yeteneğini istediğiniz zaman kullanabilirsiniz.

## Koruma Kuralları (Guardrails)

- **Asla bir bölümü tamamen silme.** Kullanıcı bir şeyi "kaldırmak" istiyorsa, değerini `[Yapılandırılmadı]` olarak ayarla ve bunun eklentinin davranışını nasıl etkileyeceğini açıkla.
- **İç tutarsızlığı (inconsistency) işaretle.** Değişiklik profili tutarsız hale getiriyorsa, bu uyuşmazlığı kullanıcıya bildir.
- **Koruma kalkanı (guardrail) zayıflaması.** Hukuki yeteneklerdeki `[doğrulanacak]`, `[UZMAN DOĞRULA]` ve benzeri kaynak etiketleri kritik yük taşıyıcılardır — kullanıcı bunları kaldırmak isterse risk takası (trade-off) hakkında bilgi ver.
- **Her seferinde tek bir değişiklik.** Bütün ilk-kurulum mülakatını yeniden sorma.
