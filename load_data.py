import requests

def fetch_tenders():
    url = "https://public.api.openprocurement.org/api/0/tenders"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Завантажено {len(data['data'])} тендерів")
    else:
        print("Помилка завантаження")

if __name__ == "__main__":
    fetch_tenders()