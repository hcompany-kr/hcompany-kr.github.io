"""지운 녹음 복구 글(ref recover-deleted-recording) 13개 언어 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_recover.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, HI_CSS
from og_gen import render
from og_summary import T as SUM
from og_divorce import panel_text, TXT_CSS

C = {
 'ko': ('사용법 · 녹음 복구', '삭제된 녹음 파일 복구', '안드로이드에서 먼저 확인할 곳.', '지운 녹음은 어디로 가나',
        [('갤럭시 음성 녹음', '더보기 > 휴지통', '복원'), ('구글 녹음(픽셀)', '휴지통 없음', '공개 사본 확인'),
         ('보낸 사본', '메일·메신저·드라이브', '찾아보기'), ('TalkSafe', '직접 백업해 둔 녹음', '클라우드에서 복구')]),
 'en': ('HOW-TO · RECOVERY', 'Recover deleted voice recordings', 'Where to look first on Android.', 'Where a deleted recording goes',
        [('Samsung Voice Recorder', 'More > Recycle bin', 'Restore'), ('Google Recorder (Pixel)', 'no trash', 'check public copy'),
         ('Copies you sent', 'email, chats, cloud drive', 'look there'), ('TalkSafe', 'recordings you backed up', 'restore from cloud')]),
 'ja': ('使い方 · 録音の復元', '削除した録音を<br>復元する方法', 'Androidでまず確認する場所。', '削除した録音の行き先',
        [('Galaxyボイスレコーダー', 'その他 > ごみ箱', '復元'), ('Googleレコーダー', 'ごみ箱なし', '公開コピーを確認'),
         ('送ったコピー', 'メール・トーク・クラウド', '探す'), ('TalkSafe', '自分でバックアップした録音', 'クラウドから復元')]),
 'es': ('GUÍA · RECUPERAR', 'Recuperar grabaciones de voz borradas', 'Dónde mirar primero en Android.', 'Adónde va una grabación borrada',
        [('Grabadora de Samsung', 'Más > Papelera', 'Restaurar'), ('Grabadora de Google', 'sin papelera', 'ver copia pública'),
         ('Copias enviadas', 'correo, chats, nube', 'buscar ahí'), ('TalkSafe', 'grabaciones copiadas', 'recuperar de la nube')]),
 'it': ('GUIDA · RECUPERO', 'Recuperare registrazioni vocali cancellate', 'Dove guardare prima su Android.', 'Dove va una registrazione cancellata',
        [('Registratore Samsung', 'Altro > Cestino', 'Ripristina'), ('Registratore Google', 'nessun cestino', 'copia pubblica'),
         ('Copie inviate', 'mail, chat, cloud', 'cercale'), ('TalkSafe', 'registrazioni salvate', 'recupero dal cloud')]),
 'de': ('ANLEITUNG · WIEDERHERSTELLEN', 'Gelöschte Sprachaufnahme wiederherstellen', 'Wo man auf Android zuerst nachsieht.', 'Wohin eine gelöschte Aufnahme geht',
        [('Samsung-Sprachrekorder', 'Mehr > Papierkorb', 'Wiederherstellen'), ('Googles Rekorder', 'kein Papierkorb', 'öffentliche Kopie'),
         ('Verschickte Kopien', 'E-Mail, Chats, Cloud', 'dort suchen'), ('TalkSafe', 'selbst gesicherte Aufnahmen', 'aus der Cloud')]),
 'fr': ('GUIDE · RÉCUPÉRATION', 'Récupérer un enregistrement vocal supprimé', 'Où chercher d’abord sur Android.', 'Où va un enregistrement supprimé',
        [('Enregistreur Samsung', 'Plus > Corbeille', 'Restaurer'), ('Enregistreur Google', 'pas de corbeille', 'copie publique'),
         ('Copies envoyées', 'e-mail, messagerie, cloud', 'y chercher'), ('TalkSafe', 'enregistrements sauvegardés', 'depuis le cloud')]),
 'tr': ('REHBER · GERİ GETİRME', 'Silinen ses kaydı geri getirme', 'Android’de önce nereye bakılır.', 'Silinen kayıt nereye gider',
        [('Samsung Ses Kaydedici', 'Diğer > Çöp kutusu', 'Geri yükle'), ('Google Kaydedici', 'çöp kutusu yok', 'açık kopyaya bak'),
         ('Gönderilen kopyalar', 'e-posta, sohbet, bulut', 'oraya bak'), ('TalkSafe', 'yedeklenen kayıtlar', 'buluttan geri yükle')]),
 'pt-br': ('GUIA · RECUPERAR', 'Recuperar gravação de voz apagada', 'Onde olhar primeiro no Android.', 'Para onde vai uma gravação apagada',
        [('Gravador da Samsung', 'Mais > Lixeira', 'Restaurar'), ('Gravador do Google', 'sem lixeira', 'ver cópia pública'),
         ('Cópias enviadas', 'e-mail, conversas, nuvem', 'procurar lá'), ('TalkSafe', 'gravações salvas', 'recuperar da nuvem')]),
 'pl': ('PORADNIK · ODZYSKIWANIE', 'Jak odzyskać usunięte nagranie', 'Gdzie najpierw szukać na Androidzie.', 'Dokąd trafia usunięte nagranie',
        [('Dyktafon Samsunga', 'Więcej > Kosz', 'Przywróć'), ('Dyktafon Google', 'brak kosza', 'kopia publiczna'),
         ('Wysłane kopie', 'e-mail, czaty, chmura', 'tam szukaj'), ('TalkSafe', 'nagrania w chmurze', 'przywróć z chmury')]),
 'nl': ('HANDLEIDING · TERUGZETTEN', 'Verwijderde spraakopname terugzetten', 'Waar je op Android eerst kijkt.', 'Waar een verwijderde opname heen gaat',
        [('Samsung Spraakrecorder', 'Meer > Prullenbak', 'Terugzetten'), ('Googles Recorder', 'geen prullenbak', 'openbare kopie'),
         ('Verstuurde kopieën', 'e-mail, chats, cloud', 'daar zoeken'), ('TalkSafe', 'geback-upte opnames', 'uit de cloud')]),
 'cs': ('NÁVOD · OBNOVENÍ', 'Jak obnovit smazanou nahrávku', 'Kde na Androidu hledat nejdřív.', 'Kam jde smazaná nahrávka',
        [('Diktafon Samsung', 'Více > Koš', 'Obnovit'), ('Diktafon Google', 'bez koše', 'veřejná kopie'),
         ('Poslané kopie', 'e-mail, chaty, cloud', 'hledat tam'), ('TalkSafe', 'zálohované nahrávky', 'obnovit z cloudu')]),
 'hi': ('गाइड · रिकॉर्डिंग वापस लाना', 'डिलीट हुई रिकॉर्डिंग वापस कैसे लाएँ', 'Android पर पहले कहाँ देखें।', 'डिलीट हुई रिकॉर्डिंग कहाँ जाती है',
        [('Samsung Voice Recorder', 'More > Recycle bin', 'Restore'), ('Google Recorder', 'बिन नहीं', 'पब्लिक कॉपी देखें'),
         ('भेजी गई कॉपियाँ', 'ईमेल, चैट, क्लाउड', 'वहाँ ढूँढें'), ('TalkSafe', 'बैकअप की गई रिकॉर्डिंग', 'क्लाउड से वापस')]),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for lang, (eyebrow, title, sub, cap, rows) in C.items():
        if only and lang not in only:
            continue
        t = dict(eyebrow=eyebrow, title=title, sub=sub, tagline=SUM[lang][3], panel=panel_text, cap=cap, rows=rows)
        extra = HI_CSS if lang == 'hi' else ("body{font-family:'Yu Gothic','Segoe UI',sans-serif;word-break:normal;line-break:strict}" if lang == 'ja' else '')
        render({('recover-deleted-recording', lang): t}, CSS + TXT_CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:50px}' + extra)
