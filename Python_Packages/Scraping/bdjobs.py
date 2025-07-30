# Problem 2: Job Postings from Indeed
# Site: https://www.indeed.com

# Goal: Scrape job titles, companies, locations, and salaries (if available) for “Data Analyst” jobs in New York.

# Note: Might require handling pagination and headers.

response = requests.get("https://bdjobs.com/")


soup = BeautifulSoup(response.content,"html.parser")
print(soup.prettify())