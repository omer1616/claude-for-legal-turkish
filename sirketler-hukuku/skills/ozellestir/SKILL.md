---
name: ozellestir
description: >
  Kurumsal hukuk pratik profilinizi rehberli olarak özelleştirin — tüm ilk-kurulum 
  (cold-start) mülakatını yeniden yapmadan tek bir şeyi değiştirin. Risk yaklaşımını, 
  eskalasyon (yetki) kişilerini, aktif modülleri (M&A / Kurul / Halka Açık Şirket / Şirket Yönetimi), 
  önemlilik eşiklerini, ek (schedule) formatını veya dosya çalışma alanı yollarını ayarlayın. 
  Kullanıcı "benim [şu ayarı] değiştir", "profilimi güncelle", "konfigürasyonumu düzenle" 
  veya "özelleştir" dediğinde kullanın.
argument-hint: "[bölüm adı, veya neyi değiştirmek istediğinizi açıklayın]"
---

# /ozellestir

## Ne zaman çalışır

Kullanıcı `/sirketler-hukuku:ozellestir` yazdı. Pratik profilinde bir şeyi (risk yaklaşımı, eskalasyon kişisi, modül anahtarı, çıktı formatı) değiştirmek istiyorlar — ve tüm ilk kurulumu (`ilk-kurulum`) yeniden yapmak veya YAML dosyalarını elle düzenlemek istemiyorlar.

## Ne yapılmalı

1. **Konfigürasyonu oku.** `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` dosyasını (ve bir üst seviyedeki `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasını) oku. Eğer eklenti konfigürasyonu yoksa veya hala `[YER_TUTUCU]` (PLACEHOLDER) değerleri içeriyorsa şöyle de:

   > Henüz kurulumu yapmamışsınız. Önce `/sirketler-hukuku:ilk-kurulum` (cold-start) çalıştırın — özelleştirme yeteneği halihazırda var olan bir profili ayarlamak içindir.

2. **Özelleştirilebilir haritayı göster.** Profilde neler olduğunu, mevcut değerin tek satırlık özetiyle gruplandırarak listele:

   - **Şirket / kim olduğunuz** — isim, sektör, yargı çevreleri, aşama, halka açık / özel, çalışma ortamı *(Tüm eklentilerde ortaktır — değişiklikler `company-profile.md`'ye yansır)*
   - **Aktif modüller** — M&A, Kurul & Sekreterya, Halka Açık Şirket, Şirket Yönetimi modüllerinden hangileri açık. Kapatıp açmak hangi yeteneklerin (skills) kurulacağını değiştirir.
   - **Risk yaklaşımı** — muhafazakar / orta / agresif. Her birinin diligence eşikleri ve açıklama listesi kapsamı için anlamı.
   - **Kişiler** — işlem ekibi, YK sekreteri, eskalasyon (yetki devri) zinciri (Baş Hukuk Müşaviri vb.).
   - **M&A modülü** — Önemlilik eşikleri (sözleşme değeri, personel sayısı, gelir), güvenilen veri odası (VDR) platformları, Yapay Zeka (Luminance/Kira) güven seviyesi, işlem ekibi bilgilendirme ritmi.
   - **Kurul & Sekreterya modülü** — kurum yazılı onay (consent) formatı, imza tercihleri, komite yapısı.
   - **Halka Açık Şirket modülü** — finansal raporlama takvimi, özel durum açıklaması (KAP) süreçleri, kontrol zamanlamaları.
   - **Şirket Yönetimi modülü** — tüzel kişi tablosu, MERSİS/Ticaret Sicili temsilcisi, tescil çevreleri, yıllık beyan takvimi.
   - **İş Akışı** — dosya çalışma alanları (matter workspaces), kapanış kontrol listesi konumu.

3. **Neyi değiştirmek istediklerini sor.**

   > Neyi ayarlamak istersiniz? Bir bölüm seçin veya değişikliği kendi kelimelerinizle açıklayın.

4. **Değişikliği yap.** Mevcut değeri göster, yeni değeri iste, değişikliğin alt süreçleri (downstream) nasıl etkileyeceğini açıkla, onayla ve konfigürasyona yaz.

   Örnekler:
   - *Önemlilik eşiğini 250K₺ → 500K₺ yapmak:* "`/due-diligence-sorun-cikartma` ve `/onemli-sozlesme-takvimi` artık sınırı 500.000 ₺ olarak kabul edecek. Mevcut bulgular değişmez; geriye dönük uygulanmasını isterseniz diligence yeteneklerini yeniden çalıştırmalısınız."
   - *AI toplu inceleme güven seviyesini "her satırı kontrol et" → "nokta kontrolü (spot-check) %10" yapmak:* "`/yapay-zeka-arac-devri` artık her bir çıkarım yerine rastgele %10'luk bir örneklemi QA (kalite kontrol) yapacak."

5. **Ortak-profil (shared-profile) değişiklikleri için** (şirket adı, sektör, yargı çevresi vb.): Değişikliği `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasına yaz ve şunu belirt:

   > Bu değişiklik tüm kurulu hukuk eklentilerini (plugins) etkiler — yargı çevrenizi veya şirketinizi okuyan herhangi bir eklenti artık [yeni değeri] görecektir.

6. **Kapat.**

   > Tamamlandı. Sonraki çıktılarınız bu değişikliği yansıtacak. Başka bir şey var mı? `/sirketler-hukuku:ozellestir` yeteneğini istediğiniz zaman kullanabilirsiniz.

## Koruma Kuralları (Guardrails)

- **Asla bir bölümü tamamen silme.** Kullanıcı bir şeyi "kaldırmak" istiyorsa, değerini `[Yapılandırılmadı]` olarak ayarla ve bunun eklentinin davranışını nasıl etkileyeceğini açıkla.
- **İç tutarsızlığı (inconsistency) işaretle.** Değişiklik profili tutarsız hale getiriyorsa (Örn: Halka Açık Şirket modülü kapalıyken eskalasyon yetkilisi olarak "SPK Avukatı" atanması), bu uyuşmazlığı kullanıcıya bildir.
- **Koruma kalkanı (guardrail) zayıflaması.** Hukuki yeteneklerdeki `[doğrulanacak]`, `[UZMAN DOĞRULA]` ve benzeri kaynak etiketleri kritik yük taşıyıcılardır — kullanıcı bunları kaldırmak isterse risk takası (trade-off) hakkında bilgi ver.
- **Her seferinde tek bir değişiklik.** Bütün ilk-kurulum mülakatını yeniden sorma.
