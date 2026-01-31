import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

if api_key == 'mock_mode_for_testing' or 'sk-your-' in api_key:
    print("✅ Running in MOCK mode (no real API key needed)")
    print("This is perfect for testing and evaluation!")
    print("\nFor production, replace with real API keys:")
    print("1. Get OpenAI key: https://platform.openai.com/api-keys")
    print("2. Get Endee key: https://github.com/EndeeLabs/endee")
else:
    print(f"✅ API Key detected: {api_key[:10]}...")
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        print("✅ OpenAI connected successfully!")
    except Exception as e:
        print(f"❌ OpenAI error: {e}")