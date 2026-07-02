---
name: yonetim-kurulu-tutanagi
description: >
  Kurum formatında yönetim kurulu veya komite toplantı tutanakları taslaklar. 
  Takviminizden yaklaşan YK toplantılarını otomatik algılar, gündemi ve 
  sunumları (pre-read) ister ve tohum tutanaklardan öğrendiği formatta tam bir 
  taslak üretir. Kullanıcı "yönetim kurulu tutanağı", "tutanak taslakla", 
  "yaklaşan YK toplantısı" dediğinde kullanın.
---

# /yonetim-kurulu-tutanagi

1. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` yükle → Kurul & Sekreterya bölümü.
2. Takvim entegrasyonu varsa toplantıyı bul veya kullanıcıdan detayları iste.
3. Yoklama, gündem ve materyalleri al.
4. Kurum formatında tutanak taslağını oluştur.
5. `[UZMAN DOĞRULA]` uyarılarını ve çıktı onay kapısını (gate) ekle.

---

## Dosya (Matter) Bağlamı

`CLAUDE.md` içindeki `## Dosya çalışma alanları`nı kontrol et. Eğer etkinse ve aktif dosya yoksa sor. Çıktıları `matters/<dosya-slug>/` klasörüne yaz.

---

## Amaç

Yönetim kurulu tutanakları yasal bir kayıttır (TTK m.390/6). İlerideki bir M&A due diligence sürecinde veya yasal denetimde incelemeye dayanacak şekilde doğru ve eksiksiz olmalıdır. Bu yetenek, formatlama yerine inceleme ve düzeltmeye zaman ayırmanız için tutanakları kurum formatında (house format) taslaklar.

> **[UZMAN DOĞRULA] - Türk Hukuku Notu:** TTK m.390/6 uyarınca yönetim kurulu toplantılarında kararların geçerli olabilmesi için tutanağa geçirilmesi ve altının toplantı başkanı ve üyeler tarafından imzalanması şarttır. Bu yetenek bir taslak üretir; toplantı yeter sayısı (nisap), geçerli imza prosedürleri ve sicil tescil (MERSİS) işlemleri bir hukukçu tarafından doğrulanmalıdır.

---

## Adım 1: Toplantıyı Belirle

Takvim bağlayıcısı yetkiliyse, YK ve komite anahtar kelimeleriyle (Yönetim Kurulu, Denetim Komitesi, Riskin Erken Saptanması Komitesi vb.) yaklaşan (30 gün) veya geçmiş (14 gün) toplantıları ara.
Kullanıcıya sor: "Gündeminizde şu toplantıları buldum... Hangisi için tutanak hazırlıyoruz?"
Değilse doğrudan sor: Toplantı türü, tarihi, saati, yeri (fiziki/online).
Çağrı usulü: Usulüne uygun çağrı yapıldı mı? (TTK'ya veya iç yönergeye göre)

## Adım 2: Katılım (Yoklama)

Katılımcı listesini sor veya takvim davetinden çek (onaylıysa).
- **Katılan/Katılmayan Üyeler:** Nisap için önemli.
- **Toplantı Başkanı:** Kim başkanlık etti? (TTK m.390 uyarınca tutanağın başkanca imzalanması şart).
- **Misafirler:** Yöneticiler, dış avukatlar, danışmanlar.

> **Toplantı ve Karar Nisabı (Quorum):** TTK m.390/1 uyarınca, esas sözleşmede aksine ağırlaştırıcı bir hüküm yoksa, YK üye tam sayısının çoğunluğu ile toplanır ve hazır bulunanların çoğunluğu ile karar alır. Nisap yoksa dur, kullanıcıyı uyar.

## Adım 3: Materyaller

Gündem ve toplantı öncesi okuma materyallerini (sunumlar vb.) iste. Bunlardan şunları çıkar:
- Gündem maddeleri
- Oylamaya sunulan kararlar ("onaylanması", "yetkilendirilmesi" gibi)
- Referans verilen ekler (finansal raporlar, değerlemeler vb.)

## Adım 4: Tutanağı Taslakla

`CLAUDE.md`'deki kurum formatını kullan. Asla jenerik formata dönme. Tohum belgeler (seed documents) şablondur.

### Standart Yapı (Kurum formatına uyarla)

```
[ŞİRKET ADI]
YÖNETİM KURULU TOPLANTI TUTANAĞI

Toplantı Tarihi: [Tarih]
Toplantı Yeri: [Fiziki yer / Online]

1. Açılış ve Yoklama
Toplantı, [Başkanın Adı] başkanlığında saat [saat]'te açıldı. Yapılan yoklamada, Yönetim Kurulu üyelerinden [Katılanlar]'ın hazır bulunduğu, TTK ve esas sözleşmede öngörülen toplantı nisabının mevcut olduğu anlaşıldı.

2. [Gündem Maddesi 1]
[Başkan/Sunucu], [Konu] hakkında bilgi verdi. Kurul üyeleri konuyu değerlendirdi.

Karar: Görüşmeler sonucunda, [Karar Metni - Tohum belgedeki dili kullan] oybirliği / oy çokluğu ile karar verildi.

3. Kapanış
Gündemde görüşülecek başka madde kalmadığından, toplantı saat [saat]'te başkan tarafından kapatıldı.

[İmzalar - Toplantı Başkanı ve Üyeler]
```

### Taslaklama Notları
- **Tartışma Özetleri:** Tutanak dilinin ne kadar detaylı olacağı kurum tercihidir. Sadece kararları yazan (action minutes) bir sisteminiz varsa, gereksiz hikaye yazma.
- **Kararlar (Resolutions):** Tohum tutanaktaki dili (Karar, Karar Verildi, Onaylandı vb.) aynen kopyala.
- **Bilgi Eksikse:** `[YER TUTUCU - Tartışma özetini buraya yazın]` şeklinde işaret bırak, içerik uydurma.

## Adım 5: Sonuç Doğuran Eylem Kapısı (Tutanağı Kesinleştirme)

**Avukat Olmayanlar İçin Uyarı:**
> Yönetim kurulu tutanağının kabul edilmesi, onu YK kararlarının resmi (hukuki) kaydı yapar. Bunu bir avukatla veya kurum içi hukuk müşaviriyle incelediniz mi? Bu bir taslaktır. Hatalı ifadeler M&A sürecinde sorun yaratabilir.

## Adım 6: Çıktı ve İnceleme Listesi

Tutanağı üret ve altına bir inceleme listesi (checklist) ekle:

```
İNCELEME LİSTESİ — Dolaşıma sokmadan önce doğrulayın:
□ Katılan/katılmayan üyeler (nisap) doğru mu?
□ Karar dili (TTK ve esas sözleşmeye uygun mu)?
□ Oylar (muhalefet şerhi var mı) doğru kaydedilmiş mi?
□ TTK m.393 (menfaat uyuşmazlığı) kapsamında oylamaya katılmayan üye var mı?
□ Dış avukat / Kurum avukatı inceledi mi?
```
