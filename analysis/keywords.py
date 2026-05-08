import pandas as pd
from collections import Counter
import re

# 분석에서 제외할 불용어
STOPWORDS = {
    "the", "and", "for", "with", "this", "that", "are", "from",
    "will", "have", "been", "their", "they", "other", "such",
    "also", "more", "into", "than", "its", "not", "all", "any",
    "our", "your", "can", "may", "new", "per", "including",
    "ensure", "support", "provide", "work", "working", "within",
    "experience", "required", "relevant", "years", "ability"
}

def clean_text(text):
    """HTML 태그 및 특수문자 제거"""
    text = re.sub(r"<[^>]+>", " ", str(text))
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    return text.lower()

def extract_keywords(df, top_n=30):
    """데이터프레임에서 상위 키워드 추출"""
    if df.empty or "body" not in df.columns:
        return []

    all_words = []
    for text in df["body"].dropna():
        cleaned = clean_text(text)
        words = cleaned.split()
        words = [w for w in words if len(w) > 3 and w not in STOPWORDS]
        all_words.extend(words)

    counter = Counter(all_words)
    return counter.most_common(top_n)

def extract_by_country(df, country_name, top_n=30):
    """특정 국가 채용공고에서 키워드 추출"""
    filtered = df[df["country"].str.lower() == country_name.lower()]
    return extract_keywords(filtered, top_n)

if __name__ == "__main__":
    # 샘플 테스트
    sample = pd.DataFrame({
        "body": ["We need a data analyst with experience in Python and SQL",
                 "Project manager needed with leadership and communication skills"],
        "country": ["Kenya", "Kenya"]
    })
    result = extract_keywords(sample, top_n=10)
    print(result)