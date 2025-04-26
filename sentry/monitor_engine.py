import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Fungsi untuk mengambil konten berita dari sebuah URL
def fetch_news(url):
    try:
        headers = {'User-Agent': 'SentinelGaruda/1.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Memastikan request sukses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news from {url}: {e}")
        return None

# Fungsi untuk menganalisis berita dan mencari kata kunci tertentu
def analyze_news(content, keywords):
    soup = BeautifulSoup(content, 'html.parser')
    titles = soup.find_all('h1')  # Misalnya, ambil semua tag <h1> yang umumnya berisi judul berita
    relevant_titles = []

    for title in titles:
        if any(keyword.lower() in title.text.lower() for keyword in keywords):
            relevant_titles.append(title.text.strip())

    return relevant_titles

# Fungsi utama untuk memantau berita
def monitor_news(keywords, urls):
    monitored_data = []
    
    while True:
        print(f"Monitoring started at {datetime.now()}")

        # Memantau setiap URL
        for url in urls:
            print(f"Checking {url}")
            content = fetch_news(url)
            if content:
                relevant_titles = analyze_news(content, keywords)
                if relevant_titles:
                    print(f"Found relevant news at {url}:")
                    for title in relevant_titles:
                        print(f"- {title}")
                    monitored_data.append({'url': url, 'found_titles': relevant_titles, 'timestamp': datetime.now()})
                else:
                    print(f"No relevant news found at {url}.")
            time.sleep(5)  # Delay untuk menghindari request terlalu cepat
        
        print("Monitoring paused for 60 seconds.")
        time.sleep(60)  # Jeda selama 60 detik sebelum memulai pemantauan berikutnya

# Daftar URL yang ingin dipantau
urls_to_monitor = [
    "https://www.example-news-site.com",
    "https://www.another-news-site.com"
]

# Daftar kata kunci yang digunakan untuk mendeteksi disinformasi
keywords_to_search = ["palsu", "hoaks", "berita bohong", "propaganda"]

# Mulai proses pemantauan
if __name__ == "__main__":
    monitor_news(keywords_to_search, urls_to_monitor)
  
