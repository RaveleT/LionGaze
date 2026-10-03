import os
import streamlit as st
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

# Page configuration
st.set_page_config(
    page_title="LionGaze Product Presentation", page_icon="🦁", layout="wide"
)

st.markdown(
    """
    <style>
        /* Improve contrast for muted text, small labels, and captions */
        p, span, label, .streamlit-expanderHeader, [data-testid="stMetricLabel"] {
            color: #E2E8F0 !important;
        }
        
        /* Specific boost for secondary/muted metadata headers */
        .muted-label, small, [data-testid="stCaptionContainer"] {
            color: #94A3B8 !important;
        }

        /* Ensure metric values stand out brightly */
        [data-testid="stMetricValue"] {
            color: #F8FAFC !important;
        }

        /* Fix button text contrast inside custom buttons */
        div.stButton > button {
            color: #0F172A !important;
            background-color: #38BDF8 !important;
            font-weight: 600;
            border: none;
        }
        
        div.stButton > button:hover {
            background-color: #0EA5E9 !important;
            color: #FFFFFF !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# CSS Footer and Header Remover Injection + Dark Theme Enforcement
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Dark Mode Enforcement & Custom Styling */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .slide-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 24px;
        color: #f8fafc;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }
    .slide-title {
        color: #06b6d4;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .slide-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 16px;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def check_password():
    """Returns True if the user enters the correct password/PIN."""

    def password_entered():
        correct_password = st.secrets.get("app_password", "9452")
        if st.session_state["password_input"] == correct_password:
            st.session_state["password_correct"] = True
            del st.session_state["password_input"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("### 🔐 Restricted Access — LionGaze")
        st.text_input(
            "Enter Access PIN / Password:",
            type="password",
            on_change=password_entered,
            key="password_input",
        )
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("### 🔐 Restricted Access — LionGaze")
        st.text_input(
            "Enter Access PIN / Password:",
            type="password",
            on_change=password_entered,
            key="password_input",
        )
        st.error("😕 Incorrect password or PIN. Please try again.")
        return False
    else:
        return True


if not check_password():
    st.stop()


# ==========================================
# MAIN PRODUCT PRESENTATION (Protected Area)
# ==========================================

st.title("🦁 LionGaze (狮视) — Product Presentation")
st.subheader(
    "AI-Powered Road-Mapping & Safety Device for Logistics and Municipal Infrastructure"
)

st.markdown("---")

view_mode = st.radio(
    "Select View Mode:",
    ["📊 Dashboard & Metrics", "🖥️ Interactive Slide Deck Viewer"],
    horizontal=True,
)

if view_mode == "📊 Dashboard & Metrics":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Development Stage", "R&D / Working Prototype")
    with col2:
        st.metric("Core Vision Model", "YOLO11n (Fine-tuned)")
    with col3:
        st.metric("Target Market", "Logistics & Municipalities")

    st.markdown("### 🚀 Executive Summary")
    st.write(
        "LionGaze maps road potholes using an onboard camera and electronic"
        " sensors, capturing exact geolocated coordinates to construct dynamic"
        " road profiles. Data is edge-preprocessed and synchronized with the"
        " cloud to give following vehicle fleets instant hazard warnings and"
        " provide municipalities with data-driven repair insights."
    )

    st.markdown("---")
    st.markdown("### 🤖 YOLO11n Model Performance & Benchmarks")

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("mAP50", "88.50%")
    with m2:
        st.metric("mAP50-95", "47.51%")
    with m3:
        st.metric("Precision", "93.13%")
    with m4:
        st.metric("Recall", "80.08%")

    with st.expander("🛠️ View Detailed Training & Hardware Metrics"):
        st.markdown("""
            - **Environment & Hardware:** Ultralytics v8.4.171 | Python 3.13.15 | PyTorch 2.14.1+cu130 | NVIDIA Tesla T4 (14,913 MiB VRAM)
            - **Model Architecture:** YOLO11n Fused (100 layers, 2,582,347 parameters, 6.4 GFLOPs)
            - **Dataset Validation:** 92 test images, 251 instances evaluated.
            - **Inference Speed Breakdown (per image):**
              - Preprocess: `10.1 ms`
              - Inference: `6.6 ms`
              - Loss: `0.0 ms`
              - Postprocess: `5.6 ms`
            """)

    st.markdown("---")
    st.markdown("### 📊 Live System Status / Demo")
    st.info("System operational. Edge sensor node connected.")

    if st.button("Run Simulation Check"):
        st.success(
            "Pothole cluster detected at GPS [-23.0021, 30.4485]. Fleet broadcast successful."
        )

else:
    st.markdown("### 🖥️ Interactive Slide Deck Viewer")
    st.write("Browse through the rendered slide cards of your pitch deck below.")

    # Download button code removed entirely

    st.markdown("---")

    slide_option = st.selectbox(
        "Select Slide to Preview:",
        [
            "Slide 1: Title & Introduction",
            "Slide 2: Problem Statement",
            "Slide 3: Solution Overview",
            "Slide 4: Technology & Prototyping",
            "Slide 5: Market Potential & Team",
        ],
    )

    if "Slide 1" in slide_option:
        st.markdown(
            """
            <div class="slide-card" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); text-align: center; padding: 50px;">
                <div style="color: #06b6d4; font-weight: bold; font-size: 1.1rem; letter-spacing: 2px; margin-bottom: 15px;">LIONGAZE (狮视) | ZONE 6 (AFRICA)</div>
                <div style="font-size: 2.5rem; font-weight: 800; color: #ffffff; margin-bottom: 20px;">Smart Road Infrastructure & Fleet Protection</div>
                <div style="color: #94a3b8; font-size: 1.1rem;">The 5th China-Africa Youth Innovation and Entrepreneurship Competition</div>
                <div style="color: #06b6d4; font-size: 1rem; margin-top: 15px;">Presented by Thendo Ravele | University of Venda (Aveler Solutions)</div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    elif "Slide 2" in slide_option:
        st.markdown(
            """
            <div class="slide-card">
                <div style="color: #06b6d4; font-size: 0.9rem; font-weight: bold; text-transform: uppercase;">Problem Statement</div>
                <div class="slide-title">Degraded Road Infrastructure Threatens Developing Economies</div>
                <div style="display: flex; gap: 20px; margin-top: 20px;">
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px; border-left: 4px solid #ef4444;">
                        <b>Economic Toll on Logistics</b><br><br>Potholes and unmonitored road damage cost logistics companies millions annually in vehicle wear, tire destruction, and delayed freight delivery across developing regions.
                    </div>
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                        <b>Safety Hazards</b><br><br>Unpredicted road hazards present severe accident risks for both personal and public transport networks daily, threatening commuter safety and transport reliability.
                    </div>
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px; border-left: 4px solid #3b82f6;">
                        <b>Reactive Responses</b><br><br>Municipal authorities lack real-time, precise data on road damage severity, leading to inefficient resource allocation and prolonged infrastructure downtime.
                    </div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    elif "Slide 3" in slide_option:
        st.markdown(
            """
            <div class="slide-card">
                <div style="color: #06b6d4; font-size: 0.9rem; font-weight: bold; text-transform: uppercase;">Solution Overview</div>
                <div class="slide-title">LionGaze: AI-Powered Edge Mapping for Safer Roads</div>
                <div style="display: flex; gap: 20px; margin-top: 20px;">
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px; border-top: 4px solid #06b6d4;">
                        <b>01 / Crowdsourced Sensors</b><br><br>Transform existing delivery and public transport fleets into active diagnostic sensors capturing continuous road conditions without extra hardware overhead.
                    </div>
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px; border-top: 4px solid #10b981;">
                        <b>02 / Edge Pre-Processing</b><br><br>Utilize onboard edge computing to detect and classify road anomalies locally, filtering noise before transmitting lightweight, high-value data packets.
                    </div>
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px; border-top: 4px solid #8b5cf6;">
                        <b>03 / Municipal Intelligence</b><br><br>Deliver real-time, high-precision geospatial maps and severity analytics directly to city planners for proactive infrastructure maintenance.
                    </div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    elif "Slide 4" in slide_option:
        st.markdown(
            """
            <div class="slide-card">
                <div style="color: #06b6d4; font-size: 0.9rem; font-weight: bold; text-transform: uppercase;">Technology & Prototyping</div>
                <div class="slide-title">Robust R&D Built on Edge Computing and Machine Learning</div>
                <div style="display: flex; gap: 20px; margin-top: 20px;">
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px;">
                        <b>Hardware Setup</b><br><br>Powered by Raspberry Pi 4B paired with integrated IMU sensors and high-definition optical capture units for precise vibration and visual mapping.
                    </div>
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px;">
                        <b>Machine Learning Models</b><br><br>Optimized computer vision models running locally on edge hardware to identify potholes, cracks, and road degradation instantly.
                    </div>
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px;">
                        <b>Functional Prototype Stage</b><br><br>Current hardware enclosure successfully designed and 3D-printed, moving through rigorous road-testing phases for field validation.
                    </div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    elif "Slide 5" in slide_option:
        st.markdown(
            """
            <div class="slide-card">
                <div style="color: #06b6d4; font-size: 0.9rem; font-weight: bold; text-transform: uppercase;">Market Potential & Team</div>
                <div class="slide-title">Positioned for Scalable Impact in Developing Nations</div>
                <div style="display: flex; gap: 20px; margin-top: 20px;">
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px;">
                        <b>Commercial Value</b><br><br>Targeting municipal infrastructure contracts and logistics fleet operators across Africa and emerging markets to drastically reduce maintenance and repair costs.
                    </div>
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px;">
                        <b>Team Credentials</b><br><br>Developed under Aveler Solutions at the University of Venda (UNIVEN), competing in the AI & Green Technology category under Zone 6.
                    </div>
                    <div style="flex: 1; background: #0f172a; padding: 20px; border-radius: 8px;">
                        <b>Strategic Scalability</b><br><br>Modular architecture enables rapid deployment across diverse municipal road networks with minimal capital expenditure.
                    </div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
