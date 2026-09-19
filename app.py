import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LionGaze Product Presentation", page_icon="🦁", layout="wide"
)


def check_password():
  """Returns True if the user enters the correct password/PIN."""

  def password_entered():
    # Retrieves password from st.secrets, falls back to your project PIN "9452" if not configured
    correct_password = st.secrets.get("app_password", "9452")
    if st.session_state["password_input"] == correct_password:
      st.session_state["password_correct"] = True
      del st.session_state["password_input"]  # Clean up state
    else:
      st.session_state["password_correct"] = False

  # First run or incorrect state
  if "password_correct" not in st.session_state:
    st.markdown("### 🔐 Restricted Access")
    st.text_input(
        "Enter Access PIN / Password:",
        type="password",
        on_change=password_entered,
        key="password_input",
    )
    return False
  elif not st.session_state["password_correct"]:
    st.markdown("### 🔐 Restricted Access")
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


# Run the authentication check before showing the product
if not check_password():
  st.stop()

# ==========================================
# MAIN PRODUCT PRESENTATION (Protected Area)
# ==========================================

st.title("🦁 LionGaze (狮视) — Product Presentation")
st.subheader(
    "AI-Powered Road-Mapping & Safety Device for Logistics and Municipal"
    " Infrastructure"
)

st.markdown("---")

# Metrics or Quick Overview
col1, col2, col3 = st.columns(3)
with col1:
  st.metric("Development Stage", "R&D / Working Prototype")
with col2:
  st.metric("Hardware Stack", "Raspberry Pi 4B + IMU")
with col3:
  st.metric("Target Market", "Logistics & Municipalities")

st.markdown("### 🚀 Executive Summary")
st.write(
    "LionGaze maps road potholes using an onboard camera and electronic"
    " sensors, capturing exact geolocated coordinates to construct dynamic"
    " road profiles. Data is edge-preprocessed and synchronized with the cloud"
    " to give following vehicle fleets instant hazard warnings and provide"
    " municipalities with data-driven repair insights."
)

st.markdown("### 📊 Live System Status / Demo")
st.info("System operational. Edge sensor node connected.")

# Add your charts, maps, or interactive components below
if st.button("Run Simulation Check"):
  st.success(
      "Pothole cluster detected at GPS [-23.0021, 30.4485]. Fleet broadcast"
      " successful."
  )
