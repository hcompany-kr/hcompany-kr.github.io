"""아이폰 통화 녹음 글(ref call-recording-iphone) 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_callrec.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, panel_compare, HI_CSS
from og_gen import render
from og_summary import T as SUM

# 열: 아이폰 기본 통화 녹음 / 3자 통화 방식 앱 / 스피커폰 + 다른 기기
VALS = [(True, False, True), (True, None, False), (False, None, True)]

T = {
 'ko': ('사용법 · 통화 녹음', '아이폰 통화 녹음, 상대에게 안내가 나가는 이유', 'iOS 18부터 전화 앱에 기본 탑재. EU·튀르키예 등 19곳은 미지원.', ['아이폰', '앱', '스피커'],
        [('앱 설치 없이', '기본 전화 앱'), ('상대에게 안내 음성', '녹음 시작 때, 반복'), ('EU에서도 사용', '독일·프랑스·스페인 등')]),
 'en': ('HOW-TO · CALL RECORDING', 'Record a call on iPhone, and why they hear it', 'Built into the Phone app since iOS 18. Not in the EU, Turkey and 17 others.', ['iPhone', 'App', 'Speaker'],
        [('No app needed', 'built-in Phone app'), ('Other person is told', 'audio notice, repeated'), ('Works in the EU', 'Germany, France, Spain…')]),
 'ja': ('使い方 · 通話録音', 'iPhoneの通話録音と、相手に通知が流れる理由', 'iOS 18から電話アプリに標準搭載。EU・トルコなど19か所は対象外。', ['iPhone', 'アプリ', 'スピーカー'],
        [('アプリ不要', '標準の電話アプリ'), ('相手に音声で通知', '開始時、繰り返し'), ('EUでも使える', 'ドイツ・フランスなど')]),
 'es': ('GUÍA · GRABAR LLAMADAS', 'Grabar una llamada en el iPhone', 'En la app Teléfono desde iOS 18. No en la UE (España incluida) ni en Turquía.', ['iPhone', 'App', 'Altavoz'],
        [('Sin instalar apps', 'app Teléfono'), ('Avisa al otro', 'aviso de audio, repetido'), ('Funciona en la UE', 'España, Francia…')]),
 'it': ('GUIDA · REGISTRARE CHIAMATE', 'Registrare una chiamata su iPhone', 'Nell’app Telefono da iOS 18. Non nell’UE, Italia compresa; sì in Svizzera.', ['iPhone', 'App', 'Vivavoce'],
        [('Nessuna app', 'app Telefono'), ('Avvisa l’altra persona', 'avviso sonoro, ripetuto'), ('Funziona nell’UE', 'Italia, Francia…')]),
 'de': ('ANLEITUNG · ANRUFAUFNAHME', 'Anrufe auf dem iPhone aufnehmen', 'Seit iOS 18 in der Telefon-App. Nicht in der EU, also nicht in DE und AT; in der Schweiz schon.', ['iPhone', 'App', 'Lautspr.'],
        [('Ohne zusätzliche App', 'Telefon-App'), ('Gegenüber wird informiert', 'Ansage, wiederholt'), ('In der EU verfügbar', 'Deutschland, Österreich…')]),
 'fr': ('PRATIQUE · ENREGISTRER UN APPEL', 'Enregistrer un appel sur iPhone', 'Dans l’app Téléphone depuis iOS 18. Pas dans l’UE ; oui en Suisse et au Québec.', ['iPhone', 'App', 'H.-P.'],
        [('Sans application', 'app Téléphone'), ('L’autre est prévenu', 'avertissement répété'), ('Disponible dans l’UE', 'France, Belgique…')]),
 'tr': ('NASIL YAPILIR · ARAMA KAYDI', 'iPhone’da arama kaydı', 'iOS 18’den beri Telefon uygulamasında. Türkiye’de ve AB’de yok; İsviçre’de var.', ['iPhone', 'Uygulama', 'Hoparlör'],
        [('Uygulama gerekmez', 'Telefon uygulaması'), ('Karşı taraf uyarılır', 'sesli uyarı, tekrarlı'), ('Türkiye ve AB’de', 'Almanya, Fransa…')]),
 'pt-br': ('COMO FAZER · GRAVAR LIGAÇÃO', 'Como gravar ligação no iPhone', 'No app Telefone desde o iOS 18. Funciona no Brasil, com transcrição; não em Portugal.', ['iPhone', 'App', 'Viva-voz'],
        [('Sem instalar app', 'app Telefone'), ('Avisa o outro lado', 'aviso de áudio, repetido'), ('Funciona na UE', 'Portugal, Espanha…')]),
 'pl': ('PORADNIK · NAGRYWANIE ROZMÓW', 'Nagrywanie rozmów na iPhonie', 'W aplikacji Telefon od iOS 18. Nie w UE, więc nie w Polsce; w Wielkiej Brytanii tak.', ['iPhone', 'Aplikacja', 'Głośnik'],
        [('Bez instalowania aplikacji', 'aplikacja Telefon'), ('Rozmówca jest uprzedzany', 'komunikat, powtarzany'), ('Działa w UE', 'Polska, Niemcy…')]),
 'nl': ('HANDLEIDING · GESPREKSOPNAME', 'Gesprekken opnemen op de iPhone', 'Sinds iOS 18 in de Telefoon-app. Niet in de EU, dus niet in Nederland en België.', ['iPhone', 'App', 'Luidspr.'],
        [('Geen app nodig', 'Telefoon-app'), ('De ander krijgt een melding', 'audiomelding, herhaald'), ('Werkt in de EU', 'Nederland, België…')]),
 'cs': ('NÁVOD · NAHRÁVÁNÍ HOVORŮ', 'Nahrávání hovorů na iPhonu', 'Od iOS 18 v aplikaci Telefon. Ne v EU, tedy ani v Česku a na Slovensku.', ['iPhone', 'Aplikace', 'Reprod.'],
        [('Bez další aplikace', 'aplikace Telefon'), ('Druhá strana je upozorněna', 'oznámení, opakované'), ('Funguje v EU', 'Česko, Slovensko…')]),
 'hi': ('तरीका · कॉल रिकॉर्डिंग', 'iPhone पर कॉल रिकॉर्डिंग', 'iOS 18 से फ़ोन ऐप में। भारत में उपलब्ध; यूरोपीय संघ में नहीं।', ['iPhone', 'ऐप', 'स्पीकर'],
        [('कोई ऐप नहीं चाहिए', 'फ़ोन ऐप'), ('सामने वाले को सूचना', 'ऑडियो सूचना, दोहराई'), ('यूरोपीय संघ में', 'जर्मनी, फ़्रांस…')]),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for lang, (eyebrow, title, sub, cols, rows) in T.items():
        if only and lang not in only:
            continue
        t = dict(eyebrow=eyebrow, title=title, sub=sub, tagline=SUM[lang][3], panel=panel_compare, cols=cols,
                 rows=[(a, b, v) for (a, b), v in zip(rows, VALS)])
        extra = HI_CSS if lang == 'hi' else ("body{font-family:'Yu Gothic','Segoe UI',sans-serif;word-break:normal;line-break:strict}" if lang == 'ja' else '')
        render({('call-recording-iphone', lang): t}, CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:50px}.cmp td.m{width:84px}.cmp th{font-size:15px}' + extra)
