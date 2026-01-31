import requests
import json

BASE_URL = "http://localhost:5000"

def test_all_features():
    print("🧪 Testing Legal RAG Assistant Features")
    print("=" * 50)
    
    # Test 1: Health endpoint
    print("\n1. Testing Health API...")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # Test 2: Chat API
    print("\n2. Testing Chat API...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/chat",
            json={"query": "What is contract law?"}
        )
        data = response.json()
        print(f"   Success: {data.get('success')}")
        print(f"   Mode: {data.get('mode')}")
        print(f"   Answer preview: {data.get('answer', '')[:80]}...")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # Test 3: Search API
    print("\n3. Testing Search API...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/search",
            json={"query": "intellectual property", "filters": {"jurisdiction": "international"}}
        )
        data = response.json()
        print(f"   Results: {data.get('count')}")
        print(f"   Query: {data.get('query')}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # Test 4: List documents
    print("\n4. Testing Documents API...")
    try:
        response = requests.get(f"{BASE_URL}/api/documents")
        data = response.json()
        print(f"   Documents: {data.get('total')}")
        print(f"   Total chunks: {data.get('total_chunks')}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\n🌐 Open browser to: http://localhost:5000")
    print("📚 Check all 5 pages work correctly")

if __name__ == "__main__":
    test_all_features()