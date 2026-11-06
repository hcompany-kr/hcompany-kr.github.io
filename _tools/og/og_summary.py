"""AI 요약 기능 글(ref summarize-recording) 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_summary.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, panel_compare, HI_CSS
from og_gen import render

COLS = ['Pixel', 'Galaxy', 'TalkSafe']
VALS = [(True, True, True), (True, True, False), (False, False, True)]

T = {
 'ko': ('사용법 · AI 요약', '녹음 요약 AI, 안드로이드에서 쓰는 방법', '구글 녹음, 삼성 음성 녹음, TalkSafe 비교.', '키워드로 시작하는 녹음기',
        [('AI 요약', '녹음 내용 정리'), ('전체 받아쓰기', '말 그대로 옮긴 글'), ('녹음이 스스로 시작', '정해둔 말로')]),
 'en': ('HOW-TO · AI SUMMARY', 'Get an AI summary of a voice recording', 'Google Recorder, Samsung Voice Recorder and TalkSafe.', 'RECORDER THAT STARTS ON A WORD',
        [('AI summary', 'of the recording'), ('Full transcript', 'word for word'), ('Starts recording by itself', 'on a word you set')]),
 'ja': ('使い方 · AI要約', '録音をAIで要約する方法', 'Googleレコーダー、Samsung、TalkSafeを比較。', 'キーワードで始まる録音アプリ',
        [('AI要約', '録音の内容'), ('全文の文字起こし', '言葉そのまま'), ('録音が自分で始まる', '決めた言葉で')]),
 'es': ('GUÍA · RESUMEN CON IA', 'Resumir una grabación con IA en Android', 'Grabadora de Google, Samsung y TalkSafe.', 'GRABADORA QUE EMPIEZA CON UNA PALABRA',
        [('Resumen con IA', 'de la grabación'), ('Transcripción completa', 'palabra por palabra'), ('Empieza a grabar sola', 'con una palabra elegida')]),
 'it': ('GUIDA · RIASSUNTO IA', 'Riassumere una registrazione con l’IA', 'Registratore di Google, Samsung e TalkSafe.', 'REGISTRATORE CHE PARTE CON UNA PAROLA',
        [('Riassunto IA', 'della registrazione'), ('Trascrizione completa', 'parola per parola'), ('Parte da sola', 'con una parola scelta')]),
 'de': ('ANLEITUNG · KI-ZUSAMMENFASSUNG', 'Sprachaufnahme mit KI zusammenfassen', 'Google Rekorder, Samsung und TalkSafe im Vergleich.', 'AUFNAHME-APP MIT STARTWORT',
        [('KI-Zusammenfassung', 'der Aufnahme'), ('Vollständiges Transkript', 'Wort für Wort'), ('Startet von selbst', 'bei einem festgelegten Wort')]),
 'fr': ('GUIDE · RÉSUMÉ PAR IA', 'Résumer un enregistrement vocal avec l’IA', 'Enregistreur de Google, Samsung et TalkSafe.', 'ENREGISTREUR QUI DÉMARRE SUR UN MOT',
        [('Résumé par IA', 'de l’enregistrement'), ('Transcription complète', 'mot à mot'), ('Démarre tout seul', 'sur un mot choisi')]),
 'tr': ('REHBER · YAPAY ZEKÂ ÖZETİ', 'Ses kaydını yapay zekâ ile özetlemek', 'Google Kaydedici, Samsung ve TalkSafe.', 'KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI',
        [('Yapay zekâ özeti', 'kaydın içeriği'), ('Tam döküm', 'kelimesi kelimesine'), ('Kaydı kendisi başlatır', 'belirlenen kelimeyle')]),
 'pt-br': ('GUIA · RESUMO COM IA', 'Resumir um áudio gravado com IA', 'Gravador do Google, Samsung e TalkSafe.', 'GRAVADOR QUE COMEÇA COM UMA PALAVRA',
        [('Resumo com IA', 'da gravação'), ('Transcrição completa', 'palavra por palavra'), ('Começa a gravar sozinho', 'com uma palavra escolhida')]),
 'pl': ('PORADNIK · PODSUMOWANIE AI', 'Jak streścić nagranie za pomocą AI', 'Dyktafon Google, Samsung i TalkSafe.', 'DYKTAFON URUCHAMIANY SŁOWEM',
        [('Podsumowanie AI', 'treści nagrania'), ('Pełna transkrypcja', 'słowo w słowo'), ('Samo zaczyna nagrywać', 'po wybranym słowie')]),
 'nl': ('HANDLEIDING · AI-SAMENVATTING', 'Een spraakopname samenvatten met AI', 'Google Recorder, Samsung en TalkSafe.', 'OPNAME-APP DIE START OP EEN WOORD',
        [('AI-samenvatting', 'van de opname'), ('Volledige transcriptie', 'woord voor woord'), ('Start zelf met opnemen', 'op een gekozen woord')]),
 'cs': ('NÁVOD · SHRNUTÍ OD AI', 'Jak shrnout nahrávku pomocí AI', 'Diktafon Google, Samsung a TalkSafe.', 'DIKTAFON, KTERÝ SPUSTÍ SLOVO',
        [('Shrnutí od AI', 'obsahu nahrávky'), ('Úplný přepis', 'slovo od slova'), ('Spustí nahrávání sám', 'na zvolené slovo')]),
 'hi': ('गाइड · AI सारांश', 'AI से रिकॉर्डिंग का सारांश', 'Google Recorder, Samsung और TalkSafe की तुलना।', 'कीवर्ड से शुरू होने वाला रिकॉर्डर',
        [('AI सारांश', 'रिकॉर्डिंग का'), ('पूरा ट्रांसक्रिप्ट', 'शब्दशः'), ('ख़ुद रिकॉर्डिंग शुरू', 'चुने हुए शब्द पर')]),
}

if __name__ == '__main__':
    for lang, (eyebrow, title, sub, tagline, rows) in T.items():
        t = dict(eyebrow=eyebrow, title=title, sub=sub, tagline=tagline, panel=panel_compare, cols=COLS,
                 rows=[(a, b, v) for (a, b), v in zip(rows, VALS)])
        extra = HI_CSS if lang == 'hi' else ("body{font-family:'Yu Gothic','Segoe UI',sans-serif;word-break:normal;line-break:strict}" if lang == 'ja' else '')
        render({('summarize-recording', lang): t}, CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:52px}.cmp td.m{width:74px}' + extra)
