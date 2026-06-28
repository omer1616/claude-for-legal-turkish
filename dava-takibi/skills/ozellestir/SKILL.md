---
name: ozellestir
description: >
  Dava pratik profilinin rehberli özelleştirmesi — tüm ilk kurulum görüşmesini
  yeniden çalıştırmadan tek bir şeyi değiştir. Pratik rolünü, tarafını, risk
  kalibrasyonunu, manzarayı, ev tarzını, eskalasyon irtibatlarını, şiddet
  sözlüğünü veya dosya çalışma alanı yollarını ayarla. Kullanıcı
  "[bir şeyi] değiştir", "profilimi güncelle", "yapılandırmamı düzenle" veya
  "özelleştir" dediğinde kullan.
argument-hint: "[bölüm adı veya ne değiştirmek istediğini açıkla]"
---

# /ozellestir

## Bu Ne Zaman Çalışır

Kullanıcı `/dava-takibi:ozellestir` yazdı. Dava profilinde bir şeyi değiştirmek istiyor — bir risk kalibrasyonu, bir ev tarzı kuralı, bir eskalasyon irtibatı, bir manzara notu — tüm ilk kurulum görüşmesini yeniden çalıştırmadan ve YAML'ı elle düzenlemeden.

## Ne Yapmalı

1. **Yapılandırmayı oku.** Şunu oku:
   `~/.claude/plugins/config/claude-for-legal-turkish/dava-takibi/CLAUDE.md`
   (ve bir üst seviyedeki `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md`). Plugin yapılandırması mevcut değilse veya hâlâ `[YER_TUTUCU]` değerleri içeriyorsa, şunu söyle:

   > Henüz kurulum yapmamışsınız. Önce `/dava-takibi:ilk-kurulum` çalıştırın — özelleştirme, zaten sahip olduğunuz bir profili ayarlamak içindir.

2. **Özelleştirilebilir haritayı göster.** Profildekini gruplandırılmış hâlde, mevcut değerin tek satırlık özetiyle listele:

   - **Şirket / kim olduğumuz** — ad, sektör, yargı çevreleri, aşama, pratik ortamı *(tüm eklentilerde paylaşılır — değişiklikler `company-profile.md` üzerinden yansır)*
   - **Pratik rolü** — şirket-içi avukat / dış avukat / bağımsız / klinik
   - **Taraf** — davacı / davalı / her ikisi, ve herhangi bir duruş nüansı (toplu dava savunması, düzenleyici yaptırım savunması, ticari davacı, vb.)
   - **Risk kalibrasyonu** — gelen talep, müzekkere veya yeni dosyada yüksek / orta / düşük riskin ne sayıldığı; eskalasyon tetikleyicileri
   - **Manzara** — sık hasımlar, dost ve düşman forumlar, bilinmesi gereken hakimler, mevcut dış avukat ilişkileri
   - **Ev tarzı** — dilekçe tarzı, delil toplama beyanı formatı, talep mektubu şablonu, tutanak taslak yapısı, delil saklama şablonu
   - **Şiddet sözlüğü eşlemesi** — müvekkil / iç / mahkemeye yönelik çıktılar genelinde şiddet etiketlerini nasıl çevirdiğiniz
   - **Kişiler** — dosya liderleri, iç hukuk ekibi, dosya türüne göre dış avukat, eskalasyon zinciri
   - **İş akışı** — dosya çalışma alanları, portföy günlüğü, dış avukat durum kadansı, delil saklama tazeleme kadansı
   - **Entegrasyonlar** — belge depolama / e-sunum / takvim / Slack durumu, yedekler

3. **Ne değiştirmek istediklerini sor.**

   > Ne ayarlamak istersiniz? Bir bölüm seçin veya değişikliği kendi kelimelerinizle açıklayın.

4. **Değişikliği yap.** Mevcut değeri göster, yeni değeri sor, aşağı akışta ne değişeceğini açıkla, teyit et, yapılandırmaya yaz.

   Örnekler:
   - *Taraf her ikisi → yalnızca davalı:* "`/dosya-acilis` davacı tarafı soruları sormayı bırakacak. Davalı tarafı savunmacı talepler için hâlâ çalışacak ama başlangıç çerçevesi farklı olacak."
   - *Risk kalibrasyonu yüksek risk eşiğini sıkılaştırma:* "Daha fazla gelen talep ve müzekkere `/dosya-brifingi` ve `/karsi-vekil-durumu` üzerinden geçecek."
   - *İP dosyaları için yeni mevcut dış avukat:* "`/karsi-vekil-durumu` bu büroyu İP etiketli dosyalar için haftalık taramalara dahil edecek."

5. **Paylaşılan profil değişiklikleri** için (şirket adı, sektör, yargı çevreleri, pratik ortamı, aşama):
   `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md`'ye yaz ve not et:

   > Bu değişiklik tüm eklentileri etkiliyor — yargı çevresi ayak izinizi okuyan herhangi bir eklenti artık [yeni değer]'i görüyor.

6. **Kapat.**

   > Tamam. Bir sonraki çıktınuz değişikliği yansıtacak. Başka bir şey var mı? `/dava-takibi:ozellestir`'i istediğiniz zaman çalıştırabilirsiniz.

## Guardrail'lar

- **Asla bir bölümü silme.** Kullanıcı bir dosya türünü kapsamdan "kaldırmak" istiyorsa, onu `[Şu anda ele alınmıyor]` olarak işaretlemeyi teklif et ve intake yönlendirme değişikliklerini açıkla.
- **İç tutarsızlığı işaretle.** Değişiklik profili tutarsız hâle getirirse (ör. yalnızca-davacı tarafı + yalnızca-davalı dış avukat listesi; veya "yüksek hacim" portföy + yapılandırılmış dosya çalışma alanı yok), gerilimi işaretle.
- **Guardrail bozunmasını işaretle.** Delil saklama bildirimi üzerindeki gizlilik kapısı, dosya çıktılarındaki iş ürünü başlığı, kaynak atıf etiketleri ve `[doğrula]` etiketleri yük taşıyan öğelerdir — çıkarma. `[incele]` bayrağı ve "avukat incelemesi olmadan sunma" çerçevelemesi yük taşıyan öğelerdir.
- **Bir seferde bir değişiklik.** Tüm görüşmeyi yeniden sorma.