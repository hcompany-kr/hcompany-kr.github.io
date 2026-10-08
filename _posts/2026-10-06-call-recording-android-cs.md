---
lang: cs
ref: call-recording-android
categories: cs
permalink: /blog/cs/call-recording-android/
date: 2026-10-06
eyebrow: Návod
title: "Proč aplikace na nahrávání hovorů na Androidu přestaly fungovat a co funguje dál"
description: "Android odstranil rozhraní v roce 2015, v roce 2019 zablokoval cestu přes mikrofon a Google v květnu 2022 zavřel poslední skulinu. Vestavěná aplikace Telefon pod zákaz nikdy nespadala. A co říká zákon v Česku a na Slovensku."
app: true
app_description: "Aplikace pro nahrávání zvuku na Android, která sama začne nahrávat, když uslyší předem zvolené slovo. Při spuštění uloží i 30 sekund před začátkem."
faq:
  - q: "Proč na Androidu přestaly fungovat aplikace na nahrávání hovorů?"
    a: "Android 6 v roce 2015 odstranil rozhraní pro nahrávání hovorů a Android 10 v roce 2019 zablokoval nahrávání hovorů přes mikrofon. Vývojáři pak přešli na rozhraní usnadnění přístupu a 11. května 2022 Google zavřel i tuto cestu. Aplikace třetích stran na nahrávání hovorů byly z Obchodu Play odstraněny."
  - q: "Umí vestavěná aplikace Telefon nahrávat hovory v Česku?"
    a: "Na některých telefonech ano. Do české verze aplikace Telefon od Googlu dorazilo nahrávání hovorů v roce 2026; obě strany přitom uslyší česky, že se hovor nahrává. U Samsungu podle Mobilmanie funguje nahrávání hovorů s nadstavbou One UI 8, ve které je potřeba stáhnout českou hlasovou syntézu pro upozornění druhé strany."
  - q: "Smím v Česku nahrát telefonní hovor, kterého se účastním?"
    a: "Podle § 86 občanského zákoníku nelze bez svolení člověka pořizovat zvukový záznam jeho soukromého života, podle § 88 odst. 1 ale svolení není třeba, pokud se záznam pořídí nebo použije k výkonu nebo ochraně jiných práv nebo právem chráněných zájmů jiných osob. Trestní zákoník v § 182 postihuje porušení tajemství zpráv posílaných sítí elektronických komunikací a prozrazení tajemství z telefonního hovoru, který nebyl určen pachateli; hovor, kterého se účastníte, určen vám je."
  - q: "A na Slovensku?"
    a: "Podle § 12 slovenského občanského zákoníku lze zvukový záznam fyzické osoby pořídit nebo použít jen s jejím svolením, s výjimkami pro úřední, vědecké, umělecké a zpravodajské účely. Trestným činem podle § 377 trestního zákona je neoprávněné zachycení neveřejně pronesených slov, pokud se záznam zpřístupní třetí osobě nebo jinak použije a způsobí vážnou újmu na právech."
  - q: "Funguje dát hovor na hlasitý odposlech a nahrávat ho aplikací?"
    a: "Ano, na každém telefonu s Androidem, protože aplikace pak nahrává zvuk v místnosti, ne samotný hovor. Cenou je horší kvalita zvuku, hluk v pozadí a to, že hovor slyší všichni v okolí."
  - q: "Je TalkSafe aplikace na nahrávání telefonních hovorů?"
    a: "Ne. TalkSafe je aplikace pro nahrávání zvuku na Android, která nahrává to, co mikrofon slyší v místnosti; k samotnému hovoru přístup nemá. Při hovoru na hlasitý odposlech nahraje obě strany. Začne nahrávat, když uslyší předem zvolené slovo, funguje při zamčené obrazovce a uloží 30 sekund před začátkem."
  - q: "Mění samostatné nahrávací zařízení něco na právní úpravě?"
    a: "Ne. Právo se týká rozhovoru, ne zařízení. Druhý telefon, diktafon nebo hlasitý odposlech nic nemění na tom, jaký souhlas vyžaduje země, ve které jste."
---

Nainstalujete si z Obchodu Play aplikaci na nahrávání hovorů. V hodnoceních všichni píšou, že přestala fungovat. Nainstalujete jinou. Totéž.

S vaším telefonem je všechno v pořádku. Cesta, kterou tyto aplikace používaly, je už roky zavřená, krok za krokem, a většina návodů na tohle téma je starší než ta změna.

<p class="pull">Nahrávání hovorů aplikacemi třetích stran na Androidu skončilo. Vestavěná aplikace Telefon pod zákaz nikdy nespadala — proto to některé telefony stále umějí a váš možná ne.</p>

## Co říká zákon v Česku a na Slovensku

Nejdřív právo. Česká i slovenská úprava stojí hlavně na občanském zákoníku, ale každá jinak.

| Země | Nahrání vlastního hovoru bez souhlasu | Trestní zákon | Základ |
|---|---|---|---|
| Česká republika | Svolení není třeba, pokud se záznam pořídí nebo použije k výkonu nebo ochraně práv; nesmí jít o nepřiměřený zásah | Porušení tajemství zpráv v síti; prozrazení tajemství z hovoru, který nebyl určen pachateli | § 86, 88, 90 obč. zák.; § 182 tr. zák. |
| Slovensko | Zvukový záznam jen se svolením, s výjimkami pro úřední, vědecké, umělecké a zpravodajské účely | Neoprávněné zachycení neveřejných slov, pokud se záznam zpřístupní nebo použije a způsobí vážnou újmu (až 2 roky) | § 12 obč. zák.; § 377 tr. zák. |

Podrobněji:

- **Česká republika:** podle § 86 občanského zákoníku nelze bez svolení člověka pořizovat zvukový záznam jeho soukromého života ani takový záznam šířit. Podle § 88 odst. 1 svolení není třeba, pokud se záznam **pořídí nebo použije k výkonu nebo ochraně jiných práv nebo právem chráněných zájmů** jiných osob, a podle § 90 nesmí být takový důvod využit nepřiměřeným způsobem. Ústavní soud v nálezu II. ÚS 1774/14 z 9. prosince 2014 rozhodl, že tajně pořízený záznam nelze jako důkaz odmítnout jen proto, že obsahuje projevy osobní povahy. Trestní zákoník v § 182 postihuje úmyslné porušení tajemství zpráv posílaných sítí elektronických komunikací a také prozrazení tajemství z telefonního hovoru, **který nebyl určen pachateli**, s úmyslem způsobit škodu nebo získat prospěch; hrozí až dva roky odnětí svobody nebo zákaz činnosti.
- **Slovensko:** podle § 12 občanského zákoníku lze zvukový záznam fyzické osoby pořídit nebo použít jen s jejím svolením, s výjimkami pro úřední, vědecké, umělecké a zpravodajské účely. Podle § 377 trestního zákona je trestným činem neoprávněné zachycení neveřejně pronesených slov záznamovým zařízením, pokud se takový záznam **zpřístupní třetí osobě nebo jinak použije a způsobí jinému vážnou újmu na právech**; hrozí až dva roky odnětí svobody.

## Jak se ta cesta zavřela, ve třech krocích

**2015 — Android 6.** Odstranilo se rozhraní pro nahrávání hovorů. Aplikace už nemohly žádat systém o zvuk hovoru.

**2019 — Android 10.** Zablokovala se zbývající oklika, nahrávání hovoru přes mikrofon.

**11. května 2022 — pravidla Obchodu Play.** Vývojáři přešli na **rozhraní usnadnění přístupu** (Accessibility API), na které se dřívější blokace nevztahovaly. Google zavřel i tuto cestu s tím, že rozhraní **není určeno k nahrávání zvuku hovorů**, a aplikace třetích stran na nahrávání hovorů byly z Obchodu Play odstraněny.

Aplikace, která dnes slibuje nahrávání hovorů, tedy buď využívá vestavěnou aplikaci Telefon — nebo nedělá to, co si myslíte.

## Co nikdy zakázáno nebylo

**Aplikace Telefon, která přišla s vaším telefonem.**

Pravidla z roku 2022 se týkají aplikací třetích stran. Vestavěného nahrávání výrobců se nikdy netýkala a funguje dál tam, kde je nabízeno.

Proto to zvenčí vypadá tak nahodile: dva lidé s Androidem, jeden nahrává hovory jedním klepnutím, druhý nenajde jedinou funkční aplikaci.

## Co nabízejí aplikace Telefon

**Google:** do české verze aplikace Telefon od Googlu dorazilo nahrávání hovorů v únoru 2026. **Obě strany přitom uslyší česky**, že se hovor nahrává, a před začátkem nahrávání proběhne krátké odpočítávání. Google ho zavádí postupně, takže se nemusí objevit všem najednou.

**Samsung:** podle Mobilmanie u Samsungu nahrávání hovorů opět funguje s nadstavbou **One UI 8**, ve které je potřeba stáhnout českou hlasovou syntézu — ta slouží k upozornění druhé strany, že se hovor nahrává.

Co je dostupné na vašem telefonu, závisí na modelu, verzi softwaru a regionu a mění se to. Nejrychleji to zjistíte tak, že otevřete aplikaci Telefon, zahájíte hovor a podíváte se, jestli tam je tlačítko nahrávání. Pokud tam není, žádná aplikace z Obchodu Play ho nepřidá.

## Proč upozornění není drobnost

To upozornění není zdvořilost. Je to mechanismus, díky kterému mohou výrobci funkci nabízet i tam, kde se vyžaduje souhlas: kdo upozornění slyší a mluví dál, ví, že se nahrává.

## Co funguje vždy: místnost, ne linka

Pokud vaše aplikace Telefon tlačítko nahrávání nemá, zbývá jeden způsob, který funguje na každém Androidu.

**Dejte hovor na hlasitý odposlech a nahrávejte místnost.**

Aplikace, která nahrává zvuk v místnosti, se samotného hovoru vůbec nedotýká, takže se na ni žádné z omezení nevztahuje. Váš hlas nahrává přímo, hlas druhé strany z reproduktoru.

Nevýhody jsou skutečné. **Kvalita zvuku klesne**, protože se nahrává malý reproduktor v místnosti místo čistého signálu. **Přidá se hluk v pozadí.** A **hovor slyší všichni v okolí** — v open space nebo ve vlaku tenhle způsob nepřipadá v úvahu.

Z těch tří nevýhod se dá hluk v pozadí řešit dodatečně. **Odstranění šumu pomocí AI** v TalkSafe odstraní z hotové nahrávky hluk v pozadí a ponechá hlasy. Běží v zařízení a vyčištěná verze se uloží jako nový soubor; originál zůstane beze změny.

Pro hovor, který můžete vyřídit na klidném místě, funguje.

## Kde je místo této aplikace, a kde ne

**[TalkSafe](/talksafe/cs/) není aplikace na nahrávání telefonních hovorů.** K samotnému hovoru nemá přístup, ze stejného důvodu jako všechny ostatní aplikace v Obchodu Play. Nahrává to, co mikrofon slyší v místnosti.

Při hovoru na hlasitý odposlech jsou to obě strany. Při rozhovoru tváří v tvář je to rozhovor před vámi — k tomu byla vlastně vytvořena.

Jejím přínosem je začátek. Začne nahrávat, když uslyší **předem zvolené slovo**, funguje při **zamčené obrazovce** a uloží **30 sekund před začátkem**. U hovoru, který se v půlce zkomplikuje, je to přesně ta část, která by jinak chyběla.

## Nahrát rovnou i souhlas

Tam, kde je potřeba souhlas, nebo když se prostě chcete zeptat, může k tomu posloužit klíčové slovo. Nastavte slovo ze své otázky, například **„nahrát“**, a zapněte hlasitý odposlech.

Pak se zeptejte: „Můžu si ten hovor nahrát?“ Nahrávání začne ve chvíli, kdy se ptáte, a odpověď druhé strany je v souboru. Nemusíte nejdřív viditelně mačkat tlačítko a teprve pak se ptát.

## Co se nezměnilo

**Právo se týká rozhovoru, ne zařízení.**

Druhý telefon, diktafon nebo hlasitý odposlech nic nemění na tom, co platí v zemi, ve které jste. Omezení Obchodu Play jsou pravidla platformy, ne zákon — splnit jedno neznamená splnit druhé.

## Stručně

**Nahrávání hovorů aplikacemi třetích stran skončilo**, ve třech krocích do května 2022, a žádnou aplikací se nevrátí.

**Vestavěná aplikace Telefon zakázaná nikdy nebyla.** Google i Samsung v ní nahrávání nabízejí, s upozorněním pro druhou stranu.

**Hlasitý odposlech a aplikace na nahrávání fungují všude**, za cenu kvality zvuku a soukromí.

**A nic z toho nemění pravidla** země, ve které jste.

Způsoby, jak spustit nahrávání bez rukou, popisuje [Jak začít nahrávat, aniž byste se dotkli telefonu](/blog/cs/hands-free-recording/).

Pět významů „automatického nahrávání“, včetně nahrávání při spojení hovoru, popisuje [Ne každý „automatický“ diktafon dělá totéž](/blog/cs/auto-recording-types/).

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">Údaje o zařízeních a regionech vycházejí z oznámení výrobců a článků, které se často mění; zkontrolujte vlastní aplikaci Telefon. Obecná informace, nikoli právní rada — pravidla pro nahrávání se v jednotlivých zemích liší.</p>
