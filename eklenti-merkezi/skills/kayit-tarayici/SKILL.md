---
name: kayit-tarayici
description: >
  Topluluk hukuki eklentileri için izlenen kayıtları (registries) arar, açıklamalarla birlikte eşleşmeleri gösterir ve kurmadan önce tam SKILL.md'yi göstermeyi teklif eder. Kullanıcı "göz at", "eklentilerde ara", "şunun için eklenti bul", "dışarıda ne var" dediğinde veya izleme listesine yeni bir kayıt eklemek istediğinde kullanın.
argument-hint: "[arama sorgusu]"
---

# /kayit-tarayici

1. `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` dosyasını yükleyin → izlenen kayıtlar (watched registries).
2. Aşağıdaki iş akışını kullanın.
3. Her bir kaydı arayın. Açıklamalarla birlikte eşleşmeleri gösterin.
4. Herhangi bir eşleşme için tam SKILL.md dosyasını göstermeyi teklif edin.

---

## Amaç

İzlenen kayıtlar genelinde eklentileri bulmak. Arama, önizleme, karar.

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` → izlenen kayıtlar listesi.

## İş Akışı

### Adım 1: Kayıt dizinlerini getir

İzlenen her kayıt için:

- GitHub repoları: `skills/` dizin listesini ve her `SKILL.md` ön-madde verisini (isim + açıklama) getirin.
- Pazaryeri (Marketplace) tarzı kayıtlar: dizini getirin.

Göz atmanın hızlı olması için dizini yerel olarak önbelleğe alın (`references/registry-cache.json`). Önbellek >7 günlükse veya istek üzerine yenileyin.

### Adım 2: Arama

Sorguyu eklenti adları ve açıklamalarıyla eşleştirin. Basit anahtar kelime eşleşmesi yeterlidir — bunlar bulanık (fuzzy) aramanın gereksiz olacağı kadar küçüktür.

Ayrıca: kayıt, eklentileri kategoriye göre düzenliyorsa kategoriye göre göz atın.

### Adım 3: Eşleşmeleri sunun

```markdown
## Arama: "[sorgu]"

**[M] kayıt içinde [N] eklenti bulundu:**

### [eklenti-adi]
**Kaynak:** [kayıt adı]
**Açıklama:** [ön-madde verisinden (frontmatter)]
[Tam SKILL.md'yi Görüntüle] [Kur]

### [eklenti-adi]
[...]
```

### Adım 4: Önizleme

"Tam SKILL.md'yi Görüntüle" üzerine: tüm dosyayı getirin ve gösterin. Kullanıcı kurmaya karar vermeden önce okur. Sürpriz yok.

### Adım 5: Bir kayıt ekle

Kullanıcıda izleme listesinde olmayan bir kaydın URL'si varsa:

1. Getirin, bunun bir eklenti (skills) reposu olduğunu doğrulayın (`skills/` veya `.claude-plugin/` dizini vardır)
2. İçinde ne olduğunu gösterin
3. Onay üzerine `~/.claude/plugins/config/claude-for-legal-turkish/eklenti-merkezi/CLAUDE.md` → izlenen kayıtlar bölümüne ekleyin.

## Varsayılan kayıtlar

- **lpm-skills** — 14 hukuki proje yönetimi eklentisi. Pratik-bağımsızdır. İyi bir başlangıç noktasıdır.
- Ekosistem büyüdükçe eklenebilecek diğerleri için boşluk.

## Bu eklentinin yapmadığı şeyler

- Herhangi bir şeyi kurmak. Sadece tarar. Kurulumu `eklenti-kurucu` yapar.
- Eklentileri derecelendirmek veya incelemek. Size SKILL.md'yi gösterir; siz yargılarsınız.
- Tüm interneti aramak. Sadece izlenen kayıtlarda arar.
