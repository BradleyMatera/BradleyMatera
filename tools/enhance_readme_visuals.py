from pathlib import Path
from html import escape
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'readme'
README = ROOT / 'README.md'
OUT.mkdir(parents=True, exist_ok=True)

BLUE='#58a6ff'; GREEN='#7ee787'; PURPLE='#d2a8ff'; ORANGE='#ffb86b'; RED='#ff7b72'
FONT='ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace'
DEFS='''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#07111f"/><stop offset=".5" stop-color="#102a56"/><stop offset="1" stop-color="#28104f"/></linearGradient>
<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#58a6ff"/><stop offset=".5" stop-color="#7ee787"/><stop offset="1" stop-color="#d2a8ff"/></linearGradient>
<filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#8b949e" stroke-opacity=".06"/></pattern>
</defs>'''

def strip(title, kicker, tags, accent=BLUE, glyph='//'):
    xs=[]; x=430
    for tag in tags:
        w=max(112, min(210, 28 + len(tag)*8))
        if x+w>1140: break
        xs.append((x,w,tag)); x+=w+12
    pills=''.join(f'''<g><rect x="{x}" y="43" width="{w}" height="38" rx="12" fill="{accent}" fill-opacity=".09" stroke="{accent}" stroke-opacity=".55"/><text x="{x+w/2}" y="67" text-anchor="middle" fill="#f0f6fc" font-family="{FONT}" font-size="12">{escape(tag)}</text></g>''' for x,w,tag in xs)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="112" viewBox="0 0 1200 112" role="img" aria-label="{escape(title)} technology strip">{DEFS}
<rect width="1200" height="112" rx="18" fill="url(#bg)"/><rect width="1200" height="112" rx="18" fill="url(#grid)"/><rect x="1" y="1" width="1198" height="110" rx="17" fill="none" stroke="#30363d"/>
<rect x="24" y="25" width="62" height="62" rx="15" fill="#0d1117" fill-opacity=".75" stroke="{accent}" stroke-opacity=".7"/><text x="55" y="63" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="16" font-weight="700">{escape(glyph)}</text>
<text x="108" y="44" fill="#8b949e" font-family="{FONT}" font-size="11" letter-spacing="1.5">{escape(kicker.upper())}</text><text x="108" y="70" fill="#f0f6fc" font-family="{FONT}" font-size="20" font-weight="700">{escape(title)}</text>
{pills}<path d="M108 88H380" stroke="{accent}" stroke-width="2" stroke-dasharray="8 10"><animate attributeName="stroke-dashoffset" values="0;-72" dur="4s" repeatCount="indefinite"/></path><circle cx="1164" cy="56" r="5" fill="{accent}" filter="url(#glow)"><animate attributeName="r" values="3;7;3" dur="2.4s" repeatCount="indefinite"/></circle></svg>'''

def action(label, sub, glyph, accent=BLUE, width=290):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="78" viewBox="0 0 {width} 78" role="img" aria-label="{escape(label)}">{DEFS}<rect x="1" y="1" width="{width-2}" height="76" rx="16" fill="#0d1117" stroke="#30363d" stroke-width="2"/><rect x="15" y="15" width="48" height="48" rx="12" fill="{accent}" fill-opacity=".10" stroke="{accent}" stroke-opacity=".65"/><text x="39" y="45" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="13" font-weight="700">{escape(glyph)}</text><text x="76" y="32" fill="#f0f6fc" font-family="{FONT}" font-size="15" font-weight="700">{escape(label)}</text><text x="76" y="53" fill="#8b949e" font-family="{FONT}" font-size="11">{escape(sub)}</text><path d="M{width-40} 29L{width-28} 39L{width-40} 49" fill="none" stroke="{accent}" stroke-width="2"><animate attributeName="transform" values="translate(0 0);translate(4 0);translate(0 0)" dur="2s" repeatCount="indefinite"/></path></svg>'''

def note(title, lines, accent=PURPLE, glyph='!'):
    text=''.join(f'<text x="120" y="{66+i*24}" fill="{("#f0f6fc" if i==0 else "#c9d1d9")}" font-family="{FONT}" font-size="{15 if i==0 else 13}">{escape(line)}</text>' for i,line in enumerate(lines))
    h=105+max(0,len(lines)-1)*24
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="{escape(title)}">{DEFS}<rect width="1200" height="{h}" rx="18" fill="#0d1117"/><rect width="1200" height="{h}" rx="18" fill="url(#grid)"/><rect x="1" y="1" width="1198" height="{h-2}" rx="17" fill="none" stroke="{accent}" stroke-opacity=".45"/><rect x="28" y="28" width="66" height="66" rx="17" fill="{accent}" fill-opacity=".10" stroke="{accent}" stroke-opacity=".7"/><text x="61" y="70" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="20" font-weight="700">{escape(glyph)}</text><text x="120" y="38" fill="{accent}" font-family="{FONT}" font-size="11" letter-spacing="1.6">{escape(title.upper())}</text>{text}<path d="M1050 55H1150" stroke="{accent}" stroke-width="2" stroke-dasharray="6 9"><animate attributeName="stroke-dashoffset" values="0;-60" dur="3s" repeatCount="indefinite"/></path></svg>'''

def education():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="210" viewBox="0 0 1200 210" role="img" aria-label="Bachelor of Science in Web Development">{DEFS}<rect width="1200" height="210" rx="22" fill="url(#bg)"/><rect width="1200" height="210" rx="22" fill="url(#grid)"/><rect x="28" y="28" width="1144" height="154" rx="18" fill="#0d1117" fill-opacity=".62" stroke="#30363d"/><text x="58" y="62" fill="#7ee787" font-family="{FONT}" font-size="12" letter-spacing="1.8">DEGREE // COMPLETED</text><text x="58" y="104" fill="#f0f6fc" font-family="{FONT}" font-size="28" font-weight="700">B.S. in Web Development</text><text x="58" y="135" fill="#c9d1d9" font-family="{FONT}" font-size="16">Full Sail University · August 2023 to October 2025</text><text x="58" y="162" fill="#8b949e" font-family="{FONT}" font-size="13">interfaces · databases · server-side · cloud · deployment · security · integration · discrete math</text><g transform="translate(930 66)"><circle cx="60" cy="40" r="38" fill="#7ee787" fill-opacity=".08" stroke="#7ee787" stroke-opacity=".55"/><text x="60" y="47" text-anchor="middle" fill="#7ee787" font-family="{FONT}" font-size="19" font-weight="700">B.S.</text><circle cx="60" cy="40" r="48" fill="none" stroke="#58a6ff" stroke-dasharray="6 9"><animate attributeName="stroke-dashoffset" values="0;-60" dur="5s" repeatCount="indefinite"/></circle></g></svg>'''

def img(name, alt, width='100%'):
    return f'<p align="center">\n  <img src="https://raw.githubusercontent.com/BradleyMatera/BradleyMatera/main/assets/readme/{name}" width="{width}" alt="{alt}" />\n</p>'

def actions(url1, image1, alt1, url2=None, image2=None, alt2=None):
    bits=[f'<a href="{url1}"><img src="https://raw.githubusercontent.com/BradleyMatera/BradleyMatera/main/assets/readme/{image1}" width="290" alt="{alt1}" /></a>']
    if url2: bits.append(f'<a href="{url2}"><img src="https://raw.githubusercontent.com/BradleyMatera/BradleyMatera/main/assets/readme/{image2}" width="290" alt="{alt2}" /></a>')
    return '<p align="center">\n  '+'\n  '.join(bits)+'\n</p>'

PROJECTS={
 'Car-Match':('project-car-match.svg','React + Express + Cloud Run',['React','Express','Cloud Run','MongoDB'],BLUE,'CAR'),
 'ProjectHub / Scout':('project-scout.svg','AI systems experiment',['Node.js','Express','BM25 + RRF','AI-assisted'],PURPLE,'AI'),
 'Interactive Pokédex':('project-pokedex.svg','Next.js static application',['Next.js 16','PokeAPI','GitHub Actions'],RED,'DEX'),
 'AnimalSounds':('project-animal-sounds.svg','offline-ready soundboard',['Next.js 14','Bun','offline-ready'],GREEN,'SFX'),
 'Convo-AI':('project-convo-ai.svg','local-first voice assistant',['FastAPI','Ollama','WebSockets','Docker'],PURPLE,'VOX'),
 'Triangle Shader Lab':('project-triangle.svg','WebGPU learning lab',['WebGPU','WGSL editor','16 lessons'],PURPLE,'GPU'),
 'SecureLearn LMS':('project-securelearn.svg','TypeScript learning-management demo',['TypeScript','Next.js 15','security training'],RED,'LMS'),
 'CheeseMath':('project-cheesemath.svg','calculator + testing suite',['Next.js 16','TypeScript','Jest','Selenium'],ORANGE,'TST'),
 'AWS Serverless Metadata Workflow':('project-aws-metadata.svg','internship capstone + public reconstruction',['Lambda','S3','DynamoDB','AWS SAM'],ORANGE,'AWS'),
}

for title,(name,kicker,tags,accent,glyph) in PROJECTS.items():
    (OUT/name).write_text(strip(title,kicker,tags,accent,glyph),encoding='utf-8')
(OUT/'experience-aws.svg').write_text(strip('AWS Support Engineering Intern','professional experience',['Seattle','12 weeks','training + labs','cloud support'],ORANGE,'AWS'),encoding='utf-8')
(OUT/'experience-ciris.svg').write_text(strip('CIRIS Ethical AI','frontend contribution',['10 PRs submitted','7 merged','Docker Compose','JWT debugging'],PURPLE,'PR'),encoding='utf-8')
(OUT/'action-live.svg').write_text(action('OPEN LIVE','deployed experience','RUN',GREEN),encoding='utf-8')
(OUT/'action-github.svg').write_text(action('VIEW SOURCE','repository on GitHub','GIT',BLUE),encoding='utf-8')
(OUT/'action-walkthrough.svg').write_text(action('OPEN WALKTHROUGH','public project guide','DOC',ORANGE),encoding='utf-8')
(OUT/'action-pull-requests.svg').write_text(action('VIEW PULL REQUESTS','inspect CIRIS contributions','PR',PURPLE,330),encoding='utf-8')
(OUT/'project-context.svg').write_text(note('Project inventory',['These are projects deliberately kept in my professional inventory.','AI assistance varies. The links point to software, demos, or repositories people can inspect.'],PURPLE,'i'),encoding='utf-8')
(OUT/'activity-context.svg').write_text(note('Activity context',['I build and experiment frequently.','Commit volume is not a measurement of seniority, code quality, or how much was written without AI assistance.'],GREEN,'i'),encoding='utf-8')
(OUT/'education-overview.svg').write_text(education(),encoding='utf-8')
for p in OUT.glob('*.svg'): ET.parse(p)

if README.exists():
    text=README.read_text(encoding='utf-8')
    # Finish the education conversion missed by the first generator.
    text=text.replace('## 🎓 Education',img('section-education.svg','Education'),1)
    text=re.sub(r'### Bachelor of Science in Web Development · Full Sail University\n\n`August 2023 → October 2025`',img('education-overview.svg','Bachelor of Science in Web Development'),text,count=1)
    # Replace the remaining third-party badge clusters in professional experience.
    text=re.sub(r'<img src="https://img\.shields\.io/badge/AWS-Support_Engineering-.*?\n<img src="https://img\.shields\.io/badge/ENVIRONMENT-Training_%26_Labs-.*?\n',img('experience-aws.svg','AWS Support Engineering experience')+'\n',text,count=1)
    text=re.sub(r'<img src="https://img\.shields\.io/badge/10_PULL_REQUESTS-SUBMITTED-.*?\n<img src="https://img\.shields\.io/badge/7-MERGED-.*?\n',img('experience-ciris.svg','CIRIS Ethical AI contribution activity')+'\n',text,count=1)
    # Replace project badge clusters with custom animated technology strips.
    for title,(name,_,_,_,_) in PROJECTS.items():
        marker=re.escape(f'<summary><strong>')+r'.*?'+re.escape(title)+r'.*?</summary>\n<br />\n\n'
        m=re.search(marker,text)
        if not m: continue
        start=m.end(); tail=text[start:]
        badge_block=re.match(r'(?:<img src="https://img\.shields\.io/[^\n]+\n)+\n?',tail)
        if badge_block:
            text=text[:start]+img(name,f'{title} technology stack')+'\n\n'+tail[badge_block.end():]
    # Replace action text links with reusable custom clickable SVG controls.
    pairs=[
      ('https://bradleymatera.github.io/car-match/','https://github.com/BradleyMatera/car-match'),
      ('https://bradleymatera.github.io/ProjectHub/','https://github.com/BradleyMatera/ProjectHub'),
      ('https://bradleymatera.github.io/Interactive-Pokedex/','https://github.com/BradleyMatera/Interactive-Pokedex'),
      ('https://bradleymatera.github.io/AnimalSounds/','https://github.com/BradleyMatera/AnimalSounds'),
      ('https://bradleymatera.github.io/Convo-Ai/','https://github.com/BradleyMatera/Convo-Ai'),
      ('https://bradleymatera.github.io/TriangleDemo/','https://github.com/BradleyMatera/TriangleDemo'),
      ('https://bradleymatera.github.io/EthicsFrontEndDemo/','https://github.com/BradleyMatera/EthicsFrontEndDemo'),
      ('https://bradleymatera.github.io/CheeseMath-Jest-Tests/','https://github.com/BradleyMatera/CheeseMath-Jest-Tests'),
    ]
    for live,repo in pairs:
        old=f'**[▶ Live]({live})** · **[⌘ GitHub]({repo})**'
        text=text.replace(old,actions(live,'action-live.svg','Open live project',repo,'action-github.svg','View GitHub repository'),1)
    old='**[▶ Walkthrough](https://bradleymatera.github.io/AWS-Serverless-Metadata-Workflow/)** · **[⌘ GitHub](https://github.com/BradleyMatera/AWS-Serverless-Metadata-Workflow)**'
    text=text.replace(old,actions('https://bradleymatera.github.io/AWS-Serverless-Metadata-Workflow/','action-walkthrough.svg','Open project walkthrough','https://github.com/BradleyMatera/AWS-Serverless-Metadata-Workflow','action-github.svg','View GitHub repository'),1)
    text=text.replace('**[View my CIRISNode pull requests →](https://github.com/CIRISAI/CIRISNode/pulls?q=is%3Apr+author%3ABradleyMatera)**',actions('https://github.com/CIRISAI/CIRISNode/pulls?q=is%3Apr+author%3ABradleyMatera','action-pull-requests.svg','View CIRIS pull requests'),1)
    # Replace informational blockquotes with designed callout panels.
    text=text.replace('> **How to read this section:** these are projects I deliberately keep in my professional project inventory. Some were built with substantial AI assistance. The links are here because the resulting software, demos, or repositories are things people can actually inspect.',img('project-context.svg','Project inventory context'),1)
    text=text.replace('> **Context:** I build and experiment frequently. Commit volume is not a measurement of seniority, code quality, or how much of a project was written without AI assistance.',img('activity-context.svg','GitHub activity context'),1)
    README.write_text(text.rstrip()+'\n',encoding='utf-8')
