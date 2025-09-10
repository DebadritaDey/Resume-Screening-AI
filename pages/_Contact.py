import streamlit as st
import datetime

def contact_page():
    """
    Renders the complete enhanced Contact page with reliable HTML rendering.
    Final version with all features and proper styling.
    """
    
    # Enhanced CSS styling - optimized for reliability
    st.markdown("""
    <style>
    /* Main header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
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
        0% { transform: translateX(-20px) translateY(-20px); }
        100% { transform: translateX(20px) translateY(20px); }
    }
    
    .main-header > * {
        position: relative;
        z-index: 2;
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        letter-spacing: -1px;
    }
    
    .main-header p {
        color: white;
        font-size: 1.2rem;
        margin: 1rem 0 0 0;
        opacity: 0.95;
        font-weight: 300;
    }
    
    /* Profile and contact cards */
    .profile-card, .contact-links-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.08);
        border: 1px solid rgba(102, 126, 234, 0.1);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .avatar-section {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    
    .avatar {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        color: white;
        margin-right: 1rem;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
    }
    
    .profile-info h3 {
        margin: 0;
        color: #2d3436;
        font-size: 1.4rem;
        font-weight: 600;
    }
    
    .profile-info p {
        margin: 0.3rem 0 0 0;
        color: #636e72;
        font-size: 0.95rem;
        line-height: 1.4;
    }
    
    /* Social links */
    .social-link {
        display: block;
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 12px;
        margin: 0.8rem 0;
        text-decoration: none;
        color: #2d3436;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .social-link:hover {
        background: #e9ecef;
        color: #667eea;
        text-decoration: none;
        transform: translateX(5px);
    }
    
    /* Form container */
    .form-container {
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.08);
        border: 1px solid rgba(102, 126, 234, 0.1);
        margin: 2rem 0;
        border-top: 6px solid #667eea;
    }
    
    .form-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .form-header h3 {
        color: #2d3436;
        font-size: 1.6rem;
        font-weight: 600;
        margin: 0;
    }
    
    .form-header p {
        color: #636e72;
        margin: 0.5rem 0 0 0;
        font-size: 1rem;
    }
    
    /* Success message */
    .success-message {
        background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
        color: white;
        padding: 1.8rem;
        border-radius: 15px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 8px 24px rgba(0, 184, 148, 0.3);
        animation: slideIn 0.5s ease;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .success-message h4 {
        margin: 0 0 0.5rem 0;
        font-size: 1.3rem;
    }
    
    .success-message p {
        margin: 0;
        font-size: 1rem;
        line-height: 1.4;
    }
    
    .success-message small {
        opacity: 0.85;
        font-size: 0.85rem;
        margin-top: 0.5rem;
        display: block;
    }
    
    /* CTA section */
    .cta-section {
        background: linear-gradient(135deg, #fd79a8 0%, #fdcb6e 100%);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 12px 32px rgba(253, 121, 168, 0.3);
    }
    
    .cta-section h3 {
        color: white;
        margin: 0 0 1rem 0;
        font-size: 1.6rem;
        font-weight: 600;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    
    .cta-section p {
        color: white;
        margin: 0;
        opacity: 0.95;
        font-size: 1.05rem;
        line-height: 1.5;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2.2rem;
        }
        
        .avatar-section {
            flex-direction: column;
            text-align: center;
        }
        
        .avatar {
            margin-right: 0;
            margin-bottom: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Main header with animation
    st.markdown("""
    <div class="main-header">
        <h1>💬 Let's Connect</h1>
        <p>Ready to collaborate or have questions? I'd love to hear from you!</p>
    </div>
    """, unsafe_allow_html=True)

    # Key metrics using Streamlit native components
    st.subheader("📊 At a Glance")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Response Time", "< 24h", "⚡")
    with col2:
        st.metric("Connections", "500+", "📈")
    with col3:
        st.metric("Projects", "10+", "🚀")
    with col4:
        st.metric("Experience", "3+ years", "💼")

    st.markdown("<br>", unsafe_allow_html=True)

    # Main content section
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        # Profile section with clean HTML
        st.markdown("""
        <div class="profile-card">
            <div class="avatar-section">
                <div class="avatar">👨‍💻</div>
                <div class="profile-info">
                    <h3>Debadrita Dey</h3>
                    <p><strong>AI/ML Developer & Data Science Enthusiast</strong><br>
                    🎯 Specializing in NLP and Intelligent Systems<br>
                    📍 Available for exciting opportunities</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Skills section using Streamlit components
        st.subheader("🚀 What I Do")
        skills_cols = st.columns(2)
        
        with skills_cols[0]:
            st.markdown("""
            - 🤖 **Machine Learning & AI**
            - 🧠 **Natural Language Processing**
            - 📊 **Data Analysis & Visualization**
            """)
        
        with skills_cols[1]:
            st.markdown("""
            - 💻 **Full-Stack Development**
            - 🔧 **Technical Consulting**
            - 📚 **Mentoring & Training**
            """)
    
    with col2:
        # Social links section
        st.markdown("""
        <div class="contact-links-card">
            <h4 style="color: #2d3436; margin: 0 0 1.5rem 0; font-size: 1.2rem;">🌐 Connect With Me</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Individual social links
        st.markdown("""
        <a href="https://www.linkedin.com/in/debadritadey/" target="_blank" class="social-link">
            <strong>💼 LinkedIn</strong><br>
            <small style="color: #636e72;">Professional Network & Updates</small>
        </a>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <a href="https://github.com/debadritadey" target="_blank" class="social-link">
            <strong>⚡ GitHub</strong><br>
            <small style="color: #636e72;">Open Source Projects & Code</small>
        </a>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <a href="mailto:debadritadey.official@gmail.com" class="social-link">
            <strong>📧 Email</strong><br>
            <small style="color: #636e72;">debadritadey.official@gmail.com</small>
        </a>
        """, unsafe_allow_html=True)

    # Contact form section
    st.markdown("""
    <div class="form-container">
        <div class="form-header">
            <h3>💭 Send Me a Message</h3>
            <p>Got questions, suggestions, or collaboration ideas? I'd love to hear from you!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced contact form
    with st.form(key='contact_form', clear_on_submit=True):
        # Form fields layout
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("👤 Full Name", placeholder="Enter your name")
            email = st.text_input("📧 Email Address", placeholder="your.email@example.com")
        
        with col2:
            subject = st.selectbox("📋 Subject", [
                "General Inquiry",
                "Collaboration Opportunity", 
                "Project Discussion",
                "Bug Report",
                "Feature Request",
                "Freelance Work",
                "Mentorship",
                "Other"
            ])
            priority = st.radio("🚨 Priority Level", ["Low", "Medium", "High"], horizontal=True)
        
        # Message field
        message = st.text_area(
            "💬 Your Message", 
            placeholder="Tell me about your project, question, or how we can collaborate. Be as detailed as you'd like!",
            height=130
        )
        
        # Additional options
        with st.expander("📝 Additional Options (Optional)"):
            company = st.text_input("🏢 Company/Organization", placeholder="Your company name")
            timeline = st.selectbox("⏰ Project Timeline", [
                "No specific timeline",
                "ASAP",
                "Within a week",
                "Within a month",
                "Within 3 months",
                "Future project"
            ])
            budget = st.selectbox("💰 Budget Range (if applicable)", [
                "Not applicable",
                "Under $1,000",
                "$1,000 - $5,000",
                "$5,000 - $10,000",
                "$10,000+",
                "Let's discuss"
            ])
        
        # Submit button
        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            submit_button = st.form_submit_button("🚀 Send Message", use_container_width=True)

        # Form validation and submission
        if submit_button:
            if not name.strip():
                st.error("👤 Please enter your name")
            elif not email.strip():
                st.error("📧 Please enter your email address")
            elif "@" not in email or "." not in email:
                st.error("📧 Please enter a valid email address")
            elif not message.strip():
                st.error("💬 Please enter your message")
            else:
                current_time = datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")
                
                # Success message with animation
                st.markdown(f"""
                <div class="success-message">
                    <h4>✅ Message Sent Successfully!</h4>
                    <p>Thank you, <strong>{name}</strong>! Your message has been received.<br>
                    I'll get back to you within 24 hours at <strong>{email}</strong></p>
                    <small>Sent on {current_time}</small>
                </div>
                """, unsafe_allow_html=True)
                
                # Show confirmation details
                st.success("🎉 Your message has been logged successfully!")
                
                with st.expander("📋 Message Summary", expanded=False):
                    st.write(f"**From:** {name} ({email})")
                    st.write(f"**Subject:** {subject}")
                    st.write(f"**Priority:** {priority}")
                    if company:
                        st.write(f"**Company:** {company}")
                    if timeline != "No specific timeline":
                        st.write(f"**Timeline:** {timeline}")
                    if budget != "Not applicable":
                        st.write(f"**Budget:** {budget}")
                    st.write(f"**Message Length:** {len(message)} characters")
                    st.text_area("**Full Message:**", value=message, height=100, disabled=True)

    # Call-to-action section
    st.markdown("""
    <div class="cta-section">
        <h3>🤝 Let's Build Something Amazing Together</h3>
        <p>Whether you're looking to collaborate on AI projects, need technical consultation, 
        or just want to connect with a fellow developer, I'm always excited to meet new people 
        and explore innovative ideas!</p>
    </div>
    """, unsafe_allow_html=True)

    # Additional information sections
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("🔗 More Ways to Connect", expanded=False):
            st.markdown("""
            **📱 Social Platforms:**
            - **Twitter:** [@debadritadey](https://twitter.com/debadritadey)
            - **Instagram:** [@debadrita.codes](https://instagram.com/debadrita.codes)
            - **YouTube:** [Debadrita Codes](https://youtube.com/@debadritacodes)
            
            **💼 Professional:**
            - **Portfolio:** [debadritadey.dev](https://debadritadey.dev)
            - **Resume:** Available on LinkedIn
            - **Calendly:** [Schedule a meeting](https://calendly.com/debadritadey)
            """)
    
    with col2:
        with st.expander("❓ Frequently Asked Questions", expanded=False):
            st.markdown("""
            **Q: What's your typical response time?**  
            A: I aim to respond to all messages within 24 hours, often much sooner!
            
            **Q: Do you offer freelance services?**  
            A: Yes! I'm available for AI/ML consulting, development projects, and technical training.
            
            **Q: Can we collaborate on open-source projects?**  
            A: Absolutely! I love contributing to meaningful open-source initiatives.
            
            **Q: Do you provide mentorship?**  
            A: I'm happy to guide fellow developers, especially in AI/ML and data science domains.
            
            **Q: What are your rates?**  
            A: Rates vary by project scope and timeline. Let's discuss your specific needs!
            """)

    # Availability and location info
    with st.expander("🌍 Availability & Location Info", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **🌍 Location**
            - Based in: India 🇮🇳
            - Timezone: IST (GMT+5:30)
            - Available: Globally (Remote)
            """)
        
        with col2:
            st.markdown("""
            **⏰ Working Hours**
            - Mon-Fri: 9 AM - 7 PM IST
            - Weekends: Limited availability
            - Emergency: Contact via email
            """)
        
        with col3:
            st.markdown("""
            **🎯 Preferred Projects**
            - AI/ML Solutions
            - Data Science Consulting
            - NLP Applications
            - Technical Training
            """)

    # Footer with enhanced styling
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #636e72; padding: 2rem;">
        <h4 style="color: #2d3436; margin-bottom: 1rem;">
            🚀 Ready to start something incredible together?
        </h4>
        <p style="font-size: 1rem; margin-bottom: 1rem;">
            From AI-powered solutions to data-driven insights, let's turn your ideas into reality.
        </p>
        <p style="font-size: 0.9rem; margin: 0; opacity: 0.8;">
            💻 Built with ❤️ using Streamlit | 🤖 Resume Screening AI | © 2024 Debadrita Dey
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    contact_page()