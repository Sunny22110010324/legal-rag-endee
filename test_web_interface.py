import webbrowser
import time
import requests

def test_web_interface():
    print("🌐 Testing Web Interface")
    print("=" * 50)
    
    base_url = "http://localhost:5000"
    endpoints = [
        ("🏠 Home", "/"),
        ("💬 Chat", "/chat"),
        ("🔍 Search", "/search"),
        ("⬆️ Upload", "/upload"),
        ("📁 Documents", "/documents"),
        ("❤️ Health API", "/api/health")
    ]
    
    print("\nOpening pages in browser...")
    for name, endpoint in endpoints[:3]:  # Open first 3 pages
        url = base_url + endpoint
        print(f"  Opening {name}: {url}")
        webbrowser.open(url)
        time.sleep(1)  # Wait between openings
    
    print("\nChecking all endpoints...")
    for name, endpoint in endpoints:
        url = base_url + endpoint
        try:
            response = requests.get(url, timeout=5)
            status = "✅ 200 OK" if response.status_code == 200 else f"❌ {response.status_code}"
            print(f"  {name:15} {status}")
        except:
            print(f"  {name:15} ❌ Failed")
    
    print("\n" + "=" * 50)
    print("🎯 Manual Testing Instructions:")
    print("1. Chat Page: Try asking 'What is contract law?'")
    print("2. Search Page: Search for 'intellectual property'")
    print("3. Upload Page: Click upload area")
    print("4. Documents Page: Check document list")
    print("\nAll pages should work without errors!")

if __name__ == "__main__":
    test_web_interface()