# Lumetra: A Labour Market Analysis Dashboard for International Organizations

*Data Science meets Unity in Diversity*

A SaaS-style web dashboard for analyzing labour market trends across international organizations — covering job postings, role distributions, and geographic demand patterns across continents and countries.

## Overview

International organizations (UN agencies, NGOs, IGOs) post labour market opportunities across dozens of platforms with no unified way to analyze trends across regions, sectors, or roles. Lumetra aggregates and visualizes this labour market data to surface patterns that are otherwise scattered across individual organizational sites — geographic concentration of demand, role-type trends, and keyword/skill frequency across postings.

This project is framed as a **labour market analysis tool**, not a job board: the goal is descriptive and analytical insight into how international organization labour demand is distributed, not individual job matching.

**Status:** In progress

## Data Sources

| Source | Status | Description |
|---|---|---|
| ReliefWeb API | Access approved | Humanitarian sector job postings and organizational data |
| UN Talent API | Request pending | UN system-wide vacancy data |

*Devex and Idealist were evaluated and found inaccessible for this use case.*

## Methodology

1. **Data ingestion** — pull job posting data from ReliefWeb API (UN Talent API pending approval)
2. **Geographic aggregation** — map postings to continent → country hierarchy for spatial analysis
3. **Role & keyword analysis** — extract and visualize top roles and recurring keywords/skills across postings
4. **Visualization** — interactive Streamlit dashboard with choropleth maps, bar charts, and tag-cloud keyword views

## Dashboard Structure

- **Job Postings** — metric overview, choropleth map of posting density, top roles bar chart, keyword tag cloud, individual posting cards
- **Labour Market Analysis** — *(in progress)*
- **By Role** — *(in progress)*
- **Insights** — *(in progress)*
- **About** — project background and methodology

## Repository Structure

```
├── app.py              # Main Streamlit application
├── analysis/           # Data analysis & keyword extraction logic
├── data/               # Raw and processed labour market data
├── assets/             # Logo and static design assets
└── requirements.txt    # Python dependencies
```

## Tech Stack

**Current:** Python · Streamlit · Plotly (choropleth maps, bar charts)

**Planned:** FastAPI · Docker (for API layer and containerized deployment)

**Deployment:** Streamlit Community Cloud

## About

Dongju — M.Sc. Data Science candidate at Pusan National University, background in International Relations

This project is part of an ongoing portfolio combining data science methods with international organization labour market applications.
