---
lang: en
ref: call-recording-android
categories: en
permalink: /blog/en/call-recording-android/
date: 2026-09-04
eyebrow: How to
title: "Why call recording stopped working on your Android, and what still does"
description: "Android removed the API in 2015, blocked the microphone route in 2019, and Google closed the accessibility loophole in May 2022. Built-in dialers were never affected — whether yours has it depends on the phone and the country."
app: true
app_description: "An Android voice recorder that starts recording automatically when it hears a word you set in advance. When recording begins, the 30 seconds preceding it are saved with the file."
faq:
  - q: "Why do call recording apps no longer work on Android?"
    a: "Android 6, released in 2015, removed the call recording API. Android 10, released in 2019, blocked call recording through the microphone. Developers then used the Accessibility API as a workaround, and on 11 May 2022 Google closed that route as well, stating the API was not designed for remote call audio recording. Third-party call recording apps were removed from the Play Store."
  - q: "Why does my friend's phone still record calls then?"
    a: "The 2022 policy applies to third-party apps, not to the dialer that came with the phone. Built-in call recording in apps such as Google Phone, Samsung's dialer or Xiaomi's dialer was never affected and continues to work where it is offered."
  - q: "Which phones and countries have built-in call recording?"
    a: "It varies by manufacturer, model and region, and it changes. Reporting places reliable native call recording in markets including India, Indonesia, South Africa and parts of Latin America. Google has offered it on Pixel 6 and later in the US, the UK and several other countries, with Call Notes and transcription on Pixel 9 and later excluding the 9a in the US, UK, Canada, Ireland, Australia and Japan. Samsung added call recording in the US through a One UI update on the Galaxy S25, S24, S23, Z Fold and Flip 5 and 6, and selected A-series devices."
  - q: "Why is it missing in some countries?"
    a: "Two-party consent laws and carrier policies. In places where every participant must agree before a call can be recorded, shipping a silent recorder by default creates a legal problem for the manufacturer, so the feature is disabled or absent."
  - q: "Does built-in recording announce itself?"
    a: "Google's Phone app plays an audible announcement that the call is being recorded, which all parties hear. That is how the feature satisfies all-party consent requirements in jurisdictions that have them."
  - q: "Does putting the call on speakerphone and using a voice recorder work?"
    a: "Yes, and it works on any Android device regardless of the restrictions, because the recorder is capturing room audio rather than the call stream. The trade-offs are audio quality, background noise and the fact that everyone nearby can hear the call."
  - q: "Do recording laws still apply if I use a separate device?"
    a: "Yes. The law is about the conversation, not the equipment. Using an external recorder does not change what consent your jurisdiction requires."
---

You install a call recorder from the Play Store. The reviews are full of people saying it stopped working. You install another one. Same thing.

Nothing is wrong with your phone. The route those apps used has been closed for years, in stages, and most articles about it are older than the change.

<p class="pull">Third-party call recording on Android is over. Built-in dialer recording was never part of the ban, which is why some phones still do it and yours may not.</p>

## How it was closed, in three steps

**2015 — Android 6.** The call recording API was removed. Apps could no longer ask the system for the call audio.

**2019 — Android 10.** The remaining workaround, capturing the call through the microphone, was blocked.

**11 May 2022 — the Play Store policy.** Developers had moved to the **Accessibility API**, which was exempt from the earlier blocks and became the loophole that kept these apps alive. Google closed it, stating the API was **not designed for remote call audio recording**, and third-party call recording apps were removed from the Play Store.

There is a second reason worth knowing. The Accessibility API exists for apps that assist users with disabilities, and a number of developers had been using it to track people. The call recording ban was part of tightening that door generally.

So an app promising call recording today is either using the built-in dialer, or it is not doing what you think it is doing.

## What was never banned

**The dialer that came with your phone.**

The 2022 policy applies to third-party apps. Built-in call recording in **Google Phone**, **Samsung's dialer**, **Xiaomi's dialer** and others was untouched and keeps working where it is offered.

Which is why this looks so arbitrary from the outside. Two people with Android phones, one records calls with a tap and the other cannot install anything that works.

## Where it exists

This varies by manufacturer, model and region, and it moves. Treat the following as a snapshot rather than a rule.

Native call recording is reported as working reliably in markets including **India, Indonesia, South Africa and parts of Latin America.**

**Google** has offered it on **Pixel 6 and later** in the US, the UK and several other countries. **Pixel 9 and later**, excluding the 9a, add **Call Notes** with transcription, currently in the US, UK, Canada, Ireland, Australia and Japan.

**Samsung** added call recording in the **US** through a One UI update, on the **Galaxy S25, S24, S23, Z Fold and Flip 5 and 6**, and selected A-series devices.

The fastest way to know is to open your own dialer, start a call, and look for a record button. If it is not there, no app from the Play Store is going to put it there.

## Why some countries do not get it

**Two-party consent laws and carrier policies.**

Where every participant in a call must agree before it can be recorded, a manufacturer that ships a silent recorder by default is creating a legal exposure in that market. So the feature is disabled or simply absent.

Note how Google solves the same problem where the feature does exist: the Phone app **plays an audible announcement that the call is being recorded**, which everyone on the call hears. That announcement is not a courtesy. It is the mechanism that satisfies all-party consent. Which jurisdictions require what is in [Is it legal to record a conversation you're in?](/blog/en/recording-consent-law/) and [Nine states are strict. The rest of the list is an argument.](/blog/en/state-recording-consent/)

## What still works: the room, not the line

If your dialer has no record button, one method remains and it works on every Android phone.

**Put the call on speakerphone and record the room.**

A voice recorder capturing room audio is not touching the call stream at all, so none of the restrictions apply to it. It picks up your side directly and the other side out of the speaker.

The trade-offs are real and worth stating plainly. **Audio quality drops**, because you are recording a small speaker in a room rather than a clean signal. **Background noise gets in.** And **everyone nearby hears the call**, which rules the method out in an office or on a train.

For a call you can take somewhere quiet, it works.

## Where this app sits, and where it does not

Being exact here matters more than being persuasive.

**[TalkSafe](https://hcompany-kr.github.io/talksafe/) is not a call recorder.** It cannot access the call stream, for the same reason nothing else on the Play Store can. What it records is what the microphone hears in the room.

On speakerphone, that includes both sides of the call. In person, it includes the conversation in front of you — which is the case it was actually built for.

What it adds is the start. It begins when it hears a **word you set in advance**, works with the **screen locked**, and saves the **30 seconds before the start** with the file. On a call that turns difficult halfway through, that is the part that would otherwise be missing.

The five different things "automatic recording" can mean, including call-triggered recording, are laid out in [Not every "automatic" recorder means the same thing](/blog/en/auto-recording-types/).

## One thing that did not change

**Recording law is about the conversation, not the equipment.**

Using a second phone, a dedicated recorder or a speakerphone does not alter what consent your jurisdiction requires. If your state or country needs every party to agree, that requirement follows the conversation onto whatever device you use.

The Play Store restrictions are a platform policy. They are not the law, and satisfying one does not satisfy the other.

## In short

**Third-party call recording is gone**, in three steps ending in May 2022, and it is not coming back through an app.

**Built-in dialer recording was never banned.** Whether you have it depends on your phone, your model and your country.

**Speakerphone plus a room recorder still works everywhere**, at the cost of audio quality and privacy.

**And none of it changes the consent rules** where you live.

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">Device and regional availability described here reflects reporting that changes frequently; check your own dialer. General information, not legal advice — recording law differs by country and by state.</p>
