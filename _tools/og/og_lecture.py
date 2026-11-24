"""강의 녹음 글(ref lecture-recording) 13개 언어 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_lecture.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, HI_CSS
from og_gen import render
from og_summary import T as SUM
from og_divorce import panel_text, TXT_CSS

C = {
 'ko': ('사용법 · 강의 녹음', '휴대폰으로 강의 녹음하는 법', '수업 전체부터 중요한 대목만 남기기까지.', '강의 · TalkSafe',
        [('수업 전체', '시작 화면 버튼', '수동 녹음'), ('중요한 대목만', '교수가 할 말을 키워드로', '지나간 30초까지'),
         ('끝난 뒤', '강의한 언어 그대로', 'AI 요약'), ('녹음 파일', '공유는 교수 허락 먼저', '내 공부용')]),
 'en': ('HOW-TO · LECTURES', 'How to record a lecture on your phone', 'The whole class, or just the parts that matter.', 'Lectures · TalkSafe',
        [('Whole class', 'start-screen button', 'manual recording'), ('Key parts only', "the lecturer's words", '+ the 30 s already gone'),
         ('Afterwards', 'in the language of the lecture', 'AI summary'), ('The file', 'ask before sharing', 'for your study')]),
 'ja': ('使い方 · 講義の録音', 'スマホで<br>講義を録音する方法', '授業まるごと、または大事なところだけ。', '講義 · TalkSafe',
        [('授業まるごと', '開始画面のボタン', '手動録音'), ('大事なところだけ', '先生の言葉をキーワードに', '過ぎた30秒まで'),
         ('終わったあと', '講義の言語のまま', 'AI要約'), ('録音ファイル', '共有は先生の許可を先に', '自分の勉強用')]),
 'es': ('GUÍA · CLASES', 'Cómo grabar clases con el celular', 'La clase entera o solo lo importante.', 'Clases · TalkSafe',
        [('Clase entera', 'botón de inicio', 'grabación manual'), ('Solo lo importante', 'palabras del profesor', '+ 30 s que ya pasaron'),
         ('Al terminar', 'en el idioma de la clase', 'resumen con IA'), ('El archivo', 'pide permiso para compartir', 'para tu estudio')]),
 'it': ('GUIDA · LEZIONI', 'Come registrare le lezioni con il telefono', 'Tutta la lezione o solo le parti importanti.', 'Lezioni · TalkSafe',
        [('Tutta la lezione', 'pulsante iniziale', 'registrazione manuale'), ('Solo l’importante', 'parole del docente', '+ 30 s già passati'),
         ('Alla fine', 'nella lingua della lezione', 'riassunto IA'), ('Il file', 'chiedi prima di condividere', 'studio personale')]),
 'de': ('ANLEITUNG · VORLESUNGEN', 'Vorlesung mit dem Handy aufnehmen', 'Die ganze Stunde oder nur das Wichtige.', 'Vorlesungen · TalkSafe',
        [('Ganze Vorlesung', 'Taste auf dem Startbildschirm', 'manuelle Aufnahme'), ('Nur das Wichtige', 'Worte der Lehrperson', '+ 30 s davor'),
         ('Danach', 'in der Vorlesungssprache', 'KI‑Zusammenfassung'), ('In Deutschland', 'vorher fragen', 'Einwilligung')]),
 'fr': ('GUIDE · COURS', 'Enregistrer un cours avec son téléphone', 'Tout le cours ou seulement l’essentiel.', 'Cours · TalkSafe',
        [('Tout le cours', 'bouton de l’écran d’accueil', 'enregistrement manuel'), ('L’essentiel', 'mots de l’enseignant', '+ 30 s déjà passées'),
         ('Après', 'dans la langue du cours', 'résumé par IA'), ('Le fichier', 'demander avant de partager', 'usage privé')]),
 'tr': ('REHBER · DERSLER', 'Dersi telefonla kaydetmek', 'Tüm ders ya da yalnızca önemli kısımlar.', 'Dersler · TalkSafe',
        [('Tüm ders', 'başlangıç ekranı düğmesi', 'manuel kayıt'), ('Yalnızca önemli', 'hocanın sözleri', '+ geçmiş 30 saniye'),
         ('Sonrasında', 'dersin dilinde', 'yapay zekâ özeti'), ('Türkiye’de', 'önce hocaya sorun', 'rıza')]),
 'pt-br': ('GUIA · AULAS', 'Como gravar aula pelo celular', 'A aula inteira ou só o que importa.', 'Aulas · TalkSafe',
        [('Aula inteira', 'botão da tela inicial', 'gravação manual'), ('Só o importante', 'palavras do professor', '+ 30 s que já passaram'),
         ('Depois', 'no idioma da aula', 'resumo com IA'), ('Brasil', 'publicar exige autorização', 'art. 46, IV')]),
 'pl': ('PORADNIK · WYKŁADY', 'Jak nagrywać wykłady telefonem', 'Cały wykład albo tylko to, co ważne.', 'Wykłady · TalkSafe',
        [('Cały wykład', 'przycisk na ekranie startowym', 'ręczne nagrywanie'), ('Tylko ważne', 'słowa wykładowcy', '+ 30 s, które minęły'),
         ('Po wykładzie', 'w języku wykładu', 'podsumowanie AI'), ('Plik', 'pytaj przed udostępnieniem', 'do nauki')]),
 'nl': ('HANDLEIDING · COLLEGES', 'Een college opnemen met je telefoon', 'Het hele college of alleen wat telt.', 'Colleges · TalkSafe',
        [('Hele college', 'knop op het startscherm', 'handmatige opname'), ('Alleen het belangrijke', 'woorden van de docent', '+ 30 s die voorbij waren'),
         ('Daarna', 'in de taal van het college', 'AI-samenvatting'), ('Het bestand', 'vraag voor je deelt', 'eigen studie')]),
 'cs': ('NÁVOD · PŘEDNÁŠKY', 'Jak nahrávat přednášky na telefon', 'Celou hodinu, nebo jen to podstatné.', 'Přednášky · TalkSafe',
        [('Celá přednáška', 'tlačítko na úvodní obrazovce', 'ruční nahrávání'), ('Jen podstatné', 'slova přednášejícího', '+ 30 s, které uběhly'),
         ('Potom', 'v jazyce přednášky', 'shrnutí od AI'), ('Soubor', 'před sdílením se zeptat', 'osobní potřeba')]),
 'hi': ('गाइड · लेक्चर', 'फ़ोन से लेक्चर कैसे रिकॉर्ड करें', 'पूरी क्लास या सिर्फ़ ज़रूरी हिस्से।', 'लेक्चर · TalkSafe',
        [('पूरी क्लास', 'स्टार्ट स्क्रीन का बटन', 'मैनुअल रिकॉर्डिंग'), ('सिर्फ़ ज़रूरी हिस्से', 'टीचर के शब्द', '+ बीते 30 सेकंड'),
         ('बाद में', 'लेक्चर की भाषा में', 'AI सारांश'), ('फ़ाइल', 'शेयर से पहले पूछें', 'अपनी पढ़ाई')]),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for lang, (eyebrow, title, sub, cap, rows) in C.items():
        if only and lang not in only:
            continue
        t = dict(eyebrow=eyebrow, title=title, sub=sub, tagline=SUM[lang][3], panel=panel_text, cap=cap, rows=rows)
        extra = HI_CSS if lang == 'hi' else ("body{font-family:'Yu Gothic','Segoe UI',sans-serif;word-break:normal;line-break:strict}" if lang == 'ja' else '')
        render({('lecture-recording', lang): t}, CSS + TXT_CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:50px}' + extra)
