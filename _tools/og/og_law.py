"""나라별 녹음법 허브 글 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_law.py [ref ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_gen import render

CSS = '''.cmp{width:100%;border-collapse:collapse;font-size:19px}
.cmp th{font-size:17px;color:#cfcaff;font-weight:700;text-align:center;padding:0 0 12px}
.cmp th:first-child{text-align:left}
.cmp td{padding:12px 0;border-top:1px solid rgba(255,255,255,.14);color:#e3e0ff;line-height:1.25;vertical-align:middle}
.cmp td small{display:block;color:#bdb8ff;font-size:15px;font-weight:600;margin-top:2px}
.cmp td.m{width:78px;text-align:center}
.cmp td.m span{display:inline-flex;width:34px;height:34px;border-radius:50%;align-items:center;justify-content:center;font-weight:900;font-size:19px;background:#ff4d5a}
.cmp td.m span.ok{background:#2ecc8a}
.lab small{display:block;color:#bdb8ff;font-size:16px;font-weight:600;margin-top:2px}'''

def mark(v):
    return '<span class="ok">✓</span>' if v else '<span>✕</span>'

def panel_compare(t):
    head = '<tr><th></th>' + ''.join(f'<th>{c}</th>' for c in t['cols']) + '</tr>'
    body = ''.join(f'<tr><td>{a}<small>{b}</small></td>' + ''.join(f'<td class="m">{mark(v)}</td>' for v in vs) + '</tr>'
                   for a, b, vs in t['rows'])
    return f'<div class="panel" style="padding:22px 26px"><table class="cmp">{head}{body}</table></div>'

def panel_rules(t):
    rows = ''.join(f'<div class="row"><div class="lab">{a}<small>{b}</small></div><div class="x{" ok" if v else ""}">{"✓" if v else "✕"}</div></div>'
                   for a, b, v in t['rows'])
    return f'<div class="panel" style="padding:18px 26px"><div class="cap">{t["cap"]}</div>{rows}</div>'

CARDS = {
 ('gravar-conversa', 'pt-br'): (dict(eyebrow='LEI · GRAVAR CONVERSA', title='Gravar a própria conversa: Brasil sim, Portugal não', sub='STF, TST, Lei 9.296 e o artigo 199.º, lado a lado.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA', panel=panel_compare,
     cols=['Brasil', 'Portugal'], rows=[
       ('Gravar conversa da qual participa', 'sem o outro saber', (True, False)),
       ('Usar essa gravação como prova', 'feita sem o outro saber', (True, False)),
       ('Gravar conversa de outras pessoas', 'interceptação, escuta', (False, False)),
       ('Gravar com consentimento', 'a resposta fica no arquivo', (True, True))]),
     '.title{font-size:50px}'),
 ('recording-law-india', 'hi'): (dict(eyebrow='कानून · भारत', title='भारत में बातचीत रिकॉर्ड करना', sub='रिकॉर्डिंग आसान हिस्सा है, प्रमाणपत्र नहीं।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर', panel=panel_rules,
     cap='एक नज़र में', rows=[
       ('अपनी बातचीत रिकॉर्ड करना', 'इंटरसेप्शन नहीं — मलकानी 1973', True),
       ('बिना सहमति की रिकॉर्डिंग, सबूत में', 'अपने आप बाहर नहीं — विभोर गर्ग 2025', True),
       ('अदालत में पेश करना', 'हैश वैल्यू वाला प्रमाणपत्र — BSA 63(4)', True),
       ('दूसरों का संदेश इंटरसेप्ट करना', 'अपराध — दूरसंचार अधिनियम 42', False)]),
     "body{font-family:'Nirmala UI','Segoe UI',sans-serif}.title{font-size:52px;line-height:1.3}.sub{line-height:1.5}.eyebrow{letter-spacing:0}"),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for key, (t, extra) in CARDS.items():
        if only and key[0] not in only:
            continue
        render({key: t}, CSS + '.left{min-width:0}.right{min-width:0}' + extra)
