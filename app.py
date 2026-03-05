import streamlit as st
import folium
from streamlit.components.v1 import html

st.set_page_config(page_title="AI Travel Planner", layout="centered")

st.title("🎒 AI Travel Planner for Students")
st.write("Plan your trip within your budget easily!")

# User Inputs
destination = st.text_input("Enter Destination (e.g., Goa, Manali)")
budget = st.number_input("Enter Budget (₹)", min_value=1000, value=10000)
days = st.number_input("Number of Days", min_value=1, max_value=30, value=3)

if st.button("Generate Travel Plan"):
    
    st.subheader("📍 Your Personalized Travel Plan")
    
    daily_budget = budget // days
    
    for i in range(1, int(days)+1):
        st.write(f"### Day {i}")
        st.write(f"- Visit popular attractions in {destination}")
        st.write(f"- Try local street food and authentic cuisine")
        st.write(f"- Explore markets and cultural spots")
        st.write(f"- Budget-friendly activities and sightseeing")
        st.write(f"**Estimated daily budget: ₹{daily_budget}**")
        st.write("---")
    
    st.success(f"✅ Trip planned successfully within ₹{budget} budget! 🎉")
    
    # Budget Breakdown
    st.subheader("💰 Budget Breakdown")
    accommodation = budget * 0.40
    food = budget * 0.30
    activities = budget * 0.20
    transport = budget * 0.10
    
    st.write(f"- 🏨 Accommodation: ₹{accommodation:.0f} (40%)")
    st.write(f"- 🍽️ Food: ₹{food:.0f} (30%)")
    st.write(f"- 🎭 Activities: ₹{activities:.0f} (20%)")
    st.write(f"- 🚗 Local Transport: ₹{transport:.0f} (10%)")
    
    # Map Display
    st.subheader("🗺️ Location Map")
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    folium.Marker([20.5937, 78.9629], popup=destination, tooltip=destination).add_to(m)
    html(m._repr_html_(), height=400)

st.info("💡 Tip: Adjust your budget and days to get different travel plans!")
