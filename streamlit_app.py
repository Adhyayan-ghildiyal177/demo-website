import streamlit as st

st.set_page_config(
    page_title="Delta-X Web Solutions",
    page_icon="🚀",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "Home"

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
    font-size: 85px;
    font-weight: 900;
    text-align: center;
    color: #38bdf8;
    text-shadow: 5px 5px 0px #075985, 10px 10px 25px #000000;
}

.hero, .card, .price, .contact, .market {
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

.email-btn {
    background: #2563eb;
    box-shadow: 0px 8px 0px #1e3a8a;
}

.market {
    background: linear-gradient(145deg, #7c2d12, #020617);
}

.floating-whatsapp {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background: #22c55e;
    color: white !important;
    padding: 15px 20px;
    border-radius: 50px;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    z-index: 9999;
    box-shadow: 0px 8px 20px #000000;
}

@media only screen and (max-width: 768px) {
    .logo {
        font-size: 48px;
    }
    .title {
        font-size: 28px;
    }
    .hero, .card, .price, .contact, .market {
        padding: 24px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<a class="floating-whatsapp" href="https://wa.me/918076664925" target="_blank">
💬 WhatsApp
</a>
""", unsafe_allow_html=True)

# Navigation
n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"

with n2:
    if st.button("💰 Pricing", use_container_width=True):
        st.session_state.page = "Pricing"

with n3:
    if st.button("📢 Updates", use_container_width=True):
        st.session_state.page = "Updates"

with n4:
    if st.button("❓ FAQ", use_container_width=True):
        st.session_state.page = "FAQ"

with n5:
    if st.button("📞 Contact", use_container_width=True):
        st.session_state.page = "Contact"


# HOME
if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="logo">DELTA-X</div>
        <h2>Delta-X Web Solutions</h2>
        <h1>Get More Customers With A Professional Website</h1>
        <p>Fast • Mobile Friendly • WhatsApp Ready • Affordable</p>
        <h2 style="color:#facc15;">Starting From ₹1000</h2>
        <a class="btn" href="https://wa.me/918076664925" target="_blank">💬 Order on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Why Businesses Trust Us</div>', unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown('<div class="card"><h2>24-48 Hrs</h2><p>Fast Delivery</p></div>', unsafe_allow_html=True)

    with s2:
        st.markdown('<div class="card"><h2>100%</h2><p>Mobile Friendly</p></div>', unsafe_allow_html=True)

    with s3:
        st.markdown('<div class="card"><h2>Free</h2><p>Consultation</p></div>', unsafe_allow_html=True)

    with s4:
        st.markdown('<div class="card"><h2>Low Cost</h2><p>For Small Business</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="title">What We Make</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <h2>🏢 Business Website</h2>
            <p>For shops, gyms, cafes, clinics, schools and local services.</p>
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
            <p>For students, freelancers, creators and professionals.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="market">
        <h2>Market Price: ₹5000+</h2>
        <h1 style="color:#facc15;">Our Launch Offer: ₹1000</h1>
        <h2>Save Up To 80%</h2>
        <p>Professional 3D-style website at a beginner-friendly price.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Why Choose Us</div>', unsafe_allow_html=True)

    w1, w2, w3 = st.columns(3)

    with w1:
        st.markdown('<div class="card"><h2>⚡ Fast</h2><p>Website ready in 24-48 hours.</p></div>', unsafe_allow_html=True)

    with w2:
        st.markdown('<div class="card"><h2>📱 Responsive</h2><p>Looks good on phone and computer.</p></div>', unsafe_allow_html=True)

    with w3:
        st.markdown('<div class="card"><h2>💬 Lead Ready</h2><p>WhatsApp button for direct customer contact.</p></div>', unsafe_allow_html=True)


# PRICING
elif st.session_state.page == "Pricing":

    st.markdown('<div class="logo">DELTA-X</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">Website Packages</div>', unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown("""
        <div class="price">
            <h2>Starter</h2>
            <h1 style="color:#facc15;">₹1000</h1>
            <p>One-page website</p>
            <p>Mobile friendly</p>
            <p>WhatsApp button</p>
            <p>Contact section</p>
        </div>
        """, unsafe_allow_html=True)

    with p2:
        st.markdown("""
        <div class="price">
            <h2>Business</h2>
            <h1 style="color:#facc15;">₹2500</h1>
            <p>3-4 sections</p>
            <p>Service details</p>
            <p>Contact form</p>
            <p>Better business look</p>
        </div>
        """, unsafe_allow_html=True)

    with p3:
        st.markdown("""
        <div class="price">
            <h2>Premium</h2>
            <h1 style="color:#facc15;">₹5000</h1>
            <p>Advanced 3D design</p>
            <p>More sections</p>
            <p>Professional layout</p>
            <p>Priority delivery</p>
        </div>
        """, unsafe_allow_html=True)


# UPDATES
elif st.session_state.page == "Updates":

    st.markdown('<div class="logo">DELTA-X</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <h1>📢 Latest Updates</h1>
        <p>First website offer is now available at ₹1000.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>🔥 Launch Offer</h2>
        <p>Market price is normally ₹5000+, but our starter website begins from ₹1000.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>🚀 3D Website Design</h2>
        <p>We create modern 3D-style websites for local businesses.</p>
    </div>
    """, unsafe_allow_html=True)


# FAQ
elif st.session_state.page == "FAQ":

    st.markdown('<div class="logo">DELTA-X</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">Frequently Asked Questions</div>', unsafe_allow_html=True)

    with st.expander("How long does it take to make a website?"):
        st.write("Most starter websites can be delivered within 24-48 hours after getting all details.")

    with st.expander("Will the website work on mobile?"):
        st.write("Yes, the website is designed to look good on phone, tablet, laptop and desktop.")

    with st.expander("Can you add WhatsApp button?"):
        st.write("Yes, WhatsApp button is included so customers can contact you directly.")

    with st.expander("What details do you need from me?"):
        st.write("Business name, phone number, services, address, email and photos/logo if available.")

    with st.expander("Is ₹1000 the final price?"):
        st.write("₹1000 is for a starter one-page website. Extra pages or advanced features may cost more.")


# CONTACT
elif st.session_state.page == "Contact":

    st.markdown('<div class="logo">DELTA-X</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="contact">
        <h1>📞 Contact Delta-X Web Solutions</h1>
        <h2>📞 8076664925</h2>
        <h3>📧 agentx.webb@gmail.com</h3>
        <p>Call, WhatsApp or Email us to start your website.</p>

        <a class="btn" href="https://wa.me/918076664925" target="_blank">💬 Chat on WhatsApp</a>
        <br>
        <a class="btn email-btn" href="mailto:agentx.webb@gmail.com">📧 Email Us</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Send Enquiry</div>', unsafe_allow_html=True)

    name = st.text_input("Your Name")
    phone = st.text_input("Your Phone Number")
    business = st.text_input("Business Name")
    message = st.text_area("Website Requirement")

    if st.button("Submit"):
        st.success("Thank you! We will contact you soon.")

st.markdown("""
<center style="color:#94a3b8;margin-top:35px;">
© 2026 Delta-X Web Solutions • 3D Websites for Modern Businesses
</center>
""", unsafe_allow_html=True)
