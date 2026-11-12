"""면접 조건 vs 계약서 글(ref job-offer-terms) 8개 언어 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_joboffer.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, panel_compare, panel_rules, HI_CSS
from og_gen import render
from og_summary import T as SUM

C = {
 'de': ('ARBEIT · VORSTELLUNGSGESPRÄCH', 'Arbeitsvertrag anders als besprochen', 'Nachweisgesetz, Dienstzettel, Art. 330b OR – und wer die Zusage beweisen muss.', panel_compare, ['DE', 'AT', 'CH'],
        [('Schriftliche Bedingungen Pflicht', 'NachwG · AVRAG · OR 330b', (True, True, True)),
         ('Mündliche Zusage wirksam', 'Beweis beim Arbeitnehmer', (True, True, True)),
         ('Eigenes Gespräch heimlich aufnehmen', '§ 201 · § 120 · Art. 179ter', (False, True, False))]),
 'fr': ('TRAVAIL · ENTRETIEN', 'Le contrat ne reprend pas la promesse', 'Offre ou promesse d’embauche, informations écrites, preuve de l’oral.', panel_compare, ['FR', 'BE', 'CH', 'QC'],
        [('Information écrite obligatoire', 'R1221-34 · loi 2022 · CO 330b', (True, True, True, False)),
         ('Promesse verbale valable', 'preuve à la charge du salarié', (True, True, True, True)),
         ('Enregistrer sans accord', 'participant', (False, True, False, True))]),
 'tr': ('İŞ HAYATI · MÜLAKAT', 'İş sözleşmesi mülakattan farklıysa', 'İş Kanunu md. 8, ispat ve ses kaydı.', panel_rules, 'Türkiye',
        [('Sözlü iş sözleşmesi geçerli', 'İş K. md. 8', True),
         ('Yazılı sözleşme yoksa 2 ay içinde belge', 'İş K. md. 8', True),
         ('Bir yıl ve üzeri sözleşme yazılı', 'İş K. md. 8', True),
         ('Rıza olmadan kaydetmek', 'TCK 133/2', False)]),
 'pt-br': ('TRABALHO · ENTREVISTA', 'Contrato diferente do combinado', 'CLT, CTPS em 5 dias úteis, promessa frustrada e Código do Trabalho.', panel_compare, ['Brasil', 'Portugal'],
        [('Prazo para registro/informação', 'CTPS 5 dias úteis · CT 7 dias', (True, True)),
         ('Promessa frustrada indenizável', 'boa-fé pré-contratual', (True, None)),
         ('Gravar a própria conversa sem avisar', 'STF Tema 237 · CP 199.º', (True, False))]),
 'pl': ('PRACA · ROZMOWA KWALIFIKACYJNA', 'Umowa inna niż ustalenia', 'Art. 29 i 281 Kodeksu pracy oraz dowód ustnych obietnic.', panel_rules, 'Polska',
        [('Potwierdzenie na piśmie przed pracą', 'art. 29 § 2 k.p.', True),
         ('Informacja o warunkach w 7 i 30 dni', 'art. 29 § 3 k.p.', True),
         ('Grzywna 1000–30 000 zł', 'art. 281 k.p.', True),
         ('Nagranie własnej rozmowy', 'co do zasady dozwolone', True)]),
 'nl': ('WERK · SOLLICITATIE', 'Contract anders dan afgesproken', 'Art. 7:655 BW, de Belgische wet van 2022 en het bewijs van een toezegging.', panel_compare, ['NL', 'BE'],
        [('Schriftelijke informatie verplicht', '7:655 BW · wet 2022', (True, True)),
         ('Mondelinge afspraak geldig', 'bewijs bij werknemer', (True, True)),
         ('Eigen gesprek opnemen', '139a Sr · Cassatie 2015', (True, True))]),
 'cs': ('PRÁCE · POHOVOR', 'Smlouva jinak než na pohovoru', '§ 34 a § 37 zákoníku práce a důkaz ústního příslibu.', panel_compare, ['CZ', 'SK'],
        [('Písemná pracovní smlouva', '§ 34 ZP · § 42 ZP', (True, True)),
         ('Informace do 7 dnů', '§ 37 ZP', (True, None)),
         ('Nahrávka bez souhlasu', '§ 88 OZ · § 12 OZ', (None, False))]),
 'hi': ('काम · इंटरव्यू', 'इंटरव्यू की सैलरी और लेटर अलग', 'अपॉइंटमेंट लेटर, मौखिक वादा और रिकॉर्डिंग।', panel_rules, 'भारत',
        [('अपॉइंटमेंट लेटर अनिवार्य', 'OSH कोड, 21.11.2025 से', True),
         ('मौखिक वादा भी अनुबंध', 'अनुबंध अधिनियम, धारा 10', True),
         ('अपनी बातचीत रिकॉर्ड करना', 'मलकानी 1973', True)]),
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
        render({('job-offer-terms', lang): t}, CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:50px}.cmp td.m{width:70px}' + extra)
