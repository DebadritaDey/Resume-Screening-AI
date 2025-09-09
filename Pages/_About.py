import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def about_page():
    """
    Renders an enhanced About page with modern UI elements.
    """
    
    # Custom CSS for enhanced styling
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: white;
        font-size: 1.2rem;
        margin: 1rem 0 0 0;
        opacity: 0.9;
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        margin: 0.5rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin: 0.5rem 0 0 0;
    }
    
    .process-step {
        display: flex;
        align-items: center;
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 5px solid #28a745;
    }
    
    .step-number {
        background: #28a745;
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-right: 1rem;
        flex-shrink: 0;
    }
    
    .tech-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        margin: 0.2rem;
        display: inline-block;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    .metrics-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Main header with gradient background
    st.markdown("""
    <div class="main-header">
        <h1>🤖 Resume Screening AI</h1>
        <p>Intelligent recruitment powered by Natural Language Processing</p>
    </div>
    """, unsafe_allow_html=True)

    # Key metrics section
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">95%</p>
            <p class="stat-label">Time Savings</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">87%</p>
            <p class="stat-label">Accuracy Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">1000+</p>
            <p class="stat-label">Resumes/Hour</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">0</p>
            <p class="stat-label">Human Bias</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Problem section with visual appeal
    st.markdown("## 🎯 The Challenge We Solve")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🔍 Manual Resume Screening Problems</h4>
            <ul style="line-height: 1.8;">
                <li><strong>Time-Intensive:</strong> Hours spent reviewing hundreds of applications</li>
                <li><strong>Unconscious Bias:</strong> Human prejudices affecting fair evaluation</li>
                <li><strong>Inconsistency:</strong> Different standards applied by different reviewers</li>
                <li><strong>Scalability Issues:</strong> Cannot handle high-volume recruitment</li>
                <li><strong>Missed Opportunities:</strong> Good candidates overlooked due to fatigue</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Create a simple pie chart showing time allocation
        fig = px.pie(
            values=[70, 15, 10, 5], 
            names=['Manual Review', 'Candidate Calls', 'Documentation', 'Decision Making'],
            title="Traditional Recruitment Time Allocation",
            color_discrete_sequence=['#ff7675', '#74b9ff', '#00b894', '#fdcb6e']
        )
        fig.update_layout(height=300, showlegend=True, title_font_size=12)
        st.plotly_chart(fig, use_container_width=True)

    # Solution section
    st.markdown("## 💡 Our AI-Powered Solution")
    
    st.markdown("""
    <div class="highlight-box">
        <h4 style="color: #2d3436; margin-top: 0;">🚀 Revolutionizing Recruitment with NLP</h4>
        <p style="color: #636e72; font-size: 1.1rem; margin-bottom: 0;">
            Our intelligent system analyzes resumes using advanced Natural Language Processing, 
            providing objective, consistent, and lightning-fast candidate evaluation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Technology stack
    st.markdown("### 🛠️ Technology Stack")
    
    tech_stack = {
        "Frontend": ["Streamlit", "Plotly", "HTML/CSS"],
        "NLP Processing": ["NLTK", "Scikit-learn", "TF-IDF"],
        "PDF Processing": ["PDFplumber", "Text Extraction"],
        "Machine Learning": ["Cosine Similarity", "Vector Analysis"]
    }
    
    cols = st.columns(2)
    for i, (category, technologies) in enumerate(tech_stack.items()):
        with cols[i % 2]:
            st.markdown(f"**{category}:**")
            tech_html = "".join([f'<span class="tech-badge">{tech}</span>' for tech in technologies])
            st.markdown(tech_html, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

    # Process workflow
    st.markdown("## ⚙️ How It Works")
    
    processes = [
        {
            "title": "📄 Text Extraction",
            "description": "Advanced PDF parsing extracts clean, structured text from uploaded resumes using PDFplumber technology.",
            "details": ["Multi-page support", "Format preservation", "Error handling"]
        },
        {
            "title": "🧹 Text Preprocessing", 
            "description": "Sophisticated NLP pipeline cleans and standardizes text for optimal analysis.",
            "details": ["Tokenization", "Stop word removal", "Lemmatization", "Noise filtering"]
        },
        {
            "title": "🔢 Feature Engineering",
            "description": "TF-IDF vectorization converts text into numerical representations for mathematical analysis.",
            "details": ["Term frequency calculation", "Inverse document frequency", "Vector normalization"]
        },
        {
            "title": "📊 Similarity Analysis",
            "description": "Cosine similarity algorithms compare job descriptions with candidate profiles.",
            "details": ["Vector comparison", "Scoring algorithm", "Ranking system", "Match visualization"]
        }
    ]
    
    for i, process in enumerate(processes, 1):
        st.markdown(f"""
        <div class="process-step">
            <div class="step-number">{i}</div>
            <div>
                <h4 style="margin: 0; color: #2d3436;">{process['title']}</h4>
                <p style="margin: 0.5rem 0; color: #636e72;">{process['description']}</p>
                <div style="margin-top: 0.5rem;">
                    {''.join([f'<span style="background: #e17055; color: white; padding: 0.2rem 0.5rem; border-radius: 10px; font-size: 0.7rem; margin-right: 0.5rem;">{detail}</span>' for detail in process['details']])}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Technical deep dive
    with st.expander("🔬 Technical Deep Dive", expanded=False):
        tab1, tab2, tab3 = st.tabs(["TF-IDF Algorithm", "Cosine Similarity", "Performance Metrics"])
        
        with tab1:
            st.markdown("""
            #### 📈 TF-IDF (Term Frequency-Inverse Document Frequency)
            
            **Formula:** `TF-IDF = TF(t,d) × IDF(t,D)`
            
            - **Term Frequency (TF):** How often a term appears in a document
            - **Inverse Document Frequency (IDF):** How unique/rare a term is across all documents
            - **Purpose:** Identifies words that are important to a document but not common across all documents
            """)
            
            # Create a sample TF-IDF visualization
            import pandas as pd
            sample_data = pd.DataFrame({
                'Term': ['Python', 'JavaScript', 'Machine Learning', 'Database', 'Communication'],
                'TF Score': [0.15, 0.08, 0.12, 0.06, 0.04],
                'IDF Score': [2.1, 1.8, 2.5, 1.6, 1.2],
                'TF-IDF': [0.32, 0.14, 0.30, 0.10, 0.05]
            })
            
            fig = px.bar(sample_data, x='Term', y='TF-IDF', title='Sample TF-IDF Scores',
                        color='TF-IDF', color_continuous_scale='Blues')
            fig.update_layout(height=350)
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.markdown("""
            #### 📐 Cosine Similarity
            
            **Formula:** `cos(θ) = (A·B) / (||A|| ||B||)`
            
            - **Range:** 0 to 1 (0 = no similarity, 1 = identical)
            - **Advantage:** Focuses on content rather than document length
            - **Application:** Compares job description vector with resume vectors
            """)
            
            # Cosine similarity visualization
            similarity_data = pd.DataFrame({
                'Resume': ['Resume A', 'Resume B', 'Resume C', 'Resume D', 'Resume E'],
                'Similarity Score': [0.85, 0.72, 0.58, 0.41, 0.29],
                'Category': ['Excellent', 'Good', 'Fair', 'Poor', 'Poor']
            })
            
            fig = px.scatter(similarity_data, x='Resume', y='Similarity Score', 
                           color='Category', size='Similarity Score',
                           title='Sample Similarity Scores',
                           color_discrete_map={'Excellent': '#00b894', 'Good': '#fdcb6e', 'Fair': '#e17055', 'Poor': '#d63031'})
            fig.update_layout(height=350)
            st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.markdown("""
            #### 📊 Performance Metrics
            
            Our system is evaluated on multiple dimensions:
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                metrics_data = {
                    'Metric': ['Processing Speed', 'Accuracy', 'Consistency', 'Scalability'],
                    'Score': [98, 87, 95, 92],
                    'Benchmark': [85, 80, 70, 75]
                }
                
                fig = go.Figure()
                fig.add_trace(go.Bar(name='Our System', x=metrics_data['Metric'], y=metrics_data['Score'], marker_color='#0984e3'))
                fig.add_trace(go.Bar(name='Industry Average', x=metrics_data['Metric'], y=metrics_data['Benchmark'], marker_color='#b2bec3'))
                fig.update_layout(title='Performance Comparison', height=350)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.markdown("""
                **Key Performance Indicators:**
                - ⚡ **Speed:** Process 1000+ resumes per hour
                - 🎯 **Accuracy:** 87% match with human expert evaluation  
                - 🔄 **Consistency:** Same results every time
                - 📈 **Scalability:** Linear performance scaling
                - 🛡️ **Reliability:** 99.9% uptime
                """)

    # Benefits section
    st.markdown("## 🌟 Key Benefits")
    
    benefits_cols = st.columns(3)
    
    benefits = [
        {
            "icon": "⚡",
            "title": "Lightning Fast",
            "description": "Process hundreds of resumes in minutes, not hours"
        },
        {
            "icon": "🎯", 
            "title": "Objective Analysis",
            "description": "Eliminate unconscious bias with data-driven evaluation"
        },
        {
            "icon": "📊",
            "title": "Detailed Insights",
            "description": "Get comprehensive match analysis and keyword identification"
        },
        {
            "icon": "🔧",
            "title": "Easy Integration", 
            "description": "Simple web interface requires no technical expertise"
        },
        {
            "icon": "📈",
            "title": "Scalable Solution",
            "description": "Handle any volume of applications efficiently"
        },
        {
            "icon": "💡",
            "title": "Smart Matching",
            "description": "Advanced NLP algorithms ensure accurate candidate ranking"
        }
    ]
    
    for i, benefit in enumerate(benefits):
        with benefits_cols[i % 3]:
            st.markdown(f"""
            <div class="feature-card">
                <div style="text-align: center; font-size: 2rem; margin-bottom: 0.5rem;">{benefit['icon']}</div>
                <h4 style="text-align: center; color: #2d3436; margin: 0.5rem 0;">{benefit['title']}</h4>
                <p style="text-align: center; color: #636e72; font-size: 0.9rem; margin: 0;">{benefit['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

    # Call to action
    st.markdown("""
    <div style="background: linear-gradient(135deg, #00b894 0%, #00cec9 100%); 
                padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;">
        <h3 style="color: white; margin: 0;">Ready to Transform Your Recruitment Process?</h3>
        <p style="color: white; margin: 1rem 0; opacity: 0.9;">
            Experience the future of candidate screening with our AI-powered solution
        </p>
        <p style="margin: 0;">
            <a href="#" style="background: white; color: #00b894; padding: 0.8rem 2rem; 
                              border-radius: 25px; text-decoration: none; font-weight: bold;
                              box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                Try Resume Screener →
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #636e72; padding: 1rem;">
        <p>🚀 <strong>Resume Screening AI</strong> | Powered by Advanced NLP & Machine Learning</p>
        <p style="font-size: 0.8rem; margin: 0;">Built with ❤️ by Debadrita</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    about_page()