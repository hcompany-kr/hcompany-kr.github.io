---
lang: de
ref: call-recording-android
categories: de
permalink: /blog/de/call-recording-android/
date: 2026-10-01
eyebrow: Anleitung
title: "Warum Anrufaufnahme-Apps auf Android nicht mehr funktionieren – und was noch geht"
description: "Android hat die Schnittstelle 2015 entfernt, 2019 den Weg über das Mikrofon gesperrt, und Google hat im Mai 2022 das letzte Schlupfloch geschlossen. Die eingebaute Telefon-App war nie betroffen. Dazu, was in Deutschland, Österreich, der Schweiz, Liechtenstein, Luxemburg und Belgien gilt."
app: true
app_description: "Eine Aufnahme-App für Android, die automatisch mit der Aufnahme beginnt, wenn sie ein vorher festgelegtes Wort hört. Beim Start werden auch die 30 Sekunden davor gespeichert."
faq:
  - q: "Warum funktionieren Apps zur Anrufaufnahme auf Android nicht mehr?"
    a: "Android 6 hat 2015 die Schnittstelle zur Anrufaufnahme entfernt, Android 10 hat 2019 die Aufnahme von Anrufen über das Mikrofon gesperrt. Entwickler wichen danach auf die Bedienungshilfen-Schnittstelle (Accessibility API) aus, und am 11. Mai 2022 hat Google auch diesen Weg geschlossen. Anrufaufnahme-Apps von Drittanbietern wurden aus dem Play Store entfernt."
  - q: "Kann man in Deutschland Anrufe mit der eingebauten Telefon-App aufnehmen?"
    a: "Auf manchen Geräten ja. Samsung bietet auf der Galaxy-S25-Serie mit One UI 7 eine Anrufaufzeichnung in der Telefon-App an, bei der das Gegenüber eine automatische Ansage hört, dass das Gespräch aufgezeichnet wird. Google hat im September 2025 angekündigt, die Anrufaufnahme der Telefon-App für Pixel 6 und neuer in allen Ländern einzuführen, in denen Pixel angeboten wird; auch dabei werden die Beteiligten benachrichtigt."
  - q: "Darf man ein Telefonat aufnehmen, an dem man selbst teilnimmt?"
    a: "Das hängt vom Land ab. In Deutschland ist es nach § 201 StGB ohne Einwilligung strafbar, in der Schweiz nach Art. 179ter StGB ebenfalls, mit einer Ausnahme für Bestellungen und Reservationen im Geschäftsverkehr. In Österreich und Liechtenstein fällt die Aufnahme als Teilnehmer nicht unter § 120 Abs. 1 StGB, die Weitergabe ohne Zustimmung aber unter Abs. 2. In Belgien begeht ein Teilnehmer, der aufnimmt, nach dem Kassationshof keine Straftat. In Luxemburg enthält Art. 2 des Gesetzes vom 11. August 1982 keine Ausnahme für Teilnehmer."
  - q: "Funktioniert es, das Telefonat auf Lautsprecher zu stellen und mit einer Aufnahme-App aufzunehmen?"
    a: "Ja, auf jedem Android-Telefon, weil die App dann den Ton im Raum aufnimmt und nicht den Anruf selbst. Die Nachteile sind schlechtere Tonqualität, Hintergrundgeräusche und dass alle in der Nähe das Gespräch mithören."
  - q: "Ist TalkSafe eine App zur Anrufaufnahme?"
    a: "Nein. TalkSafe ist eine Aufnahme-App für Android, die aufnimmt, was das Mikrofon im Raum hört; auf den Anruf selbst hat sie keinen Zugriff. Bei einem Telefonat auf Lautsprecher nimmt sie beide Seiten auf. Sie startet, wenn sie ein vorher festgelegtes Wort hört, funktioniert bei gesperrtem Bildschirm und speichert die 30 Sekunden vor dem Start mit."
  - q: "Wie holt man am Telefon die Einwilligung ein, ohne umständlich zu werden?"
    a: "Legen Sie in TalkSafe ein Wort aus Ihrer Frage als Schlüsselwort fest, etwa ‚aufnehmen‘, und stellen Sie das Telefonat auf Lautsprecher. Fragen Sie dann ‚Darf ich das Gespräch aufnehmen?‘, beginnt die Aufnahme in diesem Moment, und die Antwort Ihres Gegenübers ist in der Datei."
  - q: "Ändert ein separates Aufnahmegerät etwas an der Rechtslage?"
    a: "Nein. Das Recht knüpft an das Gespräch an, nicht an das Gerät. Ein zweites Telefon, ein Diktiergerät oder der Lautsprecher ändert nichts daran, welche Einwilligung in Ihrem Land nötig ist."
---

Sie installieren eine App zur Anrufaufnahme aus dem Play Store. In den Bewertungen schreiben alle, dass sie nicht mehr funktioniert. Sie installieren eine andere. Dasselbe.

Mit Ihrem Telefon stimmt alles. Der Weg, den diese Apps benutzt haben, ist seit Jahren geschlossen, in mehreren Schritten, und die meisten Anleitungen dazu sind älter als die Änderung.

<p class="pull">Anrufaufnahme durch Drittanbieter-Apps ist auf Android vorbei. Die eingebaute Telefon-App war nie Teil des Verbots – deshalb können manche Telefone es noch und Ihres vielleicht nicht.</p>

## Was im deutschsprachigen Raum gilt

Bevor es um Technik geht: Ob Sie ein eigenes Telefonat ohne Einwilligung des Gegenübers aufnehmen dürfen, ist in den Ländern, in denen Deutsch Amtssprache ist, sehr unterschiedlich geregelt.

| Land | Eigenes Telefonat ohne Einwilligung aufnehmen | Grundlage |
|---|---|---|
| Deutschland | Strafbar, auch als Teilnehmer | § 201 StGB |
| Österreich | Nicht nach Abs. 1 strafbar; Weitergabe an Dritte ohne Zustimmung strafbar | § 120 StGB |
| Schweiz | Strafbar auf Antrag; Ausnahme für Bestellungen und Reservationen im Geschäftsverkehr | Art. 179ter, 179quinquies StGB |
| Liechtenstein | Wie Österreich | § 120 StGB |
| Luxemburg | Wortlaut ohne Ausnahme für Teilnehmer | Art. 2 Gesetz vom 11.08.1982 |
| Belgien | Keine Straftat für den Teilnehmer; Verwendung in Schädigungsabsicht strafbar | Art. 314bis StGB, Kassationshof 2015 |

Im Einzelnen:

- **Deutschland:** Nach § 201 StGB ist es strafbar, das nichtöffentlich gesprochene Wort eines anderen unbefugt aufzunehmen – **auch als Gesprächsteilnehmer**. Die Strafe reicht bis zu drei Jahren Freiheitsstrafe oder Geldstrafe.
- **Österreich:** § 120 Abs. 1 StGB erfasst, wer sich mit einem Aufnahmegerät Kenntnis von einer Äußerung verschafft, die **nicht für ihn bestimmt** ist. Ein Telefonat, an dem Sie teilnehmen, ist für Sie bestimmt. Wer eine solche Aufnahme aber ohne Zustimmung des Sprechers einem Dritten zugänglich macht oder veröffentlicht, macht sich nach § 120 Abs. 2 strafbar.
- **Schweiz:** Art. 179ter StGB bestraft auf Antrag, wer als Gesprächsteilnehmer ein nichtöffentliches Gespräch ohne Einwilligung der anderen aufnimmt. Nicht strafbar ist nach Art. 179quinquies StGB die Aufnahme von Telefongesprächen im Geschäftsverkehr, die **Bestellungen, Aufträge, Reservationen und ähnliche Geschäftsvorfälle** zum Inhalt haben.
- **Liechtenstein:** § 120 des liechtensteinischen StGB ist wie der österreichische aufgebaut: Abs. 1 betrifft Äußerungen, die nicht für den Aufnehmenden bestimmt sind, Abs. 2 die Weitergabe einer Aufnahme ohne Einverständnis des Sprechenden.
- **Luxemburg:** Art. 2 des Gesetzes vom 11. August 1982 über den Schutz des Privatlebens bestraft, wer im privaten Rahmen gesprochene Worte eines Menschen **ohne dessen Einwilligung** aufnimmt, mit acht Tagen bis einem Jahr Freiheitsstrafe und/oder Geldstrafe. Eine Ausnahme für Gesprächsteilnehmer enthält der Wortlaut nicht; eine Gerichtsentscheidung, die genau diesen Fall klärt, haben wir nicht gefunden.
- **Belgien** (auch Ostbelgien): Der Kassationshof hat 2015 bestätigt, dass ein Teilnehmer, der eine Kommunikation aufnimmt, keine Straftat begeht. Wer die Aufnahme in betrügerischer oder schädigender Absicht verwendet, wird nach Art. 314bis StGB bestraft.

Südtirol, wo italienisches Recht gilt, ist hier nicht erfasst.

## Wie es geschlossen wurde, in drei Schritten

**2015 – Android 6.** Die Schnittstelle zur Anrufaufnahme wurde entfernt. Apps konnten das System nicht mehr nach dem Ton des Anrufs fragen.

**2019 – Android 10.** Der verbleibende Umweg, den Anruf über das Mikrofon mitzuschneiden, wurde gesperrt.

**11. Mai 2022 – die Play-Store-Richtlinie.** Entwickler waren auf die **Bedienungshilfen-Schnittstelle** (Accessibility API) ausgewichen, die von den früheren Sperren nicht betroffen war. Google hat auch diesen Weg geschlossen, mit der Begründung, die Schnittstelle sei **nicht für die Aufnahme von Anrufen gedacht**, und Anrufaufnahme-Apps von Drittanbietern wurden aus dem Play Store entfernt.

Eine App, die heute Anrufaufnahme verspricht, nutzt also entweder die eingebaute Telefon-App – oder sie tut nicht das, was Sie denken.

## Was nie verboten wurde

**Die Telefon-App, die auf Ihrem Gerät vorinstalliert ist.**

Die Richtlinie von 2022 gilt für Drittanbieter-Apps. Die eingebaute Anrufaufnahme der Hersteller war davon nie betroffen und funktioniert weiter, wo sie angeboten wird.

Deshalb wirkt das von außen so willkürlich: Zwei Menschen mit Android-Telefon, der eine nimmt Anrufe mit einem Tippen auf, der andere findet keine einzige App, die funktioniert.

## Was es in der Telefon-App gibt

**Samsung** bietet auf der **Galaxy-S25-Serie mit One UI 7** eine Anrufaufzeichnung in der Telefon-App an. Laut Samsungs deutscher Support-Seite erhält das Gegenüber dabei **eine automatische Ansage, dass das Gespräch aufgezeichnet wird**. Kommt ein weiterer Teilnehmer dazu, wird die Ansage nicht erneut abgespielt; Samsung weist darauf hin, diesen dann selbst zu informieren.

**Google** hat im September 2025 angekündigt, die Anrufaufnahme der Telefon-App für **Pixel 6 und neuer** in allen Ländern einzuführen, in denen Pixel angeboten wird. Auch hier werden laut Google **beide Seiten benachrichtigt**, wenn die Aufnahme beginnt.

Was genau auf Ihrem Gerät verfügbar ist, hängt von Modell, Softwarestand und Region ab und ändert sich. Am schnellsten finden Sie es heraus, indem Sie die Telefon-App öffnen, einen Anruf starten und nach einer Aufnahmetaste suchen. Ist dort keine, kann keine App aus dem Play Store sie hinzufügen.

## Warum die Ansage kein Zufall ist

Die Ansage ist keine Höflichkeit. Sie ist der Mechanismus, mit dem die Hersteller Länder bedienen, in denen alle Beteiligten einwilligen müssen: Wer die Ansage hört und weiterspricht, weiß, dass aufgenommen wird.

Eine stille Aufnahme als Standard auszuliefern, wäre für einen Hersteller in Deutschland ein rechtliches Risiko. Deshalb bieten Samsung und Google die Funktion hier mit Ansage an.

## Was immer geht: der Raum, nicht die Leitung

Wenn Ihre Telefon-App keine Aufnahmetaste hat, bleibt ein Weg, und der funktioniert auf jedem Android-Telefon.

**Stellen Sie das Telefonat auf Lautsprecher und nehmen Sie den Raum auf.**

Eine Aufnahme-App, die den Ton im Raum aufnimmt, berührt den Anruf selbst nicht, deshalb gilt keine der Sperren für sie. Ihre Seite nimmt sie direkt auf, die andere Seite über den Lautsprecher.

Die Nachteile sind real. **Die Tonqualität sinkt**, weil ein kleiner Lautsprecher im Raum aufgenommen wird statt eines sauberen Signals. **Hintergrundgeräusche kommen dazu.** Und **alle in der Nähe hören mit** – im Großraumbüro oder im Zug scheidet das aus.

Für ein Telefonat, das Sie an einem ruhigen Ort führen können, funktioniert es.

## Wo diese App steht – und wo nicht

**[TalkSafe](/talksafe/de/) ist keine App zur Anrufaufnahme.** Auf den Anruf selbst hat sie keinen Zugriff, aus demselben Grund wie alle anderen Apps im Play Store. Sie nimmt auf, was das Mikrofon im Raum hört.

Bei einem Telefonat auf Lautsprecher sind das beide Seiten. Bei einem Gespräch von Angesicht zu Angesicht ist es das Gespräch vor Ihnen – dafür wurde sie eigentlich gebaut.

Was sie beiträgt, ist der Start. Sie beginnt, wenn sie ein **vorher festgelegtes Wort** hört, funktioniert bei **gesperrtem Bildschirm** und speichert die **30 Sekunden vor dem Start** mit. Bei einem Telefonat, das mittendrin schwierig wird, ist das genau der Teil, der sonst fehlen würde.

## Die Einwilligung gleich mit aufnehmen

Wo die Einwilligung aller nötig ist, lässt sich das Schlüsselwort dafür nutzen. Legen Sie ein Wort aus Ihrer Frage fest, zum Beispiel **„aufnehmen“**, und stellen Sie auf Lautsprecher.

Dann fragen Sie: „Darf ich das Gespräch aufnehmen?“ In dem Moment, in dem Sie fragen, beginnt die Aufnahme, und die Antwort Ihres Gegenübers ist in der Datei. Sie müssen nicht erst sichtbar auf Aufnahme drücken und danach fragen.

## Was sich nicht geändert hat

**Das Recht knüpft an das Gespräch an, nicht an das Gerät.**

Ein zweites Telefon, ein Diktiergerät oder der Lautsprecher ändert nichts daran, welche Einwilligung in Ihrem Land nötig ist. Die Sperren im Play Store sind eine Plattformrichtlinie, kein Gesetz – wer die eine erfüllt, hat damit nicht das andere erfüllt.

## Kurz gesagt

**Anrufaufnahme durch Drittanbieter-Apps ist vorbei**, in drei Schritten bis Mai 2022, und sie kommt über keine App zurück.

**Die eingebaute Telefon-App war nie verboten.** Samsung und Google bieten die Aufnahme dort an, mit einer Ansage für das Gegenüber.

**Lautsprecher plus Aufnahme-App funktioniert überall**, auf Kosten von Tonqualität und Privatsphäre.

**Und nichts davon ändert die Einwilligungsregeln** dort, wo Sie leben.

Welche Arten automatischer Aufnahme es gibt, einschließlich der Aufnahme beim Zustandekommen eines Anrufs, steht in [„Automatische Aufnahme“ heißt nicht immer dasselbe](/blog/de/auto-recording-types/). Wie man eine Aufnahme ganz ohne Hände startet, steht in [Aufnahme starten, ohne das Telefon zu berühren](/blog/de/hands-free-recording/).

Was man nach der Aufnahme mit der Datei tun sollte – und warum das Weitergeben eigene Regeln hat –, steht in [Was man mit einer Aufnahme tun sollte – und was nicht](/blog/de/after-recording/).

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">Die Angaben zu Geräten und Regionen beruhen auf Herstellerangaben und Berichten, die sich häufig ändern; prüfen Sie Ihre eigene Telefon-App. Allgemeine Information, keine Rechtsberatung – das Aufnahmerecht unterscheidet sich von Land zu Land.</p>
