import requests


class JobFetcher:
    def __init__(self):
        self.url = "https://remoteok.com/api"

    def fetch_jobs(self):
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(self.url, headers=headers)

        if response.status_code == 200:
            return response.json()

        print("[ERROR] Failed request")
        return []