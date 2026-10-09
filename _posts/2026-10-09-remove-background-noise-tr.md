---
lang: tr
ref: remove-background-noise
categories: tr
permalink: /blog/tr/remove-background-noise/
date: 2026-10-09
eyebrow: Nasıl yapılır
title: "Android'de bir ses kaydındaki arka plan gürültüsü nasıl giderilir"
description: "Trafik, rüzgâr, arkada bir kafe. Kaydedilmiş bir konuşmayı temizlemenin dört yolu — kayıt sırasında telefonda, sonradan telefonda, bilgisayarda ya da yükleyerek — ve hangilerinin sokak gürültüsüyle başa çıktığı."
app: true
app_description: "Önceden belirlediğiniz bir kelimeyi duyduğunda kayda otomatik olarak başlayan bir Android ses kayıt uygulaması. Kayıt başladığında önceki 30 saniyeyi de saklar."
faq:
  - q: "Android'de bir ses kaydındaki arka plan gürültüsünü nasıl gideririm?"
    a: "Dört yol var: Pixel 9 serisindeki Google Kaydedici uygulamasının Clear voice özelliği gibi kayıt sırasında gürültüyü azaltan bir kayıt uygulaması; TalkSafe'in yapay zekâ ile gürültü giderme özelliği gibi dosyayı sonradan telefonda temizleyen bir uygulama; Audacity'nin Gürültü Azaltma efekti gibi bir bilgisayar programı; ya da Adobe Podcast Enhance Speech gibi dosyayı yüklediğiniz bir web hizmeti."
  - q: "Bir kayıttaki arka plan gürültüsünü doğrudan telefonda gideren bir Android uygulaması var mı?"
    a: "TalkSafe'te yapay zekâ ile gürültü giderme özelliği var. Tamamlanmış bir kayda ya da kırpılmış bir bölüme uygulandığında sokak sesi gibi arka plan gürültülerini temizler ve konuşmayı bırakır. İşlem cihazda yapılır; temizlenmiş sürüm yeni bir dosya olarak kaydedilir, orijinal olduğu gibi kalır."
  - q: "Audacity trafik gürültüsünü giderebilir mi?"
    a: "İyi değil. Audacity'nin kılavuzu Gürültü Azaltma efektini cızırtı ya da uğultu gibi sabit gürültüler için uygun, trafik ya da seyirci gibi düzensiz arka plan gürültüleri için uygun değil olarak tanımlar. Konuşma olmayan bir bölümden alınan gürültü profiliyle çalışır."
  - q: "Gürültüyü gidermek kaydı delil olarak değiştirir mi?"
    a: "Sesin başka bir sürümünü oluşturur; bu yüzden orijinal saklanmalıdır. Daha anlaşılırsa temizlenmiş kopyayı sunun, dokunulmamış orijinali yanında tutun ve kopyanın temizlendiğini belirtin. TalkSafe'in gürültü giderme özelliği yeni bir dosya kaydeder ve orijinali olduğu gibi bırakır."
  - q: "Gürültüyü gidermek için kaydımı yüklemem gerekir mi?"
    a: "Hayır. Adobe Podcast Enhance Speech gibi web hizmetleri dosyayı yükleyerek çalışır; bu, konuşmanın bir kopyasını o hizmete gönderir. TalkSafe'in yapay zekâ ile gürültü giderme özelliği gibi cihazda çalışan araçlar ise dosyayı telefonda işler."
  - q: "Kaydın yalnızca bir kısmını temizleyebilir miyim?"
    a: "Evet. TalkSafe'te önce gereken bölümü kırpabilirsiniz — kırpılan bölüm yeni bir dosya olarak kaydedilir, orijinal kalır — ve sonra o bölüme yapay zekâ ile gürültü giderme uygularsınız."
---

Konuşmayı kaydettiniz. Eve dönerken dinliyorsunuz ve yarısı kalkan bir otobüsün sesi.

Sözler orada. Sadece her şeyin altında kalmışlar.

<p class="pull">Gürültü giderme artık stüdyo işi değil. Hangi düğmeye bastığınızdan çok, işlemin nerede yapıldığı ve orijinale ne olduğu önemli.</p>

## Dört yol yan yana

| Yöntem | Ne zaman | Ses nereye gider | Orijinal | Sokak ya da trafik gürültüsü |
|---|---|---|---|---|
| Kayıt sırasında gürültüyü azaltan uygulama (Pixel Kaydedici Clear voice) | Kayıt sırasında, Pixel 9 serisi | Kaydedici uygulaması | Oynatırken bir anahtarla azaltmasız dinlenebilir | Genel arka plan gürültüsüne yönelik |
| Dosyayı sonradan temizleyen uygulama (TalkSafe yapay zekâ ile gürültü giderme) | Kayıttan sonra, kırpılmış bölümde de | Telefonda işlenir | Kalır; temizlenmiş sürüm yeni dosyadır | Evet, iki kişilik testlerde |
| Bilgisayar programı (Audacity Gürültü Azaltma) | Kayıttan sonra | Bilgisayarınız | Üzerine yazmazsanız dokunulmaz | Kılavuzuna göre uygun değil |
| Web hizmeti (Adobe Podcast Enhance Speech) | Kayıttan sonra | Hizmete yüklenir | Temizlenmiş bir kopya indirirsiniz | Konuşmayı gürültüden ayırmak için yapılmış |

Sayfanın geri kalanı her birinin sizden gerçekte ne istediğine bakıyor.

## Kayıt sırasında: Pixel Kaydedici'nin Clear voice özelliği

Google, Aralık 2024'te Pixel telefonlardaki Kaydedici uygulamasına **Clear voice** ayarını ekledi. Kayıt sırasında arka plan gürültüsünü azaltır; oynatırken bir anahtarla kaydı azaltma olmadan dinleyebilirsiniz.

Sorun koşullarda. O dönemki haberlere göre yalnızca **Pixel 9 serisinin dahili mikrofonuyla**, mono kayıtta çalışıyordu. Sonraki bir güncellemeyle adı **Auto Clear Voice** oldu.

O telefonlardan birine sahipseniz ve gürültülü bir yerde olacağınızı önceden biliyorsanız, buradaki en az zahmetli yol budur. Başka bir telefonda bu bir seçenek değildir.

## Bilgisayarda: Audacity

Audacity ücretsizdir ve **Gürültü Azaltma** efekti bu işin klasik yoludur. Yalnızca gürültünün olduğu birkaç saniyeyi seçer, bir gürültü profili alır, sonra efekti tüm kayda uygularsınız.

Yapıldığı iş için iyidir: cızırtı, uğultu ya da klima gibi sabit sesler. **Audacity'nin kendi kılavuzu, trafik ya da seyirci gibi düzensiz arka plan gürültüleri için uygun olmadığını söyler.** Sokakta yapılan bir kayıt tam da bununla doludur.

Ayrıca bir bilgisayar, dosya aktarımı ve sürgülerle biraz sabır gerekir. Ayarları fazla zorlarsanız kılavuz yapay seslere — kısa, rastgele ton parçalarına — karşı uyarır.

## Yükleyerek: web hizmetleri

**Adobe Podcast Enhance Speech** gibi araçlar dosyanızı yükleyerek çalışır. Hizmet işler, siz de temizlenmiş bir sürüm indirirsiniz. Konuşma için yapılmışlardır ve etkileyici olabilirler.

Gerçek bir konuşma için kullanmadan önce bilinmesi gereken iki şey var. Birincisi, **yüklemek, konuşmanın bir kopyasının o hizmete gitmesi demektir.** Bir podcast için sorun değil. İçinde başka birinin olduğu özel bir konuşma için bu bilerek verilmesi gereken bir karardır. İkincisi, ücretsiz katmanların uzunluk ve günlük kullanım sınırları vardır ve bunlar değişir.

## Telefonda, sonradan: TalkSafe

[TalkSafe](/talksafe/tr/), yapılmış bir kayda uyguladığınız **yapay zekâ ile gürültü giderme** özelliğine sahiptir.

- **Cihazda çalışır.** Dosyayı temizlemek için hiçbir şey yüklenmez.
- **Orijinal kalır.** Temizlenmiş sürüm yanına yeni bir dosya olarak kaydedilir.
- **Kırpılmış bir bölümde de çalışır.** Önce önemli iki dakikayı kırpın, sonra yalnızca onu temizleyin.

Sokakta kaydedilmiş iki kişilik konuşmalarla yapılan testlerde trafik gitti, konuşma kaldı.

**Önceden belirlediğiniz bir kelimeyi** duyduğunda kayda başlayan, ekran kilitliyken çalışan ve başlangıçtan **önceki 30 saniyeyi** de saklayan uygulamanın aynısıdır. Sokakta bu iki özellik kaydın olmasını sağlar; gürültü giderme onu dinlenebilir kılar.

## Orijinali her zaman saklayın

Gürültü giderme sesin başka bir sürümünü üretir. Amacı budur ve orijinalin önemli olmasının nedeni de budur.

Kayıt bir yerde kullanılabilecekse — bir şikâyette, bir uyuşmazlıkta, bir talepte —, **daha anlaşılırsa temizlenmiş kopyayı sunun ve dokunulmamış orijinali yanında saklayın.** Kopyanın temizlendiğini belirtin. Başka hiçbir şeyin değiştirilmediğini gösteren orijinaldir. Dosyalarla sonradan ne yapılacağı [Bir kayıtla ne yapmalı, ne yapmamalı](/blog/tr/after-recording/) yazısında. Kaydın kendisinin serbest olup olmadığı ayrı bir sorudur: Türkiye'de katıldığınız aleni olmayan bir söyleşiyi diğerlerinin rızası olmadan kaydetmek Türk Ceza Kanunu'nun 133. maddesinin 2. fıkrasına göre suçtur.

## İhtiyaç duymadan önce: daha yakından kaydedin

Hiçbir araç mikrofonun hiç yakalamadığını geri getiremez. Birkaç alışkanlık temizliği kolaylaştırır:

- **En önemlisi mesafedir.** İki kişinin arasında masaya konmuş bir telefon, çantadaki bir telefondan iyidir.
- **En zor gürültü rüzgârdır.** Rüzgâra sırtınızı dönmek ya da bir kapı girişine adım atmak herhangi bir ayardan daha çok işe yarar.
- **Hoparlördeki görüşmeler odayı da alır.** Bir görüşmeyi böyle kaydettiyseniz, gürültü giderme sonradan arka plan gürültüsünü çıkarabilir. Android'de hoparlörün neden kalan yol olduğu [Android'de arama kaydı uygulamaları neden artık çalışmıyor, ve hâlâ ne çalışıyor](/blog/tr/call-recording-android/) yazısında.

## Özet

- **Sabit cızırtı ya da uğultu, bilgisayarda:** Audacity.
- **Bir Pixel 9 ve biraz planlama:** Kaydedici'nin Clear voice özelliği, başlamadan açılmış olarak.
- **Stüdyo sonucu ve gizlilik endişesi yok:** yükleyerek bir web hizmeti.
- **Telefonda kalmasını istediğiniz bir sokak konuşması:** TalkSafe'in yapay zekâ ile gürültü giderme özelliği, cihazda, orijinal korunarak.

Ayrı kayıt cihazlarının ses kalitesinde telefonlarla nasıl karşılaştırıldığı [Kayıt cihazlarını birbirinden ayıran, ne zaman başladıklarıdır](/blog/tr/choosing-a-recorder/) yazısında.

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">Üçüncü taraf araçların özellikleri, yazıldığı tarihteki belgelerine ve haberlere dayanır ve değişebilir. Yukarıda belirtildiği gibi biz de bir kayıt uygulaması geliştiriyoruz.</p>
