---
name: dosya-calisma-alani
description: >
  Dosya (matter) çalışma alanlarını yönetin — yeni dosya oluşturma, listeleme, 
  geçiş yapma, kapatma veya aktif dosyadan çıkma. Birden fazla müvekkil 
  veya projeyle çalışan bürolarda, bir müvekkilin bağlamını diğerinden ayırmak 
  için kullanın.
argument-hint: "<yeni (new) | listele (list) | gec (switch) | kapat (close) | hicbiri (none)> [kisa-ad]"
---

# /dosya-calisma-alani

Avukatlar birden fazla müvekkil ve dosyada çalışırlar. "Dosya çalışma alanı" (matter workspace), bir müvekkilin veya işin bağlamını diğerinden ayrı tutar. Bu yetenek (skill) o çalışma alanlarını yönetir.

## Alt Komutlar (Subcommands)

- `/fikri-mulkiyet:dosya-calisma-alani yeni <kisa-ad>` — yeni bir dosya çalışma alanı yaratır, kısa bir mülakat yapar, `matter.md` dosyasını yazar.
- `/fikri-mulkiyet:dosya-calisma-alani listele` — dosyaları durumları ve aktiflik bayraklarıyla listeler.
- `/fikri-mulkiyet:dosya-calisma-alani gec <kisa-ad>` — aktif dosyayı değiştirir.
- `/fikri-mulkiyet:dosya-calisma-alani kapat <kisa-ad>` — bir dosyayı arşive kaldırır (asla silmez).
- `/fikri-mulkiyet:dosya-calisma-alani hicbiri` — herhangi bir aktif dosyadan çıkar, sadece pratik profili genelinde çalışır.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` dosyasını okuyun. "Dosya Çalışma Alanları" kısmı devre dışıysa (in-house kullanım gibi), kullanıcıya bunun kapalı olduğunu belirtin.
2. Parametreye göre aşağıdaki adımları uygulayın.
3. Değişiklikleri `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/matters/` dizini altında uygulayın. Yeni bir dosya açılırken `matter.md`, `history.md`, `notes.md` dosyalarını şablona uygun oluşturun.
4. Arşive kaldırılanlar `matters/_archived/` içine gider.

*(Detaylar orijinal matter-workspace/SKILL.md'deki ile aynıdır, dizinler sadece claude-for-legal-turkish/fikri-mulkiyet olacak şekilde değiştirilmiştir.)*
