---
lang: it
ref: call-recording-android
categories: it
permalink: /blog/it/call-recording-android/
date: 2026-09-04
eyebrow: Come si fa
title: "Perché le app per registrare le chiamate non funzionano più su Android"
description: "Android ha tolto l'API nel 2015, chiuso la via del microfono nel 2019 e a maggio 2022 Google ha tappato l'ultima scorciatoia. Il dialer di serie non è mai rientrato nel divieto, ed è per questo che ad alcuni funziona e ad altri no."
app: true
app_description: "Un registratore vocale per Android che inizia a registrare da solo quando sente una parola scelta in anticipo. All'avvio salva anche i 30 secondi precedenti."
faq:
  - q: "Perché le app per registrare le chiamate non funzionano più su Android?"
    a: "Android 6, del 2015, ha rimosso l'API per la registrazione delle chiamate. Android 10, del 2019, ha bloccato la registrazione attraverso il microfono. Gli sviluppatori sono passati alla API di accessibilità come scorciatoia e l'11 maggio 2022 Google ha chiuso anche quella, precisando che quella API non era stata progettata per registrare l'audio delle chiamate. Le app di terze parti sono state rimosse dal Play Store."
  - q: "Allora perché sul telefono di un'altra persona funziona?"
    a: "La policy del 2022 riguarda le app di terze parti, non il dialer preinstallato sul telefono. La registrazione integrata in Google Phone, nel dialer Samsung o in quello Xiaomi non è stata toccata e continua a funzionare dove viene offerta."
  - q: "In quali paesi e su quali telefoni è disponibile?"
    a: "Dipende dal produttore, dal modello e dalla regione, e cambia nel tempo. Viene documentato un funzionamento stabile in mercati come India, Indonesia, Sudafrica e parte dell'America Latina. Google la offre su Pixel 6 e successivi negli Stati Uniti, nel Regno Unito e in altri paesi, e Pixel 9 e successivi, escluso il 9a, aggiungono Call Notes con trascrizione negli Stati Uniti, Regno Unito, Canada, Irlanda, Australia e Giappone."
  - q: "Perché in alcuni paesi non c'è?"
    a: "Per le leggi che richiedono il consenso di tutti i partecipanti e per le politiche degli operatori. Dove serve che tutti acconsentano prima di registrare, un produttore che includa di serie una registrazione silenziosa si espone in quel mercato, quindi la funzione viene disattivata o non c'è affatto."
  - q: "La registrazione integrata avvisa l'altra persona?"
    a: "L'app Phone di Google riproduce un avviso sonoro che informa che la chiamata è in registrazione, e lo sentono tutti i partecipanti. È il meccanismo con cui la funzione soddisfa i requisiti di consenso di tutte le parti dove esistono."
  - q: "Funziona mettere il vivavoce e registrare con un'altra app?"
    a: "Sì, e funziona su qualunque Android a prescindere dalle restrizioni, perché il registratore capta il suono della stanza e non l'audio della chiamata. In cambio la qualità cala, entra rumore di fondo e chi è vicino sente la conversazione."
  - q: "Cambia qualcosa dal punto di vista legale se uso un apparecchio separato?"
    a: "No. La legge riguarda la conversazione, non l'attrezzatura. Usare un registratore esterno non modifica il consenso richiesto nella tua giurisdizione."
---

Installi un'app per registrare le chiamate. Le recensioni sono piene di gente che dice che ha smesso di funzionare. Ne installi un'altra. Uguale.

Non è il telefono. **La strada che quelle app usavano è stata chiusa a tappe nell'arco di anni**, e la maggior parte degli articoli che escono cercando è precedente al cambiamento.

<p class="pull">Le app di terze parti per registrare le chiamate sono finite. Il dialer di serie non è mai rientrato nel divieto, ed è per questo che ad alcuni funziona e ad altri no.</p>

## È stata chiusa in tre passaggi

**2015, Android 6.** Rimossa l'API per la registrazione delle chiamate. Le app non potevano più chiedere al sistema l'audio della conversazione.

**2019, Android 10.** Bloccata la scorciatoia rimasta: registrare la chiamata attraverso il microfono.

**11 maggio 2022, la policy del Play Store.** Gli sviluppatori si erano spostati sulla **API di accessibilità**, rimasta fuori dai blocchi precedenti e diventata l'unica cosa che teneva in vita queste app. Google l'ha chiusa precisando che quella API **non era stata progettata per registrare l'audio delle chiamate**, e le app di terze parti sono uscite dallo store.

C'è una seconda ragione che vale la pena conoscere. La API di accessibilità esiste per le app che assistono le persone con disabilità, e diversi sviluppatori la stavano usando per tracciare gli utenti. Il divieto sulla registrazione delle chiamate ha fatto parte di una stretta più ampia su quella porta.

Quindi un'app che oggi promette di registrare le chiamate **o sta usando il dialer di sistema, o non fa quello che pensi.**

## Quello che non è mai stato vietato

**Il dialer preinstallato sul telefono.**

La policy del 2022 riguarda le app di terze parti. La registrazione integrata in **Google Phone**, nel **dialer Samsung** o in quello **Xiaomi** è rimasta intatta e continua a funzionare dove viene offerta.

Ecco perché da fuori sembra arbitrario. Due persone con Android: una registra con un pulsante, l'altra non riesce a far funzionare niente.

## Dove esiste

Dipende da produttore, modello e regione, e si muove. Da leggere come una fotografia del momento, non come una regola.

Viene documentato un funzionamento stabile in mercati come **India, Indonesia, Sudafrica e parte dell'America Latina.**

**Google** la offre su **Pixel 6 e successivi** negli Stati Uniti, nel Regno Unito e in altri paesi. **Pixel 9 e successivi**, escluso il 9a, aggiungono **Call Notes** con trascrizione negli Stati Uniti, Regno Unito, Canada, Irlanda, Australia e Giappone.

**Samsung** ha aggiunto la registrazione delle chiamate negli **Stati Uniti** con un aggiornamento One UI, sui Galaxy S25, S24, S23, Z Fold e Flip 5 e 6 e su alcuni modelli della serie A.

Il modo più rapido per togliersi il dubbio è aprire il proprio dialer durante una chiamata e vedere se c'è il pulsante di registrazione. **Se non c'è, nessuna app del Play Store ce lo metterà.**

## Perché in alcuni paesi manca

**Per le leggi sul consenso di tutte le parti e per le politiche degli operatori.**

Dove tutti i partecipanti devono acconsentire prima che una chiamata venga registrata, un produttore che include di serie una registrazione silenziosa si crea un'esposizione legale in quel mercato. Quindi la funzione viene disattivata o semplicemente non compare.

Guarda come Google risolve lo stesso problema dove la funzione c'è: l'app Phone **riproduce un avviso sonoro che informa che la chiamata è in registrazione**, e lo sentono tutti. Quell'avviso non è cortesia. È il meccanismo che soddisfa il consenso di tutte le parti.

Come viene trattata in Italia la registrazione di una conversazione a cui partecipi è in [Registrare sì, diffondere no](/blog/it/registrare-conversazione/).

## Quello che resta è la stanza, non la linea

Se il tuo dialer non ha il pulsante di registrazione, resta un metodo. E funziona su qualunque Android.

**Mettere la chiamata in vivavoce e registrare il suono della stanza.**

Un registratore che capta l'ambiente non tocca l'audio della chiamata, quindi nessuna delle restrizioni lo riguarda. La tua voce entra direttamente, quella dell'altro esce dall'altoparlante.

Gli svantaggi sono reali e vanno detti. **La qualità cala**, perché stai registrando un piccolo altoparlante in una stanza. **Entra rumore di fondo.** E **chi è vicino sente la chiamata**, il che esclude il metodo in ufficio o in treno.

Per una chiamata che puoi ricevere in un posto tranquillo, funziona.

## Cosa fa questa app e cosa non fa

Qui conta più essere esatti che convincenti.

**[TalkSafe](https://hcompany-kr.github.io/talksafe/) non è un registratore di chiamate.** Non può accedere all'audio della conversazione telefonica, per lo stesso motivo per cui non può nessun'altra app del Play Store. Quello che registra è **il suono della stanza che arriva al microfono.**

In vivavoce questo comprende entrambe le parti della chiamata. Di persona comprende la conversazione che hai davanti, **che è il caso per cui è stata pensata.**

Quello che aggiunge è l'avvio. Parte quando sente una **parola scelta in anticipo**, funziona a **schermo bloccato** e salva i **30 secondi precedenti** all'inizio. In una chiamata che si mette male a metà, è esattamente la parte che di solito manca.

Le cinque cose diverse che possono chiamarsi registrazione automatica sono in ["Registrazione automatica" non vuol dire la stessa cosa in tutte le app](/blog/it/auto-recording-types/).

## Quello che non è cambiato

**La legge riguarda la conversazione, non l'attrezzatura.**

Usare un secondo telefono, un registratore dedicato o il vivavoce non modifica il consenso richiesto nella tua giurisdizione.

Le restrizioni del Play Store sono **una policy di piattaforma, non una legge.** Rispettare l'una non significa aver rispettato l'altra.

## In sintesi

**Le app di terze parti per registrare le chiamate non ci sono più**, in tre passaggi che finiscono a maggio 2022, e non torneranno.

**La registrazione del dialer di sistema non è mai stata vietata.** Averla dipende dal telefono e dal paese.

**Vivavoce più registratore d'ambiente funziona ovunque**, al prezzo di qualità e riservatezza.

**E niente di tutto questo cambia le regole sul consenso** dove vivi.

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">La disponibilità per dispositivo e regione cambia spesso; controlla il tuo dialer. Informazioni di carattere generale, non consulenza legale.</p>
