---
name: acik-kaynak-inceleme
description: >
  Bir bağımlılık (dependency) listesi, tek bir kütüphane veya dışa açılacak kod 
  için açık kaynak lisans uyumluluk kontrolü yapar. Bir manifest dosyasını (package.json, vb.), 
  SBOM'u veya repoyu lisans yükümlülükleri ve uyumluluk açısından incelerken kullanın.
argument-hint: "[manifest / SBOM dosya yolu | paket adı | repo yolu | yapıştırılan metin]"
---

# /acik-kaynak-inceleme

Bağımlılıkları `~/.claude/plugins/config/claude-for-legal-turkish/fikri-mulkiyet/CLAUDE.md` içindeki pratik profiline göre açık kaynak lisans uyumluluğu açısından inceler. Bağımlılıkları lisans ailelerine göre sınıflandırır, yükümlülükleri dağıtım modeliyle (deployment model) eşleştirir, lisansı belirsiz veya açık kaynak gibi davranan (non-OSI) paketleri işaretler ve eylem önerisinde bulunur (uyum sağla, değiştir, kaldır, hukuki inceleme iste vb.).

## Talimatlar

1. **`CLAUDE.md` dosyasını yükleyin.** Eğer yer tutucular varsa, durun ve önce `/fikri-mulkiyet:ilk-kurulum` çalıştırılmasını isteyin. Açık kaynak (OSS) politikası eklenmişse onu da referans alın.
2. **Kapsamı belirleyin:** Bağımlılık listesi (package.json, requirements.txt, vb.), tek bir kütüphane veya açık kaynak yapılacak kurum içi kod.
3. **Dağıtım (Deployment) modelini sorun:** Yükümlülükleri belirlemeden önce kodun nasıl kullanılacağını (SaaS, Dağıtılan Binary, Sadece İç Kullanım, Gömülü/Firmware) öğrenin.
4. **İş akışını izleyin:**
   - Metadata yerine gerçek lisans metnini (LICENSE) okuyun.
   - Sınıflandırın: İzin verici (Permissive) / Zayıf copyleft / Güçlü copyleft / Kamu malı (Public domain) / OSI-dışı / Bilinmeyen.
   - SSPL, BUSL, Commons Clause gibi açık kaynak OLMAYAN (source-available) lisansları işaretleyin.
5. **Çıktı üretin:** Şablona göre; rol bazlı başlık, özet, paket bazlı analiz, varsa dışa açım (outbound) kontrolü ve onay rotası.
6. **Karar Duruşunu Koruyun:** AGPL'in "ağ üzerinden etkileşim" veya LGPL'in statik/dinamik linkleme sınırları gibi tartışmalı durumlarında her zaman avukat incelemesine yönlendirin.

## Örnekler

```
/fikri-mulkiyet:acik-kaynak-inceleme ~/code/my-project/package.json
/fikri-mulkiyet:acik-kaynak-inceleme redis
/fikri-mulkiyet:acik-kaynak-inceleme ~/code/my-project  # repo kökü
```

---

## İş Akışı

### Adım 1: Kapsam Nedir?
- Bağımlılık listesi (manifest/SBOM)
- Tek paket
- Dışa açılacak kendi kodumuz (embedded lisans uyumluluğunu kontrol eder)

### Adım 2: Dağıtım Modeli Nedir?
- **SaaS (Bulut Hizmeti):** Genellikle sadece AGPL tetiklenir (veya SSPL gibi kısıtlayıcılar). GPL tetiklenmez.
- **Dağıtılan Binary / İstemci Uygulaması:** GPL, LGPL, MPL, EPL tetiklenir (Dağıtım şartı).
- **Sadece İç Kullanım:** Copyleft genelde tetiklenmez.
- **Gömülü (Embedded) / Firmware:** GPL kaynak kodu açmayı ve kurulum bilgisini (tivoization) gerektirebilir.

### Adım 3: Sınıflandırma
- **İzin Verici (Permissive):** MIT, BSD, Apache-2.0, ISC (Atıf zorunluluğu).
- **Zayıf Copyleft:** LGPL, MPL, CDDL (Kütüphane seviyesinde kaynak açma, linkleme kurallarına bağlı).
- **Güçlü Copyleft:** GPL, AGPL, EUPL (Tüm projenin kaynak kodunu açma zorunluluğu bulaşır).
- **OSI-dışı (Source-available):** SSPL, BUSL vb. (Rakip hizmet sunmayı yasaklar).

### Adım 4: Yükümlülükleri Eşleştirme
Her paket için dağıtım modeline göre ne yapılması gerektiğini listeleyin:
- 🔴 Kritik: Yanlış dağıtımda Güçlü Copyleft (örn. Binary içinde GPL). Ticari modele uymayan SSPL.
- 🟠 Yüksek: Bildirim (NOTICE) veya dosya seviyesinde kaynak açma isteyen Zayıf Copyleft. Lisans metinleri çelişenler.
- 🟡 Orta: Sadece atıf (attribution) isteyen ama build sürecine eklenmemiş Permissive lisanslar.
- 🟢 Düşük: Dağıtım olmadığı için tetiklenmeyen copyleft'ler.

### Adım 5: Uyarıları Öne Çıkar
- Lisansı belirsiz olanlar.
- Lisans değiştirenler (örn. Redis, Elastic).
- Uyumsuz kombinasyonlar (GPL-2.0 only ile Apache-2.0 vb.).

## Çıktı Formatı

Bkz. orijinal `oss-review/SKILL.md`. Aynı başlık yapısını kullanarak:
- Bottom line (Özet)
- Top-of-memo flags (Kritik uyarılar listesi)
- By package (Risk durumuna göre paket paket liste)
- Jurisdiction note (Yargı yetkisi notu - AGPL'nin mahkeme testleri, Kamu malı kavramının bazı ülkelerde (Türk Hukukunda FSEK kapsamında eserden feragat mümkün olsa da usulü farklıdır) tam karşılığı olmaması vb.)
- Outbound check (Varsa dışa açım kontrolü)
- Approval routing (Onay rotası)
