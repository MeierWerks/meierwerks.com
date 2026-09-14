#!/usr/bin/env python3
"""Assemble meierwerks.com from verbatim copy. Every string in COPY traces to a source noted in COPY-SOURCES.md."""
import html, pathlib, hashlib, re
ROOT = pathlib.Path(__file__).parent; SITE = ROOT/"site"
LIVE = pathlib.Path("/Users/meierwerksinc./Desktop/MeierWerks/business/website/_incoming-2026-09-14/live-site-text")

DIVISIONS = [  # name, slug, colour, one-line descriptor (Brand Architecture sheet, Aug 2026), current products
 ("MW Acoustics","acoustics","#0F492B","Audio products, systems and design tools.",["neo-one","sds"]),
 ("MW Heavy","heavy","#D38912","Engineering for demanding physical applications.",[]),
 ("MW Deep Learning","deeplearning","#80843E","AI-enabled products and intelligent systems.",["metagraph"]),
 ("MW Magnetics","magnetics","#9D3F2C","Magnetic technologies and applications.",[]),
 ("MW Composites","composites","#9D8974","Advanced composite materials and systems.",[]),
 ("MW Additive","additive","#145868","Additive design and manufacturing.",[]),
]
DIVISION_SITES = {"acoustics":"https://mwacoustic.com"}  # Bennett 2026-09-14: a division with a live site is clickable through to it
PRODUCTS = {  # Brand Architecture sheet + Brand Guide p.11
 "neo-one": dict(name="NEO • ONE", tag="Premier floor-standing speaker", mark="neo-one-mark.svg", pow=False,
   blurb="A floor-standing speaker of exceptional quality and beauty, created through an agnostic approach to design and engineering—drawing from traditional analogue craft and advanced digital technologies wherever each best serves the sound. The result is outstanding acoustics, distinctive beauty and a singularly expressive listening experience."),
 "sds": dict(name="SDS : Speaker Design Suite", tag="Design your sound. See every decision.", mark="sds-mark.svg", pow=True,
   blurb="SDS turns speaker building into a guided, interactive experience. Explore components and configurations—and see, in real time, how every choice affects cost, performance and the finished result."),
 "metagraph": dict(name="MetaGraph", tag="Coordinate your desktop and all of your AI in one system", mark="mg-mark.svg", pow=True,
   blurb="Connect, clarify and harness your AI tools, apps, information, data and correspondence in one engineered, adaptable and highly usable system."),
}
# Live meierwerks.com/divisions copy, verbatim (headline, paragraphs)
LIVE_DIV = {
 "acoustics": ("A Fresh Take on Audio", ["MW Acoustics develops next generation, hardware and software, including: FOCuS™, innovative horn designs, automated dispersion profile generation through: SONIFoRM™, Automated additive infill profiles optimized for frequency and load FoAM™, and AI-Optimized manufacturing: BRiDG™ that push the boundaries of what’s possible in Audio. All of our technologies, including, ISo–TL™, and THNSeT™ Composites have applications in High End Home Audio, Consumer Electronics, Professional Audio, and beyond."]),
 "magnetics": ("FOCuS™ Hardware & Software.", ["To reduce distortion in our speaker while keeping the source signal purely analog, we had to re-engineer how magnetic motor systems are built. MW-Magnetics develops advanced magnet technologies, including variable field-coil systems, high-energy permanent magnets with novel non linear geometries, leading to precision electromagnetic solutions for industries beyond speakers such as Energy Storage, Transportation, and Industrial Automation."]),
 "composites": ("THNSeT™ composite matrix material for superior performance.", ["A process and formula that delivers greater strength, damping, and cost all while reducing weight, with no compromise in sustainability and scaleability. Ideal for the most demanding applications.","The high-strength, low weight, ultra-low resonance, and sustainable materials required for our speakers had not been invented. We needed to develop our own.","MW-Composites specializes in cutting-edge composite technologies, including high-performance carbon fiber, and thermoset/ thermoplastic matrices. Our innovations extend far beyond Audio, enabling breakthroughs in Aerospace, Automotive and Industrial applications."]),
 "additive": ("Revolutionizing high-performance 3D Printing with our FoAM™ Software.", ["No existing additive processes or materials could deliver the vibration-damping characteristics we needed for our speaker. So, we created it. MW Additive specializes in additive manufacturing Software solutions that combine automated geometries with variable constraints. Our solution works with legacy advanced polymer and metal printing technologies, enabling stronger, lighter, and more precise components for industries including Medical, Aerospace and communications."]),
 "deeplearning": ("AI-driven optimizations for manufacturing and engineering with BRiDG™", ["To improve efficiency and precision in our own processes, we had to develop AI tools and workflows that could design, optimize and scale our innovations. MW Deep-Learning deploys an AI Software hub leveraging LLM agents that can augment existing manufacturing workflows, automate complex engineering challenges, and drive next-generation Industrial Automation all while utilizing legacy digital manufacturing Hardware & Software."]),
 "heavy": ("Industrial Scale Solutions", ["MW-Heavy services Businesses in Energy, Transportation and Infrastructure."]),
}
PRINCIPLES = [  # Brand Guide p.4
 ("Craft is a way of thinking","Material judgment, disciplined execution and respect for how things are made guide every decision."),
 ("Technology must earn its place","Use advanced tools where they improve usefulness, performance, access or understanding—not for novelty."),
 ("Complexity should become clear","Engineering and intelligence should make sophisticated systems easier to use, not harder to understand."),
 ("The system must outlive the moment","Every mark, product and communication belongs to an architecture built to expand without losing itself."),
]
TEAM = [  # live meierwerks.com/team, verbatim
 ("Bennett Meier","team-bennett-meier.jpg","Bennett Meier is the founder and CEO of MeierWerks, a company redefining acoustics, deep learning, material science and manufacturing. With expertise in business management, manufacturing, and business strategy, Bennett has built MeierWerks into a vertically integrated/ United States based domestic manufacturer, developing class leading solutions in: Acoustics, Deep Learning, Additive Manufacturing, Composites, Magnetics and Heavy Industries. Under his leadership, the company is positioning itself as a global leader in post digital manufacturing and next-generation audio technology."),
 ("Roger Shively","team-roger-shively.jpg","Roger Shively brings nearly 40 years of expertise in acoustical engineering, product development, and advanced simulation. He previously served as Chief Engineer for Harman’s North American and Asian acoustic systems divisions. A Purdue alumnus, Roger was awarded the university’s 2022 Outstanding Alumni Award in Engineering Education. Roger is an active member of AES, ASA, SAE, and IEEE, and has published extensively on transducers, psychoacoustics, and computer modeling. Roger holds several patents and currently serves as Co-Chair of the AES Automotive Audio Technical Committee and Chair of the APDA’s Automotive Audio Education Pillar."),
 ("Diane Meier","team-diane-meier.jpg","Diane Meier is a branding expert with a proven track record in corporate direction, market expansion, and high-value brand positioning. As Principal of Meier Advertising, she has guided numerous companies toward growth, investment, and successful exits. Notably, she led the transformation of a disparate group of international factories into Sunworthy, the largest global luxury wall-covering brand, culminating in a $1 billion sale. Diane has advised leading brands across luxury retail, technology, and consumer goods, including Neiman Marcus, Balmain, Condé Nast, Blanc de Chine, and Chopard. Her expertise spans corporate strategy, brand storytelling, and scaling businesses from startup to unicorn status, making her a sought-after consultant for founders, executives, and investors."),
 ("Dr. Maximilian Heres","team-maximilian-heres.jpg","Dr. Maximilian Heres is an accomplished engineer and scientist specializing in advanced manufacturing, additive technologies, and automation. Holding an M.S. in Physics and a Ph.D. in Chemical Engineering from the University of Tennessee, Knoxville, he conducted doctoral research at Oak Ridge National Laboratory, focusing on molecular dynamics in polymers. He played a key role in developing the 3D-printed autonomous shuttle, Olli 2.0, at Local Motors, later co-founding Loci Robotics, Inc., where he designed large-format robotic 3D printers. As founder of Heres 3D, he has provided engineering consulting, prototyping, and manufacturing solutions. A hands-on engineer and automotive enthusiast, Maximilian combines expertise in composites, CNC machining, and digital fabrication to push the boundaries of high-tech manufacturing."),
]
NAV = [("Divisions","divisions.html"),("Principles","principles.html"),("Team","team.html"),("Contact","contact.html")]
E = html.escape

CSS_VER=hashlib.md5((SITE/"assets/styles.css").read_bytes()).hexdigest()[:8]
def shell(title, body, current=None, desc="MeierWerks. Where the craft of work meets advanced technology."):
    CUR=' aria-current="page"'
    nav = "".join(f'<li><a href="{h}"{CUR if h==current else ""}>{E(l)}</a></li>' for l,h in NAV)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="icon" href="assets/logos/mw-circle-black.svg" type="image/svg+xml"><link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"><link rel="icon" type="image/png" sizes="192x192" href="icon-192.png"><link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png"><meta name="theme-color" content="#145868">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700&family=Jost:ital,wght@0,500;1,500&display=swap">
<link rel="stylesheet" href="assets/styles.css?v={CSS_VER}"></head>
<body>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html" aria-label="MeierWerks home"><img class="stamp" src="assets/logos/mw-stamp-white.svg" alt=""><img class="wordmark" src="assets/logos/wordmark-white.svg" alt="MeierWerks"></a>
<nav aria-label="Primary"><ul class="nav">{nav}</ul></nav>
</div></header>
<main>{body}</main>
<footer class="site-footer"><div class="wrap">
<img src="assets/logos/mw-stamp+wordmark-white.svg" alt="MeierWerks">
<div><ul>{"".join(f'<li><a href="{h}">{E(l)}</a></li>' for l,h in NAV)}</ul>
<p class="fine">Kent, CT USA &nbsp;·&nbsp; <a href="mailto:info@meierwerks.com">info@meierwerks.com</a> &nbsp;·&nbsp; (714) 440-5526</p></div>
<div class="right">© MeierWerks Inc. All rights reserved.</div>
</div></footer>
</body></html>'''

def division_tile(d):
    name,slug,c,desc,prods = d
    if prods: p = '<div class="products">Current products: ' + " · ".join(E(PRODUCTS[k]["name"]) for k in prods) + '</div>'
    else: p = ""
    href=DIVISION_SITES.get(slug,f"divisions.html#{slug}"); ext=' target="_blank" rel="noopener"' if slug in DIVISION_SITES else ""
    return f'''<a class="division" href="{href}"{ext}><img class="tile" src="assets/logos/tile-{slug}.svg" alt="">
<div><div class="name">{E(name)}</div><div class="role">Division</div><p>{E(desc)}</p>{p}</div></a>'''

def product_card(k):
    p = PRODUCTS[k]
    img = f'<img src="assets/logos/{p["mark"]}" alt="">' if p["mark"] else ""
    pow_ = '<div class="pow">Powered by WRKS</div>' if p["pow"] else ""
    return f'<div class="product">{img}<div class="pname">{E(p["name"])}</div><div class="ptag">{E(p["tag"])}</div><p>{E(p["blurb"])}</p>{pow_}</div>'

# ---------- Home ----------
home = f'''
<section class="hero"><div class="wrap"><p class="eyebrow">Foundation</p>
<div class="grid"><h1>Where the craft of work meets advanced technology.</h1>
<div class="statement"><p>MeierWerks creates products and systems by joining analog judgment and material intelligence with skilled workmanship and the most advanced technologies.</p><p>Technology is not the identity. It is a tool in service of more thoughtful, useful and beautiful work.</p></div></div></div></section>
<section class="band-teal"><div class="wrap"><p class="eyebrow">Brand architecture</p>
<h2>One ownership brand. Distinct divisions. Products with a clear home.</h2>
<p class="lead" style="margin:18px 0 36px">Every product belongs to one division. Only software carries the WRKS endorsement.</p>
<div class="divisions">{"".join(division_tile(d) for d in DIVISIONS)}</div></div></section>
<section><div class="wrap"><p class="eyebrow">Foundation</p><h2>Four governing principles</h2><hr class="rule" style="margin-bottom:36px">
<div class="principles">{"".join(f'<div class="principle"><div class="num">{i:02d}</div><div><h3>{E(t)}</h3><p>{E(b)}</p></div></div>' for i,(t,b) in enumerate(PRINCIPLES,1))}</div></div></section>
<section class="band-black tight"><div class="wrap wrks"><img src="assets/logos/wrks-color.svg" alt="WRKS"><p><img class="pbw" src="assets/logos/powered-by-wrks-white.svg" alt="Powered by WRKS"><small>WRKS is MeierWerks’ proprietary software engine, deployed across every MW software solution.</small></p></div></section>
'''
# ---------- Divisions ----------
def plain_tiles():
    """tile-{slug}-plain.svg = the delivered tile with its accent band filled in the tile cream (start state of the wipe)"""
    cream='rgb(95.53833%, 93.418884%, 89.089966%)'
    for name,slug,c,desc,prods in DIVISIONS:
        src=(SITE/"assets/logos"/f"tile-{slug}.svg").read_text()
        (SITE/"assets/logos"/f"tile-{slug}-plain.svg").write_text(src.replace(f'fill="{c}"',f'fill="{cream}"',1))
plain_tiles()
divs = []
for name,slug,c,desc,prods in DIVISIONS:
    head, paras = LIVE_DIV[slug]
    prod_html = f'<div class="products-grid">{"".join(product_card(k) for k in prods)}</div>' if prods else ""
    divs.append(f'''<div class="div-section" id="{slug}" data-slug="{slug}"><div>
<div class="mark">{'<a href="'+DIVISION_SITES[slug]+'" target="_blank" rel="noopener" aria-label="'+E(name)+' website">' if slug in DIVISION_SITES else ''}<img class="tile big" src="assets/logos/tile-{slug}.svg" alt=""><canvas class="tile big reel-tile" width="264" height="264" data-plain="assets/logos/tile-{slug}-plain.svg" aria-hidden="true"></canvas><img class="divname" src="assets/logos/division-{slug}-black.svg" alt="{E(name)}">{'</a>' if slug in DIVISION_SITES else ''}</div>
</div>
<div><p class="label">Division</p><h2>{E(name)}</h2><p class="head">{E(head)}</p>{"".join(f"<p>{E(x)}</p>" for x in paras)}
{('<p class="label" style="margin-top:26px">Current products</p>' + prod_html) if prods else ""}</div></div>''')
divisions = f'''<section class="tight"><div class="wrap"><p class="eyebrow">Brand architecture</p><h1 style="font-size:clamp(40px,5.5vw,76px)">The operating structure</h1><hr class="rule"><p class="lead" style="margin-top:18px">Every product belongs to one division. Only software carries the WRKS endorsement.</p></div></section>
<div class="wrap divs-list">{"".join(divs)}</div>
<script>
(function(){{
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;          // static SVG tiles stay
  var DPR=Math.min(3,window.devicePixelRatio||1), N=Math.round(132*DPR), FEATHER=0.05, EASE=0.22;
  var tiles=Array.prototype.slice.call(document.querySelectorAll('canvas.reel-tile'));
  function bitmap(img){{ var c=document.createElement('canvas'); c.width=c.height=N; c.getContext('2d').drawImage(img,0,0,N,N); return c; }}   // rasterise each SVG once
  var off=document.createElement('canvas'); off.width=off.height=N; var ox=off.getContext('2d');
  var items=tiles.map(function(cv){{ cv.width=cv.height=N; var img=cv.previousElementSibling; var plain=new Image(); plain.src=cv.dataset.plain;
    return {{cv:cv,ctx:cv.getContext('2d'),color:img,plain:plain,pb:null,cb:null,p:0,target:0,ready:false}}; }});
  function draw(it,p){{ var c=it.ctx; c.clearRect(0,0,N,N); c.drawImage(it.pb,0,0); if(p<=0) return;
    ox.globalCompositeOperation='source-over'; ox.clearRect(0,0,N,N); ox.drawImage(it.cb,0,0);
    if(p<1){{ var g=ox.createLinearGradient(0,N,N,0); var a=Math.max(0,p-FEATHER); g.addColorStop(0,'rgba(0,0,0,1)'); g.addColorStop(a,'rgba(0,0,0,1)'); g.addColorStop(Math.min(1,p),'rgba(0,0,0,0)'); g.addColorStop(1,'rgba(0,0,0,0)');
      ox.globalCompositeOperation='destination-in'; ox.fillStyle=g; ox.fillRect(0,0,N,N); ox.globalCompositeOperation='source-over'; }}
    c.drawImage(off,0,0); }}
  function progress(it){{ var r=it.cv.getBoundingClientRect(), H=window.innerHeight;
    var atBottom=(window.innerHeight+window.scrollY)>=(document.documentElement.scrollHeight-2); if(atBottom) return 1;
    return Math.min(1,Math.max(0,(H-r.bottom)/(H*0.33))); }}           // 0 = mark just fully on screen at the bottom edge; 1 a third of the screen higher
  var raf=null;
  function frame(){{ raf=null; var moving=false;
    items.forEach(function(it){{ if(!it.ready) return; var d=it.target-it.p; if(Math.abs(d)<0.0015){{ if(it.p!==it.target){{ it.p=it.target; draw(it,it.p); }} return; }}
      it.p+=d*EASE; draw(it,it.p); moving=true; }});
    if(moving) raf=requestAnimationFrame(frame); }}
  function retarget(){{ items.forEach(function(it){{ if(it.ready) it.target=progress(it); }}); if(!raf) raf=requestAnimationFrame(frame); }}
  items.forEach(function(it){{ var n=0; function ok(){{ if(++n<2) return; it.pb=bitmap(it.plain); it.cb=bitmap(it.color); it.ready=true; it.p=it.target=progress(it); draw(it,it.p);
      it.cv.classList.add('on'); it.color.classList.add('hidden'); }}
    it.plain.addEventListener('load',ok,{{once:true}}); if(it.color.complete&&it.color.naturalWidth) ok(); else it.color.addEventListener('load',ok,{{once:true}}); }});
  window.addEventListener('scroll',retarget,{{passive:true}}); window.addEventListener('resize',function(){{ retarget(); }});
}})();
</script>'''
# ---------- Principles ----------
principles = f'''<section class="hero" style="padding-bottom:0"><div class="wrap"><p class="eyebrow">Foundation</p>
<div class="grid"><h1>Where the craft of work meets advanced technology.</h1>
<div class="statement"><p>MeierWerks creates products and systems by joining analog judgment and material intelligence with skilled workmanship and the most advanced technologies.</p><p>Technology is not the identity. It is a tool in service of more thoughtful, useful and beautiful work.</p></div></div></div></section>
<section><div class="wrap"><h2>Four governing principles</h2><hr class="rule" style="margin-bottom:36px">
<div class="principles">{"".join(f'<div class="principle"><div class="num">{i:02d}</div><div><h3>{E(t)}</h3><p>{E(b)}</p></div></div>' for i,(t,b) in enumerate(PRINCIPLES,1))}</div></div></section>
<section class="band-teal"><div class="wrap"><p class="eyebrow">Mission</p><h2>Mission and proof</h2>
<p class="lead" style="margin-top:22px">Using a proprietary method of agnostic pursuit, we aim to deliver B2B/B2C technology, engineered for superior performance, scalability, &amp; innovation across hardware, software, and manufacturing.</p>
<p class="lead">Our first product is a truly remarkable speaker, blending analog and digital technology in ways that deliver extraordinary warmth with the efficiencies of new thinking, new materials, and new processes.</p></div></section>'''
# ---------- Team ----------
team = f'''<section><div class="wrap"><p class="eyebrow">MeierWerks</p><h1 style="font-size:clamp(40px,5.5vw,76px)">Meet the Team</h1><hr class="rule" style="margin-bottom:40px">
<div class="team">{"".join(f'<div class="member"><div class="portrait"><img src="assets/img/{img}" alt="{E(n)}" loading="lazy"></div><div><h3>{E(n)}</h3><p>{E(b)}</p></div></div>' for n,img,b in TEAM)}</div></div></section>'''
# ---------- Contact ----------
contact = '''<section><div class="wrap"><p class="eyebrow">MeierWerks</p><h1 style="font-size:clamp(40px,5.5vw,76px)">Contact</h1><hr class="rule" style="margin-bottom:40px">
<div class="contact"><dl><dt>Location</dt><dd>Kent, CT USA</dd><dt>Email</dt><dd><a href="mailto:info@meierwerks.com">info@meierwerks.com</a></dd><dt>Phone</dt><dd><a href="tel:+17144405526">(714) 440-5526</a></dd></dl>
<form action="mailto:info@meierwerks.com" method="post" enctype="text/plain">
<label>Name<input id="name" name="name" type="text" autocomplete="name" required></label>
<label>Email<input id="email" name="email" type="email" autocomplete="email" required></label>
<label>Subject<input id="subject" name="subject" type="text"></label>
<label>Message<textarea id="message" name="message" rows="6" required></textarea></label>
<button type="submit">Send</button></form></div></div></section>'''
# Privacy page moved to MW Acoustics (owner of SDS) on 2026-09-14 at Bennett's request.

pages = {"index.html":("MeierWerks",home,None),"divisions.html":("Divisions — MeierWerks",divisions,"divisions.html"),
 "principles.html":("Principles — MeierWerks",principles,"principles.html"),"team.html":("Team — MeierWerks",team,"team.html"),
 "contact.html":("Contact — MeierWerks",contact,"contact.html")}
for fn,(t,b,cur) in pages.items(): (SITE/fn).write_text(shell(t,b,cur)); print("built",fn)
