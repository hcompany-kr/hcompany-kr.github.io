---
lang: de
ref: remove-background-noise
categories: de
permalink: /blog/de/remove-background-noise/
date: 2026-10-09
eyebrow: Anleitung
title: "Hintergrundgeräusche aus einer Sprachaufnahme entfernen – so geht es auf Android"
description: "Verkehr, Wind, ein Café im Rücken. Vier Wege, ein aufgenommenes Gespräch zu bereinigen – auf dem Telefon beim Aufnehmen, auf dem Telefon danach, am Computer oder per Upload – und welche davon mit Straßenlärm umgehen."
app: true
app_description: "Eine Aufnahme-App für Android, die automatisch mit der Aufnahme beginnt, wenn sie ein vorher festgelegtes Wort hört. Beim Start werden auch die 30 Sekunden davor gespeichert."
faq:
  - q: "Wie entferne ich Hintergrundgeräusche aus einer Sprachaufnahme auf Android?"
    a: "Es gibt vier Wege: eine Aufnahme-App, die schon beim Aufnehmen Geräusche reduziert, etwa Clear voice in Googles Rekorder-App auf der Pixel-9-Serie; eine App, die die Datei danach auf dem Telefon bereinigt, etwa die KI-Rauschentfernung von TalkSafe; Software am Computer wie der Effekt Rauschverminderung in Audacity; oder ein Webdienst, auf den man die Datei hochlädt, etwa Adobe Podcast Enhance Speech."
  - q: "Gibt es eine Android-App, die Hintergrundgeräusche direkt auf dem Telefon aus einer Aufnahme entfernt?"
    a: "TalkSafe hat eine KI-Rauschentfernung. Auf eine fertige Aufnahme oder einen ausgeschnittenen Abschnitt angewendet, entfernt sie Hintergrundgeräusche wie Straßenlärm und lässt das Gespräch übrig. Die Verarbeitung erfolgt auf dem Gerät, und die bereinigte Fassung wird als neue Datei gespeichert, während das Original unverändert bleibt."
  - q: "Kann Audacity Verkehrslärm entfernen?"
    a: "Nicht gut. Das Handbuch von Audacity beschreibt den Effekt Rauschverminderung als geeignet für gleichmäßige Geräusche wie Rauschen oder Brummen und als nicht geeignet für unregelmäßige Hintergrundgeräusche wie Verkehr oder Publikum. Er arbeitet mit einem Rauschprofil aus einem Abschnitt ohne Sprache."
  - q: "Verändert die Rauschentfernung die Aufnahme als Beweis?"
    a: "Sie erzeugt eine andere Fassung des Tons, deshalb sollte das Original erhalten bleiben. Reichen Sie die bereinigte Fassung ein, wenn sie besser verständlich ist, behalten Sie das unveränderte Original daneben und sagen Sie dazu, dass die Kopie bereinigt wurde. Die Rauschentfernung von TalkSafe speichert eine neue Datei und lässt das Original unverändert."
  - q: "Muss ich meine Aufnahme hochladen, um die Geräusche zu entfernen?"
    a: "Nein. Webdienste wie Adobe Podcast Enhance Speech arbeiten per Upload, wodurch eine Kopie des Gesprächs an diesen Dienst geht. Werkzeuge, die auf dem Gerät arbeiten, wie die KI-Rauschentfernung von TalkSafe, verarbeiten die Datei stattdessen auf dem Telefon."
  - q: "Kann ich nur einen Teil der Aufnahme bereinigen?"
    a: "Ja. In TalkSafe schneiden Sie zuerst den benötigten Abschnitt aus – er wird als neue Datei gespeichert, das Original bleibt – und wenden dann die KI-Rauschentfernung auf diesen Abschnitt an."
---

Sie haben das Gespräch aufgenommen. Auf dem Heimweg hören Sie es an, und die Hälfte ist ein anfahrender Bus.

Die Worte sind da. Nur liegen sie unter allem anderen.

<p class="pull">Rauschentfernung ist keine Studioarbeit mehr. Wo sie läuft und was mit dem Original passiert, zählt mehr als die Taste, die Sie drücken.</p>

## Vier Wege im Vergleich

| Methode | Wann sie greift | Wohin der Ton geht | Original | Straßen- oder Verkehrslärm |
|---|---|---|---|---|
| Aufnahme-App, die beim Aufnehmen reduziert (Clear voice im Pixel-Rekorder) | Beim Aufnehmen, Pixel-9-Serie | Rekorder-App | Ein Schalter bei der Wiedergabe spielt sie ohne Reduktion ab | Für Hintergrundgeräusche allgemein gedacht |
| App, die die Datei danach bereinigt (KI-Rauschentfernung von TalkSafe) | Nach der Aufnahme, auch bei einem Ausschnitt | Auf dem Telefon verarbeitet | Bleibt; die bereinigte Fassung ist eine neue Datei | Ja, in Tests mit zwei Personen |
| Software am Computer (Rauschverminderung in Audacity) | Nach der Aufnahme | Ihr Computer | Unverändert, wenn Sie es nicht überschreiben | Laut Handbuch nicht geeignet |
| Webdienst (Adobe Podcast Enhance Speech) | Nach der Aufnahme | Hochgeladen zum Dienst | Sie laden eine bereinigte Kopie herunter | Dafür gebaut, Sprache von Geräusch zu trennen |

Der Rest dieser Seite geht durch, was jeder Weg tatsächlich verlangt.

## Beim Aufnehmen: Clear voice im Pixel-Rekorder

Google hat der Rekorder-App auf Pixel-Telefonen im Dezember 2024 eine Einstellung **Clear voice** hinzugefügt. Sie reduziert Hintergrundgeräusche während der Aufnahme, und bei der Wiedergabe lässt ein Schalter die Aufnahme ohne Reduktion hören.

Der Haken sind die Bedingungen. Berichten zufolge funktionierte sie nur mit dem **eingebauten Mikrofon der Pixel-9-Serie**, in Mono. Ein späteres Update benannte sie in **Auto Clear Voice** um.

Wenn Sie eines dieser Telefone haben und vorher wissen, dass es laut wird, ist das hier der geringste Aufwand. Mit jedem anderen Telefon ist es keine Option.

## Am Computer: Audacity

Audacity ist kostenlos, und sein Effekt **Rauschverminderung** ist der klassische Weg. Sie markieren ein paar Sekunden, in denen nur Geräusch zu hören ist, erfassen ein Rauschprofil und wenden den Effekt dann auf die ganze Aufnahme an.

Für das, wofür er gebaut ist, taugt er gut: gleichmäßige Geräusche wie Rauschen, Brummen oder eine Klimaanlage. **Das Handbuch von Audacity sagt selbst, dass er für unregelmäßige Hintergrundgeräusche wie Verkehr oder Publikum nicht geeignet ist.** Genau davon ist eine Straßenaufnahme voll.

Dazu braucht es einen Computer, eine Übertragung und etwas Geduld mit den Reglern. Übertreibt man die Einstellungen, warnt das Handbuch vor Artefakten – kurzen, zufälligen Tonfetzen.

## Per Upload: Webdienste

Werkzeuge wie **Adobe Podcast Enhance Speech** arbeiten, indem Sie Ihre Datei hochladen. Der Dienst verarbeitet sie, und Sie laden eine bereinigte Fassung herunter. Sie sind für Sprache gebaut und können beeindruckend sein.

Zwei Dinge sollte man wissen, bevor man so einen Dienst für ein echtes Gespräch nutzt. Erstens: **Hochladen heißt, dass eine Kopie des Gesprächs an diesen Dienst geht.** Für einen Podcast ist das in Ordnung. Für ein privates Gespräch mit einem anderen Menschen darin ist es eine Entscheidung, die man bewusst treffen sollte. Zweitens haben kostenlose Stufen Grenzen bei Länge und täglicher Nutzung, und die ändern sich.

## Auf dem Telefon, danach: TalkSafe

[TalkSafe](/talksafe/de/) hat eine **KI-Rauschentfernung**, die man auf eine fertige Aufnahme anwendet.

- **Sie läuft auf dem Gerät.** Zum Bereinigen wird nichts hochgeladen.
- **Das Original bleibt.** Die bereinigte Fassung wird als neue Datei daneben gespeichert.
- **Sie funktioniert bei einem Ausschnitt.** Erst die zwei Minuten ausschneiden, auf die es ankommt, dann nur diese bereinigen.

In Tests mit Zwei-Personen-Gesprächen, die auf der Straße aufgenommen wurden, verschwand der Verkehr und das Gespräch blieb.

Es ist dieselbe App, die mit der Aufnahme beginnt, wenn sie **ein vorher festgelegtes Wort** hört, bei gesperrtem Bildschirm funktioniert und **die 30 Sekunden vor dem Start** behält. Auf der Straße sorgen diese beiden Funktionen dafür, dass es die Aufnahme überhaupt gibt; die Rauschentfernung macht sie hörbar.

## Das Original immer behalten

Rauschentfernung erzeugt eine andere Fassung des Tons. Das ist ihr Zweck, und genau deshalb zählt das Original.

Wenn die Aufnahme verwendet werden könnte – in einer Beschwerde, einem Streit, einem Anspruch –, **reichen Sie die bereinigte Fassung ein, wenn sie besser verständlich ist, und behalten Sie das unveränderte Original daneben.** Sagen Sie dazu, dass die Kopie bereinigt wurde. Das Original zeigt, dass sonst nichts verändert wurde. Wie man mit den Dateien danach umgeht, steht in [Was man mit einer Aufnahme tun sollte – und was nicht](/blog/de/after-recording/). Ob die Aufnahme selbst zulässig war, ist eine eigene Frage: In Deutschland ist es nach § 201 StGB strafbar, das nichtöffentlich gesprochene Wort eines anderen unbefugt aufzunehmen, auch als Teilnehmer.

## Bevor Sie es brauchen: näher aufnehmen

Kein Werkzeug holt zurück, was das Mikrofon nie erfasst hat. Ein paar Gewohnheiten machen das Bereinigen leichter:

- **Der Abstand zählt am meisten.** Ein Telefon auf dem Tisch zwischen zwei Personen schlägt ein Telefon in der Tasche.
- **Wind ist das schwierigste Geräusch.** Ihm den Rücken zuzudrehen oder in einen Hauseingang zu treten, hilft mehr als jede Einstellung.
- **Telefonate auf Lautsprecher nehmen den Raum mit auf.** Wenn Sie ein Telefonat so aufnehmen, kann die Rauschentfernung danach die Hintergrundgeräusche herausnehmen. Warum der Lautsprecher auf Android der verbleibende Weg ist, steht in [Warum Anrufaufnahme-Apps auf Android nicht mehr funktionieren – und was noch geht](/blog/de/call-recording-android/).

## Kurz gesagt

- **Gleichmäßiges Rauschen oder Brummen, am Computer:** Audacity.
- **Ein Pixel 9 und etwas Planung:** Clear voice im Rekorder, vor dem Start eingeschaltet.
- **Studioergebnis und keine Datenschutzbedenken:** ein Webdienst, per Upload.
- **Ein Straßengespräch, das auf dem Telefon bleiben soll:** die KI-Rauschentfernung von TalkSafe, auf dem Gerät, mit erhaltenem Original.

Wie sich eigene Aufnahmegeräte und Telefone bei der Tonqualität vergleichen, steht in [Was Aufnahmegeräte unterscheidet, ist, wann sie starten](/blog/de/choosing-a-recorder/).

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">Die Angaben zu Werkzeugen anderer Anbieter beruhen auf deren Dokumentation und Berichten zum Zeitpunkt des Schreibens und können sich ändern. Wir entwickeln selbst eine Aufnahme-App, wie oben offengelegt.</p>
