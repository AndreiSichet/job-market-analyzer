from scraper.fetcher import JobFetcher
from scraper.parser import JobParser
import pandas as pd


def main():
    fetcher = JobFetcher()
    parser = JobParser()

    keywords = [
        "software engineer",
        "data engineer",
        "AI engineer",
        "ML engineer"
    ]

    all_jobs = []

    data = fetcher.fetch_jobs()

    for keyword in keywords:
        jobs = parser.parse_jobs(data, keyword)
        all_jobs.extend(jobs)

    df = pd.DataFrame(all_jobs)

    df.to_csv("data/jobs.csv", index=False)

    print(f"[INFO] Total jobs scraped: {len(all_jobs)}")


if __name__ == "__main__":
    main()
