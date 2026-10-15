"""직업·용도 글 표지 이미지.

사용법: /c/Users/user/miniconda3/python.exe _tools/og/og_work.py [ref ...]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from og_gen import render
from og_law import panel_rules, CSS

CARDS = {
 ('interview-recording', 'ko'): (dict(eyebrow='직업 · 탐문과 면담', title='탐문 중에 녹음기를 꺼내면 대화가 끝납니다', sub='탐정·형사·기자·조사원을 위한 기록법.', tagline='키워드로 시작되는 녹음 앱', panel=panel_rules,
     cap='탐문 중 녹음', rows=[
       ('녹음기를 탁자에 꺼낸다', '상대가 기록용으로 말을 고른다', False),
       ('대화 중 휴대폰을 꺼내 버튼', '그 동작이 대화를 끊는다', False),
       ('상대가 꺼낼 말을 키워드로', '손대지 않고 시작 + 직전 30초', True),
       ('내가 없는 자리의 대화', '누가 해도 범죄 — 통비법 16조', False)]), '.title{font-size:54px}'),
 ('interview-recording', 'en'): (dict(eyebrow='WORK · INTERVIEWS', title='Put a recorder on the table and the interview changes', sub='For investigators, detectives, journalists and adjusters.', tagline='KEYWORD-TRIGGERED RECORDER', panel=panel_rules,
     cap='Recording an interview', rows=[
       ('Recorder on the table', 'they start speaking for the record', False),
       ('Reaching for the phone mid-talk', 'the gesture breaks the conversation', False),
       ('Their likely word as the keyword', 'hands off, plus the 30 seconds before', True),
       ("A conversation you're not in", 'off limits for everyone — § 2511(1)', False)]), '.title{font-size:50px}'),
}

if __name__ == '__main__':
    only = set(sys.argv[1:])
    for key, (t, extra) in CARDS.items():
        if only and key[0] not in only:
            continue
        render({key: t}, CSS + '.left{min-width:0}.right{min-width:0}' + extra)
