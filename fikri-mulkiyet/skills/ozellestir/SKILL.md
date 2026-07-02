---
name: ozellestir
description: >
  Fikri Mülkiyet (FM) pratik profilinizin yönlendirmeli özelleştirmesi — tüm ilk 
  kurulum mülakatını yeniden çalıştırmadan tek bir şeyi değiştirin. Risk toleransını, 
  eskalasyon kişilerini, portföy kapsamını, marka koruma stratejisini veya 
  ihlal yaklaşımını ayarlayın.
argument-hint: "[bölüm adı, veya neyi değiştirmek istediğinizi açıklayın]"
---

# /ozellestir

Kullanıcı profilini (CLAUDE.md ve company-profile.md) YAML dosyalarını manuel olarak düzenlemeden güncellemek istediğinde çalışır. 

1. `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` okuyun. Profil yoksa `/fikri-mulkiyet:ilk-kurulum`'a yönlendirin.
2. Nelerin değiştirilebileceğinin haritasını gösterin: Şirket bilgileri, risk iştahı, kişiler, portföy kapsamı, marka koruma (izleme), ihlal-ihtarname toleransı vb.
3. Ne değiştirmek istediğini sorun.
4. Yeni değeri alın, etki edeceği yeri söyleyip onay alın ve dosyayı güncelleyin. Şirket genel profilinde (company-profile.md) yapılan değişikliğin diğer eklentileri (plugins) de etkileyeceğini uyarın.

*(Detaylar orijinal customize/SKILL.md ile aynıdır.)*
