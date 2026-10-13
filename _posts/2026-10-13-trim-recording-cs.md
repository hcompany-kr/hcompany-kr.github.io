---
lang: cs
ref: trim-recording
categories: cs
permalink: /blog/cs/trim-recording/
date: 2026-10-13
eyebrow: Návod
title: "Jak na Androidu zkrátit hlasovou nahrávku a nepřijít o originál"
description: "Zkrátit dlouhou nahrávku na dvě minuty, na kterých záleží, trvá pár sekund. Jestli celý soubor střih přežije, záleží na aplikaci. Jak to řeší běžné aplikace a proč se uchovává originál."
image: /assets/img/og/trim-recording-cs.png
image_alt: "Průběh dlouhé nahrávky s vybraným dvouminutovým úsekem. V TalkSafe se úsek uloží jako nový soubor a celý originál zůstane beze změny."
app: true
app_description: "Aplikace pro nahrávání zvuku na Android, která sama začne nahrávat, když uslyší předem zvolené slovo. Při spuštění uloží i 30 sekund před začátkem."
faq:
  - q: "Jak na Androidu zkrátit hlasovou nahrávku?"
    a: "Většina aplikací pro nahrávání má funkci střihu: přetáhnete dvě úchytky, vyberete úsek a uložíte. Na telefonech Pixel má Záznamník Google funkci Oříznout a odstranit (Crop & Remove), která funguje na zvuku i na přepisu a končí uložením kopie. Hlasový záznamník Samsung umožňuje stříhat a při ukládání vybrat, zda soubor nahradit, nebo vytvořit nový. TalkSafe uloží vystřižený úsek jako nový soubor a originálu se nedotkne."
  - q: "Smaže zkrácení nahrávky originál?"
    a: "Záleží na aplikaci. Záznamník Google ukládá úpravu jako kopii. Hlasový záznamník Samsung se ptá, zda soubor nahradit, nebo vytvořit nový; volba nahradit originál přepíše. V TalkSafe originál vždy zůstane a vystřižený úsek se stane samostatným souborem."
  - q: "Existuje aplikace pro Android, která nahrávku zkrátí a originál zachová automaticky?"
    a: "Ano. TalkSafe je aplikace pro nahrávání na Android, jejíž funkce střihu vždy uloží vybraný úsek jako nový soubor, takže neexistuje možnost přepsání, kterou by šlo omylem zvolit. Na vystřižený úsek lze použít odstranění šumu pomocí AI v TalkSafe, které probíhá v zařízení, a poslat ho přes nabídku sdílení Androidu."
  - q: "Mohu jako důkaz předložit jen část nahrávky?"
    a: "Můžete předložit úsek, ale uchovejte celý originál. Ústavní soud v nálezu II. ÚS 1774/14 rozhodl, že tajně pořízený záznam nelze jako důkaz odmítnout jen proto, že obsahuje projevy osobní povahy. Pokud ale druhá strana zpochybní pravost, je to právě nedotčený originál, co ukáže, že úsek je jen výřez."
  - q: "Mohu odstranit hluk v pozadí jen z vystřiženého úseku?"
    a: "Ano. V TalkSafe nejdřív vystřihněte úsek a pak na tento soubor použijte odstranění šumu pomocí AI. Oba kroky ukládají nové soubory, takže vedle sebe máte originál, vystřižený úsek i vyčištěný úsek."
  - q: "Jak poslat zkrácenou nahrávku?"
    a: "TalkSafe používá nabídku sdílení Androidu, takže vystřižený úsek může jít do jakékoli aplikace, která přijímá soubory — na váš e-mail, do cloudu, do chatovací aplikace nebo do počítače. Poslat soubor sobě znamená uschovat ho; poslat ho jiným znamená šířit ho, a pro to platí v Česku § 86 až 90 občanského zákoníku."
---

Nahrávka trvá hodinu a čtyřicet minut. Potřebujete dvě minuty někde po první hodině.

Zbytek nikdo poslouchat nebude. Ani zaměstnavatel, ani policie, ani soud. Když odevzdáte celý soubor, někdo musí ty dvě minuty najít. Když odevzdáte jen dvě minuty, někdo se zeptá, co zaznělo předtím.

<p class="pull">Stříhat je snadné. Záleží na tom, jestli celý soubor potom ještě existuje.</p>

## Jak to řeší běžné aplikace

| Aplikace | Kde | Jak se stříhá | Co se stane s originálem |
|---|---|---|---|
| Záznamník Google | Pixel | Nabídka → Oříznout a odstranit (Crop & Remove), na zvuku nebo přepisu | Úprava končí uložením kopie (Save copy) |
| Hlasový záznamník Samsung | Galaxy | Přetažením úchytek střihu | Vyberete: nahradit soubor, nebo vytvořit nový |
| Audacity | Počítač | Vybrat, smazat, exportovat | Beze změny, pokud přes něj neexportujete pod stejným názvem |
| TalkSafe | Android | Vybrat úsek a vystřihnout | Zůstane vždy; úsek se uloží jako nový soubor |

Rozdíl, na kterém záleží, je v posledním sloupci.

## Záznamník Google na Pixelu

Záznamník Google stříhá přes **Oříznout a odstranit (Crop & Remove)** v nabídce nahrávky. **Oříznout** ponechá vybranou část, **odstranit** vybranou část vyjme. Vybírat lze na průběhu zvuku nebo na **přepisu**, což je nejrychlejší způsob, jak v dlouhém souboru najít větu. V obou případech krok končí **uložením kopie (Save copy)** a novému souboru dáte jméno.

Pokud máte Pixel, je to dobrý editor. Na jiných telefonech není.

## Hlasový záznamník Samsung

Na Galaxy umožňuje předinstalovaný hlasový záznamník (Voice Recorder) přetáhnout úchytky na požadovanou délku a úsek si před uložením poslechnout. Návod Samsungu popisuje volbu na konci: **nahradit soubor, nebo vytvořit nový zvukový soubor.**

Jen u této otázky se vyplatí zpomalit. Nahradit přepíše nahrávku, se kterou jste začali. Pokud je jen malá šance, že nahrávka bude později důležitá, zvolte nový soubor. Názvy v nabídce se mohou podle modelu a verze One UI trochu lišit.

## Audacity v počítači

Audacity je zdarma a přesné na milisekundu: vyberete úsek, smažete nepotřebné a exportujete. Zdrojový soubor se nezmění, pokud přes něj neexportujete pod stejným názvem, takže výřez exportujte pod novým názvem.

Cenou je cesta: dostat soubor z telefonu, upravit ho a případně vrátit zpět.

## TalkSafe

[TalkSafe](/talksafe/cs/) stříhá v telefonu a **nikdy nenabízí přepsání**. Vybraný úsek se uloží jako nový soubor a originál zůstane přesně tam, kde byl. Není tu žádná otázka, na kterou by šlo odpovědět špatně.

Z toho plynou tři věci.

- **Začátek si určíte sami.** TalkSafe začne nahrávat na předem zvolené slovo a uloží i **30 sekund předtím**, než zaznělo, takže soubor začíná o kousek dřív než daný okamžik. Střihem přesně určíte, kde výřez začíná, a celý úvod zůstane v originálu.
- **Úsek lze vyčistit samostatně.** **Odstranění šumu pomocí AI** v TalkSafe funguje i na vystřiženém úseku. Nejdřív vystřihněte dvě minuty a vyčistěte jen ty: zpracování probíhá v zařízení a výsledek se uloží jako další nový soubor.
- **Úsek může jít kamkoli.** Odesílání využívá **nabídku sdílení Androidu**, takže výřez jde do každé aplikace, která přijímá soubory: na váš e-mail, do cloudu, do počítače.

## Proč se uchovává originál

Výřez je tvrzení: *tohle zaznělo a nic důležitého kolem nemění smysl.* Originál je to, co toto tvrzení podpírá.

Nahrávka nemá podpis ani razítko. Než někdo posoudí, co obsahuje, musí být jasné, že soubor je tím, za co se vydává, a že zachycuje rozhovor celý.

V **Česku** upravuje nahrávání hlavně občanský zákoník. Podle § 86 nelze bez svolení člověka pořizovat zvukový záznam jeho soukromého života, podle § 88 odst. 1 ale svolení není třeba, pokud se záznam **pořídí nebo použije k výkonu nebo ochraně jiných práv nebo právem chráněných zájmů**. Ústavní soud v nálezu **II. ÚS 1774/14** rozhodl, že tajně pořízený záznam nelze jako důkaz odmítnout jen proto, že obsahuje projevy osobní povahy.

Na **Slovensku** lze podle § 12 občanského zákoníku zvukový záznam pořídit nebo použít jen se svolením, s výjimkami.

Pokud druhá strana pravost zpochybní a zbyl jen výřez, není s čím ho porovnat; pokud je originál stále v telefonu, který ho nahrál, odpověď existuje.

## Krátký postup

1. **Na originál nesahejte.** Nepřejmenovávat, znovu neukládat, nepřevádět.
2. **Vystřihněte úsek, na kterém záleží**, s trochou toho, co je před ním a po něm.
3. **Úsek případně vyčistěte.** Odstranění šumu na výřezu, ne na originálu.
4. **Napište poznámku.** Datum, místo, kdo byl přítomen a v které minutě originálu výřez začíná.
5. **Zálohujte originál mimo telefon.** Pošlete si ho.

Pak předložte úsek s poznámkou a originál mějte připravený.

## Poslat není uschovat

Tlačítko sdílení dělá dvě různé věci. Poslat soubor na vlastní e-mail nebo do vlastního cloudu znamená uschovat ho. Poslat ho kolegovi, do rodinné skupiny nebo na fórum znamená šířit ho, a to je jiná právní otázka než samotné nahrávání. Vysvětluje to [Co s nahrávkou dělat, a co s ní nedělat](/blog/cs/after-recording/).

U hlučných úseků porovnává [Jak odstranit hluk v pozadí z hlasové nahrávky na Androidu](/blog/cs/remove-background-noise/) nástroje, které si s hlukem ulice poradí, a ty, které ne.

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">Funkce jiných aplikací jsou popsány podle jejich oficiálních návodů v době psaní a mohou se změnit. Sami vyvíjíme aplikaci pro nahrávání, jak je uvedeno výše. Obecné informace, nikoli právní rada.</p>
