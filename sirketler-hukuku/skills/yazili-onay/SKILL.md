---
name: yazili-onay
description: >
  Kurum formatında, karar/onay havuzundan (repository) emsal arayarak 
  yönetim kurulu veya komite için oybirliğiyle alınmış yazılı karar (TTK m.390/7) 
  taslağı hazırlar. Çoklu kararları, üye çıkar çatışmalarını, yasal bildirim gerekliliklerini 
  ve imza takibini yönetir; büyük işlemlerde kapsam uyarısı yapar. Kullanıcı "yazılı onay", 
  "yazılı karar", "elden dolaştırma yoluyla karar", "YK kararı" dediğinde kullanın.
argument-hint: "[YK onayı gerektiren işlemi açıklayın]"
---

# /yazili-onay

1. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` yükle → Kurul & Sekreterya (onay havuzu, karar dili, YK yapısı).
2. Aşağıdaki iş akışını kullan.
3. Eylemi tanımla ve sınıflandır (rutin / inceleme gerektiren).
4. İnceleme gerektiren (büyük) işlemse: Dış avukat uyarısını göster ve devam etmeden önce onayla.
5. Karar havuzunda en yakın emsali (precedent) ara. Havuz yoksa: `CLAUDE.md` içindeki tohum örnekleri kullan.
6. Emsali temel alarak kurum formatında karar taslağı oluştur.
7. Çıktı: Karar taslağı + imza listesi (checklist) + inceleme hatırlatıcıları.

---

## Dosya (Matter) Bağlamı

`CLAUDE.md` içindeki `## Dosya çalışma alanları`nı kontrol et. Eğer etkinse ve aktif dosya yoksa sor: "Bu hangi dosya için? `/sirketler-hukuku:dosya-calisma-alani degistir <slug>` çalıştır." Çıktıları `matters/<dosya-slug>/` klasörüne yaz.

---

## Amaç

Rutin yönetim kurulu onaylarının çoğu için toplantıya gerek yoktur (TTK m.390/7 uyarınca elden dolaştırma/yazılı karar). Müdür atamaları, imza sirküleri güncellemeleri, banka yetkileri, belirli eşiğin üzerindeki sözleşmeler. Bu yetenek (skill) bunları kurum formatında hızla taslaklar.

> **[UZMAN DOĞRULA] - Türk Hukuku Notu:** TTK m.390/7 uyarınca, üyelerden hiçbiri toplantı yapılmasını istemediği takdirde, kararlar yazılı onay (elden dolaştırma) yoluyla alınabilir. Bu usulde tüm üyelerin aynı öneriye yazılı onay vermesi veya hepsinin imzasının bulunduğu tek bir belgenin olması gerekir. Taslak üretilirken, bu TTK kuralının sağlandığı varsayılır ancak bağlayıcılık avukat teyidine tabidir.

## Kapsam Uyarısı — Taslaklamadan Önce Oku

> **Bu yetenek, havuzunuzdaki veya tohum belgelerinizdeki (seed) emsallere uyan günlük onaylar için tasarlanmıştır.**
>
> **Büyük işlemler için dış avukat (outside counsel) incelemesi ihtiyat gereğidir:** M&A, yeni finansman turları, yeni yatırımcıya pay ihracı (sermaye artırımı), tasfiye vb. Yetenek bunu tespit ettiğinde otomatik olarak uyarır.

---

## Adım 1: Eylemi tanımla

Kullanıcıya YK'nın neyi onaylaması gerektiğini sor. Topla:
- **Ne onaylanıyor?** (Tek cümle)
- **Detay:** Atanan müdürün adı, sözleşme bedeli vb.
- **Yürürlük tarihi:** Bugün mü, geçmiş/gelecek mi?
- **İmzacı:** Tüm YK mı, özel komite mi?
- **Çıkar çatışması:** Herhangi bir YK üyesinin bu işlemde menfaati var mı? (TTK m.393 uyarınca müzakereye/oylamaya katılma yasağı).

### Eylem sınıflandırması

**Rutin — emsal muhtemel:**
- Müdür/yetkili ataması (İmza sirküleri)
- Banka hesap yetkisi
- Rutin ticari sözleşme onayı

**İnceleme (Review flag) — dış avukat ihtiyatlı olur:**
- M&A işlemi (birleşme, bölünme, devralma)
- Sermaye artırımı / Finansman
- Şirketin tasfiyesi veya konkordato
- Gayrimenkul alım/satımı (büyük ölçekli)

İnceleme kategorisindeyse şu uyarıyı göster:
> ⚠️ **Dış avukat incelemesi önerilir.** Bu, [eylem türü] gibi büyük bir kurumsal eyleme benziyor. Dolaşıma sokmadan önce dış avukata inceletmeyi düşünün. Yine de taslağa devam edeyim mi?

---

## Adım 2: Emsal ara

Kurumun onay havuzunda "müdür ataması", "banka yetkisi" gibi anahtar kelimelerle ara. En yakın olanı kullan. Yoksa `CLAUDE.md` içindeki tohum (seed) formatı baz al ve kullanıcıya havuz bulunamadığını söyle.

---

## Adım 3: Kararı Taslakla

Kurum formatını kullan. Genel TTK m.390/7 taslak yapısı (emsaldeki dili harfiyen kopyala):

```
[ŞİRKET ADI]
YÖNETİM KURULU KARARI

Karar Tarihi: [Tarih]
Karar No: [Yıl/Sıra]
Toplantıya Katılanlar: [Tüm üyeler - TTK m.390/7 elden dolaştırma]

Şirket Yönetim Kurulu şirket merkezinde toplanarak aşağıdaki kararları almışlardır:

1. [Arka plan / Gerekçe]
2. [Kararın kendisi - Kesin ve net ifadeler kullanın. "İşlemin onaylanmasına" yerine "A Şirketi ile B Şirketi arasındaki [Tarih] tarihli [Sözleşme Adı]'nın onaylanmasına..."]

[İmza Blokları - YK üyeleri]
```

### Taslaklama notları
- **Kesin olun.** "İşlemi onayladı" işe yaramaz. Belgenin adını, tarihini ve tarafını belirtin.
- **Yetkilileri adlandırın.** Kimin imza yetkisi olacağını (münferiden mi müştereken mi) kurum diline uygun belirtin.

---

## Adım 4: Yasal bildirimleri ve usulleri teyit et

- TTK m.390/7 uyarınca fiziki toplantı yapılmaksızın karar alınabilmesi için önerinin **tüm üyelere** yapılmış olması şarttır.
- Kararın ticaret siciline tescili gerekip gerekmediğini (örn. imza yetkilisi atanması tescile tabidir) avukata bırak.

---

## Adım 5: Çıktı

1. **Karar Taslağı**
2. **İmza Listesi (Checklist):**
   ```
   Gerekli imzalar (Oybirliği veya çoğunluk):
   □ [Üye Adı 1]
   □ [Üye Adı 2]
   ```
3. **İnceleme Hatırlatıcıları:**
   ```
   DOLAŞIMA SOKMADAN ÖNCE - Kontrol edin:
   □ Karar dili eylemi kesin olarak tanımlıyor mu?
   □ Tescil/ilan gerekiyor mu? (MERSİS)
   □ TTK m.393 uyarınca çatışma (menfaat uyuşmazlığı) beyan edildi mi?
   ```

> **Taslak Üzerine Son Not:** Bu, avukat incelemesi için bir taslaktır. Kabul edilmesi şirketi bağlar. Bir avukatın incelemesi olmadan imzaya sunmayın.
