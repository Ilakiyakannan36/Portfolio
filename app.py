import streamlit as st
from PIL import Image
import os
import base64

# --- Page config ---
st.set_page_config(
    page_title="K. ILAKIYA | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
<style>
/* Main title */
.main-title {
    font-size: 4.5rem !important;
    font-weight: 900 !important;
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    animation: gradient 8s ease infinite;
    background-size: 400% 400%;
}
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.sub-title {
    font-size: 1.8rem !important;
    color: #2D3436 !important;
    font-weight: 500 !important;
    margin-bottom: 2rem !important;
    padding-left: 10px;
}
/* Section headers */
.section-header {
    font-size: 2.5rem !important;
    color: #2D3436 !important;
    font-weight: 800 !important;
    margin: 3rem 0 1.5rem 0 !important;
    padding-bottom: 0.8rem !important;
    border-bottom: 4px solid linear-gradient(90deg, #4ECDC4, #45B7D1) !important;
    background: linear-gradient(90deg, #4ECDC4, #45B7D1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
/* Card styling */
.card {
    background: linear-gradient(145deg, rgba(255,255,255,0.9), rgba(255,255,255,0.7));
    backdrop-filter: blur(15px);
    border-radius: 24px !important;
    padding: 2rem !important;
    margin: 1.5rem 0 !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1) !important;
    border: 1px solid rgba(255,255,255,0.4) !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
    transition: 0.5s;
}
.card:hover::before {
    left: 100%;
}
.card:hover {
    transform: translateY(-10px) scale(1.02) !important;
    box-shadow: 0 25px 50px rgba(0,0,0,0.15) !important;
}
/* Profile image */
.profile-img-container {
    width: 280px;
    height: 280px;
    border-radius: 50%;
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
    padding: 8px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    animation: float 6s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}
.profile-img {
    width: 100% !important;
    height: 100% !important;
    border-radius: 50% !important;
    object-fit: cover !important;
    border: 5px solid white !important;
}
/* Skill tags */
.skill-tag {
    display: inline-block;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 8px 20px;
    margin: 5px;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    transition: all 0.3s ease;
}
.skill-tag:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}
/* Contact info */
.contact-item {
    display: flex;
    align-items: center;
    margin: 1rem 0;
    padding: 15px;
    background: rgba(255,255,255,0.8);
    border-radius: 15px;
    transition: transform 0.3s ease;
}
.contact-item:hover {
    transform: translateX(10px);
}
/* Tab styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 2px;
    background-color: #f0f2f6;
    padding: 10px;
    border-radius: 15px;
}
.stTabs [data-baseweb="tab"] {
    height: 60px;
    white-space: pre-wrap;
    background-color: white;
    border-radius: 10px;
    color: #2D3436;
    font-weight: 600;
    font-size: 1.1rem;
    padding: 10px 24px;
    margin: 0 5px;
    transition: all 0.3s ease;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4) !important;
    color: white !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
/* Progress bars */
.progress-container {
    background: #e0e0e0;
    border-radius: 10px;
    margin: 15px 0;
    height: 12px;
    overflow: hidden;
}
.progress-bar {
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, #4ECDC4, #45B7D1);
    transition: width 1s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar with Contact Info ---
with st.sidebar:
    st.markdown("## 📱 Contact Information")
    
    contact_info = {
        "📍": "Villupuram, Tamil Nadu",
        "📧": "ilakiyakannan36@gmail.com",
        "📱": "+91 90430 66305",
        "🔗": "[View LinkedIn Profile](https://www.linkedin.com/in/ilakiya-kannan-3860a0394/)",
        "🐱": "[View GitHub Profile](https://github.com/Ilakiyakannan36)"
    }
    
    for icon, info in contact_info.items():
        if "http" in info:
            st.markdown(f"**{icon}** {info}")
        else:
            st.markdown(f"**{icon}** {info}")
    
    st.markdown("---")
    st.markdown("## 🛠️ Technical Skills")

    skills = {
        "Python": 90,
        "Power BI": 85,
        "MS Office": 80,
        "SQL": 85,
        "C/C++": 75
    }

    for skill, value in skills.items():
        st.markdown(f"**{skill}**")
        st.progress(value/100)  # Just the bar, no numbers


# --- Header Section ---
header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    st.markdown('<p class="main-title">K. ILAKIYA</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">🎯 Aspiring Computer Science Engineer</p>', unsafe_allow_html=True)
    
    # Quick intro
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea0d 0%, #764ba20d 100%); 
                padding: 2rem; border-radius: 20px; margin-top: 1rem;">
        <h4 style="color: #2D3436; margin-bottom: 1rem;">🌟 About Me</h4>
        <p style="color: #555; line-height: 1.8;">
        Passionate Computer Science student specializing in AI, Machine Learning, and Data Analytics. 
        Seeking opportunities to apply technical expertise in innovative projects and contribute to 
        cutting-edge technological solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)

with header_col2:
    PROFILE_IMAGE_PATH = "assets/profile.jpg"
    try:
        profile_img = Image.open(PROFILE_IMAGE_PATH)
        st.image(profile_img, width=250, use_container_width=False, output_format="PNG", caption="")
    except:
        st.markdown("""
        <div style="width: 250px; height: 250px; border-radius: 50%;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    display: flex; align-items: center; justify-content: center;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
            <span style="color: white; font-size: 4rem; font-weight: bold;">KI</span>
        </div>
        """, unsafe_allow_html=True)


# --- Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Home", "💼 Experience", "🎓 Education", "📄 Resume", "🛠️ Projects"])

# --- Home Tab ---
with tab1:
    col1, col2 = st.columns(2)

    # --- Expertise Column ---
    with col1:
        st.markdown('<h2 class="section-header">🔬 Expertise</h2>', unsafe_allow_html=True)

        expertise_areas = [
            ("🤖", "Artificial Intelligence & Machine Learning"),
            ("📊", "Data Analytics & Visualization"), 
            ("🔍", "Power BI"),
            ("📱", "Streamlit Applications")
        ]
        
        for icon, area in expertise_areas:
            st.markdown(f"""
            <div class="card" style="padding: 1rem; margin: 0.8rem 0;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.5rem;">{icon}</span>
                    <span style="font-weight: 600; font-size: 1.1rem;">{area}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # --- Achievements Column ---
    with col2:
        st.markdown('<h2 class="section-header">🏆 Achievements</h2>', unsafe_allow_html=True)

        achievements = [
            "🏅 Secured 8.4 CGPA in Computer Science Engineering",
            "💼 Completed multiple AI/ML internships",
            "🛠️ Developed a Deepfake Image Forgery Detection System",
            "👥 Active contributor to tech communities"
        ]

        # Build the complete HTML string
        achievements_html = """
        <div class="card" style="padding: 1.5rem; margin: 0.8rem 0;">
            <ul style="color: #555; line-height: 1.8; padding-left: 20px; margin: 0;">
        """
        
        # Add each achievement as a list item
        for achievement in achievements:
            achievements_html += f"<li style='margin-bottom: 0.8rem;'>{achievement}</li>"
        
        # Close the HTML
        achievements_html += """
            </ul>
        </div>
        """
        
        # Render it once
        st.markdown(achievements_html, unsafe_allow_html=True)

# --- Experience Tab ---
with tab2:
    st.markdown('<h2 class="section-header">💼 Professional Experience</h2>', unsafe_allow_html=True)
    
    experiences = [
        {
            "title": "🤖 AI Internship",
            "company": "Skillforge E-learning Pvt Ltd",
            "duration": "Jan 2024 - May 2024",
            "description": "Worked on machine learning models and AI implementations for educational platforms.",
            "technologies": ["Python", "TensorFlow", "Scikit-learn", "Pandas"]
        },
        {
            "title": "📊 Data Analytics Internship",
            "company": "Internship Studio",
            "duration": "Aug 2024 - Sep 2024",
            "description": "Analyzed datasets, created visualizations, and generated insights for business decisions.",
            "technologies": ["Python", "SQL", "Excel"]
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <div>
                    <h3 style="margin: 0; color: #2D3436;">{exp['title']}</h3>
                    <h4 style="margin: 10px 0; color: #4ECDC4;">{exp['company']}</h4>
                </div>
                <span style="background: linear-gradient(45deg, #FF6B6B, #4ECDC4); 
                            color: white; padding: 5px 15px; border-radius: 20px; 
                            font-weight: 600;">{exp['duration']}</span>
            </div>
            <p style="color: #555; line-height: 1.7; margin: 15px 0;">{exp['description']}</p>
            <div style="margin-top: 20px;">
                {"".join([f'<span class="skill-tag">{tech}</span>' for tech in exp['technologies']])}
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- Education Tab ---
with tab3:
    st.markdown('<h2 class="section-header">🎓 Academic Journey</h2>', unsafe_allow_html=True)
    
    education = [
        {
            "degree": "🎓 B.E. Computer Science Engineering",
            "institution": "Dhanalakshmi Srinivasan Engineering College (Autonomous)",
            "duration": "2022 - 2026 (Pursuing)",
            "score": "CGPA: 8.4",
            "icon": "🏛️"
        },
        {
            "degree": "📚 12th Grade",
            "institution": "Sri Sampourna Vidyalayam HSS",
            "duration": "2020 - 2022",
            "score": "Percentage: 77%",
            "icon": "🎒"
        },
        {
            "degree": "📘 10th Grade",
            "institution": "Ramakrishna Mission Matriculation School",
            "duration": "2019 - 2020",
            "score": "Percentage: 79%",
            "icon": "📖"
        }
    ]
    
    for edu in education:
        st.markdown(f"""
        <div class="card">
            <div style="display: flex; align-items: center; gap: 20px;">
                <div style="font-size: 2.5rem;">{edu['icon']}</div>
                <div style="flex: 1;">
                    <h3 style="margin: 0; color: #2D3436;">{edu['degree']}</h3>
                    <p style="margin: 5px 0; color: #666; font-size: 1.1rem;">
                        <strong>{edu['institution']}</strong>
                    </p>
                    <p style="margin: 5px 0; color: #555;">{edu['score']}</p>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                        <span style="color: #4ECDC4; font-weight: 600;">{edu['duration']}</span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- Resume Tab ---
with tab4:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="section-header">📄 Resume Preview</h2>', unsafe_allow_html=True)
        
        RESUME_IMAGE_PATH = "assets/resume.jpg"
        RESUME_PDF_PATH = "assets/resume.pdf"
        
        try:
            resume_img = Image.open(RESUME_IMAGE_PATH)
            st.image(resume_img, use_container_width=True, caption="Resume Preview")
        except:
            st.warning("⚠️ Resume image not found. Please check the file path.")
            st.info("Expected path: D:/portfolio/resume.jpg")
    
    with col2:
        st.markdown('<h3 style="color: #2D3436; margin-top: 40px;">📥 Download Resume</h3>', unsafe_allow_html=True)
        
        if os.path.exists(RESUME_PDF_PATH):
            with open(RESUME_PDF_PATH, "rb") as f:
                pdf_bytes = f.read()
            
            st.download_button(
                label="⬇️ Download PDF Resume",
                data=pdf_bytes,
                file_name="K_ILAKIYA_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        else:
            st.error("PDF file not found at the specified path.")
        
        st.markdown("---")
        st.markdown("### 🎯 Key Highlights")
        highlights = [
            "• AI/ML Specialization",
            "• Data Analytics Expertise",
            "• Python Development",
            "• Deep Learning Projects",
            "• Academic Excellence"
        ]
        
        for highlight in highlights:
            st.markdown(f"""
            <div style="background: rgba(78, 205, 196, 0.1); 
                        padding: 12px; margin: 8px 0; 
                        border-radius: 10px; border-left: 4px solid #4ECDC4;">
                {highlight}
            </div>
            """, unsafe_allow_html=True)

# --- Projects Tab ---
with tab5:
    st.markdown('<h2 class="section-header">Projects</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>Deepfake Image Forgery Detection System</h3>
        <p>Detects fake images and videos using advanced AI models (CNN & Image Forensics).</p>
        <a href="https://github.com/Ilakiyakannan36/Deepfake-image-detection-system" target="_blank">View on GitHub →</a>
    </div>
    """, unsafe_allow_html=True)
# --- Footer ---
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: #666;">📍 Villupuram, Tamil Nadu</p>
    </div>
    """, unsafe_allow_html=True)

with footer_col2:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: #666;">© 2025 K. ILAKIYA Portfolio</p>
    </div>
    """, unsafe_allow_html=True)

with footer_col3:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: #666;">📧 ilakiyakannan36@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)
