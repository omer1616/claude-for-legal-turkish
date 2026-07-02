---
name: ilgili-eklentiler
description: >
  Diğer eklentilerdeki son etkinliklere dayanarak topluluk eklentileri (skills) önerir. Topluluğun bir görevle ilgili bir şey inşa edip etmediğini kontrol eder ve rahatsız etmeden bir kez bahseder. Kullanıcı "bunun için bir topluluk eklentisi var mı", "başka neler var" dediğinde veya eklenti önerileri istediğinde kullanın; ayrıca diğer eklentilerin iş akışlarının bir parçası olarak pasif bir şekilde çalışır.
---

# /ilgili-eklentiler

1. `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` dosyasını yükleyin → pratik profili.
2. Aşağıdaki iş akışını kullanın.
3. Diğer eklentilerin neler yaptığını kontrol edin. Kayıtlarla (registry) eşleştirin.
4. Önerin: "X yapıyorsunuz — topluluğun bununla ilgili Y eklentisi var."

---

## Amaç

Topluluk tam da inşa etmek üzere olduğunuz şeyi inşa etmiş olabilir. Bu eklenti bunu fark eder ve bahseder — bir kez, kısaca, rahatsız etmeden.

## Nasıl çalışır

Bu eklenti bir görevden sonra ilgili topluluk eklentilerini yüzeye çıkarır. Kullanıcı tarafından doğrudan çağrılabilir ("X için başka ne var?") veya bir Stop kancası (hook) aracılığıyla diğer eklentilere bağlanabilir — kancaya dayalı model, diğer her eklentinin bu skill'i çağıran bir Stop kancası bildirmesini gerektirir; bu varsayılan olarak bağlı değildir. Kanca bağlantısı olmadan, doğrudan çağırın.

Diğer eklentiler bir görevin sonunda hafif bir kontrol içerebilir:
> "eklenti-merkezi bu tür bir şeyde yardımcı olabilecek bir topluluk eklentisi buldu: [isim] — [tek-satır]. Göz atmak ister misiniz?"

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` → pratik profili, kurulu eklentiler (zaten kurulu olanı önermeyin).
`kayit-tarayici`'dan (registry-browser) kayıt önbelleği.

## Eşleştirme

Bir görev açıklaması (kullanıcının az önce ne yaptığı) verildiğinde, şunlarla eşleşen kayıt (registry) eklentilerini bulun:

- Görev ve eklenti açıklamaları arasındaki anahtar kelime örtüşmesi
- Pratik profil uyumu (işlemsel bir avukata dava eklentileri önermeyin)
- Halihazırda kurulu olmaması

**Eşik:** Sadece eşleşme güçlüyse yüzeye çıkarın. Zayıf eşleşmeler gürültüdür. Rahatsız etmektense hiçbir şeyi yüzeye çıkarmamak daha iyidir.

## Çıktı

Eğer güçlü bir eşleşme varsa:
> 💡 Topluluğun bunun için bir eklentisi var: [kayıt]'tan **[isim]** — "[açıklama]". Denemek için `/eklenti-merkezi:eklenti-kurucu [isim]`.

Eğer güçlü bir eşleşme yoksa: sessiz. Çıktı yok. "Hiçbir şey bulamadım" diye duyurmayın.

## Frekans sınırı

Aynı eklentiyi iki kez yüzeye çıkarmayın. Kullanıcı onu ilk seferinde kurmadıysa, görmüş ve hayır demiştir. Reddedilenleri `references/surfaced.json` içinde takip edin.

## Kullanıcı kontrolü

`~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` → yeni eklenti bildirimlerine göre:
- **Hepsi (All):** Herhangi bir eşleşmeyi yüzeye çıkarın
- **Pratik profiliyle eşleşenler:** Profile göre filtreleyin (varsayılan)
- **Hiçbiri (None):** Bu skill kapalıdır

## Sonraki adımlar karar ağacıyla kapatın

CLAUDE.md `## Çıktılar` (Outputs) bölümüne göre sonraki adımlar karar ağacıyla bitirin. Seçenekleri bu skill'in az önce ürettiği şeye göre özelleştirin — beş varsayılan dal (X'i taslakla, eskale et, daha fazla olgu topla, izle ve bekle, başka bir şey) kilitli bir şey değil, başlangıç noktasıdır. Ağaç çıktının kendisidir; avukat seçer.

## Bu eklentinin yapmadığı şeyler

- Herhangi bir şeyi kurmak.
- Devam eden bir görevi kesintiye uğratmak. Yüzeye çıkarma, bir görevin ortasında değil, *sonunda* gerçekleşir.
- Dır dır etmek. Eklenti başına bir bahsetme.
