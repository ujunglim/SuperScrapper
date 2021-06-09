import requests
from bs4 import BeautifulSoup

 # get number of last page 
def get_last_page(url):
  result = requests.get(url) # get result from request
  soup = BeautifulSoup(result.text, 'html.parser') # get text of result
  # find all anchor pages
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  last_page = int(pages[-2].get_text(strip=True)) 
  return last_page

# extract details of a job
def extract_job(html):
  job_title = html.find("h2", {"class": "mb4"}).find("a")["title"]
  company, location = html.find("h3", {
      "class": "fc-black-700"
  }).find_all("span", recursive=False)  # recursive prevents go deep
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id = html["data-jobid"]
  return {
    'title': job_title,
    'company': company,
    'location': location,
    'link': f"https://stackoverflow.com/jobs/{job_id}"
  }

# extract list of jobs
def extract_jobs(last_page, url):
  jobs = []
  # get data of each page
  for page in range(last_page):
    print(f"Scrapping so_page {page+1}")
    result = requests.get(f"{url}&pg={page+1}") 
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_job(result) # get detail of each job
      jobs.append(job) # push to jobs list
  return jobs

# get list of jobs by word
def get_jobs(word):
  url = f"https://stackoverflow.com/jobs?q={word}&pg=2"
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs
