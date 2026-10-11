#!/usr/bin/env python3
"""Generates the static pages for the Eminiyeza Dreamlife website.

Run:  python build.py
Edit copy / contact details in the CONFIG + page functions below, then re-run.
Output is plain HTML in this folder — no server, framework or build step needed to host it.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ CONFIG
ORG = "Eminiyeza Dreamlife"
EMAIL = "masihiyuaja@gmail.com"
PHONE_DISPLAY = "+27 (0) 60 985 1907"
PHONE_TEL = "+27609851907"
ADDRESS = "17681 Vuyani Street, Bongolethu, 6625"
MAPS = "https://www.google.com/maps/search/?api=1&query=17681+Vuyani+Street+Bongolethu+6625"
FACEBOOK = "https://facebook.com/groups/1527069571787101"
CONTACT_PERSON = "Mr. Samuel Kasereka Misemengo"
FORM_ENDPOINT = "https://formsubmit.co/ajax/" + EMAIL
TAGLINE = "Building the economics of humanity, healing and permanence through tourism and hospitality in the family of the nations."

# ------------------------------------------------------------------ ICONS (Lucide-style, 24px grid)
ICONS = {
    "map": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "cap": '<path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 8v6M9 11h6"/>',
    "landmark": '<path d="M3 22h18M6 18v-7M10 18v-7M14 18v-7M18 18v-7M12 2 3 7h18z"/>',
    "sprout": '<path d="M7 20h10M12 20v-9"/><path d="M12 11c0-4-3-6-7-6 0 4 3 6 7 6zM12 11c0-3 2-5 6-5 0 3-2 5-6 5z"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "heart": '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.7 0-3 .8-4.5 2.5C10.5 3.8 9.2 3 7.5 3A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
    "star": '<path d="m12 2 2.9 6.9L22 10l-5.5 4.8L18.2 22 12 18.3 5.8 22l1.7-7.2L2 10l7.1-1.1z"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "coins": '<circle cx="8" cy="8" r="6"/><path d="M18.1 10.4A6 6 0 1 1 10.4 18.1M7 6h1v4"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
}


def icon(name, cls="icon"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'


NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "What We Do"),
    ("get-involved.html", "Get Involved"),
    ("blog.html", "Blog"),
    ("contact.html", "Contact"),
]

# ------------------------------------------------------------------ SHELL
def shell(filename, title, desc, body, og_image="assets/img/hero-mountains.webp", extra_head=""):
    nav_links = "\n".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == filename else ""}>{label}</a>'
        for href, label in NAV[:-1]
    )
    contact_cur = ' aria-current="page"' if filename == "contact.html" else ""
    full_title = f"{title} | {ORG}" if title != ORG else f"{ORG} | Tourism, Culture & Skills Development"
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#143d0c">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{ORG}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_image}">
<link rel="icon" type="image/png" href="assets/img/emblem.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,700;1,9..40,400&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="{ORG} — home"><img src="assets/img/logo.png" alt="{ORG}" width="607" height="195"></a>
    <button class="menu-toggle" aria-label="Menu" aria-expanded="false" aria-controls="site-nav"><svg viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
    <nav class="nav" id="site-nav" aria-label="Main">
{nav_links}
<a class="btn" href="contact.html"{contact_cur}>Partner With Us</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def footer():
    links = "\n".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img src="assets/img/logo-white.png" alt="{ORG}" width="607" height="195">
        <p>A non-profit company working through tourism, cultural experiences and skills development. Self-made, politically independent and guided by the Sustainable Development Goals.</p>
        <div class="social"><a href="{FACEBOOK}" aria-label="{ORG} on Facebook" target="_blank" rel="noopener">{icon("facebook")}</a></div>
      </div>
      <div><h4>Explore</h4><ul>
{links}
</ul></div>
      <div><h4>What We Do</h4><ul>
<li><a href="services.html#tourism">Heritage &amp; tourism</a></li>
<li><a href="services.html#skills">Skills for youth</a></li>
<li><a href="services.html#languages">Languages</a></li>
<li><a href="services.html#resilience">Community resilience</a></li>
<li><a href="get-involved.html">Funding &amp; networking</a></li>
</ul></div>
      <div><h4>Contact</h4><ul>
<li>{icon("map")}<span>{ADDRESS}</span></li>
<li>{icon("phone")}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
<li>{icon("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
</ul></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> {ORG} NPC. All rights reserved.</span>
      <span>Registered NPO 192-961 NPO</span>
    </div>
  </div>
</footer>"""


def newsletter():
    return f"""<section style="padding-block:0 96px">
  <div class="wrap">
    <div class="newsletter reveal">
      <div>
        <h2>Stay close to the work</h2>
        <p>Programme updates, funding calls and stories from the community, sent to your inbox. No noise, unsubscribe any time.</p>
      </div>
      <form class="news-form-wrap" data-ajax data-endpoint="{FORM_ENDPOINT}" data-fallback="{EMAIL}" data-success="Thank you — you are on the list." novalidate style="position:relative;z-index:1">
        <div class="news-form">
          <label class="sr" for="nl-email" style="position:absolute;left:-9999px">Email address</label>
          <input id="nl-email" type="email" name="email" placeholder="Your email address" autocomplete="email" required>
          <div class="hp" aria-hidden="true"><input type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
          <input type="hidden" name="_subject" value="Newsletter signup — Eminiyeza Dreamlife website">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="form" value="Newsletter">
          <button class="btn" type="submit">Subscribe</button>
        </div>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>"""


# ------------------------------------------------------------------ BLOG DATA
POSTS = [
    {
        "slug": "why-cultural-tourism-builds-communities",
        "title": "Why cultural tourism builds stronger communities",
        "tag": "Tourism",
        "img": "assets/img/ridge-view.webp",
        "excerpt": "When visitors come for the heritage, nature and stories of a place, the benefit can stay with the people who live there.",
        "body": [
            "<p>Tourism is often measured in arrivals and bed-nights. At Eminiyeza Dreamlife we prefer a different measure: what is left behind in the community once the visitors have gone home.</p>",
            "<h2>Heritage as a living resource</h2>",
            "<p>Songs, crafts, food, landmarks and the stories told by elders are not museum pieces. They are a living resource, and when they are shared with pride and respect they create work, keep traditions alive and give young people a reason to know their own history.</p>",
            "<h2>Hospitality is a skill that can be taught</h2>",
            "<p>Guiding, languages, first aid, booking and basic administration are all learnable. That is why our tourism work and our skills work are one effort, not two. A young person who can welcome a visitor in their language, keep them safe and manage a simple booking has a career, not just a job.</p>",
            "<blockquote>Tourism done well is a way of building a better tomorrow for everyone involved.</blockquote>",
            "<h2>Serving with pride</h2>",
            "<p>Our principle is simple: anyone who is ready to serve with pride is welcome. If you would like to take part in, fund or promote cultural experiences, <a href=\"contact.html\">get in touch with us</a>.</p>",
        ],
    },
    {
        "slug": "skills-for-the-next-generation",
        "title": "Skills for the next generation: from agriculture to digital technology",
        "tag": "Youth & Skills",
        "img": "assets/img/hills-gold.webp",
        "excerpt": "Whether it is digital technology or agriculture, each person can be the change they want to see in the world.",
        "body": [
            "<p>We believe that each person can be the change they want to see in the world, regardless of their circumstances. Skills are how that belief turns into something practical.</p>",
            "<h2>A wide field on purpose</h2>",
            "<p>We do not limit our youth work to a single trade. Digital technology opens doors in every sector, agriculture feeds communities and builds enterprises, and hospitality connects both to visitors and markets. Our aim is to equip young people with different skills so they can choose a direction that fits them.</p>",
            "<h2>Practical safety and service skills</h2>",
            "<p>Alongside trade and technology skills we offer disaster-management training, including first aid and basic firefighting. These are the skills that make a community resilient and a young person employable.</p>",
            "<h2>How you can help</h2>",
            "<p>Training needs venues, equipment, mentors and funding. If your organisation would like to sponsor a skills programme or share expertise, please read about <a href=\"get-involved.html\">ways to get involved</a>.</p>",
        ],
    },
    {
        "slug": "sustainable-development-goals-local-action",
        "title": "Local action, global goals: how the SDGs guide our work",
        "tag": "Insight",
        "img": "assets/img/valley-portrait.webp",
        "excerpt": "We are not politically aligned. We are inspired by state legislation and the Sustainable Development Goals.",
        "body": [
            "<p>Eminiyeza Dreamlife is self-made and not politically aligned. What guides us is the law of the land and the Sustainable Development Goals, a shared agenda for people and planet.</p>",
            "<h2>Goals we can act on locally</h2>",
            "<p>Quality education, decent work and economic growth, sustainable cities and communities, and partnerships for the goals are all things a local organisation can move forward, one programme at a time. Our tourism, skills and community-resilience work is where those goals become concrete.</p>",
            "<h2>Standards we hold ourselves to</h2>",
            "<p>Our tone is soft but firm. We are warm with the people we serve and clear about the standards we keep: transparency, respect for community, lawful operation and service delivered with pride.</p>",
            "<h2>Work with us</h2>",
            "<p>Funders, partners and volunteers who share these standards are welcome. <a href=\"contact.html\">Send us a message</a> and let us talk about what we can build together.</p>",
        ],
    },
]


# ------------------------------------------------------------------ PAGES
def page_home():
    cards = [
        ("map", "Heritage &amp; Cultural Tourism", "Heritage, nature, culture, marine and astronomy tours that share local stories and create work for local people."),
        ("cap", "Youth Skills Development", "From digital technology to agriculture, we equip young people with practical skills for work and enterprise."),
        ("chat", "Languages", "Foreign, domestic and sign languages: French, Swahili, Dutch, German, English, Afrikaans and sign language."),
        ("shield", "Disaster Management", "First aid and basic firefighting skills that make communities and workplaces safer."),
        ("landmark", "Administrative &amp; Legal Support", "Administrative, legal and social interventions that help people and organisations get things done."),
        ("users", "Local Government Mandates", "Strategic services aligned to local economic development mandates and the Executive Mayor's office."),
    ]
    cards_html = "\n".join(
        f'<article class="card reveal"><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p>{d}</p></article>'
        for i, t, d in cards
    )
    posts_html = "\n".join(blog_card(p) for p in POSTS)
    body = f"""
<section class="hero" style="padding:0">
  <div class="hero__bg"><img src="assets/img/hero-mountains.webp" alt="" width="1400" height="788" fetchpriority="high"></div>
  <div class="wrap">
    <span class="eyebrow">Non-profit company &middot; Tourism &middot; Culture &middot; Skills</span>
    <h1>Securing a <em>better tomorrow</em> for all.</h1>
    <p class="lead">{ORG} builds opportunity through tourism and cultural experiences, and equips young people with the skills to shape their own future.</p>
    <div class="hero__cta">
      <a class="btn" href="get-involved.html">Fund &amp; Partner With Us {icon("arrow")}</a>
      <a class="btn btn--ghost" href="services.html">See What We Do</a>
    </div>
  </div>
</section>

<div class="actions">
  <div class="wrap actions__grid">
    <div class="action reveal"><span class="label">Funding</span><h3>Back our programmes</h3><p>Funding opportunities for tourism, culture and youth skills initiatives.</p><a class="more" href="get-involved.html#fund">Funding opportunities {icon("arrow")}</a></div>
    <div class="action reveal"><span class="label">Networking</span><h3>Join the network</h3><p>Connect with an independent organisation built on service, pride and partnership.</p><a class="more" href="get-involved.html#network">Start networking {icon("arrow")}</a></div>
    <div class="action reveal"><span class="label">Serve</span><h3>Serve with pride</h3><p>Anyone is welcome who is ready to serve. Tell us how you would like to contribute.</p><a class="more" href="contact.html">Contact us {icon("arrow")}</a></div>
  </div>
</div>

<section id="programmes">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="kicker">What we do</span>
      <h2>Quality services, built around people</h2>
      <p>We offer the best quality for less: tourism-related services and practical skills that equip our youth and strengthen our communities.</p>
    </div>
    <div class="cards">
{cards_html}
    </div>
    <p class="reveal" style="text-align:center;margin:44px 0 0"><a class="btn btn--outline" href="services.html">Explore all services</a></p>
  </div>
</section>

<section class="bg-sand">
  <div class="wrap split">
    <div class="split__media reveal">
      <img src="assets/img/elder-heritage.webp" alt="An elder in a black-and-white patterned headwrap at a community gathering" width="554" height="554" loading="lazy">
      <div class="badge"><strong>Rooted in community</strong>Heritage is carried by people. We exist to honour it and open it to the world.</div>
    </div>
    <div class="split__body reveal">
      <span class="kicker">About us</span>
      <h2>Soft but firm. Independent and self-made.</h2>
      <p>{ORG} is a non-profit company focusing on tourism and cultural experiences. We are self-made and not politically aligned, inspired by state legislation and the Sustainable Development Goals.</p>
      <p>Whether it is digital technology or agriculture, we believe each one of us can be the change we want to see in the world, regardless of our circumstances.</p>
      <div class="stats">
        <div class="stat"><strong>7</strong><span>languages offered, including sign language</span></div>
        <div class="stat"><strong>5</strong><span>core service areas for people and communities</span></div>
        <div class="stat"><strong>NPC</strong><span>registered non-profit company</span></div>
      </div>
      <a class="btn btn--green" href="about.html">More about us {icon("arrow")}</a>
    </div>
  </div>
</section>

<section class="quote-band">
  <div class="hero__bg"><img src="assets/img/valley-portrait.webp" alt="" loading="lazy" width="415" height="739"></div>
  <div class="wrap reveal">
    <blockquote>Building the economics of humanity, healing and permanence through tourism and hospitality in the family of the nations.</blockquote>
    <cite>Our guiding statement</cite>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">The landscape we celebrate</span>
      <h2>Mountains, valleys and living heritage</h2>
      <p>Nature and culture are the heart of the experiences we want to share.</p>
    </div>
    <div class="gallery reveal">
      <figure><img src="assets/img/hero-mountains.webp" alt="Green mountains and valleys under a cloudy sky" loading="lazy" width="1400" height="788"><figcaption>Mountain heritage and nature</figcaption></figure>
      <figure><img src="assets/img/ridge-view.webp" alt="Layered mountain ridges in warm light" loading="lazy" width="729" height="420"><figcaption>Ridge-line views</figcaption></figure>
      <figure><img src="assets/img/hills-gold.webp" alt="Golden grassy hillsides" loading="lazy" width="400" height="400"><figcaption>Open hillsides</figcaption></figure>
      <figure><img src="assets/img/valley-portrait.webp" alt="A green valley at sunset" loading="lazy" width="415" height="739"><figcaption>Valley at golden hour</figcaption></figure>
      <figure><img src="assets/img/elder-heritage.webp" alt="An elder at a community event" loading="lazy" width="554" height="554"><figcaption>Elders and tradition</figcaption></figure>
    </div>
  </div>
</section>

<section class="bg-green">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="kicker">Get involved</span>
      <h2>Three ways to help us grow</h2>
      <p style="color:rgba(255,255,255,.8)">Funding and networking are our main goals. Here is where you can plug in.</p>
    </div>
    <div class="ways">
      <div class="way reveal"><div class="card__icon">{icon("coins")}</div><h3>Fund a programme</h3><p>Support tourism, culture and youth skills initiatives with a grant, sponsorship or in-kind contribution.</p><a href="get-involved.html#fund">Funding opportunities {icon("arrow")}</a></div>
      <div class="way reveal"><div class="card__icon">{icon("globe")}</div><h3>Build a partnership</h3><p>Tourism operators, training providers, government and NGOs: let us connect and work together.</p><a href="get-involved.html#network">Networking {icon("arrow")}</a></div>
      <div class="way reveal"><div class="card__icon">{icon("heart")}</div><h3>Volunteer your skills</h3><p>Guides, trainers, translators, first-aiders and digital volunteers all strengthen the work.</p><a href="contact.html">Offer your time {icon("arrow")}</a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal" style="display:flex;justify-content:space-between;align-items:end;gap:20px;max-width:none;flex-wrap:wrap">
      <div style="max-width:620px"><span class="kicker">From the blog</span><h2 style="margin:0">Stories &amp; insight</h2></div>
      <a class="btn btn--outline" href="blog.html">All articles</a>
    </div>
    <div class="posts">
{posts_html}
    </div>
  </div>
</section>

{newsletter()}
"""
    ld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"NGO","name":"{ORG}","description":"Non-profit company focusing on tourism, cultural experiences and youth skills development.","email":"{EMAIL}","telephone":"{PHONE_TEL}","address":{{"@type":"PostalAddress","streetAddress":"17681 Vuyani Street, Bongolethu","postalCode":"6625","addressCountry":"ZA"}},"sameAs":["{FACEBOOK}"]}}
</script>"""
    return shell("index.html", ORG, "Eminiyeza Dreamlife is a non-profit company offering tourism, cultural experiences and youth skills development. Funding opportunities and networking welcome.", body, extra_head=ld)


def blog_card(p):
    return f"""<article class="post reveal">
  <a href="{p['slug']}.html" tabindex="-1" aria-hidden="true"><img src="{p['img']}" alt="" loading="lazy"></a>
  <div class="post__body"><span class="tag">{p['tag']}</span>
  <h3><a href="{p['slug']}.html">{p['title']}</a></h3>
  <p>{p['excerpt']}</p>
  <a class="more" href="{p['slug']}.html">Read more {icon("arrow")}</a></div>
</article>"""


def page_hero(title, text, img="hills-gold.webp"):
    return f"""<section class="page-hero" style="padding:0">
  <div class="hero__bg"><img src="assets/img/{img}" alt="" width="1400" height="788"></div>
  <div class="wrap"><span class="eyebrow">{ORG}</span><h1>{title}</h1><p>{text}</p></div>
</section>"""


def page_about():
    principles = [
        ("01", "Independent", "Self-made and not politically aligned. We answer to our mission and the communities we serve."),
        ("02", "Lawful &amp; accountable", "Inspired by state legislation, registered and operating openly as a non-profit company."),
        ("03", "Goal-driven", "Guided by the Sustainable Development Goals, turned into practical local action."),
        ("04", "Proud to serve", "Anyone is welcome who is ready to serve with pride and to hold a high standard."),
    ]
    pr = "\n".join(f'<div class="principle reveal"><span class="num">{n}</span><h3>{t}</h3><p>{d}</p></div>' for n, t, d in principles)
    body = f"""
{page_hero("A better tomorrow, built together", "Who we are, what we believe and the standards we keep.", "ridge-view.webp")}

<section>
  <div class="wrap split">
    <div class="split__media reveal"><img src="assets/img/valley-portrait.webp" alt="A green valley at sunset" width="415" height="739" loading="lazy"></div>
    <div class="split__body reveal">
      <span class="kicker">Our story</span>
      <h2>Tourism and culture with a purpose</h2>
      <p>{ORG} is a non-profit company focusing on tourism and cultural experiences. The organisation is self-made and not politically aligned, aiming to be inspired by state legislation and the Sustainable Development Goals.</p>
      <p>Whether it is digital technology or agriculture, we believe each one can be the change they want to see in the world, regardless of our circumstances.</p>
      <p>What makes us unique is our commitment to <strong>securing a better tomorrow for all</strong>. We speak in a soft but firm tone, setting the standards for the work we do.</p>
      <ul class="checks">
        <li>{icon("check")}<span>We offer the best quality for less in tourism-related matters</span></li>
        <li>{icon("check")}<span>We equip our youth with different skills</span></li>
        <li>{icon("check")}<span>Anyone is welcome who is ready to serve with pride</span></li>
      </ul>
      <a class="btn" href="contact.html">Talk to us {icon("arrow")}</a>
    </div>
  </div>
</section>

<section class="bg-sand">
  <div class="wrap">
    <div class="section-head center reveal"><span class="kicker">Our values</span><h2>What guides every decision</h2></div>
    <div class="principles">
{pr}
    </div>
  </div>
</section>

<section>
  <div class="wrap split split--rev">
    <figure class="calendar-fig split__media reveal">
      <img src="assets/img/business-calendar-2026.webp" alt="Eminiyeza Dreamlife Business Calendar 2026 showing services offered and registration numbers" width="1000" height="1414" loading="lazy" style="aspect-ratio:auto">
      <figcaption>Our 2026 Business Calendar</figcaption>
    </figure>
    <div class="split__body reveal">
      <span class="kicker">Registered &amp; accountable</span>
      <h2>Open about who we are</h2>
      <p>We operate as a registered non-profit company. Our registration details are printed on our business calendar and available on request from our office.</p>
      <div class="reg"><dl>
        <dt>Organisation</dt><dd>{ORG} NPC</dd>
        <dt>NPO number</dt><dd>192-961 NPO</dd>
        <dt>CIPC</dt><dd>2025/628405/08</dd>
        <dt>Contact person</dt><dd>{CONTACT_PERSON}</dd>
      </dl></div>
    </div>
  </div>
</section>

{newsletter()}
"""
    return shell("about.html", "About Us", "Eminiyeza Dreamlife is a self-made, politically independent non-profit company inspired by state legislation and the Sustainable Development Goals.", body)


def page_services():
    blocks = [
        ("tourism", "map", "Heritage, nature &amp; cultural tourism", "Experiences that share the character of a place and the pride of its people.",
         ["Heritage and culture tours", "Nature tours", "Marine and astronomy tours", "Hospitality in the family of the nations"], "hero-mountains.webp"),
        ("skills", "cap", "Youth skills development", "Practical skills for work, enterprise and community leadership.",
         ["Digital technology", "Agriculture", "Hospitality and guiding", "Mentoring and leadership"], "hills-gold.webp"),
        ("languages", "chat", "Languages", "Communication across borders, cultures and communities.",
         ["French and Swahili", "Dutch and German", "English and Afrikaans", "Sign language"], "ridge-view.webp"),
        ("resilience", "shield", "Community resilience", "Keeping people safe and organisations running well.",
         ["First aid", "Basic firefighting", "Administrative, legal and social interventions", "Local government mandate services (LED strategic services, Executive Mayor's office)"], "valley-portrait.webp"),
    ]
    out = []
    for i, (id_, ic, title, intro, items, img) in enumerate(blocks):
        lis = "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in items)
        rev = " split--rev" if i % 2 else ""
        bg = ' class="bg-sand"' if i % 2 == 0 else ""
        out.append(f"""<section id="{id_}"{bg}>
  <div class="wrap split{rev}">
    <div class="split__media reveal"><img src="assets/img/{img}" alt="" loading="lazy" style="aspect-ratio:4/3"></div>
    <div class="split__body reveal">
      <div class="card__icon">{icon(ic)}</div>
      <h2>{title}</h2>
      <p>{intro}</p>
      <ul class="checks">{lis}</ul>
      <a class="btn btn--green" href="contact.html">Enquire about this {icon("arrow")}</a>
    </div>
  </div>
</section>""")
    body = f"""
{page_hero("What we do", "Tourism, culture and practical skills — delivered with quality and pride.", "hero-mountains.webp")}
{''.join(out)}
{newsletter()}
"""
    return shell("services.html", "What We Do", "Heritage and cultural tourism, youth skills, languages, first aid and firefighting, and administrative support from Eminiyeza Dreamlife.", body)


def page_involved():
    body = f"""
{page_hero("Get involved", "Our main goals are funding opportunities and networking. Here is how to take part.", "valley-portrait.webp")}

<section id="fund">
  <div class="wrap split">
    <div class="split__body reveal">
      <div class="card__icon">{icon("coins")}</div>
      <span class="kicker">Funding opportunities</span>
      <h2>Fund work that lasts</h2>
      <p>Your support helps us run tourism and cultural experiences, train young people and keep communities safe. We welcome grants, sponsorships, corporate social investment and in-kind support such as venues, equipment and mentors.</p>
      <ul class="checks">
        <li>{icon("check")}<span>Sponsor a youth skills programme</span></li>
        <li>{icon("check")}<span>Support heritage and tourism experiences</span></li>
        <li>{icon("check")}<span>Provide equipment, training venues or expertise</span></li>
      </ul>
      <a class="btn" href="contact.html">Discuss funding {icon("arrow")}</a>
    </div>
    <div class="split__media reveal"><img src="assets/img/hills-gold.webp" alt="Golden hills" loading="lazy" style="aspect-ratio:4/3"></div>
  </div>
</section>

<section id="network" class="bg-sand">
  <div class="wrap split split--rev">
    <div class="split__body reveal">
      <div class="card__icon">{icon("globe")}</div>
      <span class="kicker">Networking</span>
      <h2>Let us build something together</h2>
      <p>We work best in partnership. If you represent a tourism operator, training provider, government office, NGO or business that shares our standards, we would like to meet you.</p>
      <ul class="checks">
        <li>{icon("check")}<span>Tourism and hospitality partnerships</span></li>
        <li>{icon("check")}<span>Skills-training and education collaborations</span></li>
        <li>{icon("check")}<span>Local government and community programmes</span></li>
      </ul>
      <a class="btn btn--green" href="contact.html">Start a conversation {icon("arrow")}</a>
    </div>
    <div class="split__media reveal"><img src="assets/img/ridge-view.webp" alt="Mountain ridges" loading="lazy" style="aspect-ratio:4/3"></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head center reveal"><span class="kicker">Serve with pride</span><h2>Volunteer your skills</h2><p>Anyone is welcome who is ready to serve with pride. Guides, trainers, translators, first-aiders, designers and digital helpers can all make a difference.</p></div>
    <p style="text-align:center" class="reveal"><a class="btn" href="contact.html">Offer your time {icon("arrow")}</a></p>
  </div>
</section>

{newsletter()}
"""
    return shell("get-involved.html", "Get Involved", "Fund our programmes, join our network or volunteer your skills with Eminiyeza Dreamlife.", body)


def page_blog():
    cards = "\n".join(blog_card(p) for p in POSTS)
    body = f"""
{page_hero("Blog", "Stories, insight and updates from our work in tourism, culture and skills.", "ridge-view.webp")}
<section><div class="wrap"><div class="posts">
{cards}
</div></div></section>
{newsletter()}
"""
    return shell("blog.html", "Blog", "Articles on cultural tourism, youth skills and the Sustainable Development Goals from Eminiyeza Dreamlife.", body)


def page_post(p):
    others = [x for x in POSTS if x["slug"] != p["slug"]]
    more = "\n".join(blog_card(x) for x in others)
    body = f"""
{page_hero(p['title'], p['excerpt'], p['img'].split('/')[-1])}
<section>
  <div class="wrap">
    <article class="article">
      <img class="feature" src="{p['img']}" alt="">
      <span class="tag">{p['tag']}</span>
      {''.join(p['body'])}
      <p style="margin-top:2em"><a class="btn btn--outline" href="blog.html">&larr; Back to blog</a></p>
    </article>
  </div>
</section>
<section class="bg-sand"><div class="wrap"><div class="section-head reveal"><h2>Keep reading</h2></div><div class="posts" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr))">
{more}
</div></div></section>
"""
    return shell(f"{p['slug']}.html", p["title"], p["excerpt"], body, og_image=p["img"])


def page_contact():
    body = f"""
{page_hero("Contact us", "Funding, partnerships, volunteering or general questions — we would love to hear from you.", "hills-gold.webp")}
<section>
  <div class="wrap contact-grid">
    <div class="reveal">
      <span class="kicker">Get in touch</span>
      <h2>Let us talk</h2>
      <p>Send us a message and we will respond as soon as we can. You can also reach us directly using the details below.</p>
      <ul class="contact-list">
        <li><div class="card__icon">{icon("users")}</div><div><strong>Contact person</strong><span>{CONTACT_PERSON}</span></div></li>
        <li><div class="card__icon">{icon("mail")}</div><div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
        <li><div class="card__icon">{icon("phone")}</div><div><strong>Phone / WhatsApp</strong><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div></li>
        <li><div class="card__icon">{icon("map")}</div><div><strong>Address</strong><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS}</a></div></li>
        <li><div class="card__icon">{icon("facebook")}</div><div><strong>Facebook community</strong><a href="{FACEBOOK}" target="_blank" rel="noopener">Join our Facebook group</a></div></li>
      </ul>
    </div>
    <div class="panel reveal">
      <h3>Send a message</h3>
      <form data-ajax data-endpoint="{FORM_ENDPOINT}" data-fallback="{EMAIL}" data-success="Thank you — your message has been sent. We will be in touch soon." novalidate>
        <div class="form-grid">
          <div><label for="name">Your name</label><input id="name" name="name" autocomplete="name" required></div>
          <div><label for="email">Email address</label><input id="email" type="email" name="email" autocomplete="email" required></div>
          <div><label for="phone">Phone (optional)</label><input id="phone" type="tel" name="phone" autocomplete="tel"></div>
          <div><label for="topic">I am interested in</label>
            <select id="topic" name="topic"><option>General enquiry</option><option>Funding / sponsorship</option><option>Partnership / networking</option><option>Volunteering</option><option>Tourism &amp; cultural experiences</option><option>Skills training</option></select></div>
          <div class="full"><label for="message">Message</label><textarea id="message" name="message" rows="6" required></textarea></div>
        </div>
        <div class="hp" aria-hidden="true"><input type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
        <input type="hidden" name="_subject" value="New website enquiry — Eminiyeza Dreamlife">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="form" value="Contact">
        <p class="form-note">By sending this form you agree that we may contact you about your enquiry.</p>
        <button class="btn" type="submit">Send message {icon("arrow")}</button>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
"""
    return shell("contact.html", "Contact Us", "Contact Eminiyeza Dreamlife about funding, partnerships, volunteering or tourism and skills programmes.", body)


def page_404():
    body = f"""
<section style="min-height:60vh;display:grid;place-items:center;text-align:center">
  <div class="wrap"><span class="kicker">Error 404</span><h1>This path has gone off the map</h1><p style="color:var(--muted);font-size:1.15rem">The page you are looking for does not exist or has moved.</p><a class="btn" href="index.html">Back to home</a></div>
</section>"""
    return shell("404.html", "Page not found", "Page not found.", body)


def main():
    pages = {
        "index.html": page_home(),
        "about.html": page_about(),
        "services.html": page_services(),
        "get-involved.html": page_involved(),
        "blog.html": page_blog(),
        "contact.html": page_contact(),
        "404.html": page_404(),
    }
    for p in POSTS:
        pages[f"{p['slug']}.html"] = page_post(p)
    for name, html in pages.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
    print(f"Built {len(pages)} pages")


if __name__ == "__main__":
    main()
