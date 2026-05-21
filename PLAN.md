# PLAN: Restore Content to Match Web Archive (Aug 2025)

## Objective
Update all page content to match the August 2025 Wayback Machine archive, applying proper responsive spacing (web/tablet/mobile). Preserve all existing color/font/button styles (already verified 1:1 with archive).

## Archive Reference
- Source: `assets/recovered/website-content.html` + Wayback Machine CSS (post-48, post-55, post-61, post-64)
- Colors, fonts, button styles — already match archive exactly ✅

## Content Gaps (from archive comparison)

| # | File | What's Missing/Mismatched |
|---|------|--------------------------|
| 1 | `index.astro` | **8 Core Values strip** — completely missing. Archive has: Passion, Care, Integrity, Transparency, Accountability, Respect, Independence, Courage with icons on gradient bg |
| 2 | `index.astro` | **Testimonials** — archive has a carousel with 6 different reviewers (Lisa Anne La Vita, Jomosne Conway Geduld, Masiyenze Mpisi, Vaughan Karriem, Unathi Magodla, Nkosinathi Mbali). Current has 4 static cards with Google review excerpts |
| 3 | `index.astro` | **Client logos** — archive has 9 specific clients: Clothing Junction, African Ideas, Victory Lab, Senqu, HumanInsights, Hbook, Goodwall, EasyPay, CMS Software Solutions. Current has generic client-logo-1/2/3 + 3 named logos |
| 4 | All pages | **Mobile responsive spacing** — ensure consistent padding on small screens |

## Implementation Steps

### Step 1: `index.astro` — Add 8 Core Values strip
- Insert after "Why Choose Us?" section, on gradient bg (`from-brand-hero to-brand-dark`)
- 8 values with SVG icons in responsive grid (4-col desktop, 2-col tablet, 1-col mobile)

### Step 2: `index.astro` — Replace testimonials with archive content
- Update reviewer names and quotes to match archive
- Keep existing card layout (not adding JS carousel — simpler and correct)

### Step 3: `index.astro` — Update client logos
- Replace generic logo names with archive-matching labels
- Ensure responsive grid layout

### Step 4: Responsive spacing audit
- Add responsive padding/margin classes throughout all pages
- Mobile-first: `px-4 sm:px-6 lg:px-8` pattern consistent
- Hero section responsive padding

### Step 5: `about.astro` — Add client logos section
- Add "Trusted By" section matching homepage pattern

### Step 6: Build & verify
- `npm run build` — zero errors
- `npm run dev` — localhost link for user confirmation

## Risks
- Some archive client logos (Victory Lab, HumanInsights, Hbook, Goodwall, EasyPay, CMS Software) don't have local images — will use alt text with logo file paths
- No archive content for contact/jobs pages — those stay as-is with correct styling