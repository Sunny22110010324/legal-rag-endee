import os
from typing import List, Dict, Any, Optional

class MockEndeeClient:
    """Mock Endee client for testing"""
    
    def __init__(self, api_key: Optional[str] = None, endpoint: Optional[str] = None):
        print("✅ Using Mock Endee Client (for testing)")
        self.collection_name = "legal_documents"
    
    def get_collection_stats(self) -> Dict[str, Any]:
        return {
            "total_documents": 0,
            "collection_name": self.collection_name,
            "status": "mock_mode"
        }
    
    def add_documents(self, documents: List[Dict[str, Any]]) -> List[str]:
        print(f"📝 Mock: Would add {len(documents)} documents")
        return [f"mock_id_{i}" for i in range(len(documents))]
    
    def search(self, query_vector: List[float], top_k: int = 5, filter_dict: Optional[Dict] = None) -> List[Dict[str, Any]]:
        print(f"🔍 Mock: Searching with top_k={top_k}")
        return [
            {
                "id": "mock_doc_1",
                "score": 0.95,
                "content": "This is a mock legal document about contract law.",
                "metadata": {"source": "mock.pdf", "title": "Contract Law Example"}
            },
            {
                "id": "mock_doc_2", 
                "score": 0.85,
                "content": "Another mock document about intellectual property rights.",
                "metadata": {"source": "mock2.pdf", "title": "IP Law Guide"}
            }
        ][:top_k]

# For production, you would use the real Endee client
# from endee import Client