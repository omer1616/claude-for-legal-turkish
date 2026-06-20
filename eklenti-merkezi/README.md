# Eklenti Merkezi (Legal Builder Hub) Eklentisi

Topluluk hukuk eklentilerini keşfetme ve kurma. GitHub kayıt depolarını (lpm-skills, [ek depolar — `/eklenti-merkezi:kayit-tarayici` ile ekleyin] ve diğerleri) tarar, kurar ve otomatik günceller, diğer hukuk eklentilerinizin içinde ilgili topluluk eklentilerini önünüze getirir. İlk kurulum görüşmesi AYNI zamanda başlangıç paketi önericisidir — pratik tipinizi sorar, ne kuracağınızı önerir.

**Her topluluk eklentisi kurulumdan önce ham haliyle önünüze konur, prompt-enjeksiyon kalıplarına karşı taranır ve Hukuk Eklentisi Tasarım Çerçevesi'ne göre değerlendirilir. Eklenti bulmanıza ve değerlendirmenize yardım eder; neye güveneceğinize siz karar verirsiniz.**

## Kimler için

Diğer hukuk eklentilerini kullanan herkes. Burası uygulama mağazası.

## İlk çalıştırma: ilk-kurulum

Pratik tipinizi, sektörünüzü, ekip büyüklüğünüzü, araç kullanım rahatlığınızı sorar. Eşleşen bir başlangıç topluluk eklentisi paketi önerir. Seçtiklerinizi kurar.

```
/eklenti-merkezi:ilk-kurulum
```

Yapılandırmanız `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` altında saklanır ve eklenti güncellemelerini atlatarak korunur.

## Güvenlik duruşu

Kurulan topluluk eklentileri; müvekkil verilerinize, dosya kayıtlarınıza ve ekibinizin oyun kitabına (playbook) sizin erişiminizle çalışır. Merkez, her kurulumu ve her güncellemeyi bir güven kararı olarak ele alır. Tek başına yeterli olmayan dört savunma katmanı:

- **İzin listesi (yönetici denetiminde):** `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/allowlist.yaml`, topluluk eklentilerinin hangi kayıt depolarını, yayıncıları ve MCP bağlayıcılarını kullanabileceğini belirler. `permissive` modu (varsayılan) liste dışı her şeyde uyarır; `restrictive` modu (firma/kurumsal kurulumlar için önerilir) reddeder. İzin listesi, kurucu herhangi bir üçüncü taraf içeriği okumadan önce kontrol edilir. Şema için bkz. `skills/eklenti-kurucu/references/allowlist.md`.
- **Özet değil, ham kaynak:** kurucu, herhangi bir şey yazılmadan önce size tam ham `SKILL.md`'yi gösterir — yapay zekâ özeti değil. Özet bir kolaylıktır; şüpheli bir iş yapan eklentinin bunu ham gösterimin ortaya çıkaracağı metinle yapması gerekir.
- **Sezgisel (heuristic) taramalar:** hem kurucu hem de `eklenti-kalite-kontrol`, eklentiyi prompt-enjeksiyon kalıplarına karşı tarar (yetki/üstünlük iddiaları, kapsam dışı okuma-yazmalar, dış URL'ler, gizli unicode, kabuk çalıştırma, kimlik bilgisi istekleri). Bunlar açıkça öyle etiketlenmiş yapay zekâ-sezgisel taramalardır — temiz bir tarama bir güvenlik denetimi değildir, metni kendiniz okumanız için bir uyarıdır.
- **Her seferinde insan onayı:** taze, elle yazılmış bir `evet` olmadan diske hiçbir şey yazılmaz. Onay önceki mesajlardan çıkarsanmaz. Derinlemesine savunma için kurucu, getirme/analiz işlemini salt-okunur bir alt-ajanda çalıştırmayı önerir; böylece Yazma yetenekleri ancak onaydan sonra kullanılabilir olur.

Güncellemeler aynı duruşu kullanır: otomatik güncelleyici değişebilen etiketlere değil commit SHA'larına sabitlenir, hook ve MCP değişiklikleri dâhil tam farkı gösterir ve her güncelleme için açık onay ister. Otomatik-uygula modu yoktur.

Bir eklenti kurulumdan sonra ters giderse: `/eklenti-merkezi:devre-disi-birak [eklenti]` dosyaları silmeden sustur; `/eklenti-merkezi:kaldir [eklenti]` tamamen kaldırır. İkisi de yalnızca bu merkez üzerinden kurulan topluluk eklentileriyle sınırlıdır — birinci taraf eklenti skill'lerine dokunmayı reddederler.

## Ön koşullar

- registry-sync ajanından gelen Slack bildirimleri, ortamınızda yapılandırılmış bir Slack MCP sunucusu gerektirir. Olmadığında ajan özetini bir dosyaya yazar.
- `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md`'deki varsayılan kayıt deposu listesi `lpm-skills` dışında boş gelir. Güvendiğiniz depoları `/eklenti-merkezi:kayit-tarayici` ile veya bu dosyayı düzenleyerek ekleyin.

## Komutlar

| Komut | Ne yapar |
|---|---|
| `/eklenti-merkezi:ilk-kurulum` | Pratik profili + başlangıç paketi önerisi |
| `/eklenti-merkezi:kayit-tarayici [sorgu]` | İzlenen depolarda eklenti arar |
| `/eklenti-merkezi:eklenti-kurucu [eklenti]` | Bir topluluk eklentisi kurar |
| `/eklenti-merkezi:otomatik-guncelleyici` | Kurulu eklentiler için güncelleme kontrol eder |
| `/eklenti-merkezi:ilgili-eklentiler` | Yaptığınız işe göre eklenti önerir |
| `/eklenti-merkezi:eklenti-kalite-kontrol [eklenti]` | Kurmadan önce bir eklentiyi Hukuk Eklentisi Tasarım Çerçevesi'ne göre değerlendirir |
| `/eklenti-merkezi:devre-disi-birak [eklenti]` | Kurulu bir topluluk eklentisini dosyalarını silmeden devre dışı bırakır |
| `/eklenti-merkezi:kaldir [eklenti]` | Merkez üzerinden kurulan bir topluluk eklentisini kaldırır |

## Skill'ler

| Skill | Amaç |
|---|---|
| **ilk-kurulum** | Pratik profili → başlangıç paketi |
| **kayit-tarayici** | İzlenen depolar genelinde arama |
| **eklenti-kurucu** | İzin-listesi kapısı, getirme, ham SKILL.md gösterimi, güven kontrolü, KK, topluluk eklentilerini kurma |
| **kaldir** | Merkez üzerinden kurulan bir topluluk eklentisini kaldırma (birinci taraf eklenti skill'leri kapsam dışı) |
| **devre-disi-birak** | Bir topluluk eklentisini dosyalarını silmeden devre dışı bırakma; sonra yeniden etkinleştirme |
| **eklenti-yoneticisi** | Referans: `kaldir` ve `devre-disi-birak` skill'lerinin kullandığı ayrıntılı kaldırma/devre-dışı/yeniden-etkinleştirme akışları |
| **eklenti-kalite-kontrol** | Bir eklentiyi Hukuk Eklentisi Tasarım Çerçevesi'ne göre değerlendirme — tasarım, hata modları, güven yüzeyi ve bir prompt-enjeksiyon sezgisel taraması |
| **otomatik-guncelleyici** | Güncelleme kontrol eder; farkı ve güven incelemesini gösterir; yalnızca açık onayla uygular |
| **ilgili-eklentiler** | Bir görevden sonra ilgili topluluk eklentilerini önüne getirir (doğrudan veya hook ile) |

## Etkileşimli komutlar vs. zamanlanmış ajanlar

Yukarıdaki komutlar siz çağırdığınızda çalışır — bir dosya üzerinde çalışırken. Aşağıdaki ajanlar bir zamanlamayla çalışır — siz bakmazken hareket edenler için:

| Ajan | Neyi izler | Varsayılan sıklık |
|---|---|---|
| **registry-sync** | İzlenen depolarda yeni ve güncellenen eklentiler; güncelleme tercihlerine göre bildirim gönderir | Haftalık |

## İzlenen kayıt depoları (varsayılan)

Varsayılan izin listesi, önceden incelediğimiz topluluk depolarını yapılandırılmış olarak getirir. Eklemek, çıkarmak veya restrictive/permissive modları arasında geçiş yapmak için repodaki `references/allowlist-default.yaml`'ı ya da kurulum başına izin listenizi (`~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/allowlist.yaml`) düzenleyin.

- **lpm-skills** — Hukuki proje yönetimi (Scott Margetts / LegalOps Consulting) — `github.com/legalopsconsulting/lpm-skills`
- **Lawvable / awesome-legal-skills** — Hukuk işleri için derlenmiş yapay zekâ ajan eklentileri listesi — `github.com/lawvable/awesome-legal-skills`
- **Lawvable / agent-skills** — Hukuk işleri için derlenmiş ajan eklentileri koleksiyonu — `github.com/lawvable/agent-skills`
- Kendi deponuzu `/eklenti-merkezi:kayit-tarayici` ile veya izin listesini düzenleyerek ekleyin

## Nasıl öğrenir

`~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md`'deki pratik profiliniz durağan değildir — eklentiyi kullandıkça gelişir. Merkez onu her `/eklenti-merkezi:kayit-tarayici` ve `/eklenti-merkezi:ilgili-eklentiler` çağrısında yeniden okur; böylece pratik tipinizi, sektörünüzü veya izlenen depolarınızı düzenlemek gelecekteki önerileri keskinleştirir. Dosyayı doğrudan düzenleyin veya işiniz değiştiğinde `/eklenti-merkezi:ilk-kurulum --redo` çalıştırın.

## Notlar

- Topluluk eklentileri kurulumdan önce okunur. Kabul etmeden önce **ham** SKILL.md'yi görürsünüz — özet değil.
- Otomatik güncelleme varsayılan olarak kapalıdır. Kaynağa güveniyorsanız eklenti başına açın.
- ilgili-eklentiler diğer eklentilerin içinde çalışır: bir görev yaparken, topluluğun ilgili bir şeyi olup olmadığını kontrol eder.
- Kurumsal/firma kurulumları: `allowlist.yaml`'da `mode: restrictive` ayarlayın ve `registries`, `publishers`, `connectors` listelerini doldurun. Restrictive modda kurucu, listede olmayan bir kaynaktan hiçbir şey getirmeyi, analiz etmeyi veya kurmayı reddeder.
