import requests
import vars
from datetime import date

session_cookie = vars.session_cookie

year = date.today().year
day = date.today().day

url = f"https://adventofcode.com/{year}/day/{day}/input"

payload = {}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Sec-Fetch-Site': 'none',
  'Cookie': f'session={session_cookie}',
  'Accept-Encoding': 'gzip, deflate, br',
  'Sec-Fetch-Mode': 'navigate',
  'Host': 'adventofcode.com',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
  'Accept-Language': 'en-GB,en;q=0.9',
  'Sec-Fetch-Dest': 'document',
  'Connection': 'keep-alive'
}

response = requests.request("GET", url, headers=headers, data=payload)
# print(f"{year}/day{day:02d}/input.txt")
f = open(f"{year}/day{day:02d}/input.txt", "w")
f.write(response.text)
f.close()


