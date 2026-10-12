import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_gen import render

HI_CSS = '''body{font-family:'Nirmala UI','Segoe UI',sans-serif}
.title{font-size:52px;line-height:1.3}
.sub{font-size:24px;line-height:1.5}
.eyebrow{letter-spacing:0}
.track{position:relative;display:flex;height:64px;border-radius:14px;overflow:hidden;margin:6px 0 10px}
.track .kept{flex:3;background:repeating-linear-gradient(135deg,rgba(255,255,255,.55) 0 8px,rgba(255,255,255,.25) 8px 16px)}
.track .live{flex:5;background:#fff}
.track .mark{position:absolute;left:37.5%;top:-6px;bottom:-6px;width:4px;background:#ff4d5a}
.tl{display:flex;justify-content:space-between;font-size:17px;color:#d4d0ff;font-weight:600;margin-bottom:12px}
.tl b{color:#fff}
.num{width:34px;height:34px;border-radius:50%;background:rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:18px}
.trig{color:#bdb8ff;font-size:17px;font-weight:600}
.bubble{background:#fff;color:#1d1866;border-radius:22px 22px 22px 6px;padding:22px 24px;font-size:28px;font-weight:700;line-height:1.4}
.bubble mark{background:#ffd84d;color:#1d1866;border-radius:8px;padding:0 6px}
.rec{display:flex;align-items:center;gap:12px;margin-top:18px;font-size:22px;font-weight:800}
.rec i{width:18px;height:18px;border-radius:50%;background:#ff4d5a;box-shadow:0 0 0 6px rgba(255,77,90,.3)}
.lab small{display:block;color:#bdb8ff;font-size:16px;font-weight:600;margin-top:2px}
'''

TAG = 'कीवर्ड से शुरू होने वाला रिकॉर्डर'

def chips(t):
    return '<div class="chips">' + ''.join(f'<div class="chip">{c}</div>' for c in t['chips']) + '</div>'

def panel_delay(t):
    return ('<div class="panel"><div class="cap">रिकॉर्डिंग शुरू होने का पल</div>'
            '<div class="track"><div class="kept"></div><div class="live"></div><div class="mark"></div></div>'
            '<div class="tl"><span><b>−30 सेकंड</b> · सेव</span><span>बटन / कीवर्ड</span><span>उसके बाद</span></div>'
            '<div class="row"><div class="lab">आम रिकॉर्डर<small>बटन दबाने के बाद से</small></div><div class="x">✕</div></div>'
            '<div class="row hl"><div class="lab"><b>TalkSafe</b><small>शुरुआत से पहले के 30 सेकंड भी</small></div><div class="x ok">✓</div></div>'
            + chips(t) + '</div>')

def panel_types(t):
    rows = ''.join(f'<div class="row"><div class="num">{i}</div><div class="lab">{a}<small>{b}</small></div></div>'
                   for i, (a, b) in enumerate(t['types'][:-1], 1))
    a, b = t['types'][-1]
    rows += f'<div class="row hl"><div class="num">5</div><div class="lab"><b>{a}</b><small>{b}</small></div><div class="x ok">✓</div></div>'
    return f'<div class="panel" style="padding:18px 26px">{rows}</div>'

def panel_say(t):
    return ('<div class="panel"><div class="cap">आप वैसे भी पूछते हैं</div>'
            '<div class="bubble">„क्या मैं यह <mark>रिकॉर्ड</mark> कर सकता हूँ?”</div>'
            '<div class="rec"><i></i>रिकॉर्डिंग उसी पल शुरू</div>' + chips(t) + '</div>')

def panel_rec(t):
    rows = ''.join(f'<div class="row"><div class="lab">{a}<small>{b}</small></div></div>' for a, b in t['kinds'][:-1])
    a, b = t['kinds'][-1]
    rows += f'<div class="row hl"><div class="lab"><b>{a}</b><small>{b}</small></div><div class="x ok">✓</div></div>'
    return f'<div class="panel" style="padding:18px 26px"><div class="cap">एक दिन बाद आपके पास क्या है</div>{rows}</div>'

CARDS = {
 ('recording-delay', 'hi'): dict(eyebrow='Android · रिकॉर्डिंग', title='रिकॉर्ड बटन हमेशा देर से क्यों दबता है', sub='ज़रूरी बात बटन से पहले कही जा चुकी होती है।', tagline=TAG, panel=panel_delay,
     chips=['पहले के 30 सेकंड', 'कीवर्ड से शुरू', 'लॉक स्क्रीन पर']),
 ('auto-recording-types', 'hi'): dict(eyebrow='Android · ऑटोमैटिक रिकॉर्डिंग', title='हर „ऑटोमैटिक” रिकॉर्डर एक जैसा काम नहीं करता', sub='पाँच प्रकार — और हर एक को शुरू कौन करता है।', tagline=TAG, panel=panel_types,
     types=[('कॉल रिकॉर्डिंग', 'जुड़ी हुई कॉल'), ('आवाज़ से (VOX)', 'हर आवाज़'), ('तय समय पर', 'कैलेंडर का समय'), ('पिछला बफ़र', 'बटन दबाना'), ('शब्द से शुरुआत', 'चुना हुआ शब्द + पहले के 30 सेकंड')]),
 ('say-it-first', 'hi'): dict(eyebrow='Android · कीवर्ड रिकॉर्डिंग', title='पहले आप कुछ कहते हैं', sub='मुँह हाथों से तेज़ है — तो वही ट्रिगर बने।', tagline=TAG, panel=panel_say,
     chips=['फ़ोन जेब में', 'लॉक स्क्रीन', 'सहमति फ़ाइल में']),
 ('choosing-a-recorder', 'hi'): dict(eyebrow='वॉइस रिकॉर्डर · तुलना', title='<span style="display:block;font-size:46px;line-height:1.3">रिकॉर्डर इस बात से अलग होते हैं कि वे कब शुरू होते हैं</span>', sub='शाम को वे दो मिनट कौन-सा रिकॉर्डर ढूँढने देता है।', tagline=TAG, panel=panel_rec,
     kinds=[('पोर्टेबल, लगातार', 'पूरे दिन की एक फ़ाइल'), ('पोर्टेबल, VOX', 'ढेर सारे क्लिप'), ('अलग वॉइस रिकॉर्डर', 'हर सेशन की एक फ़ाइल'), ('AI नोटटेकर', 'फ़ाइल + ट्रांसक्रिप्ट'), ('फ़ोन, कीवर्ड पर', 'उसी पल से शुरू होने वाली फ़ाइल')]),
}

if __name__ == '__main__':
    render(CARDS, HI_CSS)
