"""Contribution gate: DCO syntax, immutable snapshots, and scoped review evidence.

This does not establish scientific validity or prove that an authorization claim
is true. GitHub protections and accountable human stewardship remain necessary.
"""
import json, os, re, subprocess, urllib.request
from pathlib import Path

SIGNOFF = re.compile(r'^Signed-off-by: [^<>\n]+ <[^<>\s]+@[^<>\s]+>$', re.MULTILINE)

def require_signoffs(commits):
    missing=[sha for sha,message in commits if not SIGNOFF.search(message)]
    if missing:raise ValueError('Missing valid DCO sign-off: '+', '.join(missing))

def classify_changes(paths, existing_release_dirs, declared):
    if declared not in ('maintenance','normative'):raise ValueError('Declare Change-Class: maintenance or normative in the PR body')
    requires_independent=declared=='normative'
    roots={'package.json','package-lock.json','playwright.config.js','.gitattributes','.gitignore','requirements-ci.txt','requirements-site.txt','CITATION.cff'}
    for path in paths:
        parts=path.split('/')
        if len(parts)>1 and parts[0]=='releases':
            if parts[1] in existing_release_dirs:raise ValueError('Frozen release path changed: '+path)
            requires_independent=True
        elif not (path.startswith(('scripts/','tests/','site/','.github/')) or path in roots or ('/' not in path and path.endswith('.md'))):
            requires_independent=True
    return requires_independent

def has_trusted_approval(reviews, author, head):
    latest={}
    for review in sorted(reviews,key=lambda r:r['id']):
        if review['state'] in ('APPROVED','CHANGES_REQUESTED','DISMISSED'):
            latest[review['user']['login']]=review
    return any(r['state']=='APPROVED' and r.get('commit_id')==head
               and login!=author and r['user'].get('type')=='User'
               and r.get('author_association') in ('OWNER','MEMBER','COLLABORATOR')
               for login,r in latest.items())

def git(*args):return subprocess.check_output(['git',*args]).decode('utf-8').strip()

def main():
    event=json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text(encoding='utf-8'))
    pr=event['pull_request'];base=pr['base']['sha'];head=pr['head']['sha'];body=pr.get('body') or ''
    commits=[(sha,git('show','-s','--format=%B',sha)) for sha in git('rev-list',base+'..'+head).splitlines()]
    if not commits:raise ValueError('No PR commits found')
    require_signoffs(commits)
    paths=git('diff','--name-only','--no-renames',base,head).splitlines()
    release_files=git('ls-tree','-r','--name-only',base,'--','releases/').splitlines()
    existing={x.split('/')[1] for x in release_files if len(x.split('/'))>2}
    match=re.search(r'^Change-Class:\s*(maintenance|normative)\s*$',body,re.MULTILINE)
    independent=classify_changes(paths,existing,match.group(1) if match else None)
    author=pr['user']['login'];owner=event['repository']['owner']['login']
    if independent or author!=owner:
        # Read-only API request; head code receives no write token or account secrets.
        reviews=[];page=1
        while True:
            url=f'https://api.github.com/repos/{os.environ["GITHUB_REPOSITORY"]}/pulls/{pr["number"]}/reviews?per_page=100&page={page}'
            req=urllib.request.Request(url,headers={'Authorization':'Bearer '+os.environ['GITHUB_TOKEN'],'Accept':'application/vnd.github+json','User-Agent':'RippleLogic-contribution-check'})
            with urllib.request.urlopen(req,timeout=30) as response:batch=json.load(response)
            reviews.extend(batch)
            if len(batch)<100:break
            page+=1
        if not has_trusted_approval(reviews,author,head):raise ValueError('An approving review of this exact head from a different trusted human is required')
        review_mode='trusted non-author approval on exact head'
    else:
        if not re.search(r'^Owner-Authorization:\s*\S.+$',body,re.MULTILINE):raise ValueError('Owner maintenance PRs must reference their authorization record')
        review_mode='owner-authorized maintenance; authorization is a recorded human responsibility, not independently proved by CI'
    print(json.dumps({'signed_off_commits':len(commits),'changed_paths':len(paths),'existing_release_paths_unchanged':True,'review_mode':review_mode},indent=2))

if __name__=='__main__':main()
