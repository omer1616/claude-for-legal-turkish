---
name: ozellestir
description: >
  Ticari sözleşmeler pratik profilinizin rehberli özelleştirmesi — tüm ilk-kurulum
  görüşmesini yeniden çalıştırmadan tek bir şeyi değiştirin. Risk duruşunu,
  eskalasyon irtibatlarını, oyun kitabı pozisyonlarını, NDA triyaj tercihlerini, ev
  tarzını, inceleme tercihlerini veya dosya çalışma alanı yollarını ayarlayın.
  Kullanıcı "[bir şeyi] değiştir", "profilimi güncelle", "oyun kitabımı düzenle",
  "yapılandırmamı ayarla" veya "özelleştir" dediğinde kullan.
argument-hint: "[bölüm adı, ya da ne değiştirmek istediğinizi açıklayın]"
---

# /ozellestir

## Bu Ne Zaman Çalışır

Kullanıcı `/ticari-hukuk:ozellestir` yazdı. Pratik profilinde bir şeyi değiştirmek
istiyor — bir risk duruşu, bir eskalasyon irtibatı, bir oyun kitabı pozisyonu, bir
yargı çevresi, bir çıktı formatı — tüm ilk-kurulum görüşmesini yeniden çalıştırmadan
ve YAML'ı elle düzenlemeden.

## Ne Yapmalı

1. **Yapılandırmayı oku.**
   `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`
   dosyasını oku (ve bir üst seviyedeki
   `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md`). Eklenti
   yapılandırması mevcut değilse veya hâlâ `[YER_TUTUCU]` değerleri içeriyorsa, şunu
   söyle:

   > Henüz kurulum yapmamışsınız. Önce `/ticari-hukuk:ilk-kurulum` çalıştırın —
   > özelleştirme, zaten sahip olduğunuz bir profili ayarlamak içindir.

2. **Özelleştirilebilir haritayı göster.** Profildekini gruplandırılmış hâlde,
   mevcut değerin tek satırlık özetiyle listele:

   - **Şirket / kim olduğumuz** — ad, sektör, yargı çevreleri, aşama, pratik ortamı,
     satış-tarafı vs. satın alma-tarafı yönelimi *(tüm eklentilerde paylaşılır —
     değişiklikler `company-profile.md` üzerinden yansır)*
   - **Risk duruşu** — muhafazakâr / orta / agresif, her birinin yedek pozisyonlar ve
     eskalasyon tetikleyicileri için ne anlama geldiği
   - **Kişiler** — eskalasyon zinciri, tutar eşiğine ve madde türüne göre
     onaylayıcılar
   - **Oyun kitabı pozisyonları** — esaslı sözleşme pozisyonları: sorumluluk
     tavanları, tazminat kapsamı, fikri mülkiyet sahipliği, veri koruma, fesih,
     otomatik yenileme, fiyat artışı ve her biri için yedekler
   - **NDA triyaj tercihleri** — gelen NDA'lar için yeşil / sarı / kırmızının nasıl
     göründüğü
   - **İnceleme tercihleri** — redline tarzı, açıklama derinliği, varsayılan olarak
     bir paydaş özeti üretilip üretilmeyeceği
   - **Ev tarzı** — belge formatı, imza bloğu, yenileme-uyarı kanalı, sapma-günlüğü
     formatı
   - **İş akışı** — dosya çalışma alanı yolları, intake yolu, yenileme izleyici
     kadansı
   - **Entegrasyonlar** — Ironclad / DocuSign / Slack / belge depolama durumu,
     yedekler

3. **Ne değiştirmek istediklerini sor.**

   > Ne ayarlamak istersiniz? Bir bölüm seçin veya değişikliği kendi
   > kelimelerinizle açıklayın.

4. **Değişikliği yap.** Mevcut değeri göster, yeni değeri sor, aşağı akışta ne
   değişeceğini açıkla, teyit et, yapılandırmaya yaz.

   Örnekler:
   - *Sorumluluk tavanı yedeği 12 aydan 6 aya:* "`/sozlesme-inceleme` artık 6 ayın
     üstündeki herhangi bir şeyi bir sapma olarak işaretleyecek; mevcut
     anlasma-degerlendirme girişleri kaydedildiği gibi kalır."
   - *Yeni eskalasyon onaylayıcısı:* "Kendi yetkinizi aşan herhangi bir redline
     artık bu onaylayıcıya yönlendirilecek —
     `/eskalasyon-isaretleyici` eşleşen risk bandı için onları varsayılan olarak
     dahil edecek."
   - *Risk duruşu orta → agresif:* "İşaretlemeden daha fazla satıcı-lehine
     pozisyonu kabul edeceğim ve `[incele]` çıtasını yükselteceğim."

5. **Paylaşılan profil değişiklikleri** için (şirket adı, sektör, yargı çevreleri,
   pratik ortamı, aşama):
   `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md`'ye yaz ve
   not et:

   > Bu değişiklik tüm eklentileri etkiliyor — yargı çevresi ayak izinizi okuyan
   > herhangi bir eklenti artık [yeni değer]'i görüyor.

6. **Kapat.**

   > Tamam. Bir sonraki çıktınız değişikliği yansıtacak. Başka bir şey var mı?
   > `/ticari-hukuk:ozellestir`'i istediğiniz zaman çalıştırabilirsiniz.

## Guardrail'lar

- **Asla bir bölümü silme.** Kullanıcı bir sözleşme türünü kapsamdan "kaldırmak"
  istiyorsa, onu `[Şu anda ele alınmıyor]` olarak işaretlemeyi teklif et ve intake
  yönlendirme değişikliklerini açıkla.
- **İç tutarsızlığı işaretle.** Değişiklik profili tutarsız hâle getirirse (ör.
  yalnızca-satış-tarafı yönelimi + yalnızca-satın-alma-tarafı oyun kitabı listesi;
  ya da risk duruşu agresif + "her redline BHM onayı gerektirir"), gerilimi
  işaretle ve hangisini istediğini sor.
- **Guardrail bozunmasını işaretle.** Kullanıcı bir guardrail'i kapatmak isterse
  (`[incele]` bayrağını düşürme, meslek sırrı başlığını atlama, `[doğrula]`
  etiketlerini kaldırma), guardrail'in neyi koruduğunu açıkla ve takas anlaştığından
  emin ol. `[incele]` bayrağı, kaynak atıf etiketleri ve alıntılanan kanunlar
  üzerindeki `[doğrula]` etiketleri yük taşır ve kaldırılmamalıdır.
- **Bir seferde bir değişiklik.** Tüm görüşmeyi yeniden sorma.
