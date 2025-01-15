from ip_net_vision import WebScraper

def main():
    try:
        site = WebScraper("https://whatismyipaddress.com/")
        ip_details = site.fetch_ip_details()
        print("Public IP Information:")
        for key, value in ip_details.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
