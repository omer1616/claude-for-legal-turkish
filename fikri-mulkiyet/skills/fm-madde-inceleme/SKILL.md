---
name: fm-madde-inceleme
description: >
  Bir sözleşmedeki (iş, danışmanlık, hizmet alımı, lisans) Fikri Mülkiyet (FM) maddelerini — 
  devir, mülkiyet, lisans verilmesi, garantiler, tazminatlar — inceleyin. Fikri mülkiyetin 
  devri (assignment) veya lisans kapsamı kontrol edildiğinde, veya içinde FM hükümleri olan 
  bir sözleşme metni paylaşıldığında kullanın.
argument-hint: "[dosya yolu | bulut linki | yapıştırılan metin]"
---

# /fm-madde-inceleme

Bir sözleşmedeki FM maddelerini `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` içindeki pratik profiline göre inceler. Devir/temlik boşluklarını, mülkiyet belirsizliklerini, lisans kapsamı sorunlarını ve garanti/tazminat (indemnity) risklerini işaretler. Risk düzeyine göre önceliklendirilmiş ve gerektiğinde değişiklik önerilerini (redline) içeren bir inceleme notu üretir.

## Talimatlar

1. **Profili yükle:** `CLAUDE.md`. Yoksa `/fikri-mulkiyet:ilk-kurulum`'a yönlendir.
2. **Sözleşmeyi al:** Dosya, link veya metin.
3. **İş Akışını İzle:**
   - Sözleşme türü nedir ve FM açısından hangi taraftayız (Devreden/Lisans Veren mi, Devralan/Lisans Alan mı)?
   - İş, danışmanlık veya eser sözleşmesi ise **ilk olarak devir boşluğu (assignment gap) kontrolü** yapın.
   - Her madde için risk bazlı bulgular üretin (FSEK ve SMK'ya uygunluk).
   - Çapraz madde tutarlılığını kontrol edin.
   - Yargı çevresi/Türk Hukuku (FSEK ve SMK) uyarılarını ekleyin.
4. **Çıktı üret:** Başlık, sonuç, devir kontrolü, risklere göre maddeler, tutarlılık, onay rotası.

## Örnekler

```
/fikri-mulkiyet:fm-madde-inceleme ~/Documents/yazilim-gelistirme-sozlesmesi.pdf
/fikri-mulkiyet:fm-madde-inceleme
```

---

## Türk Hukuku Adaptasyonları (ÇOK ÖNEMLİ)

Amerika/İngiliz pratiğinden (Work-for-hire, assignment) farklı olarak Türk Hukukunda şu noktalara **KESİNLİKLE DİKKAT EDİN**:

1. **Manevi Haklar (FSEK m. 14-17):** Türk Hukukunda manevi haklar (Umuma arz, adın belirtilmesi, eserde değişiklik yapılmasını men etme) **DEVREDİLEMEZ**, feragat edilemez. Sözleşmede "Manevi haklarını devreder" yazıyorsa bu geçersizdir. Doğrusu: **"Manevi hakları kullanma yetkisinin devri"** (FSEK m. 18) olmalıdır. Bunu `🟠 Yüksek` risk olarak işaretleyin ve düzeltin.
2. **Mali Hakların Devri Şekil Şartı (FSEK m. 52):** FSEK'e göre mali hakların devri **YAZILI** olmalı ve hangi hakların (çoğaltma, yayma, temsil, işaret/ses/görüntü nakli, işleme) devredildiği **AYRI AYRI AÇIKÇA SAYILMALIDIR**. "Tüm Fikri Mülkiyet haklarını devreder" gibi genel ve yuvarlak ifadeler geçersiz/hükümsüz sayılabilir. Bu, bir sözleşmedeki en büyük `🔴 Kritik` risktir. 
3. **Çalışanların Eserleri (FSEK m. 18):** İşçilerin işlerini görürken yarattıkları eserlerin mali haklarını kullanma yetkisi aksi kararlaştırılmadıkça işverene aittir. Ancak yine de açıkça belirtilmesi sözleşmesel güvence sağlar.
4. **Çalışanların Buluşları (SMK m. 113):** Çalışanın işi gereği yaptığı "hizmet buluşları"nda işverenin hak talep etme prosedürü (bildirim süreleri vb.) kanunla sabittir. Sözleşme buna aykırı olmamalıdır.
5. **Gelecekteki Eserler (FSEK m. 48):** İleride yaratılacak eserler için yapılan devir taahhütleri geçerlidir ancak taraflardan biri sözleşmeyi sonradan feshedebilir (FSEK m. 50). "Hereby assigns" (peşinen şimdiden devreder) ifadesi Türk hukukunda tartışmalı olsa da, "devir ve temlik etmeyi taahhüt eder ve eser/buluş ortaya çıkar çıkmaz ayrıca bir işleme gerek kalmaksızın tüm hakların devredilmiş sayılacağını kabul eder" gibi sağlamlaştırıcı bir `Redline` önerin.

## İş Akışı

### Adım 1: Yönelim (Orient)
Sözleşme türü, hangi taraftayız (hak alan mı veren mi), sözleşme bedeli ne, uygulanacak hukuk Türk Hukuku mu? (Bunu sor veya metinden anla).

### Adım 2: Devir Boşluğu Kontrolü (Assignment gap check - En Yüksek Öncelik)
Çalışan, danışman, taşeron yazılım geliştirici ise:
- FSEK m. 52'ye göre haklar açıkça sayılmış mı? (İşleme, çoğaltma, yayma, temsil, umuma iletim). 
- FSEK m. 18 manevi hakları kullanma yetkisi düzgün formüle edilmiş mi?
- Eksikse, `🔴 Kritik` veya `🟠 Yüksek` risk olarak en başa yazın ve Türk Hukukuna uygun Redline önerin.

### Adım 3: Madde Madde İnceleme
Her bir FM (IP) maddesi için:
- **Ne diyor:** Kısa özet.
- **Piyasa standardı (Market standard):** Bu tür sözleşmelerde beklenen durum.
- **Risk:** 🔴 Kritik | 🟠 Yüksek | 🟡 Orta | 🟢 Düşük
- **Neden önemli:** Hukuki / Ticari sonuç.
- **Önerilen değişiklik (Redline):** Sadece sorunlu kelime/cümleyi değiştirecek cerrahi müdahale (wholesale rewrite yapmayın).

### Adım 4: Çapraz Madde Tutarlılığı
- Verilen lisansın kapsamı ile garanti edilen konular uyuşuyor mu?
- Fesih halinde lisans/hak durumu net mi?

## Çıktı Formatı

Bkz. orijinal `ip-clause-review/SKILL.md`. Aynı başlık yapısını kullanarak:
- Bottom line (Özet)
- Assignment gap check (Devir boşluğu kontrolü)
- Clauses by severity (Risk düzeyine göre maddeler)
- Cross-clause consistency (Çapraz tutarlılık)
- Jurisdiction note (Türk hukuku FSEK/SMK notu)
- Approval routing (Onay rotası)

*Yapay Zeka (AI) Üretimi Notu:* Buluşlarda veya eserlerde AI araçları kullanılmışsa, Türk hukukunda yapay zekanın eser sahibi (feser sahibi olabilmek için "hususiyet taşıyan bir insan çabası" gerekir) olamaması nedeniyle telif haklarının doğmaması riski vardır. Bunu da sözleşmede açıkça beyan edecek (AI kullanımını ifşa) bir kloz eklenmesini (AI-use disclosure obligation) 🟠 Yüksek risk olarak önerin.
