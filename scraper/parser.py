class JobParser:
    def parse_jobs(self, data, keyword):
        jobs = []

        for item in data:
            if not isinstance(item, dict):
                continue

            if "position" in item and "company" in item:

                jobs.append({
                    "keyword": keyword,
                    "title": item.get("position"),
                    "company": item.get("company"),
                    "location": item.get("location", "Remote"),
                    "tags": item.get("tags", [])
                })

        return jobs