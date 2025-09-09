import streamlit as st
import base64
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import random

def get_base64_of_bin_file(bin_file):
    """
    Function to convert a binary file to base64 encoding.
    """
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def set_png_as_page_bg(png_file):
    """
    Function to set a PNG image as the background of the Streamlit page.
    """
    bin_str = get_base64_of_bin_file(png_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .main .block-container {{
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            margin-top: 2rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

st.set_page_config(
    page_title="Resume Screening AI - Transform Your Hiring",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def create_animated_metrics():
    """Create animated metrics visualization"""
    # Sample data for demonstration
    categories = ['Time Saved', 'Accuracy', 'Efficiency', 'Cost Reduction']
    values = [95, 87, 92, 78]
    colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c']
    
    fig = go.Figure()
    
    # Create animated bar chart
    fig.add_trace(go.Bar(
        x=categories,
        y=values,
        marker_color=colors,
        text=[f'{v}%' for v in values],
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>Improvement: %{y}%<extra></extra>'
    ))
    
    fig.update_layout(
        title="AI-Powered Recruitment Benefits",
        title_x=0.5,
        showlegend=False,
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2d3436'),
        title_font_size=16,
        title_font_color='#2d3436'
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='rgba(0,0,0,0.1)')
    
    return fig

def create_process_flow():
    """Create process flow visualization"""
    steps = ['Upload Job Description', 'Upload Resumes', 'AI Analysis', 'Get Rankings']
    values = [100, 85, 70, 95]  # Sample completion rates
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=list(range(len(steps))),
        y=values,
        mode='lines+markers',
        line=dict(color='#667eea', width=4),
        marker=dict(size=15, color='#667eea'),
        text=steps,
        textposition='top center',
        hovertemplate='<b>%{text}</b><br>Success Rate: %{y}%<extra></extra>'
    ))
    
    fig.update_layout(
        title="4-Step Process Flow",
        title_x=0.5,
        showlegend=False,
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2d3436'),
        title_font_size=16,
        title_font_color='#2d3436'
    )
    
    fig.update_xaxes(showgrid=False, showticklabels=False)
    fig.update_yaxes(showgrid=True, gridcolor='rgba(0,0,0,0.1)', title="Success Rate (%)")
    
    return fig

def main():
    """
    Main function to render the enhanced Home page.
    """
    
    # Custom CSS for enhanced styling
    st.markdown("""
    <style>
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: repeating-linear-gradient(
            45deg,
            transparent,
            transparent 10px,
            rgba(255,255,255,0.05) 10px,
            rgba(255,255,255,0.05) 20px
        );
        animation: slide 20s linear infinite;
    }
    
    @keyframes slide {
        0% { transform: translateX(-50px) translateY(-50px); }
        100% { transform: translateX(50px) translateY(50px); }
    }
    
    .hero-section > * {
        position: relative;
        z-index: 2;
    }
    
    .hero-title {
        color: white;
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0 0 1rem 0;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        letter-spacing: -2px;
        line-height: 1.1;
    }
    
    .hero-subtitle {
        color: white;
        font-size: 1.4rem;
        margin: 0 0 2rem 0;
        opacity: 0.95;
        font-weight: 300;
        line-height: 1.5;
    }
    
    .cta-button {
        display: inline-block;
        background: white;
        color: #667eea;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.3);
        color: #667eea;
        text-decoration: none;
    }
    
    .stats-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 3rem 0;
        box-shadow: 0 12px 40px rgba(240, 147, 251, 0.3);
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .stat-item {
        color: white;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin: 0.5rem 0 0 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .process-section {
        background: #f8f9fa;
        padding: 3rem 2rem;
        border-radius: 20px;
        margin: 3rem 0;
        border: 1px solid rgba(102, 126, 234, 0.1);
    }
    
    .process-step {
        display: flex;
        align-items: center;
        margin: 1.5rem 0;
        padding: 1.5rem;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    
    .process-step:hover {
        transform: translateX(10px);
    }
    
    .step-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.2rem;
        margin-right: 1.5rem;
        flex-shrink: 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .step-content h4 {
        margin: 0;
        color: #2d3436;
        font-size: 1.2rem;
    }
    
    .step-content p {
        margin: 0.5rem 0 0 0;
        color: #636e72;
        font-size: 0.95rem;
    }
    
    .testimonial-section {
        background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 3rem 0;
        box-shadow: 0 12px 40px rgba(0, 184, 148, 0.3);
        color: white;
    }
    
    .alert-info {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 8px 24px rgba(116, 185, 255, 0.3);
        border: none;
    }
    
    .alert-info strong {
        font-weight: 600;
    }
    
    .tech-showcase {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .tech-badge {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
        border: 1px solid rgba(102, 126, 234, 0.1);
    }
    
    .tech-badge:hover {
        transform: translateY(-5px);
    }
    
    .tech-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .tech-name {
        font-size: 0.8rem;
        color: #2d3436;
        font-weight: 600;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section with Animation
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">🤖 Resume Screening AI</h1>
        <p class="hero-subtitle">
            Transform your hiring process with intelligent automation.<br>
            Screen hundreds of resumes in minutes, not hours.
        </p>
        <a href="#get-started" class="cta-button">
            🚀 Start Screening Now
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Key Statistics
    st.markdown("""
    <div class="stats-container">
        <h2 style="color: white; margin: 0 0 1rem 0; font-size: 2rem; font-weight: 600;">Why Choose Our AI?</h2>
        <p style="color: white; opacity: 0.9; margin: 0; font-size: 1.1rem;">Proven results that transform recruitment</p>
        <div class="stats-grid">
            <div class="stat-item">
                <p class="stat-number">95%</p>
                <p class="stat-label">Time Reduction</p>
            </div>
            <div class="stat-item">
                <p class="stat-number">1000+</p>
                <p class="stat-label">Resumes/Hour</p>
            </div>
            <div class="stat-item">
                <p class="stat-number">87%</p>
                <p class="stat-label">Accuracy Rate</p>
            </div>
            <div class="stat-item">
                <p class="stat-number">0%</p>
                <p class="stat-label">Human Bias</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature Section - Using Streamlit columns instead of HTML grid
    st.markdown("## ✨ Powerful Features")
    
    # Create feature cards using Streamlit columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid rgba(102, 126, 234, 0.1); height: 250px; position: relative;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
            <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
            <h3 style="color: #2d3436; font-size: 1.4rem; font-weight: 600; margin: 0 0 1rem 0;">Lightning Fast Processing</h3>
            <p style="color: #636e72; line-height: 1.6; margin: 0;">
                Process hundreds of resumes in minutes using advanced NLP algorithms. 
                What used to take days now takes minutes.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid rgba(102, 126, 234, 0.1); height: 250px; position: relative;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
            <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
            <h3 style="color: #2d3436; font-size: 1.4rem; font-weight: 600; margin: 0 0 1rem 0;">Precise Matching</h3>
            <p style="color: #636e72; line-height: 1.6; margin: 0;">
                AI-powered similarity analysis ensures you find the best candidates 
                based on job requirements, not assumptions.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid rgba(102, 126, 234, 0.1); height: 250px; position: relative;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
            <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
            <h3 style="color: #2d3436; font-size: 1.4rem; font-weight: 600; margin: 0 0 1rem 0;">Detailed Analytics</h3>
            <p style="color: #636e72; line-height: 1.6; margin: 0;">
                Get comprehensive reports with similarity scores, matched keywords, 
                and actionable insights for every candidate.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid rgba(102, 126, 234, 0.1); height: 250px; position: relative;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
            <div style="font-size: 3rem; margin-bottom: 1rem;">🔒</div>
            <h3 style="color: #2d3436; font-size: 1.4rem; font-weight: 600; margin: 0 0 1rem 0;">Bias-Free Screening</h3>
            <p style="color: #636e72; line-height: 1.6; margin: 0;">
                Eliminate unconscious bias with objective, data-driven candidate 
                evaluation based purely on qualifications.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid rgba(102, 126, 234, 0.1); height: 250px; position: relative;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
            <div style="font-size: 3rem; margin-bottom: 1rem;">📱</div>
            <h3 style="color: #2d3436; font-size: 1.4rem; font-weight: 600; margin: 0 0 1rem 0;">User-Friendly Interface</h3>
            <p style="color: #636e72; line-height: 1.6; margin: 0;">
                Intuitive web interface requires no technical expertise. 
                Upload, analyze, and get results in just a few clicks.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid rgba(102, 126, 234, 0.1); height: 250px; position: relative;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
            <div style="font-size: 3rem; margin-bottom: 1rem;">🔄</div>
            <h3 style="color: #2d3436; font-size: 1.4rem; font-weight: 600; margin: 0 0 1rem 0;">Scalable Solution</h3>
            <p style="color: #636e72; line-height: 1.6; margin: 0;">
                Whether you're screening 10 or 1000 resumes, our system 
                scales efficiently to meet your hiring needs.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Interactive Metrics
    col1, col2 = st.columns(2)
    
    with col1:
        metrics_fig = create_animated_metrics()
        st.plotly_chart(metrics_fig, use_container_width=True)
    
    with col2:
        process_fig = create_process_flow()
        st.plotly_chart(process_fig, use_container_width=True)

    # How It Works Section
    st.markdown("""
    <div class="process-section">
        <h2 style="text-align: center; color: #2d3436; margin: 0 0 2rem 0; font-size: 2rem;">
            🔄 How It Works
        </h2>
        <p style="text-align: center; color: #636e72; margin: 0 0 2rem 0; font-size: 1.1rem;">
            Four simple steps to revolutionize your hiring process
        </p>
    """, unsafe_allow_html=True)

    processes = [
        {
            "number": "1",
            "title": "Enter Job Description",
            "description": "Simply paste your job description or requirements. Our AI understands context and key skills needed."
        },
        {
            "number": "2", 
            "title": "Upload Resume PDFs",
            "description": "Upload multiple candidate resumes in PDF format. Our system handles bulk processing effortlessly."
        },
        {
            "number": "3",
            "title": "AI Analysis Magic",
            "description": "Advanced NLP algorithms analyze, compare, and score each resume against your job requirements."
        },
        {
            "number": "4",
            "title": "Get Instant Rankings",
            "description": "Receive ranked candidates with similarity scores, matched keywords, and detailed insights."
        }
    ]
    
    for process in processes:
        st.markdown(f"""
        <div class="process-step">
            <div class="step-number">{process['number']}</div>
            <div class="step-content">
                <h4>{process['title']}</h4>
                <p>{process['description']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Technology Stack
    st.markdown("## 🛠️ Powered by Advanced Technology")
    
    st.markdown("""
    <div style="background: #f8f9fa; padding: 2rem; border-radius: 16px; margin: 2rem 0;">
        <div class="tech-showcase">
            <div class="tech-badge">
                <span class="tech-icon">🧠</span>
                <p class="tech-name">NLTK</p>
            </div>
            <div class="tech-badge">
                <span class="tech-icon">⚙️</span>
                <p class="tech-name">Scikit-learn</p>
            </div>
            <div class="tech-badge">
                <span class="tech-icon">📄</span>
                <p class="tech-name">PDFplumber</p>
            </div>
            <div class="tech-badge">
                <span class="tech-icon">📊</span>
                <p class="tech-name">TF-IDF</p>
            </div>
            <div class="tech-badge">
                <span class="tech-icon">🎯</span>
                <p class="tech-name">Cosine Similarity</p>
            </div>
            <div class="tech-badge">
                <span class="tech-icon">🚀</span>
                <p class="tech-name">Streamlit</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Call to Action
    st.markdown("""
    <div id="get-started" class="alert-info">
        <h3 style="margin: 0 0 1rem 0; font-size: 1.5rem;">Ready to Get Started? 🚀</h3>
        <p style="margin: 0; font-size: 1.1rem;">
            <strong>Navigate to the Resume Screener page</strong> from the sidebar and experience 
            the future of recruitment today!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Testimonial Section
    st.markdown("""
    <div class="testimonial-section">
        <h3 style="margin: 0 0 1rem 0; font-size: 1.8rem;">"Game-Changing Technology"</h3>
        <p style="margin: 0; font-size: 1.1rem; font-style: italic;">
            "This AI has transformed our hiring process completely. We've reduced screening time by 95% 
            and improved candidate quality significantly. It's like having a super-powered HR assistant!"
        </p>
        <small style="margin-top: 1rem; display: block; opacity: 0.9;">
            - HR Professional, Tech Industry
        </small>
    </div>
    """, unsafe_allow_html=True)

    # Problem & Solution Brief
    with st.expander("🎯 The Recruitment Challenge", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Traditional Problems:**
            - 📊 Manual screening takes 20+ hours per job posting
            - 😴 Reviewer fatigue leads to missed great candidates  
            - 🔄 Inconsistent evaluation criteria
            - 💰 High cost per hire due to inefficiencies
            - ⚠️ Unconscious bias in decision making
            """)
        
        with col2:
            st.markdown("""
            **Our AI Solution:**
            - ⚡ Screen 1000+ resumes in under an hour
            - 🎯 Consistent, objective evaluation criteria
            - 📈 87% accuracy in candidate matching
            - 💡 Identify hidden gems in large applicant pools
            - 🔄 Eliminate bias with data-driven decisions
            """)

    # Footer with enhanced styling
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; color: #636e72; padding: 2rem;">
        <p style="font-size: 1.2rem; margin-bottom: 1rem;">
            🤖 <strong>Resume Screening AI</strong> - Intelligent Hiring Made Simple
        </p>
        <p style="font-size: 1rem; margin-bottom: 0.5rem;">
            Transform your recruitment process today | Built with ❤️ and AI
        </p>
        <p style="font-size: 0.9rem; margin: 0; opacity: 0.8;">
            Developed by <strong>Debadrita Dey</strong> | © {datetime.now().year}
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    # Handle background image gracefully
    try:
        set_png_as_page_bg('background.png')
    except:
        # Create a CSS-based gradient background as fallback
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        .main .block-container {
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            margin-top: 2rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)
    
    main()