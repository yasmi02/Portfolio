import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Yasemin Adatepe - Portfolio",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with Modern Design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

    /* Dark theme background */
    .main {
        background: #000000;
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
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 50%, #FF8C42 100%);
        padding: 4rem 3rem;
        border-radius: 30px;
        text-align: center;
        margin: 2rem 0 3rem 0;
        box-shadow: 0 25px 80px rgba(255, 107, 53, 0.5);
        position: relative;
        overflow: hidden;
    }

    .hero-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
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
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }

    .hero-subtitle {
        font-family: 'Outfit', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: rgba(255,255,255,0.95);
        margin: 1rem 0;
        position: relative;
        z-index: 2;
    }

    .hero-desc {
        font-family: 'Outfit', sans-serif;
        font-size: 1.15rem;
        color: rgba(255,255,255,0.85);
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
        background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(247, 184, 1, 0.1) 100%);
        border: 2px solid rgba(255, 107, 53, 0.3);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }

    .stat-box:hover {
        transform: translateY(-8px);
        border-color: #FF6B35;
        box-shadow: 0 20px 40px rgba(255, 107, 53, 0.3);
        background: linear-gradient(135deg, rgba(255, 107, 53, 0.2) 0%, rgba(247, 184, 1, 0.2) 100%);
    }

    .stat-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    .stat-label {
        font-family: 'Outfit', sans-serif;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
    }

    /* Section Title */
    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        color: white;
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
        background: rgba(10, 10, 10, 0.8);
        border: 2px solid rgba(255, 107, 53, 0.3);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }

    .content-box:hover {
        border-color: rgba(255, 107, 53, 0.6);
        transform: translateX(10px);
        box-shadow: 0 10px 30px rgba(255, 107, 53, 0.3);
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
        color: #FF8C42;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .content-date {
        display: inline-block;
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%);
        color: white;
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .content-text {
        font-family: 'Outfit', sans-serif;
        color: rgba(255,255,255,0.75);
        font-size: 1.05rem;
        line-height: 1.6;
    }

    /* Project Card */
    .project-card {
        background: rgba(10, 10, 10, 0.8);
        border: 2px solid rgba(255, 107, 53, 0.3);
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
        background: linear-gradient(90deg, #FF6B35 0%, #F7B801 100%);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }

    .project-card:hover::before {
        transform: scaleX(1);
    }

    .project-card:hover {
        border-color: #FF6B35;
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(255, 107, 53, 0.3);
    }

    .project-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    /* Tech Badge */
    .tech-badge {
        display: inline-block;
        background: rgba(255, 107, 53, 0.2);
        border: 1px solid rgba(255, 107, 53, 0.4);
        color: #FFB380;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-size: 0.9rem;
        font-weight: 500;
        font-family: 'Outfit', sans-serif;
    }

    /* Contact Card */
    .contact-card {
        background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(247, 184, 1, 0.1) 100%);
        border: 2px solid rgba(255, 107, 53, 0.3);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }

    .contact-card:hover {
        border-color: #FF6B35;
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(255, 107, 53, 0.3);
    }

    .contact-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .contact-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: white;
        margin: 0.5rem 0;
    }

    .contact-text {
        font-family: 'Outfit', sans-serif;
        color: rgba(255,255,255,0.7);
        font-size: 0.95rem;
    }

    /* Buttons */
    .stButton button {
        width: 100%;
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 2rem !important;
        border-radius: 15px !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3) !important;
    }

    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 35px rgba(255, 107, 53, 0.5) !important;
    }

    /* Link buttons styling */
    a[data-testid="stLinkButton"] {
        text-decoration: none !important;
    }

    a[data-testid="stLinkButton"] > button {
        background: linear-gradient(135deg, #FF6B35 0%, #F7B801 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border: none !important;
    }

    /* Text styling */
    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: white !important;
    }

    p, div, span, label {
        font-family: 'Outfit', sans-serif !important;
        color: rgba(255,255,255,0.85) !important;
    }

    /* Form styling */
    .stTextInput input, .stTextArea textarea {
        background: rgba(10, 10, 10, 0.9) !important;
        border: 2px solid rgba(255, 107, 53, 0.3) !important;
        color: white !important;
        border-radius: 15px !important;
        font-family: 'Outfit', sans-serif !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #FF6B35 !important;
        box-shadow: 0 0 20px rgba(255, 107, 53, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation (Top Menu)
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    home_btn = st.button("🏠 Home", use_container_width=True)
with col2:
    about_btn = st.button("👤 About", use_container_width=True)
with col3:
    exp_btn = st.button("💼 Experience", use_container_width=True)
with col4:
    skills_btn = st.button("🛠️ Skills", use_container_width=True)
with col5:
    projects_btn = st.button("🚀 Projects", use_container_width=True)
with col6:
    contact_btn = st.button("📧 Contact", use_container_width=True)

# Determine which section to show
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'home'

if home_btn:
    st.session_state.current_section = 'home'
elif about_btn:
    st.session_state.current_section = 'about'
elif exp_btn:
    st.session_state.current_section = 'experience'
elif skills_btn:
    st.session_state.current_section = 'skills'
elif projects_btn:
    st.session_state.current_section = 'projects'
elif contact_btn:
    st.session_state.current_section = 'contact'

# HOME SECTION
if st.session_state.current_section == 'home':
    st.markdown("""
        <div class="hero-box">
            <div class="hero-title">Yasemin Adatepe</div>
            <div class="hero-subtitle">UI/UX Designer & Frontend Developer</div>
            <div class="hero-desc">
                I design intuitive digital experiences backed by technical implementation skills.
                Combining education expertise with design thinking to create user-centered solutions.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">3.51</div>
                <div class="stat-label">University GPA</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">6+</div>
                <div class="stat-label">Design Projects</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">5</div>
                <div class="stat-label">Certifications</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="stat-box">
                <div class="stat-number">2</div>
                <div class="stat-label">Internship Experiences</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Quick Contact
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.link_button("📧 Email Me", "mailto:yaseminadatepe200@gmail.com", use_container_width=True)
    with col2:
        st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/yasemin-adatepe-a25a4922b/", use_container_width=True)
    with col3:
        st.link_button("💻 GitHub", "https://github.com/yasmi02", use_container_width=True)
    with col4:
        st.link_button("📱 Call Me", "tel:+905380822742", use_container_width=True)

# ABOUT SECTION
elif st.session_state.current_section == 'about':
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
            <div class="content-box">
                <div class="content-title">👋 Hello!</div>
                <div class="content-text">
                    I'm a <strong>UI/UX Designer</strong> with a unique background in education and technical development. 
                    Recently completed a UI & Web Design internship at <strong>Nüans Ajans</strong>, where I gained hands-on 
                    experience with professional design workflows and real client projects.
                    <br><br>
                    Currently working as a Software Developer Apprentice at Arı Bilgi Eğitim Akademisi, I combine 
                    <strong>design thinking with technical implementation</strong> to create meaningful digital experiences. 
                    My journey into design started during my teaching years at MEF University, where I discovered 
                    the power of <strong>user-centered design</strong>. This background allows me to deeply understand 
                    user needs, create intuitive interfaces, and communicate design decisions effectively to both 
                    technical and non-technical stakeholders.
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="content-box">
                <div class="content-title">🎓 Education</div>
                <div class="content-subtitle">MEF University | 2020-2025</div>
                <div class="content-text">
                    English Language Teaching<br>
                    <strong>GPA: 3.51</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="content-box">
                <div class="content-title">🏆 Achievements</div>
                <div class="content-text">
                    ✅ Python course: <strong>100/100</strong><br>
                    ✅ Deep Learning certified<br>
                    ✅ 5+ full-stack projects<br>
                    ✅ 5 certifications<br>
                    ✅ Teaching experience<br>
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
        ("January 2026 (15 days)", "UI Design & Web Design Intern", "Nüans Ajans",
         "Gained hands-on experience in professional design workflow, creating UI mockups and web design assets. Worked on real client projects and learned industry-standard design practices."),
        ("July 2025 - Present", "Software Developer Apprentice", "Arı Bilgi Eğitim Akademisi",
         "Developing software solutions and expanding technical expertise in full-stack development with Python, Java, and modern frameworks."),
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
    st.markdown('<div class="section-title">Skills & Expertise</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="content-box">
                <div class="content-title">🎨 Design Skills</div>
                <div style="margin-top: 1rem;">
                    <span class="tech-badge">Figma</span>
                    <span class="tech-badge">Wireframing</span>
                    <span class="tech-badge">Prototyping</span>
                    <span class="tech-badge">User Research</span>
                    <span class="tech-badge">Usability Testing</span>
                    <span class="tech-badge">UI Design</span>
                    <span class="tech-badge">Design Systems</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="content-box">
                <div class="content-title">💻 Frontend Development</div>
                <div style="margin-top: 1rem;">
                    <span class="tech-badge">HTML</span>
                    <span class="tech-badge">CSS</span>
                    <span class="tech-badge">JavaScript</span>
                    <span class="tech-badge">React</span>
                    <span class="tech-badge">Responsive Design</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="content-box">
                <div class="content-title">⚡ Technical Advantage</div>
                <div style="margin-top: 1rem;">
                    <span class="tech-badge">Python</span>
                    <span class="tech-badge">Java</span>
                    <span class="tech-badge">SQLite</span>
                    <span class="tech-badge">Git</span>
                    <span class="tech-badge">UI Implementation</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="content-box">
                <div class="content-title">📜 Certifications</div>
                <div class="content-text">
                    ✅ Python (100/100) - Arı IT Academy<br>
                    ✅ Marketing in Digital World - UIUC<br>
                    ✅ Deep Learning (100/100) - Arı IT Academy<br>
                    ✅ Understanding AI - MEF University<br>
                    ✅ Software Expertise 100/100) - Arı IT Academy<br>
                </div>
            </div>
        """, unsafe_allow_html=True)

# PROJECTS SECTION
elif st.session_state.current_section == 'projects':
    st.markdown('<div class="section-title">Design Projects</div>', unsafe_allow_html=True)

    projects = [
        ("📄", "PDF AI Assistant",
         "Designed an intelligent document interaction interface that makes PDF analysis intuitive and accessible. Created a conversational UI pattern that simplifies complex document queries with clear visual hierarchy and smart information retrieval.",
         ["UI/UX Design", "Conversational UI", "Python", "AI Integration"]),

        ("🌙", "Sleep Tracker",
         "Designed a calming sleep monitoring experience focusing on minimal UI and emotional usability. Created intuitive data visualization for sleep patterns with soothing color palette and gentle animations.",
         ["UI Design", "User Research", "Prototyping", "Java", "JavaFX"]),

        ("📔", "Cozy Diary App",
         "Designed a journaling experience emphasizing privacy and emotional comfort. Researched user needs for personal reflection spaces and created a soft, welcoming interface with thoughtful micro-interactions.",
         ["UI/UX Design", "User Testing", "Wireframing", "Java Swing"]),

        ("📚", "Smart Study Assistant",
         "Created an intuitive study management interface that reduces cognitive load. Focused on clear information hierarchy and progress visualization to motivate student engagement.",
         ["Information Architecture", "UI Design", "Python", "SQLite"]),

        ("📝", "BlogHub",
         "Designed a clean blogging platform with focus on readability and content discovery. Implemented responsive layouts and accessible design patterns for diverse user needs.",
         ["Web Design", "Responsive Design", "Python", "HTML/CSS"]),

        ("🎵", "Media Converter",
         "Simplified complex file conversion process through intuitive interface design. Created clear user flows and visual feedback systems for technical operations.",
         ["UX Design", "User Flows", "Python", "JavaScript"])
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
