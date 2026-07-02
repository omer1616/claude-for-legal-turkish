---
name: politika-taslagi
description: >
  Ayak izi genelinde hukukun farklılaştığı yerlerde bölge/birim ekleriyle bir
  iş hukuku politikası taslaklar. Kullanıcı "[konu] politikası taslakla",
  "şu konuda bir politikaya ihtiyacımız var", "[konu] politikamızı güncelle"
  dediğinde veya bir politika boşluğu adlandırdığında kullan.
argument-hint: "[politika konusu — ör. 'uzaktan çalışma', 'doğum izni', 'yıllık izin']"
---

# /politika-taslagi

1. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
   dosyasını yükle → yargı çevresi ayak izi, çalışma kılavuzu konumu.
2. Aşağıdaki iş akışını kullan.
3. Temel politikayı taslakla. Ayak izindeki her yargı çevresini gerekli
   varyantlar için kontrol et.
4. Çıktı: temel politika + bölge/birim ekleri. Hukukun şu an değişmekte
   olduğu yerleri işaretle.

---

## Dosya bağlamı

**Dosya bağlamı.** Pratik düzeyi CLAUDE.md'deki `## Dosya çalışma alanları`
bölümünü kontrol et. `Etkin` `✗` ise (şirket içi kullanıcılar için
varsayılan), bu paragrafın geri kalanını atla — skill'ler pratik düzeyi
bağlamı kullanır ve dosya makinesi görünmez. Etkinse ve aktif bir dosya
yoksa sor: "Bu hangi dosya için? `/is-hukuku:dosya-calisma-alani switch
<slug>` çalıştır veya `pratik-duzeyi` de." Aktif dosyanın `matter.md`'sini
dosyaya özgü bağlam ve geçersizleştirmeler için yükle. Çıktıları dosya
klasörüne yaz:
`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/matters/<dosya-slug>/`.
`Çapraz-dosya bağlamı` `on` olmadıkça başka bir dosyanın dosyalarını asla
okuma.

---

## Amaç

İstanbul merkez için doğru olan bir politika, yurt dışı bir şube için yanlış
(veya gereksiz) olabilir. Bu skill temel bir politika taslaklar ve ayak
izinin farklı kurallar gerektirdiği yerlerde bölge/birim ekleri oluşturur.

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` →
yargı çevresi ayak izi, çalışma kılavuzu konumu ve formatı.

## İş akışı

### Adım 1: Politikayı kapsamla

- Politika ne için? (Uzaktan çalışma, doğum izni, sosyal medya vb.)
- Neden şimdi? (Yasal gereklilik, olay, büyüme, fark edilen boşluk)
- Kime uygulanıyor? (Tüm çalışanlar, belirli roller, belirli konumlar)

### Adım 2: Yargı çevresi taraması

Ayak izindeki her ülke/bölge için kontrol edin: bu yargı çevresinin bu
konuda spesifik bir kuralı var mı?

**Yargı çevresi farklılığı olan yaygın konular:**

| Konu | Farklılık |
|---|---|
| Ücretli izin | Farklı tahakkuk oranları, kullanımlar, devir ile TR'de 4857 m.53-60
  ulusal düzeyde, yurt dışı şubelerde yerel asgari `[doğrulanacak]` |
| Doğum/babalık izni | TR'de 4857 m.74/m.56 ulusal düzeyde; yurt dışı şubelerde
  yerel programlar üzerine katmanlanır |
| Ara dinlenme ve gece çalışması | TR'de 4857 m.68-69 ulusal düzeyde tektir;
  yurt dışı şubelerde değişebilir |
| Masraf iadesi | Yargı çevresine göre zorunlu olabilir |
| İlan şeffaflığı | Bazı yargı çevrelerinde ilanlarda ücret aralığı gerektiren
  artan bir liste |
| Rekabet yasağı | Bkz. `ise-alim-inceleme` skill'i — bazı yargı çevrelerinde
  uygulanamaz |
| Son ödeme zamanlaması | Zamanlama geniş ölçüde değişir |

Konunun yargı çevresi farklılığı yoksa (kıyafet kuralı gibi), bu adımı
atlayın.

### Adım 3: Temel politikayı taslakla

Tek politika. Her yerde geçerli. Açık ve okunabilir — çalışanlar bunu bir
avukat olmadan anlayabilmeli.

Yapı:
- Amaç (tek cümle — bu politika neden var)
- Kapsam (kime uygulanıyor)
- Kural (ne gerekli/izin verilen/yasak)
- Süreç (nasıl talep edilir, kim onaylar, ne olur)
- Sorular (kime sorulur)

Kaçının: gereksiz hukuki jargon, iç içe istisnalar. Bu bir çalışma kılavuzu
politikası, bir sözleşme değil.

### Adım 4: Bölge/birim ekleri

Kuralın farklı olduğu her yargı çevresi için bir ek:

```markdown
### [Bölge/Ülke] Eki

[Bölge/Ülke]'de çalışan çalışanlar, temel politikaya ek olarak / onun
yerine aşağıdakilere tabidir:

- [Spesifik fark]
- [Yardımcı olacaksa yerel kanuna atıf yapın]
```

Ekleri sıkı tutun. Yalnızca farklı olanı — temeli tekrarlamayın.

### Adım 5: Çapraz kontrol

- Bu politika çalışma kılavuzunda zaten olan bir şeyle çelişiyor mu?
- Şirketin sağlamayı amaçladığından fazlasını mı vaat ediyor? (Bir politika
  bir vaattir — mahkemeler işverenleri çalışma kılavuzu vaatlerine
  bağlı tutabilir `[doğrulanacak — TR hukukunda kapsamı]`.)
- Yanlışlıkla bir sözleşme mi yaratıyor? (Çalışma kılavuzu bunu henüz
  içermiyorsa, standart "bu bir sözleşme değildir" dilini ekleyin.)

## Çıktı

```markdown
# [Politika Adı]

## Temel Politika

[Tam metin]

## Bölge/Birim Ekleri

### [Bölge/Birim 1]
[Ek]

### [Bölge/Birim 2]
[Ek]

---

## Taslaklama Notları (iç — çalışma kılavuzuna eklemeden önce kaldırın)

- **Yargı çevresi taraması:** [hangi yargı çevreleri kontrol edildi, hangisinde
  farklılık var]
- **Mevcut çalışma kılavuzuyla çelişkiler:** [yok | liste]
- **Hukuk şu an değişmekte:** [dalgalı olan herhangi bir yargı çevresi]
- **Gözden geçirme sıklığı:** [ne zaman yeniden bakılacak — yıllık, veya X
  olduğunda]
```

> **Taslak, yürürlükte bir politika değil.** Bu, avukat incelemesi için bir
> taslaklama yardımıdır, yayınlayabileceğiniz bir politika değil. Bir
> çalışma kılavuzu politikasını yayınlamanın hukuki sonuçları vardır — bazı
> yorumlarda şirketi sözleşme niteliğinde bağlayabilir ve izin/uyarlama
> politikaları rutin olarak işverenin aleyhine yorumlanır. Yargı çevresinde
> lisanslı bir avukat gözden geçirir, gerektiği gibi düzenler ve devreye
> alınmadan önce mesleki sorumluluğu üstlenir. Bu taslağı incelenmeden
> yayınlamayın veya dağıtmayın.

## Devir

`calisma-kilavuzu-guncelleme` skill'ine: bu politika onaylandığında, mevcut
çalışma kılavuzuna karşı fark alır ve nelerin değiştiğini işaretler.

## Bu skill'in yapmadıkları

- Politikayı onaylamak. Taslaklar; bir insan onaylar.
- Politikayı devreye almak. Çalışanlara iletişim bir İK iş akışıdır.
- Yeryüzündeki her yargı çevresini kapsamak — yalnızca ayak izindekiler.
  Ayak izi genişlerse, yeniden çalıştırın.
