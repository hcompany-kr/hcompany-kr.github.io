---
lang: pt-BR
ref: call-recording-android
categories: pt-br
permalink: /blog/pt-br/call-recording-android/
date: 2026-10-01
eyebrow: Como fazer
title: "Por que os apps de gravar ligação pararam de funcionar no Android, e o que ainda funciona"
description: "O Android removeu a interface em 2015, bloqueou o caminho pelo microfone em 2019, e o Google fechou a última brecha em maio de 2022. O app de Telefone que vem no celular nunca foi afetado. E o que diz a lei no Brasil e em Portugal."
app: true
app_description: "Um app de gravação de voz para Android que começa a gravar sozinho quando ouve uma palavra escolhida por você. Ao começar, também salva os 30 segundos anteriores."
faq:
  - q: "Por que os apps de gravar ligação não funcionam mais no Android?"
    a: "O Android 6 removeu em 2015 a interface de gravação de chamadas, e o Android 10 bloqueou em 2019 a gravação de ligações pelo microfone. Os desenvolvedores passaram então a usar a interface de acessibilidade, e em 11 de maio de 2022 o Google fechou esse caminho também. Os apps de terceiros para gravar ligações foram removidos da Play Store."
  - q: "Dá para gravar ligação com o app de Telefone do Samsung no Brasil?"
    a: "Em muitos modelos, sim. Nos Galaxy vendidos no Brasil, a gravação de chamadas fica no app Telefone, em Configurações, na opção Gravar chamadas, com a possibilidade de gravar automaticamente todas as ligações ou só algumas. A Samsung ativa ou desativa o recurso conforme o país e a operadora, então ele pode não aparecer em todos os aparelhos."
  - q: "No Brasil é crime gravar uma ligação da qual eu participo?"
    a: "Não. O STF fixou no Tema 237 (RE 583.937) que é lícita a prova consistente em gravação ambiental realizada por um dos interlocutores sem o conhecimento do outro, e trata da mesma forma a gravação de uma ligação por quem participa dela, que não se confunde com interceptação. Ao tratar da captação ambiental, a Lei 9.296/1996 diz no art. 10-A, § 1º, que não há crime se a captação é realizada por um dos interlocutores. Crime é a interceptação feita por terceiro sem autorização judicial."
  - q: "E em Portugal, posso gravar uma chamada sem avisar?"
    a: "Não. O artigo 199.º do Código Penal pune quem, sem consentimento, grava palavras de outra pessoa não destinadas ao público, mesmo que lhe sejam dirigidas, com prisão até 1 ano ou multa até 240 dias. Os tribunais da Relação já admitiram que uma causa de justificação afaste o crime, por exemplo quando a gravação feita pela vítima registra o crime de que ela está sendo alvo."
  - q: "Colocar a ligação no viva-voz e gravar com um app funciona?"
    a: "Sim, em qualquer Android, porque o app grava o som do ambiente e não a ligação em si. O preço é a qualidade de áudio mais baixa, o barulho em volta e o fato de que todo mundo por perto escuta a conversa."
  - q: "O TalkSafe é um app de gravar ligação?"
    a: "Não. O TalkSafe é um app de gravação de voz para Android que grava o que o microfone ouve no ambiente; ele não tem acesso à ligação em si. Com a ligação no viva-voz, grava os dois lados. Ele começa quando ouve uma palavra escolhida por você, funciona com a tela bloqueada e salva os 30 segundos anteriores ao início."
  - q: "Usar outro aparelho para gravar muda alguma coisa na lei?"
    a: "Não. A lei trata da conversa, não do aparelho. Um segundo celular, um gravador ou o viva-voz não mudam o consentimento exigido onde você está."
---

Você instala um app de gravar ligação da Play Store. Nas avaliações, todo mundo diz que parou de funcionar. Você instala outro. A mesma coisa.

Não tem nada de errado com o seu celular. O caminho que esses apps usavam foi fechado há anos, em etapas, e a maioria dos textos sobre o assunto é mais antiga que a mudança.

<p class="pull">Gravar ligação com app de terceiros acabou no Android. O app de Telefone que vem no celular nunca entrou na proibição, e é por isso que alguns celulares ainda gravam e o seu talvez não.</p>

## O que diz a lei no Brasil e em Portugal

Antes da parte técnica: gravar a própria ligação sem avisar o outro lado é tratado de forma oposta nos dois países.

| País | Gravar a própria ligação sem avisar | Base |
|---|---|---|
| Brasil | Permitido para quem participa da conversa | STF Tema 237 |
| Portugal | Crime, mesmo para quem participa | Art. 199.º do Código Penal |

Em detalhe:

- **Brasil:** o STF fixou em 2009, no Tema 237 de repercussão geral (RE 583.937), que **é lícita a prova consistente em gravação ambiental realizada por um dos interlocutores sem o conhecimento do outro**, e o tribunal trata da mesma forma a gravação de uma ligação por quem participa dela: isso não se confunde com interceptação. Ao tratar da captação ambiental, a Lei 9.296/1996, no art. 10-A incluído pelo Pacote Anticrime (Lei 13.964/2019), diz expressamente que **não há crime se a captação é realizada por um dos interlocutores**. O que a lei pune é a **interceptação**: um terceiro gravar a ligação dos outros sem autorização judicial.
- **Portugal:** o artigo 199.º do Código Penal pune quem, sem consentimento, grava palavras de outra pessoa não destinadas ao público, **mesmo que lhe sejam dirigidas**, com pena de prisão até 1 ano ou multa até 240 dias. Os tribunais da Relação já admitiram que uma causa de justificação afaste o crime, por exemplo quando a gravação feita pela vítima registra o próprio crime de que ela está sendo alvo.

Os outros países de língua portuguesa não foram pesquisados aqui.

## Como o caminho foi fechado, em três etapas

**2015 — Android 6.** A interface de gravação de chamadas foi removida. Os apps não conseguiam mais pedir ao sistema o áudio da ligação.

**2019 — Android 10.** O desvio que sobrava, gravar a ligação pelo microfone, foi bloqueado.

**11 de maio de 2022 — a política da Play Store.** Os desenvolvedores tinham passado para a **interface de acessibilidade** (Accessibility API), que escapava dos bloqueios anteriores. O Google fechou esse caminho também, dizendo que a interface **não foi feita para gravar o áudio de ligações**, e os apps de terceiros para gravar ligações foram removidos da Play Store.

Ou seja, um app que hoje promete gravar ligação ou está usando o app de Telefone do próprio celular, ou não está fazendo o que você pensa.

## O que nunca foi proibido

**O app de Telefone que veio com o seu celular.**

A política de 2022 vale para apps de terceiros. A gravação embutida dos fabricantes nunca foi afetada e continua funcionando onde é oferecida.

Por isso, de fora, tudo parece tão arbitrário: duas pessoas com Android, uma grava a ligação com um toque e a outra não acha nenhum app que funcione.

## O que o app de Telefone oferece

**Samsung:** nos Galaxy vendidos no Brasil, a gravação fica no app **Telefone**, em **Configurações > Gravar chamadas**. Dá para ativar a gravação automática e escolher entre todas as ligações, só números não salvos ou números específicos. A Samsung ativa ou desativa o recurso conforme o país e a operadora, então ele pode não aparecer em todos os aparelhos.

**Google:** em setembro de 2025, o Google anunciou a gravação de chamadas no app Telefone para **Pixel 6 e mais novos** em todos os países onde o Pixel é oferecido. Segundo o Google, **os dois lados são avisados** quando a gravação começa.

O que está disponível no seu aparelho depende do modelo, da versão do software e da região, e muda. O jeito mais rápido de saber é abrir o app de Telefone, começar uma ligação e procurar um botão de gravar. Se ele não estiver lá, nenhum app da Play Store vai conseguir colocá-lo.

## O que sempre funciona: o ambiente, não a linha

Se o seu app de Telefone não tem botão de gravar, sobra um caminho, e ele funciona em qualquer Android.

**Coloque a ligação no viva-voz e grave o ambiente.**

Um app que grava o som do ambiente não toca na ligação em si, então nenhuma das restrições vale para ele. Ele pega a sua voz diretamente e a do outro lado pelo alto-falante.

O preço é real. **A qualidade cai**, porque você está gravando um alto-falante pequeno numa sala, e não um sinal limpo. **O barulho em volta entra.** E **todo mundo por perto escuta a ligação**, o que descarta o escritório aberto ou o ônibus.

Para uma ligação que você pode atender num lugar quieto, funciona.

## Onde este app se encaixa, e onde não

**O [TalkSafe](/talksafe/pt-br/) não é um app de gravar ligação.** Ele não tem acesso à ligação em si, pelo mesmo motivo que nenhum outro app da Play Store tem. Ele grava o que o microfone ouve no ambiente.

Com a ligação no viva-voz, isso inclui os dois lados. Pessoalmente, é a conversa na sua frente — o caso para o qual ele foi feito de verdade.

O que ele acrescenta é o começo. Ele começa quando ouve uma **palavra escolhida por você**, funciona com a **tela bloqueada** e salva os **30 segundos anteriores** ao início. Numa ligação que fica tensa no meio, é justamente a parte que faltaria.

## Gravar o consentimento junto

Em Portugal, onde gravar sem consentimento é crime, ou sempre que você preferir pedir, a palavra-chave serve para isso. Escolha uma palavra da sua pergunta, como **"gravar"**, e coloque no viva-voz.

Depois pergunte: "Posso gravar a nossa conversa?" A gravação começa no momento em que você pergunta, e a resposta do outro lado fica no arquivo. Não é preciso apertar um botão à vista antes de perguntar.

## O que não mudou

**A lei trata da conversa, não do aparelho.**

Um segundo celular, um gravador ou o viva-voz não mudam o consentimento exigido onde você está. As restrições da Play Store são uma política de plataforma, não uma lei; cumprir uma não significa cumprir a outra.

## Resumindo

**Gravar ligação com app de terceiros acabou**, em três etapas até maio de 2022, e não volta por meio de nenhum app.

**O app de Telefone do celular nunca foi proibido.** Nos Galaxy vendidos no Brasil, a gravação costuma estar lá.

**Viva-voz mais um app de gravação funciona em qualquer lugar**, ao custo da qualidade e da privacidade.

**E nada disso muda as regras de consentimento** de onde você está.

Os cinco significados de "gravação automática", incluindo a que começa quando uma ligação é conectada, estão em [Nem todo gravador “automático” faz a mesma coisa](/blog/pt-br/auto-recording-types/). Os jeitos de começar sem as mãos estão em [Como começar a gravar sem tocar no celular](/blog/pt-br/hands-free-recording/).

O que fazer com o arquivo depois, e por que divulgar tem regras próprias, está em [O que fazer com uma gravação, e o que não fazer](/blog/pt-br/after-recording/).

<p style="font-size:0.8125rem;color:#8A8F9E;margin-top:2rem;">As informações sobre aparelhos e regiões se baseiam em anúncios dos fabricantes e em reportagens que mudam com frequência; confira o seu próprio app de Telefone. Informação geral, não é aconselhamento jurídico — a lei sobre gravação muda de país para país.</p>
