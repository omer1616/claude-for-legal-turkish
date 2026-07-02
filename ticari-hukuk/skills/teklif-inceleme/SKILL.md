---
name: teklif-inceleme
description: >
  oyun-kitabi-izleyici agent'ından gelen bekleyen oyun kitabı güncelleme
  tekliflerini gözden geçirin (onaylayın veya reddedin) ve onaylanan değişiklikleri
  pratik profiline uygulayın. oyun-kitabi-izleyici agent'ı teklifler yüzeye
  çıkardığında, kullanıcı "oyun kitabı tekliflerini gözden geçir", "hangi oyun
  kitabı güncellemeleri bekliyor" dediğinde veya sapma-güdümlü oyun kitabı
  değişikliklerini adım adım incelemek istediğinde kullanın.
argument-hint: "[argüman gerekmez — bekleyen teklifler dosyasından çalışır]"
---

# /teklif-inceleme

İzleyici agent'ından gelen bekleyen oyun kitabı güncelleme tekliflerini adım adım
gözden geçirir ve onaylanan değişiklikleri
`~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye uygular.

## Talimatlar

1. **oyun-kitabi-izleyici agent'ını yükle** ve Adım 5'i (gözden geçirme ve onay
   akışı) çalıştır.

2. **Bir teklif dosyası yoksa** veya boşsa: yanıtla *"Bekleyen teklif yok. Oyun
   kitabı güncel."* Daha fazla ilerleme.

3. **Teklifleri tek tek sun.** Her biri için tam teklif bloğunu göster ve dört
   seçenek sun: Kabul et, Reddet, Düzenle, Ertele.

4. **Kabul et veya Düzenle için:** yazmadan önce
   `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'ye
   tam farkı göster. Yalnızca avukat açıkça onayladıktan sonra uygula.

5. **Reddet veya Ertele için:** kararı kaydet.
   `~/.claude/plugins/config/claude-for-legal-turkish/ticari-hukuk/CLAUDE.md`'yi
   değiştirme.

6. **Tüm teklifler çözüldükten sonra:** neyin değiştiğinin bir özetini göster,
   sonra teklifler dosyasını arşivle.

## Örnekler

```
/ticari-hukuk:teklif-inceleme
```

```
/ticari-hukuk:teklif-inceleme
(oyun-kitabi-izleyici sizi bilgilendirdikten sonra otomatik çalışır)
```
