"""블로그 표지 이미지(1200x630) 생성기.

사용법: 언어별 카드 파일(og_hi.py 등)을 만들어 render(CARDS, extra_css)를 호출합니다.
  /c/Users/user/miniconda3/python.exe _tools/og/og_hi.py
결과: assets/img/og/<ref>-<lang>.png  → 글 앞머리에 image, image_alt를 넣습니다.
헤드리스 Edge로 렌더링하므로 Windows의 시스템 글꼴(Segoe UI, Malgun Gothic, Yu Gothic, Nirmala UI)을 씁니다.
"""
import io, os, random, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(tempfile.gettempdir(), 'og_cards')
os.makedirs(OUT, exist_ok=True)
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
REPO = os.path.normpath(os.path.join(HERE, '..', '..', 'assets', 'img', 'og'))
os.makedirs(REPO, exist_ok=True)

ICON = '''<svg width="56" height="56" viewBox="0 0 56 56"><circle cx="28" cy="28" r="28" fill="#fff"/>
<path d="M28 11l13 5v10c0 9-6 16-13 19-7-3-13-10-13-19V16z" fill="none" stroke="#4b3cf0" stroke-width="3" stroke-linejoin="round"/>
<rect x="24" y="18" width="8" height="13" rx="4" fill="#4b3cf0"/><path d="M20.5 27c0 4.5 3.4 7.5 7.5 7.5s7.5-3 7.5-7.5" fill="none" stroke="#4b3cf0" stroke-width="2.6" stroke-linecap="round"/>
<path d="M28 34.5v3.5" stroke="#4b3cf0" stroke-width="2.6" stroke-linecap="round"/></svg>'''

CSS = '''html,body{margin:0;width:1200px;height:630px;overflow:hidden}
body{background:linear-gradient(155deg,#4b3cf0 0%,#3a2fc4 45%,#1d1866 100%);font-family:'Segoe UI','Malgun Gothic','Yu Gothic','Nirmala UI',sans-serif;color:#fff;position:relative;word-break:keep-all;overflow-wrap:break-word}
.wrap{position:absolute;inset:0;display:flex;padding:64px 64px 56px 72px;box-sizing:border-box;gap:48px}
.left{flex:1.25;display:flex;flex-direction:column}
.eyebrow{display:inline-block;align-self:flex-start;font-size:20px;font-weight:600;letter-spacing:.06em;padding:8px 16px;border-radius:999px;background:rgba(255,255,255,.16);color:#e6e3ff}
.title{margin-top:26px;font-size:58px;line-height:1.12;font-weight:800;letter-spacing:-.01em}
.sub{margin-top:20px;font-size:25px;line-height:1.4;color:#d4d0ff;font-weight:500}
.brand{margin-top:auto;display:flex;align-items:center;gap:16px;font-size:32px;font-weight:800}
.brand small{display:block;font-size:17px;font-weight:600;color:#bdb8ff;letter-spacing:.08em}
.right{flex:1;display:flex;align-items:center}
.panel{width:100%;background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.18);border-radius:28px;padding:30px 30px;box-sizing:border-box}
.row{display:flex;align-items:center;gap:14px;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.14);font-size:21px}
.row:last-child{border-bottom:0}
.yr{font-weight:800;width:62px;color:#fff}
.lab{flex:1;color:#e3e0ff;line-height:1.25}
.x{width:34px;height:34px;border-radius:50%;background:#ff4d5a;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:20px}
.ok{background:#2ecc8a}
.hl{background:rgba(255,255,255,.14);border-radius:16px;padding:14px 14px;margin-top:8px;border:0}
.cap{font-size:18px;color:#cfcaff;font-weight:600;margin:4px 0 10px}
.wave{display:flex;align-items:center;gap:4px;height:96px}
.wave i{display:block;width:7px;border-radius:4px}
.arrow{display:flex;align-items:center;gap:12px;margin:14px 0;font-size:20px;font-weight:800;color:#fff}
.arrow span{flex:1;height:2px;background:rgba(255,255,255,.4)}
.chips{display:flex;gap:10px;margin-top:16px;flex-wrap:wrap}
.chip{font-size:17px;font-weight:700;padding:8px 14px;border-radius:999px;background:#fff;color:#3a2fc4}'''

def bars(seed, noisy):
    r = random.Random(seed); out = []
    for i in range(46):
        if noisy:
            h = r.randint(26, 92); c = 'rgba(255,255,255,.45)' if r.random() < .6 else 'rgba(255,120,130,.75)'
        else:
            speech = (8 <= i <= 18) or (24 <= i <= 37)
            h = r.randint(40, 92) if speech else r.randint(4, 8); c = '#ffffff'
        out.append(f'<i style="height:{h}px;background:{c}"></i>')
    return '<div class="wave">' + ''.join(out) + '</div>'

def panel_call(t):
    rows = ''.join(f'<div class="row"><div class="yr">{y}</div><div class="lab">{l}</div><div class="x">✕</div></div>' for y, l in t['steps'])
    rows += f'<div class="row hl"><div class="lab"><b>{t["ok"]}</b></div><div class="x ok">✓</div></div>'
    return f'<div class="panel">{rows}</div>'

def panel_noise(t):
    return (f'<div class="panel"><div class="cap">{t["before"]}</div>{bars(7, True)}'
            f'<div class="arrow"><span></span>{t["arrow"]}<span></span></div>'
            f'<div class="cap">{t["after"]}</div>{bars(11, False)}'
            '<div class="chips">' + ''.join(f'<div class="chip">{c}</div>' for c in t['chips']) + '</div></div>')

CARDS = {
 ('call-recording-android', 'en'): dict(eyebrow='ANDROID · CALL RECORDING', title='Why call recording apps stopped working', sub='And the one thing that was never banned.', tagline='KEYWORD-TRIGGERED RECORDER', panel=panel_call,
     steps=[('2015', 'Android 6 removed the call recording API'), ('2019', 'Android 10 blocked the microphone route'), ('2022', 'Play Store closed the accessibility loophole')], ok='The built-in dialer was never part of the ban'),
 ('call-recording-android', 'ko'): dict(eyebrow='안드로이드 · 통화 녹음', title='통화 녹음 앱이 전부 안 되는 이유', sub='그리고 한 번도 막힌 적 없는 단 하나.', tagline='키워드로 시작되는 녹음 앱', panel=panel_call,
     steps=[('2015', '안드로이드 6, 통화 녹음 API 제거'), ('2019', '안드로이드 10, 마이크 경로 차단'), ('2022', 'Play 스토어, 접근성 우회로 차단')], ok='기본 전화 앱은 처음부터 금지 대상이 아니었습니다'),
 ('remove-background-noise', 'en'): dict(eyebrow='ANDROID · NOISE REMOVAL', title='Remove background noise from a voice recording', sub='Street noise out, the conversation stays — on the phone.', tagline='KEYWORD-TRIGGERED RECORDER', panel=panel_noise,
     before='Recorded on the street', arrow='AI noise removal', after='Cleaned · saved as a new file', chips=['On the device', 'Original kept', 'Works on a trimmed clip']),
 ('remove-background-noise', 'ko'): dict(eyebrow='안드로이드 · 잡음 제거', title='녹음 파일 잡음 제거, 휴대폰에서 바로', sub='길거리 소음은 빼고, 대화는 남기고.', tagline='키워드로 시작되는 녹음 앱', panel=panel_noise,
     before='길거리에서 녹음한 원본', arrow='AI 노이즈 제거', after='정리본 · 새 파일로 저장', chips=['기기 안에서 처리', '원본 그대로 보존', '잘라낸 파일에도']),
}

def render(cards, extra_css=''):
  for (ref, lang), t in cards.items():
    doc = (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}{extra_css}</style></head><body><div class="wrap">'
           f'<div class="left"><div class="eyebrow">{t["eyebrow"]}</div><div class="title">{t["title"]}</div><div class="sub">{t["sub"]}</div>'
           f'<div class="brand">{ICON}<div>TalkSafe<small>{t["tagline"]}</small></div></div></div>'
           f'<div class="right">{t["panel"](t)}</div></div></body></html>')
    name = f'{ref}-{lang}'
    hp = os.path.join(OUT, name + '.html'); io.open(hp, 'w', encoding='utf-8').write(doc)
    png = os.path.join(REPO, name + '.png')
    subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1200,630', f'--screenshot={png}', 'file:///' + hp.replace('\\', '/')], capture_output=True)
    print(name, os.path.getsize(png))

if __name__ == '__main__':
    render(CARDS)
