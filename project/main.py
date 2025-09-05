from fastapi import FastAPI # type: ignore
import requests  # type: ignore

app = FastAPI()


NEWS_API_KEY = "4921d161130f4f948360ee2e4b75bb4e"  
NEWS_URL = "https://newsapi.org/v2/top-headlines"


@app.get("/tech-news")
def get_tech_news():
    """Fetch latest technology news"""
    params = {
        "category": "technology",
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_URL, params=params)
    data = response.json()

    if data["status"] == "ok":
        news_list = []
        for article in data["articles"]:
            news_list.append({
                "title": article["title"],
                "description": article["description"],
                "source": article["source"]["name"],
                "url": article["url"]
            })
        return {"status": "success", "articles": news_list}
    else:
        return {"status": "error", "message": data}



JOBS_API_URL = "https://jsearch.p.rapidapi.com/search"
JOBS_API_HEADERS = {
    "x-rapidapi-host": "jsearch.p.rapidapi.com",
    "x-rapidapi-key": "50844c9e5dmsh610c2464f3f06f4p1c1836jsnaf8efdf0ebac"  
}


@app.get("/tech-jobs")
def get_tech_jobs():
    """Fetch latest tech job postings"""
    querystring = {"query": "software engineer OR python developer OR data scientist", "page": "1", "num_pages": "1"}
    response = requests.get(JOBS_API_URL, headers=JOBS_API_HEADERS, params=querystring)
    data = response.json()

    if "data" in data:
        job_list = []
        for job in data["data"][:5]:  
            job_list.append({
                "title": job["job_title"],
                "company": job["employer_name"],
                "location": job["job_city"],
                "url": job["job_apply_link"]
            })
        return {"status": "success", "jobs": job_list}
    else:
        return {"status": "error", "message": data}
