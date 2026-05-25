import streamlit as st

st.set_page_config(
    page_title="Delta Website",
    page_icon="💻",
    layout="wide"
)

# Background Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #020617, #0f172a, #000000);
    color: white;
}

.main-title {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    color: #38bdf8;
}

.subtitle {
    font-size: 22px;
    text-align: center;
    color: #cbd5e1;
}

.section-title {
    font-size: 40px;
    font-weight: bold;
    margin-top: 50px;
    color: #38bdf8;
}

.card {
    background-color: #111827;
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0px 0px 15px rgba(56,189,248,0.3);
}

.price-box {
    background-color: #082f49;
    padding: 20px;
    border-radius: 20px;
    margin-top: 20px;
}

.contact-box {
    background-color: #0f172a;
    padding: 20px;
    border-radius: 20px;
    margin-top: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<p class="main-title">Delta Website</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Modern • Fast • Affordable Websites for Small Businesses</p>',
    unsafe_allow_html=True
)

st.write("")

# Services Section
st.markdown(
    '<p class="section-title">Our Services</p>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h2>Business Websites</h2>
    <p>Professional websites for shops, gyms, cafes, and local businesses.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h2>Portfolio Websites</h2>
    <p>Modern portfolio websites for creators, students, and freelancers.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h2>Landing Pages</h2>
    <p>High-converting pages with WhatsApp integration and mobile optimization.</p>
    </div>
    """, unsafe_allow_html=True)

# Pricing Section
st.markdown(
    '<p class="section-title">Pricing</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="price-box">
<h2>🔥 Special Offer</h2>
<h3>₹299 for First-Time Clients</h3>
<h3>₹499 Afterwards</h3>
<p>Affordable websites with premium quality design.</p>
</div>
""", unsafe_allow_html=True)

# Why Choose Us
st.markdown(
    '<p class="section-title">Why Choose Delta Website?</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">
✅ Mobile Friendly Design<br><br>
✅ Fast Delivery<br><br>
✅ Modern UI/UX<br><br>
✅ Affordable Pricing<br><br>
✅ WhatsApp Integration<br><br>
✅ Beginner Friendly Support
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown(
    '<p class="section-title">Contact Us</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="contact-box">
<h2>📞 8076664925</h2>
<h2>📞 9213458804</h2>
<p>DM or Call Now To Get Your Website Started</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

st.markdown(
    "<center>© 2026 Delta Website • Modern Websites for Modern Businesses</center>",
    unsafe_allow_html=True
)
