---
name: ozellestir
description: >
  İş hukuku pratik profilinizin rehberli özelleştirmesi — tüm ilk-kurulum
  görüşmesini yeniden çalıştırmadan tek bir şeyi değiştirin. Yargı çevresi
  ayak izini, risk duruşunu, eskalasyon irtibatlarını, işe alım/fesih
  inceleme kurallarını, çalışma kılavuzu pozisyonlarını, izin türlerini,
  soruşturma tercihlerini veya dosya çalışma alanı yollarını ayarlayın.
  Kullanıcı "[bir şeyi] değiştir", "profilimi güncelle", "yargı çevremi
  ekle", "yapılandırmamı ayarla" veya "özelleştir" dediğinde kullan.
argument-hint: "[bölüm adı, ya da ne değiştirmek istediğinizi açıklayın]"
---

# /ozellestir

## Bu Ne Zaman Çalışır

Kullanıcı `/is-hukuku:ozellestir` yazdı. Pratik profilinde bir şeyi
değiştirmek istiyor — bir yargı çevresi, bir risk duruşu, bir eskalasyon
irtibatı, bir izin türü, bir çıktı formatı — tüm ilk-kurulum görüşmesini
yeniden çalıştırmadan ve YAML'ı elle düzenlemeden.

## Ne Yapmalı

1. **Yapılandırmayı oku.**
   `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
   dosyasını oku (ve bir üst seviyedeki
   `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md`).
   Eklenti yapılandırması mevcut değilse veya hâlâ `[YER_TUTUCU]` değerleri
   içeriyorsa, şunu söyle:

   > Henüz kurulum yapmamışsınız. Önce `/is-hukuku:ilk-kurulum` çalıştırın
   > — özelleştirme, zaten sahip olduğunuz bir profili ayarlamak içindir.

2. **Özelleştirilebilir haritayı göster.** Profildekini gruplandırılmış
   hâlde, mevcut değerin tek satırlık özetiyle listele:

   - **Şirket / kim olduğumuz** — ad, sektör, pratik ortamı *(tüm
     eklentilerde paylaşılır — değişiklikler `company-profile.md` üzerinden
     yansır)*
   - **Yargı çevresi ayak izi** — çalışanı olan ülkeler ve sektöre göre
     uygulanacak rejim, tek-ülke vs. çok-ülkeli, herhangi bir yaklaşan
     genişleme. Bu, yargı çevresine özgü ek mantığını yönlendirir.
   - **Risk duruşu** — muhafazakâr / orta / agresif, her birinin fesih
     riskini işaretleme, rekabet yasağı uygulanabilirliği ve izin
     uyarlaması için ne anlama geldiği
   - **Kişiler** — İK sorumlusu, ekip lideri, dış avukat, eskalasyon
     zinciri, soruşturma sponsoru
   - **İşe alım incelemesi** — teklif mektubu şablonu, rekabet yasağı
     duruşu, arka plan kontrolü sağlayıcısı, standart şartlar
   - **Fesih incelemesi** 🅱️ — B kademesinde, `isten-cikartma-inceleme`
     taşınana kadar kullanılamaz
   - **Ücret ve çalışma süresi** 🅱️ — B kademesinde,`ucret-saat-sss`
     taşınana kadar kullanılamaz
   - **Çalışma kılavuzu** — kılavuz dosya yolu, bölge/birim ekleri
     yaklaşımı, gözden geçirme sıklığı
   - **İzin türleri** — profildeki izin türleri tablosu (yıllık, doğum,
     babalık, hastalık-rapor vb.) ve süreleri
   - **Soruşturma tercihleri** — meslek sırrı etiketleme, görüşme
     protokolü, hedef kitleye özel özet şablonları
   - **İş akışı** — dosya çalışma alanı yolları, izin izleyici eşikleri,
     genişleme proje yolları
   - **Entegrasyonlar** — İK sistemi / Slack / belge depolama durumu,
     yedekler

3. **Ne değiştirmek istediklerini sor.**

   > Ne ayarlamak istersiniz? Bir bölüm seçin veya değişikliği kendi
   > kelimelerinizle açıklayın.

4. **Değişikliği yap.** Mevcut değeri göster, yeni değeri sor, aşağı
   akışta ne değişeceğini açıkla, teyit et, yapılandırmaya yaz.

   Örnekler:
   - *Yargı çevresi ayak izine yeni bir ülke eklemek:* "`/ise-alim-inceleme`
     ve `uluslararasi-genisletme` artık bu ülkeyi tanıyacak.
     `/calisma-kilavuzu-guncelleme` bir bölge/birim eki için soracak."
   - *İzin türleri tablosuna yeni bir tür eklemek (ör. sendikal izin):*
     "`/izin-takibi` ve `/izin-kaydi` artık bu türü bir seçenek olarak
     gösterecek."
   - *Risk duruşu orta → muhafazakâr:* "Daha fazla fesih ve işe alım
     kararını eskalasyona işaretleyeceğim, rekabet yasağı hükümlerinde
     daha temkinli olacağım."

5. **Paylaşılan profil değişiklikleri** için (şirket adı, sektör, pratik
   ortamı): `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md`'ye
   yaz ve not et:

   > Bu değişiklik tüm eklentileri etkiliyor — yargı çevresi ayak izinizi
   > okuyan herhangi bir eklenti artık [yeni değer]'i görüyor.

6. **Kapat.**

   > Tamam. Bir sonraki çıktınız değişikliği yansıtacak. Başka bir şey var
   > mı? `/is-hukuku:ozellestir`'i istediğiniz zaman çalıştırabilirsiniz.

## Guardrail'lar

- **Asla bir bölümü silme.** Kullanıcı bir yargı çevresini "kaldırmak"
  istiyorsa, onu `[Şu anda çalışanı yok — yeniden giriş için kuralları
  koru]` olarak işaretlemeyi teklif et ve `[Yapılandırılmamış]`'a geçmenin
  yargı çevresine özgü işaretlemeyi düşüreceğini açıkla.
- **İç tutarsızlığı işaretle.** Değişiklik profili tutarsız hâle
  getirirse (ör. ayak izinde bir ülke + o ülke için hiç eskalasyon kuralı
  yok; ya da risk duruşu agresif + "her fesih dış avukata gider"),
  gerilimi işaretle ve hangisini istediğini sor.
- **Guardrail bozunmasını işaretle.** Kullanıcı bir guardrail'i kapatmak
  isterse (`[incele]` bayrağını düşürme, meslek sırrı başlığını atlama,
  `[doğrula]` etiketlerini kaldırma), guardrail'in neyi koruduğunu açıkla
  ve takas anlaştığından emin ol. `[incele]` bayrağı, kaynak atıf
  etiketleri ve alıntılanan kanunlar üzerindeki `[doğrulanacak]` etiketleri
  yük taşır ve kaldırılmamalıdır.
- **B kademesi bölümlerini hatırlat.** Kullanıcı "fesih incelemesi
  politikamı değiştir" veya "fazla mesai politikamı ayarla" isterse, bu
  alanların şu an `isten-cikartma-inceleme` ve `ucret-saat-sss` (henüz
  taşınmadı) tarafından kullanıldığını, profildeki 🅱️ notunun bunun
  yerine güncellendiğini açıkla.
- **Bir seferde bir değişiklik.** Tüm görüşmeyi yeniden sorma.
