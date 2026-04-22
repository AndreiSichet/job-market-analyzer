from collections import Counter
def extract_top_skills(df):
    all_skills = []
    for tags in df["tags"]:
        if isinstance(tags, list):
            all_skills.extend(tags)
    return Counter(all_skills).most_common(10)

def jobs_by_role(df):
    return df["keyword"].value_counts()