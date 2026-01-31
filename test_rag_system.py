import sys
sys.path.append('.')

def test_components():
    print("🧪 Testing Legal RAG Assistant Components...")
    
    # Test 1: Config loader
    try:
        from src.utils.config_loader import load_config
        config = load_config()
        print("✅ Config loader: Working")
    except Exception as e:
        print(f"❌ Config loader: {e}")
    
    # Test 2: Logger
    try:
        from src.utils.logger import get_logger
        logger = get_logger("test")
        logger.info("Test log message")
        print("✅ Logger: Working")
    except Exception as e:
        print(f"❌ Logger: {e}")
    
    # Test 3: Endee client
    try:
        from src.database.endee_client import MockEndeeClient
        client = MockEndeeClient()
        stats = client.get_collection_stats()
        print(f"✅ Endee client: {stats}")
    except Exception as e:
        print(f"❌ Endee client: {e}")
    
    # Test 4: Flask app
    try:
        from app import app
        print("✅ Flask app: Imported successfully")
    except Exception as e:
        print(f"❌ Flask app: {e}")
    
    print("\n🎯 All tests completed!")

if __name__ == "__main__":
    test_components()