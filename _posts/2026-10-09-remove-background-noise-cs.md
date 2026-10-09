---
lang: cs
ref: remove-background-noise
categories: cs
permalink: /blog/cs/remove-background-noise/
date: 2026-10-09
eyebrow: Návod
title: "Jak odstranit hluk v pozadí z hlasové nahrávky na Androidu"
description: "Doprava, vítr, kavárna za zády. Čtyři způsoby, jak vyčistit nahraný rozhovor — v telefonu během nahrávání, v telefonu potom, v počítači, nebo nahráním na web — a které z nich si poradí s hlukem ulice."
app: true
app_description: "Aplikace pro nahrávání zvuku na Android, která sama začne nahrávat, když uslyší předem zvolené slovo. Při spuštění uloží i 30 sekund před začátkem."
faq:
  - q: "Jak odstranit hluk v pozadí z hlasové nahrávky na Androidu?"
    a: "Cesty jsou čtyři: aplikace, která hluk snižuje už při nahrávání, jako Clear voice v aplikaci Záznamník od Googlu na řadě Pixel 9; aplikace, která soubor vyčistí potom v telefonu, jako odstranění šumu pomocí AI v TalkSafe; program do počítače, jako efekt Redukce šumu v Audacity; nebo webová služba, na kterou soubor nahrajete, jako Adobe Podcast Enhance Speech."
  - q: "Existuje aplikace pro Android, která odstraní hluk v pozadí z nahrávky přímo v telefonu?"
    a: "TalkSafe má odstranění šumu pomocí AI. Použité na hotovou nahrávku nebo vystřižený úsek odstraní hluk v pozadí, například z ulice, a ponechá rozhovor. Zpracování probíhá v zařízení a vyčištěná verze se uloží jako nový soubor, zatímco originál zůstane beze změny."
  - q: "Umí Audacity odstranit hluk dopravy?"
    a: "Moc ne. Příručka Audacity popisuje efekt Redukce šumu jako vhodný pro stálý šum, jako je syčení nebo bručení, a nevhodný pro nepravidelný hluk v pozadí, jako je doprava nebo publikum. Pracuje s profilem šumu z úseku bez řeči."
  - q: "Mění odstranění šumu nahrávku jako důkaz?"
    a: "Vytváří jinou verzi zvuku, proto je potřeba originál ponechat. Předložte vyčištěnou verzi, pokud je srozumitelnější, ponechte vedle ní nedotčený originál a uveďte, že kopie byla vyčištěna. Odstranění šumu v TalkSafe uloží nový soubor a originál ponechá beze změny."
  - q: "Musím nahrávku nahrát na internet, abych odstranil šum?"
    a: "Ne. Webové služby jako Adobe Podcast Enhance Speech pracují tak, že soubor nahrajete, čímž se kopie rozhovoru dostane k té službě. Nástroje, které pracují v zařízení, jako odstranění šumu pomocí AI v TalkSafe, zpracují soubor v telefonu."
  - q: "Můžu vyčistit jen část nahrávky?"
    a: "Ano. V TalkSafe nejdřív vystřihnete potřebný úsek — uloží se jako nový soubor a originál zůstane — a potom na něj použijete odstranění šumu pomocí AI."
---

Rozhovor jste nahráli. Cestou domů si ho pustíte a polovina je rozjíždějící se autobus.

Slova tam jsou. Jen leží pod vším ostatním.

<p class="pull">Odstranění šumu už není práce pro studio. Kde probíhá zpracování a co se stane s originálem, je důležitější než tlačítko, které zmáčknete.</p>

## Čtyři způsoby vedle sebe

| Způsob | Kdy funguje | Kam jde zvuk | Originál | Hluk ulice nebo dopravy |
|---|---|---|---|---|
| Aplikace, která snižuje hluk při nahrávání (Clear voice v Záznamníku Pixel) | Při nahrávání, řada Pixel 9 | Aplikace Záznamník | Přepínač při přehrávání umožní poslech bez redukce | Zaměřeno na hluk v pozadí obecně |
| Aplikace, která soubor vyčistí potom (odstranění šumu pomocí AI v TalkSafe) | Po nahrání, i na vystřiženém úseku | Zpracováno v telefonu | Zůstane; vyčištěná verze je nový soubor | Ano, v testech se dvěma lidmi |
| Program do počítače (Redukce šumu v Audacity) | Po nahrání | Váš počítač | Nedotčen, pokud ho nepřepíšete | Podle příručky nevhodné |
| Webová služba (Adobe Podcast Enhance Speech) | Po nahrání | Nahráno do služby | Stáhnete si vyčištěnou kopii | Určeno k oddělení řeči od hluku |

Zbytek stránky prochází, co po vás který z nich ve skutečnosti chce.

## Při nahrávání: Clear voice v Záznamníku Pixel

Google v prosinci 2024 přidal do aplikace Záznamník na telefonech Pixel nastavení **Clear voice**. Snižuje hluk v pozadí během nahrávání a při přehrávání přepínač umožní poslechnout si nahrávku bez redukce.

Háček je v podmínkách. Podle tehdejších zpráv funguje jen s **vestavěným mikrofonem řady Pixel 9**, v monu. Pozdější aktualizace ho přejmenovala na **Auto Clear Voice**.

Pokud máte jeden z těch telefonů a víte předem, že budete na hlučném místě, je to tu nejméně práce. S jakýmkoli jiným telefonem to možnost není.

## V počítači: Audacity

Audacity je zdarma a jeho efekt **Redukce šumu** je klasický způsob. Označíte pár sekund, kde je jen šum, zachytíte profil šumu a potom efekt použijete na celou nahrávku.

Na to, k čemu vznikl, je dobrý: na stálé zvuky jako syčení, bručení nebo klimatizaci. **Příručka Audacity sama říká, že není vhodný pro nepravidelný hluk v pozadí, jako je doprava nebo publikum.** A přesně tím je nahrávka z ulice plná.

Potřebuje také počítač, přenos souboru a trochu trpělivosti s posuvníky. Když nastavení přeženete, příručka varuje před artefakty — krátkými náhodnými záblesky tónu.

## Nahráním na web: webové služby

Nástroje jako **Adobe Podcast Enhance Speech** pracují tak, že nahrajete svůj soubor. Služba ho zpracuje a vy si stáhnete vyčištěnou verzi. Jsou stavěné na řeč a umějí být působivé.

Než nějakou použijete na skutečný rozhovor, vyplatí se vědět dvě věci. Za prvé, **nahrát soubor znamená, že kopie rozhovoru odejde k té službě.** U podcastu to nevadí. U soukromého rozhovoru, ve kterém je někdo další, je to rozhodnutí, které je dobré udělat vědomě. Za druhé, bezplatné verze mají limity délky a denního použití a ty se mění.

## V telefonu, potom: TalkSafe

[TalkSafe](/talksafe/cs/) má **odstranění šumu pomocí AI**, které použijete na už pořízenou nahrávku.

- **Běží v zařízení.** K vyčištění souboru se nic nenahrává.
- **Originál zůstane.** Vyčištěná verze se uloží vedle jako nový soubor.
- **Funguje na vystřiženém úseku.** Nejdřív vystřihněte ty dvě minuty, na kterých záleží, a pak vyčistěte jen je.

V testech s rozhovory dvou lidí nahranými na ulici doprava zmizela a rozhovor zůstal.

Je to stejná aplikace, která začne nahrávat, když uslyší **předem zvolené slovo**, funguje při zamčené obrazovce a uloží **30 sekund před začátkem**. Na ulici tyto dvě funkce zajistí, že nahrávka vůbec existuje; odstranění šumu z ní udělá něco, co se dá poslouchat.

## Originál si vždycky nechte

Odstranění šumu vytváří jinou verzi zvuku. V tom je jeho smysl, a právě proto na originálu záleží.

Pokud by se nahrávka mohla použít — ve stížnosti, ve sporu, v nároku —, **předložte vyčištěnou verzi, pokud je srozumitelnější, a nedotčený originál si nechte vedle ní.** Uveďte, že kopie byla vyčištěna. Originál ukazuje, že nic jiného změněno nebylo. Co se soubory dělat potom, popisuje [Co s nahrávkou dělat, a co s ní nedělat](/blog/cs/after-recording/).

## Dřív, než to budete potřebovat: nahrávejte blíž

Žádný nástroj nevrátí to, co mikrofon nikdy nezachytil. Několik zvyků čištění usnadní:

- **Nejvíc záleží na vzdálenosti.** Telefon na stole mezi dvěma lidmi je lepší než telefon v tašce.
- **Vítr je nejtěžší hluk.** Otočit se k němu zády nebo vstoupit do průchodu pomůže víc než jakékoli nastavení.
- **Hovory na hlasitý odposlech zachytí i místnost.** Pokud takto nahráváte hovor, odstranění šumu může potom hluk v pozadí odstranit. Proč je hlasitý odposlech na Androidu cestou, která zbyla, popisuje [Proč aplikace na nahrávání hovorů na Androidu přestaly fungovat a co funguje dál](/blog/cs/call-recording-android/).

## Stručně

- **Stálé syčení nebo bručení, v počítači:** Audacity.
- **Pixel 9 a trochu plánování:** Clear voice v Záznamníku, zapnutý před začátkem.
- **Výsledek jako ze studia a žádné obavy o soukromí:** webová služba, nahráním souboru.
- **Rozhovor z ulice, který chcete mít v telefonu:** odstranění šumu pomocí AI v TalkSafe, v zařízení, s ponechaným originálem.

Jak se samostatné diktafony srovnávají s telefonem v kvalitě zvuku, popisuje [Diktafony se liší tím, kdy začnou nahrávat](/blog/cs/choosing-a-recorder/).

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">Funkce nástrojů třetích stran jsou popsány podle jejich dokumentace a zpráv v době psaní a mohou se změnit. Sami vyvíjíme aplikaci na nahrávání, jak je uvedeno výše.</p>
