import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Phone Number Reuse Detector", page_icon="📱")

st.title("📱 Phone Number Reuse Detector")
st.caption("Check if a phone number has been recycled in India")

st.markdown("---")

# Input
phone = st.text_input("Enter Phone Number", placeholder="9876543210", max_chars=10)

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Check Number", use_container_width=True):
        if phone:
            with st.spinner("Checking..."):
                try:
                    res = requests.post(f"{API_URL}/check", json={"phone": phone})
                    data = res.json()
                    
                    if data["status"] == "recycled":
                        st.error(f"⚠️ RECYCLED NUMBER DETECTED")
                        st.markdown(f"**Recycled Date:** {data['recycled_date']}")
                        st.markdown(f"**Old User:** {data['old_user']}")
                        st.markdown(f"**Reason:** {data['reason']}")
                        
                        # Risk level color
                        risk = data["risk_level"]
                        if risk == "CRITICAL":
                            st.error(f"🚨 Risk Level: {risk}")
                        elif risk == "HIGH":
                            st.warning(f"⚠️ Risk Level: {risk}")
                        else:
                            st.info(f"ℹ️ Risk Level: {risk}")
                        
                        st.markdown("### 🚨 Expected Alerts:")
                        for alert in data["alerts"]:
                            st.markdown(f"- {alert}")
                        
                        st.markdown("### 💡 Advice:")
                        for advice in data["advice"]:
                            st.markdown(f"- {advice}")
                    
                    elif data["status"] == "clean":
                        st.success(f"✅ {data['message']}")
                        st.info(f"Risk Level: {data['risk_level']}")
                    
                    else:
                        st.warning(data["message"])
                
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a phone number")

with col2:
    if st.button("📢 Report Issue", use_container_width=True):
        if phone:
            issue = st.selectbox("Select Issue Type", [
                "Receiving loan recovery calls",
                "Receiving unknown OTPs",
                "Old user WhatsApp verification",
                "Receiving bank SMS",
                "Other issue"
            ])
            res = requests.post(f"{API_URL}/report", json={"phone": phone, "issue": issue})
            data = res.json()
            st.success(f"Report ID: {data['report_id']}")
            st.info(data["message"])

st.markdown("---")
st.caption("Demo: Try 9876543210, 8765432109, 7654321098")