"""회의 녹음 글(ref meeting-recording) 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_meeting.py [lang ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_law import CSS, HI_CSS
from og_gen import render
from og_summary import T as SUM
from og_divorce import panel_text, TXT_CSS

C = {
 'ko': ('사용법 · 회의 녹음', '휴대폰으로 회의 녹음하는 법', '시작 전에 나온 말부터 끝난 뒤 요약까지.', '대면 회의 · TalkSafe',
        [('시작', '진행자의 말을 키워드로', '이미 지나간 30초까지'),
         ('카페 1:1 미팅', '기기 안에서 처리', 'AI 노이즈 제거'),
         ('끝난 뒤', '녹음한 언어 그대로', '녹음마다 AI 요약'),
         ('지우거나 잃어버려도', '클라우드 백업', '복구')]),
 'en': ('HOW-TO · MEETINGS', 'How to record a meeting on your phone', 'From the words before you pressed record to the summary.', 'In-person meetings · TalkSafe',
        [('Start', "the chair's words as a keyword", 'plus the 30 s already gone'),
         ('Café one-to-one', 'processed on the phone', 'AI noise removal'),
         ('Afterwards', 'in the language spoken', 'AI summary'),
         ('Deleted or lost', 'cloud backup', 'restore')]),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for lang, (eyebrow, title, sub, cap, rows) in C.items():
        if only and lang not in only:
            continue
        t = dict(eyebrow=eyebrow, title=title, sub=sub, tagline=SUM[lang][3], panel=panel_text, cap=cap, rows=rows)
        extra = HI_CSS if lang == 'hi' else ("body{font-family:'Yu Gothic','Segoe UI',sans-serif;word-break:normal;line-break:strict}" if lang == 'ja' else '')
        render({('meeting-recording', lang): t}, CSS + TXT_CSS + '.left{min-width:0}.right{min-width:0}.title{font-size:52px}' + extra)
