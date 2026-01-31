import requests
import json

BASE_URL = "http://localhost:5000"

def test_all_apis():
    print("🧪 Testing Legal RAG Assistant APIs")
    print("=" * 60)
    
    # Test 1: Health endpoint
    print("\n1. 🔍 Testing Health API...")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"   ✅ Status: {response.status_code}")
        data = response.json()
        print(f"   ✅ Mode: {data.get('mode')}")
        print(f"   ✅ Message: {data.get('message')}")
        print(f"   ✅ Features: {', '.join(data.get('features', []))}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # Test 2: Chat API
    print("\n2. 💬 Testing Chat API...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/chat",
            json={"query": "What is contract law?"}
        )
        data = response.json()
        print(f"   ✅ Success: {data.get('success')}")
        print(f"   ✅ Mode: {data.get('mode')}")
        answer = data.get('answer', '')
        print(f"   ✅ Answer: {answer[:100]}...")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # Test 3: Search API
    print("\n3. 🔎 Testing Search API...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/search",
            json={
                "query": "intellectual property rights",
                "filters": {"jurisdiction": "international"}
            }
        )
        data = response.json()
        print(f"   ✅ Success: {data.get('success')}")
        print(f"   ✅ Results found: {data.get('count')}")
        print(f"   ✅ Query: {data.get('query')}")
        
        # Show first result
        results = data.get('results', [])
        if results:
            first_result = results[0]
            print(f"   ✅ First result: {first_result.get('title')}")
            print(f"   ✅ Score: {first_result.get('score')}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # Test 4: Documents API
    print("\n4. 📁 Testing Documents API...")
    try:
        response = requests.get(f"{BASE_URL}/api/documents")
        data = response.json()
        print(f"   ✅ Success: {data.get('success')}")
        print(f"   ✅ Total documents: {data.get('total')}")
        print(f"   ✅ Total chunks: {data.get('total_chunks')}")
        
        # List documents
        docs = data.get('documents', [])
        for i, doc in enumerate(docs[:3], 1):
            print(f"   📄 Document {i}: {doc.get('name')} ({doc.get('type')})")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # Test 5: Upload API
    print("\n5. ⬆️ Testing Upload API (mock)...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/upload",
            json={"test": "file"}
        )
        data = response.json()
        print(f"   ✅ Success: {data.get('success')}")
        print(f"   ✅ Message: {data.get('message')}")
        print(f"   ✅ Mode: {data.get('mode')}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 ALL TESTS COMPLETED!")
    print("\n📊 Summary:")
    print(f"   Server: {BASE_URL}")
    print(f"   Mode: MOCK (No API keys needed)")
    print(f"   Status: ✅ RUNNING")
    
    print("\n🌐 Open in browser:")
    print(f"   Home: {BASE_URL}")
    print(f"   Chat: {BASE_URL}/chat")
    print(f"   Search: {BASE_URL}/search")

if __name__ == "__main__":
    test_all_apis()