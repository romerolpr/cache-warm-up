import requests, random, string
from datetime import datetime

current_date = datetime.now()
current_date_string = current_date.strftime("%Y-%m-%d %H:%M:%S")

def save_results(response, output_file = 'results.txt'):
    with open(output_file, 'a') as file:
        url = response.url
        cf_cache_status = response.headers.get('cf-cache-status')
        result = f'[{current_date_string}] CF CACHE STATUS: {cf_cache_status} => {url}\n'
        file.write(result)
        print(f"OK - {url}")

def handle_header_response(response):
    if response.status_code == 200:
        save_results(response)
    else:
        print("Failed to fetch headers. Status code:", response.status_code)

def fetch(url):
    try:
        response = requests.head(url)
        return response
    except requests.RequestException as e:
        print("Error fetching headers:", e)
        
def generate_url_string_with_query_string(utm_campaign_prefix):
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return utm_campaign_prefix + random_chars

domain = input("Enter the ONLY domain URL (e.g., www.valesaude.com.br): ")
query_string = input("Enter the QUERY STTRING: ")
times = 100

domain = f'https://{domain}/'

for time in range(times):
    if time == 1:
        response = fetch(domain)
        handle_header_response(response)
    else:
        url = generate_url_string_with_query_string(domain + query_string)
        response = fetch(url)
        handle_header_response(response)

print('Finished.')