---
name: otomatik-guncelleyici
description: >
  Kurulu topluluk eklentilerinde (skills) güncellemeleri kontrol eder. Bir diff (fark) gösterir ve uygulamadan önce açık onay gerektirir. Kullanıcı "güncellemeleri kontrol et", "eklentilerimi güncelle", "kurulu eklentilerimde yeni bir şey var mı" dediğinde veya kayit-tarayici ajanı tarafından çağrıldığında kullanın.
argument-hint: "[hepsini güncellemek için --apply, aksi takdirde sadece bildir]"
---

# /otomatik-guncelleyici

1. `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` dosyasını yükleyin → kurulu eklentiler + otomatik-güncelleme tercihleri.
2. Aşağıdaki iş akışını kullanın.
3. Her kurulu eklentinin kaynağında daha yeni bir sürüm olup olmadığını kontrol edin.
4. Tercihe göre: uygula / bildir / diff göster.

---

## Amaç

Topluluk eklentileri zamanla gelişir. Bu skill bunun ne zaman olduğunu fark eder, neyin değiştiğini gösterir ve güncellemeleri SADECE sizin açık onayınızla uygular.

## Güven durumu (Trust posture)

Kurulu eklentiler ayrıcalıklı hukuki ortamınızda çalışan kodlardır. Bir kaynak (upstream) depo ele geçirilebilir, yeni bir sahibe devredilebilir veya sizin istemediğiniz şekillerde davranışı değişebilir. Bu skill, **hiçbir güncellemenin siz diff'i okumadan ve onaylamadan asla uygulanmayacağı** şekilde tasarlanmıştır. Bu bir tercih değildir — tasarımın kendisidir.

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` → kurulu eklentiler (sürüm/commit SHA ile birlikte), güncelleme tercihleri (bildir / manuel).

## İş Akışı

### Adım 1: Her kurulu eklentiyi kontrol edin

Kurulu listesindeki her eklenti (skill) için:
- Kaynak kaydından (registry) mevcut commit SHA'sını getirin (tam commit, etiket veya branch başı değil — etiketler değiştirilebilir; sadece commit SHA'ları değişmezdir)
- Kurulum zamanından sabitlenmiş (pinned) SHA ile karşılaştırın
- Farklıysa: güncelleme mevcuttur

### Adım 2: Diff ve güven incelemesi

Her güncelleme için tam diff'i (farkı) gösterin:

```diff
# [eklenti-adi] — [kurulu SHA] → [en yeni SHA]

## SKILL.md değişiklikleri
[birleştirilmiş diff]

## hooks/hooks.json değişiklikleri
[birleştirilmiş diff — İŞARET: kancalar (hooks) keyfi kod çalıştırabilir]

## .mcp.json değişiklikleri
[birleştirilmiş diff — İŞARET: MCP sunucuları kimlik bilgilerinizle çalışır]

## Diğer dosyalar
[diff'leri ile birlikte eklenen/kaldırılan/değiştirilen dosyaların listesi]
```

Sonra güven kontrolünü (trust check) çalıştırın:
- **`hooks/hooks.json` değişti mi?** Diff'i belirgin şekilde gösterin ve kullanıcıdan yeni kancaların (hooks) ne yaptığını anladığını teyit etmesini isteyin.
- **`.mcp.json` değişti mi?** Aynı muamele.
- **`allowed-tools` veya `tools` izinleri genişledi mi?** Yeni araç erişimi bir yetki yükseltmesidir.
- **Yeni ağ çağrıları, eklenti dizini dışında dosya yazma eylemleri vb.?** İşaretleyin.
- **Eklentinin `description` (açıklaması) veya belirtilen amacı değişti mi?** Amacı değişen bir eklenti kendisini yeniden yapılandırmıştır.

### Adım 2.5: Yeni sürümü yeniden tara (GlassWorm kapısı)

Güncellemeyi uygulamadan önce YENİ sürüme karşı tam `eklenti-kalite-kontrol` (skills-qa) taramasını yeniden çalıştırın. Kurulum zamanındaki güven güncellemeyle doğrudan aktarılamaz. Eğer sorun (REFUSE vb.) varsa, kullanıcı uyarılsın ve güncelleme zorla uygulanmasın.

### Adım 2.6: Tazelik (Freshness) tetiklemeli yeniden doğrulama

Referans materyallerin tazelik süresi (freshness_window) dolmuş mu diye kontrol edin. Dolmuşsa ve güncelleme yoksa kullanıcıyı uyarın. Güncelleme varsa ve `last_verified` tarihi ileri gitmemişse, kullanıcıyı uyarın.

### Adım 3: Tercihe göre yönetin

**Bildir (varsayılan):** Tam diff'i ve güven kontrolünü gösterin. "Güncelleme mevcut. Yukarıdaki diff'i inceleyin. Uygulansın mı? [e/h]"
**Manuel:** Sadece hangi güncellemelerin mevcut olduğunu listeleyin. Kullanıcı hazır olduğunda `--apply [eklenti]` ile uygular.
"Otomatik" mod yoktur. İnsan onaylamalıdır.

### Adım 4: Uygula (açık onaydan sonra)

Kurulu eklenti dosyalarını yeni sürümle değiştirin. CLAUDE.md'yi yeni commit SHA'sı ile güncelleyin. Eski sürümü geri alma (rollback) ihtimaline karşı yedekleyin (`~/.claude/skills/.backups/[eklenti]-[eski-sha]/`).

## Geri Alma (Rollback)

Eğer bir güncelleme bir şeyi bozarsa: `/eklenti-merkezi:otomatik-guncelleyici --rollback [eklenti]` komutu yedekten geri yükler.

## Bu eklentinin yapmadığı şeyler

- Güncellemeleri otomatik olarak (insan onayı olmadan) uygulamak.
- Merkez (hub) üzerinden kurulmayan eklentileri güncellemek.
- Etiketlere veya sürüm numaralarına güvenmek. (Sadece commit SHA'larına güvenir).
