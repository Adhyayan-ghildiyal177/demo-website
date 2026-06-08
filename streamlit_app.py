import streamlit as st

st.set_page_config(
    page_title="Website for Sale",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #111827);
    color: white;
}
.hero {
    text-align: center;
    padding: 70px 20px;
}
.hero h1 {
    font-size: 62px;
    color: #38bdf8;
    margin-bottom: 10px;
}
.hero p {
    font-size: 22px;
    color: #cbd5e1;
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 20px 50px rgba(0,0,0,0.35);
    margin-bottom: 25px;
}
.price {
    font-size: 45px;
    color: #22c55e;
    font-weight: bold;
}
.btn {
    display: inline-block;
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: white !important;
    padding: 15px 35px;
    border-radius: 40px;
    font-size: 20px;
    text-decoration: none;
    font-weight: bold;
}
.feature {
    font-size: 20px;
    margin: 12px 0;
}
.footer {
    text-align: center;
    color: #94a3b8;
    padding: 40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🚀 AI Website for Sale</h1>
    <p>A ready-to-use modern AI-powered web application built with Streamlit.</p>
    <br>
    <a class="btn" href="#contact">Contact for Buying</a>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h2>🌐 About This Website</h2>
        <p class="feature">✅ AI-powered browser agent concept</p>
        <p class="feature">✅ Clean and modern UI</p>
        <p class="feature">✅ Mobile and desktop responsive</p>
        <p class="feature">✅ Ready for customization</p>
        <p class="feature">✅ Good for startups, agencies, and AI demos</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2>💰 Asking Price</h2>
        <p class="price">₹49,999</p>
        <p>Price negotiable for serious buyers.</p>
        <p>Source code, deployment help, and basic setup support included.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h2>✨ Key Features</h2>
    <p class="feature">🤖 AI-based automation idea</p>
    <p class="feature">⚡ Fast Streamlit deployment</p>
    <p class="feature">🎨 Premium dark 3D-style design</p>
    <p class="feature">📱 Works on mobile, tablet, and PC</p>
    <p class="feature">🛠️ Easy to modify for any business</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h2>👤 Who Should Buy?</h2>
    <p class="feature">✔️ Digital marketing agencies</p>
    <p class="feature">✔️ AI startup founders</p>
    <p class="feature">✔️ Website developers</p>
    <p class="feature">✔️ Business owners wanting AI automation</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card" id="contact">
    <h2>📞 Contact to Buy</h2>
    <p class="feature">Interested buyers can contact directly.</p>
    <p class="feature"><b>Email:</b>Adhyayanghildiyal177@gmail.com</p>
    <p class="feature"><b>WhatsApp:</b> +91-8076664925</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    © 2026 AI Website Sale Page | Built with Streamlit
</div>
""", unsafe_allow_html=True)
