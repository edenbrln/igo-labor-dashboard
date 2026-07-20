import streamlit as st
import base64
import plotly.graph_objects as go
import pandas as pd
from PIL import Image  # 파비콘 로드를 위해 추가

# 1. assets 폴더의 favicon.png 로드
try:
    favicon = Image.open("assets/favicon-32x32.png")
except FileNotFoundError:
    favicon = "🌍" # 파일이 없을 경우 대비한 백업 아이콘

st.set_page_config(
    page_title="Lumetra",
    page_icon=favicon,
    layout="wide"
)

def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""

# 로고 및 푸터 이미지 로드
logo_base64 = get_image_base64("assets/image_1.png")
footer_logo_base64 = get_image_base64("assets/image_2.png")


st.markdown("""
<style>
    .block-container {
    padding-top: 2rem !important;
}
    [data-testid="stSidebar"] {
        background-color: #012235;
    }
    [data-testid="stSidebarContent"] * {
        color: white;
    }
    [data-testid="stSidebar"] .stButton button {
        background-color: #012235 !important;
        color: white !important;
        border: none !important;
        text-align: left !important;
        width: 100% !important;
        padding: 4px 8px !important;
    }
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #185fa5 !important;
        color: white !important;
    }
    [data-testid="stSidebar"] .stButton button p {
        font-size: 14.5px !important;
        text-align: left !important;
    }
            
    [data-testid="stSidebar"] .streamlit-expanderHeader {
        background-color: #012235 !important;
        color: white !important;
    }
    [data-testid="stSidebar"] .streamlit-expanderContent {
        background-color: #012235 !important;
    }
    [data-testid="stSidebar"] details {
        background-color: #012235 !important;
    }
    [data-testid="stSidebar"] details summary {
        background-color: #012235 !important;
        color: white !important;
    }
    [data-testid="stSidebar"] details[open] {
        background-color: #012235 !important;
    }
    .metric-card {
        background: white;
        border: 0.5px solid #e8edf3;
        border-radius: 12px;
        padding: 16px 20px;
        text-align: center;
    }
    .metric-label {
        font-size: 12px;
        color: #7a9ab5;
        font-weight: 500;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .metric-value {
        font-size: 28px;
        font-weight: 600;
        color: #0d2137;
    }
    .metric-delta {
        font-size: 11px;
        color: #1d9e75;
        margin-top: 4px;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 56px;
        background: white;
        border-top: 0.5px solid #e8edf3;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 32px;
        z-index: 999;
    }
    .footer-logo {
        width: 28px;
        height: 28px;
        flex-shrink: 0;
    }
    .footer-brand {
        font-size: 13px;
        font-weight: 700;
        color: #0d2137;
        letter-spacing: 0.12em;
    }
    .footer-icon a {
        color: #7a9ab5;
        text-decoration: none;
        font-size: 12px;
        font-weight: 500;
        letter-spacing: 0.04em;
        transition: color 0.2s;
    }
    .footer-icon a:hover {
        color: #185fa5;
    }
    .support-btn {
        background: #185fa5;
        color: white !important;
        font-size: 12px;
        font-weight: 600;
        padding: 6px 14px;
        border-radius: 20px;
        text-decoration: none !important;

        display: flex;
        align-items: center;
        gap: 6px;
        white-space: nowrap;
        transition: background 0.2s;
    }
    .support-btn:hover {
        background: #0c447c;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown(f"""
<div style="display:flex; align-items:center; gap:10px; padding:8px 0 16px 0; border-bottom: 0.5px solid rgba(255,255,255,0.1);">
    <img src="data:image/png;base64,{logo_base64}" style="width:160px;">
    <div style="color:#7a9ab5; font-size:11px; font-style:italic; line-height:1.6;">
        Illuminating Global<br>Labour Markets with Data
    </div>
</div>
""", unsafe_allow_html=True)

REGIONS = {
    "Africa": ["Ethiopia", "Kenya", "Nigeria", "Somalia", "Sudan"],
    "Asia": ["Afghanistan", "Bangladesh", "Indonesia", "Jordan", "Myanmar", "South Korea"],
    "Americas": ["Brazil", "Colombia", "Haiti", "Mexico"],
    "Europe": ["France", "Germany", "Switzerland", "Ukraine", "United Kingdom"],
    "Middle East": ["Iraq", "Lebanon", "Syria", "Yemen"],
    "Oceania": ["Australia", "Papua New Guinea"],
}

COUNTRY_COUNTS = {
    "Ethiopia": 98, "Kenya": 142, "Nigeria": 31, "Somalia": 67, "Sudan": 54,
    "Afghanistan": 87, "Bangladesh": 23, "Indonesia": 19, "Jordan": 61, "Myanmar": 44, "South Korea": 23,
    "Brazil": 29, "Colombia": 18, "Haiti": 42, "Mexico": 15,
    "France": 38, "Germany": 45, "Switzerland": 72, "Ukraine": 44, "United Kingdom": 56,
    "Iraq": 38, "Lebanon": 51, "Syria": 89, "Yemen": 76,
    "Australia": 12, "Papua New Guinea": 8,
}


st.sidebar.markdown("""
<div style="display:flex; align-items:center; justify-content:space-between; padding:12px 0 8px 0; border-bottom:0.5px solid rgba(255,255,255,0.1); margin-bottom:8px;">
    <span style="font-size:14px; font-weight:600; color:#7a9ab5; letter-spacing:0.08em; text-transform:uppercase;">Location</span>
    <span style="font-size:14px; background:rgba(55,138,221,0.2); color:#378add; padding:2px 8px; border-radius:10px; font-weight:500;">Global</span>
</div>
""", unsafe_allow_html=True)

for region, countries in REGIONS.items():
    with st.sidebar.expander(region):
        for c in countries:
            count = COUNTRY_COUNTS.get(c, 0)
            col_btn, col_badge = st.columns([4, 1])
            with col_btn:
                if st.button(c, key=c, use_container_width=True):
                    st.session_state["selected_country"] = c
            with col_badge:
                st.markdown(f"""
                <div style="display:flex; align-items:center; height:100%; padding-top:4px;">
                    <span style="font-size:10px; background:rgba(55,138,221,0.25); color:#378add; padding:1px 7px; border-radius:10px; font-weight:600;">{count}</span>
                </div>
                """, unsafe_allow_html=True)

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
    sample_map_data = pd.DataFrame({
        "country": ["Kenya", "Ethiopia", "Somalia", "Sudan", "South Korea", "Germany", "France", "Brazil", "Jordan", "Ukraine"],
        "count": [142, 98, 67, 54, 23, 45, 38, 29, 61, 44],
        "top_role": ["Field Officer", "Health Officer", "Logistics", "Education", "Data Analyst", "Program Manager", "Communications", "Field Officer", "Protection Officer", "Logistics"]
    })

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<div class="metric-card"><div class="metric-label">Total Postings</div><div class="metric-value">605</div><div class="metric-delta">↑ 12% this month</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="metric-card"><div class="metric-label">Organizations</div><div class="metric-value">38</div><div class="metric-delta">↑ 3 new</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="metric-card"><div class="metric-label">Countries</div><div class="metric-value">10</div><div class="metric-delta">Across 5 regions</div></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<div class="metric-card"><div class="metric-label">New This Week</div><div class="metric-value">47</div><div class="metric-delta">↑ 8% vs last week</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    fig_map = go.Figure(go.Choropleth(
        locations=sample_map_data["country"],
        locationmode="country names",
        z=sample_map_data["count"],
        text=sample_map_data["top_role"],
        colorscale=[[0, "#e6f1fb"], [0.3, "#378add"], [1, "#0c447c"]],
        hovertemplate="<b>%{location}</b><br>Postings: %{z}<br>Top Role: %{text}<extra></extra>",
        colorbar=dict(
            title=dict(text="Postings", font=dict(size=11, color="#7a9ab5")),
            thickness=8, len=0.4, x=1.01,
            bgcolor="rgba(0,0,0,0)", borderwidth=0,
            tickfont=dict(size=10, color="#7a9ab5"),
        ),
        marker_line_color="#ffffff",
        marker_line_width=0.8,
    ))
    fig_map.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        paper_bgcolor="#f4f6fb",
        geo=dict(
            showframe=False, showcoastlines=True, coastlinecolor="#d0dce8",
            showland=True, landcolor="#f0f3f7",
            showocean=True, oceancolor="#ddeef7",
            showlakes=False, showcountries=True, countrycolor="#d0dce8",
            bgcolor="#f4f6fb", projection_type="natural earth",
            lonaxis=dict(range=[-150, 160]), lataxis=dict(range=[-55, 80]),
        ),
        height=310,
    )
    st.plotly_chart(fig_map, use_container_width=True)

    st.divider()

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("#### Top Hiring Roles")
        roles_data = pd.DataFrame({
            "Role": ["Field Officer", "Health Officer", "Data Analyst", "Program Manager", "Logistics"],
            "Count": [89, 77, 64, 57, 41]
        })
        fig_bar = go.Figure(go.Bar(
            x=roles_data["Count"], y=roles_data["Role"],
            orientation="h",
            marker=dict(color=roles_data["Count"], colorscale=[[0, "#b5d4f4"], [1, "#0c447c"]]),
            width=0.4,
        ))
        fig_bar.update_layout(
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            plot_bgcolor="white", paper_bgcolor="white", height=260,
            yaxis={"categoryorder": "total ascending"},
            xaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_right:
        st.markdown("#### Keyword Cloud")
        word_freq = {
            "data": 89, "health": 77, "program": 64,
            "management": 57, "community": 49, "monitoring": 41,
            "field": 34, "reporting": 28, "nutrition": 22,
            "logistics": 18, "education": 15, "policy": 12
        }
        max_count = max(word_freq.values())

        def get_style(count):
            ratio = count / max_count
            if ratio > 0.8:
                return "font-size:22px; background:#185fa5; color:#fff;"
            elif ratio > 0.6:
                return "font-size:18px; background:#378add; color:#fff;"
            elif ratio > 0.4:
                return "font-size:15px; background:#b5d4f4; color:#0c447c;"
            else:
                return "font-size:13px; background:#e6f1fb; color:#185fa5;"

        tags_html = "".join([
            f'<span style="display:inline-block; margin:4px; padding:5px 12px; border-radius:20px; font-weight:500; {get_style(count)}">{word}</span>'
            for word, count in sorted(word_freq.items(), key=lambda x: -x[1])
        ])
        st.markdown(f"""
        <div style="background:white; border:0.5px solid #e0e0e0; border-radius:12px; padding:16px; min-height:200px;">
            {tags_html}
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.markdown("#### Latest Job Postings")
    jobs = [
        {"title": "Data Analyst", "org": "UNHCR", "country": "Kenya", "posted": "2026-05-06", "url": "https://reliefweb.int"},
        {"title": "Health Officer", "org": "WHO", "country": "Ethiopia", "posted": "2026-05-05", "url": "https://reliefweb.int"},
        {"title": "M&E Specialist", "org": "UNDP", "country": "Kenya", "posted": "2026-05-04", "url": "https://reliefweb.int"},
        {"title": "Field Coordinator", "org": "WFP", "country": "Somalia", "posted": "2026-05-03", "url": "https://reliefweb.int"},
        {"title": "Logistics Officer", "org": "UNICEF", "country": "Sudan", "posted": "2026-05-02", "url": "https://reliefweb.int"},
    ]
    for job in jobs:
        st.markdown(f"""
        <div style="background:white; border:0.5px solid #e8edf3; border-radius:12px; padding:16px 20px; margin-bottom:10px; display:flex; align-items:center; justify-content:space-between;">
            <div>
                <div style="font-size:15px; font-weight:600; color:#0d2137;">{job['title']}</div>
                <div style="font-size:12px; color:#7a9ab5; margin-top:4px;">{job['org']} &nbsp;·&nbsp; {job['country']} &nbsp;·&nbsp; Posted {job['posted']}</div>
            </div>
            <a href="{job['url']}" target="_blank" style="background:#185fa5; color:white; font-size:12px; font-weight:500; padding:8px 16px; border-radius:20px; text-decoration:none; white-space:nowrap;">View Posting →</a>
        </div>
        """, unsafe_allow_html=True)



with tab2:
    import plotly.graph_objects as go
    import plotly.express as px
    import pandas as pd

    st.markdown(f"### Labour Market Analysis — {country}")
    st.divider()

    # 상단 요약 지표
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Top Keyword</div>
            <div class="metric-value" style="font-size:20px; margin-top:4px;">data</div>
            <div class="metric-delta">↑ 23% vs last month</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Top Role</div>
            <div class="metric-value" style="font-size:18px; margin-top:4px;">Field Officer</div>
            <div class="metric-delta">89 postings</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Top Organization</div>
            <div class="metric-value" style="font-size:18px; margin-top:4px;">UNHCR</div>
            <div class="metric-delta">38 postings</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Avg. Postings/Month</div>
            <div class="metric-value">24</div>
            <div class="metric-delta">↑ 8% growth</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 키워드 트렌드 바차트
    st.markdown("#### Top Demand Keywords")
    keywords_data = pd.DataFrame({
        "Keyword": ["data", "health", "program", "management", "community", "monitoring", "field", "reporting", "nutrition", "logistics"],
        "Count": [89, 77, 64, 57, 49, 41, 34, 28, 22, 18]
    })
    fig_kw = go.Figure(go.Bar(
        x=keywords_data["Keyword"],
        y=keywords_data["Count"],
        marker=dict(
            color=keywords_data["Count"],
            colorscale=[[0, "#b5d4f4"], [1, "#0c447c"]],
        ),
    ))
    fig_kw.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=260,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
    )
    st.plotly_chart(fig_kw, use_container_width=True)

    st.divider()

    # 파이차트 + 기관별 바차트
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("#### Job Sector Distribution")
        sector_data = pd.DataFrame({
            "Sector": ["Health", "Education", "Logistics", "Data & Analytics", "Field Operations", "Communications"],
            "Count": [142, 98, 76, 64, 54, 38]
        })
        fig_pie = px.pie(
            sector_data,
            names="Sector",
            values="Count",
            color_discrete_sequence=["#0c447c", "#185fa5", "#378add", "#85b7eb", "#b5d4f4", "#e6f1fb"],
            hole=0.4,
        )
        fig_pie.update_layout(
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            paper_bgcolor="white",
            height=280,
            legend=dict(font=dict(size=11), orientation="v"),
        )
        fig_pie.update_traces(textinfo="percent", textfont_size=11)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_right:
        st.markdown("#### Top Hiring Organizations")
        org_data = pd.DataFrame({
            "Organization": ["UNHCR", "WFP", "UNICEF", "WHO", "UNDP", "IOM"],
            "Count": [98, 87, 76, 65, 54, 43]
        })
        fig_org = go.Figure(go.Bar(
            x=org_data["Count"],
            y=org_data["Organization"],
            orientation="h",
            marker=dict(
                color=org_data["Count"],
                colorscale=[[0, "#b5d4f4"], [1, "#0c447c"]],
            ),
            width=0.4,
        ))
        fig_org.update_layout(
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            plot_bgcolor="white",
            paper_bgcolor="white",
            height=280,
            yaxis={"categoryorder": "total ascending"},
            xaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
        )
        st.plotly_chart(fig_org, use_container_width=True)

    st.divider()

    # 월별 트렌드 라인차트
    st.markdown("#### Monthly Posting Trend")
    trend_data = pd.DataFrame({
        "Month": ["Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May"],
        "Postings": [54, 61, 48, 72, 89, 95, 105]
    })
    fig_trend = go.Figure(go.Scatter(
        x=trend_data["Month"],
        y=trend_data["Postings"],
        mode="lines+markers",
        line=dict(color="#185fa5", width=2.5),
        marker=dict(color="#185fa5", size=7),
        fill="tozeroy",
        fillcolor="rgba(55,138,221,0.08)",
    ))
    fig_trend.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=220,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
    )
    st.plotly_chart(fig_trend, use_container_width=True)



with tab3:
    st.write(f"By Role - {country}")



with tab4:
    st.write("Insights - 준비 중")



with tab5:
    st.write("About - 준비 중")




# Footer
st.markdown(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<div class="footer">
    <div style="display:flex; align-items:center; gap:10px;">
        <img src="data:image/png;base64,{footer_logo_base64}" class="footer-logo">
        <span class="footer-brand">LUMETRA</span>
        <span style="color:#e8edf3; margin:0 12px;">|</span>
        <div style="display:flex; flex-direction:column; gap:3px;">
            <span style="font-size:10x; color:#7a9ab5; ">Data Science meets Unity in Diversity</span>
            <span style="font-size:10px; color:#b5c9d8; letter-spacing:0.03em;">Engineered by <span style="color:#b5c9d8; font-weight:600;">Dongju Park</span></span>
        </div>
    </div>
    <div style="display:flex; align-items:center; gap:20px;">
        <div class="footer-icon"><a href="https://github.com/edenbrln" target="_blank">GitHub</a></div>
        <div class="footer-icon"><a href="https://linkedin.com" target="_blank">LinkedIn</a></div>
        <div class="footer-icon"><a href="mailto:dongjupark.kr@gmail.com">Email</a></div>
        <a href="https://www.buymeacoffee.com" target="_blank" class="support-btn">
            <i class="fa-solid fa-mug-hot"></i> Support Me
        </a>
    </div>
</div>
""", unsafe_allow_html=True)