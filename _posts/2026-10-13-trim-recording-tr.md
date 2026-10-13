---
lang: tr
ref: trim-recording
categories: tr
permalink: /blog/tr/trim-recording/
date: 2026-10-13
eyebrow: Rehber
title: "Android'de bir ses kaydı orijinali kaybetmeden nasıl kırpılır"
description: "Uzun bir kaydı önemli olan iki dakikaya indirmek saniyeler sürer. Tam dosyanın kesimden sağ çıkıp çıkmadığı uygulamaya bağlıdır. Yaygın uygulamalar bunu nasıl yapıyor, ve neden saklanan şey orijinaldir."
image: /assets/img/og/trim-recording-tr.png
image_alt: "Uzun bir kaydın dalga biçiminde iki dakikalık bir bölüm seçilmiş. TalkSafe'te seçilen bölüm yeni bir dosya olarak kaydedilir, tam orijinal olduğu gibi kalır."
app: true
app_description: "Önceden belirlediğiniz bir kelimeyi duyduğunda kayda otomatik olarak başlayan bir Android ses kayıt uygulaması. Kayıt başladığında önceki 30 saniyeyi de saklar."
faq:
  - q: "Android'de bir ses kaydı nasıl kırpılır?"
    a: "Çoğu kayıt uygulamasında kırpma özelliği vardır: iki tutamacı sürükleyerek bölümü seçer ve kaydedersiniz. Pixel telefonlarda Google'ın Kaydedici uygulamasında Kırp ve kaldır (Crop & Remove) bulunur; ses üzerinde ya da metin dökümü üzerinde çalışır ve Kopyayı kaydet ile biter. Samsung'un Ses Kaydedici uygulaması kırpmaya ve kaydederken dosyayı değiştirmek ile yeni dosya oluşturmak arasında seçim yapmaya izin verir. TalkSafe kırpılan bölümü yeni bir dosya olarak kaydeder ve orijinale dokunmaz."
  - q: "Bir kaydı kırpmak orijinali siler mi?"
    a: "Uygulamaya bağlıdır. Google'ın Kaydedici uygulaması düzenlemeyi kopya olarak kaydeder. Samsung'un Ses Kaydedici uygulaması dosyayı değiştirmek mi yoksa yeni dosya oluşturmak mı istediğinizi sorar; değiştir seçilirse orijinalin üzerine yazılır. TalkSafe'te orijinal her zaman korunur ve kırpılan bölüm ayrı bir dosya olur."
  - q: "Kaydı kırpıp orijinali otomatik olarak koruyan bir Android uygulaması var mı?"
    a: "Evet. TalkSafe, kırpma özelliği seçilen bölümü her zaman yeni bir dosya olarak kaydeden bir Android ses kayıt uygulamasıdır; yanlışlıkla seçilebilecek bir üzerine yazma seçeneği yoktur. Kırpılan bölüme TalkSafe'in cihaz üzerinde çalışan yapay zekâ gürültü giderme özelliği uygulanabilir ve Android paylaşım menüsüyle gönderilebilir."
  - q: "Bir kaydı kırpmak, kaydın hukuka uygun olup olmadığını değiştirir mi?"
    a: "Hayır. Türk Ceza Kanunu'nun 133. maddesinin 2. fıkrasına göre katıldığınız aleni olmayan bir söyleşiyi diğer konuşanların rızası olmadan ses alma cihazıyla kaydetmek altı aydan iki yıla kadar hapis veya adli para cezası gerektiren bir suçtur ve 3. fıkra bu verilerin hukuka aykırı olarak ifşasını cezalandırır. Kesmek bunu değiştirmez. Kaydın hukuka uygun olduğu durumlarda ilgili bölümü sunun, tam orijinali saklayın."
  - q: "Gürültüyü yalnızca kırpılan bölümden giderebilir miyim?"
    a: "Evet. TalkSafe'te önce bölümü kırpın, sonra o dosyaya yapay zekâ gürültü gidermeyi uygulayın. Her iki adım da yeni dosya oluşturur; böylece orijinal, kırpılan bölüm ve temizlenmiş bölüm yan yana kalır."
  - q: "Kırpılmış bir kaydı nasıl gönderirim?"
    a: "TalkSafe Android paylaşım menüsünü kullanır; kırpılan bölüm dosya kabul eden her uygulamaya gidebilir — kendi e-postanız, bir bulut, bir mesajlaşma uygulaması ya da bilgisayarınız. Bir dosyayı kendinize göndermek saklamaktır; başkalarına göndermek yaymaktır ve Türkiye'de TCK 133/3 kapsamında ayrı bir sorundur."
---

Kayıt bir saat kırk dakika. Size gereken, ilk saati geçtikten sonra bir yerdeki iki dakika.

Geri kalanını kimse dinlemeyecek. Ne işveren, ne polis, ne hâkim. Dosyanın tamamını verirseniz birinin o iki dakikayı bulması gerekir. Yalnızca iki dakikayı verirseniz biri öncesinde ne söylendiğini soracaktır.

<p class="pull">Kırpmak kolaydır. Önemli olan, kırptıktan sonra tam dosyanın hâlâ yerinde olup olmadığıdır.</p>

## Yaygın uygulamalar bunu nasıl yapıyor

| Uygulama | Nerede | Nasıl kırpılır | Orijinale ne olur |
|---|---|---|---|
| Google Kaydedici | Pixel | Menü → Kırp ve kaldır (Crop & Remove), ses ya da metin dökümü üzerinde | Düzenleme Kopyayı kaydet (Save copy) ile biter |
| Samsung Ses Kaydedici | Galaxy | Kırpma tutamaçlarını sürükleyerek | Siz seçersiniz: dosyayı değiştir ya da yeni dosya oluştur |
| Audacity | Bilgisayar | Seç, sil, dışa aktar | Aynı adla üzerine dışa aktarmadıkça olduğu gibi kalır |
| TalkSafe | Android | Bölümü seçip kırp | Her zaman kalır; bölüm yeni dosya olarak kaydedilir |

Önemli olan fark son sütunda.

## Pixel'de Google Kaydedici

Google'ın Kaydedici uygulaması, kaydın menüsündeki **Kırp ve kaldır (Crop & Remove)** ile kırpar. **Kırp** seçtiğiniz kısmı tutar; **kaldır** seçtiğiniz kısmı çıkarır. Seçimi dalga biçimi üzerinde ya da **metin dökümü** üzerinde yapabilirsiniz; uzun bir dosyada bir cümleyi bulmanın en hızlı yolu budur. Her iki durumda da adım **Kopyayı kaydet (Save copy)** ile biter ve yeni dosyaya ad verirsiniz.

Pixel'iniz varsa iyi bir düzenleyicidir. Diğer telefonlarda yoktur.

## Samsung Ses Kaydedici

Galaxy telefonlarda yüklü gelen Ses Kaydedici (Voice Recorder), kırpma tutamaçlarını istediğiniz uzunluğa sürüklemenize ve kaydetmeden önce bölümü dinlemenize izin verir. Samsung'un kendi kılavuzu sondaki seçimi anlatır: **dosyayı değiştirmek ya da yeni bir ses dosyası oluşturmak.**

Yavaşlamanız gereken tek yer bu sorudur. Değiştir, başladığınız kaydın üzerine yazar. Kaydın ileride önem taşıma ihtimali azıcık bile varsa yeni dosyayı seçin. Menü adları modele ve One UI sürümüne göre biraz farklı olabilir.

## Bilgisayarda Audacity

Audacity ücretsizdir ve milisaniyesine kadar hassastır: bölümü seçer, gereksizi siler, dışa aktarırsınız. Kaynak dosya, aynı adla üzerine dışa aktarmadığınız sürece değişmez; bu yüzden alıntıyı yeni bir adla dışa aktarın.

Bedeli yolculuktur: dosyayı telefondan çıkarmak, düzenlemek, gerekirse geri koymak.

## TalkSafe

[TalkSafe](/talksafe/tr/) telefonda kırpar ve **üzerine yazmayı hiç önermez**. Seçtiğiniz bölüm yeni bir dosya olarak kaydedilir ve orijinal tam olarak bulunduğu yerde kalır. Yanlış cevaplanacak bir soru yoktur.

Buradan üç şey çıkar.

- **Başlangıcı siz seçersiniz.** TalkSafe önceden belirlediğiniz bir kelimeyle kayda başlar ve o kelime duyulmadan **önceki 30 saniyeyi** de saklar; dosya o andan biraz önce başlar. Kırpma ile alıntının nerede başlayacağını tam olarak belirlersiniz, öncesinin tamamı orijinalde kalır.
- **Bölüm tek başına temizlenebilir.** TalkSafe'in **yapay zekâ gürültü giderme** özelliği kırpılmış bir bölümde de çalışır. Önce iki dakikayı kırpın, sonra yalnızca onları temizleyin: işlem cihazda yapılır ve sonuç başka bir yeni dosya olarak kaydedilir.
- **Bölüm her yere gidebilir.** Gönderme **Android paylaşım menüsünü** kullanır; alıntı dosya kabul eden her uygulamaya gider: kendi e-postanız, bir bulut, bilgisayarınız.

## Önce: kaydetmeye hakkınız var mıydı?

Türkiye'de kırpmadan önce başka bir soru gelir ve kırpmak onu değiştirmez.

**Türk Ceza Kanunu'nun 133. maddesinin 2. fıkrasına** göre katıldığınız aleni olmayan bir söyleşiyi diğer konuşanların rızası olmadan ses alma cihazıyla kaydetmek **altı aydan iki yıla kadar hapis veya adli para cezası** gerektirir. **3. fıkra**, bu yollarla elde edilen verileri hukuka aykırı olarak ifşa etmeyi **iki yıldan beş yıla kadar hapis ve dört bin güne kadar adli para cezası** ile cezalandırır. Böyle bir kayıttan alınan bir parça hâlâ o kayıttır.

Yargıtay, kişinin tehdit veya hakarete uğradığı ve bunu başka bir yolla ispat etme imkânının bulunmadığı durumlarda böyle bir kaydı hukuka uygun kabul eden kararlar vermiştir. Herkesin kabul ettiği durumlarda — üzerinde anlaşılmış bir görüşme, bir röportaj, herkesin kaydedilmesine razı olduğu bir toplantı — kırpma tam da doğru araçtır.

## Neden saklanan şey orijinaldir

Bir alıntı bir iddiadır: *söylenen buydu ve çevresindeki önemli hiçbir şey anlamı değiştirmiyor.* Bu iddiayı destekleyen orijinaldir.

Bir kaydın imzası ya da mührü yoktur. Ne söylediği değerlendirilmeden önce, dosyanın iddia edildiği şey olduğu ve konuşmayı eksiksiz yansıttığı ortaya konmalıdır. Elinizde yalnızca alıntı kalmışsa karşılaştırılacak bir şey yoktur; orijinal onu kaydeden telefonda duruyorsa cevap oradadır.

## Kısa bir sıra

1. **Orijinale dokunmayın.** Yeniden adlandırmayın, yeniden kaydetmeyin, dönüştürmeyin.
2. **Önemli bölümü kırpın**, öncesinden ve sonrasından biraz payla.
3. **Gerekirse bölümü temizleyin.** Gürültü giderme orijinale değil, alıntıya.
4. **Bir not yazın.** Tarih, yer, kimlerin bulunduğu ve alıntının orijinalin kaçıncı dakikasında başladığı.
5. **Orijinali telefonun dışında da yedekleyin.** Kendinize gönderin.

Sonra bölümü ve notu sunun, orijinali hazır tutun.

## Göndermek saklamak değildir

Paylaş düğmesi iki farklı iş yapar. Bir dosyayı kendi e-postanıza ya da bulutunuza göndermek saklamaktır. Bir iş arkadaşına, aile grubuna ya da bir foruma göndermek yaymaktır. Ayrıntılar [Bir kayıtla ne yapmalı, ne yapmamalı](/blog/tr/after-recording/) yazısında.

Gürültülü bölümler için [Android'de bir ses kaydındaki arka plan gürültüsü nasıl giderilir](/blog/tr/remove-background-noise/) sokak gürültüsünün üstesinden gelen ve gelemeyen araçları karşılaştırıyor.

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">Diğer uygulamaların özellikleri yazım sırasındaki resmî kılavuzlarına göre anlatılmıştır ve değişebilir. Biz de bir kayıt uygulaması geliştiriyoruz; bunu yukarıda belirttik. Genel bilgidir, hukuki tavsiye değildir.</p>
