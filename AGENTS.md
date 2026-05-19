# AGENTS DIRECTIVE

This project involves migrating from Hostinger's proprietary website builder to a custom-coded, locally-managed tech recruitment website.

## PROJECT CONTEXT

- **Current Status**: Hostinger plan expired, site returning 403 Forbidden
- **Target**: Modern, interactive tech recruitment portal with local management via Claude
- **Domain**: bossenterprise.co.za (using Hostinger for domain/hosting only)
- **Technology Stack**: Astro + Tailwind CSS (static site generator with islands architecture)

## DEVELOPMENT ENVIRONMENT

- **Local Setup**: Use Node.js v18+ and npm
- **Build Tool**: `npm run dev` for local development
- **Preview**: `npm run preview` for production preview
- **Deployment**: Build to static files, deploy via FTP/hosting panel

## TECHNICAL STACK

- **Frontend**: Astro + Tailwind CSS
- **Interactivity**: Alpine.js for lightweight interactivity
- **Forms**: PHP contact forms on Hostinger server
- **Hosting**: Hostinger shared hosting (static files)
- **Domain**: Hostinger DNS management

## CODING PRINCIPLES

1. **Content-First**: Build static HTML first, add interactivity second
2. **Mobile-First**: Responsive design for all devices
3. **Accessibility**: WCAG 2.1 compliant
4. **Performance**: Optimize images, minify CSS/JS
5. **SEO**: Proper meta tags, semantic HTML

## RECOVERY ASSETS

Assets recovered from Wayback Machine (Aug 2025):
- Boss Baby Enterprise Logo (main)
- Boss Consult Logo (white)
- Hero image
- Client/partner logos (3+)
- Full website HTML structure

## WORKFLOW

1. **Recovery Phase**: Extract content from archive
2. **Design Phase**: Create modern UI with Tailwind
3. **Development Phase**: Build static pages with Astro
4. **Testing Phase**: Local preview and validation
5. **Deployment Phase**: Upload via FTP/hosting panel

## DEPLOYMENT NOTES

- Build command: `npm run build`
- Output: `/dist/` directory
- Upload entire `/dist/` folder to `/public_html/` on Hostinger
- Update DNS if needed (domain already configured)

## MAINTENANCE

- Update content via local development
- Deploy changes with updated build
- Monitor for 404 errors after updates
- Backup regularly before deployments