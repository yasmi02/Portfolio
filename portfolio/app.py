import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Yasemin Adatepe - Portfolio",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with Dark Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

    /* Dark theme background */
.stApp {
    background-color: #000000;
    color: #FFFFFF;
}

    .block-container {
        padding-top: 1rem !important;
        max-width: 1400px !important;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Hero Section */
    .hero-box {
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%);
        padding: 4rem 3rem;
        border-radius: 30px;
        text-align: center;
        margin: 2rem 0 3rem 0;
        box-shadow: 0 25px 80px rgba(255, 107, 53, 0.5);
        position: relative;
        overflow: hidden;
        border: 2px solid #FF6B35;
    }

    .hero-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 50%, rgba(255, 107, 53, 0.12) 0%, transparent 50%),
                    radial-gradient(circle at 70% 60%, rgba(0, 217, 255, 0.08) 0%, transparent 50%);
        animation: pulse 4s ease-in-out infinite;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 4.5rem;
        font-weight: 700;
        color: white;
        margin: 0 0 1rem 0;
        position: relative;
        z-index: 2;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }

    .hero-subtitle {
        font-family: 'Outfit', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: white;
        margin: 1rem 0;
        position: relative;
        z-index: 2;
    }

    .hero-desc {
        font-family: 'Outfit', sans-serif;
        font-size: 1.15rem;
        color: white;
        max-width: 750px;
        margin: 1.5rem auto 0 auto;
        line-height: 1.7;
        position: relative;
        z-index: 2;
    }

    /* Stats Grid */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 3rem 0;
    }

    .stat-box {
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%);
        border: 2px solid #FF6B35;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }

    .stat-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.1);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .stat-box:hover {
        transform: translateY(-8px);
        border-color: #F7B801;
        box-shadow: 0 20px 40px rgba(255, 107, 53, 0.6);
    }

    .stat-box:hover::before {
        opacity: 1;
    }

    .stat-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
        position: relative;
        z-index: 1;
    }

    .stat-label {
        font-family: 'Outfit', sans-serif;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        position: relative;
        z-index: 1;
    }

    /* Section Title */
    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        color: #E8EAED;
        text-align: center;
        margin: 4rem 0 2.5rem 0;
        position: relative;
    }

    .section-title::after {
        content: '';
        display: block;
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, #FF6B35 0%, #F7B801 100%);
        margin: 1rem auto 0 auto;
        border-radius: 2px;
    }

    /* Content Box */
    .content-box {
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%);
        border: 2px solid #FF6B35;
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }

    .content-box:hover {
        border-color: #F7B801;
        transform: translateX(10px);
        box-shadow: 0 10px 30px rgba(255, 107, 53, 0.6);
    }

    .content-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }

    .content-subtitle {
        font-family: 'Outfit', sans-serif;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .content-date {
        display: inline-block;
        background: white;
        color: #FF6B35;
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .content-text {
        font-family: 'Outfit', sans-serif;
        color: white;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    .content-text strong {
        color: white;
    }

    /* Project Card */
    .project-card {
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%);
        border: 2px solid #FF6B35;
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: white;
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }

    .project-card:hover::before {
        transform: scaleX(1);
    }

    .project-card:hover {
        transform: translateY(-10px) scale(1.02);
        border-color: #F7B801;
        box-shadow: 0 20px 50px rgba(255, 107, 53, 0.6);
    }

    .project-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: inline-block;
        filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
    }

    /* Tech Badge */
    .tech-badge {
        display: inline-block;
        background: white;
        color: #FF6B35;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1px solid white;
        transition: all 0.3s ease;
    }

    .tech-badge:hover {
        background: #000000;
        color: white;
        transform: translateY(-2px);
        border-color: white;
    }

    /* Contact Card */
    .contact-card {
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%);
        border: 2px solid #FF6B35;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }

    .contact-card:hover {
        transform: translateY(-10px);
        border-color: #F7B801;
        box-shadow: 0 20px 40px rgba(255, 107, 53, 0.6);
    }

    .contact-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
    }

    .contact-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }

    .contact-text {
        font-family: 'Outfit', sans-serif;
        color: white;
        font-size: 0.95rem;
    }

    /* Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 30px rgba(255, 107, 53, 0.3) !important;
    }

    div.stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 40px rgba(255, 107, 53, 0.4) !important;
    }

    /* Form Inputs */
    .stTextInput input, .stTextArea textarea {
        background: #222222 !important;
        border: 2px solid #FF6B35 !important;
        border-radius: 15px !important;
        color: white !important;
        padding: 1rem !important;
        font-size: 1rem !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #F7B801 !important;
        box-shadow: 0 0 20px rgba(255, 107, 53, 0.5) !important;
    }

    /* Success/Error Messages */
    .stSuccess {
        background: rgba(0, 217, 255, 0.1) !important;
        border: 2px solid #00D9FF !important;
        border-radius: 15px !important;
        color: #00D9FF !important;
    }

    .stError {
        background: rgba(255, 107, 53, 0.1) !important;
        border: 2px solid #FF6B35 !important;
        border-radius: 15px !important;
        color: #FF6B35 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'home'

# Navigation
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_section = 'home'
with col2:
    if st.button("👤 About", use_container_width=True):
        st.session_state.current_section = 'about'
with col3:
    if st.button("💼 Experience", use_container_width=True):
        st.session_state.current_section = 'experience'
with col4:
    if st.button("🛠️ Skills", use_container_width=True):
        st.session_state.current_section = 'skills'
with col5:
    if st.button("🚀 Projects", use_container_width=True):
        st.session_state.current_section = 'projects'
with col6:
    if st.button("📧 Contact", use_container_width=True):
        st.session_state.current_section = 'contact'

# HOME SECTION
if st.session_state.current_section == 'home':
    st.markdown("""
        <div class="hero-box">
            <div class="hero-title">Yasemin Adatepe</div>
            <div class="hero-subtitle">Software Developer & Educator</div>
            <div class="hero-desc">
               Software developer with an education background, focused on building thoughtful and practical digital experiences.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Quick Stats</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">3.51</div>
                <div class="stat-label">GPA Excellence</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">6+</div>
                <div class="stat-label">Programming Languages</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">5+</div>
                <div class="stat-label">Featured Projects</div>
            </div>
        """, unsafe_allow_html=True)

# ABOUT SECTION
elif st.session_state.current_section == 'about':
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="content-box">
                <div class="content-title">🎓 Education</div>
                <div class="content-text">
                    <strong>English Language Teaching</strong><br>
                    MEF University (2020-2025)<br>
                    GPA: 3.51/4.00<br><br>
                    <strong>Software Development</strong><br>
                    Arı IT Academy (2024-Present)<br>
                    Full-Stack Development Program
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="content-box">
                <div class="content-title">🏆 Achievements</div>
                <div class="content-text">
                    ✅ Python course: <strong>100/100</strong><br>
                    ✅ Deep Learning certified<br>
                    ✅ 5+ full-stack projects<br>
                    ✅ 8+ certifications<br>
                    ✅ Teaching experience<br>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="content-box">
                <div class="content-title">💡 About</div>
                <div class="content-text">
                    I’m a software developer with a background in education. I like to combine technical skills with a strong sense of communication. I enjoy building clear, user-friendly applications and learning something new with every project. I am especially interested in Web Design.
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="content-box">
                <div class="content-title">🌍 Languages</div>
                <div class="content-text">
                    🇬🇧 <strong>English:</strong> C1 Level<br>
                    🇪🇸 <strong>Spanish:</strong> A2 Level<br>
                    🇹🇷 <strong>Turkish:</strong> Native
                </div>
            </div>
        """, unsafe_allow_html=True)

# EXPERIENCE SECTION
elif st.session_state.current_section == 'experience':
    st.markdown('<div class="section-title">Work Experience</div>', unsafe_allow_html=True)

    experiences = [
        ("July 2025 - Present", "Software Developer Apprentice", "Arı Bilgi Eğitim Akademisi",
         "Developing software solutions and expanding technical expertise in full-stack development with Python, Java, and modern frameworks."),
        ("September 2024 - May 2025", "English Teacher Intern", "Hüseyin Avni Sözen Anadolu Lisesi",
         "Facilitated engaging English language instruction and developed creative teaching methodologies for high school students."),
        ("September 2023 - May 2024", "English Teacher Intern", "Çamlıca Eyüboğlu Koleji",
         "Delivered comprehensive English language education and mentored students in a prestigious private school environment."),
        ("June 2020 - August 2020", "Secretary", "Eray Law Office",
         "Managed administrative operations and client communications in a professional legal environment.")
    ]

    for date, title, company, desc in experiences:
        st.markdown(f"""
            <div class="content-box">
                <div class="content-date">{date}</div>
                <div class="content-title">{title}</div>
                <div class="content-subtitle">{company}</div>
                <div class="content-text">{desc}</div>
            </div>
        """, unsafe_allow_html=True)

# SKILLS SECTION
elif st.session_state.current_section == 'skills':
    st.markdown('<div class="section-title">Skills & Technologies</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="content-box">
                <div class="content-title">💻 Programming Languages</div>
                <div style="margin-top: 1rem;">
                    <span class="tech-badge">Python</span>
                    <span class="tech-badge">Java</span>
                    <span class="tech-badge">JavaScript</span>
                    <span class="tech-badge">C#</span>
                    <span class="tech-badge">HTML</span>
                    <span class="tech-badge">CSS</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="content-box">
                <div class="content-title">🛠️ Technologies & Tools</div>
                <div style="margin-top: 1rem;">
                    <span class="tech-badge">JavaFX</span>
                    <span class="tech-badge">Java Swing</span>
                    <span class="tech-badge">SQLite</span>
                    <span class="tech-badge">FXML</span>
                    <span class="tech-badge">Git</span>
                    <span class="tech-badge">UI/UX Design</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="content-box">
                <div class="content-title">🎯 Specializations</div>
                <div style="margin-top: 1rem;">
                    <span class="tech-badge">Deep Learning</span>
                    <span class="tech-badge">Full-Stack Development</span>
                    <span class="tech-badge">Database Management</span>
                    <span class="tech-badge">Teaching & Mentoring</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="content-box">
                <div class="content-title">📜 Certifications</div>
                <div class="content-text">
                    ✅ Python (100/100) - Arı IT Academy<br>
                    ✅ Deep Learning - Arı IT Academy<br>
                    ✅ C# - Arı IT Academy<br>
                    ✅ Marketing in Digital World - University of Illinois Urbana-Champaign<br>
                    ✅ Psychological First Aid - Johns Hopkins University<br>
                    ✅ Understanding AI - MEF University<br>
                    ✅ Creating Behavioral Change - Wesleyan University<br> 
                </div>
            </div>
        """, unsafe_allow_html=True)

# PROJECTS SECTION
elif st.session_state.current_section == 'projects':
    st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)

    projects = [
        ("🌙", "Sleep Tracker",
         "A comprehensive sleep monitoring application with audio playback, data persistence, and beautiful UI/UX design.",
         ["Java", "JavaFX", "SQLite", "FXML", "JLayer"]),
        ("📝", "BlogHub",
         "A full-featured Python-based blogging platform with modern web interface and content management.",
         ["Python", "HTML", "CSS", "Web Dev"]),
        ("🎵", "Mp3 & Mp4 Converter",
         "A versatile media conversion tool with intuitive interface for audio and video formats.",
         ["Python", "HTML", "CSS", "JavaScript"]),
        ("📔", "Cozy Diary App",
         "A beautifully designed personal diary with rich UI/UX features and secure data storage.",
         ["Java", "Java Swing", "UI/UX Design"]),
        ("📚", "Smart Study Assistant",
         "An intelligent study management tool with data export and productivity analytics.",
         ["Python", "SQLite", "CSV Export"])
    ]

    for icon, title, desc, tech in projects:
        tech_badges = "".join([f'<span class="tech-badge">{t}</span>' for t in tech])
        st.markdown(f"""
            <div class="project-card">
                <div class="project-icon">{icon}</div>
                <div class="content-title">{title}</div>
                <div class="content-text">{desc}</div>
                <div style="margin-top: 1rem;">
                    {tech_badges}
                </div>
            </div>
        """, unsafe_allow_html=True)

# CONTACT SECTION
elif st.session_state.current_section == 'contact':
    st.markdown('<div class="section-title">Let\'s Connect</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="content-text" style="text-align: center; max-width: 700px; margin: 0 auto 3rem auto; font-size: 1.2rem;">
            I'm always open to discussing new opportunities, collaborations, or just having a chat about technology and education!
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
            <div class="contact-card">
                <div class="contact-icon">📧</div>
                <div class="contact-title">Email</div>
                <div class="contact-text">yaseminadatepe200@gmail.com</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Send Email", "mailto:yaseminadatepe200@gmail.com", use_container_width=True)

    with col2:
        st.markdown("""
            <div class="contact-card">
                <div class="contact-icon">💼</div>
                <div class="contact-title">LinkedIn</div>
                <div class="contact-text">Professional Network</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Connect", "https://www.linkedin.com/in/yasemin-adatepe-a25a4922b/", use_container_width=True)

    with col3:
        st.markdown("""
            <div class="contact-card">
                <div class="contact-icon">💻</div>
                <div class="contact-title">GitHub</div>
                <div class="contact-text">View My Code</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("View Projects", "https://github.com/yasmi02", use_container_width=True)

    with col4:
        st.markdown("""
            <div class="contact-card">
                <div class="contact-icon">📱</div>
                <div class="contact-title">Phone</div>
                <div class="contact-text">+90 538 082 27 42</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Call Me", "tel:+905380822742", use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Contact Form
    st.markdown('<div class="content-title" style="text-align: center;">Send Me a Message</div>',
                unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message", height=150)
            submit = st.form_submit_button("Send Message", use_container_width=True)

            if submit:
                if name and email and message:
                    st.success("✅ Thank you for your message! I'll get back to you soon.")
                else:
                    st.error("⚠️ Please fill in all fields.")

