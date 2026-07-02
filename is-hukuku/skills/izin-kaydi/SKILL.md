---
name: izin-kaydi
description: >
  İzin kaydına, son tarihleri ilk günden takip etmeye başlamak için gereken
  minimum bilgiyle yeni bir izin ekler. Bir çalışan izne çıktığında ve
  izleyicinin bildirim, rapor ve tükenme saatlerini ilk günden izlemesini
  istediğinde kullan.
argument-hint: "[izni tanımlayın — çalışan/rol, tür, yer, başlangıç tarihi]"
---

# /izin-kaydi

`~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/izin-kaydi.yaml`
dosyasına, son tarihleri takip etmeye başlamak için gereken minimum bilgiyle
yeni bir izin girdisi ekler. Bir çalışan izne çıktığında ve izleyicinin
saatleri ilk günden izlemesini istediğinde kullan.

## Talimatlar

1. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
   dosyasını oku → izin türleri tablosu ve Sistemler bölümü.

2. Aşağıdakilerin hepsini tek bir istemde sor — birer birer damla damla
   sorma:

   > İzin takibini kurmak için birkaç hızlı soru:
   >
   > - Çalışan adı veya rolü (anonimleştirilmiş olması sorun değil)
   > - Nerede çalışıyor? (Türkiye içi mi, yurt dışı şube mi — hangi kuralların
   >   geçerli olduğunu belirler)
   > - İzin türü: yıllık izin / doğum izni / babalık izni / hastalık-rapor /
   >   ücretsiz izin / mazeret izni / diğer (pratik profilindeki izin türleri
   >   tablosuna bakın)
   > - İzin başlangıç tarihi
   > - Bu aralıklı (parça parça) bir izin mi?
   > - Beklenen dönüş tarihi (biliniyorsa — bilinmiyorsa boş bırakın)
   > - İşverene bildirim yapıldı mı? Yapıldıysa ne zaman?
   > - Sağlık raporu istendi mi? İstendiyse ne zaman?

3. `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/CLAUDE.md`
   dosyasındaki izin türleri tablosunu kullanarak, bu izin türü ve yer için
   geçerli izin hakkını (gün/hafta) ara.

4. Verilen bilgiye dayanarak ilk yaklaşan son tarihi hesapla:
   - Bildirim henüz yapılmadı → son tarih araştırılmış kurala göre belirlenir
     (ör. 4857 kapsamında bildirim süreleri) `[doğrulanacak — kesin gün
     sayısı bir Türk iş hukuku uzmanınca teyit edilmeli]`
   - Sağlık raporu istendi ama alınmadı → son tarih ilgili kuruma göre
     belirlenir `[doğrulanacak]`
   - İkisi de tamam → sonraki son tarih hak edişin %75'inde

5. `izin-izleyici` agent'ındaki izin kaydı formatını kullanarak
   `~/.claude/plugins/config/claude-for-legal-turkish/is-hukuku/izin-kaydi.yaml`
   dosyasına yeni bir girdi yaz. Dosya yoksa oluştur.

6. Tek satırla teyit et:
   > "Kaydedildi. [Çalışan/Rol] — [İzin türü] — [Yer] — [tarih] başladı.
   > İlk son tarih: [ne olduğu ve ne zaman]. İzin izleyici otomatik olarak
   > uyaracak."

## Örnekler

```
/is-hukuku:izin-kaydi
```

```
/is-hukuku:izin-kaydi
Ayşe (Kd. Mühendis, İstanbul'da çalışıyor) bugün doğum izni başlattı.
Bildirim henüz yapılmadı.
```
