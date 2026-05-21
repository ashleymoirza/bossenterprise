# BOSS Enterprise — bossenterprise.co.za

Tech recruitment agency site migrated from WordPress/Elementor → Astro + Tailwind + Alpine.js.

## Context
- Original site lost after Hostinger plan expiry; recovered via Wayback Machine (Aug 2025)
- Recovered assets in `/assets/`; full HTML in `/assets/recovered/`
- Deploy: `npm run build` → upload `/dist/` to Hostinger `/public_html/`

## Stack
Astro, Tailwind CSS, Alpine.js. PHP forms on Hostinger. Mobile-first, SEO-optimized.

## Commands
- `npm run dev` — local dev server
- `npm run build` — production build to `/dist/`
- `npm run preview` — preview production build