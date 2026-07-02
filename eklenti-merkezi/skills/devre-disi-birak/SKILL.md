---
name: devre-disi-birak
description: >
  Merkez aracılığıyla kurulan bir topluluk eklentisini dosyalarını kaldırmadan devre dışı bırakır. Kullanıcı bir topluluk eklentisini geçici olarak sessize almak istediğinde ("devre dışı bırak [eklenti]"), yapılandırmasını korurken kancalarının tetiklenmesini durdurmak için veya önceden devre dışı bırakılmış bir eklentiyi yeniden etkinleştirmek için kullanın.
argument-hint: "[eklenti adı]"
---

# /devre-disi-birak

Belirtilen eklenti (skill) için referans olan `eklenti-yoneticisi` eklentisindeki `disable` (devre dışı bırak) iş akışını çalıştırın.

Devre dışı bırakma ne yapar:

- Eklentinin `SKILL.md` dosyasını `SKILL.md.disabled` olarak yeniden adlandırır, böylece Claude onu artık aktif bir eklenti olarak keşfetmez. Dosyalar, referanslar, şablonlar ve yapılandırmalar (config) yerinde kalır.
- Eğer eklenti `hooks/hooks.json` içinde kancalar (hooks) sunuyorsa, bu dosyayı da `hooks.json.disabled` olarak yeniden adlandırır; böylece eklenti devre dışıyken hiçbir otomatik tetikleyici çalışmaz.
- Eylemi `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/install-log.yaml` dosyasına kaydeder.

Güvenlik kuralları:

1. **Yalnızca bu merkez üzerinden kurulan topluluk eklentilerini devre dışı bırakın.** Kaldırma (uninstall) işlemi ile aynı kontrol — kurulum günlüğüne ve CLAUDE.md kurulu tablosuna başvurun.
2. **Asla birinci taraf bir eklentinin (plugin'in) skill'ini devre dışı bırakmayın.** Ulaşılamazdır.
3. **Yeniden adlandırmadan önce onaylayın.** Yolları gösterin, açıkça `evet` alın.

Aynı eklenti adıyla komutu tekrar çalıştırarak yeniden etkinleştirebilirsiniz — `eklenti-yoneticisi` iş akışı devre dışı bırakılmış bir eklentiyi tanır ve yeniden adlandırmayı geri çevirir.

> Detaylı kaldırma, devre dışı bırakma ve yeniden etkinleştirme iş akışları `eklenti-yoneticisi` referans eklentisinde yaşar — esaslı bir işlem yapmadan önce onu yükleyin.
