---
name: serbest-kullanim-triaji
description: >
  Serbest kullanım (Freedom-to-operate / FTO) triyajı — olası engelleyici patentlere 
  yönelik yapılandırılmış bir ilk bakıştır, kesin bir FTO görüşü DEĞİLDİR. 
  Bir ürün, süreç veya özellik engelleyici patentler açısından değerlendirilirken, 
  "Bizi durduracak bir patent var mı?" diye sorulduğunda veya vekil incelemesinden 
  önce istem (claim) haritası oluşturmak için kullanın.
argument-hint: "[ürünü / süreci / özelliği ve pazarları açıklayın — veya sadece konuyu verin, ben sorarım]"
---

# /serbest-kullanim-triaji

**Bu bir serbest kullanım (FTO) görüşü değildir.** Resmi bir FTO görüşü; kapsamlı bir araştırma, istemlerin (claim) tam yorumlanması ve tescilli patent vekili/uzman avukat tarafından her bir istemin unsur unsur (element-by-element) tecavüz analizini gerektirir. Patent tecavüzü (SMK m. 141) kusursuz sorumluluk doğurabilir. "Açık bir engelleyici patent yok" sonucu, bu taramanın bulamadığı anlamına gelir; ürünün serbest olduğu anlamına gelmez.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` dosyasını okuyun. Profil yoksa `/fikri-mulkiyet:ilk-kurulum`'a yönlendirin.
2. Aşağıdaki iş akışını izleyin.
3. Girdi alın (ürün/süreç, teknik detay, pazarlar/yargı çevreleri, bilinen patentler, zamanlama).
4. Bağlı bir araç varsa (Solve Intelligence, Lexpera/Kazancı vb.) patent araştırması yapın. Yoksa bunu açıkça belirtin ve kullanıcının verdiği patentlerle devam edin.
5. En olası 2-5 patent için bağımsız istemleri unsur unsur eşleyerek ilk istem haritasını (claim chart) oluşturun. Önce kelimesi kelimesine (literal) örtüşmeyi, sonra eşdeğer unsurlar doktrinini (SMK m. 89/5 - DOE) işaretleyin.
6. Hükümsüzlük, kullanım zorunluluğu (SMK m. 130), itiraz durumu (SMK m. 99) gibi gerçek bir FTO analizinin çözeceği açık soruları listeleyin.
7. İnceleme notunu (memo) aktif dosyaya yazın ve role uygun başlık atın.
8. Sonraki adımlarla bitirin.

## Örnekler

```
/fikri-mulkiyet:serbest-kullanim-triaji "tüketici giyilebilir cihazları için cihaz-içi konuşma tanıma modeli, önce Türkiye pazarı"
```

---

## BU BİR SERBEST KULLANIM (FTO) GÖRÜŞÜ DEĞİLDİR

**En güçlü uyarı. Bunu her çıktının başına koyun.**

> **Bu bir serbest kullanım (freedom-to-operate) hukuki görüşü değildir.** FTO görüşü, tescilli patent vekilleri veya uzman avukatlar tarafından yapılan kapsamlı bir araştırma ve SMK m. 89 kapsamında istemlerin unsur unsur ihlal analizine dayanan profesyonel bir hukuki karardır. "Açık bir engelleyici patent bulunamadı" demek, sadece bu sınırlı taramanın bulamadığı anlamına gelir. Üretim, kullanım, satış veya ithalat (SMK m. 85) kararı, bu taramaya göre değil, resmi bir FTO çalışmasına ve vekil/avukat görüşüne dayanılarak alınan ticari bir karardır.

---

## Bağlam ve Kapsam

- İstem Haritası (Claim Chart) Çıkarırken, faydalı modeller ve patentler analiz edilir.
- Tasarım Tescilleri (SMK m. 55 vd.) farklıdır, bu analizde değerlendirilmez, sadece genel görünüm itirazı varsa tasarım incelemesine havale edilir.

## Girdi Alma (Intake)

> 1. **Ürün, süreç veya özellik:** Tam olarak ne üretiliyor, kullanılıyor veya satılıyor? Pazarlama metni değil, teknik özünü anlatın.
> 2. **Teknik detay:** Mimari şemalar, kodlar, veya özellik dökümanları var mı?
> 3. **Yargı Çevreleri:** Nerede üretilip satılacak? (Türkiye, EP/Avrupa, vd. - Her biri bağımsız ihlal eylemidir).
> 4. **Bilinen patentler:** Radarda olan, rakibin patenti veya daha önce uyarı alınan patent var mı?
> 5. **Zamanlama:** Piyasaya sürülmesine ne kadar var? Erken aşamadaysa tasarım değişikliği (design-around) mümkündür.

## İstem Haritası (Claim Chart) - İlk Bakış

Seçilen en kritik patentlerin bağımsız istemlerini unsur unsur (element-by-element) ayırın:

| İstem Unsuru | Ürün bunu uyguluyor mu? | Gerekçe / Dayanak |
|---|---|---|
| "[Giriş cümlesi]" | [evet / hayır / muhtemelen] | [Üründeki karşılığı veya eksikliği] |
| "içeren [1. unsur]" | [evet / hayır] | [Açıklama] |
| "şurada [2. unsur]" | [evet / hayır] | [Açıklama] |

**Kural:** Bütün unsurlar kuralı (All-elements rule). İhlalden söz edebilmek için bağımsız istemin TÜR unsurlarının üründe bulunması (aynen veya eşdeğer) gerekir. Bir unsur yoksa literal ihlal yoktur.

**Eşdeğerlik Doktrini (SMK m. 89/5):** Unsurlar aynen yoksa bile, "aynı işlevi, aynı yolla gerçekleştirip aynı sonucu elde ediyorsa" eşdeğer (DOE) sayılır. Bunu işaretleyin ama kesin karar vermeyin.

## Açık Sorular ve Sonraki Adımlar

- Patent hala geçerli mi? (Yıllık sicil ücretleri ödenmiş mi?)
- Hükümsüzlük veya itiraz davası var mı?
- Gerçek bir FTO analizi yapılması tavsiyesi.

Çıktıyı orjinal `fto-triage/SKILL.md` formatında oluşturun (Subject, Search scope, Patents identified, Claim charts, Open questions, Next steps). Avukat olmayan kullanıcı için uyarıyı (Non-lawyer gate) ekleyin.
