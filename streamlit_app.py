import streamlit as st

st.set_page_config(
    page_title="Delta-X Web Solutions",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #000000);
    color: white;
}

.block-container {
    padding-top: 25px;
    padding-bottom: 40px;
}

.hero {
    text-align: center;
    padding: 60px 20px 45px 20px;
    border-radius: 30px;
    background: radial-gradient(circle at top, #075985, #020617 60%);
    box-shadow: 0px 0px 45px rgba(56,189,248,0.35);
}

.main-title {
    font-size: 115px;
    font-weight: 1000;
    color: #38bdf8;
    letter-spacing: 4px;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 30px;
    color: #ffffff;
    font-weight: 700;
}

.tagline {
    font-size: 20px;
    color: #cbd5e1;
    margin-top: 15px;
}

.section-title {
    font-size: 46px;
    font-weight: 900;
    margin-top: 70px;
    margin-bottom: 25px;
    color: #38bdf8;
    text-align: center;
}

.card {
    background: linear-gradient(145deg, #111827, #020617);
    padding: 28px;
    border-radius: 24px;
    margin-top: 20px;
    min-height: 210px;
    box-shadow: 0px 0px 18px rgba(56,189,248,0.22);
    border: 1px solid rgba(56,189,248,0.22);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 0px 35px rgba(56,189,248,0.55);
}

.price-box {
    background: linear-gradient(135deg, #082f49, #0f766e);
    padding: 40px;
    border-radius: 28px;
    text-align: center;
    box-shadow: 0px 0px 35px rgba(34,211,238,0.45);
    border: 1px solid #38bdf8;
}

.contact-box {
    background: linear-gradient(135deg, #052e16, #0f172a);
    padding: 38px;
    border-radius: 28px;
    text-align: center;
    box-shadow: 0px 0px 30px rgba(34,197,94,0.38);
}

.badge {
    background-color: rgba(14,165,233,0.20);
    border: 1px solid #38bdf8;
    padding: 11px 18px;
    border-radius: 40px;
    display: inline-block;
    margin: 8px;
    font-size: 17px;
    color: #e0f2fe;
}

.cta-button {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: white !important;
    padding: 18px 34px;
    border-radius: 45px;
    text-decoration: none;
    font-size: 23px;
    font-weight: 900;
    display: inline-block;
    margin-top: 25px;
    box-shadow: 0px 0px 25px rgba(34,197,94,0.45);
}

.stats-box {
    text-align: center;
    background-color: #020617;
    padding: 25px;
    border-radius: 22px;
    border: 1px solid rgba(56,189,248,0.25);
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 55px;
    font-size: 15px;
}

@media only screen and (max-width: 768px) {
    .main-title {
        font-size: 58px;
        letter-spacing: 1px;
    }

    .subtitle {
        font-size: 22px;
    }

    .tagline {
        font-size: 16px;
    }

    .section-title {
        font-size: 32px;
    }

    .card {
        min-height: auto;
        padding: 22px;
    }

    .price-box {
        padding: 25px;
    }

    .cta-button {
        font-size: 18px;
        padding: 14px 22px;
    }
}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <div class="main-title">DELTA-X</div>
    <div class="subtitle">Premium Websites That Bring More Customers</div>
    <div class="tagline">
        AI-Powered • Mobile Friendly • SEO Ready • Fast Delivery • Business Focused
    </div>

    <div style="margin-top:25px;">
        <span class="badge">⚡ 24-48 Hours Delivery</span>
        <span class="badge">📱 Phone + PC Responsive</span>
        <span class="badge">🔍 SEO Optimized</span>
        <span class="badge">💬 WhatsApp Leads</span>
    </div>

    <a class="cta-button" href="https://wa.me/918076664925" target="_blank">
        💬 Get Free Website Consultation
    </a>
</div>
""", unsafe_allow_html=True)

# STATS
st.markdown('<p class="section-title">Why Your Business Needs a Website</p>', unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown('<div class="stats-box"><h1>24/7</h1><p>Online Presence</p></div>', unsafe_allow_html=True)

with s2:
    st.markdown('<div class="stats-box"><h1>More</h1><p>Customer Trust</p></div>', unsafe_allow_html=True)

with s3:
    st.markdown('<div class="stats-box"><h1>Fast</h1><p>Lead Generation</p></div>', unsafe_allow_html=True)

with s4:
    st.markdown('<div class="stats-box"><h1>Low</h1><p>Marketing Cost</p></div>', unsafe_allow_html=True)

# SERVICES
st.markdown('<p class="section-title">Our Website Services</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h2>🏢 Business Websites</h2>
    <p>Websites for shops, clinics, restaurants, gyms, schools, coaching centers, and local services.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h2>🎯 Landing Pages</h2>
    <p>Single-page websites designed to convert visitors into calls, WhatsApp messages, and inquiries.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h2>👨‍💻 Portfolio Websites</h2>
    <p>Modern profile websites for freelancers, students, creators, consultants, and professionals.</p>
    </div>
    """, unsafe_allow_html=True)

# FEATURES INSPIRED BY TOP WEBSITE BUILDERS
st.markdown('<p class="section-title">Advanced Features Included</p>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="card">
    <h2>🤖 AI-Style Smart Design</h2>
    <p>Modern layouts, clean sections, attractive content, and business-ready structure.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="card">
    <h2>📱 Responsive Layout</h2>
    <p>Your website will look proper on phone, tablet, laptop, and desktop.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="card">
    <h2>🔍 SEO Ready</h2>
    <p>Basic Google-friendly structure, headings, service keywords, and fast loading design.</p>
    </div>
    """, unsafe_allow_html=True)

f4, f5, f6 = st.columns(3)

with f4:
    st.markdown("""
    <div class="card">
    <h2>💬 WhatsApp Button</h2>
    <p>Customers can contact you directly on WhatsApp with one click.</p>
    </div>
    """, unsafe_allow_html=True)

with f5:
    st.markdown("""
    <div class="card">
    <h2>📊 Lead Focused Sections</h2>
    <p>Clear pricing, services, testimonials, FAQ, and call-to-action areas.</p>
    </div>
    """, unsafe_allow_html=True)

with f6:
    st.markdown("""
    <div class="card">
    <h2>⚡ Fast Loading</h2>
    <p>Lightweight design made for quick opening and better user experience.</p>
    </div>
    """, unsafe_allow_html=True)

# TOP PLATFORM FEATURE ANALYSIS
st.markdown('<p class="section-title">Features Inspired From Top Website Platforms</p>', unsafe_allow_html=True)

platform_data = [
    ["Wix", "AI website creation + templates", "Smart ready-made sections"],
    ["Webflow", "Professional design control", "Premium agency-style layout"],
    ["Framer", "Fast websites + SEO", "Modern hero and clean spacing"],
    ["WordPress", "Flexible content sections", "Blog/service-ready structure"],
    ["Shopify", "Conversion-focused selling", "Strong CTA and offer box"],
    ["Squarespace", "Elegant visual design", "Clean premium cards"],
    ["Hostinger", "AI builder simplicity", "Quick delivery message"],
    ["GoDaddy", "Small business focus", "Local business service sections"],
    ["Weebly", "Simple drag-drop style", "Easy readable layout"],
    ["Duda", "Agency/client websites", "Professional service presentation"],
]

st.table(platform_data)

# PRICING
st.markdown('<p class="section-title">Limited Time Launch Offer</p>', unsafe_allow_html=True)

st.markdown("""
<div class="price-box">
<h2>💎 Professional Starter Website</h2>
<h1 style="color:#facc15; font-size:70px;">₹1000</h1>
<h3><strike>Regular Price ₹1500</strike></h3>

<p style="font-size:21px; line-height:1.8;">
✔ Modern Homepage Design<br>
✔ Mobile + PC Responsive Layout<br>
✔ WhatsApp Chat Button<br>
✔ Contact / Inquiry Form<br>
✔ Service Section<br>
✔ Pricing Section<br>
✔ Testimonials Section<br>
✔ Basic SEO Setup<br>
✔ Fast Delivery<br>
✔ Free Beginner Support
</p>

<h3 style="color:#facc15;">First-Time Client Special Offer</h3>
</div>
""", unsafe_allow_html=True)

# WEBSITE TYPES
st.markdown('<p class="section-title">Websites We Can Build</p>', unsafe_allow_html=True)

w1, w2, w3 = st.columns(3)

with w1:
    st.markdown("""
    <div class="card">
    <h2>🍽 Restaurant Website</h2>
    <p>Menu, photos, timing, location, WhatsApp order button, and customer inquiry.</p>
    </div>
    """, unsafe_allow_html=True)

with w2:
    st.markdown("""
    <div class="card">
    <h2>📚 Coaching Website</h2>
    <p>Courses, admission inquiry, teacher profile, student reviews, and contact form.</p>
    </div>
    """, unsafe_allow_html=True)

with w3:
    st.markdown("""
    <div class="card">
    <h2>🏥 Clinic Website</h2>
    <p>Doctor profile, services, appointment button, timings, and Google map section.</p>
    </div>
    """, unsafe_allow_html=True)

w4, w5, w6 = st.columns(3)

with w4:
    st.markdown("""
    <div class="card">
    <h2>🏋️ Gym Website</h2>
    <p>Plans, trainer details, photos, monthly package, and joining inquiry button.</p>
    </div>
    """, unsafe_allow_html=True)

with w5:
    st.markdown("""
    <div class="card">
    <h2>🏠 Property Dealer Website</h2>
    <p>Property listings, location details, contact button, and lead generation form.</p>
    </div>
    """, unsafe_allow_html=True)

with w6:
    st.markdown("""
    <div class="card">
    <h2>🛒 Small Shop Website</h2>
    <p>Products, offers, store timing, address, and WhatsApp inquiry button.</p>
    </div>
    """, unsafe_allow_html=True)

# PROCESS
st.markdown('<p class="section-title">How We Work</p>', unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.markdown('<div class="card"><h2>1️⃣ Details</h2><p>You share business name, phone, services, and photos.</p></div>', unsafe_allow_html=True)

with p2:
    st.markdown('<div class="card"><h2>2️⃣ Design</h2><p>We create a modern website design for your business.</p></div>', unsafe_allow_html=True)

with p3:
    st.markdown('<div class="card"><h2>3️⃣ Review</h2><p>You check the website and suggest changes.</p></div>', unsafe_allow_html=True)

with p4:
    st.markdown('<div class="card"><h2>4️⃣ Delivery</h2><p>Final website is delivered with contact buttons.</p></div>', unsafe_allow_html=True)

# REVIEWS
st.markdown('<p class="section-title">Client Reviews</p>', unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)

with r1:
    st.markdown("""
    <div class="card">
    <h2>⭐⭐⭐⭐⭐</h2>
    <p>"Very professional website and quick delivery."</p>
    <b>— Local Business Owner</b>
    </div>
    """, unsafe_allow_html=True)

with r2:
    st.markdown("""
    <div class="card">
    <h2>⭐⭐⭐⭐⭐</h2>
    <p>"Good design and easy WhatsApp contact button."</p>
    <b>— Coaching Center</b>
    </div>
    """, unsafe_allow_html=True)

with r3:
    st.markdown("""
    <div class="card">
    <h2>⭐⭐⭐⭐⭐</h2>
    <p>"Affordable service for small businesses."</p>
    <b>— Shop Owner</b>
    </div>
    """, unsafe_allow_html=True)

# FAQ
st.markdown('<p class="section-title">Frequently Asked Questions</p>', unsafe_allow_html=True)

with st.expander("Will the website work properly on mobile and PC?"):
    st.write("Yes, the website is designed to look proper on mobile, tablet, laptop, and desktop.")

with st.expander("How fast can you deliver the website?"):
    st.write("Most basic business websites can be delivered within 24-48 hours after receiving all details.")

with st.expander("Can you add WhatsApp button?"):
    st.write("Yes, WhatsApp button can be added so customers can directly message you.")

with st.expander("What details do you need?"):
    st.write("Business name, services, phone number, address, logo/photos if available, and your preferred colors.")

with st.expander("Is ₹1000 the final price?"):
    st.write("₹1000 is the first-time starter offer. Extra pages or advanced features may cost more.")

# CONTACT FORM
st.markdown('<p class="section-title">Start Your Website Today</p>', unsafe_allow_html=True)

with st.form("contact_form"):
    name = st.text_input("Your Name")
    business = st.text_input("Business Name")
    phone = st.text_input("Mobile / WhatsApp Number")
    website_type = st.selectbox(
        "Website Type",
        ["Business Website", "Landing Page", "Portfolio Website", "Restaurant Website", "Coaching Website", "Clinic Website", "Other"]
    )
    requirement = st.text_area("Tell us your requirement")
    submitted = st.form_submit_button("Submit Inquiry")

    if submitted:
        st.success("Thank you! Your inquiry has been received. Please call or WhatsApp us for faster response.")

# CONTACT BOX
st.markdown("""
<div class="contact-box">
<h1 style="color:#38bdf8;">📞 8076664925</h1>
<h2>📞 9213458804</h2>
<h3 style="color:#facc15;">FREE CONSULTATION AVAILABLE</h3>
<p style="font-size:20px;">Call or WhatsApp now and get your business online.</p>

<a class="cta-button" href="https://wa.me/918076664925" target="_blank">
💬 Chat on WhatsApp
</a>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
© 2026 DELTA-X Web Solutions • Premium Websites for Modern Businesses
</div>
""", unsafe_allow_html=True)
