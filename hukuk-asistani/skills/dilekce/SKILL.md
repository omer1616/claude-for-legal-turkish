---
name: dilekce
description: Türk yargı usulüne uygun dilekçe taslağı hazırlar — dava, cevap, istinaf/temyiz, itiraz dilekçeleri ve ihtarname. Mahkemeye, icra dairesine veya karşı tarafa verilecek bir metin gerektiğinde kullan.
argument-hint: "[tür — ör. 'cevap dilekçesi' | 'ihtarname']"
---

# /dilekce

Amaç: mahkeme formatında, olgusu delile bağlanmış, atıf disiplinli bir dilekçe
taslağı. **Uydurulmuş içtihat bu skill'in tek ölümcül günahıdır** — hiçbir koşulda
Yargıtay/BAM/AYM karar numarası, tarihi veya içeriği uydurulmaz.

## Adımlar

### 1. Türü ve bağlamı belirle

Tür verilmediyse sor: dava dilekçesi · cevap dilekçesi · cevaba cevap / ikinci cevap ·
istinaf başvuru · temyiz · icra takibine itiraz · ihtiyati tedbir/haciz talebi ·
ihtarname · delil/tanık listesi · sulh önerisi · başka bir şey.

Konu kayıtlı bir dosyaya aitse (`dosyalar/` altında eşleşme ara) öner: "Bu
[dosya adı] dosyası için mi? Kayıttaki taraf, mahkeme ve olay bilgilerini kullanayım
mı?" Kullanırsan hangi bilgileri aldığını söyle.

### 2. Malzemeyi topla

Tek mesajda, dosyadan gelmeyenleri sor:

> 1. **Merci** — hangi mahkeme/daire/noterlik? (esas no varsa)
> 2. **Taraflar** — ad/unvan; vekil bilgileri
> 3. **Olaylar** — kronolojik anlat veya belgeyi yapıştır; elindeki dilekçe/karar
>    varsa yolla, olguları oradan çıkarırım
> 4. **Talep** — mahkemeden/muhataptan tam olarak ne istiyoruz?
> 5. **Deliller** — elde ne var? (sözleşme, yazışma, tanık, bilirkişi…)
> 6. **Süre durumu** — tebliğ tarihi ve son gün biliniyorsa yaz (hesap gerekiyorsa
>    yaparım ama `[doğrula — süre hesabı]` etiketiyle)

Cevap/istinaf/temyiz türlerinde, yanıt verilecek dilekçe veya karar metnini iste —
onsuz yazılan cevap dilekçesi zayıf olur; kullanıcı yine de isterse eksikliği
inceleyen notuna yaz.

### 3. İskelet

Mahkeme dilekçesi (türe göre uyarla):

```
                    [ANKARA 5. İŞ MAHKEMESİ]'NE

                                             Esas No: [.........]
DAVACI            : [ad/unvan, TC/vergi no, adres]
VEKİLİ            : [Av. ..., adres]
DAVALI            : [ad/unvan, adres]
KONU              : [tek cümlede talep]
HARCA ESAS DEĞER  : [.........] (gerekiyorsa)

AÇIKLAMALAR

1. [Numaralı, kronolojik, her olgusal iddia delile bağlı]
...

HUKUKİ NEDENLER   : [ilgili kanunlar ve maddeler — etiket kurallarına tabi]
HUKUKİ DELİLLER   : [numaralı delil listesi; karşı delil sunma hakkı saklı kaydı]
SONUÇ VE İSTEM    : [numaralı, açık talepler; yargılama gideri ve vekâlet ücreti]

                                             [tarih]
                                             Davacı Vekili
                                             Av. [.........]
```

İhtarname için noter formatı: İHTAR EDEN / MUHATAP / KONU / AÇIKLAMALAR / SONUÇ VE
İHTAR + "üç nüshadan ibaret işbu ihtarnamenin bir nüshasının muhataba tebliğini…"
kapanışı. Ton dosya bazında sorulur (sert mi, kapı açık mı) — varsayılan: kararlı ama
köprüleri atmayan.

### 4. İçerik disiplini

- **Olgular:** kullanıcının anlattıkları taraf iddiası olarak yazılır; belgeyle
  desteklenmeyen kritik olgu `[DOĞRULA: …]` işareti alır.
- **Hukuki nedenler:** madde atıfları etiket kurallarına tabi (çoğu
  `[model bilgisi — doğrula]`). Emin olmadığın maddeyi yazma; `[ATIF: dayanak madde
  eklenecek]` bırak.
- **İçtihat:** bu oturumda gerçek bir kaynaktan gelmedikçe karar künyesi YAZILMAZ.
  Yerleşik içtihadı anlatmak gerekiyorsa künyesiz yaz: "Yargıtay'ın yerleşik uygulaması
  … yönündedir `[ATIF: emsal karar eklenecek — Lexpera/Kazancı taraması gerekli]`".
- **Alıntılar:** karşı dilekçeden/karardan alıntı ancak metin eldeyse ve kelimesi
  kelimesine ise tırnak içinde yapılır (kanonik alıntı kuralı).
- **Garanti dili yok:** "davayı kesin kazanırız" tarzı ifadeler ne dilekçede ne
  kapanış mesajında yer alır.
- **Süre uyarısı:** süreye tabi dilekçelerde son günü inceleyen notunda tekrar et.

### 5. Teslim

Dilekçe **dışa dönük belgedir**: gövdeye iş-ürünü başlığı koyma; inceleyen notu
taslağın ÜSTÜNDE ayrı blokta (kaynak durumu, `[DOĞRULA]`/`[ATIF]`/`[incele]` sayıları,
süre uyarısı). Rol profilde **hukukçu değil** ise: mahkemeye sunulacak dilekçe hukuki
sonuç doğuran adımdır — bir avukatla incelenip incelenmediğini sor, taslağı "avukatına
götüreceğin çalışma metni" olarak çerçevele.

Kaydet: dosyaya bağlıysa `dosyalar/<slug>/<tur>-v1.md`, değilse `dilekceler/` altına.

Karar ağacıyla kapat — tipik: (1) işaretli boşlukları birlikte kapatalım, (2) karşı
tarafın muhtemel cevabını çıkarayım, (3) delil listesini ayrıntılandırayım.
