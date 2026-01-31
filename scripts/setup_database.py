#!/usr/bin/env python3
"""
Setup script for Legal RAG Assistant
"""
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def setup_project():
    print("=" * 50)
    print("Legal RAG Assistant - Setup Script")
    print("=" * 50)
    
    # Create necessary directories
    directories = ['uploads', 'logs', 'data/sample_documents']
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created directory: {directory}")
    
    # Check for .env file
    if not os.path.exists('.env'):
        print("\n⚠  Warning: .env file not found!")
        print("   Copy .env.example to .env and add your API keys")
        print("   Command: copy .env.example .env")
    else:
        print("\n✓ .env file found")
    
    # Import test
    try:
        from src.database.endee_client import MockEndeeClient
        client = MockEndeeClient()
        stats = client.get_collection_stats()
        print(f"✓ Database client: {stats['collection_name']} ({stats['status']})")
    except Exception as e:
        print(f"✗ Database client error: {e}")
    
    # Flask test
    try:
        import flask
        print(f"✓ Flask version: {flask.__version__}")
    except:
        print("✗ Flask not installed")
    
    print("\n" + "=" * 50)
    print("Setup complete!")
    print("Next steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Add API keys to .env file")
    print("3. Run the app: python app.py")
    print("4. Visit: http://localhost:5000")
    print("=" * 50)

if __name__ == "__main__":
    setup_project()