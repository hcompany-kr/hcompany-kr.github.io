---
lang: es
ref: call-recording-android
categories: es
permalink: /blog/es/call-recording-android/
date: 2026-09-04
eyebrow: Cómo hacerlo
title: "Por qué dejaron de funcionar las apps para grabar llamadas en Android"
description: "Android quitó la API en 2015, cerró la vía del micrófono en 2019 y Google tapó el último atajo en mayo de 2022. El marcador que trae el teléfono nunca estuvo incluido, y por eso a unos les funciona y a otros no."
app: true
app_description: "Una grabadora de voz para Android que empieza a grabar sola cuando escucha una palabra que hayas elegido. Al iniciarse, guarda también los 30 segundos anteriores."
faq:
  - q: "¿Por qué ya no funcionan las apps para grabar llamadas en Android?"
    a: "Android 6, de 2015, eliminó la API de grabación de llamadas. Android 10, de 2019, bloqueó la grabación a través del micrófono. Los desarrolladores pasaron entonces a usar la API de accesibilidad como atajo, y el 11 de mayo de 2022 Google cerró también esa vía, señalando que esa API no fue diseñada para grabar el audio de las llamadas. Las apps de terceros fueron retiradas de Play Store."
  - q: "¿Y por qué al teléfono de otra persona sí le funciona?"
    a: "La política de 2022 se aplica a las aplicaciones de terceros, no al marcador que viene instalado en el teléfono. La grabación integrada en Google Phone, en el marcador de Samsung o en el de Xiaomi no se vio afectada y sigue funcionando donde se ofrece."
  - q: "¿En qué países y teléfonos está disponible?"
    a: "Depende del fabricante, del modelo y de la región, y va cambiando. Se documenta funcionamiento estable en mercados como India, Indonesia, Sudáfrica y partes de América Latina. Google la ofrece en Pixel 6 y posteriores en Estados Unidos, Reino Unido y otros países, y Pixel 9 y posteriores, salvo el 9a, añaden Call Notes con transcripción en Estados Unidos, Reino Unido, Canadá, Irlanda, Australia y Japón."
  - q: "¿Por qué no está disponible en algunos países?"
    a: "Por las leyes que exigen el consentimiento de todas las partes y por las políticas de las operadoras. Donde hace falta que todos los participantes acepten antes de grabar, un fabricante que incluya de serie una grabación silenciosa asume un riesgo legal en ese mercado, así que la función se desactiva o directamente no está."
  - q: "¿La grabación integrada avisa al otro?"
    a: "La aplicación Phone de Google reproduce un aviso audible de que la llamada se está grabando, y lo oyen todos los participantes. Ese aviso es el mecanismo con el que la función cumple los requisitos de consentimiento de todas las partes donde existen."
  - q: "¿Sirve poner el manos libres y grabar con otra app?"
    a: "Sí, y funciona en cualquier Android al margen de las restricciones, porque la grabadora capta el sonido de la sala y no el audio de la llamada. A cambio baja la calidad, entra ruido de fondo y quien esté cerca oye la conversación."
  - q: "¿Cambia algo legalmente si uso un aparato aparte?"
    a: "No. La ley se ocupa de la conversación, no del equipo. Usar una grabadora externa no modifica el consentimiento que exija tu jurisdicción."
---

Instalas una app para grabar llamadas. Las reseñas están llenas de gente diciendo que dejó de funcionar. Instalas otra. Lo mismo.

No es tu teléfono. **La vía que usaban esas aplicaciones se cerró por etapas a lo largo de varios años**, y la mayoría de los artículos que aparecen al buscar son anteriores al cambio.

<p class="pull">Las apps de terceros para grabar llamadas se acabaron. El marcador que trae el teléfono nunca formó parte del veto, y por eso a unos les funciona y a otros no.</p>

## Se cerró en tres pasos

**2015, Android 6.** Se eliminó la API de grabación de llamadas. Las aplicaciones dejaron de poder pedirle al sistema el audio de la llamada.

**2019, Android 10.** Se bloqueó el atajo que quedaba: grabar la llamada a través del micrófono.

**11 de mayo de 2022, la política de Play Store.** Los desarrolladores se habían pasado a la **API de accesibilidad**, que había quedado fuera de los bloqueos anteriores y era lo que mantenía vivas estas apps. Google cerró esa vía señalando que la API **no fue diseñada para grabar el audio de las llamadas**, y las aplicaciones de terceros salieron de la tienda.

Hay una segunda razón que conviene conocer. La API de accesibilidad existe para aplicaciones que asisten a personas con discapacidad, y varios desarrolladores la estaban usando para rastrear usuarios. El veto a la grabación de llamadas formó parte de cerrar esa puerta en general.

Así que una app que hoy promete grabar llamadas **o está usando el marcador del sistema, o no hace lo que crees que hace.**

## Lo que nunca se prohibió

**El marcador que venía instalado en el teléfono.**

La política de 2022 afecta a las aplicaciones de terceros. La grabación integrada en **Google Phone**, en el **marcador de Samsung** o en el de **Xiaomi** quedó intacta y sigue funcionando donde se ofrece.

Por eso desde fuera parece arbitrario. Dos personas con Android: una graba con un botón y la otra no consigue que le funcione nada.

## Dónde está disponible

Depende del fabricante, del modelo y de la región, y se mueve. Tómalo como una foto del momento, no como una regla.

Se documenta funcionamiento estable en mercados como **India, Indonesia, Sudáfrica y partes de América Latina.**

**Google** la ofrece en **Pixel 6 y posteriores** en Estados Unidos, Reino Unido y otros países. **Pixel 9 y posteriores**, salvo el 9a, añaden **Call Notes** con transcripción en Estados Unidos, Reino Unido, Canadá, Irlanda, Australia y Japón.

**Samsung** añadió la grabación de llamadas en **Estados Unidos** mediante una actualización de One UI, en los Galaxy S25, S24, S23, Z Fold y Flip 5 y 6, y algunos modelos de la serie A.

La forma más rápida de salir de dudas es abrir tu propio marcador durante una llamada y mirar si hay botón de grabar. **Si no está, ninguna app de Play Store va a ponerlo.**

## Por qué falta en algunos países

**Por las leyes de consentimiento de todas las partes y por las operadoras.**

Donde todos los participantes en una llamada tienen que aceptar antes de que se grabe, un fabricante que incluya de serie una grabación silenciosa se está creando un problema legal en ese mercado. Así que la función se desactiva o simplemente no aparece.

Fíjate en cómo resuelve Google el mismo problema donde sí existe: la aplicación Phone **reproduce un aviso audible de que la llamada se está grabando**, y lo oyen todos. Ese aviso no es cortesía. Es el mecanismo que satisface el consentimiento de todas las partes.

Cómo se trata en España y en América Latina grabar una conversación en la que participas está en [Grabar sí, difundir no](/blog/es/recording-consent-law/) y en [Grabar tu propia conversación: país por país](/blog/es/grabar-latinoamerica/).

## Lo que queda es la sala, no la línea

Si tu marcador no tiene botón de grabar, queda un método. Y funciona en cualquier Android.

**Poner la llamada en manos libres y grabar el sonido de la sala.**

Una grabadora que capta el sonido ambiente no toca el audio de la llamada, así que ninguna de las restricciones la afecta. Tu voz entra directamente y la del otro sale por el altavoz.

Los inconvenientes son reales y conviene decirlos. **Baja la calidad**, porque estás grabando un altavoz pequeño en una habitación. **Entra ruido de fondo.** Y **quien esté cerca oye la llamada**, lo que descarta el método en una oficina o en el tren.

Para una llamada que puedas atender en un sitio tranquilo, sirve.

## Qué hace esta aplicación y qué no

Aquí importa más ser exacto que convincente.

**[TalkSafe](https://hcompany-kr.github.io/talksafe/) no es una grabadora de llamadas.** No puede acceder al audio de la llamada, por el mismo motivo que no puede ninguna otra en Play Store. Lo que graba es **el sonido de la sala que llega al micrófono.**

En manos libres eso incluye las dos partes de la llamada. En persona incluye la conversación que tienes delante, **que es el caso para el que se hizo.**

Lo que aporta es el arranque. Empieza cuando oye una **palabra que has elegido**, funciona con la **pantalla bloqueada** y guarda los **30 segundos anteriores** al inicio. En una llamada que se tuerce a mitad, esa es justamente la parte que suele faltar.

Las cinco cosas distintas que pueden llamarse grabación automática están en ["Grabación automática" no significa lo mismo en todas las aplicaciones](/blog/es/auto-recording-types/).

## Lo que no ha cambiado

**La ley se ocupa de la conversación, no del equipo.**

Usar un segundo teléfono, una grabadora dedicada o el manos libres no altera el consentimiento que exija tu jurisdicción.

Las restricciones de Play Store son **una política de plataforma, no una ley.** Cumplir una no es cumplir la otra.

## En resumen

**Las apps de terceros para grabar llamadas desaparecieron**, en tres pasos que terminan en mayo de 2022, y no van a volver.

**La grabación del marcador del sistema nunca se prohibió.** Que la tengas depende de tu teléfono y de tu país.

**Manos libres más grabadora de sala funciona en todas partes**, a costa de calidad y privacidad.

**Y nada de esto cambia las reglas de consentimiento** de donde vives.

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">La disponibilidad por dispositivo y región cambia con frecuencia; comprueba tu propio marcador. Información general, no asesoramiento jurídico.</p>
