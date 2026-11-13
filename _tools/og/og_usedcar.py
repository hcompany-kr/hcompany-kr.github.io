"""중고차 글(ref used-car-contract) 8개 언어 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_usedcar.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, panel_compare, panel_rules, HI_CSS
from og_gen import render
from og_summary import T as SUM

C = {
 'de': ('VERTRÄGE · GEBRAUCHTWAGEN', 'Gebrauchtwagen mit Mangel', 'Händler oder privat, „gekauft wie gesehen“ und was mündlich zugesagt wurde.', panel_compare, ['DE', 'AT', 'CH'],
        [('Händler darf Gewährleistung ausschließen', 'gegenüber Verbrauchern', (False, False, None)),
         ('Gebrauchte: auf 1 Jahr verkürzbar', '§ 476 BGB · VGG · Art. 210 OR', (True, True, True)),
         ('Privat: Ausschluss trotz Arglist', '§ 444 BGB', (False, False, False))]),
 'fr': ('CONTRATS · VOITURE D’OCCASION', 'Vice caché sur une voiture d’occasion', 'Garage ou particulier, délais, « vendu en l’état » et promesses orales.', panel_compare, ['FR', 'BE', 'CH', 'QC'],
        [('Garantie légale chez un pro', 'consommateur', (True, True, True, True)),
         ('Vices cachés entre particuliers', 'Code civil', (True, True, None, True)),
         ('« Vendu en l’état » protège le pro', 'art. 1643 et jurisprudence', (False, None, None, None))]),
 'tr': ('SÖZLEŞMELER · İKİNCİ EL ARAÇ', 'İkinci el araçta gizli ayıp', 'TBK 219–231: sorumsuzluk anlaşması, bildirim ve iki yıl.', panel_rules, 'Türkiye',
        [('Satıcı ayıptan sorumlu', 'TBK md. 219 vd.', True),
         ('Ağır kusurda sorumsuzluk anlaşması geçerli', 'TBK md. 221', False),
         ('Gizli ayıp hemen bildirilir', 'TBK md. 223', True),
         ('Rıza olmadan kaydetmek', 'TCK 133/2', False)]),
 'pt-br': ('CONTRATOS · CARRO USADO', 'Comprei carro usado com defeito', 'Loja ou particular, prazos de 90 e 30 dias, e o que foi prometido de boca.', panel_compare, ['Loja', 'Particular'],
        [('Prazo de 90 dias (CDC)', 'vício oculto conta da descoberta', (True, False)),
         ('Prazo de 30 dias (Código Civil)', 'até 180 dias da entrega', (False, True)),
         ('Gravar a própria conversa', 'STF Tema 237', (True, True))]),
 'pl': ('UMOWY · SAMOCHÓD UŻYWANY', 'Wada ukryta samochodu', 'Osoba prywatna czy handlarz, wyłączenie rękojmi i ustne zapewnienia.', panel_compare, ['Prywatnie', 'Handlarz'],
        [('Rękojmię można wyłączyć', 'art. 558 § 1 k.c.', (True, False)),
         ('Wyłączenie mimo podstępu', 'art. 558 § 2 k.c.', (False, False)),
         ('Używane: skrócenie do roku', 'art. 568 § 1 k.c.', (True, None))]),
 'nl': ('CONTRACTEN · TWEEDEHANDS AUTO', 'Verborgen gebreken aan een auto', 'Particulier of autobedrijf, bewijsvermoeden en mondelinge toezeggingen.', panel_compare, ['Autobedrijf', 'Particulier'],
        [('Bewijsvermoeden van een jaar', 'art. 7:18a lid 2 BW', (True, False)),
         ('Zware onderzoeksplicht koper', 'proefrit', (False, True)),
         ('Eigen gesprek opnemen', '139a Sr', (True, True))]),
 'cs': ('SMLOUVY · OJETÉ AUTO', 'Skrytá vada ojetého auta', 'Autobazar nebo soukromý prodejce, lhůty a ústní sliby.', panel_compare, ['Autobazar', 'Soukromě'],
        [('Vada do roka = už při převzetí', '§ 2161 odst. 5 OZ', (True, False)),
         ('Lhůta 2 roky', '§ 2165 · § 2112 OZ', (True, True)),
         ('U ojetiny zkrácení na 1 rok', '§ 2168 OZ', (True, None))]),
 'hi': ('अनुबंध · सेकंड हैंड कार', 'सेकंड हैंड कार में छिपी ख़राबी', 'डीलर या मालिक, ख़रीदार सावधान और मौखिक वादे।', panel_compare, ['डीलर', 'मालिक'],
        [('उपभोक्ता संरक्षण अधिनियम लागू', '2019', (True, False)),
         ('छिपी ख़राबी की ज़िम्मेदारी', 'धारा 16 का अपवाद', (True, None)),
         ('अपनी बातचीत रिकॉर्ड करना', 'मलकानी 1973', (True, True))]),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for lang, (eyebrow, title, sub, panel, cols, rows) in C.items():
        if only and lang not in only:
            continue
        t = dict(eyebrow=eyebrow, title=title, sub=sub, tagline=SUM[lang][3], panel=panel, rows=rows)
        if panel is panel_compare:
            t['cols'] = cols
        else:
            t['cap'] = cols
        extra = HI_CSS if lang == 'hi' else ''
        render({('used-car-contract', lang): t}, CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:50px}.cmp td.m{width:88px}' + extra)
