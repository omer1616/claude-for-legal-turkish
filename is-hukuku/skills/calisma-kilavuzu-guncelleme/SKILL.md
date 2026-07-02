---
name: calisma-kilavuzu-guncelleme
description: >
  Önerilen bir çalışma kılavuzu değişikliğini mevcut sürümle karşılaştırır,
  dalga etkilerini ve bölge/birim eki etkilerini işaretler. Kullanıcı
  "çalışma kılavuzunu güncelle", "bunu kılavuza ekle", "kılavuz değişikliği"
  dediğinde veya eklenmeye hazır bir politikası olduğunda kullan.
---

# Çalışma Kılavuzu Güncellemeleri

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

Çalışma kılavuzu değişikliklerinin dalga etkileri vardır. Yıllık izin
politikasını değiştirirsiniz ve kıdem tazminatı hesabını, izin politikası
çapraz referansını ve üç bölge ekini etkilemiş olursunuz. Bu skill
tutarsızlık haline gelmeden önce dalgaları bulur.

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md` →
çalışma kılavuzu konumu, bölge/birim ekleri listesi, güncelleme sıklığı.

## İş akışı

### Adım 1: Değişikliği al

- Hangi bölüm değişiyor?
- Yeni dil ne?
- Neden? (Yasal gereklilik, politika kararı, temizlik)

### Adım 2: Mevcutla karşılaştır

Mevcut çalışma kılavuzu bölümünü oku. Farkı göster:

```diff
- [eski dil]
+ [yeni dil]
```

### Adım 3: Çapraz referansları bul

Değişen bölüme atıf yapan referanslar için çalışma kılavuzunu ara:

- Buna atıf yapan diğer politikalar ("tahakkuk oranları için yıllık izin
  politikasına bakın")
- Bu bölümün kullandığı veya tanımladığı tanımlı terimler
- Bu bölümü değiştiren bölge/birim ekleri

Her çapraz referans: değişiklikten sonra hâlâ mantıklı mı? Bozulanları
işaretle.

### Adım 4: Bölge/birim eki etkisi

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
dosyasındaki her bölge/birim eki için:

- Bu ek, değişen bölümü değiştiriyor mu?
- Değişiklik eki eskimiş, yanlış veya eksik hale getiriyor mu?
- Değişiklik, daha önce eke ihtiyacı olmayan bir bölgede *yeni* bir eke
  ihtiyaç yaratıyor mu?

### Adım 5: Vaat kontrolü

Değişiklik eski sürümün vaat ettiği bir şeyi mi azaltıyor?

Evetse: bu bir risktir. Bazı yorumlarda çalışma kılavuzu politikaları
sözleşme niteliğinde kabul edilebilir `[doğrulanacak — Türk hukukunda
çalışma kılavuzu hükümlerinin bireysel/toplu iş sözleşmesinin eki
sayılıp sayılmadığı ve kazanılmış hak (4857 ve genel hükümler
çerçevesinde) doğurup doğurmadığı]`. Bir hakkı azaltmak belgeyi
güncellemekten fazlasını gerektirebilir — önceden bildirim, çalışanın
onayı veya bazı durumlarda geriye dönük olarak yapılamayabilir.

Bunu işaretle. Engelleme — ama işaretle.

## Çıktı

```markdown
## Çalışma Kılavuzu Güncellemesi: [Bölüm adı]

### Değişiklik

[fark]

### Çapraz referans etkisi

| Bölüm | Değişen bölüme atıf | Hâlâ doğru mu? | Gereken düzeltme |
|---|---|---|---|
| [ad] | [nasıl] | ✅/⚠️ | [ne] |

### Bölge/birim eki etkisi

| Bölge/birim | Mevcut ek | Değişiklikten sonra | Eylem |
|---|---|---|---|
| [bölge] | [ne diyor] | [hâlâ geçerli / eskimiş / güncelleme gerekiyor] | [yok / güncelle / yeni ek gerekiyor] |

### Vaat kontrolü

[Bir hak azaltılıyorsa: işaret + yargı çevresi risk notu]

### Yayınlanmaya hazır

- [ ] Çapraz referanslar güncellendi
- [ ] Bölge/birim ekleri güncellendi
- [ ] [Hak azaltmaysa: bildirim/onay ele alındı]
- [ ] Sürüm numarası ve tarih güncellendi
- [ ] Onay süreci (gerekiyorsa)
```

## Bu skill'in yapmadıkları

- Çalışma kılavuzu değişikliklerini onaylamak. İK/hukuk liderliği onaylar.
- Değişiklikleri çalışanlara iletmek.
- Onayları takip etmek.
