import streamlit as st

st.set_page_config(
    page_title="Delta-X",
    page_icon="🚀",
    layout="wide"
)

# Page memory
if "page" not in st.session_state:
    st.session_state.page = "Home"

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #000000);
    color: white;
}

.block-container {
    padding-top: 25px;
}

.logo {
    font-size: 90px;
    font-weight: 900;
    text-align: center;
    color: #38bdf8;
    text-shadow: 5px 5px 0px #075985, 10px 10px 25px #000000;
}

.hero, .card, .price, .contact {
    background: linear-gradient(145deg, #111827, #020617);
    padding: 35px;
    border-radius: 30px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 15px 15px 35px #000000,
                -8px -8px 22px rgba(56,189,248,0.22);
    border: 1px solid rgba(56,189,248,0.25);
}

.card:hover {
    transform: translateY(-8px);
    transition: 0.3s;
}

.title {
    text-align: center;
    font-size: 38px;
    color: #38bdf8;
    margin-top: 45px;
    font-weight: 800;
}

.btn {
    background: #22c55e;
    color: white !important;
    padding: 15px 28px;
    border-radius: 35px;
    text-decoration: none;
    font-size: 20px;
    font-weight: bold;
    display: inline-block;
    margin-top: 20px;
    box-shadow: 0px 8px 0px #166534;
}

.market {
    background: linear-gradient(145deg, #7c2d12, #020617);
    padding: 30px;
    border-radius: 30px;
    text-align: center;
    margin-top: 35px;
    box-shadow: 15px 15px 35px #000000;
}

@media only screen and (max-width: 768px) {
    .logo {
        font-size: 55px;
    }
    .title {
        font-size: 28px;
    }
}
</style>
""", unsafe_allow_html=True)

# Navigation
n1, n2, n3 = st.columns(3)

with n1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"

with n2:
    if st.button("📢 Updates", use_container_width=True):
        st.session_state.page = "Updates"

with n3:
    if st.button("📞 Contact", use_container_width=True):
        st.session_state.page = "Contact"


# HOME PAGE
if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="logo">DELTA-X</div>
        <h2>3D Modern Websites for Small Businesses</h2>
        <p>Mobile Friendly • Fast Delivery • WhatsApp Ready</p>
        <a class="btn" href="https://wa.me/918076664925" target="_blank">💬 Order on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">What We Make</div>', unsafe_allow_html=True)

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

    st.markdown("""
    <div class="price">
        <h2>🔥 First Website Offer</h2>
        <h1 style="font-size:60px;color:#facc15;">₹1000</h1>
        <h3>Afterwards ₹1500</h3>
        <p>Includes design, mobile view, WhatsApp button, and contact section.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="market">
        <h2>Market Price: ₹5000+</h2>
        <h1 style="color:#facc15;">Our Price Starts ₹1000</h1>
        <p>Get a professional 3D-style website at a beginner-friendly price.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Why Choose Us</div>', unsafe_allow_html=True)

    w1, w2, w3 = st.columns(3)

    with w1:
        st.markdown('<div class="card"><h2>⚡ Fast</h2><p>Website ready in 24-48 hours.</p></div>', unsafe_allow_html=True)

    with w2:
        st.markdown('<div class="card"><h2>📱 Responsive</h2><p>Looks good on phone and computer.</p></div>', unsafe_allow_html=True)

    with w3:
        st.markdown('<div class="card"><h2>💬 Lead Ready</h2><p>WhatsApp button for customer contact.</p></div>', unsafe_allow_html=True)


# UPDATES PAGE
elif st.session_state.page == "Updates":

    st.markdown('<div class="logo">DELTA-X</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <h1>📢 Latest Updates</h1>
        <p>Stay updated with our latest website offers and services.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>🔥 New Offer</h2>
        <p>First website only ₹1000. Market price normally ₹5000+.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>🚀 3D Website Design</h2>
        <p>Now we create attractive 3D-style websites for small businesses.</p>
    </div>
    """, unsafe_allow_html=True)


# CONTACT PAGE
elif st.session_state.page == "Contact":

    st.markdown('<div class="logo">DELTA-X</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="contact">
        <h1>📞 Contact Us</h1>
        <h2>8076664925</h2>
        <p>Call or WhatsApp now to start your website.</p>
        <a class="btn" href="https://wa.me/918076664925" target="_blank">💬 Chat on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Send Enquiry</div>', unsafe_allow_html=True)

    name = st.text_input("Your Name")
    phone = st.text_input("Your Phone Number")
    message = st.text_area("Your Website Requirement")

    if st.button("Submit"):
        st.success("Thank you! We will contact you soon.")

# Footer
st.markdown("""
<center style="color:#94a3b8;margin-top:35px;">
© 2026 DELTA-X • 3D Websites for Modern Businesses
</center>
""", unsafe_allow_html=True)
