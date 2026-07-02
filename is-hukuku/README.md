# İş Hukuku Eklentisi

Şirket içi iş hukuku iş akışları: işe alım incelemesi, iç soruşturma
yönetimi, izin takibi, çalışma kılavuzu güncellemeleri ve uluslararası
genişleme desteği. İlk-kurulum görüşmesinin yazdığı bir ekip pratik profili
etrafında kurulmuştur — eklenti *sizin* yargı çevresi ayak izinizi ve
eskalasyon kurallarınızı öğrenir, genel bir şablonu değil.

**Her çıktı avukat incelemesi için taslaktır — atıflı, işaretli ve kapılı —
hukuki sonuç değil.** Eklenti işi yapar: belgeleri okur, pratik profilinizi
uygular, sorunları bulur, notu taslak haline getirir. Bir avukat inceler,
doğrular ve karar verir. Atıflar kaynağına göre etiketlenir, böylece
hangisinin bir araştırma aracından geldiğini ve hangisinin kontrol edilmesi
gerektiğini bilirsiniz. Meslek sırrı işaretleri temkinli uygulanır ki
hiçbir şey yanlışlıkla feragat edilmesin. Sonuç doğuran eylemler —
işe alım teklifi göndermek, bir soruşturmayı kapatmak, dış bir cevap
göndermek — açık onay arkasında kapılıdır.

## Kademe durumu — önemli

Bu eklenti **karma kademelidir**:

- **17 A-kademesi skill** (bu README'de listelenmiştir) **taşınmıştır** —
  saf iş akışı iskeletleri, yargı-çevresi-nötr tasarlanmış, Türk iş hukuku
  bağlamına uyarlanmış.
- **3 B-kademesi skill henüz taşınmamıştır**: `isten-cikartma-inceleme`
  (kaynak: `termination-review`), `ucret-saat-sss` (kaynak:
  `wage-hour-qa`), `calisan-siniflandirma` (kaynak:
  `worker-classification`). Bunlar ABD mevzuatına (FMLA/OWBPA/WARN, FLSA,
  "ABC testi") doğrudan bağlıdır ve 4857 sayılı İş Kanunu çerçevesinde
  (ihbar/kıdem tazminatı, iş güvencesi, fazla mesai, işçi/alt işveren
  sınıflandırması) bir Türk iş hukukçusu tarafından komple yeniden
  tasarlanmayı bekliyor. Durumları için `.claude/MIGRATION.md` B kademesi
  bölümüne bakın.

Bu üç skill taşınana kadar, işe alım ve fesih incelemesinin sınıflandırma
ve fazla mesai boyutlarına dokunan adımlar `ise-alim-inceleme` skill'i
içinde `[doğrulanacak]` olarak işaretlenmiştir.

## Kimler için

| Rol | Birincil iş akışları |
|---|---|
| **İş hukuku danışmanı** | İşe alım incelemesi, iç soruşturma yönetimi, politika taslaklama |
| **İK iş ortakları** | İşe alım incelemesi, çalışma kılavuzu soruları, izin kaydı |
| **BHM (Baş Hukuk Müşaviri)** | Yüksek riskli işaretler ve toplu işten çıkarmalar için eskalasyon alıcısı |

## İlk çalıştırma: ilk-kurulum

İlk kullanımda eklenti sizi görüşür — on dakika, sohbet havasında —
çalışanı olduğunuz ülkeleri ve sektörleri sorar, çalışma kılavuzunuzu ve
üç son iş hukuku belgesini okur, yargı çevresine duyarlı bir eskalasyon
tablosu oluşturur.

```
/is-hukuku:ilk-kurulum
```

Yapılandırmanız
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
dosyasında saklanır ve eklenti güncellemelerini atlatarak korunur.

## Ön koşullar

- **Kalıcı veri yolu.** İzin kaydı, soruşturma günlükleri ve genişleme
  izleyicileri
  `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/` altına
  yazılır — eklenti güncellemelerinden etkilenmeyen bir yol. Bu dosyalar
  meslek sırrı kapsamında ve hassas özlük bilgisi içerir — bu dizinin
  yedeklendiğinden ve erişiminin kontrollü olduğundan emin olun.
- **Hukuki araştırma erişimi.** Bu eklentideki skill'ler kasıtlı olarak
  esaslı hukuki kuralları (rekabet yasağı uygulanabilirliği, izin
  hakları, fesih son tarihleri, ülkeye özgü istihdam çerçeveleri vb.)
  saklamaz. Her yargı çevresine özgü kural, inceleme anında araştırılır ve
  atıf yapılır. Oturumun güvendiğiniz araştırma araçlarına (web araması,
  dahili hukuki araştırma entegrasyonları, ekip referans malzemeleri,
  Lexpera/Kazancı/UYAP/mevzuat.gov.tr) erişimi olduğundan emin olun.
- **Dış avukat.** Herhangi bir sınırda çağrı veya yeni yargı çevresinde,
  dış avukat görevlendirmesi olmadan ülkeye özgü hukuki tavsiye üretilmez.

## Skill'ler (17 A-kademesi + 1 agent)

| Skill | Yapar |
|---|---|
| **ilk-kurulum** | İlk çalıştırma görüşmesi — `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` dosyasını yazar |
| **sorusturma-ac** | Yeni bir iç soruşturma dosyası açar — intake, kaynak kontrol listesi, kalıcı günlük |
| **sorusturma-ekle** | Açık bir soruşturmaya belge/görüşme notu/gözlem ekler, önemli kalemleri yüzeye çıkarır |
| **sorusturma-sorgu** | Soruşturma günlüğüne karşı soru sorar — tanık ifadeleri, çelişkiler, boşluklar |
| **sorusturma-notu** | Meslek sırrı kapsamındaki soruşturma notunu taslaklar veya günceller |
| **sorusturma-ozeti** | Nottan hedef kitleye özel özet üretir — İK / yönetim / dış avukat |
| **ic-sorusturma** | Referans — yukarıdaki beş soruşturma skill'inin paylaşılan çerçevesi, doğrudan çağrılmaz |
| **izin-takibi** | Açık izinleri son tarih uyarıları için kontrol eder — durum panosu değil |
| **izin-kaydi** | İzin kaydına yeni bir izin ekler, ilk günden son tarihleri hesaplar |
| **uluslararasi-genisletme** | Referans — EOR vs. tüzel kişilik çerçevesi, dış avukat brifingleri, izleyici şeması |
| **genisletme-baslangic** | Yeni bir ülke için uluslararası genişleme projesini başlatır |
| **genisletme-guncelleme** | Devam eden bir genişleme izleyicisinin durumunu günceller |
| **calisma-kilavuzu-guncelleme** | Önerilen bir kılavuz değişikliğini mevcut sürümle karşılaştırır, dalga etkilerini işaretler |
| **ise-alim-inceleme** | Teklif mektubu ve rekabet yasağı hükümleri incelemesi, yargı çevresi kontrolü dahil |
| **politika-taslagi** | Bölge/birim ekleriyle bir iş hukuku politikası taslaklar |
| **dosya-calisma-alani** | Çok-müvekkilli pratikler için dosya çalışma alanları oluşturur, listeler, değiştirir ve kapatır |
| **ozellestir** | Pratik profilinin rehberli özelleştirmesi — tüm görüşmeyi yeniden çalıştırmadan tek bir şeyi değiştirir |

Referans skill'ler `ic-sorusturma` ve `uluslararasi-genisletme` ayrıntılı
çerçeveleri ve şablonları taşır — yukarıdaki mod-bazlı skill'ler bunları
gerektiğinde yükler.

### 🅱️ B kademesi — henüz taşınmadı

| Kaynak skill | Planlanan TR slug | Neden bekliyor |
|---|---|---|
| termination-review | `isten-cikartma-inceleme` | FMLA/OWBPA/WARN → 4857 ihbar/kıdem tazminatı, iş güvencesi (m.18-21), arabuluculuk zorunluluğu — komple yeniden tasarım gerekiyor |
| wage-hour-qa | `ucret-saat-sss` | FLSA → 4857 çalışma süreleri, fazla mesai (m.41, m.63-69) |
| worker-classification | `calisan-siniflandirma` | ABD "ABC testi" → 4857 m.2, alt işveren/bağımsız çalışan ayrımı, SGK yükümlülükleri |

## Etkileşimli komutlar vs. zamanlanmış ajanlar

Yukarıdaki komutlar siz çağırdığınızda çalışır — bir dosya üzerinde
çalışırken. Aşağıdaki agent siz bakmazken hareket eden şey için bir
zamanlamayla çalışır:

| Agent | Neyi izler | Varsayılan sıklık |
|---|---|---|
| **izin-izleyici** | Açık izinler — doğum/babalık, hastalık-rapor, askerlik sonrası yeniden işe alım, engellilik uyarlaması olarak izin; son tarihler kaçırılmadan önce karar noktası uyarıları ateşler | Haftalık (Pazartesi) |

Otomatik zamanlama ayrı bir entegrasyon gerektirir (takvim hatırlatıcısı,
cron işi vb.) — Claude Code agent'ları kendi kendini zamanlamaz.

## Entegrasyonlar

**Önce bir hukuki araştırma aracı bağlayın — atıf güvencesi buna
bağlıdır.** Olmadığında her atıf `[doğrulanacak]` etiketiyle işaretlenir ve
her çıktının üzerindeki inceleyen notu kaynakların doğrulanmadığını
kaydeder. Eklenti her iki durumda da çalışır; bir araştırma aracı
bağlandığında doğrulamayı sizin için yapar.

`.mcp.json` içinde yapılandırılmış bağlayıcılarla gelir:

- **Slack** — mesajları arar, kanalları okur, tartışmaları bulur (genel
  kova)
- **Google Drive** — belgeleri arar, okur ve getirir (genel kova)

Kaynak eklentideki İK sistemi (HRIS) bağlayıcıları (Workday, BambooHR,
Rippling, ADP) ABD'ye özgü ürünlerdi ve `.mcp.json`'a dahil edilmedi —
TR pazarında yaygın İK sistemleri (SAP SuccessFactors, Logo, Netsis vb.)
için bağlayıcı `[doğrulanacak — hangi TR İK sistemi MCP'lerinin mevcut
olacağı netleşince eklenecek]`. Bağlayıcı olmadan izin takibi
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/izin-kaydi.yaml`
dosyasına düşer.

Türk hukuku araştırması için önerilen kaynaklar: **mevzuat.gov.tr**,
**UYAP**, **Lexpera**, **Kazancı**.

## Hızlı başlangıç

### 1. Görüşülün

```
/is-hukuku:ilk-kurulum
```

On dakika. Çalışma kılavuzunuzu ve paylaşmaya hazır 10-20 son iş hukuku
belgesini (fesih notları, teklif mektupları, kıdem tazminatı anlaşmaları)
bulundurun.

Yapılandırmanız
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
dosyasında saklanır ve eklenti güncellemelerini atlatarak korunur.

### 2. Bir teklifi incele

```
/is-hukuku:ise-alim-inceleme teklif-mektubu.pdf
```

Çıktı: yargı çevresi kontrolü, rekabet yasağı uygulanabilirlik analizi ve
eylem kalemleriyle bir işe alım incelemesi notu.

### 3. Bir iç soruşturma aç

```
/is-hukuku:sorusturma-ac
Ankara ofisinde bir yöneticiye karşı taciz şikayeti dosyalandı.
```

Çıktı: meslek sırrı kapsamında bir soruşturma günlüğü, kaynak kontrol
listesi ve dosya yapısı.

### 4. Açık izinleri kontrol et

```
/is-hukuku:izin-takibi
```

Çıktı: yalnızca karar veya eylem gerektiren izinler, nedeniyle birlikte.

## Nasıl öğrenir

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
adresindeki pratik profiliniz statik değildir — eklentiyi kullandıkça
gelişir. Skill'ler bir çıktı ayarlaman gereken bir varsayılan
kullandığında size söyler. Kurulumu yeniden çalıştırabilir, dosyayı
doğrudan düzenleyebilir veya `/is-hukuku:ozellestir` ile tek bir şeyi
değiştirebilirsiniz.

## Dosya yapısı

```
is-hukuku/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                    # Ekip pratik profiliniz — ilk-kurulum tarafından yazılır, sizin tarafınızdan düzenlenir
├── README.md
├── agents/
│   └── izin-izleyici.md
├── skills/
│   ├── ilk-kurulum/
│   ├── sorusturma-ac/
│   ├── sorusturma-ekle/
│   ├── sorusturma-notu/
│   ├── sorusturma-sorgu/
│   ├── sorusturma-ozeti/
│   ├── ic-sorusturma/
│   ├── izin-takibi/
│   ├── izin-kaydi/
│   ├── uluslararasi-genisletme/
│   ├── genisletme-baslangic/
│   ├── genisletme-guncelleme/
│   ├── calisma-kilavuzu-guncelleme/
│   ├── ise-alim-inceleme/
│   ├── politika-taslagi/
│   ├── dosya-calisma-alani/
│   └── ozellestir/
└── hooks/hooks.json
```

## Notlar

- Yargı çevresi farkındalığı, kaynak eklentinin tüm noktasıydı (ABD
  eyaletleri arasındaki farklar). Türkiye'de iş hukuku büyük ölçüde
  ulusal düzeyde tektir (4857 sayılı Kanun); asıl varyasyon sektöre göre
  uygulanacak rejimden (Deniz İş Kanunu, Basın İş Kanunu, genel hükümler)
  ve yurt dışı şubelerden gelir. Bu eklenti buna göre yeniden
  çerçevelenmiştir — bkz. CLAUDE.md `## Yargı çevresi ayak izi`.
- İç soruşturma çerçevesi yargı-çevresi-nötr bir prosedür iskeletidir
  (tanık görüşmesi, belge toplama, rapor yazımı); ABD'ye özgü kavramlar
  (Upjohn uyarısı, Weingarten hakları, Garrity doktrini) TR karşılıklarına
  `[doğrulanacak]` etiketiyle işaretlenmiştir.
- İzin türleri profil değişkenidir — kaynak eklentideki ABD izin
  rejimleri (FMLA, CFRA, USERRA, ADA) yerine TR izin türleri (yıllık
  izin, doğum/babalık izni, hastalık-rapor, mazeret izni) profile örnek
  olarak eklenmiştir.
- Uluslararası genişleme skill'i hem "Türk şirketin yurt dışına açılması"
  hem "yabancı şirketin Türkiye'ye girişi" senaryolarını kapsayacak
  şekilde tasarlanmıştır — intake bu yönü sorar.
- Bu eklentideki 3 B-kademesi skill (`isten-cikartma-inceleme`,
  `ucret-saat-sss`, `calisan-siniflandirma`) henüz taşınmamıştır. Durumları
  için `.claude/MIGRATION.md` bakın.
