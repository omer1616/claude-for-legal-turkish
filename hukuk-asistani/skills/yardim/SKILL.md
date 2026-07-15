---
name: yardim
description: Hukuk Asistanı'nın komutlarını ve günlük kullanım örneklerini sade bir dille gösterir. Kullanıcı ne yapabileceğini sorduğunda, bir komutu hatırlayamadığında veya eklentiyi yeni kurduğunda kullan.
---

# /yardim

Amaç: teknik bilgisi sınırlı bir avukatın "şimdi ne yazacağım?" sorusunu 30 saniyede
cevaplamak. Kısa tut, jargon kullanma, belgeye değil sohbete yaz.

## Adımlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/hukuk-asistani/CLAUDE.md`
   profilini kontrol et. Yoksa veya boşsa önce şunu söyle: "Henüz kurulum yapılmamış —
   `/hukuk-asistani:ilk-kurulum` ile başla, 3 dakika sürer." Sonra yine de aşağıdaki
   rehberi göster.

2. Şu rehberi göster (kendi sesinle, kullanıcının profiline göre örnekleri uyarla):

> ## Ne yapabilirim?
>
> | Durum | Komut |
> |---|---|
> | Yeni bir dava veya iş geldi | `/hukuk-asistani:yeni-dosya` |
> | Dosyalarım ne durumda, yaklaşan duruşma/süre var mı? | `/hukuk-asistani:dosyalarim` |
> | Dosyada gelişme oldu (duruşma, tebligat, görüşme) | `/hukuk-asistani:dosya-notu` |
> | Bir sözleşmeyi incelememi iste | `/hukuk-asistani:sozlesme-incele` |
> | Sıfırdan sözleşme hazırlat | `/hukuk-asistani:sozlesme-hazirla` |
> | Dilekçe veya ihtarname yazdır | `/hukuk-asistani:dilekce` |
> | Uzun bir kararı/raporu/sözleşmeyi özetlet | `/hukuk-asistani:ozetle` |
> | Hukuki bir soruyu araştırt | `/hukuk-asistani:arastir` |
> | Kurulumu değiştir | `/hukuk-asistani:ilk-kurulum --redo` |
>
> **Komut ezberlemene gerek yok.** Normal cümleyle yaz, ben doğru aracı seçerim:
> - "Yeni bir işçilik davası aldım, müvekkil Ahmet Yılmaz" → dosya açarım
> - "Bugün duruşma vardı, tanıklar dinlendi, yeni duruşma 12 Eylül" → dosyaya not düşerim
> - "Şu kira sözleşmesine bir bak" → incelerim
> - "Kiracı tahliye ihtarnamesi lazım" → taslağını yazarım
> - "Bu Yargıtay kararı ne diyor?" → özetlerim
>
> **Belgelerin nerede?** Her şey [profildeki çalışma klasörü] içinde düz dosya olarak
> durur — istediğin zaman kendi bilgisayarında açıp bakabilirsin, hiçbir şey kilitli
> bir sistemde değil.
>
> **Unutma:** Ürettiğim her belge senin incelemen için bir **taslaktır**. Atıf ve süre
> gibi kritik noktaları `[doğrula]` etiketiyle işaretlerim — imzalamadan, göndermeden,
> sunmadan önce bu işaretli yerleri kontrol et.

3. Kullanıcının profili doluysa sonuna, portföyüne uygun tek bir somut öneri ekle
   (ör. hiç dosya kaydı yoksa: "İlk dosyanı açalım mı?"; dosyaları varsa:
   "`/hukuk-asistani:dosyalarim` ile bu haftanın görünümünü alabilirsin").
