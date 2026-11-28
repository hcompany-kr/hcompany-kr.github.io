"""휴대폰을 바꿀 때 녹음 옮기기 글(ref transfer-recordings) 13개 언어 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_transfer.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, HI_CSS
from og_gen import render
from og_summary import T as SUM
from og_divorce import panel_text, TXT_CSS

C = {
 'ko': ('사용법 · 휴대폰 바꿀 때', '안드로이드↔아이폰, 녹음 파일 옮기기', '옛 휴대폰을 넘기기 전에 정해집니다.', '휴대폰 바꿀 때 · TalkSafe',
        [('넘기기 전에', '공유 메뉴로', '파일 먼저 보내기'), ('TalkSafe', '같은 구글 계정으로 로그인', '안드로이드↔아이폰 복원'),
         ('백업', '자동이 아니라', '직접 실행'), ('옛 휴대폰 초기화', '새 휴대폰에서 확인한 뒤', '마지막에')]),
 'en': ('HOW-TO · SWITCHING PHONES', 'Move voice recordings between Android and iPhone', 'It’s decided before you hand in the old phone.', 'Switching phones · TalkSafe',
        [('Before you hand it in', 'via the share menu', 'send files off first'), ('TalkSafe', 'same Google account', 'restore Android↔iPhone'),
         ('Backup', 'not automatic', 'you run it'), ('Reset the old phone', 'after checking the new one', 'last')]),
 'ja': ('使い方 · 機種変更', 'Android↔iPhone<br>録音ファイルの移し方', '古いスマホを手放す前に決まります。', '機種変更 · TalkSafe',
        [('手放す前に', '共有メニューで', '先にファイルを送る'), ('TalkSafe', '同じGoogleアカウント', 'Android↔iPhoneで復元'),
         ('バックアップ', '自動ではなく', '自分で実行'), ('古いスマホの初期化', '新しいスマホで確認後', '最後に')]),
 'es': ('GUÍA · CAMBIO DE TELÉFONO', 'Pasar grabaciones entre Android y iPhone', 'Se decide antes de entregar el teléfono viejo.', 'Cambio de teléfono · TalkSafe',
        [('Antes de entregarlo', 'menú de compartir', 'saca los archivos'), ('TalkSafe', 'misma cuenta de Google', 'restaurar Android↔iPhone'),
         ('Copia', 'no automática', 'la haces tú'), ('Restablecer el viejo', 'tras revisar el nuevo', 'al final')]),
 'it': ('GUIDA · CAMBIO TELEFONO', 'Spostare le registrazioni tra Android e iPhone', 'Si decide prima di consegnare il telefono vecchio.', 'Cambio telefono · TalkSafe',
        [('Prima di consegnarlo', 'menu di condivisione', 'fai uscire i file'), ('TalkSafe', 'stesso account Google', 'ripristino Android↔iPhone'),
         ('Backup', 'non automatico', 'lo avvii tu'), ('Ripristino del vecchio', 'dopo aver controllato il nuovo', 'per ultimo')]),
 'de': ('ANLEITUNG · HANDYWECHSEL', 'Aufnahmen zwischen Android und iPhone umziehen', 'Es entscheidet sich vor der Abgabe des alten Handys.', 'Handywechsel · TalkSafe',
        [('Vor der Abgabe', 'über das Teilen-Menü', 'Dateien zuerst sichern'), ('TalkSafe', 'gleiches Google-Konto', 'Android↔iPhone'),
         ('Backup', 'nicht automatisch', 'selbst starten'), ('Altes Handy zurücksetzen', 'nach Prüfung des neuen', 'zuletzt')]),
 'fr': ('GUIDE · CHANGER DE TÉLÉPHONE', 'Transférer ses enregistrements entre Android et iPhone', 'Tout se joue avant de rendre l’ancien téléphone.', 'Changer de téléphone · TalkSafe',
        [('Avant de le rendre', 'menu de partage', 'sortir les fichiers'), ('TalkSafe', 'même compte Google', 'Android↔iPhone'),
         ('Sauvegarde', 'pas automatique', 'à lancer soi-même'), ('Réinitialiser l’ancien', 'après vérification', 'en dernier')]),
 'tr': ('REHBER · TELEFON DEĞİŞTİRME', 'Ses kayıtlarını Android ile iPhone arasında taşımak', 'Eski telefonu teslim etmeden önce belli olur.', 'Telefon değiştirme · TalkSafe',
        [('Teslim etmeden önce', 'paylaşım menüsüyle', 'dosyaları gönderin'), ('TalkSafe', 'aynı Google hesabı', 'Android↔iPhone'),
         ('Yedekleme', 'otomatik değil', 'siz başlatırsınız'), ('Eskiyi sıfırlamak', 'yenisinde kontrol sonrası', 'en son')]),
 'pt-br': ('GUIA · TROCA DE CELULAR', 'Passar gravações entre Android e iPhone', 'Isso se decide antes de entregar o celular antigo.', 'Troca de celular · TalkSafe',
        [('Antes de entregar', 'menu de compartilhar', 'tire os arquivos'), ('TalkSafe', 'mesma conta do Google', 'restaurar Android↔iPhone'),
         ('Backup', 'não é automático', 'você faz'), ('Restaurar o antigo', 'depois de checar o novo', 'por último')]),
 'pl': ('PORADNIK · ZMIANA TELEFONU', 'Przenoszenie nagrań między Androidem a iPhone’em', 'Rozstrzyga się, zanim oddasz stary telefon.', 'Zmiana telefonu · TalkSafe',
        [('Przed oddaniem', 'menu udostępniania', 'wyślij pliki'), ('TalkSafe', 'to samo konto Google', 'Android↔iPhone'),
         ('Kopia', 'nie automatycznie', 'robisz ją sam'), ('Reset starego', 'po sprawdzeniu nowego', 'na końcu')]),
 'nl': ('HANDLEIDING · NIEUWE TELEFOON', 'Opnames overzetten tussen Android en iPhone', 'Het wordt beslist voordat je de oude inlevert.', 'Overstappen · TalkSafe',
        [('Vóór het inleveren', 'via het deelmenu', 'bestanden eerst eraf'), ('TalkSafe', 'zelfde Google-account', 'Android↔iPhone'),
         ('Back-up', 'niet automatisch', 'zelf starten'), ('Oude resetten', 'na controle op de nieuwe', 'als laatste')]),
 'cs': ('NÁVOD · VÝMĚNA TELEFONU', 'Přenos nahrávek mezi Androidem a iPhonem', 'Rozhodne se, než odevzdáte starý telefon.', 'Výměna telefonu · TalkSafe',
        [('Před odevzdáním', 'přes nabídku sdílení', 'pošlete soubory ven'), ('TalkSafe', 'stejný účet Google', 'Android↔iPhone'),
         ('Záloha', 'ne automaticky', 'spouštíte sami'), ('Reset starého', 'po kontrole v novém', 'nakonec')]),
 'hi': ('गाइड · फ़ोन बदलते समय', 'Android और iPhone के बीच रिकॉर्डिंग ले जाना', 'पुराना फ़ोन देने से पहले तय होता है।', 'फ़ोन बदलना · TalkSafe',
        [('देने से पहले', 'शेयर मेन्यू से', 'फ़ाइलें बाहर भेजें'), ('TalkSafe', 'वही Google खाता', 'Android↔iPhone'),
         ('बैकअप', 'अपने आप नहीं', 'ख़ुद करें'), ('पुराना फ़ोन रीसेट', 'नए में जाँचने के बाद', 'सबसे आख़िर में')]),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for lang, (eyebrow, title, sub, cap, rows) in C.items():
        if only and lang not in only:
            continue
        t = dict(eyebrow=eyebrow, title=title, sub=sub, tagline=SUM[lang][3], panel=panel_text, cap=cap, rows=rows)
        extra = HI_CSS if lang == 'hi' else ("body{font-family:'Yu Gothic','Segoe UI',sans-serif;word-break:normal;line-break:strict}" if lang == 'ja' else '')
        render({('transfer-recordings', lang): t}, CSS + TXT_CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:48px}' + extra)
