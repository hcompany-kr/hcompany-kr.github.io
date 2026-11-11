"""IndexNow로 새 글·고친 글 주소를 검색엔진(Bing, Naver, Seznam, Yandex 등)에 알립니다.

사용법:
  python _tools/indexnow.py --all          # 라이브 sitemap.xml에 있는 모든 주소
  python _tools/indexnow.py --since <sha>  # 그 커밋 이후 추가·수정된 파일의 주소
  python _tools/indexnow.py URL [URL ...]  # 지정한 주소

GitHub Actions(.github/workflows/indexnow.yml)가 Pages 배포가 끝날 때마다 --since로 실행합니다.
표준 라이브러리만 씁니다.
"""
import json, os, re, subprocess, sys, urllib.request

SITE = 'https://hcompany-kr.github.io'
HOST = 'hcompany-kr.github.io'
KEY = 'e0ab0a1ae3a84d58a8c3a4602decad16'
ENDPOINT = 'https://api.indexnow.org/indexnow'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def url_for(path):
    """저장소 안 파일 경로를 공개 주소로 바꿉니다. 해당 없으면 None."""
    path = path.replace('\\', '/')
    m = re.match(r'_posts/\d{4}-\d\d-\d\d-(.+)\.md$', path)
    if m:
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            return None
        head = open(full, encoding='utf-8').read().split('---')[1]
        pm = re.search(r'^permalink:\s*(\S+)', head, re.M)
        return SITE + (pm.group(1) if pm else f'/blog/ko/{m.group(1)}/')
    if path == 'index.html':
        return SITE + '/'
    m = re.match(r'(talksafe|blog)/(?:([a-z-]+)/)?index\.html$', path)
    if m:
        return SITE + f'/{m.group(1)}/' + (f'{m.group(2)}/' if m.group(2) else '')
    return None


def changed_since(sha):
    out = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=AM', sha, 'HEAD'],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    urls = [url_for(p) for p in out.splitlines()]
    return sorted({u for u in urls if u})


def from_sitemap():
    xml = urllib.request.urlopen(SITE + '/sitemap.xml', timeout=30).read().decode('utf-8')
    return re.findall(r'<loc>([^<]+)</loc>', xml)


def submit(urls):
    if not urls:
        print('제출할 주소가 없습니다.')
        return
    for i in range(0, len(urls), 10000):
        batch = urls[i:i + 10000]
        body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': f'{SITE}/{KEY}.txt', 'urlList': batch}).encode('utf-8')
        req = urllib.request.Request(ENDPOINT, data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                print('IndexNow', r.status, len(batch), '개 주소')
        except urllib.error.HTTPError as e:
            print('IndexNow 오류', e.code, e.read()[:300])
            sys.exit(1)
    for u in urls[:50]:
        print(' ', u)


if __name__ == '__main__':
    args = sys.argv[1:]
    if args[:1] == ['--all']:
        submit(from_sitemap())
    elif args[:1] == ['--since']:
        sha = args[1] if len(args) > 1 else ''
        if not sha:
            print('이전 배포 커밋을 찾지 못해 건너뜁니다.')
        else:
            submit(changed_since(sha))
    else:
        submit([a for a in args if a.startswith(SITE)])
