---
lang: nl
ref: call-recording-android
categories: nl
permalink: /blog/nl/call-recording-android/
date: 2026-10-06
eyebrow: Handleiding
title: "Waarom apps om gesprekken op te nemen op Android niet meer werken, en wat nog wel werkt"
description: "Android haalde de interface in 2015 weg, blokkeerde in 2019 de route via de microfoon, en Google sloot in mei 2022 de laatste maas. De ingebouwde Telefoon-app viel daar nooit onder. Plus wat de wet zegt in Nederland, België, Suriname, Aruba, Curaçao en Sint Maarten."
app: true
app_description: "Een opname-app voor Android die vanzelf begint met opnemen zodra hij een vooraf gekozen woord hoort. Bij de start worden ook de 30 seconden daarvoor bewaard."
faq:
  - q: "Waarom werken apps om telefoongesprekken op te nemen niet meer op Android?"
    a: "Android 6 haalde in 2015 de interface voor gespreksopname weg, en Android 10 blokkeerde in 2019 het opnemen van gesprekken via de microfoon. Ontwikkelaars weken daarna uit naar de toegankelijkheidsinterface, en op 11 mei 2022 sloot Google ook die route. Apps van derden om gesprekken op te nemen zijn uit de Play Store verwijderd."
  - q: "Mag ik in Nederland een telefoongesprek opnemen waaraan ik zelf deelneem?"
    a: "Ja. Artikel 139a van het Wetboek van Strafrecht stelt het opnemen van een gesprek alleen strafbaar voor wie geen deelnemer is en niet in opdracht van een deelnemer handelt, en artikel 139c het aftappen of opnemen van telecommunicatie die niet voor jou bestemd is. Een gesprek waaraan je zelf deelneemt, valt onder geen van beide."
  - q: "En in België?"
    a: "Ook daar pleegt een deelnemer die een communicatie opneemt volgens het Hof van Cassatie (2015) geen misdrijf. Wie de opname met bedrieglijk opzet of met het oogmerk te schaden gebruikt, is wel strafbaar volgens artikel 314bis van het Strafwetboek."
  - q: "Kan de ingebouwde Telefoon-app gesprekken opnemen?"
    a: "Op sommige toestellen wel. Google kondigde in september 2025 aan dat gespreksopname in de Telefoon-app voor Pixel 6 en nieuwer wordt uitgerold in alle landen waar Pixel wordt aangeboden; beide kanten krijgen dan een melding. Samsung biedt gespreksopname in One UI 7 aan met een gesproken melding voor de ander, maar niet in elk land en niet op elk toestel. Kijk in je eigen Telefoon-app of er een opnameknop is."
  - q: "Werkt het om het gesprek op de luidspreker te zetten en met een opname-app op te nemen?"
    a: "Ja, op elke Android-telefoon, omdat de app dan het geluid in de ruimte opneemt en niet het gesprek zelf. De nadelen zijn een slechtere geluidskwaliteit, achtergrondgeluid en dat iedereen in de buurt meeluistert."
  - q: "Is TalkSafe een app om telefoongesprekken op te nemen?"
    a: "Nee. TalkSafe is een opname-app voor Android die opneemt wat de microfoon in de ruimte hoort; tot het gesprek zelf heeft de app geen toegang. Bij een gesprek op de luidspreker neemt hij beide kanten op. Hij begint als hij een vooraf gekozen woord hoort, werkt met een vergrendeld scherm en bewaart de 30 seconden vóór de start."
  - q: "Verandert een apart opnameapparaat iets aan de wet?"
    a: "Nee. De wet gaat over het gesprek, niet over het apparaat. Een tweede telefoon, een dictafoon of de luidspreker verandert niets aan welke toestemming in jouw land nodig is."
---

Je installeert een app om gesprekken op te nemen uit de Play Store. In de recensies schrijft iedereen dat hij niet meer werkt. Je installeert een andere. Hetzelfde.

Er is niets mis met je telefoon. De route die deze apps gebruikten, is al jaren dicht, stap voor stap, en de meeste uitleg erover is ouder dan die verandering.

<p class="pull">Gesprekken opnemen met apps van derden is op Android voorbij. De ingebouwde Telefoon-app viel nooit onder het verbod — daarom kunnen sommige telefoons het nog wel en de jouwe misschien niet.</p>

## Wat de wet zegt in het Nederlandse taalgebied

Eerst het juridische: in alle landen die hier besproken worden, mag je een gesprek waaraan je zelf deelneemt opnemen. Strafbaar is het opnemen door iemand die **geen** deelnemer is.

| Land | Eigen gesprek opnemen zonder toestemming | Wat wel strafbaar is | Grondslag |
|---|---|---|---|
| Nederland | Toegestaan | Opnemen door een niet-deelnemer; aftappen van telecommunicatie die niet voor jou bestemd is | Art. 139a, 139b, 139c Sr |
| België | Geen misdrijf (Cassatie 2015) | De opname met bedrieglijk opzet of om te schaden gebruiken | Art. 314bis Sw. |
| Suriname | Toegestaan | Opnemen door een niet-deelnemer (tot vier jaar) | Art. 187d WvSr |
| Aruba | Toegestaan | Opnemen door een niet-deelnemer (tot zes maanden) | Art. 2:71 WvSr |
| Curaçao | Toegestaan | Opnemen door een niet-deelnemer (tot twee jaar) | Art. 2:71 WvSr |
| Sint Maarten | Toegestaan | Opnemen door een niet-deelnemer (tot twee jaar) | Art. 2:71 WvSr |

Caribisch Nederland (Bonaire, Sint Eustatius en Saba) is hier niet behandeld.

Of een rechter een opname als bewijs gebruikt, is een aparte vraag die per geval wordt beoordeeld. En dat je mag opnemen, betekent niet dat je de opname mag rondsturen: in België is precies het gebruik met het oogmerk te schaden strafbaar.

## Hoe de route werd gesloten, in drie stappen

**2015 — Android 6.** De interface voor gespreksopname werd weggehaald. Apps konden het systeem niet meer om het geluid van het gesprek vragen.

**2019 — Android 10.** De overgebleven omweg, het gesprek via de microfoon opnemen, werd geblokkeerd.

**11 mei 2022 — het Play Store-beleid.** Ontwikkelaars waren uitgeweken naar de **toegankelijkheidsinterface** (Accessibility API), die buiten de eerdere blokkades viel. Google sloot ook die route, met de uitleg dat de interface **niet bedoeld is om gespreksgeluid op te nemen**, en apps van derden om gesprekken op te nemen werden uit de Play Store verwijderd.

Een app die vandaag belooft gesprekken op te nemen, gebruikt dus de ingebouwde Telefoon-app — of doet niet wat je denkt.

## Wat nooit verboden werd

**De Telefoon-app die op je toestel stond.**

Het beleid van 2022 geldt voor apps van derden. De ingebouwde gespreksopname van fabrikanten viel er nooit onder en werkt nog steeds waar ze wordt aangeboden.

Daarom lijkt het van buitenaf zo willekeurig: twee mensen met een Android-telefoon, de een neemt gesprekken op met één tik, de ander vindt geen enkele app die werkt.

## Wat de Telefoon-apps bieden

**Google** kondigde in september 2025 aan dat gespreksopname in de Telefoon-app voor **Pixel 6 en nieuwer** wordt uitgerold in alle landen waar Pixel wordt aangeboden. Volgens Google krijgen **beide kanten een melding** als de opname begint.

**Samsung** biedt in **One UI 7** gespreksopname in de Telefoon-app aan, waarbij de ander **een gesproken melding** hoort dat het gesprek wordt opgenomen. Samsung zet de functie per land aan of uit; of ze op jouw toestel verschijnt, hangt af van model en softwareversie.

Wat er op jouw toestel beschikbaar is, hangt af van model, softwareversie en regio, en dat verandert. Het snelst kom je erachter door je Telefoon-app te openen, een gesprek te starten en naar een opnameknop te zoeken. Staat die er niet, dan kan geen enkele app uit de Play Store hem toevoegen.

## Wat altijd werkt: de ruimte, niet de lijn

Heeft je Telefoon-app geen opnameknop, dan blijft er één manier over, en die werkt op elke Android-telefoon.

**Zet het gesprek op de luidspreker en neem de ruimte op.**

Een opname-app die het geluid in de ruimte opneemt, raakt het gesprek zelf niet aan, dus geen van de beperkingen geldt ervoor. Jouw kant neemt hij rechtstreeks op, de andere kant via de luidspreker.

De nadelen zijn reëel. **De geluidskwaliteit gaat omlaag**, omdat je een klein luidsprekertje in een ruimte opneemt in plaats van een schoon signaal. **Er komt achtergrondgeluid bij.** En **iedereen in de buurt luistert mee** — in een kantoortuin of in de trein valt deze manier af.

Van de drie is het achtergrondgeluid iets wat je achteraf kunt aanpakken. De **AI-ruisonderdrukking** van TalkSafe haalt achtergrondgeluid uit een voltooide opname en laat de stemmen over. Ze werkt op het toestel, en de opgeschoonde versie wordt als nieuw bestand bewaard; het origineel blijft ongewijzigd.

Voor een gesprek dat je op een rustige plek kunt voeren, werkt het.

## Waar deze app staat, en waar niet

**[TalkSafe](/talksafe/nl/) is geen app om telefoongesprekken op te nemen.** Tot het gesprek zelf heeft hij geen toegang, om dezelfde reden als alle andere apps in de Play Store. Hij neemt op wat de microfoon in de ruimte hoort.

Bij een gesprek op de luidspreker zijn dat beide kanten. Bij een gesprek in persoon is het het gesprek voor je — daar is hij eigenlijk voor gemaakt.

Wat hij toevoegt, is de start. Hij begint als hij een **vooraf gekozen woord** hoort, werkt met een **vergrendeld scherm** en bewaart de **30 seconden vóór de start**. Bij een gesprek dat halverwege lastig wordt, is dat precies het deel dat anders zou ontbreken.

## De toestemming meteen mee opnemen

Als je liever eerst vraagt, kun je het trefwoord daarvoor gebruiken. Stel een woord uit je vraag in, bijvoorbeeld **„opnemen”**, en zet de luidspreker aan.

Vraag dan: „Mag ik dit gesprek opnemen?” De opname begint op het moment dat je het vraagt, en het antwoord van de ander staat in het bestand. Je hoeft niet eerst zichtbaar op een knop te drukken en daarna te vragen.

## Wat niet veranderd is

**De wet gaat over het gesprek, niet over het apparaat.**

Een tweede telefoon, een dictafoon of de luidspreker verandert niets aan wat er in jouw land geldt. De beperkingen van de Play Store zijn platformbeleid, geen wet — aan het ene voldoen is niet hetzelfde als aan het andere voldoen.

## Kort gezegd

**Gesprekken opnemen met apps van derden is voorbij**, in drie stappen tot mei 2022, en het komt via geen enkele app terug.

**De ingebouwde Telefoon-app werd nooit verboden.** Google en Samsung bieden er gespreksopname aan, met een melding voor de ander, maar niet op elk toestel.

**Luidspreker plus opname-app werkt overal**, ten koste van geluidskwaliteit en privacy.

**En in het hele hier besproken gebied mag je je eigen gesprek opnemen** — wat je er daarna mee doet, is een aparte vraag.

Manieren om een opname zonder handen te starten, staan in [Een opname starten zonder je telefoon aan te raken](/blog/nl/hands-free-recording/).

De vijf betekenissen van „automatisch opnemen”, inclusief opname die start als een gesprek tot stand komt, staan in [Niet elke „automatische” recorder doet hetzelfde](/blog/nl/auto-recording-types/).

Wat je na de opname met het bestand doet — en waarom verspreiden eigen regels heeft — staat in [Wat je met een opname doet, en wat je er niet mee doet](/blog/nl/after-recording/).

Hoe je straatlawaai op de telefoon uit een opname haalt, en welke hulpmiddelen dat aankunnen, staat in [Achtergrondgeluid uit een spraakopname halen op Android](/blog/nl/remove-background-noise/).

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">De informatie over toestellen en regio's berust op aankondigingen van fabrikanten en berichten die vaak veranderen; controleer je eigen Telefoon-app. Algemene informatie, geen juridisch advies — de regels voor opnemen verschillen per land.</p>
