# Api_Key-Generator
An API Key Generator is a tool that creates unique authentication keys used to access APIs securely. These keys help control access to a service and prevent unauthorized use.

My API Key Generator script scans a website for API keys and also generates random API keys for testing.
How to Run the API Key Generator in Python
1. Ensure Dependencies Are Installed
Your script requires:

requests → For making web requests.
beautifulsoup4 → For parsing website content.
re (Regex) → For pattern matching.
Install them using:

bash
Copy
Edit
pip install requests beautifulsoup4
2. Navigate to the Script Location
If your script is in WSL (Kali Linux), move to its directory:
cd /home/your-username/
Or in Windows (CMD/PowerShell):

powershell
Copy
Edit
cd C:\Users\yourname\Desktop
3. Run the Python Script
Run the script using:

bash
Copy
Edit
python api_scanner.py
Or if using Python 3:

bash
Copy
Edit
python3 api_scanner.py
4. Enter a Website URL
The script will ask for a website URL:

mathematica
Copy
Edit
Enter the website URL: https://example.com
It will then scan for exposed API keys and display results.

Example Output
yaml

Enter the website URL: https://example.com
APIs found:
API: AIzaSyD1s2E3f4G5h6J7K8L9M0N1P2Q3R4S5T6
Type: Google API Key
Generated API Key: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
Potential Exploit: Can be used to access Google services like Maps, Cloud, and more if improperly secured.
Alternative: Running in WSL

If your script is in WSL (Kali Linux) but you want to run it in Windows, copy the file first:
bash:
cp api_scanner.py /mnt/c/Users/yourname/Desktop/

Then run it from Windows:
powershell:
python C:\Users\yourname\Desktop\api_scanner.py

