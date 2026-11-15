"""협의이혼 글(ref divorce-agreement) 8개 언어 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_divorce.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, panel_compare, panel_rules, HI_CSS
from og_gen import render
from og_summary import T as SUM


def panel_text(t):
    rows = ''.join(f'<div class="row"><div class="lab">{a}<small>{b}</small></div><div class="val">{v}</div></div>' for a, b, v in t['rows'])
    return f'<div class="panel" style="padding:18px 26px"><div class="cap">{t["cap"]}</div>{rows}</div>'


C = {
 'de': ('FAMILIE · SCHEIDUNG', 'Einvernehmliche Scheidung', 'Was am Küchentisch vereinbart wurde, gilt erst beim Notar oder vor Gericht.', panel_text, 'Deutschland · Österreich · Schweiz',
        [('Deutschland', '1 Jahr getrennt · § 1566 BGB', 'Notar oder gerichtlicher Vergleich'),
         ('Österreich', '½ Jahr · § 55a EheG', 'Schriftliche Vereinbarung vor Gericht'),
         ('Schweiz', 'Art. 111 ZGB', 'Gericht genehmigt die Vereinbarung')]),
 'fr': ('FAMILLE · DIVORCE', 'Divorce par consentement mutuel', 'Ce qui a été dit à la table de la cuisine ne compte que dans la convention.', panel_text, 'France · Belgique · Suisse · Québec',
        [('France', 'un avocat par époux · 15 jours', 'Convention déposée chez un notaire'),
         ('Belgique', 'art. 1287 C. jud.', 'Tribunal de la famille'),
         ('Suisse', 'art. 111 CC · 279 CPC', 'Convention ratifiée'),
         ('Québec', 'un an de séparation', 'Projet d’accord entériné')]),
 'tr': ('AİLE · BOŞANMA', 'Anlaşmalı boşanma', 'Konuşulanlar protokole yazılmadıkça geçerli değil.', panel_rules, 'Türkiye · TMK 166/3',
        [('Evlilik en az bir yıl', 'TMK 166/3', True),
         ('Hâkim eşleri bizzat dinler', 'vekilin beyanı yerine geçmez', True),
         ('Protokolü hâkim uygun bulmalı', 'mali sonuçlar ve çocuklar', True),
         ('Hâkim değişiklik yapabilir', 'taraflar kabul ederse boşanma', True)]),
 'pt-br': ('FAMÍLIA · DIVÓRCIO', 'Divórcio consensual', 'O que foi combinado só vale se entrar na escritura ou no acordo.', panel_rules, 'Brasil · Portugal',
        [('Divórcio em cartório', 'escritura pública, art. 733 CPC', True),
         ('Advogado no cartório', 'ou defensor público', True),
         ('Prazo de separação', 'EC 66/2010', False),
         ('Filhos menores no cartório', 'após decisão judicial, Res. CNJ 571/2024', True),
         ('Portugal: na conservatória', 'acordos do art. 1775.º CC', True)]),
 'pl': ('RODZINA · ROZWÓD', 'Rozwód za porozumieniem stron', 'Liczy się to, co trafi do porozumienia i wyroku.', panel_rules, 'Polska · KRO',
        [('Rozwód tylko w sądzie', 'USC zawetowany 30.04.2026', True),
         ('Bez winy na zgodne żądanie', 'art. 57 § 2', True),
         ('Porozumienie rodzicielskie', 'art. 58 § 1', True),
         ('Podział majątku w wyroku', 'art. 58 § 3', True),
         ('Opłata 600 zł', 'połowa zwracana', True)]),
 'nl': ('FAMILIE · SCHEIDING', 'Echtscheidings­convenant', 'Wat aan de keukentafel is afgesproken, telt pas als het op papier staat.', panel_compare, ['NL', 'BE'],
        [('Samen scheiden', 'gemeenschappelijk verzoek · onderlinge toestemming', (True, True)),
         ('Advocaat verplicht', 'één voor beiden kan', (True, None)),
         ('Afspraken schriftelijk', 'convenant · voorafgaande overeenkomsten', (True, True)),
         ('Ouderschapsplan verplicht', 'bij gezamenlijk gezag', (True, None))]),
 'cs': ('RODINA · ROZVOD', 'Rozvod dohodou', 'Smluvený rozvod od roku 2026: co platí a co se změnilo.', panel_rules, 'Česko · § 757 OZ',
        [('Manželství nejméně 1 rok', 'shodné tvrzení obou', True),
         ('Dohoda o dětech', 'schválená soudem', True),
         ('Majetek a bydlení', 'písemně, ověřené podpisy', True),
         ('6 měsíců odděleně', 'zrušeno od 1. 1. 2026', False),
         ('Společný návrh', 'nově od 2026', True)]),
 'hi': ('परिवार · तलाक', 'आपसी सहमति से तलाक', 'धारा 13B: एक साल, दो अर्ज़ियाँ और सेटलमेंट की शर्तें।', panel_rules, 'HMA 13B · SMA 28',
        [('1 साल अलग, संयुक्त अर्ज़ी', 'धारा 13B(1)', True),
         ('दूसरी अर्ज़ी 6–18 महीने में', 'धारा 13B(2)', True),
         ('6 महीने की छूट संभव', 'अमरदीप सिंह 2017', True),
         ('अनुच्छेद 142', 'शिल्पा शैलेश 2023', True)]),
}

TXT_CSS = '.val{font-size:19px;font-weight:700;color:#fff;text-align:right;max-width:220px;line-height:1.3}.lab small{white-space:nowrap}'

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
        render({('divorce-agreement', lang): t}, CSS + TXT_CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:52px}.cmp td.m{width:84px}' + extra)
