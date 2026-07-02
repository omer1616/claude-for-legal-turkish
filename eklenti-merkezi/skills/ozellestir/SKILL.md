---
name: ozellestir
description: >
  Eklenti Merkezi (Legal Builder Hub) profilinizin rehberli özelleştirmesi — tüm ilk-kurulum görüşmesini yeniden çalıştırmadan tek bir şeyi değiştirin. Pratik profilini, kurulu başlangıç paketini, izlenen kayıtları, güncelleme tercihlerini veya kalite kontrol (QA) katılığını ayarlayın. Kullanıcı "[bir şeyimi] değiştir", "bir kayıt (registry) ekle", "profilimi güncelle", "yapılandırmamı düzenle" veya "özelleştir" dediğinde kullanın.
argument-hint: "[bölüm adı, veya neyi değiştirmek istediğinizi açıklayın]"
---

# /ozellestir

## Bu ne zaman çalışır

Kullanıcı `/eklenti-merkezi:ozellestir` yazmıştır. Eklenti Merkezi (Builder Hub) profilindeki bir şeyi — izlenen bir kaydı, güncelleme bildirim tercihlerini, öneriler için bir pratik alanını — tüm ilk-kurulum görüşmesini yeniden çalıştırmadan ve elle YAML düzenlemeden değiştirmek istiyorlardır.

## Ne yapılmalı

1. **Yapılandırmayı (config) okuyun.** Şunu okuyun:
   `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md`
   (ve bir üst seviyedeki `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md`). Eğer eklenti yapılandırması mevcut değilse veya hala `[YER TUTUCU]` (`[PLACEHOLDER]`) değerleri içeriyorsa, şunu söyleyin:

   > Henüz kurulumu çalıştırmamışsınız. Önce `/eklenti-merkezi:ilk-kurulum` çalıştırın — özelleştirme (customize), halihazırda sahip olduğunuz bir profili ayarlamak içindir.

2. **Özelleştirilebilir haritayı gösterin.** Profilde neler olduğunu gruplandırılmış olarak ve mevcut değerin tek satırlık bir özetiyle listeleyin:

   - **Şirket / kim olduğunuz** — isim, sektör, yargı çevreleri, aşama, pratik ortamı *(tüm temel eklentilerde paylaşılır — değişiklikler `company-profile.md` üzerinden akar)*
   - **Pratik profiliniz** — kapsama giren pratik alanları, topluluk eklentilerini önermek için kullanılır
   - **Kurulu başlangıç paketi** — merkez (hub) aracılığıyla hangi eklentilerin (plugins/skills) kurulu olduğu ve kurulum kaynakları
   - **İzlenen kayıtlar (registries)** — merkezin topluluk eklentilerini çektiği GitHub depoları / URL'ler
   - **Güncelleme tercihleri** — kontrol temposu (günlük / haftalık / talep üzerine), bildirim kanalı (Slack / oturum içi), otomatik-güncellemeye karşı sorma
   - **Kalite kontrol (QA) katılığı** — kurulumdan önce aday bir eklentide `/eklenti-kalite-kontrol`'ün sorunları ne kadar agresif işaretleyeceği (esnek / orta / katı) ve hangi hata-modu kontrollerinin açık olduğu
   - **Eklenti (skill) kurulum varsayılanları** — kurulum kapsamı (kullanıcı / proje), kurulumdan önce otomatik olarak `/eklenti-kalite-kontrol` çalıştırılıp çalıştırılmayacağı
   - **Entegrasyonlar** — Slack / belge depolama durumu, yedekler (fallbacks)

3. **Neyi değiştirmek istediklerini sorun.**

   > Neyi ayarlamak istersiniz? Bir bölüm seçin veya değişikliği kendi kelimelerinizle açıklayın.

4. **Değişikliği yapın.** Mevcut değeri gösterin, yeni değeri isteyin, aşağı akışta nelerin değiştiğini açıklayın, onaylayın ve yapılandırmaya (config) yazın.

   Örnekler:
   - *Yeni bir izlenen kayıt eklerken:* "`/kayit-tarayici` (registry-browser), bu kaydı mevcut olanlarla birlikte arayacaktır. `/otomatik-guncelleyici` bir sonraki çalışmasında bunu kontrol edecektir."
   - *QA katılığını katıdan ortaya alırken:* "`/eklenti-kalite-kontrol` aynı bulguları raporlayacak, ancak siz onaylamadıkça orta banttaki bir kurulumu engellemeyecektir."
   - *Otomatik güncellemeyi açıktan kapalıya alırken:* "Merkez, güncellemeleri otomatik olarak uygulamak yerine uygulamadan önce size soracaktır."

5. **Paylaşılan profil değişiklikleri için** (şirket adı, sektör, yargı çevreleri, pratik ortamı, aşama):
   `~/.claude/plugins/config/claude-for-legal-turkish/company-profile.md` dosyasına yazın ve şunu belirtin:

   > Bu değişiklik tüm kurulu eklentileri (plugins) etkiler — yargı çevresi izinizi okuyan herhangi bir eklenti artık [yeni değer] görecektir.

6. **Kapatın.**

   > Tamamlandı. Bir sonraki çıktınız değişikliği yansıtacaktır. Başka bir şey var mı? İstediğiniz zaman `/eklenti-merkezi:ozellestir` çalıştırabilirsiniz.

## Guardrails (Korkuluklar / Sınırlar)

- **Asla bir bölümü silmeyin.** Kullanıcı izlenen bir kaydı "kaldırmak" isterse, onu `[Duraklatıldı]` (`[Paused]`) olarak işaretlemeyi teklif edin ve duraklatmanın kurulum geçmişini tuttuğunu ancak güncelleme kontrollerini durdurduğunu açıklayın.
- **İç tutarsızlığı işaretleyin.** Eğer değişiklik profili tutarsız hale getirecekse (örneğin, otomatik-güncelleme açık + QA katılığı kapalı; veya hiçbir kurulu eklentiyle eşleşmeyen pratik profili), bu gerilimi işaretleyin.
- **Guardrail bozulmasını işaretleyin.** Hukuki Eklenti Tasarım Çerçevesi kontrolleri (dokuz tasarım parametresi, üç hukuki hata modu, güven-yüzeyi kontrolü) `/eklenti-kalite-kontrol`'ün (skills-qa) var olma nedenidir — bunları kapatmak amacı bozar. Kullanıcı katılığı düşürmek isterse, kontrolü devre dışı bırakmak yerine orta bandı önerin.
- **Tek seferde tek değişiklik yapın.** Tüm görüşmeyi yeniden sormayın.
