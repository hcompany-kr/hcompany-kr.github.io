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
.cmp td.m span.na{background:rgba(255,255,255,.22)}
.lab small{display:block;color:#bdb8ff;font-size:16px;font-weight:600;margin-top:2px}
.x.na{background:rgba(255,255,255,.22)}'''

def mark(v):
    if v is None:
        return '<span class="na">–</span>'
    return '<span class="ok">✓</span>' if v else '<span>✕</span>'

def panel_compare(t):
    head = '<tr><th></th>' + ''.join(f'<th>{c}</th>' for c in t['cols']) + '</tr>'
    body = ''.join(f'<tr><td>{a}<small>{b}</small></td>' + ''.join(f'<td class="m">{mark(v)}</td>' for v in vs) + '</tr>'
                   for a, b, vs in t['rows'])
    return f'<div class="panel" style="padding:22px 26px"><table class="cmp">{head}{body}</table></div>'

def panel_rules(t):
    rows = ''.join(f'<div class="row"><div class="lab">{a}<small>{b}</small></div><div class="x{" ok" if v else (" na" if v is None else "")}">{"✓" if v else ("–" if v is None else "✕")}</div></div>'
                   for a, b, v in t['rows'])
    return f'<div class="panel" style="padding:18px 26px"><div class="cap">{t["cap"]}</div>{rows}</div>'

HI_CSS = "body{font-family:'Nirmala UI','Segoe UI',sans-serif}.title{font-size:48px;line-height:1.3}.sub{line-height:1.5}.eyebrow{letter-spacing:0}"

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
 ('recording-police', 'de'): (dict(eyebrow='RECHT · POLIZEI', title='Darf man die Polizei filmen oder aufnehmen?', sub='Bild meist ja, beim Ton entscheidet das Land.', tagline='AUFNAHME-APP MIT STARTWORT', panel=panel_compare,
     cols=['DE', 'AT', 'CH'], rows=[
       ('Einsatz filmen, ohne zu stören', 'Bild', (True, True, None)),
       ('Gespräch mit Beamten aufnehmen', 'ohne Einwilligung', (None, True, False)),
       ('Mit Einwilligung aufnehmen', 'das „Ja“ ist in der Datei', (True, True, True))]), '.title{font-size:52px}.cmp td.m{width:62px}'),
 ('recording-police', 'fr'): (dict(eyebrow='DROIT · POLICE', title='Peut-on filmer ou enregistrer la police ?', sub='Filmer, largement ; le son dépend du pays.', tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT', panel=panel_compare,
     cols=['FR', 'BE', 'CH', 'QC'], rows=[
       ('Filmer sans gêner', 'voie publique', (True, True, None, True)),
       ("Enregistrer l'échange", 'sans consentement', (None, True, False, True)),
       ("Avec l'accord de l'agent", 'le « oui » enregistré', (True, True, True, True))]), '.title{font-size:52px}.cmp td.m{width:54px}'),
 ('recording-police', 'pt-br'): (dict(eyebrow='LEI · POLÍCIA', title='Posso gravar a polícia?', sub='Abordagem, delegacia e depoimento.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA', panel=panel_compare,
     cols=['Brasil', 'Portugal'], rows=[
       ('Gravar a conversa na abordagem', 'você é interlocutor', (True, None)),
       ('Advogado grava o depoimento', 'STJ, HC 662.690 (2022)', (True, None)),
       ('Gravar com consentimento', 'a resposta fica no arquivo', (True, True))]), ''),
 ('recording-police', 'nl'): (dict(eyebrow='RECHT · POLITIE', title='Mag je de politie filmen of opnemen?', sub='Nederland en België, naast elkaar.', tagline='OPNAME-APP DIE START OP EEN WOORD', panel=panel_compare,
     cols=['NL', 'BE'], rows=[
       ('Filmen met zichtbare camera', 'zonder te hinderen', (True, True)),
       ('Eigen gesprek met agent opnemen', 'als deelnemer', (True, True)),
       ('Verborgen filmen op straat', 'art. 441b Sr', (False, None)),
       ('Doxing van agenten', 'art. 285d Sr', (False, None))]), ''),
 ('recording-police', 'tr'): (dict(eyebrow='HUKUK · POLİS', title='Polisi kaydetmek yasak mı?', sub='EGM genelgesi, Danıştay ve TCK 133/2.', tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI', panel=panel_rules,
     cap='Türkiye', rows=[
       ('Müdahaleyi engellemeden görüntü', 'yasaklayan genelge iptal — Danıştay 2023', True),
       ('Polisle konuşmanın rızasız ses kaydı', 'riskli — TCK 133/2', False),
       ('Rızayla ses kaydı', '"evet" dosyada', True),
       ('Müdahaleyi fiziken engellemek', 'çizgi burada', False)]), ''),
 ('recording-police', 'pl'): (dict(eyebrow='PRAWO · POLICJA', title='Czy można nagrywać policję?', sub='Interwencja, kontrola i publikacja nagrania.', tagline='DYKTAFON URUCHAMIANY SŁOWEM', panel=panel_rules,
     cap='Polska', rows=[
       ('Filmowanie interwencji', 'bez utrudniania — RPO', True),
       ('Własna rozmowa z policjantem', 'uczestnik — art. 267 § 3 k.k.', True),
       ('Publikacja nagrania', 'ostrożnie — TSUE C-345/17', None),
       ('Utrudnianie interwencji', 'granica', False)]), ''),
 ('recording-police', 'cs'): (dict(eyebrow='PRÁVO · POLICIE', title='Smí se nahrávat policie?', sub='Zákrok a kontrola v Česku a na Slovensku.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO', panel=panel_compare,
     cols=['CZ', 'SK'], rows=[
       ('Natáčet zákrok', 'aniž byste bránili', (True, True)),
       ('Zakázat natáčení', 'smí to policie?', (False, False)),
       ('Bránit zákroku', 'hranice', (False, False))]), ''),
 ('recording-police', 'hi'): (dict(eyebrow='कानून · पुलिस', title='क्या पुलिस को रिकॉर्ड कर सकते हैं?', sub='थाने और जाँच के दौरान भारत में नियम।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर', panel=panel_rules,
     cap='भारत', rows=[
       ('थाने में वीडियो रिकॉर्डिंग', 'प्रतिबंधित स्थान नहीं — बॉम्बे HC 2022', True),
       ('थाने में ऑडियो रिकॉर्डिंग', 'वही तर्क — औरंगाबाद पीठ 2024', True),
       ('पुलिस से अपनी बातचीत', 'इंटरसेप्शन नहीं — मलकानी 1973', True),
       ('काम में बाधा डालना', 'सीमा यहीं है', False)]), "body{font-family:'Nirmala UI','Segoe UI',sans-serif}.title{font-size:52px;line-height:1.3}.sub{line-height:1.5}.eyebrow{letter-spacing:0}"),
 ('mobbing', 'tr'): (dict(eyebrow='İŞ HAYATI · MOBBING', title='İş yerinde mobbing nasıl ispatlanır?', sub='TBK 417, İş Kanunu 24/II ve Yargıtay.', tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI', panel=panel_rules,
     cap='Türkiye — ne işe yarar', rows=[
       ('Yazılı şikâyet, e-posta, tanık', 'kuvvetli emare', True),
       ('Sağlık raporu, olay günlüğü', 'tutarlı olgular', True),
       ('Konuşmanın rızasız ses kaydı', 'riskli — TCK 133/2', False),
       ('Kendi sesinizle olay notu', 'olaydan hemen sonra', True)]), ''),
 ('mobbing', 'de'): (dict(eyebrow='ARBEIT · MOBBING', title='Mobbing am Arbeitsplatz beweisen', sub='Kein Mobbing-Gesetz – Beweislast beim Arbeitnehmer.', tagline='AUFNAHME-APP MIT STARTWORT', panel=panel_rules,
     cap='Deutschland — was trägt', rows=[
       ('Mobbingtagebuch, E-Mails, Zeugen', 'zeitnah, mit Datum', True),
       ('Schriftliche Beschwerde', 'ab wann der Arbeitgeber wusste', True),
       ('Heimliche Tonaufnahme', 'strafbar — § 201 StGB', False),
       ('Gedächtnisprotokoll, eigene Stimme', 'direkt nach dem Vorfall', True)]), '.title{font-size:52px}'),
 ('harcelement-moral', 'fr'): (dict(eyebrow='TRAVAIL · HARCÈLEMENT MORAL', title='Prouver le harcèlement moral au travail', sub='L1152-1, L1154-1 et la Cour de cassation.', tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT', panel=panel_rules,
     cap='France — ce qui compte', rows=[
       ('Écrits, alerte, témoins', 'éléments de fait (L1154-1)', True),
       ('Certificats, journal daté', 'au fil de l\'eau', True),
       ('Enregistrement clandestin', 'seulement si indispensable', None),
       ('Récit enregistré avec sa voix', 'juste après les faits', True)]), '.title{font-size:52px}'),
 ('assedio-moral', 'pt-br'): (dict(eyebrow='TRABALHO · ASSÉDIO MORAL', title='Como provar assédio moral no trabalho', sub='CLT art. 483, dano moral e a gravação lícita.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA', panel=panel_rules,
     cap='Brasil — o que pesa', rows=[
       ('Gravar a conversa da qual participa', 'lícito — STF Tema 237, TST', True),
       ('Testemunhas e mensagens', 'reforçam a gravação', True),
       ('Denúncia na CIPA ou canal', 'Lei 14.457/2022', True),
       ('Gravar conversa dos outros', 'crime — Lei 9.296, art. 10', False)]), '.title{font-size:52px}'),
 ('mobbing', 'pl'): (dict(eyebrow='PRACA · MOBBING', title='Jak udowodnić mobbing w pracy?', sub='Art. 94³ k.p. — nowa definicja od 5 listopada 2026.', tagline='DYKTAFON URUCHAMIANY SŁOWEM', panel=panel_rules,
     cap='Polska', rows=[
       ('Nagranie własnej rozmowy', 'dozwolone — art. 267 § 3 k.k.', True),
       ('Pisemne zgłoszenie, świadkowie', 'od kiedy pracodawca wiedział', True),
       ('Od 5.11.2026: bez „długotrwałości”', 'Dz.U. 2026 poz. 1046', True),
       ('Podsłuch cudzej rozmowy', 'przestępstwo', False)]), ''),
 ('pesten-op-het-werk', 'nl'): (dict(eyebrow='WERK · PESTEN', title='Pesten op het werk bewijzen', sub='Arbowet, welzijnswet en je eigen opname.', tagline='OPNAME-APP DIE START OP EEN WOORD', panel=panel_compare,
     cols=['NL', 'BE'], rows=[
       ('Werkgever moet pesten aanpakken', 'Arbowet / welzijnswet', (True, True)),
       ('Eigen gesprek opnemen', 'als deelnemer', (True, True)),
       ('Opname als bewijs', 'niet automatisch uitgesloten', (True, True)),
       ('Gesprek van anderen opnemen', 'geen deelnemer', (False, False))]), ''),
 ('sikana-na-pracovisti', 'cs'): (dict(eyebrow='PRÁCE · ŠIKANA', title='Jak prokázat šikanu na pracovišti?', sub='Mobbing, bossing, nahrávka a kam se obrátit.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO', panel=panel_compare,
     cols=['CZ', 'SK'], rows=[
       ('Zákonná definice šikany', 'mobbing, bossing', (False, False)),
       ('Zaměstnavatel musí zakročit', 'ZP § 16, 17 / § 13', (True, True)),
       ('Nahrát vlastní rozhovor', 'k ochraně svých práv', (True, False)),
       ('Cizí rozhovor', 'neúčastníte se ho', (False, False))]), ''),
 ('workplace-harassment', 'hi'): (dict(eyebrow='काम · उत्पीड़न', title='कार्यस्थल पर उत्पीड़न कैसे साबित करें', sub='भारत में कानून, रिकॉर्डिंग और शिकायत।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर', panel=panel_rules,
     cap='भारत', rows=[
       ('बुलिंग के लिए अलग कानून', 'नहीं है', False),
       ('यौन उत्पीड़न — आंतरिक समिति', 'POSH अधिनियम 2013', True),
       ('अपनी बातचीत की रिकॉर्डिंग', 'इंटरसेप्शन नहीं — मलकानी 1973', True),
       ('सबूत में पेश करना', 'हैश वैल्यू वाला प्रमाणपत्र — BSA 63(4)', True)]), HI_CSS),
 ('sexuelle-belaestigung', 'de'): (dict(eyebrow='ARBEIT · SEXUELLE BELÄSTIGUNG', title='Sexuelle Belästigung am Arbeitsplatz beweisen', sub='AGG, GlBG und Gleichstellungsgesetz im Vergleich.', tagline='AUFNAHME-APP MIT STARTWORT', panel=panel_compare,
     cols=['DE', 'AT', 'CH'], rows=[
       ('Gesetzlicher Schutz', 'AGG · GlBG · GlG', (True, True, True)),
       ('Lange Frist für Ansprüche', 'DE 2 Monate · AT 3 Jahre', (False, True, None)),
       ('Eigenes Gespräch heimlich aufnehmen', '§ 201 · Art. 179ter', (False, True, False)),
       ('Gedächtnisprotokoll mit eigener Stimme', 'direkt danach', (True, True, True))]), '.title{font-size:50px}.cmp td.m{width:62px}'),
 ('harcelement-sexuel', 'fr'): (dict(eyebrow='TRAVAIL · HARCÈLEMENT SEXUEL', title='Harcèlement sexuel au travail : que prouver ?', sub='L1153-1, L1154-1, 222-33 — et ailleurs.', tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT', panel=panel_compare,
     cols=['FR', 'BE', 'CH', 'QC'], rows=[
       ('Un seul fait grave suffit', 'pression grave · conduite grave', (True, None, None, True)),
       ('Enregistrer sa conversation', 'sans consentement', (False, True, False, True)),
       ('Récit avec sa propre voix', 'juste après les faits', (True, True, True, True))]), '.title{font-size:50px}.cmp td.m{width:54px}'),
 ('cinsel-taciz', 'tr'): (dict(eyebrow='İŞ HAYATI · CİNSEL TACİZ', title='İş yerinde cinsel tacize uğradım, ne yapmalıyım?', sub='TCK 105, İş Kanunu 24/II-d ve Yargıtay.', tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI', panel=panel_rules,
     cap='Türkiye', rows=[
       ('Cinsel taciz suçu', 'işyeri ve hiyerarşide ceza yarı oranında artar', True),
       ('Kıdem tazminatıyla haklı fesih', 'İş Kanunu 24/II-d — 6 iş günü', True),
       ('Konuşmanın rızasız ses kaydı', 'riskli — TCK 133/2, dar istisna', False),
       ('Kendi sesinizle olay notu', 'olaydan hemen sonra', True)]), '.title{font-size:50px}'),
 ('assedio-sexual', 'pt-br'): (dict(eyebrow='TRABALHO · ASSÉDIO SEXUAL', title='Assédio sexual no trabalho: como provar', sub='Arts. 216-A e 215-A, CLT art. 483 e a gravação lícita.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA', panel=panel_compare,
     cols=['Brasil', 'Portugal'], rows=[
       ('Assédio sexual é crime ou infração', 'CP art. 216-A · CT art. 29.º', (True, True)),
       ('Gravar a própria conversa', 'sem o outro saber', (True, False)),
       ('Gravação como prova', 'STF, Tema 237', (True, False)),
       ('Relato com a própria voz', 'logo depois', (True, True))]), ''),
 ('molestowanie-w-pracy', 'pl'): (dict(eyebrow='PRACA · MOLESTOWANIE', title='Molestowanie seksualne w pracy: jak udowodnić?', sub='Art. 18³a § 6, 18³b i 18³d Kodeksu pracy.', tagline='DYKTAFON URUCHAMIANY SŁOWEM', panel=panel_rules,
     cap='Polska', rows=[
       ('Molestowanie to dyskryminacja', 'art. 18³a § 6 k.p.', True),
       ('Pracodawca musi się wytłumaczyć', 'odwrócony ciężar dowodu — art. 18³b', True),
       ('Odszkodowanie co najmniej płaca minimalna', 'art. 18³d k.p.', True),
       ('Nagranie rozmowy, w której uczestniczysz', 'co do zasady dozwolone', True)]), '.title{font-size:50px}'),
 ('seksuele-intimidatie', 'nl'): (dict(eyebrow='WERK · SEKSUELE INTIMIDATIE', title='Seksuele intimidatie op het werk', sub='Art. 7:646 BW, Arbowet en de Belgische welzijnswet.', tagline='OPNAME-APP DIE START OP EEN WOORD', panel=panel_compare,
     cols=['NL', 'BE'], rows=[
       ('Werkgever moet het voorkomen', 'Arbowet / welzijnswet', (True, True)),
       ('Woorden en appjes tellen ook', 'aanraking niet vereist', (True, True)),
       ('Eigen gesprek opnemen', 'zonder toestemming', (True, True))]), ''),
 ('sexualni-obtezovani', 'cs'): (dict(eyebrow='PRÁCE · SEXUÁLNÍ OBTĚŽOVÁNÍ', title='Sexuální obtěžování na pracovišti', sub='Antidiskriminační zákon, § 133a o. s. ř. a nahrávka.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO', panel=panel_compare,
     cols=['CZ', 'SK'], rows=[
       ('Forma diskriminace', 'antidiskriminační zákon', (True, True)),
       ('Vlastní rozhovor bez svolení', 'k ochraně svých práv', (True, False)),
       ('Vlastní výpověď hlasem', 'hned po události', (True, True))]), ''),
 ('posh-act', 'hi'): (dict(eyebrow='काम · POSH', title='POSH अधिनियम: शिकायत और सबूत', sub='3 महीने की समय-सीमा, समिति और रिकॉर्डिंग।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर', panel=panel_rules,
     cap='भारत', rows=[
       ('10+ कर्मचारी — आंतरिक समिति', 'उससे कम — स्थानीय समिति', True),
       ('लिखित शिकायत, 3 महीने में', '3 महीने तक बढ़ सकती है — धारा 9', True),
       ('यौन उत्पीड़न अपराध भी', 'भारतीय न्याय संहिता, धारा 75', True),
       ('अपनी बातचीत की रिकॉर्डिंग', 'इंटरसेप्शन नहीं — मलकानी 1973', True)]), HI_CSS),
 ('geld-verliehen', 'de'): (dict(eyebrow='GELD · DARLEHEN', title='Geld verliehen ohne Vertrag', sub='Beweis, Verjährung und Anerkenntnis – DE und CH.', tagline='AUFNAHME-APP MIT STARTWORT', panel=panel_compare,
     cols=['DE', 'CH'], rows=[
       ('Darlehen mündlich wirksam', 'Beweis beim Gläubiger', (True, None)),
       ('Lange Verjährung', 'DE 3 Jahre · CH 10 Jahre', (False, True)),
       ('Anerkenntnis startet Frist neu', '§ 212 BGB · Art. 135 OR', (True, True)),
       ('Gespräch heimlich aufnehmen', '§ 201 · Art. 179ter', (False, False)),
       ('Aufnahme mit Einwilligung', 'das „Ja“ ist in der Datei', (True, True))]), '.title{font-size:56px}.cmp td.m{width:62px}'),
 ('pret-entre-particuliers', 'fr'): (dict(eyebrow='ARGENT · PRÊT', title='Prêt entre particuliers sans écrit', sub='Preuve, prescription et reconnaissance de dette.', tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT', panel=panel_compare,
     cols=['FR', 'BE', 'CH'], rows=[
       ('Écrit exigé au-delà de', 'FR 1 500 € · BE 3 500 €', (True, True, None)),
       ('Relance interrompt la prescription', 'Cass. com. 18 mai 2022', (False, None, None)),
       ('Reconnaissance du débiteur interrompt', 'art. 2240 · 135 CO', (True, True, True)),
       ('Enregistrer sa conversation', 'sans consentement', (False, True, False))]), '.title{font-size:54px}.cmp td.m{width:58px}'),
 ('borc-verdim', 'tr'): (dict(eyebrow='PARA · BORÇ', title='Borç verdim, senet yok', sub='HMK 200, delil başlangıcı ve zamanaşımı.', tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI', panel=panel_rules,
     cap='Türkiye', rows=[
       ('Borçlunun WhatsApp mesajı', 'delil başlangıcı — Yargıtay 2024', True),
       ('Yakın akrabalar arası borç', 'tanık dinlenebilir — HMK 203', True),
       ('İhtarname zamanaşımını keser', 'kesmez; ikrar keser', False),
       ('Konuşmayı rızasız kaydetmek', 'suç — TCK 133/2', False)]), '.title{font-size:58px}'),
 ('emprestei-dinheiro', 'pt-br'): (dict(eyebrow='DINHEIRO · EMPRÉSTIMO', title='Emprestei dinheiro e não me pagaram', sub='Prova sem contrato, WhatsApp e prescrição.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA', panel=panel_compare,
     cols=['Brasil', 'Portugal'], rows=[
       ('Empréstimo verbal acima de 2 500 €', 'PT: exige documento assinado', (True, False)),
       ('Reconhecimento interrompe prazo', 'CC art. 202, VI', (True, None)),
       ('Gravar a própria conversa', 'sem o outro saber', (True, False)),
       ('Gravar com consentimento', 'a resposta fica no arquivo', (True, True))]), '.title{font-size:54px}'),
 ('pozyczka-bez-umowy', 'pl'): (dict(eyebrow='PIENIĄDZE · POŻYCZKA', title='Pożyczka bez umowy: jak odzyskać pieniądze?', sub='Art. 720, 74, 118 i 123 Kodeksu cywilnego.', tagline='DYKTAFON URUCHAMIANY SŁOWEM', panel=panel_rules,
     cap='Polska', rows=[
       ('Umowa bez formy dokumentowej ważna', 'ogranicza tylko dowody — art. 74', True),
       ('Wiadomość od dłużnika', 'może uprawdopodobnić pożyczkę', True),
       ('Uznanie długu przerywa przedawnienie', 'art. 123 § 1 pkt 2 k.c.', True),
       ('Nagranie rozmowy, w której uczestniczysz', 'co do zasady dozwolone', True)]), '.title{font-size:52px}'),
 ('geld-geleend', 'nl'): (dict(eyebrow='GELD · LENING', title='Geld geleend en niet terugbetaald', sub='Bewijs, verjaring en stuiting in NL en BE.', tagline='OPNAME-APP DIE START OP EEN WOORD', panel=panel_compare,
     cols=['NL', 'BE'], rows=[
       ('Mondelinge herinnering stuit', 'NL: alleen schriftelijk — 3:317', (False, None)),
       ('Erkenning door schuldenaar stuit', 'ook mondeling — 3:318', (True, True)),
       ('Eigen gesprek opnemen', 'zonder toestemming', (True, True))]), '.title{font-size:54px}'),
 ('pujcka-bez-smlouvy', 'cs'): (dict(eyebrow='PENÍZE · PŮJČKA', title='Půjčka bez smlouvy', sub='Důkaz, promlčení a uznání dluhu.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO', panel=panel_compare,
     cols=['CZ', 'SK'], rows=[
       ('Písemné uznání: nová lhůta 10 let', '§ 639 · § 558', (True, True)),
       ('Ústní slib prodlouží promlčení', 'nestačí', (False, False)),
       ('Vlastní rozhovor bez svolení', 'k ochraně svých práv', (True, False))]), '.title{font-size:58px}'),
 ('lent-money', 'hi'): (dict(eyebrow='पैसा · उधार', title='उधार दिए पैसे वापस कैसे लें', sub='सबूत, 3 साल की समय-सीमा और चेक बाउंस।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर', panel=panel_rules,
     cap='भारत', rows=[
       ('मुकदमे की समय-सीमा', 'उधार देने की तारीख़ से 3 साल', True),
       ('ज़बानी "लौटा दूँगा" से अवधि बढ़ती है', 'नहीं — लिखित, हस्ताक्षरित स्वीकृति', False),
       ('चेक बाउंस पर नोटिस', '30 दिन में — धारा 138', True),
       ('अपनी बातचीत की रिकॉर्डिंग', 'इंटरसेप्शन नहीं — मलकानी 1973', True)]), HI_CSS),
 ('kaution-zurueck', 'de'): (dict(eyebrow='WOHNEN · KAUTION', title='Vermieter zahlt die Kaution nicht zurück', sub='Höchstbetrag, Frist, Abnutzung – DE und CH.', tagline='AUFNAHME-APP MIT STARTWORT', panel=panel_compare,
     cols=['DE', 'CH'], rows=[
       ('Höchstens drei Monatsmieten', '§ 551 BGB · Art. 257e OR', (True, True)),
       ('Feste Rückzahlungsfrist', 'DE: meist bis 6 Monate · CH: 1 Jahr', (False, True)),
       ('Normale Abnutzung zahlt der Mieter', '§ 538 BGB', (False, None)),
       ('Übergabe heimlich aufnehmen', '§ 201 · Art. 179ter', (False, False)),
       ('Aufnahme mit Einwilligung', 'das „Ja“ ist in der Datei', (True, True))]), '.title{font-size:52px}.cmp td.m{width:62px}'),
 ('caution-non-rendue', 'fr'): (dict(eyebrow='LOGEMENT · CAUTION', title='Caution non rendue : que dit la loi ?', sub='Plafond, délais et majoration de 10 %.', tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT', panel=panel_compare,
     cols=['FR', 'CH', 'QC'], rows=[
       ('Dépôt de garantie permis', 'FR 1 mois · CH 3 mois · QC interdit', (True, True, False)),
       ('Pénalité de retard', '+10 % du loyer par mois', (True, None, None)),
       ('Enregistrer sa conversation', 'sans consentement', (False, False, True)),
       ('Enregistrer avec son accord', 'la réponse est dans le fichier', (True, True, True))]), '.title{font-size:54px}.cmp td.m{width:58px}'),
 ('kira-depozitosu', 'tr'): (dict(eyebrow='KONUT · DEPOZİTO', title='Ev sahibi depozitoyu vermiyor', sub='TBK 342, 334 ve 335 — bir bakışta.', tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI', panel=panel_rules,
     cap='Türkiye', rows=[
       ('En fazla üç aylık kira', 'vadeli hesapta — TBK 342', True),
       ('Olağan eskime kesilebilir', 'kesilemez — TBK 334', False),
       ('Ev sahibi teslimde yazılı bildirmeli', 'derhal — TBK 335', True),
       ('Konuşmayı rızasız kaydetmek', 'suç — TCK 133/2', False)]), '.title{font-size:56px}'),
 ('caucao-aluguel', 'pt-br'): (dict(eyebrow='MORADIA · CAUÇÃO', title='Caução do aluguel não devolvida', sub='Lei do Inquilinato, vistoria e gravação lícita.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA', panel=panel_compare,
     cols=['Brasil', 'Portugal'], rows=[
       ('Limite da caução', 'BR 3 aluguéis · PT 2 rendas', (True, True)),
       ('Desgaste normal descontado', 'BR: art. 23, III', (False, None)),
       ('Gravar a própria conversa', 'sem o outro saber', (True, False)),
       ('Gravar com consentimento', 'a resposta fica no arquivo', (True, True))]), '.title{font-size:56px}'),
 ('zwrot-kaucji', 'pl'): (dict(eyebrow='MIESZKANIE · KAUCJA', title='Wynajmujący nie oddaje kaucji', sub='Art. 6 ustawy o ochronie praw lokatorów i art. 675 k.c.', tagline='DYKTAFON URUCHAMIANY SŁOWEM', panel=panel_rules,
     cap='Polska', rows=[
       ('Zwrot w ciągu miesiąca', 'od opróżnienia lokalu', True),
       ('Kwota zwaloryzowana', 'według czynszu z dnia zwrotu', True),
       ('Potrącenie za normalne zużycie', 'niedopuszczalne — art. 675 k.c.', False),
       ('Nagranie rozmowy, w której uczestniczysz', 'co do zasady dozwolone', True)]), '.title{font-size:54px}'),
 ('borg-terug', 'nl'): (dict(eyebrow='WONEN · BORG', title='Verhuurder betaalt de borg niet terug', sub='Wet goed verhuurderschap en art. 7:224 BW.', tagline='OPNAME-APP DIE START OP EEN WOORD', panel=panel_rules,
     cap='Nederland', rows=[
       ('Maximaal twee maanden kale huur', 'contracten vanaf 1 juli 2023', True),
       ('Terug binnen 14 dagen', '30 dagen bij verrekening', True),
       ('Administratiekosten verrekenen', 'niet toegestaan', False),
       ('Eigen gesprek opnemen', 'ook in België', True)]), '.title{font-size:52px}'),
 ('vraceni-kauce', 'cs'): (dict(eyebrow='BYDLENÍ · KAUCE', title='Pronajímatel nevrátil kauci', sub='§ 2254 občanského zákoníku a předání bytu.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO', panel=panel_rules,
     cap='Česká republika', rows=[
       ('Nejvýše trojnásobek nájemného', '§ 2254 obč. zák.', True),
       ('Vrácení s úroky', 'alespoň zákonná sazba', True),
       ('Strhnout obvyklé opotřebení', 'nelze', False),
       ('Nahrát vlastní rozhovor při předání', 'k ochraně práv — § 88', True)]), '.title{font-size:56px}'),
 ('security-deposit', 'hi'): (dict(eyebrow='किराया · डिपॉज़िट', title='सिक्योरिटी डिपॉज़िट वापस नहीं मिला', sub='मॉडल अधिनियम, धारा 108(m) और रिकॉर्डिंग।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर', panel=panel_rules,
     cap='भारत', rows=[
       ('देशभर पर लागू डिपॉज़िट कानून', 'नहीं — मॉडल अधिनियम राज्यों के लिए', False),
       ('मॉडल अधिनियम: आवासीय सीमा', 'दो महीने का किराया', True),
       ('सामान्य टूट-फूट किरायेदार पर', 'नहीं — धारा 108(m)', False),
       ('अपनी बातचीत की रिकॉर्डिंग', 'इंटरसेप्शन नहीं — मलकानी 1973', True)]), HI_CSS),
 ('stalking-beweisen', 'de'): (dict(eyebrow='SICHERHEIT · STALKING', title='Stalking beweisen', sub='§ 238 StGB, § 107a StGB, Art. 181b StGB.', tagline='AUFNAHME-APP MIT STARTWORT', panel=panel_compare,
     cols=['DE', 'AT', 'CH'], rows=[
       ('Stalking strafbar', 'CH seit 1.1.2026', (True, True, True)),
       ('Anrufe heimlich aufnehmen', '§ 201 · Art. 179ter', (False, True, False)),
       ('Tagebuch mit eigener Stimme', 'direkt nach dem Vorfall', (True, True, True))]), '.title{font-size:60px}.cmp td.m{width:62px}'),
 ('harcelement-preuves', 'fr'): (dict(eyebrow='SÉCURITÉ · HARCÈLEMENT', title='Harcèlement et stalking : réunir des preuves', sub='Art. 222-33-2-2, ordonnance de protection, 181b CP.', tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT', panel=panel_compare,
     cols=['FR', 'BE', 'CH', 'QC'], rows=[
       ('Harcèlement puni', 'CH : stalking depuis 2026', (True, True, True, True)),
       ('Enregistrer ses appels', 'sans consentement', (False, True, False, True)),
       ('Journal avec sa propre voix', 'juste après les faits', (True, True, True, True))]), '.title{font-size:52px}.cmp td.m{width:54px}'),
 ('israrli-takip', 'tr'): (dict(eyebrow='GÜVENLİK · ISRARLI TAKİP', title='Israrlı takip suçu nasıl ispatlanır?', sub='TCK 123/A, şikâyet süresi ve 6284 sayılı Kanun.', tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI', panel=panel_rules,
     cap='Türkiye', rows=[
       ('Israrlı takip suçtur', '6 ay – 2 yıl; nitelikli 1 – 3 yıl', True),
       ('Şikâyet gerekir', 'altı ay içinde', True),
       ('Aramaları rızasız kaydetmek', 'riskli — TCK 133/2', False),
       ('Kendi sesinizle olay notu', 'olaydan hemen sonra', True)]), '.title{font-size:54px}'),
 ('crime-de-perseguicao', 'pt-br'): (dict(eyebrow='SEGURANÇA · PERSEGUIÇÃO', title='Crime de perseguição: como juntar provas', sub='Art. 147-A do CP, representação e gravação lícita.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA', panel=panel_compare,
     cols=['Brasil', 'Portugal'], rows=[
       ('Perseguição é crime', 'art. 147-A · art. 154.º-A', (True, True)),
       ('Gravar a própria conversa', 'sem o outro saber', (True, False)),
       ('Relato com a própria voz', 'logo depois', (True, True))]), '.title{font-size:52px}'),
 ('uporczywe-nekanie', 'pl'): (dict(eyebrow='BEZPIECZEŃSTWO · STALKING', title='Uporczywe nękanie: jak zebrać dowody', sub='Art. 190a Kodeksu karnego — od 6 miesięcy do 8 lat.', tagline='DYKTAFON URUCHAMIANY SŁOWEM', panel=panel_rules,
     cap='Polska', rows=[
       ('Stalking jest przestępstwem', 'art. 190a § 1 k.k.', True),
       ('Ściganie z urzędu', 'nie — na wniosek pokrzywdzonego', False),
       ('Nagranie rozmowy, w której uczestniczysz', 'co do zasady dozwolone', True),
       ('Datowany dziennik zdarzeń', 'zdarzenie po zdarzeniu', True)]), '.title{font-size:54px}'),
 ('belaging', 'nl'): (dict(eyebrow='VEILIGHEID · BELAGING', title='Stalking (belaging) bewijzen', sub='Art. 285b Sr en art. 442bis Strafwetboek.', tagline='OPNAME-APP DIE START OP EEN WOORD', panel=panel_compare,
     cols=['NL', 'BE'], rows=[
       ('Belaging strafbaar', '285b Sr · 442bis Sw.', (True, True)),
       ('Vervolging zonder klacht', 'NL: alleen op klacht', (False, None)),
       ('Eigen gesprek opnemen', 'zonder toestemming', (True, True))]), '.title{font-size:58px}'),
 ('nebezpecne-pronasledovani', 'cs'): (dict(eyebrow='BEZPEČÍ · STALKING', title='Nebezpečné pronásledování', sub='§ 354 trestního zákoníku a jak sbírat důkazy.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO', panel=panel_compare,
     cols=['CZ', 'SK'], rows=[
       ('Stalking je trestný čin', '§ 354 · § 360a', (True, True)),
       ('Vlastní rozhovor bez svolení', 'k ochraně svých práv', (True, False)),
       ('Deník vlastním hlasem', 'hned po události', (True, True))]), '.title{font-size:58px}'),
 ('stalking', 'hi'): (dict(eyebrow='सुरक्षा · स्टॉकिंग', title='स्टॉकिंग का सबूत कैसे जुटाएँ', sub='भारतीय न्याय संहिता, धारा 78 और हर घटना का रिकॉर्ड।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर', panel=panel_rules,
     cap='भारत', rows=[
       ('स्टॉकिंग अपराध है', 'धारा 78 — पहले IPC 354D', True),
       ('सज़ा', 'पहली बार 3 साल तक, दोबारा 5 साल तक', True),
       ('अपनी बातचीत की रिकॉर्डिंग', 'इंटरसेप्शन नहीं — मलकानी 1973', True),
       ('तारीख़वार डायरी', 'हर घटना के तुरंत बाद', True)]), HI_CSS),
 ('muendlicher-vertrag', 'de'): (dict(eyebrow='VERTRÄGE · MÜNDLICH', title='Mündlicher Vertrag: gilt er?', sub='Formfreiheit, § 305b BGB und der Kostenvoranschlag.', tagline='AUFNAHME-APP MIT STARTWORT', panel=panel_compare,
     cols=['DE', 'AT', 'CH'], rows=[
       ('Mündlicher Vertrag gültig', 'außer gesetzliche Form', (True, True, True)),
       ('Abrede gegen Schriftliches', 'muss bewiesen werden', (True, None, True)),
       ('Eigenes Gespräch heimlich aufnehmen', 'ohne Einwilligung', (False, True, False))]), '.title{font-size:56px}.cmp td.m{width:62px}'),
 ('contrat-verbal', 'fr'): (dict(eyebrow='CONTRATS · VERBAL', title='Contrat verbal : valable, mais à prouver', sub='Art. 1172 et 1359 C. civ., Livre 8, art. 11 CO.', tagline='ENREGISTREUR QUI DÉMARRE SUR UN MOT', panel=panel_compare,
     cols=['FR', 'BE', 'CH', 'QC'], rows=[
       ('Contrat verbal valable', 'sauf forme imposée', (True, True, True, True)),
       ('Témoins contre un écrit', 'sans autre écrit', (False, False, None, False)),
       ('Enregistrer sa conversation', 'sans consentement', (False, True, False, True))]), '.title{font-size:52px}.cmp td.m{width:54px}'),
 ('sozlu-sozlesme', 'tr'): (dict(eyebrow='SÖZLEŞME · SÖZLÜ', title='Sözlü sözleşme geçerli mi?', sub='TBK 12, HMK 200–202 ve yazılı teklif.', tagline='KELİMEYLE BAŞLAYAN KAYIT UYGULAMASI', panel=panel_rules,
     cap='Türkiye', rows=[
       ('Sözlü sözleşme', 'geçerli — TBK 12', True),
       ('Senede karşı tanıkla ispat', 'yasak — HMK 201', False),
       ('Karşı taraftan mesaj, e-posta', 'delil başlangıcı — HMK 202', True),
       ('Konuşmayı rızasız kaydetmek', 'suç — TCK 133/2', False)]), ''),
 ('contrato-verbal', 'pt-br'): (dict(eyebrow='CONTRATOS · VERBAL', title='Contrato verbal tem validade?', sub='Art. 107 CC, art. 40 CDC e o orçamento da reforma.', tagline='GRAVADOR QUE COMEÇA COM UMA PALAVRA', panel=panel_compare,
     cols=['Brasil', 'Portugal'], rows=[
       ('Contrato verbal é válido', 'salvo forma exigida', (True, True)),
       ('Testemunha contra documento', 'convenção adicional', (None, False)),
       ('Gravar a própria conversa', 'sem avisar', (True, False))]), ''),
 ('umowa-ustna', 'pl'): (dict(eyebrow='UMOWY · USTNA', title='Czy umowa ustna jest ważna?', sub='Art. 60 i 74 k.c., art. 247 k.p.c.', tagline='DYKTAFON URUCHAMIANY SŁOWEM', panel=panel_rules,
     cap='Polska', rows=[
       ('Umowa ustna', 'ważna — art. 60 k.c.', True),
       ('Świadkowie przy formie dowodowej', 'wyłączeni — art. 74 § 1', False),
       ('Konsument przeciw firmie', 'może żądać świadków — art. 74 § 2', True),
       ('Nagranie własnej rozmowy', 'co do zasady dozwolone', True)]), '.title{font-size:56px}'),
 ('mondelinge-afspraak', 'nl'): (dict(eyebrow='CONTRACTEN · MONDELING', title='Is een mondelinge afspraak geldig?', sub='Art. 3:37 BW, art. 157 Rv en Boek 8 BW.', tagline='OPNAME-APP DIE START OP EEN WOORD', panel=panel_compare,
     cols=['NL', 'BE'], rows=[
       ('Mondelinge overeenkomst geldig', 'vormvrij', (True, True)),
       ('Tegenbewijs tegen getekend stuk', 'NL: open — BE: alleen met geschrift', (True, False)),
       ('Eigen gesprek opnemen', 'als deelnemer', (True, True))]), '.title{font-size:52px}'),
 ('ustni-smlouva', 'cs'): (dict(eyebrow='SMLOUVY · ÚSTNÍ', title='Platí ústní smlouva?', sub='§ 559, 564 a 1758 občanského zákoníku.', tagline='DIKTAFON, KTERÝ SPUSTÍ SLOVO', panel=panel_rules,
     cap='Česko', rows=[
       ('Ústní smlouva', 'platná — § 559', True),
       ('Nemovitost', 'písemná forma — § 560', False),
       ('Dohoda „sepíšeme to“', 'bez formy se má za to, že nevázáni — § 1758', False),
       ('Vlastní rozhovor nahrát', 'k ochraně svých práv — § 88', True)]), '.title{font-size:58px}'),
 ('verbal-contract', 'hi'): (dict(eyebrow='अनुबंध · मौखिक', title='क्या मौखिक समझौता मान्य है?', sub='संविदा अधिनियम धारा 10, साक्ष्य अधिनियम धारा 94–95।', tagline='कीवर्ड से शुरू होने वाला रिकॉर्डर', panel=panel_rules,
     cap='भारत', rows=[
       ('मौखिक अनुबंध', 'मान्य — धारा 10', True),
       ('लिखित शर्तों के ख़िलाफ़ मौखिक सबूत', 'आम तौर पर बाहर — धारा 95', False),
       ('बाद का मौखिक संशोधन', 'साबित किया जा सकता है — धारा 95', True),
       ('अपनी बातचीत की रिकॉर्डिंग', 'इंटरसेप्शन नहीं — मलकानी 1973', True)]), HI_CSS),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for key, (t, extra) in CARDS.items():
        if only and key[0] not in only:
            continue
        render({key: t}, CSS + '.left{min-width:0}.right{min-width:0}' + extra)
