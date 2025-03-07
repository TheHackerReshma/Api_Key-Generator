import hashlib
import random
import string
import requests
import re
from bs4 import BeautifulSoup

def generate_api_key():
    """Generates a random API key."""
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    return key

def identify_api_type(api):
    """Identifies the type of API key found based on common patterns."""
    if re.search(r'AIza[0-9A-Za-z-_]{35}', api):
        return "Google API Key"
    elif re.search(r'AKIA[0-9A-Z]{16}', api):
        return "AWS API Key"
    elif re.search(r'sk_live_[0-9a-zA-Z]{24}', api):
        return "Stripe API Key"
    elif re.search(r'(eyJ[a-zA-Z0-9]{10,})', api):
        return "JWT Authentication Token"
    else:
        return "Unknown API Key"

def exploit_info(api_type):
    """Provides a brief explanation of how an API key could be exploited."""
    exploits = {
        "Google API Key": "Can be used to access Google services like Maps, Cloud, and more if improperly secured.",
        "AWS API Key": "Can allow attackers to access AWS resources, potentially leading to data breaches and service abuse.",
        "Stripe API Key": "Could be exploited to make unauthorized financial transactions if exposed.",
        "JWT Authentication Token": "Might allow unauthorized access to user accounts and sensitive data.",
        "Unknown API Key": "Potential risk depends on the service it is associated with. Always validate API exposure."
    }
    return exploits.get(api_type, "No exploitation details available.")

def scan_website_for_apis(url):
    """Scans a website for exposed API keys using regex-based detection."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            api_keys = set()
            
            # Extract scripts and page text
            soup = BeautifulSoup(response.text, 'html.parser')
            scripts = soup.find_all('script')
            text_content = soup.get_text()
            
            # Define regex patterns for common API keys
            patterns = [
                r'AIza[0-9A-Za-z-_]{35}',  # Google API Key
                r'AKIA[0-9A-Z]{16}',  # AWS API Key
                r'sk_live_[0-9a-zA-Z]{24}',  # Stripe API Key
                r'(eyJ[a-zA-Z0-9]{10,})'  # JWT Token
            ]
            
            # Search in scripts and text content
            for pattern in patterns:
                matches = re.findall(pattern, response.text)
                api_keys.update(matches)
            
            return list(api_keys)
        else:
            return []
    except Exception as e:
        print(f"Error scanning website: {e}")
        return []

def main():
    url = input("Enter the website URL: ")
    apis = scan_website_for_apis(url)
    
    if apis:
        print("APIs found:")
        for api in apis:
            api_type = identify_api_type(api)
            print(f"API: {api}")
            print(f"Type: {api_type}")
            print(f"Generated API Key: {generate_api_key()}")
            print(f"Potential Exploit: {exploit_info(api_type)}\n")
    else:
        print("No API keys found on the website.")

if __name__ == "__main__":
    main()

