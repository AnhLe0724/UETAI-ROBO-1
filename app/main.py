from scraper import fetch_chotot_data

def main():
    print("Bot Tim Do Gia Re")
    keyword = input("Bạn muốn tìm linh kiện gì: ")
    
    print(f"đang tìm kiếm cho '{keyword}'...")
    results = fetch_chotot_data(keyword)
    
    if not results:
        print("không tìm thấy")
        return

    print(f"đã tìm thấy {len(results)} kết quả. Dưới đây là 10 món đầu tiên:")
    for item in results[:10]:
        name = item.get('subject')
        price = item.get('price_string')
        print(f"- {name} | có giá: {price}")

if __name__ == "__main__":
    main()