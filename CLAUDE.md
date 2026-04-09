# RussellSpurlock.com — Website Assistant Instructions

## What This Project Is
Russell Spurlock's personal website — portfolio, flight instruction business, and hub for aviation apps.
Live at: https://russellspurlock.com

## Tech Stack
- **Main site:** Plain HTML5 + Bootstrap 5.3.3 (CDN) + vanilla JS — no build process
- **Fonts/Icons:** Google Fonts (Inter, Poppins), Bootstrap Icons (CDN)
- **Forms:** Formspree (contact form at `#contact`)
- **Scheduling:** Koalendar embed (flight training bookings)
- **Hosting:** Vercel (migrated from Squarespace, April 2026)
- **Repo:** https://github.com/rpossum/russellspurlock-site

## Folder Structure
```
russellspurlock-vercel/
├── index.html          ← entire main site (single page)
├── robots.txt
├── images-new/         ← all site images (hero, carousels, logo)
└── resume/
    └── index.html      ← redirects to Google Drive PDF download
```

## Deployment
- Hosted on **Vercel**, connected to GitHub repo `rpossum/russellspurlock-site`
- Every push to `main` auto-deploys
- No build step — Vercel serves static files directly (framework: Other)

## DNS (managed at Squarespace)
| Type | Name | Data | Purpose |
|------|------|------|---------|
| A | @ | 76.76.21.21 | Vercel — main domain |
| CNAME | www | cname.vercel-dns.com | Vercel — www |
| MX | @ | mxa.mailgun.org | Email forwarding |
| MX | @ | mxb.mailgun.org | Email forwarding |
| TXT | @ | v=spf1 include:mailgun.org ~all | Email SPF |
| TXT | krs._domainkey | (DKIM key) | Email DKIM |
| CNAME | fj4lyp2ryuar | gv-tspf646eeecgw7.dv.googlehosted.com | Google verification |

## Email
- `russell@russellspurlock.com` forwards to Russell's Gmail via **Mailgun**
- Mailgun is set up through Squarespace Email Forwarding — do not touch MX/SPF/DKIM records

## Apps (separate from this repo)
Russell has aviation apps hosted separately. They live at their own URLs (Railway or Vercel) and are NOT in this repo. Examples:
- **ChartWise** — React + Vite + Tailwind, aviation chart/study app
- **CheckSmart** — PWA checklist app (already built static)
- The main site may link to these apps but does not host them

## Russell's Background (for content decisions)
- Commercial Pilot, CFII, ~1,500 hours, based in Cape Coral / SW Florida
- Teaches flight instruction (PPL, IFR, Commercial, CFI/CFII, Discovery Flights)
- Building turbine time, pursuing Part 135 SIC roles
- Full resume always at: https://russellspurlock.com/resume/

## Site Sections (index.html)
- **Hero** — full-screen background image with CTA buttons
- **About** — bio + King Air photo
- **Training** — programs offered + carousel of training photos
- **Jet/Turbine** — turbine experience + carousel
- **Scheduling** — Koalendar embed
- **Rates** — pricing cards
- **Testimonials** — student quotes
- **Contact** — Formspree form
- **Footer** — social links (Facebook, LinkedIn, YouTube/PossumPilot)

## Important Rules
1. All dependencies are CDN-based — do not introduce npm/build steps to the main site
2. Images live in `images-new/` — keep that folder name
3. The `resume/index.html` is just a redirect — the actual resume PDF lives on Google Drive
4. Do not touch DNS MX/SPF/DKIM records — email forwarding depends on them
5. When deploying changes, just push to `main` — Vercel handles the rest
