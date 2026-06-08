import streamlit as st

st.set_page_config(
    page_title="Delta-X",
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
    padding-top: 35px;
}

.hero {
    text-align: center;
    padding: 55px 20px;
    border-radius: 35px;
    background: linear-gradient(145deg, #0f172a, #020617);
    box-shadow: 
        18px 18px 40px #000000,
        -8px -8px 25px rgba(56,189,248,0.25);
}

.logo {
    font-size: 100px;
    font-weight: 900;
    color: #38bdf8;
    text-shadow: 
        4px 4px 0px #075985,
        8px 8px 20px #000000;
}

.tagline {
    font-size: 28px;
    font-weight: 600;
    color: #ffffff;
}

.subtext {
    font-size: 20px;
    color: #cbd5e1;
}

.card {
    background: linear-gradient(145deg, #111827, #020617);
    padding: 28px;
    border-radius: 25px;
    text-align: center;
    min-height: 190px;
    box-shadow:
        12px 12px 28px #000000,
        -6px -6px 18px rgba(56,189,248,0.18);
    border: 1px solid rgba(56,189,248,0.25);
    margin-top: 25px;
}

.price {
    background: linear-gradient(145deg, #075985, #0f766e);
    padding: 35px;
    border-radius: 30px;
    text-align: center;
    box-shadow:
        15px 15px 35px #000000,
        -8px -8px 22px rgba(34,211,238,0.25);
    margin-top: 35px;
}

.contact {
    background: linear-gradient(145deg, #052e16, #020617);
    padding: 35px;
    border-radius: 30px;
    text-align: center;
    box-shadow:
        15px 15px 35px #000000,
        -8px -8px 22px rgba(34,197,94,0.25);
    margin-top: 35px;
}

.section-title {
    text-align: center;
    font-size: 38px;
    color: #38bdf8;
    margin-top: 55px;
    font-weight: 800;
}

.btn {
    background: #22c55e;
    color: white !important;
    padding: 15px 28px;
    border-radius: 35px;
    text-decoration: none;
    font-size: 22px;
    font-weight: bold;
    display: inline-block;
    margin-top: 20px;
    box-shadow: 0px 8px 0px #166534;
}

@media only screen and (max-width: 768px) {
    .logo {
        font-size: 58px;
    }
    .tagline {
        font-size: 22px;
    }
    .subtext {
        font-size: 16px;
    }
    .section-title {
        font-size: 30px;
    }
}
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <div class="logo">DELTA-X</div>
    <p class="tagline">3D Modern Websites for Small Businesses</p>
    <p class="subtext">Mobile Friendly • Fast Delivery • WhatsApp Ready</p>
    <a class="btn" href="https://wa.me/918076664925" target="_blank">💬 Order on WhatsApp</a>
</div>
""", unsafe_allow_html=True)

# Services
st.markdown('<div class="section-title">What We Make</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <h2>🏢 Business Website</h2>
        <p>For shops, gyms, cafes, clinics, and local services.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h2>🎯 Landing Page</h2>
        <p>One-page website to get calls and WhatsApp inquiries.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h2>👨‍💻 Portfolio Website</h2>
        <p>For students, freelancers, creators, and professionals.</p>
    </div>
    """, unsafe_allow_html=True)

# Price
st.markdown('<div class="section-title">Simple Pricing</div>', unsafe_allow_html=True)

st.markdown("""
<div class="price">
    <h2>🔥 First Website Offer</h2>
    <h1 style="font-size:60px;color:#facc15;">₹1000</h1>
    <h3>Afterwards ₹1500</h3>
    <p>Includes design, mobile view, WhatsApp button, and contact section.</p>
</div>
""", unsafe_allow_html=True)

# Why choose us
st.markdown('<div class="section-title">Why Choose Us</div>', unsafe_allow_html=True)

w1, w2, w3 = st.columns(3)

with w1:
    st.markdown("""
    <div class="card">
        <h2>⚡ Fast</h2>
        <p>Website ready in 24-48 hours.</p>
    </div>
    """, unsafe_allow_html=True)

with w2:
    st.markdown("""
    <div class="card">
        <h2>📱 Responsive</h2>
        <p>Looks good on phone and computer.</p>
    </div>
    """, unsafe_allow_html=True)

with w3:
    st.markdown("""
    <div class="card">
        <h2>💬 Lead Ready</h2>
        <p>WhatsApp button for direct customer contact.</p>
    </div>
    """, unsafe_allow_html=True)

# Contact
st.markdown("""
<div class="contact">
    <h1>Start Your Website Today</h1>
    <h2>📞 8076664925</h2>
    <h2>📞 9213458804</h2>
    <a class="btn" href="https://wa.me/918076664925" target="_blank">💬 Chat Now</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<center style="color:#94a3b8;margin-top:35px;">
© 2026 DELTA-X • 3D Websites for Modern Businesses
</center>
""", unsafe_allow_html=True)
