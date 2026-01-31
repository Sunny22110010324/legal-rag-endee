# Create a test file test_endee.py
import sys
sys.path.append('.')
from src.database.endee_client import MockEndeeClient

client = MockEndeeClient()
print("Mock Endee Client:", client.get_collection_stats())