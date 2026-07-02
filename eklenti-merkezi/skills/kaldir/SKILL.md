---
name: kaldir
description: >
  Merkez aracılığıyla kurulan bir topluluk eklentisini kaldırır. Dosyaları silmeden önce onay alır, birinci taraf eklentilere dokunmayı reddeder ve her eylemi günlüğe kaydeder. Kullanıcı bir eklentiyi sadece devre dışı bırakmak yerine tamamen kaldırmak istediğinde ("kaldır [eklenti]", "bu eklentiyi sil") kullanın.
argument-hint: "[eklenti adı]"
---

# /kaldir

Belirtilen eklenti (skill) için referans olan `eklenti-yoneticisi` eklentisindeki `uninstall` (kaldır) iş akışını çalıştırın.

Güvenlik kuralları:

1. **Yalnızca bu merkez üzerinden kurulan topluluk eklentilerini kaldırın.** `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/install-log.yaml` dosyasını ve CLAUDE.md kurulu başlangıç paketi tablosunu kontrol edin. Eğer eklenti oralarda kayıtlı değilse, reddedin ve kullanıcıya söyleyin.
2. **Asla birinci taraf bir eklentinin (plugin'in) skill'ini kaldırmayın.** `claude-for-legal-turkish` ile birlikte gelen temel eklentiler bu komut için ulaşılamazdır. Belirtilen eklenti bu eklentilerden birinin içindeki bir yola çözülürse reddedin.
3. **Dosyaları kaldırmadan önce onay alın.** Silinecek her yolu kullanıcıya gösterin. Yalnızca açıkça verilen `evet` durumunda ilerleyin.
4. **Kaldırma işlemini günlüğe kaydedin.** Denetim izinin (audit trail) bozulmaması için `install-log.yaml` dosyasına `action: uninstall` ve zaman damgasıyla birlikte ekleyin.

Kullanıcı bir eklentinin çalışmasını durdurmak ancak dosyaları saklamak isterse (örneğin, daha sonra yeniden etkinleştirmek veya yapılandırmayı korumak için), bunun yerine `/eklenti-merkezi:devre-disi-birak` komutunu önerin.

> Detaylı kaldırma, devre dışı bırakma ve yeniden etkinleştirme iş akışları `eklenti-yoneticisi` referans eklentisinde yaşar — esaslı bir işlem yapmadan önce onu yükleyin.
