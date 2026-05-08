import requests
import pandas as pd

def fetch_jobs(limit=100):
    url = "https://api.reliefweb.int/v2/jobs"
    payload = {
        "appname": "igo-jobs-dashboard",
        "limit": limit,
        "fields": {
            "include": ["title", "body", "country", "source", "date"]
        },
        "filter": {
            "field": "status",
            "value": "published"
        }
    }

    response = requests.post(url, json=payload)
    data = response.json()

    jobs = []
    for item in data.get("data", []):
        fields = item.get("fields", {})
        country = fields.get("country", [{}])
        source = fields.get("source", [{}])
        jobs.append({
            "title": fields.get("title", ""),
            "body": fields.get("body", ""),
            "country": country[0].get("name", "") if country else "",
            "source": source[0].get("name", "") if source else "",
            "date": fields.get("date", {}).get("created", ""),
        })

    return pd.DataFrame(jobs)

if __name__ == "__main__":
    df = fetch_jobs()
    print(df.shape)
    print(df.head())