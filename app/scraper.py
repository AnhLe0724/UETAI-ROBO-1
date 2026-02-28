import requests

def fetch_chotot_data(keyword):
    # API của ChoTot - ta lấy 20 kết quả đầu tiên
    url = f"https://gateway.chotot.com/v1/public/ad-listing?q={keyword}&limit=20"
    
    # Header giả lập trình duyệt để không bị chặn
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get('ads', [])
        return []
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
        return []