import streamlit as st

st.set_page_config(
    page_title="Delta-X Web Solutions",
    page_icon="🚀",
    layout="wide"
)

# CSS Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #000000);
    color: white;
}

.main-title {
    font-size: 85px;
    font-weight: 900;
    text-align: center;
    color: #38bdf8;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 26px;
    text-align: center;
    color: #e2e8f0;
}

.small-text {
    font-size: 18px;
    text-align: center;
    color: #cbd5e1;
}

.section-title {
    font-size: 42px;
    font-weight: bold;
    margin-top: 60px;
    color: #38bdf8;
    text-align: center;
}

.card {
    background-color: #111827;
    padding: 28px;
    border-radius: 22px;
    margin-top: 20px;
    box-shadow: 0px 0px 18px rgba(56,189,248,0.25);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 30px rgba(56,189,248,0.55);
}

.price-box {
    background: linear-gradient(135deg, #082f49, #0f766e);
    padding: 35px;
    border-radius: 25px;
    margin-top: 25px;
    text-align: center;
    box-shadow: 0px 0px 30px rgba(56,189,248,0.4);
}

.contact-box {
    background-color: #0f172a;
    padding: 35px;
    border-radius: 25px;
    margin-top: 25px;
    text-align: center;
    box-shadow: 0px 0px 25px rgba(34,197,94,0.35);
}

.badge {
    background-color: #0369a1;
    padding: 10px 18px;
    border-radius: 30px;
    display: inline-block;
    margin: 8px;
    font-size: 17px;
}

.whatsapp-button {
    background-color: #22c55e;
    color: white;
    padding: 16px 28px;
    border-radius: 40px;
    text-decoration: none;
    font-size: 22px;
    font-weight: bold;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<p class="main-title">🚀 DELTA-X</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Premium Websites For Businesses That Want More Customers</p>',
    unsafe_allow_html=True
)
st.markdown(
    '<p class="small-text">Modern • Fast • Mobile Friendly • SEO Ready • Affordable</p>',
    unsafe_allow_html=True
)

st.markdown("""
<center>
<span class="badge">⚡ 24-48 Hours Delivery</span>
<span class="badge">📱 Mobile Responsive</span>
<span class="badge">💬 WhatsApp Integration</span>
<span class="badge">🔍 SEO Ready</span>
</center>
""", unsafe_allow_html=True)

# CTA
st.markdown("""
<br>
<center>
<a class="whatsapp-button" href="https://wa.me/918076664925" target="_blank">
💬 Get Free Consultation
</a>
</center>
""", unsafe_allow_html=True)

# Services
st.markdown('<p class="section-title">Our Services</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h2>🏢 Business Websites</h2>
    <p>Professional websites for shops, gyms, cafes, clinics, schools, and local businesses.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h2>👨‍💻 Portfolio Websites</h2>
    <p>Modern portfolio websites for students, freelancers, creators, and professionals.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h2>🎯 Landing Pages</h2>
    <p>High-converting pages with contact buttons, WhatsApp links, and mobile optimization.</p>
    </div>
    """, unsafe_allow_html=True)

# Pricing
st.markdown('<p class="section-title">🔥 Limited Time Launch Offer</p>', unsafe_allow_html=True)

st.markdown("""
<div class="price-box">
<h2>💎 Professional Starter Website</h2>
<h1 style="color:#facc15; font-size:60px;">₹1000</h1>
<h3><strike>Regular Price ₹1500</strike></h3>

<p style="font-size:20px;">
✔ Mobile Friendly Design<br>
✔ WhatsApp Integration<br>
✔ Contact Form<br>
✔ Fast Loading Website<br>
✔ Basic SEO Setup<br>
✔ Free Beginner Support<br>
✔ Professional Business Look
</p>

<h3 style="color:#facc15;">
Offer Valid For First-Time Clients Only
</h3>
</div>
""", unsafe_allow_html=True)

# Why Choose Us
st.markdown('<p class="section-title">Why Choose DELTA-X?</p>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
✅ Professional Modern Design<br><br>
✅ Delivery Within 24-48 Hours<br><br>
✅ Mobile & Tablet Responsive<br><br>
✅ Google SEO Friendly Website<br><br>
✅ WhatsApp Chat Button<br><br>
✅ Clean Business Presentation<br><br>
✅ Affordable Pricing For Small Businesses
</div>
""", unsafe_allow_html=True)

# Portfolio
st.markdown('<p class="section-title">Sample Website Ideas</p>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class="card">
    <h2>🍽 Restaurant Website</h2>
    <p>Menu, photos, location, WhatsApp order button, and customer contact section.</p>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="card">
    <h2>📚 Coaching Website</h2>
    <p>Course details, admission inquiry form, student reviews, and contact button.</p>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="card">
    <h2>🏥 Clinic Website</h2>
    <p>Doctor profile, services, timing, appointment button, and Google Map location.</p>
    </div>
    """, unsafe_allow_html=True)

# Testimonials
st.markdown('<p class="section-title">Client Reviews</p>', unsafe_allow_html=True)

r1, r2 = st.columns(2)

with r1:
    st.markdown("""
    <div class="card">
    <h2>⭐⭐⭐⭐⭐</h2>
    <p>"Very professional website delivered quickly."</p>
    <b>— Local Business Owner</b>
    </div>
    """, unsafe_allow_html=True)

with r2:
    st.markdown("""
    <div class="card">
    <h2>⭐⭐⭐⭐⭐</h2>
    <p>"Website helped us get more customer inquiries."</p>
    <b>— Coaching Institute</b>
    </div>
    """, unsafe_allow_html=True)

# FAQ
st.markdown('<p class="section-title">Frequently Asked Questions</p>', unsafe_allow_html=True)

with st.expander("How fast can you deliver my website?"):
    st.write("Most basic websites can be delivered within 24-48 hours after receiving details.")

with st.expander("Will my website work on mobile?"):
    st.write("Yes, every website is designed to work on mobile, tablet, and desktop.")

with st.expander("Can you add WhatsApp button?"):
    st.write("Yes, WhatsApp chat button can be added so customers can directly contact you.")

with st.expander("What details are required from client?"):
    st.write("Business name, services, contact number, address, photos/logo if available, and any special requirement.")

# Contact Form
st.markdown('<p class="section-title">Start Your Website Today</p>', unsafe_allow_html=True)

name = st.text_input("Your Name")
business = st.text_input("Business Name")
phone = st.text_input("Mobile / WhatsApp Number")
requirement = st.text_area("Tell us what type of website you need")

if st.button("Submit Inquiry"):
    st.success("Thank you! Your inquiry has been received. We will contact you soon.")

# Contact Box
st.markdown("""
<div class="contact-box">
<h1 style="color:#38bdf8;">📞 8076664925</h1>
<h2>📞 9213458804</h2>
<h3 style="color:#facc15;">FREE CONSULTATION AVAILABLE</h3>
<p>Call or WhatsApp Now and Get Your Business Online Today.</p>
<br>
<a class="whatsapp-button" href="https://wa.me/918076664925" target="_blank">
💬 Chat on WhatsApp
</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
© 2026 DELTA-X Web Solutions • Modern Websites for Modern Businesses
</div>
""", unsafe_allow_html=True)
