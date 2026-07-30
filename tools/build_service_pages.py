#!/usr/bin/env python3
"""
Fusion Beauty Studio - service page generator.

ONE template + ONE data block below produce all seven service pages, so every
page stays visually and structurally identical.

To change a page's copy: edit SERVICES below, then re-run:

    python tools/build_service_pages.py

To change the LAYOUT of every service page at once: edit TEMPLATE below and re-run.
To change the LOOK of every service page at once: edit the .svc-* block in styles.css
(no need to re-run this script - the pages just link to that stylesheet).

Note: /hydrafacial is NOT generated here. It is a hand-built page and is left alone.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOKING_URL = "https://www.vagaro.com/ca01/fusionbeautystudio"
ASSET_VERSION = "14"          # keep in sync with index.html / hydrafacial (see CLAUDE.md)


# ============================================================================
# TEMPLATE - shared by every service page
# ============================================================================
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Fusion Beauty Studio</title>
  <meta name="description" content="{meta}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Lato:wght@300;400;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/styles.css?v={v}" />
</head>
<body>

  <!-- ===== NAVBAR (shared) ===== -->
  <header class="navbar" id="navbar">
    <div class="nav-inner">
      <a href="/" class="nav-logo">
        <img src="/logo-transparent-dark.png" alt="Fusion Beauty Studio" class="logo-img" />
      </a>
      <nav class="nav-links" id="navLinks">
        <a href="/#about">About</a>
        <a href="/#services">Services</a>
        <a href="/#booking">Booking</a>
        <a href="/#testimonials">Reviews</a>
        <a href="/#contact">Contact</a>
        <a href="{booking}" target="_blank" rel="noopener" class="nav-book-mobile btn btn-primary">Book an Appointment</a>
      </nav>
      <a href="{booking}" target="_blank" rel="noopener" class="btn btn-primary nav-cta">Book Now</a>
      <button class="hamburger" id="hamburger" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- ===== HERO ===== -->
  <section class="svc-hero">
    <img class="svc-hero-img" src="/images/services/{image}" alt="" width="1000" height="1250" decoding="async" />
    <div class="svc-hero-veil"></div>
    <div class="container">
      <div class="svc-hero-inner">
        <p class="section-eyebrow light">{eyebrow}</p>
        <h1 class="svc-hero-title">{title_html}</h1>
        <!-- [PLACEHOLDER COPY] hero tagline -->
        <p class="svc-hero-tagline">{tagline}</p>
        <a href="{booking}" target="_blank" rel="noopener" class="btn btn-primary btn-lg">Book Now</a>
      </div>
    </div>
  </section>

  <!-- ===== INTRO ===== -->
  <section class="svc-intro section">
    <div class="container">
      <div class="svc-intro-inner">
        <p class="section-eyebrow center">The Treatment</p>
        <h2 class="section-title center">{intro_heading}</h2>
        <!-- [PLACEHOLDER COPY] intro - what the treatment is and who it is for -->
{intro_paras}
      </div>
    </div>
  </section>

  <!-- ===== BENEFITS ===== -->
  <section class="svc-benefits section">
    <div class="container">
      <p class="section-eyebrow center">Benefits</p>
      <h2 class="section-title center">Why You'll Love It</h2>
      <!-- [PLACEHOLDER COPY] benefits -->
      <div class="svc-benefits-grid">
{benefits}
      </div>
    </div>
  </section>

  <!-- ===== WHAT TO EXPECT ===== -->
  <section class="svc-steps section">
    <div class="container">
      <p class="section-eyebrow center">Your Visit</p>
      <h2 class="section-title center">What to Expect</h2>
      <!-- [PLACEHOLDER COPY] what to expect -->
      <div class="svc-steps-list">
{steps}
      </div>
    </div>
  </section>

  <!-- ===== CLOSING CTA ===== -->
  <section class="svc-cta section">
    <div class="container">
      <p class="section-eyebrow center light">Ready When You Are</p>
      <h2 class="section-title center light">Book Your <em>{short_name}</em></h2>
      <!-- [PLACEHOLDER COPY] closing line -->
      <p class="section-desc center" style="color:rgba(255,255,255,0.5);">{cta_line}</p>
      <div class="svc-cta-btn">
        <a href="{booking}" target="_blank" rel="noopener" class="btn btn-primary btn-lg">Book Now</a>
      </div>
    </div>
  </section>

  <!-- ===== FOOTER (shared) ===== -->
  <footer class="footer">
    <div class="container footer-inner">
      <div class="footer-logo">
        <a href="/" aria-label="Back to home">
          <img src="/logo-transparent-light.png" alt="Fusion Beauty Studio" />
        </a>
        <p>Edmonton's Premier Laser &amp; Spa</p>
      </div>
      <div class="footer-links">
        <a href="/#about">About</a>
        <a href="/#services">Services</a>
        <a href="{booking}" target="_blank" rel="noopener">Book Now</a>
        <a href="/#contact">Contact</a>
      </div>
      <div class="footer-social">
        <p>Follow Us</p>
        <div class="social-links">
          <a href="https://www.facebook.com/fusionbeautystudio.ca/" target="_blank" rel="noopener" aria-label="Facebook" class="social-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
            </svg>
          </a>
          <a href="https://www.instagram.com/fusionbeautystudio_" target="_blank" rel="noopener" aria-label="Instagram" class="social-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>
              <circle cx="12" cy="12" r="4.5"/>
              <circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/>
            </svg>
          </a>
        </div>
        <div style="margin-top:1.2rem;">
          <a href="tel:+17807095050" style="color:rgba(255,255,255,0.45); font-size:0.85rem;">(780) 709-5050</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Fusion Beauty Studio &mdash; Laser &amp; Spa. All rights reserved. &nbsp;|&nbsp; 376 Allard Blvd SW, Edmonton, Alberta, Canada</p>
    </div>
  </footer>

  <!-- ===== FLOATING BOOK BUTTON (shared) ===== -->
  <a href="{booking}" target="_blank" rel="noopener" class="float-book" id="floatBook">Book Now</a>

  <script src="/script.js?v={v}"></script>
</body>
</html>
"""


# ============================================================================
# DATA - edit the copy here, then re-run this script
# ============================================================================
SERVICES = [
    {
        "slug": "laser-hair-removal",
        "title": "Laser Hair Removal",
        "title_html": "Laser <em>Hair Removal</em>",
        "short_name": "Laser Session",
        "eyebrow": "Smooth, Lasting Results",
        "image": "laser-hair-removal.jpg",
        "meta": "Laser hair removal in Edmonton at Fusion Beauty Studio, using the medical-grade Alma Soprano ICE Platinum. Comfortable and effective on all skin types.",
        "tagline": "Powered by the medical-grade Alma Soprano ICE Platinum - one of the best lasers in the world. Safe, comfortable, and effective on all skin types.",
        "intro_heading": "Say Goodbye to<br /><em>Daily Shaving</em>",
        "intro": [
            "Laser hair removal uses gentle pulses of light to target the hair follicle, reducing regrowth treatment after treatment. Our Alma Soprano ICE Platinum is a medical-grade system designed for comfort, with cooling technology that keeps the experience easy from start to finish.",
            "It's a wonderful fit if you're tired of shaving, waxing, or dealing with ingrown hairs, and it's suitable for all skin types and tones. We'll walk you through everything at your consultation and build a plan around your skin, your hair, and your goals.",
        ],
        "benefits": [
            ("Comfortable by design", "The Soprano ICE Platinum's cooling tip keeps the treatment gentle, even across larger areas."),
            ("Safe for all skin tones", "Advanced wavelength technology makes it suitable for the full range of skin types."),
            ("Fewer ingrown hairs", "A welcome relief if shaving or waxing has left you with irritation and bumps."),
            ("Smoother over time", "Results build with each session as treated follicles produce finer, sparser hair."),
            ("Treats most areas", "From smaller facial areas to larger areas like legs, underarms, and back."),
            ("Low maintenance", "Less time spent shaving, and no more last-minute waxing appointments."),
        ],
        "steps": [
            ("Consultation & patch test", "We assess your skin and hair, talk through your goals, and carry out a patch test to make sure you're a good candidate."),
            ("Preparing the area", "The area is cleansed and shaved if needed. You'll be given protective eyewear before we begin."),
            ("Your treatment", "The handpiece glides over the skin delivering cooled pulses. Most clients describe it as a warm, gentle sensation."),
            ("Aftercare", "We'll apply a soothing product and go through simple aftercare - typically avoiding sun exposure and heat for a short period."),
            ("Your next session", "Hair grows in cycles, so a course of sessions spaced apart gives the best result. We'll map out your schedule together."),
        ],
        "cta_line": "Book your consultation and let's build a plan for smooth, low-maintenance skin.",
    },
    {
        "slug": "waxing-threading",
        "title": "Waxing & Threading",
        "title_html": "Waxing <em>&amp; Threading</em>",
        "short_name": "Appointment",
        "eyebrow": "Precise & Gentle",
        "image": "waxing-threading.jpg",
        "meta": "Waxing and threading in Edmonton at Fusion Beauty Studio. Gentle, precise hair removal for smooth, long-lasting results.",
        "tagline": "Gentle, precise hair removal for smooth, long-lasting results. Full body waxing and expert threading.",
        "intro_heading": "Smooth Skin,<br /><em>Beautifully Done</em>",
        "intro": [
            "Waxing lifts hair from the root for results that last far longer than shaving, while threading offers incredible precision - especially around the brows and face, where every hair counts.",
            "Our team works quickly, cleanly, and with a great deal of care. Whether it's your first appointment or part of your regular routine, we'll make sure you're comfortable throughout and leave feeling polished.",
        ],
        "benefits": [
            ("Longer-lasting than shaving", "Hair is removed from the root, so skin stays smooth for noticeably longer."),
            ("Precision where it matters", "Threading gives beautifully clean, defined lines around the brows and face."),
            ("Softer regrowth", "Regular appointments tend to leave regrowth finer and easier to manage."),
            ("Full body options", "From brows and lip to legs, underarms, and full body waxing."),
            ("Gentle on sensitive skin", "Threading uses only thread - no heat, no chemicals - making it a great option for delicate areas."),
            ("Quick and efficient", "An easy appointment to fit into a busy week."),
        ],
        "steps": [
            ("A quick chat", "We'll confirm the areas you'd like treated and check for anything that might affect your appointment."),
            ("Preparing the skin", "The area is cleansed and prepped so the wax or thread can work effectively and comfortably."),
            ("Your treatment", "We work in small sections, keeping you comfortable and checking in as we go."),
            ("Soothing finish", "A calming product is applied to settle the skin before you head out."),
            ("Aftercare", "We'll share simple tips to keep skin happy and reduce the chance of ingrown hairs."),
        ],
        "cta_line": "Book your appointment and enjoy smooth, beautifully finished skin.",
    },
    {
        "slug": "skincare-facials",
        "title": "Skincare & Facials",
        "title_html": "Skincare <em>&amp; Facials</em>",
        "short_name": "Facial",
        "eyebrow": "Tailored to Your Skin",
        "image": "skincare-facials.jpg",
        "meta": "Custom facials in Edmonton at Fusion Beauty Studio - dermaplaning, chemical peels, and BB Glow, tailored to your skin's needs.",
        "tagline": "Custom facials, dermaplaning, chemical peels, and BB Glow tailored to your skin's needs.",
        "intro_heading": "A Facial Built<br /><em>Around You</em>",
        "intro": [
            "No two complexions are the same, so we don't treat them that way. Every facial begins with a proper look at your skin, then we build the treatment around what it actually needs - whether that's deep hydration, gentle resurfacing, or simply a reset.",
            "Our menu includes custom facials, dermaplaning, chemical peels, and BB Glow. If you're not sure where to start, that's completely normal - tell us your goals and we'll guide you to the right option.",
        ],
        "benefits": [
            ("Completely personalised", "Products and technique are chosen for your skin on the day, not a fixed formula."),
            ("A visible refresh", "Skin looks cleaner, brighter, and more even after your appointment."),
            ("Deep hydration", "Nourishing products help restore comfort and bounce to dry or tired skin."),
            ("Smoother texture", "Gentle resurfacing options help soften rough patches and dullness."),
            ("Expert guidance", "We'll explain what we're seeing and what will genuinely help - no pressure."),
            ("A moment for yourself", "Deeply relaxing, and a lovely way to reset."),
        ],
        "steps": [
            ("Skin consultation", "We look closely at your skin and talk through your concerns, routine, and goals."),
            ("Cleanse & prep", "A thorough double cleanse removes makeup, sunscreen, and the day's buildup."),
            ("Your custom treatment", "The core of your facial - chosen for your skin, whether that's exfoliation, extraction, or intense hydration."),
            ("Mask & massage", "A treatment mask paired with relaxing facial massage."),
            ("Finish & aftercare", "Serums, moisturiser, and SPF, plus simple guidance on caring for your skin at home."),
        ],
        "cta_line": "Book your facial and let's give your skin exactly what it's asking for.",
    },
    {
        "slug": "microneedling-peel",
        "title": "Microneedling & Peel",
        "title_html": "Microneedling <em>&amp; Peel</em>",
        "short_name": "Treatment",
        "eyebrow": "Renew & Refine",
        "image": "microneedling-peel.jpg",
        "meta": "Microneedling and chemical peels in Edmonton at Fusion Beauty Studio. Collagen-boosting treatments to smooth texture and renew your skin.",
        "tagline": "Advanced collagen-boosting treatments to smooth texture, soften fine lines, and renew your skin.",
        "intro_heading": "Smoother, Firmer,<br /><em>Renewed</em>",
        "intro": [
            "Microneedling works by creating tiny micro-channels in the skin, prompting your body's natural renewal response. Paired with a peel, it's one of the most effective ways to refine texture and bring back a fresher, smoother surface.",
            "It's a popular choice for softening the look of fine lines, uneven tone, scarring, and enlarged pores. Because it works with your skin's own renewal process, results build gradually and look natural.",
        ],
        "benefits": [
            ("Smoother texture", "Helps refine rough, uneven skin for a softer, more polished finish."),
            ("Softens fine lines", "Improves the appearance of fine lines and early signs of ageing."),
            ("Refines pores", "Helps reduce the look of enlarged pores over a course of treatments."),
            ("Improves tone", "A great option for uneven tone, dullness, and the appearance of marks left behind by breakouts."),
            ("Natural-looking results", "Works with your skin's own renewal process, so the change looks like you."),
            ("Builds over time", "Results continue to develop in the weeks following your appointment."),
        ],
        "steps": [
            ("Consultation", "We assess your skin, discuss your goals, and confirm the treatment is right for you."),
            ("Preparation", "Skin is thoroughly cleansed and prepped before we begin."),
            ("Your treatment", "We work methodically across the treatment area, keeping you comfortable throughout."),
            ("Calming finish", "Soothing serums are applied to settle and support the skin."),
            ("Recovery & aftercare", "We'll explain exactly what to expect afterwards and how to care for your skin while it renews."),
        ],
        "cta_line": "Book a consultation and let's build a plan for smoother, renewed skin.",
    },
    {
        "slug": "massage",
        "title": "Massage",
        "title_html": "<em>Massage</em>",
        "short_name": "Massage",
        "eyebrow": "Rest & Restore",
        "image": "massage.jpg",
        "meta": "Relaxing and therapeutic massage in Edmonton at Fusion Beauty Studio. Ease tension and restore your body.",
        "tagline": "Relaxing and therapeutic massage treatments to ease tension and restore your body.",
        "intro_heading": "Release Tension,<br /><em>Restore Calm</em>",
        "intro": [
            "Whether you're carrying tension in your shoulders from long days at a desk, or you simply need an hour that belongs entirely to you, our massage treatments are designed to help you properly switch off.",
            "We'll adapt pressure and focus to suit you - lighter and more relaxing, or firmer and more therapeutic through the areas that need it most. Just tell us what you need on the day.",
        ],
        "benefits": [
            ("Eases muscle tension", "Focused work through tight areas like the neck, shoulders, and back."),
            ("Deeply relaxing", "A calm, unhurried treatment in a peaceful setting."),
            ("Pressure to suit you", "From gentle and soothing to firm and therapeutic - entirely your call."),
            ("Supports better rest", "Many clients find they sleep beautifully afterwards."),
            ("A genuine reset", "Time away from screens, messages, and to-do lists."),
            ("Lovely as a regular ritual", "Works well as a standing appointment to stay ahead of tension."),
        ],
        "steps": [
            ("A quick consultation", "We'll ask about problem areas, pressure preference, and anything we should avoid."),
            ("Settling in", "You'll be made comfortable in a warm, quiet treatment room."),
            ("Your massage", "We work through the areas you've asked us to focus on, checking pressure as we go."),
            ("Coming back slowly", "A few quiet moments at the end so you're not rushed."),
            ("Aftercare", "Simple suggestions - usually water, warmth, and taking it easy."),
        ],
        "cta_line": "Book your massage and give yourself the hour you've been putting off.",
    },
    {
        "slug": "eyes-brows",
        "title": "Eyes & Brows",
        "title_html": "Eyes <em>&amp; Brows</em>",
        "short_name": "Appointment",
        "eyebrow": "Beautifully Defined",
        "image": "eyes-brows.jpg",
        "meta": "Lash extensions, brow shaping, threading, tinting, and lamination in Edmonton at Fusion Beauty Studio.",
        "tagline": "Lash extensions, brow shaping, threading, tinting, and lamination for perfectly defined eyes.",
        "intro_heading": "Framed to<br /><em>Perfection</em>",
        "intro": [
            "Brows frame the whole face, and lashes finish it. Our team shapes, tints, laminates, and extends with a careful eye on what suits your features - never a one-size-fits-all template.",
            "Whether you'd like a soft, natural definition or something fuller and more dramatic, we'll talk it through first so you know exactly what you're getting before we start.",
        ],
        "benefits": [
            ("Shaped to your face", "Brows mapped and shaped to complement your features."),
            ("Wake up ready", "Lash extensions and tinting cut your morning routine right down."),
            ("Natural or dramatic", "Classic, hybrid, and volume options to suit the look you want."),
            ("Fuller-looking brows", "Lamination and tinting help sparse brows look neater and fuller."),
            ("Precise threading", "Clean, defined lines with a technique that's gentle on delicate skin."),
            ("Long-lasting", "Results that hold beautifully between appointments."),
        ],
        "steps": [
            ("Consultation & mapping", "We discuss the look you're after and map your brows to suit your face shape."),
            ("Preparation", "The area is cleansed and prepped, and your lower lashes protected where needed."),
            ("Your treatment", "Shaping, tinting, lamination, or lash application - carried out with care and precision."),
            ("The reveal", "We check the result with you and make any final refinements."),
            ("Aftercare", "Simple guidance to keep lashes and brows looking their best for as long as possible."),
        ],
        "cta_line": "Book your appointment and let's frame your face beautifully.",
    },
    {
        "slug": "makeup",
        "title": "Makeup",
        "title_html": "<em>Makeup</em>",
        "short_name": "Makeup Appointment",
        "eyebrow": "For Your Big Moments",
        "image": "makeup.jpg",
        "meta": "Professional makeup application in Edmonton at Fusion Beauty Studio for weddings, events, and special occasions.",
        "tagline": "Professional makeup application for weddings, events, and every special occasion.",
        "intro_heading": "Polished for<br /><em>Every Occasion</em>",
        "intro": [
            "Whether it's your wedding day, a milestone celebration, or an evening you want to feel your absolute best for, professional makeup makes all the difference - especially in photographs.",
            "We work with you to create a look that still feels like you: your colouring, your features, your style. Nothing heavy, nothing generic, and nothing you won't recognise in the mirror.",
        ],
        "benefits": [
            ("Made for photographs", "Applied with an eye on how it reads on camera as well as in person."),
            ("Still looks like you", "Enhancing your features rather than covering them."),
            ("Built to last", "Products and technique chosen to hold up through a long day or evening."),
            ("Bridal specialists", "Beautiful, timeless looks for your wedding day."),
            ("Any occasion", "Weddings, engagements, graduations, birthdays, and nights out."),
            ("A relaxed experience", "An unhurried appointment so you can properly enjoy getting ready."),
        ],
        "steps": [
            ("Consultation", "We talk through your outfit, the occasion, and the look you have in mind."),
            ("Skin prep", "Cleansing, hydrating, and priming so everything sits beautifully and lasts."),
            ("Your application", "Base, eyes, brows, and lips, checking in with you as the look comes together."),
            ("Final refinements", "We adjust anything you'd like softened or intensified until you're delighted."),
            ("Setting & touch-ups", "The look is set, and we'll suggest what to carry with you for the day."),
        ],
        "cta_line": "Book your appointment and let's get you ready for the occasion.",
    },
]


# ============================================================================
# BUILD
# ============================================================================
def typo(s):
    """Copy above is written with plain ASCII hyphens so this file stays
    encoding-safe; render them as proper em dashes to match the site's
    typography."""
    return s.replace(" - ", " &mdash; ")


def render_intro(paras):
    return "\n".join(
        '        <p class="svc-intro-text">%s</p>' % typo(p) for p in paras
    )


def render_benefits(items):
    out = []
    for heading, body in items:
        out.append(
            '        <div class="svc-benefit">\n'
            '          <h3>%s</h3>\n'
            '          <p>%s</p>\n'
            '        </div>' % (heading, typo(body))
        )
    return "\n\n".join(out)


def render_steps(items):
    out = []
    for i, (heading, body) in enumerate(items, start=1):
        out.append(
            '        <div class="svc-step">\n'
            '          <div class="svc-step-num">%02d</div>\n'
            '          <div>\n'
            '            <h3>%s</h3>\n'
            '            <p>%s</p>\n'
            '          </div>\n'
            '        </div>' % (i, heading, typo(body))
        )
    return "\n\n".join(out)


def build():
    for svc in SERVICES:
        html = TEMPLATE.format(
            v=ASSET_VERSION,
            booking=BOOKING_URL,
            title=svc["title"],
            title_html=svc["title_html"],
            short_name=svc["short_name"],
            eyebrow=svc["eyebrow"],
            image=svc["image"],
            meta=svc["meta"],
            tagline=typo(svc["tagline"]),
            intro_heading=svc["intro_heading"],
            intro_paras=render_intro(svc["intro"]),
            benefits=render_benefits(svc["benefits"]),
            steps=render_steps(svc["steps"]),
            cta_line=typo(svc["cta_line"]),
        )

        out_dir = os.path.join(ROOT, svc["slug"])
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print("wrote %s/index.html  (%d bytes)" % (svc["slug"], len(html)))

    print("\n%d service pages generated." % len(SERVICES))


if __name__ == "__main__":
    build()
