import streamlit as st
import base64

st.set_page_config(
    page_title="Lumetra",
    page_icon="🌍",
    layout="wide"
)

# 로고 이미지 base64 변환
def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_image_base64("assets/image_1.png")

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #0d2137;
    }
    [data-testid="stSidebarContent"] * {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown(f"""
<div style="display:flex; align-items:center; gap:10px; padding:8px 0 16px 0; border-bottom: 0.5px solid rgba(255,255,255,0.1);">
    <img src="data:image/png;base64,{logo_base64}" style="width:130px;">
    <div style="color:#7a9ab5; font-size:11px; font-style:italic; line-height:1.6;">
        Illuminating Global<br>Labour Markets with Data
    </div>
</div>
""", unsafe_allow_html=True)

# 대륙 → 국가 계층형 메뉴
REGIONS = {
    "Africa": ["Ethiopia", "Kenya", "Nigeria", "Somalia", "Sudan"],
    "Asia": ["Afghanistan", "Bangladesh", "Indonesia", "Jordan", "Myanmar", "South Korea"],
    "Americas": ["Brazil", "Colombia", "Haiti", "Mexico"],
    "Europe": ["France", "Germany", "Switzerland", "Ukraine", "United Kingdom"],
    "Middle East": ["Iraq", "Lebanon", "Syria", "Yemen"],
    "Oceania": ["Australia", "Papua New Guinea"],
}

st.sidebar.markdown("### 🔍 Select Region & Country")

for region, countries in REGIONS.items():
    with st.sidebar.expander(region):
        for country in countries:
            if st.button(country, key=country):
                st.session_state["selected_country"] = country

country = st.session_state.get("selected_country", "Global")

# 탭 구성
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Job Postings",
    "Labour Market Analysis",
    "By Role",
    "Insights",
    "About"
])

with tab1:
    st.write(f"Job Postings - {country}")

with tab2:
    st.write(f"Labour Market Analysis - {country}")

with tab3:
    st.write(f"By Role - {country}")

with tab4:
    st.write("Insights - 준비 중")

with tab5:
    st.write("About - 준비 중")