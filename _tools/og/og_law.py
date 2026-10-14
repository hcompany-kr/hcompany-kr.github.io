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
 ('gespraech-aufnehmen', 'de'): (dict(eyebrow='RECHT · GESPRÄCH AUFNEHMEN', title='Eigenes Gespräch aufnehmen: wo es strafbar ist', sub='§ 201 StGB, § 120 StGB, Art. 179ter StGB – nebeneinander.', tagline='AUFNAHME-APP MIT STARTWORT', panel=panel_compare,
     cols=['DE', 'AT', 'CH'], rows=[
       ('Eigenes Gespräch aufnehmen', 'ohne Einwilligung', (False, True, False)),
       ('Heimliche Aufnahme weitergeben', 'an Dritte, ohne Zustimmung', (False, False, False)),
       ('Fremdes Gespräch aufnehmen', 'nicht beteiligt', (False, False, False)),
       ('Mit Einwilligung aller', 'das „Ja“ ist in der Datei', (True, True, True))]),
     '.title{font-size:50px}.cmp td.m{width:62px}'),
 ('enregistrer-conversation', 'fr'): (dict(eyebrow='DROIT · ENREGISTRER', title='Enregistrer sa conversation : <span style="white-space:nowrap">où est-ce</span> <span style="white-space:nowrap">permis ?</span>', sub='Art. 226-1, 314bis, 179ter, Code criminel — côte à côte.', tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT', panel=panel_compare,
     cols=['FR', 'BE', 'CH', 'QC'], rows=[
       ('Enregistrer sa conversation', 'sans consentement', (False, True, False, True)),
       ("Enregistrer celle d'autrui", 'sans y participer', (False, False, False, False)),
       ("Avec l'accord de tous", 'le « oui » enregistré', (True, True, True, True))]),
     '.title{font-size:50px}.cmp td.m{width:54px}'),
 ('ses-kaydi-suc-mu', 'tr'): (dict(eyebrow='HUKUK · SES KAYDI', title='Gizli ses kaydı almak suç mu?', sub='TCK 133, HMK 189/2 ve Yargıtay — bir bakışta.', tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI', panel=panel_rules,
     cap='Türkiye', rows=[
       ('Katıldığınız konuşmayı rızasız kaydetmek', 'suç — TCK 133/2', False),
       ('Başkalarının konuşmasını kaydetmek', 'suç — TCK 133/1', False),
       ('Kaydı ifşa etmek', 'suç — TCK 133/3', False),
       ('Herkesin rızasıyla kayıt', '"evet" dosyada', True)]), ''),
 ('nagrywanie-rozmowy', 'pl'): (dict(eyebrow='PRAWO · NAGRYWANIE', title='Czy można nagrywać rozmowę bez zgody?', sub='Art. 267 k.k., art. 23–24 k.c., art. 168a k.p.k.', tagline='DYKTAFON URUCHAMIANY SŁOWEM', panel=panel_rules,
     cap='Polska', rows=[
       ('Własna rozmowa bez wiedzy rozmówcy', 'co do zasady nie jest przestępstwem', True),
       ('Nagranie jako dowód', 'jeśli nie podważono autentyczności', True),
       ('Cudza rozmowa — podsłuch', 'przestępstwo — art. 267 § 3 k.k.', False),
       ('Rozpowszechnianie nagrania', 'może naruszać dobra osobiste', False)]), ''),
 ('gesprek-opnemen', 'nl'): (dict(eyebrow='RECHT · GESPREK OPNEMEN', title='Mag je een gesprek stiekem opnemen?', sub='Art. 139a Sr, art. 314bis Sw. en de hoogste rechters.', tagline='OPNAME-APP DIE START OP EEN WOORD', panel=panel_compare,
     cols=['NL', 'BE', 'SR', 'CW'], rows=[
       ('Eigen gesprek opnemen', 'zonder toestemming', (True, True, True, True)),
       ('Gesprek van anderen opnemen', 'geen deelnemer', (False, False, False, False)),
       ('Met toestemming van iedereen', 'het „ja” staat erin', (True, True, True, True))]), '.cmp td.m{width:54px}'),
 ('nahravani-rozhovoru', 'cs'): (dict(eyebrow='PRÁVO · NAHRÁVÁNÍ', title='Je legální nahrávat rozhovor bez souhlasu?', sub='Občanský zákoník, trestní zákon a Ústavní soud.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO', panel=panel_compare,
     cols=['CZ', 'SK'], rows=[
       ('Vlastní rozhovor bez svolení', 'k ochraně svých práv', (True, False)),
       ('Cizí rozhovor', 'neúčastníte se ho', (False, False)),
       ('Se svolením všech', '„ano“ je v souboru', (True, True))]), ''),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for key, (t, extra) in CARDS.items():
        if only and key[0] not in only:
            continue
        render({key: t}, CSS + '.left{min-width:0}.right{min-width:0}' + extra)
