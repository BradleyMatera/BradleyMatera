from pathlib import Path
from html import escape
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'readme'
README = ROOT / 'README.md'
OUT.mkdir(parents=True, exist_ok=True)

BLUE='#58a6ff'; GREEN='#7ee787'; PURPLE='#d2a8ff'; ORANGE='#ffb86b'
BASE_DEFS='''
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#07111f"><animate attributeName="stop-color" values="#07111f;#101638;#07111f" dur="9s" repeatCount="indefinite"/></stop>
      <stop offset="48%" stop-color="#102a56"><animate attributeName="stop-color" values="#102a56;#173b68;#102a56" dur="11s" repeatCount="indefinite"/></stop>
      <stop offset="100%" stop-color="#28104f"><animate attributeName="stop-color" values="#28104f;#123f61;#28104f" dur="13s" repeatCount="indefinite"/></stop>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#58a6ff"/><stop offset="0.5" stop-color="#7ee787"/><stop offset="1" stop-color="#d2a8ff"/></linearGradient>
    <radialGradient id="glow"><stop offset="0" stop-color="#58a6ff" stop-opacity="0.30"/><stop offset="1" stop-color="#58a6ff" stop-opacity="0"/></radialGradient>
    <filter id="softGlow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#8b949e" stroke-opacity="0.065" stroke-width="1"/></pattern>
  </defs>'''
FONT='ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace'

def section_svg(title,kicker,subtitle,glyph,accent):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="158" viewBox="0 0 1200 158" role="img" aria-label="{escape(title)}">
{BASE_DEFS}
<rect width="1200" height="158" rx="22" fill="url(#bg)"/><rect width="1200" height="158" rx="22" fill="url(#grid)"/>
<circle cx="1095" cy="20" r="170" fill="url(#glow)"><animate attributeName="cx" values="1095;1010;1095" dur="10s" repeatCount="indefinite"/></circle>
<rect x="20" y="20" width="1118" height="118" rx="17" fill="#0d1117" fill-opacity="0.38" stroke="#30363d"/>
<rect x="47" y="42" width="74" height="74" rx="17" fill="#0d1117" fill-opacity="0.8" stroke="{accent}" stroke-opacity="0.8"/>
<text x="84" y="89" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="24" font-weight="700">{escape(glyph)}</text>
<text x="148" y="57" fill="#8b949e" font-family="{FONT}" font-size="14" letter-spacing="2">{escape(kicker.upper())}</text>
<text x="148" y="95" fill="#f0f6fc" font-family="{FONT}" font-size="32" font-weight="700">{escape(title)}</text>
<text x="148" y="122" fill="#c9d1d9" font-family="{FONT}" font-size="15">{escape(subtitle)}</text>
<rect x="148" y="132" width="360" height="3" rx="2" fill="url(#accent)"><animate attributeName="width" values="130;360;130" dur="7s" repeatCount="indefinite"/></rect>
<g fill="none" stroke="{accent}" stroke-width="1.5" opacity="0.65"><path d="M830 55H902L934 87H1012L1042 57H1132" stroke-dasharray="5 8"><animate attributeName="stroke-dashoffset" values="0;-52" dur="4s" repeatCount="indefinite"/></path><path d="M866 108H935L960 83H1030L1058 108H1112" stroke="#d2a8ff" stroke-dasharray="4 9"><animate attributeName="stroke-dashoffset" values="0;52" dur="5s" repeatCount="indefinite"/></path></g>
<g filter="url(#softGlow)"><circle cx="934" cy="87" r="4" fill="#7ee787"><animate attributeName="r" values="3;6;3" dur="2.7s" repeatCount="indefinite"/></circle><circle cx="1042" cy="57" r="4" fill="#d2a8ff"><animate attributeName="r" values="4;7;4" dur="3.3s" repeatCount="indefinite"/></circle></g>
</svg>'''

def nav_svg(label,sublabel,glyph,accent):
    w=278
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="86" viewBox="0 0 {w} 86" role="img" aria-label="{escape(label)}">
{BASE_DEFS}<rect x="1" y="1" width="276" height="84" rx="17" fill="#0d1117" stroke="#30363d" stroke-width="2"/><rect x="1" y="1" width="276" height="84" rx="17" fill="url(#grid)" opacity="0.55"/>
<rect x="17" y="17" width="52" height="52" rx="13" fill="{accent}" fill-opacity="0.10" stroke="{accent}" stroke-opacity="0.70"/>
<text x="43" y="51" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="16" font-weight="700">{escape(glyph)}</text>
<text x="82" y="37" fill="#f0f6fc" font-family="{FONT}" font-size="17" font-weight="700">{escape(label)}</text><text x="82" y="58" fill="#8b949e" font-family="{FONT}" font-size="12">{escape(sublabel)}</text>
<path d="M240 35L252 43L240 51" fill="none" stroke="{accent}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><animate attributeName="transform" values="translate(0 0);translate(4 0);translate(0 0)" dur="2.2s" repeatCount="indefinite"/></path>
<rect x="82" y="67" width="76" height="2" rx="1" fill="{accent}" opacity="0.75"><animate attributeName="width" values="34;76;34" dur="4.5s" repeatCount="indefinite"/></rect></svg>'''

def snapshot_svg():
    cards=[(55,68,'01','EDUCATION','B.S. Web Development','Full Sail · Oct 2025',BLUE),(610,68,'02','CLOUD','AWS Support Engineering','Seattle · 12 weeks · 2025',ORANGE),(55,210,'03','CERTIFICATIONS','AWS SAA + AI Practitioner','Cloud architecture + AI fundamentals',PURPLE),(610,210,'04','BACKGROUND','U.S. Army Combat Veteran','Former 82nd Airborne Combat Medic',GREEN)]
    parts=[]
    for x,y,num,kicker,title,sub,accent in cards:
        parts.append(f'''<g><rect x="{x}" y="{y}" width="535" height="116" rx="18" fill="#0d1117" fill-opacity="0.72" stroke="#30363d"/><rect x="{x+18}" y="{y+18}" width="46" height="46" rx="12" fill="{accent}" fill-opacity="0.12" stroke="{accent}" stroke-opacity="0.70"/><text x="{x+41}" y="{y+48}" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="15" font-weight="700">{num}</text><text x="{x+82}" y="{y+33}" fill="#8b949e" font-family="{FONT}" font-size="11" letter-spacing="1.7">{kicker}</text><text x="{x+82}" y="{y+60}" fill="#f0f6fc" font-family="{FONT}" font-size="20" font-weight="700">{escape(title)}</text><text x="{x+82}" y="{y+85}" fill="#c9d1d9" font-family="{FONT}" font-size="13">{escape(sub)}</text><rect x="{x+82}" y="{y+96}" width="120" height="2" rx="1" fill="{accent}" opacity="0.72"><animate attributeName="width" values="44;120;44" dur="6s" repeatCount="indefinite"/></rect></g>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360" role="img" aria-label="Professional snapshot">{BASE_DEFS}<rect width="1200" height="360" rx="24" fill="url(#bg)"/><rect width="1200" height="360" rx="24" fill="url(#grid)"/><circle cx="1080" cy="30" r="180" fill="url(#glow)"><animate attributeName="cx" values="1080;960;1080" dur="12s" repeatCount="indefinite"/></circle><text x="55" y="40" fill="#8b949e" font-family="{FONT}" font-size="14">$ snapshot --professional</text>{''.join(parts)}<path d="M590 112V312" stroke="#30363d" stroke-dasharray="4 8" opacity="0.55"/></svg>'''

def skills_svg():
    groups=[('WEB + APP',['JavaScript','TypeScript','React','Next.js','Node.js','Express','HTML','CSS'],BLUE),('CLOUD + INFRA',['AWS Lambda','DynamoDB','S3','CloudFront','Amplify','Docker'],ORANGE),('WORKFLOW',['Git','GitHub','VS Code','Postman','Issues','Docs'],GREEN),('AI-ASSISTED',['Prompt design','Grounded retrieval','LLM routing','Evaluation','Validation','AI coding'],PURPLE)]
    xs=[45,325,605,885]; boxes=[]
    for x,(title,items,accent) in zip(xs,groups):
        if title=='AI-ASSISTED': a=' • '.join(items[:2]); b=' • '.join(items[2:4]); c=' • '.join(items[4:])
        else: a=' • '.join(items[:3]); b=' • '.join(items[3:6]); c=' • '.join(items[6:]) or 'systems • support'
        boxes.append(f'''<g><rect x="{x}" y="72" width="250" height="198" rx="18" fill="#0d1117" fill-opacity="0.74" stroke="#30363d"/><circle cx="{x+27}" cy="98" r="6" fill="{accent}" filter="url(#softGlow)"><animate attributeName="r" values="4;7;4" dur="3s" repeatCount="indefinite"/></circle><text x="{x+44}" y="103" fill="{accent}" font-family="{FONT}" font-size="13" font-weight="700">{title}</text><path d="M{x+22} 121H{x+228}" stroke="#30363d"/><text x="{x+22}" y="151" fill="#f0f6fc" font-family="{FONT}" font-size="12">{escape(a)}</text><text x="{x+22}" y="181" fill="#c9d1d9" font-family="{FONT}" font-size="12">{escape(b)}</text><text x="{x+22}" y="211" fill="#8b949e" font-family="{FONT}" font-size="11">{escape(c)}</text><rect x="{x+22}" y="238" width="120" height="3" rx="2" fill="{accent}" opacity="0.75"><animate attributeName="width" values="38;175;38" dur="6s" repeatCount="indefinite"/></rect></g>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="310" viewBox="0 0 1200 310" role="img" aria-label="Core skills matrix">{BASE_DEFS}<rect width="1200" height="310" rx="24" fill="url(#bg)"/><rect width="1200" height="310" rx="24" fill="url(#grid)"/><text x="45" y="40" fill="#8b949e" font-family="{FONT}" font-size="14">$ skills --matrix --signal=live</text>{''.join(boxes)}<path d="M70 286H1130" stroke="url(#accent)" stroke-width="2" stroke-dasharray="8 12"><animate attributeName="stroke-dashoffset" values="0;-80" dur="4s" repeatCount="indefinite"/></path></svg>'''

def certs_svg():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="Certification highlights">{BASE_DEFS}<rect width="1200" height="300" rx="24" fill="url(#bg)"/><rect width="1200" height="300" rx="24" fill="url(#grid)"/><text x="54" y="42" fill="#8b949e" font-family="{FONT}" font-size="14">$ verify --credentials</text><g><rect x="54" y="70" width="520" height="156" rx="20" fill="#0d1117" fill-opacity="0.76" stroke="#ff9900" stroke-opacity="0.55"/><text x="84" y="110" fill="#ffb86b" font-family="{FONT}" font-size="13" letter-spacing="1.5">AWS CERTIFIED</text><text x="84" y="148" fill="#f0f6fc" font-family="{FONT}" font-size="25" font-weight="700">Solutions Architect - Associate</text><text x="84" y="181" fill="#c9d1d9" font-family="{FONT}" font-size="15">SAA-C03 · July 2025 to July 2028</text><path d="M84 203H494" stroke="#ff9900" stroke-width="3" stroke-dasharray="8 10"><animate attributeName="stroke-dashoffset" values="0;-72" dur="4s" repeatCount="indefinite"/></path></g><g><rect x="626" y="70" width="520" height="156" rx="20" fill="#0d1117" fill-opacity="0.76" stroke="#d2a8ff" stroke-opacity="0.55"/><text x="656" y="110" fill="#d2a8ff" font-family="{FONT}" font-size="13" letter-spacing="1.5">AWS CERTIFIED</text><text x="656" y="148" fill="#f0f6fc" font-family="{FONT}" font-size="25" font-weight="700">AI Practitioner</text><text x="656" y="181" fill="#c9d1d9" font-family="{FONT}" font-size="15">AIF-C01 · August 2025 to August 2028</text><path d="M656 203H1066" stroke="#d2a8ff" stroke-width="3" stroke-dasharray="8 10"><animate attributeName="stroke-dashoffset" values="0;72" dur="4s" repeatCount="indefinite"/></path></g><g transform="translate(54 247)" font-family="{FONT}" font-size="13" fill="#8b949e"><text x="0" y="0">freeCodeCamp x4</text><text x="220" y="0">Microsoft Foundational C#</text><text x="525" y="0" fill="#7ee787">credentials backed by dated records</text></g></svg>'''

def signal_svg():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="74" viewBox="0 0 900 74" role="img" aria-label="Build, test, ship, learn">{BASE_DEFS}<rect x="1" y="1" width="898" height="72" rx="18" fill="#0d1117" stroke="#30363d" stroke-width="2"/><rect x="1" y="1" width="898" height="72" rx="18" fill="url(#grid)" opacity="0.45"/><circle cx="31" cy="37" r="6" fill="#7ee787" filter="url(#softGlow)"><animate attributeName="opacity" values="1;.35;1" dur="1.6s" repeatCount="indefinite"/></circle><text x="52" y="43" fill="#8b949e" font-family="{FONT}" font-size="16">pipeline://</text><g font-family="{FONT}" font-size="18" font-weight="700"><text x="165" y="43" fill="#58a6ff">IDEA</text><text x="224" y="43" fill="#8b949e">&gt;</text><text x="250" y="43" fill="#f0f6fc">BUILD</text><text x="320" y="43" fill="#8b949e">&gt;</text><text x="346" y="43" fill="#d2a8ff">TEST</text><text x="405" y="43" fill="#8b949e">&gt;</text><text x="431" y="43" fill="#7ee787">SHIP</text><text x="490" y="43" fill="#8b949e">&gt;</text><text x="516" y="43" fill="#ffb86b">LEARN</text></g><path d="M628 37H855" stroke="url(#accent)" stroke-width="3" stroke-dasharray="8 11"><animate attributeName="stroke-dashoffset" values="0;-76" dur="3s" repeatCount="indefinite"/></path><circle cx="855" cy="37" r="5" fill="#58a6ff"><animate attributeName="r" values="3;7;3" dur="2.4s" repeatCount="indefinite"/></circle></svg>'''

def footer_svg():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="150" viewBox="0 0 1200 150" role="img" aria-label="Developer footer">{BASE_DEFS}<rect width="1200" height="150" rx="22" fill="url(#bg)"/><rect width="1200" height="150" rx="22" fill="url(#grid)"/><rect x="28" y="28" width="1144" height="94" rx="16" fill="#0d1117" fill-opacity="0.58" stroke="#30363d"/><text x="55" y="62" fill="#8b949e" font-family="{FONT}" font-size="14">$ status --current</text><text x="55" y="95" fill="#f0f6fc" font-family="{FONT}" font-size="21" font-weight="700">Developer. I like turning ideas into things people can click, use, and finish a task with.</text><rect x="55" y="109" width="330" height="3" rx="2" fill="url(#accent)"><animate attributeName="width" values="120;330;120" dur="7s" repeatCount="indefinite"/></rect><g transform="translate(1030 53)" fill="none" stroke="#58a6ff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M0 0L24 20L0 40"/><path d="M42 0L66 20L42 40" opacity=".55"/></g></svg>'''

def img(name,alt,width='100%'):
    return f'<p align="center">\n  <img src="https://raw.githubusercontent.com/BradleyMatera/BradleyMatera/main/assets/readme/{name}" width="{width}" alt="{alt}" />\n</p>'

def transform_readme(text):
    text=re.sub(r'<p align="center">\n  <a href="https://git\.io/typing-svg">.*?</p>',img('signal-strip.svg','Bradley Matera build workflow','92%'),text,count=1,flags=re.S)
    nav='''<p align="center">\n  <a href="https://bradleymatera.dev"><img src="https://raw.githubusercontent.com/BradleyMatera/BradleyMatera/main/assets/readme/nav-website.svg" width="23%" alt="Website" /></a>\n  <a href="https://bradleymatera.dev/work/"><img src="https://raw.githubusercontent.com/BradleyMatera/BradleyMatera/main/assets/readme/nav-work.svg" width="23%" alt="Selected work" /></a>\n  <a href="https://www.linkedin.com/in/bradmatera/"><img src="https://raw.githubusercontent.com/BradleyMatera/BradleyMatera/main/assets/readme/nav-linkedin.svg" width="23%" alt="LinkedIn" /></a>\n  <a href="https://dev.to/bradleymatera"><img src="https://raw.githubusercontent.com/BradleyMatera/BradleyMatera/main/assets/readme/nav-devto.svg" width="23%" alt="DEV.to writing" /></a>\n</p>'''
    text=re.sub(r'<p align="center">\n  <a href="https://bradleymatera\.dev"><img src="https://img\.shields\.io/badge/bradleymatera\.dev-LIVE-.*?</p>',nav,text,count=1,flags=re.S)
    headings={'## 👨‍💻 Developer':img('section-developer.svg','Developer'),'## 💼 Professional technology experience':img('section-experience.svg','Professional technology experience'),'## 🚀 Selected technical projects':img('section-projects.svg','Selected technical projects'),'## 🎓 Education':img('section-education.svg','Education'),'## ✍️ Latest writing':img('section-writing.svg','Latest writing'),'## 📈 Recent public GitHub activity':img('section-activity.svg','Recent public GitHub activity')}
    for old,new in headings.items(): text=text.replace(old,new,1)
    text=re.sub(r'---\n\n## ⚡ Professional snapshot\n\n<table>.*?</table>\n\n<picture>.*?github-profile-summary-cards\.vercel\.app.*?</picture>\n\n---',img('snapshot-overview.svg','Professional snapshot'),text,count=1,flags=re.S)
    exp=img('section-experience.svg','Professional technology experience')
    text=re.sub(r'## 🧰 Core skills\n\n.*?\n---\n\n'+re.escape(exp),img('section-skills.svg','Core skills')+'\n\n'+img('skills-matrix.svg','Core skills matrix')+'\n\n'+exp,text,count=1,flags=re.S)
    text=re.sub(r'## 🏅 Certifications\n\n<p align="center">.*?</p>\n\n<p align="center">.*?</p>\n\n(?=<details>)',img('section-certifications.svg','Certifications')+'\n\n'+img('certifications-board.svg','Certification highlights')+'\n\n',text,count=1,flags=re.S)
    text=re.sub(r'<p align="center">\n  <a href="https://dev\.to/bradleymatera"><img src="https://img\.shields\.io/badge/READ_MORE-DEV\.TO-.*?</p>','<p align="center">\n  <a href="https://dev.to/bradleymatera"><img src="https://raw.githubusercontent.com/BradleyMatera/BradleyMatera/main/assets/readme/nav-devto.svg" width="278" alt="Read more on DEV.to" /></a>\n</p>',text,count=1,flags=re.S)
    text=re.sub(r'<p align="center">\n  <strong>Developer\.</strong><br />\n  I like turning ideas into things people can actually click, use, and finish a task with\.\n</p>',img('footer-terminal.svg','Developer footer'),text,count=1)
    text=re.sub(r'\n---\n\n(?=<p align="center">\n  <img src="https://raw\.githubusercontent\.com/BradleyMatera/BradleyMatera/main/assets/readme/section-)','\n\n',text)
    return text

sections={
 'section-developer.svg':('Developer','identity / approach','How I think about building complete software experiences.','{ }',BLUE),
 'section-skills.svg':('Core Skills','toolbox / systems','Web, cloud, infrastructure, workflow, support, and AI-assisted development.','</>',GREEN),
 'section-experience.svg':('Professional Technology Experience','work / evidence','Hands-on roles, environments, contributions, and operational experience.','::',ORANGE),
 'section-projects.svg':('Selected Technical Projects','build / ship','Inspect real demos, repositories, systems experiments, and learning labs.','[]',PURPLE),
 'section-certifications.svg':('Certifications','credentials / verify','Current cloud and development credentials with dates kept below.','OK',ORANGE),
 'section-education.svg':('Education','foundation / learn','B.S. Web Development plus hands-on clubs, labs, and team projects.','EDU',GREEN),
 'section-writing.svg':('Latest Writing','notes / field-log','What I am building, testing, learning, and changing my mind about.','//',PURPLE),
 'section-activity.svg':('Recent Public GitHub Activity','signal / commits','A live visual of public contribution activity generated from GitHub.','ACT',GREEN),
}
for name,args in sections.items(): (OUT/name).write_text(section_svg(*args),encoding='utf-8')
for name,args in {'nav-website.svg':('WEBSITE','bradleymatera.dev','WWW',BLUE),'nav-work.svg':('SELECTED WORK','projects + demos','<>',GREEN),'nav-linkedin.svg':('LINKEDIN','professional profile','in',BLUE),'nav-devto.svg':('DEV.TO','writing + build logs','//',PURPLE)}.items(): (OUT/name).write_text(nav_svg(*args),encoding='utf-8')
(OUT/'snapshot-overview.svg').write_text(snapshot_svg(),encoding='utf-8')
(OUT/'skills-matrix.svg').write_text(skills_svg(),encoding='utf-8')
(OUT/'certifications-board.svg').write_text(certs_svg(),encoding='utf-8')
(OUT/'signal-strip.svg').write_text(signal_svg(),encoding='utf-8')
(OUT/'footer-terminal.svg').write_text(footer_svg(),encoding='utf-8')
for p in OUT.glob('*.svg'): ET.parse(p)
if README.exists():
    old=README.read_text(encoding='utf-8'); new=transform_readme(old)
    if new!=old: README.write_text(new.rstrip()+'\n',encoding='utf-8')
