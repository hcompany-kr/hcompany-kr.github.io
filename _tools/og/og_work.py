"""직업·용도 글 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_work.py [ref ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_gen import render
from og_law import panel_rules, CSS

JA = "body{font-family:'Yu Gothic','Segoe UI',sans-serif;word-break:normal;line-break:strict}.title{font-size:56px}"
HI = "body{font-family:'Nirmala UI','Segoe UI',sans-serif}.title{font-size:50px;line-height:1.3}.sub{line-height:1.5}.eyebrow{letter-spacing:0}"

CARDS = {
 ('interview-recording', 'ko'): (dict(eyebrow='직업 · 탐문과 면담', title='탐문 중에 녹음기를 꺼내면 대화가 끝납니다', sub='탐정·형사·기자·조사원을 위한 기록법.', tagline='키워드로 시작되는 녹음 앱', panel=panel_rules,
     cap='탐문 중 녹음', rows=[
       ('녹음기를 탁자에 꺼낸다', '상대가 기록용으로 말을 고른다', False),
       ('대화 중 휴대폰을 꺼내 버튼', '그 동작이 대화를 끊는다', False),
       ('상대가 꺼낼 말을 키워드로', '손대지 않고 시작 + 직전 30초', True),
       ('내가 없는 자리의 대화', '누가 해도 범죄 — 통비법 16조', False)]), '.title{font-size:54px}'),
 ('interview-recording', 'en'): (dict(eyebrow='WORK · INTERVIEWS', title='Put a recorder on the table and the interview changes', sub='For investigators, detectives, journalists and adjusters.', tagline='KEYWORD-TRIGGERED RECORDER', panel=panel_rules,
     cap='Recording an interview', rows=[
       ('Recorder on the table', 'they start speaking for the record', False),
       ('Reaching for the phone mid-talk', 'the gesture breaks the conversation', False),
       ('Their likely word as the keyword', 'hands off, plus the 30 seconds before', True),
       ("A conversation you're not in", 'off limits for everyone — § 2511(1)', False)]), '.title{font-size:50px}'),
 ('interview-recording', 'ja'): (dict(eyebrow='仕事・聞き込みと取材', title='録音機を出すと、<br>会話が変わります', sub='探偵・記者・調査員のための記録法。', tagline='キーワードで始まる録音アプリ', panel=panel_rules,
     cap='聞き込み中の録音', rows=[
       ('録音機を机に出す', '相手が記録用に言葉を選ぶ', False),
       ('会話中にスマホを出してボタン', 'その動作が会話を切る', False),
       ('相手が口にする言葉をキーワードに', '手を触れずに開始 + 直前30秒', True),
       ('自分のいない場の会話', 'このアプリの用途外', False)]), JA),
 ('interview-recording', 'es'): (dict(eyebrow='TRABAJO · ENTREVISTAS', title='Saca la grabadora y la entrevista cambia', sub='Para detectives, periodistas y peritos.', tagline='GRABADORA QUE ARRANCA CON UNA PALABRA', panel=panel_rules,
     cap='Grabar una entrevista', rows=[
       ('Grabadora sobre la mesa', 'empieza a hablar para el acta', False),
       ('Sacar el móvil a mitad de charla', 'el gesto rompe la conversación', False),
       ('Su palabra como palabra clave', 'sin tocar el móvil + 30 s antes', True),
       ('Una conversación en la que no estás', 'delito — art. 197.1 CP (España)', False)]), '.title{font-size:50px}'),
 ('interview-recording', 'it'): (dict(eyebrow='LAVORO · COLLOQUI', title="Tiri fuori il registratore e l'intervista cambia", sub='Per investigatori, giornalisti e periti.', tagline='REGISTRATORE CHE PARTE CON UNA PAROLA', panel=panel_rules,
     cap='Registrare un colloquio', rows=[
       ('Registratore sul tavolo', 'si parla per il verbale', False),
       ('Prendere il telefono a metà', 'il gesto rompe la conversazione', False),
       ('La sua parola come parola chiave', 'senza toccare il telefono + 30 s prima', True),
       ('Una conversazione in cui non sei', 'reato — artt. 615-bis, 617 c.p.', False)]), '.title{font-size:50px}'),
 ('interview-recording', 'de'): (dict(eyebrow='BERUF · BEFRAGUNGEN', title='Aufnahmegerät auf dem Tisch, und das Gespräch ändert sich', sub='In Deutschland gilt: fragen. Die Frage startet die Aufnahme.', tagline='AUFNAHME-APP MIT STARTWORT', panel=panel_rules,
     cap='Gespräch aufnehmen in DE', rows=[
       ('Gerät sichtbar auf den Tisch', 'das Gegenüber spricht fürs Protokoll', False),
       ('Ohne Einwilligung aufnehmen', 'strafbar, auch als Teilnehmer — § 201 StGB', False),
       ('„aufnehmen“ als Schlüsselwort', 'die Frage startet, das Ja ist in der Datei', True),
       ('Gespräch anderer aufnehmen', 'überall strafbar', False)]), '.title{font-size:46px}'),
 ('interview-recording', 'fr'): (dict(eyebrow='MÉTIER · ENTRETIENS', title="Un enregistreur sur la table, et l'entretien change", sub="En France, il faut demander. La question lance l'enregistrement.", tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT', panel=panel_rules,
     cap='Enregistrer un entretien en France', rows=[
       ('Appareil posé sur la table', 'on parle pour le procès-verbal', False),
       ('Enregistrer sans consentement', 'puni, même participant — art. 226-1', False),
       ('« enregistrer » comme mot-clé', 'la question lance, le oui est dedans', True),
       ("La conversation d'autrui", 'punie partout', False)]), '.title{font-size:46px}'),
 ('interview-recording', 'tr'): (dict(eyebrow='MESLEK · GÖRÜŞMELER', title='Masaya kayıt cihazı koyunca görüşme değişir', sub="Türkiye'de sormak gerekir. Soru kaydı başlatır.", tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI', panel=panel_rules,
     cap="Türkiye'de görüşme kaydı", rows=[
       ('Cihazı masaya koymak', 'karşı taraf tutanak için konuşur', False),
       ('Rızasız kayıt', 'suç, katılımcı için de — TCK 133/2', False),
       ('"kayıt" anahtar kelime', 'soru kaydı başlatır, evet dosyada', True),
       ('Başkalarının konuşması', 'suç — TCK 133/1', False)]), '.title{font-size:48px}'),
 ('interview-recording', 'pt-br'): (dict(eyebrow='TRABALHO · ENTREVISTAS', title='Gravador na mesa, e a entrevista muda', sub='Para detetives, jornalistas e reguladores.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA', panel=panel_rules,
     cap='Gravar uma entrevista', rows=[
       ('Gravador na mesa', 'começa a falar para o registro', False),
       ('Pegar o celular no meio', 'o gesto quebra a conversa', False),
       ('A palavra dele como palavra-chave', 'sem tocar no celular + 30 s antes', True),
       ('Conversa da qual você não participa', 'crime — Lei 9.296, art. 10', False)]), '.title{font-size:50px}'),
 ('interview-recording', 'pl'): (dict(eyebrow='PRACA · ROZMOWY', title='Dyktafon na stole, a rozmowa się zmienia', sub='Dla detektywów, dziennikarzy i likwidatorów.', tagline='DYKTAFON URUCHAMIANY SŁOWEM', panel=panel_rules,
     cap='Nagrywanie rozmowy', rows=[
       ('Dyktafon na stole', 'rozmówca mówi do protokołu', False),
       ('Sięganie po telefon w trakcie', 'gest przerywa rozmowę', False),
       ('Jego słowo jako słowo kluczowe', 'bez dotykania telefonu + 30 s wcześniej', True),
       ('Cudza rozmowa', 'podsłuch — art. 267 § 3 k.k.', False)]), '.title{font-size:50px}'),
 ('interview-recording', 'nl'): (dict(eyebrow='WERK · GESPREKKEN', title='Recorder op tafel, en het gesprek verandert', sub='Voor rechercheurs, journalisten en schade-experts.', tagline='OPNAME-APP DIE START OP EEN WOORD', panel=panel_rules,
     cap='Een gesprek opnemen', rows=[
       ('Recorder op tafel', 'de ander praat voor het verslag', False),
       ('Tijdens het gesprek de telefoon pakken', 'het gebaar breekt het gesprek', False),
       ('Zijn woord als trefwoord', 'telefoon niet aanraken + 30 s ervoor', True),
       ('Gesprek van anderen', 'strafbaar — art. 139a Sr', False)]), '.title{font-size:50px}'),
 ('interview-recording', 'cs'): (dict(eyebrow='PRÁCE · ROZHOVORY', title='Diktafon na stole a rozhovor se změní', sub='Pro detektivy, novináře a likvidátory.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO', panel=panel_rules,
     cap='Nahrávání rozhovoru', rows=[
       ('Diktafon na stole', 'druhá strana mluví do protokolu', False),
       ('Sáhnout po telefonu uprostřed', 'gesto naruší rozhovor', False),
       ('Jeho slovo jako klíčové slovo', 'bez sahání na telefon + 30 s předtím', True),
       ('Cizí rozhovor', 'pod žádnou výjimku nespadá', False)]), '.title{font-size:50px}'),
 ('interview-recording', 'hi'): (dict(eyebrow='काम · पूछताछ और इंटरव्यू', title='मेज़ पर रिकॉर्डर रखते ही बातचीत बदल जाती है', sub='जासूस, पत्रकार और जाँचकर्ताओं के लिए।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर', panel=panel_rules,
     cap='बातचीत रिकॉर्ड करना', rows=[
       ('रिकॉर्डर मेज़ पर', 'सामने वाला रिकॉर्ड के लिए बोलता है', False),
       ('बीच में फ़ोन निकालना', 'यह हरकत बातचीत तोड़ती है', False),
       ('उसका शब्द कीवर्ड बने', 'फ़ोन छुए बिना + पहले के 30 सेकंड', True),
       ('दूसरों का संदेश इंटरसेप्ट करना', 'अपराध — दूरसंचार अधिनियम 42', False)]), HI),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for key, (t, extra) in CARDS.items():
        if only and key[0] not in only:
            continue
        render({key: t}, CSS + '.left{min-width:0}.right{min-width:0}' + extra)
