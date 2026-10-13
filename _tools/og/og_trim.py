"""trim-recording 표지 이미지 (ja, es, it, de, fr, tr, pt-br, pl, nl, cs, hi).

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_trim.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_gen import render, panel_trim, TRIM_CSS

FONT = {
    'ja': "body{font-family:'Yu Gothic','Segoe UI',sans-serif;word-break:normal;line-break:strict}.title{font-size:56px}",
    'hi': "body{font-family:'Nirmala UI','Segoe UI',sans-serif}.title{font-size:52px;line-height:1.3}.sub{line-height:1.5}.eyebrow{letter-spacing:0}",
}
BASE = '.left{min-width:0}.right{min-width:0}'
LONG = '.title{font-size:50px}'
for l in ('es', 'it', 'fr', 'pt-br', 'nl'):
    FONT[l] = FONT.get(l, '') + LONG
TIME = dict(mark='1:04:10 → 1:06:10', end='1:40:00')

CARDS = {
 'ja': dict(eyebrow='Android・録音の切り取り', title='録音を切り取る、<br>原本は残して', sub='必要な2分だけ — 録音全体はそのまま。', tagline='キーワードで始まる録音アプリ',
     cap='1時間40分の録音', rows=[('原本', '触らずにそのまま'), ('切り取った区間', '新しいファイルとして保存')], chips=['切り取ったファイルにノイズ除去', 'Androidの共有メニュー']),
 'es': dict(eyebrow='ANDROID · RECORTAR', title='Recorta una grabación, conserva el original', sub='Los dos minutos que importan, y el archivo completo detrás.', tagline='GRABADORA QUE ARRANCA CON UNA PALABRA',
     cap='Grabación de 1 h 40 min', rows=[('Original', 'Intacto, donde estaba'), ('Tramo recortado', 'Guardado como archivo nuevo')], chips=['Quitar ruido del tramo', 'Menú para compartir']),
 'it': dict(eyebrow='ANDROID · TAGLIARE', title="Taglia una registrazione, tieni l'originale", sub="I due minuti che contano, e il file completo dietro.", tagline='REGISTRATORE CHE PARTE CON UNA PAROLA',
     cap='Registrazione di 1 h 40 min', rows=[('Originale', "Intatto, dov'era"), ('Tratto tagliato', 'Salvato come nuovo file')], chips=['Rimozione rumore sul tratto', 'Menu di condivisione']),
 'de': dict(eyebrow='ANDROID · AUFNAHME KÜRZEN', title='Aufnahme kürzen, Original behalten', sub='Die zwei Minuten, auf die es ankommt – und die ganze Datei dahinter.', tagline='AUFNAHME-APP MIT STARTWORT',
     cap='Aufnahme, 1 Std. 40 Min.', rows=[('Original', 'Unverändert, wo es war'), ('Geschnittener Abschnitt', 'Als neue Datei gespeichert')], chips=['Rauschentfernung am Abschnitt', 'Android-Teilen-Menü']),
 'fr': dict(eyebrow='ANDROID · COUPER', title="Couper un enregistrement, garder l'original", sub='Les deux minutes qui comptent, et le fichier complet derrière.', tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT',
     cap='Enregistrement de 1 h 40', rows=[('Original', 'Intact, là où il était'), ('Passage coupé', 'Enregistré comme nouveau fichier')], chips=['Suppression du bruit du passage', 'Menu de partage']),
 'tr': dict(eyebrow='ANDROID · KAYIT KIRPMA', title='Kaydı kırpın, orijinali saklayın', sub='Önemli olan iki dakika — ve arkasındaki tam dosya.', tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI',
     cap='1 saat 40 dakikalık kayıt', rows=[('Orijinal', 'Dokunulmadan, yerinde'), ('Kırpılan bölüm', 'Yeni dosya olarak kaydedildi')], chips=['Bölümde gürültü giderme', 'Android paylaşım menüsü']),
 'pt-br': dict(eyebrow='ANDROID · CORTAR GRAVAÇÃO', title='Corte a gravação, guarde o original', sub='Os dois minutos que importam, e o arquivo completo por trás.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA',
     cap='Gravação de 1 h 40 min', rows=[('Original', 'Intacto, onde estava'), ('Trecho cortado', 'Salvo como arquivo novo')], chips=['Remoção de ruído no trecho', 'Menu de compartilhamento']),
 'pl': dict(eyebrow='ANDROID · PRZYCINANIE', title='Przytnij nagranie, zachowaj oryginał', sub='Dwie minuty, które się liczą — i pełny plik za nimi.', tagline='DYKTAFON URUCHAMIANY SŁOWEM',
     cap='Nagranie 1 h 40 min', rows=[('Oryginał', 'Nietknięty, tam gdzie był'), ('Wycięty fragment', 'Zapisany jako nowy plik')], chips=['Usuwanie szumów z fragmentu', 'Menu udostępniania']),
 'nl': dict(eyebrow='ANDROID · OPNAME INKORTEN', title='Kort je opname in, bewaar het origineel', sub='De twee minuten die ertoe doen — en het hele bestand erachter.', tagline='OPNAME-APP DIE START OP EEN WOORD',
     cap='Opname van 1 u 40 min', rows=[('Origineel', 'Ongemoeid, waar het was'), ('Geknipt stuk', 'Opgeslagen als nieuw bestand')], chips=['Ruisverwijdering op het stuk', 'Deelmenu van Android']),
 'cs': dict(eyebrow='ANDROID · STŘIH NAHRÁVKY', title='Zkraťte nahrávku, originál si nechte', sub='Dvě minuty, na kterých záleží — a celý soubor za nimi.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO',
     cap='Nahrávka 1 h 40 min', rows=[('Originál', 'Nedotčený, kde byl'), ('Vystřižený úsek', 'Uložen jako nový soubor')], chips=['Odstranění šumu z úseku', 'Nabídka sdílení']),
 'hi': dict(eyebrow='Android · रिकॉर्डिंग ट्रिम', title='रिकॉर्डिंग ट्रिम करें, मूल फ़ाइल रखें', sub='ज़रूरी दो मिनट — और पीछे पूरी फ़ाइल।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर',
     cap='1 घंटा 40 मिनट की रिकॉर्डिंग', rows=[('मूल फ़ाइल', 'बिना छुए, वहीं'), ('ट्रिम किया हिस्सा', 'नई फ़ाइल के रूप में सेव')], chips=['हिस्से पर नॉइज़ रिमूवल', 'Android शेयर मेन्यू']),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for lang, t in CARDS.items():
        if only and lang not in only:
            continue
        render({('trim-recording', lang): dict(t, panel=panel_trim, **TIME)}, TRIM_CSS + BASE + FONT.get(lang, ''))
