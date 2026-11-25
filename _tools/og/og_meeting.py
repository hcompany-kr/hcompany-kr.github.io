"""회의 녹음 글(ref meeting-recording) 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_meeting.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, HI_CSS
from og_gen import render
from og_summary import T as SUM
from og_divorce import panel_text, TXT_CSS

C = {
 'ko': ('사용법 · 회의 녹음', '휴대폰으로 회의 녹음하는 법', '시작 전에 나온 말부터 끝난 뒤 요약까지.', '대면 회의 · TalkSafe',
        [('시작', '진행자의 말을 키워드로', '이미 지나간 30초까지'),
         ('카페 1:1 미팅', '기기 안에서 처리', 'AI 노이즈 제거'),
         ('끝난 뒤', '녹음한 언어 그대로', 'AI 요약'),
         ('지우거나 잃어버려도', '클라우드 백업', '복구')]),
 'en': ('HOW-TO · MEETINGS', 'How to record a meeting on your phone', 'From the words before you pressed record to the summary.', 'In-person meetings · TalkSafe',
        [('Start', "the chair's words as a keyword", 'plus the 30 s already gone'),
         ('Café one-to-one', 'processed on the phone', 'AI noise removal'),
         ('Afterwards', 'in the language spoken', 'AI summary'),
         ('Deleted or lost', 'cloud backup', 'restore')]),
 'ja': ('使い方 · 会議の録音', 'スマホで<br>会議を録音する方法', '始まる前の言葉から、終わったあとの要約まで。', '対面の会議 · TalkSafe',
        [('開始', '司会の言葉をキーワードに', '過ぎた30秒まで'),
         ('カフェで1対1', 'スマホの中で処理', 'AIノイズ除去'),
         ('終わったあと', '録音した言語のまま', 'AI要約'),
         ('削除・紛失しても', 'クラウドバックアップ', '復元')]),
 'es': ('GUÍA · REUNIONES', 'Cómo grabar una reunión con el celular', 'De lo que se dijo antes de pulsar grabar al resumen.', 'Reuniones presenciales · TalkSafe',
        [('Inicio', 'las palabras de quien dirige', '+ los 30 s que ya pasaron'),
         ('A solas en un café', 'en el teléfono', 'Eliminación de ruido'),
         ('Al terminar', 'en el idioma hablado', 'Resumen con IA'),
         ('Borrada o perdida', 'copia en la nube', 'Recuperar')]),
 'it': ('GUIDA · RIUNIONI', 'Come registrare una riunione con il telefono', 'Da quello che si è detto prima di premere registra al riassunto.', 'Riunioni in presenza · TalkSafe',
        [('Inizio', 'le parole di chi conduce', '+ i 30 s già passati'),
         ('A due al bar', 'sul telefono', 'Rimozione del rumore'),
         ('Alla fine', 'nella lingua parlata', 'Riassunto IA'),
         ('Cancellata o persa', 'backup sul cloud', 'Recupero')]),
 'de': ('ANLEITUNG · BESPRECHUNGEN', 'Besprechung mit dem Handy aufnehmen', 'Von den Sätzen vor der Aufnahmetaste bis zur Zusammenfassung.', 'Besprechungen vor Ort · TalkSafe',
        [('Beginn', 'Worte der Gesprächsleitung', '+ die vergangenen 30 s'),
         ('Zu zweit im Café', 'auf dem Handy', 'KI-Rauschentfernung'),
         ('Danach', 'in der Gesprächssprache', 'KI‑Zusammenfassung'),
         ('Gelöscht oder verloren', 'Cloud-Backup', 'Wiederherstellen')]),
 'fr': ('GUIDE · RÉUNIONS', 'Enregistrer une réunion avec son téléphone', 'De ce qui a été dit avant d’appuyer sur enregistrer au résumé.', 'Réunions en présentiel · TalkSafe',
        [('Début', 'les mots de qui anime', '+ les 30 s déjà passées'),
         ('À deux au café', 'sur le téléphone', 'Suppression du bruit'),
         ('Après', 'dans la langue parlée', 'Résumé par IA'),
         ('Supprimé ou perdu', 'sauvegarde cloud', 'Restaurer')]),
 'tr': ('REHBER · TOPLANTILAR', 'Toplantı telefonla nasıl kaydedilir', 'Kayıt tuşundan önce söylenenlerden özete.', 'Yüz yüze toplantılar · TalkSafe',
        [('Başlangıç', 'toplantıyı yönetenin sözleri', '+ geçmiş 30 saniye'),
         ('Kafede iki kişi', 'telefonda işlenir', 'Gürültü giderme'),
         ('Sonrasında', 'konuşulan dilde', 'Yapay zekâ özeti'),
         ('Silinse de kaybolsa da', 'bulut yedekleme', 'Geri yükleme')]),
 'pt-br': ('GUIA · REUNIÕES', 'Como gravar uma reunião pelo celular', 'Do que foi dito antes de apertar gravar ao resumo.', 'Reuniões presenciais · TalkSafe',
        [('Início', 'as palavras de quem conduz', '+ os 30 s que já passaram'),
         ('A dois no café', 'no celular', 'Remoção de ruído'),
         ('No fim', 'no idioma falado', 'Resumo com IA'),
         ('Apagada ou perdida', 'backup na nuvem', 'Recuperar')]),
 'pl': ('PORADNIK · SPOTKANIA', 'Jak nagrać spotkanie telefonem', 'Od słów sprzed naciśnięcia nagrywania do podsumowania.', 'Spotkania na żywo · TalkSafe',
        [('Początek', 'słowa prowadzącego', '+ 30 s, które minęły'),
         ('We dwoje w kawiarni', 'w telefonie', 'Usuwanie szumów'),
         ('Po spotkaniu', 'w języku rozmowy', 'Podsumowanie AI'),
         ('Usunięte lub zgubione', 'kopia w chmurze', 'Przywracanie')]),
 'nl': ('HANDLEIDING · VERGADERINGEN', 'Een vergadering opnemen met je telefoon', 'Van wat er vóór de opnameknop werd gezegd tot de samenvatting.', 'Vergaderingen op locatie · TalkSafe',
        [('Begin', 'woorden van de voorzitter', '+ de 30 s die al voorbij waren'),
         ('Met z’n tweeën in een café', 'op de telefoon', 'Ruisonderdrukking'),
         ('Daarna', 'in de gesproken taal', 'AI-samenvatting'),
         ('Gewist of kwijt', 'cloudback-up', 'Terugzetten')]),
 'cs': ('NÁVOD · PORADY', 'Jak nahrát poradu na telefon', 'Od slov před stisknutím nahrávání po shrnutí.', 'Osobní porady · TalkSafe',
        [('Začátek', 'slova vedoucího porady', '+ 30 s, které uběhly'),
         ('Ve dvou v kavárně', 'v telefonu', 'Odstranění šumu'),
         ('Potom', 'v jazyce rozhovoru', 'Shrnutí od AI'),
         ('Smazaná nebo ztracená', 'záloha do cloudu', 'Obnovení')]),
 'hi': ('गाइड · मीटिंग', 'फ़ोन से मीटिंग कैसे रिकॉर्ड करें', 'रिकॉर्ड बटन से पहले कही गई बातों से सारांश तक।', 'आमने-सामने की मीटिंग · TalkSafe',
        [('शुरुआत', 'मीटिंग चलाने वाले के शब्द', '+ बीते 30 सेकंड'),
         ('कैफ़े में दो लोग', 'फ़ोन के अंदर', 'नॉइज़ रिमूवल'),
         ('बाद में', 'बोली गई भाषा में', 'AI सारांश'),
         ('डिलीट या खो जाए', 'क्लाउड बैकअप', 'वापस लाना')]),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for lang, (eyebrow, title, sub, cap, rows) in C.items():
        if only and lang not in only:
            continue
        t = dict(eyebrow=eyebrow, title=title, sub=sub, tagline=SUM[lang][3], panel=panel_text, cap=cap, rows=rows)
        extra = ('.val{max-width:260px}' if lang == 'de' else '') + (HI_CSS if lang == 'hi' else ("body{font-family:'Yu Gothic','Segoe UI',sans-serif;word-break:normal;line-break:strict}" if lang == 'ja' else ''))
        render({('meeting-recording', lang): t}, CSS + TXT_CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:52px}' + extra)
