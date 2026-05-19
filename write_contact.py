#!/usr/bin/env python3
"""Write the contact.astro file."""

filepath = "/Users/ashleymoir/Downloads/free-claude-code-main/bossenterprise.co.za/src/pages/contact.astro"

# Build the file section by section to avoid encoding issues
lines = []
lines.append('---')
lines.append("import BaseLayout from '../layouts/BaseLayout.astro';")
lines.append('---')
lines.append('<BaseLayout')
lines.append('  title="Contact Us | BOSS Enterprise"')
lines.append('  description="Get in touch with BOSS Enterprise for your tech recruitment needs. Contact us via phone, email, or use our contact form."')
lines.append('>')
lines.append('  <div class="pt-24">')
lines.append('    <section class="bg-brand-dark text-white py-20">')
lines.append('      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">')
lines.append('        <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold">Get in Touch</h1>')
lines.append('        <p class="text-xl mt-6 max-w-2xl mx-auto text-gray-400">')
lines.append("          Have a question, or want to discuss your recruitment needs? We'd love to hear from you.")
lines.append('        </p>')
lines.append('      </div>')
lines.append('    </section>')

lines.append('    <section class="bg-white py-16 lg:py-24">')
lines.append('      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">')
lines.append('        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16">')

# Left column
lines.append('          <div>')
lines.append('            <h2 class="text-2xl font-bold text-brand-dark mb-8">Send Us a Message</h2>')
lines.append('            <form action="/php/contact.php" method="POST" class="space-y-6">')

# Name field
lines.append('              <div>')
lines.append('                <label for="name" class="block text-sm font-medium text-brand-dark mb-1">Full Name</label>')
lines.append('                <input type="text" id="name" name="name" required')
lines.append('                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-accent focus:border-brand-accent outline-none transition"')
lines.append('                  placeholder="Your full name" />')
lines.append('              </div>')

# Email field
lines.append('              <div>')
lines.append('                <label for="email" class="block text-smfont-medium text-brand-dark mb-1">Email Address</label>')
lines.append('                <input type="email" id="email" name="email" required')
lines.append('                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-accent focus:border-brand-accent outline-none transition"')
lines.append('                  placeholder="your@email.com" />')
lines.append('              </div>')

# Phone field
lines.append('              <div>')
lines.append('                <label for="phone" class="block text-sm font-medium text-brand-dark mb-1">Phone Number</label>')
lines.append('                <input type="tel" id="phone" name="phone"')
lines.append('                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-accent focus:border-brand-accent outline-none transition"')
lines.append('                  placeholder="+27 XX XXX XXXX" />')
lines.append('              </div>')

# Subject field
lines.append('              <div>')
lines.append('          class="block text-sm font-medium text-brand-dark mb-1">Subject</label>')
lines.append('                <select id="subject" name="subject" required')
lines.append('                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-accent focus:border-brand-accent outline-none transition bg-white">')
lines.append('                  <option value="">Select a subject</option>')
lines.append('                  <option value="General Inquiry">General Inquiry</option>')
lines.append('                  <option value="Job Application">Job Application</option>')
lines.append('                  <option value="Employer Services">Employer Services</option>')
lines.append('                  <option value="Partnership Inquiry">Partnership Inquiry</option>')
lines.append('                  <option value="Other">Other</option>')
lines.append('                </select>')
lines.append('              </div>')

# Message field
lines.append('              <div>')
lines.append('                <label for="message" class="block text-sm font-medium text-brand-dark mb-1">Message</label>')
lines.append('                <textarea id="message" name="message" rows="5" required')
lines.append('                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-accent focus:border-brand-accent outline-none transition resize-vertical"')
lines.append('                  placeholder="How can we help you?"></textarea>')
lines.append('              </div>')

# Submit button
lines.append('              <button type="submit"')
lines.append('                class="w-full bg-brand-accent hover:bg-brand-accent-light text-white font-semibold px-6 py-3.5 rounded-lg transition duration-300 cursor-pointer">')
lines.append('                Send Message')
lines.append('              </button>')
lines.append('            </form>')
lines.append('          </div>')

# Right column
lines.append('          <div>')
lines.append('            <h2 class="text-2xl font-bold text-brand-dark mb-8">Contact Information</h2>')

# Phone
lines.append('            <div class="flex items-start mb-6">')
lines.append('              <div class="flex-shrink-0 w-12 h-12 bg-brand-accent/10 rounded-full flex items-center justify-center">')
lines.append('                <svg class="w-5 h-5 text-brand-accent" fill="none" stroke="currentColor" viewBox="0 0 0 24 24">')
lines.append('                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.948V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />')
lines.append('                </svg>')
lines.append('              </div>')
lines.append('              <div class="ml-4">')
lines.append('                <h3 class="text-sm font-semibold text-brand-dark uppercase tracking-wider">Phone</h3>')
lines.append('                <a href="tel:+27632404447" class="text-brand-accent hover:text-brand-accent-light transition text-lg font-medium">+27 63 240 4447</a>')
lines.append('              </div>')
lines.append('            </div>')

# Email
lines.append('            <div class="flex items-start mb-6">')
lines.append('              <div class="flex-shrink-0 w-12 h-12 bg-brand-accent/10 rounded-full flex items-center justify-center">')
lines.append('                <svg class="w-5 h-5 text-brand-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24-incap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 5h14a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2z" />')
lines.append('                </svg>')
lines.append('              </div>')
lines.append('              <div class="ml-4">')
lines.append('                <h3 class="text-sm font-semibold text-brand-dark uppercase tracking-wider">Email</h3>')
lines.append('                <a href="mailto:gaylene@bossenterprise.co.za" class="text-brand-accent hover:text-brand-accent-light transition text-lg font-medium">gaylene@bossenterprise.co.za</a>')
lines.append('              </div>')
lines.append('            </div>')

# Location
lines.append('            <div class="flex items-start mb-6">')
lines.append('              <div class="flex-shrink-0 w-12 h-12 bg-brand-accent/10 rounded-full flex items-center justify-center">')
lines.append('                <svg class="w-5 h-5 text-brand-accent" fill="none" stroke="currentColo 24 24">')
lines.append('                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a2 2 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />')
lines.append('                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 ϵ 0 3 0 016 0z" />')
lines.append('                </svg>')
lines.append('              </div>')
lines.append('              <div class="ml-4">')
lines.append('                <h3 class="text-sm font-semibold text-brand-dark uppercase tracking-wider">Location</h3>')
lines.append('                <p class="text-brand-gray text-lg">Cape Town, Western Cape</p>')
lines.append('              </div>')
lines.append('            </div>')

# Social
lines.append('            <div class="mt-12 pt-8 border-t border-gray-200">')
lines.append('              <h3 class="text-sm font-semibold text-brand-dark uppercase tracking-wider mb-6">Follow Us</h3>')
lines.append('              <div class="space-y-4">')

# Facebook
lines.append('                <a href="https://www.facebook.com/teambossbabe/" target="_blank" rel="noopener noreferrer"')
lines.append('                  class="flex items-center text-brand-gray hover:text-brand-accent transition group">')
lines.append('                  <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 24 24">')
lines.append('                    <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.076v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.028 24 18.062 24 12.073z" />')
lines.append('                  </svg>')
lines.append('                  <span>Facebook</span>')
lines.append('                </a>')

# LinkedIn
lines.append('                <a href="https://www.linkedin.com/company/boss-babe-enterprise/" target="_blank" rel="noopener noreferrer"')
lines.append('                  class="flex items-center text-brand-gray hover:text-brand-accent transition group">')
lines.append('                  <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 24 24">')
lines.append('                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h-3.564v5.027h3.564v6.286z" />')
lines.append('                  </svg>')
lines.append('                  <span>LinkedIn</span>')
lines.append('                </a>')

# Instagram
lines.append('                <a href="https://www.instagram.com/boss_consultenterprise?igsh=dXcyMG45eHdndWht" target="_blank" rel="noopener noreferrer"')
lines.append('                  class="flex items-center text-brand-gray hover:text-brand-accent transition group">')
lines.append('                  <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 24 24">')
lines.append('                    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.645-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358-2.618 6 6.78-6.98 6.98C8.668 23.986 8.259 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354.2 6.782-2.618 6.98-6.98.058-1.28.072-1.689.072-3.948 0-3.259-.014-3.668-.072-4.948-.2-4.358-2.618-6.78-6.98-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8z" />')
lines.append('                  </svg>')
lines.append('                  <span>Instagram</span>')
lines.append('                </a>')
lines.append('              </div>')
lines.append('            </div>')
lines.append('          </div>')
lines.append('        </div>')
lines.append('      </div>')
lines.append('    </section>')
lines.append('  </div>')

# WhatsApp floating button
lines.append('  <a href="https://wa.me/27632404447" target="_blank" rel="noopener noreferrer"')
lines.append('    lines.append('    class="fixed bottom-6 right-6 z-50 w-14 h-14 bg-green-500 hover:bg-green-600 text-white rounded-full shadow-lg flex items-center justify-center transition duration-300 hover:scale-110"')
lines.append('    aria-label="Chat on WhatsApp">')
lines.append('    <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24">')
lines.append('      <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.149-.28.587-.874.973-.911 1.038-.277.33-.565.366-1.015.183a3.931 3.931 0 01-1.47-.892v5.41 5.41 0 01-1.021-1.275c-.28-.501-.265-.717.198-.995.277-.166.277-.332.193-.578-.083-.247-.75 1.807-.928-2.278-.173-.465-.346-.427-.472-.434l-.386-.008-.001c-.246-.007-.425-.009-.64.119-.217.128-.82.801-.82 1.954 0 1.152.838 2.266 1.689 2.695.2.334.583.714.986 1.066.403.352.723.571.947.716.403.262.717.364.96.448.269.093.518.08.714.05.237-.037 1.022-.417 1.166-.819.144-.402.144-.747.101-.819-.043-.072-.159-.115-.326-.193zM12.078 2.447c-5.218 0-9.456 4.07-9.456 9.048 0 4.979 4.238 9.05 9.456 9.05 2.643 0 5.256-.871 7.266-2.345l5.368 1.408 1.433-5.252a9.934 9.934 0 01-1.656-5.478c0-5.521 4.812-10.238 10.72-10.238 5.161 0 9.982 4.719 9.982 10.238 0 5.518-4.821 10.237-9.982 10.237-2.707 0-5.256-.871-7.266-2.345l-5.368 1.408 1.433-5.252a9.934 9.934 0 01-1.656-5.478c0-5.521 4.812-10.238 10.72-10.238z" />')
lines.append('    </svg>')
lines.append('  </a>')
lines.append('</BaseLayout>')

content = '\n'.join(lines)
with open(filepath, 'w') as f:
    f.write(content)
print("File written successfully.")
