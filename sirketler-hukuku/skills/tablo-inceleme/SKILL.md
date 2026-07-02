---
name: tablo-inceleme
description: >
  Tablo incelemesi — belge başına bir satır, veri noktası başına bir sütun, 
  her hücre kaynağa atıflı. M&A due diligence için oluşturulmuştur 
  ("bu 200 hedef şirket sözleşmesini kontrol değişikliği, devir ve MAC klozları için incele") 
  ancak sonunda bir elektronik tablo (Excel) gerektiren herhangi bir toplu inceleme için çalışır. 
  Kullanıcı "tablo incelemesi", "inceleme tablosu", "bir tablo oluştur", 
  "bu alanları bu sözleşmelerden çıkar", "bu belgeleri X, Y, Z için incele", 
  "bana bir Excel ver", "toplu inceleme" dediğinde veya bir klasörü işaret edip 
  belgeleri karşılaştırmanızı istediğinde kullanın.
---

# /tablo-inceleme

1. `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` dosyasını yükle → due diligence yapısı, eşikler, ev formatı.
2. Doğrula: Hangi belgeler, hangi sütunlar, çıktı nereye gidecek?
3. Tiplenmiş şemayı oluştur. `.inceleme-semasi.yaml` dosyasını yaz. Kullanıcı ile onayla.
4. Örnek çalıştırma (3–5 belge). Şemayı ayarla. Onayla.
5. Dağıl — her belge için bir alt-ajan (sub-agent), paralel. Her hücre: değer + durum + birebir alıntı + konum.
6. Normalizasyon aşaması. Aykırı değerleri ve tutarsızlıkları işaretle.
7. Çıktı: `.xlsx` veya Google Sheets (hangisi olduğunu sor), artı her zaman `.csv` + `_kaynaklar.csv` + markdown. İş-ürünü başlığı ekle.
8. Özet: Doğrulama iş yükü (sütun başına `yok` / `belirsiz` / `inceleme_gerekli` sayıları), işaretli sütunlar, dosyaların konumu, her hücrenin bir bulgu değil bir ipucu olduğuna dair hatırlatma.

```
/sirketler-hukuku:tablo-inceleme
/sirketler-hukuku:tablo-inceleme --schema .inceleme-semasi.yaml --docs ./vdr/02-Sozlesmeler/
/sirketler-hukuku:tablo-inceleme --template ma-diligence
```

**`--schema <yol>`:** Yeni bir şema oluşturmak yerine mevcut bir şema dosyasını kullanır. Yeniden çalıştırmalar için kullanışlıdır.
**`--template <isim>`:** `references/` içindeki bir şablondan başlar. Şu an mevcut: `ma-diligence`.
**`--docs <yol>`:** Belge kaynağı. Yerel klasör, Drive klasör ID'si veya VDR yolu. Belirtilmezse sorar.
**`--output <xlsx|gsheets|csv>`:** Çıktı formatı. Belirtilmezse sorar.
**`--sample <n>`:** Şema kontrolü için örnek boyutu. Varsayılan 5.

---

## Dosya (Matter) Bağlamı

`CLAUDE.md` içindeki `## Dosya çalışma alanları`nı kontrol et. Eğer `Etkin` değilse (şirket-içi kullanıcılar için varsayılan), bu paragrafın geri kalanını atla. Eğer etkinse ve aktif dosya yoksa sor: "Bu hangi dosya (matter) için? `/sirketler-hukuku:dosya-calisma-alani degistir <slug>` çalıştır." Dosyaya özel bağlam için `matter.md` dosyasını yükle. Çıktıları `matters/<dosya-slug>/` klasörüne yaz.

---

## Amaç

Elinizde bir yığın belge ve her birinde tutarlı bir şekilde yanıtlanması gereken bir liste soru var. Due diligence talep listesi, tedarikçi sözleşmesi denetimi, kira portföyü incelemesi. Çıktı bir tablodur: belge satırları, veri noktası sütunları ve kaynaktaki tam kelimelere kadar izlenebilen her bir hücre.

Bu sorun çıkarma (issue spotting) **değildir**. `due-diligence-sorun-cikartma` 2.000 belgede saklanan 30 sorunu bulur. Bu yetenek (skill) ise 2.000 belgenin tamamı hakkında aynı 15 soruyu yanıtlar. Her ikisi de meşrudur; farklı soruları yanıtlarlar.

Bu ayrıca belgeyi okuyan bir insanın yerini tutmaz. Ürettiği her hücre **doğrulanması gereken bir ipucudur**, kesin bir bulgu değil. Çıktı, atlamayı değil doğrulamayı hızlandırmak için tasarlanmıştır.

## İçerik Yükle

- `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/CLAUDE.md` → yapı, eşikler, format tercihleri.
- `~/.claude/plugins/config/claude-for-legal-turkish/sirketler-hukuku/deals/[kod]/deal-context.md` (belirli bir işlemde çalışılıyorsa).
- Varsa mevcut şema dosyası (`.inceleme-semasi.yaml`).

## Sütun Tip Sistemi

Her sütunun yanıt formatını kısıtlayan bir **tipi** vardır:

| Tip | Ne döndürür | Kullanım alanı |
|---|---|---|
| `birebir` | Belgeden tam alıntı | Tanımlı terimler, operatif hüküm dili, kelimelerin önemli olduğu yerler |
| `siniflandir` | Belirlediğiniz sabit bir listeden tek bir değer | Evet/Hayır, var/yok, madde varyantları (ör. "tek taraflı onay" / "onay makul olmayan şekilde esirgenemez" / "sessiz") |
| `tarih` | ISO tarih | Yürürlük tarihi, bitiş, fesih ihbar süresi |
| `sure` | Sayı + birim | Sözleşme süresi, bildirim süresi, ayakta kalma süresi |
| `para` | Sayı + para birimi kodu | Üst sınırlar, eşikler, ücretler, satın alma bedeli referansları |
| `sayi` | Sadece sayı | Sayımlar, yüzdeler, sayfa referansları |
| `serbest` | Kısa serbest metin özeti | Seyrek kullanın — bu kayan/değişen tiptir. |

**Birebir Kuralı:** `birebir` (verbatim) olmayan her sütun, yanıtı destekleyen tam kaynak alıntıyı yol arkadaşı bir alan olarak yakalar. Hücredeki yanıt yorumdur; alıntı kanıttır. Kaynak cümle olmadan "onay makul olmayan şekilde esirgenemez" diyen bir `siniflandir` hücresi işe yaramazdır.

## "Bulunamadı"nın 3 Durumu

Boş bir hücre bilgiyi saklar. Olumlu bir yanıt üretemediğinizde her zaman şu üç açık durumdan birini kullanın:

| Durum | Anlamı | Ne zaman kullanılır |
|---|---|---|
| `yok` | Belge okundu ve hüküm yok. | Konunun ele alınmadığından eminsiniz. |
| `belirsiz` | Bir şey var ama güvenle sınıflandıramıyorsunuz. | Belirsiz yazım, kısmi hüküm, çelişkili maddeler. |
| `inceleme_gerekli` | Bir şey buldunuz ama bir insan karar vermeli. | Uç durum, olağandışı yazım, yanıt şemanın yakalayamayacağı bir yargıya dayanıyor. |

Bunlar 3 farklı bilgidir. Onları tek bir boş hücrede birleştirmek ayrımı kaybettirir.

## İş Akışı

### Adım 0: Ne ve nerede

1. **Belgeler:** Neredeler? Kaç tane? >200 ise bir önemlilik filtresi (materiality filter) öner.
2. **Şema:** Hangi sütunlar? Doğal dilde istenirse şemayı kur.
3. **Çıktı:** Excel mi Google Sheets mi? Sor. CSV ve markdown her zaman düşüş (fallback) olarak yazılır.

### Adım 1: Şemayı oluştur ve onayla

`.inceleme-semasi.yaml` dosyasına yaz. Dağılmadan önce kullanıcıya göster ve onayla.

```yaml
schema:
  name: "M&A Diligence — Proje [Kod]"
  created: 2026-05-07
  columns:
    - id: karsi_taraf
      label: "Karşı Taraf"
      type: birebir
      prompt: "Hedef şirket dışındaki sözleşme tarafı kimdir?"
    - id: yururluk_tarihi
      label: "Yürürlük Tarihi"
      type: tarih
      prompt: "Sözleşme ne zaman yürürlüğe girdi?"
    - id: kontrol_degisikligi
      label: "Kontrol Değişikliği (CoC)"
      type: siniflandir
      options: [sessiz, onay_gerekli, onay_makul_olmayan_sekilde_esirgenemez, otomatik_fesih, sadece_bildirim]
      prompt: "Sözleşme hedef şirketin kontrol değişikliğini düzenliyor mu? Ne gerektiriyor?"
```

### Adım 2: Örnek çalıştırma

200 belgeye denenmemiş şemayla dalma. Önce 3-5 belge çalıştır. Şemayı ayarla (örn. çoğu `belirsiz` dönen sütunlarda prompt'u yeniden yaz). Onayla.

### Adım 3: Dağıl (Fan out)

Her belge için paralel bir alt-ajan (sub-agent):
1. Tüm belgeyi okur.
2. Her sütun için `değer`, `durum`, `alinti`, `konum` içeren yapılandırılmış bir satır döndürür.
3. Alıntı `birebir` (harfi harfine) olmak **ZORUNDADIR**. Paraphrase kabul edilemez.

### Adım 4: Normalize et

Sütun bazında tüm tabloyu oku.
- Tutarsızlıkları bul (örn. 195 belge "onay gerekli", 5 belge "serbestçe devredilebilir" diyorsa 5'i incele).
- Mantıksız değerleri (99 yıllık süre, 1₺ üst sınır) `inceleme_gerekli` olarak işaretle.
- Alıntıları nokta atışı kontrol et (spot-check). Herhangi bir uydurma (hallucination) veya paraphrase varsa hücreyi düşür ve tüm sütunu şüpheli işaretle.

### Adım 5: Çıktı

- **Markdown** (oturum içi inceleme için)
- **CSV** (ana tablo `.csv` ve destekleyici alıntılar `_kaynaklar.csv`)
- **Excel/Sheets**: İş-ürünü başlığı ekle (Gizlilik ve Meslek Sırrı uyarısı ile). Renk kodlaması kullan. Her veri sütunu yanına bir "Doğrulandı" (Verified) sütunu koy.

### Adım 6: Özet

Sonuçları özetle (veri noktası sayısı, iş yükü, dosyaların konumu).

## Kapanış: Sonraki Adımlar Karar Ağacı

CLAUDE.md'deki `## Çıktılar` standartlarına göre bir karar ağacı ile kapat.

## Bu yetenek (skill) ne yapmaz

- Belgeleri okumanın yerini **almaz**. Sadece nereye bakacağınızı söyler.
- Belge atlamaz.
- Alıntıyı özetleyip alıntıymış gibi davranmaz.

## Diğer yeteneklerle ilişkisi

- `due-diligence-sorun-cikartma` sorun bulur; bu veri noktası çıkarır.
- `onemli-sozlesme-takvimi` (disclosure schedule) doğrudan bu çıktıyı tüketip listesini kurabilir.
- `yapay-zeka-arac-devri` — çok büyük hacimlerde Luminance/Kira gibi araçlara iş devri için.
