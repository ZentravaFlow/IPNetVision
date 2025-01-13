import cloudscraper
from bs4 import BeautifulSoup

def fetch_ip_details():
    scraper = cloudscraper.create_scraper()
    
    response = scraper.get("https://whatismyipaddress.com/")
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    ipv4 = soup.find("span", id="ipv4")
    ipv4 = ipv4.text.strip() if ipv4 else "Not found"
    
    ipv6 = soup.find("span", id="ipv6")
    ipv6 = ipv6.text.strip() if ipv6 else "Not found"
    
    if ipv6 == "Checking...":
        ipv6 = "Not detected"
    
    ip_info = {}
    info_elements = soup.find_all("p", class_="information")
    
    for element in info_elements:
        label = element.find("span").text.strip().rstrip(":")
        value = element.find_all("span")[1].text.strip()
        ip_info[label] = value
    
    return {
        "IPv4": ipv4,
        "IPv6": ipv6,
        "ISP": ip_info.get("ISP", "Not found"),
        "Services": ip_info.get("Services", "Not found"),
        "Country": ip_info.get("Country", "Not found"),
        "Region": ip_info.get("Region", "Not found"),
        "City": ip_info.get("City", "Not found")
    }

def main():
    try:
        ip_details = fetch_ip_details()
        
        print("Public IP Information:")
        for key, value in ip_details.items():
            print(f"{key}: {value}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
