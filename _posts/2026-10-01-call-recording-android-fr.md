---
lang: fr
ref: call-recording-android
categories: fr
permalink: /blog/fr/call-recording-android/
date: 2026-10-01
eyebrow: Pratique
title: "Pourquoi les applications d'enregistrement d'appels ne marchent plus sur Android, et ce qui fonctionne encore"
description: "Android a retiré l'interface en 2015, bloqué la voie du micro en 2019, et Google a fermé la dernière brèche en mai 2022. L'application Téléphone intégrée n'a jamais été concernée. Et ce que dit la loi en France, en Belgique, en Suisse, au Luxembourg, à Monaco et au Québec."
app: true
app_description: "Une application d'enregistrement pour Android qui démarre automatiquement quand elle entend un mot choisi à l'avance. Au démarrage, elle conserve aussi les 30 secondes précédentes."
faq:
  - q: "Pourquoi les applications d'enregistrement d'appels ne fonctionnent-elles plus sur Android ?"
    a: "Android 6 a retiré en 2015 l'interface d'enregistrement des appels, et Android 10 a bloqué en 2019 l'enregistrement des appels par le micro. Les développeurs sont alors passés par l'interface d'accessibilité, et le 11 mai 2022 Google a fermé cette voie aussi. Les applications tierces d'enregistrement d'appels ont été retirées du Play Store."
  - q: "Peut-on enregistrer un appel avec l'application Téléphone en France ?"
    a: "Sur certains appareils, oui. Samsung propose l'enregistrement des appels en France depuis 2025 sur des modèles récents sous One UI 7, avec une voix qui prévient les participants que l'appel va être enregistré. Google a annoncé en septembre 2025 le déploiement de l'enregistrement des appels de l'application Téléphone sur les Pixel 6 et plus récents dans tous les pays où Pixel est proposé ; les participants y sont aussi avertis."
  - q: "Peut-on enregistrer un appel auquel on participe sans prévenir ?"
    a: "Cela dépend du pays. En France, l'article 226-1 du Code pénal le punit d'un an d'emprisonnement et de 45 000 euros d'amende, même pour un participant. En Suisse, l'article 179ter du Code pénal le punit aussi, sauf pour les commandes et réservations dans les relations d'affaires. À Monaco, l'article 308-2 du Code pénal et, au Luxembourg, l'article 2 de la loi du 11 août 1982 ne prévoient pas d'exception pour le participant. En Belgique, la Cour de cassation a jugé en 2015 qu'un participant qui enregistre ne commet pas d'infraction, et au Québec le Code criminel canadien le permet aussi."
  - q: "Mettre l'appel sur haut-parleur et utiliser un enregistreur, ça marche ?"
    a: "Oui, sur n'importe quel téléphone Android, parce que l'application enregistre alors le son de la pièce et non le flux de l'appel. Les inconvénients sont une qualité audio moindre, le bruit ambiant et le fait que tout le monde autour entend l'appel."
  - q: "TalkSafe est-elle une application d'enregistrement d'appels ?"
    a: "Non. TalkSafe est une application d'enregistrement pour Android qui enregistre ce que le micro entend dans la pièce ; elle n'a pas accès au flux de l'appel. Sur haut-parleur, elle enregistre les deux côtés. Elle démarre quand elle entend un mot choisi à l'avance, fonctionne écran verrouillé et conserve les 30 secondes qui précèdent le démarrage."
  - q: "Comment demander l'accord au téléphone sans alourdir la conversation ?"
    a: "Dans TalkSafe, choisissez comme mot-clé un mot de votre question, par exemple « enregistrer », et mettez l'appel sur haut-parleur. Quand vous demandez « Je peux enregistrer notre échange ? », l'enregistrement démarre à ce moment-là et la réponse de votre interlocuteur est dans le fichier."
  - q: "Utiliser un appareil séparé change-t-il quelque chose à la loi ?"
    a: "Non. La loi porte sur la conversation, pas sur l'appareil. Un deuxième téléphone, un dictaphone ou le haut-parleur ne change rien au consentement exigé dans votre pays."
---

Vous installez une application d'enregistrement d'appels depuis le Play Store. Les avis disent tous qu'elle ne marche plus. Vous en installez une autre. Pareil.

Votre téléphone n'a rien. La voie qu'utilisaient ces applications est fermée depuis des années, par étapes, et la plupart des articles sur le sujet datent d'avant le changement.

<p class="pull">L'enregistrement d'appels par des applications tierces, c'est fini sur Android. L'application Téléphone intégrée n'a jamais été visée, et c'est pourquoi certains téléphones le font encore et le vôtre peut-être pas.</p>

## Ce que dit la loi dans les pays francophones

Avant la technique : enregistrer son propre appel sans l'accord de l'autre est traité de façon très différente selon le pays.

| Pays | Enregistrer son propre appel sans accord | Base |
|---|---|---|
| France | Punissable, même pour un participant | Art. 226-1 Code pénal |
| Belgique | Pas une infraction pour le participant ; l'usage dans l'intention de nuire est puni | Art. 314bis Code pénal, Cassation 2015 |
| Suisse | Punissable sur plainte ; exception pour commandes et réservations dans les affaires | Art. 179ter, 179quinquies Code pénal |
| Luxembourg | Le texte ne prévoit pas d'exception pour le participant | Art. 2, loi du 11 août 1982 |
| Monaco | Le texte ne prévoit pas d'exception pour le participant | Art. 308-2 Code pénal |
| Québec | Permis pour un participant | Art. 184 Code criminel (Canada) |

En détail :

- **France :** l'article 226-1 du Code pénal punit d'**un an d'emprisonnement et de 45 000 euros d'amende** le fait d'enregistrer sans consentement des paroles prononcées à titre privé ou confidentiel, même lorsqu'on participe à la conversation. Devant le juge civil, l'assemblée plénière de la Cour de cassation a admis le 22 décembre 2023 qu'une preuve obtenue de façon déloyale peut être recevable si elle est indispensable à l'exercice d'un droit et que l'atteinte est proportionnée.
- **Belgique :** la Cour de cassation a confirmé en 2015 qu'un participant qui enregistre une communication ne commet pas d'infraction. En revanche, utiliser cet enregistrement dans une intention frauduleuse ou de nuire est puni (article 314bis du Code pénal).
- **Suisse :** l'article 179ter du Code pénal punit, sur plainte, le participant qui enregistre une conversation non publique sans le consentement des autres. L'article 179quinquies exclut l'enregistrement des appels dans les relations d'affaires qui portent sur des **commandes, mandats, réservations et opérations semblables**.
- **Luxembourg :** l'article 2 de la loi du 11 août 1982 concernant la protection de la vie privée punit de **huit jours à un an d'emprisonnement** et/ou d'une amende celui qui enregistre des paroles prononcées en privé par une personne **sans le consentement de celle-ci**. Le texte ne prévoit pas d'exception pour le participant ; nous n'avons pas trouvé de décision tranchant précisément ce cas.
- **Monaco :** l'article 308-2 du Code pénal punit de **six mois à trois ans d'emprisonnement** le fait d'enregistrer sans son consentement des paroles prononcées par une personne à titre privé ou confidentiel. Le consentement n'est présumé que lorsque l'enregistrement a lieu au cours d'une réunion, au vu et au su de la personne.
- **Québec :** le Code criminel canadien interdit d'intercepter une communication privée, sauf avec le consentement de l'une des parties. Un participant peut donc enregistrer sa propre conversation.

Les pays francophones d'Afrique ne sont pas couverts ici.

## Comment la voie a été fermée, en trois étapes

**2015 — Android 6.** L'interface d'enregistrement des appels a été retirée. Les applications ne pouvaient plus demander au système le son de l'appel.

**2019 — Android 10.** Le contournement restant, capter l'appel par le micro, a été bloqué.

**11 mai 2022 — la règle du Play Store.** Les développeurs étaient passés par l'**interface d'accessibilité**, épargnée par les blocages précédents. Google l'a fermée aussi, en indiquant que cette interface **n'est pas conçue pour enregistrer l'audio des appels**, et les applications tierces d'enregistrement d'appels ont été retirées du Play Store.

Une application qui promet aujourd'hui d'enregistrer les appels passe donc par l'application Téléphone intégrée, ou ne fait pas ce que vous croyez.

## Ce qui n'a jamais été interdit

**L'application Téléphone livrée avec votre appareil.**

La règle de 2022 vise les applications tierces. L'enregistrement intégré des fabricants n'a jamais été concerné et continue de fonctionner là où il est proposé.

C'est pour cela que tout paraît si arbitraire vu de l'extérieur : deux personnes avec un Android, l'une enregistre ses appels d'un geste, l'autre ne trouve aucune application qui marche.

## Ce que proposent les applications Téléphone

**Samsung** a ouvert l'enregistrement des appels en France en 2025, sur des modèles récents sous **One UI 7**. Quand on l'active, **une voix prévient les participants que l'appel va être enregistré**. Samsung avait d'abord livré One UI 7 sans cette fonction pour s'adapter pays par pays aux règles en vigueur.

**Google** a annoncé en septembre 2025 le déploiement de l'enregistrement des appels de l'application Téléphone sur les **Pixel 6 et plus récents** dans tous les pays où Pixel est proposé. Selon Google, **les deux côtés sont avertis** quand l'enregistrement commence.

Ce qui est disponible sur votre appareil dépend du modèle, de la version logicielle et de la région, et cela change. Le plus rapide est d'ouvrir votre application Téléphone, de lancer un appel et de chercher un bouton d'enregistrement. S'il n'y en a pas, aucune application du Play Store ne pourra l'ajouter.

## Pourquoi l'annonce n'est pas un détail

Cette annonce n'est pas une politesse. C'est le mécanisme qui permet aux fabricants de proposer la fonction là où l'accord de tous est exigé : celui qui entend l'annonce et continue de parler sait qu'il est enregistré.

Livrer par défaut un enregistreur silencieux exposerait un fabricant à un risque juridique en France. C'est pourquoi Samsung et Google y proposent la fonction avec une annonce.

## Ce qui marche toujours : la pièce, pas la ligne

Si votre application Téléphone n'a pas de bouton d'enregistrement, il reste une méthode, et elle fonctionne sur tous les Android.

**Mettez l'appel sur haut-parleur et enregistrez la pièce.**

Une application qui capte le son de la pièce ne touche pas au flux de l'appel, donc aucune des restrictions ne s'applique à elle. Elle capte votre voix directement et celle de l'autre par le haut-parleur.

Les inconvénients sont réels. **La qualité baisse**, puisqu'on enregistre un petit haut-parleur dans une pièce plutôt qu'un signal propre. **Le bruit ambiant s'invite.** Et **tout le monde autour entend l'appel**, ce qui exclut l'open space ou le train.

Des trois, le bruit ambiant est celui qu'on peut traiter après coup. La **suppression du bruit par IA** de TalkSafe retire le bruit de fond d'un enregistrement terminé et garde les voix. Le traitement se fait sur l'appareil, et la version nettoyée est enregistrée dans un nouveau fichier, l'original restant intact.

Pour un appel que vous pouvez prendre dans un endroit calme, cela marche.

## Où se situe cette application, et où elle ne se situe pas

**[TalkSafe](/talksafe/fr/) n'est pas une application d'enregistrement d'appels.** Elle n'a pas accès au flux de l'appel, pour la même raison que tout le reste du Play Store. Elle enregistre ce que le micro entend dans la pièce.

Sur haut-parleur, cela inclut les deux côtés de l'appel. En face à face, c'est la conversation devant vous — le cas pour lequel elle a vraiment été conçue.

Ce qu'elle apporte, c'est le démarrage. Elle commence quand elle entend un **mot choisi à l'avance**, fonctionne **écran verrouillé** et conserve les **30 secondes qui précèdent** le démarrage. Sur un appel qui se tend en cours de route, c'est justement la partie qui manquerait sinon.

## Enregistrer l'accord en même temps

Là où l'accord de tous est nécessaire, le mot-clé peut servir à cela. Choisissez un mot de votre question, par exemple **« enregistrer »**, et passez en haut-parleur.

Demandez alors : « Je peux enregistrer notre échange ? » L'enregistrement démarre au moment où vous posez la question, et la réponse de votre interlocuteur est dans le fichier. Inutile d'appuyer d'abord visiblement sur un bouton avant de demander.

## Ce qui n'a pas changé

**La loi porte sur la conversation, pas sur l'appareil.**

Un deuxième téléphone, un dictaphone ou le haut-parleur ne change rien au consentement exigé dans votre pays. Les restrictions du Play Store sont une règle de plateforme, pas une loi : respecter l'une ne revient pas à respecter l'autre.

## En résumé

**L'enregistrement d'appels par des applications tierces est terminé**, en trois étapes jusqu'en mai 2022, et il ne reviendra par aucune application.

**L'application Téléphone intégrée n'a jamais été interdite.** Samsung et Google y proposent l'enregistrement, avec une annonce pour l'interlocuteur.

**Haut-parleur et application d'enregistrement fonctionnent partout**, au prix de la qualité audio et de la discrétion.

**Et rien de tout cela ne change les règles de consentement** là où vous vivez.

Les cinq sens de « enregistrement automatique », y compris celui qui démarre avec un appel, sont détaillés dans [Tous les enregistreurs « automatiques » ne font pas la même chose](/blog/fr/auto-recording-types/). Les façons de démarrer sans les mains sont dans [Lancer un enregistrement sans toucher son téléphone](/blog/fr/hands-free-recording/).

Ce qu'il faut faire du fichier ensuite, et pourquoi le diffuser obéit à ses propres règles, est expliqué dans [Ce qu'il faut faire d'un enregistrement, et ce qu'il ne faut pas en faire](/blog/fr/after-recording/).

Comment retirer le bruit de la rue d'un enregistrement sur le téléphone, et quels outils y parviennent, est expliqué dans [Comment retirer le bruit de fond d'un enregistrement vocal sur Android](/blog/fr/remove-background-noise/).

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">Les informations sur les appareils et les régions reposent sur des annonces des fabricants et des articles qui changent souvent ; vérifiez votre propre application Téléphone. Information générale, pas un conseil juridique — le droit de l'enregistrement diffère d'un pays à l'autre.</p>
