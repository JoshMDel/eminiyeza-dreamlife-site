# Eminiyeza Dreamlife — Website

Static, fast, mobile-first website for **Eminiyeza Dreamlife NPC**, a non-profit company focused on tourism, cultural experiences and youth skills development.

Design reference: Weblium "Charity Foundation" template (hero + action cards, programmes grid, about with stats, ways to help, blog, newsletter). Colours are taken from the organisation's 2026 business calendar.

## Pages

| Page | File |
| --- | --- |
| Home | `index.html` |
| About | `about.html` |
| What We Do | `services.html` |
| Get Involved (funding & networking) | `get-involved.html` |
| Blog + 3 articles | `blog.html`, `*.html` |
| Contact (form) | `contact.html` |
| 404 | `404.html` |

## Editing content

Pages are generated from `build.py` so the header/footer stay consistent.

```bash
python build.py     # rewrites every .html file
```

Contact details, nav, blog posts and all page copy live in `build.py`. Styles are in `assets/css/style.css`; images in `assets/img/`.

## Forms (contact + newsletter)

Both forms post to [FormSubmit](https://formsubmit.co) and are delivered to `masihiyuaja@gmail.com`. **The first submission after going live triggers an activation email to that address — click the link once** and all later messages arrive normally. To change the recipient, edit `EMAIL` in `build.py` and re-run it.

## Hosting

No build step or server code is needed — upload the folder contents (everything except `build.py`/`README.md` if you like) to any host: cPanel/Truehost `public_html`, Netlify, Cloudflare Pages, or GitHub Pages.

## To do before launch

- Add the live domain to the `og:` tags and a `sitemap.xml` once the final URL is confirmed.
- Replace the placeholder blog posts with real stories/dates, and add real photos of programmes and events when available.
- Add partner logos, a funding/banking details section, or a donation link if the organisation wants them.
