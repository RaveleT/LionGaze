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
# GENERATE PPTX ON THE FLY FOR DOWNLOAD
# ==========================================
def generate_pptx_file():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    DARK_BG = RGBColor(15, 23, 42)
    LIGHT_BG = RGBColor(248, 250, 252)
    CARD_BG = RGBColor(255, 255, 255)
    ACCENT_CYAN = RGBColor(6, 182, 212)
    TEXT_DARK = RGBColor(15, 23, 42)
    TEXT_MUTED = RGBColor(100, 116, 139)
    BORDER_COLOR = RGBColor(226, 232, 240)

    def set_bg(slide, color):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def add_header(slide, tracker, title):
        tb_tr = slide.shapes.add_textbox(
            Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.35)
        )
        p_tr = tb_tr.text_frame.paragraphs[0]
        p_tr.text = tracker.upper()
        p_tr.font.size = Pt(11)
        p_tr.font.bold = True
        p_tr.font.color.rgb = ACCENT_CYAN
        p_tr.font.name = "Arial"

        tb_ti = slide.shapes.add_textbox(
            Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.9)
        )
        tb_ti.text_frame.word_wrap = True
        p_ti = tb_ti.text_frame.paragraphs[0]
        p_ti.text = title
        p_ti.font.size = Pt(24)
        p_ti.font.bold = True
        p_ti.font.color.rgb = TEXT_DARK
        p_ti.font.name = "Arial"

    # Slide 1
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1, DARK_BG)
    bar = s1.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_CYAN
    bar.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p0 = tf1.paragraphs[0]
    p0.text = "LIONGAZE (狮视) | ZONE 6 (AFRICA)"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_CYAN
    p0.space_after = Pt(12)

    p1 = tf1.add_paragraph()
    p1.text = "Smart Road Infrastructure & Fleet Protection"
    p1.font.size = Pt(38)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)
    p1.space_after = Pt(15)

    p2 = tf1.add_paragraph()
    p2.text = (
        "The 5th China-Africa Youth Innovation and Entrepreneurship Competition\n"
        "Presented by Thendo Ravele | University of Venda (Aveler Solutions)"
    )
    p2.font.size = Pt(16)
    p2.font.color.rgb = RGBColor(148, 163, 184)

    # Slide 2
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2, LIGHT_BG)
    add_header(
        s2,
        "Problem Statement",
        "Degraded Road Infrastructure Threatens Developing Economies & Logistics",
    )
    problems = [
        (
            "Economic Toll on Logistics",
            (
                "Potholes and unmonitored road damage cost logistics companies"
                " millions annually in vehicle wear, tire destruction, and"
                " delayed freight delivery across developing regions."
            ),
        ),
        (
            "Safety Hazards for Road Users",
            (
                "Unpredicted road hazards present severe accident risks for both"
                " personal and public transport networks daily, threatening"
                " commuter safety and transport reliability."
            ),
        ),
        (
            "Reactive Municipal Responses",
            (
                "Municipal authorities lack real-time, precise data on road"
                " damage severity, leading to inefficient resource allocation and"
                " prolonged infrastructure downtime."
            ),
        ),
    ]
    for i, (h, b) in enumerate(problems):
        cx = Inches(0.8 + i * 4.0)
        card = s2.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(2.1), Inches(3.64), Inches(4.5)
        )
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR
        tb = s2.shapes.add_textbox(
            cx + Inches(0.3), Inches(2.3), Inches(3.04), Inches(4.1)
        )
        tf = tb.text_frame
        tf.word_wrap = True
        ph = tf.paragraphs[0]
        ph.text = h
        ph.font.size = Pt(17)
        ph.font.bold = True
        ph.font.color.rgb = TEXT_DARK
        ph.space_after = Pt(12)
        pb = tf.add_paragraph()
        pb.text = b
        pb.font.size = Pt(13)
        pb.font.color.rgb = TEXT_MUTED

    # Slide 3
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3, LIGHT_BG)
    add_header(
        s3,
        "Solution Overview",
        "LionGaze: AI-Powered Edge Mapping for Safer Roads",
    )
    solutions = [
        (
            "01 / Crowdsourced Sensors",
            (
                "Transform existing delivery and public transport fleets into"
                " active diagnostic sensors capturing continuous road conditions"
                " without extra hardware overhead."
            ),
        ),
        (
            "02 / Edge Pre-Processing",
            (
                "Utilize onboard edge computing to detect and classify road"
                " anomalies locally, filtering noise before transmitting"
                " lightweight, high-value data packets."
            ),
        ),
        (
            "03 / Municipal Intelligence",
            (
                "Deliver real-time, high-precision geospatial maps and severity"
                " analytics directly to city planners for proactive"
                " infrastructure maintenance."
            ),
        ),
    ]
    for i, (h, b) in enumerate(solutions):
        cx = Inches(0.8 + i * 4.0)
        card = s3.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(2.1), Inches(3.64), Inches(4.5)
        )
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR
        tb = s3.shapes.add_textbox(
            cx + Inches(0.3), Inches(2.3), Inches(3.04), Inches(4.1)
        )
        tf = tb.text_frame
        tf.word_wrap = True
        ph = tf.paragraphs[0]
        ph.text = h
        ph.font.size = Pt(17)
        ph.font.bold = True
        ph.font.color.rgb = TEXT_DARK
        ph.space_after = Pt(12)
        pb = tf.add_paragraph()
        pb.text = b
        pb.font.size = Pt(13)
        pb.font.color.rgb = TEXT_MUTED

    # Slide 4
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4, LIGHT_BG)
    add_header(
        s4,
        "Technology & Prototyping",
        "Robust R&D Built on Edge Computing and Machine Learning",
    )
    tech_items = [
        (
            "Hardware Setup",
            (
                "Powered by Raspberry Pi 4B paired with integrated IMU sensors"
                " and high-definition optical capture units for precise vibration"
                " and visual mapping."
            ),
        ),
        (
            "Machine Learning Models",
            (
                "Optimized computer vision models running locally on edge"
                " hardware to identify potholes, cracks, and road degradation"
                " instantly."
            ),
        ),
        (
            "Functional Prototype Stage",
            (
                "Current hardware enclosure successfully designed and"
                " 3D-printed, moving through rigorous road-testing phases for"
                " field validation."
            ),
        ),
    ]
    for i, (h, b) in enumerate(tech_items):
        cx = Inches(0.8 + i * 4.0)
        card = s4.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(2.1), Inches(3.64), Inches(4.5)
        )
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR
        tb = s4.shapes.add_textbox(
            cx + Inches(0.3), Inches(2.3), Inches(3.04), Inches(4.1)
        )
        tf = tb.text_frame
        tf.word_wrap = True
        ph = tf.paragraphs[0]
        ph.text = h
        ph.font.size = Pt(17)
        ph.font.bold = True
        ph.font.color.rgb = TEXT_DARK
        ph.space_after = Pt(12)
        pb = tf.add_paragraph()
        pb.text = b
        pb.font.size = Pt(13)
        pb.font.color.rgb = TEXT_MUTED

    # Slide 5
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5, LIGHT_BG)
    add_header(
        s5,
        "Market Potential & Team",
        "Positioned for Scalable Impact in Developing Nations",
    )
    market_items = [
        (
            "Commercial & Social Value",
            (
                "Targeting municipal infrastructure contracts and logistics"
                " fleet operators across Africa and emerging markets to"
                " drastically reduce maintenance and repair costs."
            ),
        ),
        (
            "Team Credentials & Vision",
            (
                "Developed under Aveler Solutions at the University of Venda"
                " (UNIVEN), competing in the AI & Green Technology category under"
                " Zone 6."
            ),
        ),
        (
            "Strategic Scalability",
            (
                "Modular architecture enables rapid deployment across diverse"
                " municipal road networks with minimal capital expenditure."
            ),
        ),
    ]
    for i, (h, b) in enumerate(market_items):
        cx = Inches(0.8 + i * 4.0)
        card = s5.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(2.1), Inches(3.64), Inches(4.5)
        )
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR
        tb = s5.shapes.add_textbox(
            cx + Inches(0.3), Inches(2.3), Inches(3.04), Inches(4.1)
        )
        tf = tb.text_frame
        tf.word_wrap = True
        ph = tf.paragraphs[0]
        ph.text = h
        ph.font.size = Pt(17)
        ph.font.bold = True
        ph.font.color.rgb = TEXT_DARK
        ph.space_after = Pt(12)
        pb = tf.add_paragraph()
        pb.text = b
        pb.font.size = Pt(13)
        pb.font.color.rgb = TEXT_MUTED

    filename = "LionGaze_Saucy_Pitch_Deck-v3.pptx"
    prs.save(filename)
    return filename


pptx_path = generate_pptx_file()

# ==========================================
# MAIN PRODUCT PRESENTATION (Protected Area)
# ==========================================

st.title("🦁 LionGaze (狮视) — Product Presentation")
st.subheader(
    "AI-Powered Road-Mapping & Safety Device for Logistics and Municipal"
    " Infrastructure"
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
            "Pothole cluster detected at GPS [-23.0021, 30.4485]. Fleet broadcast"
            " successful."
        )

else:
    st.markdown("### 🖥️ Interactive Slide Deck Viewer")
    st.write(
        "Browse through the rendered slide cards of your pitch deck below, and"
        " download the complete editable PowerPoint presentation."
    )

    with open(pptx_path, "rb") as f:
        st.download_button(
            label="📥 Download PowerPoint Presentation (.pptx)",
            data=f,
            file_name="LionGaze_Saucy_Pitch_Deck-v3.pptx",
            mime=(
                "application/vnd.openxmlformats-officedocument.presentationml.presentation"
            ),
        )

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
