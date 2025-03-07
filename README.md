# API Key Generator & Scanner

A Python tool to scan websites for exposed API keys and generate test keys.

## Features
- Scan websites for exposed API keys
- Identify API key types (Google, AWS, Stripe, JWT, etc.)
- Generate random API keys for testing
- Provide exploitation risk details

## Installation
### Prerequisites
Ensure you have Python 3.x installed. If not, download it from [Python.org](https://www.python.org/).

### Install Dependencies
Run the following command to install required packages:
```bash
pip install requests beautifulsoup4
```

## Usage
### Run the Script
```bash
python api_scanner.py
```
or  
```bash
python3 api_scanner.py
```

### Enter a Website URL
The script will prompt you:
```
Enter the website URL: https://example.com
```
It will scan the site and display API keys (if found).

## Example Output
```
Enter the website URL: https://example.com

APIs found:
API: AIzaSyD1s2E3f4G5h6J7K8L9M0N1P2Q3R4S5T6
Type: Google API Key
Generated API Key: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
Potential Exploit: Can be used to access Google services like Maps, Cloud, and more if improperly secured.
```
If no API keys are found:
```
No API keys found on the website.
```

## Supported API Key Types
- Google API Keys (`AIza...`)
- AWS API Keys (`AKIA...`)
- Stripe API Keys (`sk_live_...`)
- JWT Tokens (`eyJ...`)
- More can be added easily!

## How It Works
1. The script fetches the website’s HTML source code.
2. Uses Regular Expressions (Regex) to scan for API keys.
3. Identifies the type of API key.
4. Generates random test API keys.
5. Shows potential security risks for exposed keys.

## Disclaimer
- This tool is intended for **educational and security testing purposes only**.
- Do **not** use it on websites without permission.
- The developer is **not responsible** for any misuse.

## License
This project is licensed under the **MIT License**. Feel free to modify and use it!

## Contributing
Want to improve this tool? Fork the repo and submit a PR!

