"""대금 미지급 글(ref freelance-payment) 8개 언어 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_freelance.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, panel_compare, panel_rules, HI_CSS
from og_gen import render
from og_summary import T as SUM

C = {
 'de': ('VERTRÄGE · OFFENE RECHNUNG', 'Rechnung nicht bezahlt', 'Verzugszinsen, 40 Euro Pauschale und was im ersten Gespräch vereinbart wurde.', panel_compare, ['DE', 'AT', 'CH'],
        [('Verzug ohne Mahnung', '30 Tage nach Rechnung', (True, None, False)),
         ('Pauschale 40 €', '§ 288 BGB · § 458 UGB', (True, True, False)),
         ('Verzugszins B2B', '9 · 9,2 Pkt. über Basiszins · 5 %', (True, True, True))]),
 'fr': ('CONTRATS · FACTURE IMPAYÉE', 'Facture impayée', 'Délais, pénalités, 40 € par facture et ce qui a été dit au premier rendez-vous.', panel_compare, ['FR', 'BE', 'CH'],
        [('30 jours à défaut d’accord', 'entre professionnels', (True, True, None)),
         ('Indemnité forfaitaire 40 €', 'frais de recouvrement', (True, True, False)),
         ('Intérêts de retard', 'BCE + 10 · légaux · 5 %', (True, True, True))]),
 'tr': ('SÖZLEŞMELER · ÖDENMEYEN FATURA', 'Fatura ödenmedi', 'TTK 1530: 30 gün, temerrüt faizi ve asgari giderim.', panel_rules, 'Türkiye · 2026',
        [('Faturadan 30 gün sonra temerrüt', 'sözleşmede süre yoksa', True),
         ('Ödeme süresi 60 günü aşabilir', 'kural olarak', False),
         ('Temerrüt faizi %43', 'TCMB, TTK 1530/7', True),
         ('Asgari giderim 2.020 TL', 'TCMB, TTK 1530/7', True)]),
 'pt-br': ('CONTRATOS · CLIENTE NÃO PAGOU', 'Cliente não pagou o serviço', 'Sem contrato, com prints de WhatsApp, e o que foi combinado de boca.', panel_rules, 'Brasil · Portugal',
        [('Monitória com e-mail ou WhatsApp', 'STJ, REsp 1.381.603-MS', True),
         ('Monitória só com prova oral', 'não é admitida', False),
         ('Portugal: 40 € sem interpelação', 'DL 62/2013', True),
         ('Gravar a própria conversa (Brasil)', 'STF Tema 237', True)]),
 'pl': ('UMOWY · NIEZAPŁACONA FAKTURA', 'Rekompensata 40 euro', 'Odsetki i rekompensata bez wezwania, oraz to, co ustalono ustnie.', panel_rules, 'Polska · art. 10 ustawy',
        [('Do 5000 zł', 'rekompensata', '40 €'), ('Do 50 000 zł', 'rekompensata', '70 €'), ('Od 50 000 zł', 'rekompensata', '100 €')]),
 'nl': ('CONTRACTEN · ONBETAALDE FACTUUR', 'Factuur niet betaald', 'Betalingstermijn, handelsrente, € 40 en wat er in het eerste gesprek is afgesproken.', panel_compare, ['NL', 'BE'],
        [('30 dagen zonder afspraak', 'tussen bedrijven', (True, True)),
         ('Minimaal € 40 vergoeding', 'incassokosten', (True, True)),
         ('Grootbedrijf → zzp binnen 30 dagen', 'Ondernemersplein', (True, None))]),
 'cs': ('SMLOUVY · NEUHRAZENÁ FAKTURA', 'Neuhrazená faktura', 'Splatnost 30 dnů, úrok z prodlení a 1 200 Kč.', panel_rules, 'Česko',
        [('Splatnost 30 dnů mezi podnikateli', '§ 1963 OZ', True),
         ('Úrok: repo + 8 p. b.', 'NV 351/2013 Sb.', True),
         ('Náhrada nákladů 1 200 Kč', 'NV 351/2013 Sb.', True),
         ('Promlčení 3 roky', '§ 629 OZ', True)]),
 'hi': ('अनुबंध · MSME भुगतान', 'MSME 45 दिन पेमेंट नियम', 'ब्याज, MSME समाधान और पहली मीटिंग में तय बातें।', panel_rules, 'MSMED एक्ट 2006',
        [('45 दिन के भीतर भुगतान', 'धारा 15', True),
         ('बैंक दर का तीन गुना ब्याज', 'धारा 16', True),
         ('फ़ैसिलिटेशन काउंसिल', 'धारा 18, MSME समाधान', True)]),
}

def panel_amounts(t):
    rows = ''.join(f'<div class="row"><div class="lab">{a}<small>{b}</small></div><div class="amt">{v}</div></div>' for a, b, v in t['rows'])
    return f'<div class="panel" style="padding:18px 26px"><div class="cap">{t["cap"]}</div>{rows}</div>'

AMT_CSS = '.amt{font-size:34px;font-weight:900;color:#fff;white-space:nowrap}'

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for lang, (eyebrow, title, sub, panel, cols, rows) in C.items():
        if only and lang not in only:
            continue
        if lang == 'pl':
            panel = panel_amounts
        t = dict(eyebrow=eyebrow, title=title, sub=sub, tagline=SUM[lang][3], panel=panel, rows=rows)
        if panel is panel_compare:
            t['cols'] = cols
        else:
            t['cap'] = cols
        extra = HI_CSS if lang == 'hi' else ''
        render({('freelance-payment', lang): t}, CSS + AMT_CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:52px}.cmp td.m{width:84px}' + extra)
