# BOSS Enterprise Website Project

## PROJECT CONTEXT

**Client Website**: bossenterprise.co.za - Tech Recruitment Agency
**Current Issue**: Hostinger hosting plan expired, site returning 403 Forbidden
**Objective**: Migrate from proprietary builder to custom-coded, locally-managed site

### Project Overview
BOSS Enterprise is a tech recruitment agency specializing in placing high-impact talent across Data Science, Development, and related fields. The original website was built with WordPress + Elementor but became inaccessible after hosting plan expiration.

## RECOVERY STATUS

### ✅ Completed Recovery
- **Wayback Machine**: Successfully recovered full site (Aug 2025 snapshot)
- **Assets Downloaded**: All logos, images, and branding materials
- **Content Extracted**: Complete HTML structure and styling information

### Recovered Assets Location
`/assets/logos/` contains:
- Boss Baby Enterprise Logo (main)
- Boss Consult Logo (white version)
- Hero image
- Client/partner logos
- Recovered HTML content in `/assets/recovered/`

## TECHNICAL REQUIREMENTS

### Stack Selection
- **Framework**: Astro (static site generator)
- **Styling**: Tailwind CSS (utility-first)
- **Interactivity**: Alpine.js for lightweight features
- **Forms**: PHP backend on Hostinger server
- **Deployment**: Static files to Hostinger shared hosting

### Key Features Needed
1. **Job Listings Board**: Searchable/filterable job postings
2. **Candidate Application Form**: CV upload, contact details
3. **Employer Portal**: Vacancy submission, staffing requests
4. **Blog/Content**: Industry articles, career advice

## DEVELOPMENT ENVIRONMENT

### Local Setup
```bash
# Initialize project (to be done)
npm create astro@latest . -- --template minimal
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Development Commands
- `npm run dev` - Local development server
- `npm run build` - Production build
- `npm run preview` - Preview production build

### File Structure
```
/
├── src/
│   ├── components/    # Reusable UI components
│   ├── layouts/       # Page layouts
│   ├── pages/         # Individual pages
│   └── styles/        # Global styles
├── public/           # Static assets (images, etc.)
├── dist/            # Build output (for deployment)
└── assets/          # Recovered assets
```

## DEPLOYMENT STRATEGY

### Hostinger Configuration
1. **Domain**: Already registered with Hostinger
2. **Hosting**: Shared hosting plan renewed
3. **FTP**: Ready for file uploads
4. **SSL**: Free Let's Encrypt certificate available

### Deployment Process
1. Build static site: `npm run build`
2. Upload entire `/dist/` folder to `/public_html/`
3. Set up PHP contact forms
4. Configure SSL for HTTPS
5. Test all functionality

### Form Handling (PHP)
```php
// contact-form.php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];
    
    $to = "info@bossenterprise.co.za";
    $headers = "From: $email";
    
    mail($to, $subject, $message, $headers);
}
?>
```

## CONTENT RECOVERY DETAILS

### Original Site Structure
- Homepage: Hero section, services, testimonials, client logos
- Job listings: Category-based filtering
- Application process: Multi-step form
- Employer section: Vacancy submission
- Blog: Industry articles and news

### Key Content Elements
- Tagline: "We're not just recruiters — we're your growth partners"
- Specializations: Data Science, Development, Tech talent
- Clients: Multiple tech companies (logos recovered)
- Services: Staffing solutions, recruitment

## NEXT STEPS

1. **Initialize Astro project**
2. **Set up Tailwind CSS**
3. **Create base layouts and components**
4. **Build homepage with recovered content**
5. **Implement job listings board**
6. **Add application form with PHP backend**
7. **Deploy to Hostinger**

## NOTES

- All branding assets recovered and available
- Original content structure preserved
- Hostinger supports PHP for form handling
- Static site approach ensures fast loading
- Mobile-first design required
- SEO optimization needed for job listings