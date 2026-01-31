from flask import Flask, render_template, jsonify, request
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, 
           template_folder='src/web/templates',
           static_folder='src/web/static')
app.secret_key = os.getenv('SECRET_KEY', 'test-secret-key')

# Check if we're in mock mode
MOCK_MODE = os.getenv('OPENAI_API_KEY') in ['mock_mode_for_testing', 'sk-your-openai-key-here']

# Mock responses for testing
MOCK_RESPONSES = {
    "legal": [
        "Based on contract law principles, agreements require offer, acceptance, and consideration to be valid.",
        "Intellectual property rights protect creations including patents, copyrights, and trademarks.",
        "A valid contract must have: competent parties, lawful object, consideration, and mutual consent.",
        "Copyright protection automatically applies to original works fixed in a tangible medium."
    ],
    "general": [
        "I'm your legal AI assistant. I can help analyze legal documents and answer questions.",
        "Please upload legal documents to get specific answers based on your content.",
        "I specialize in contract law, intellectual property, and legal document analysis."
    ]
}

@app.route('/')
def index():
    return render_template('index.html', mock_mode=MOCK_MODE)

@app.route('/chat')
def chat():
    return render_template('chat.html', mock_mode=MOCK_MODE)

@app.route('/search')
def search():
    return render_template('search.html', mock_mode=MOCK_MODE)

@app.route('/upload')
def upload():
    return render_template('upload.html', mock_mode=MOCK_MODE)

@app.route('/documents')
def documents():
    return render_template('documents.html', mock_mode=MOCK_MODE)

# API Routes
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Legal RAG Assistant is running',
        'mode': 'MOCK' if MOCK_MODE else 'PRODUCTION',
        'version': '1.0.0',
        'features': ['chat', 'search', 'upload', 'documents', 'api']
    })

@app.route('/api/chat', methods=['POST'])
def chat_api():
    """Chat API endpoint - works in both mock and real mode"""
    try:
        data = request.json
        query = data.get('query', '').strip().lower()
        
        if not query:
            return jsonify({'error': 'No query provided'}), 400
        
        if MOCK_MODE:
            # Return mock response
            import random
            responses = MOCK_RESPONSES["legal"] if any(word in query for word in ['contract', 'law', 'legal', 'rights', 'property']) else MOCK_RESPONSES["general"]
            response_text = random.choice(responses)
            
            return jsonify({
                'success': True,
                'answer': f"[MOCK MODE] {response_text}",
                'mode': 'mock',
                'sources': [
                    {'source': 'mock_document.pdf', 'relevance_score': 0.95},
                    {'source': 'sample_contract.docx', 'relevance_score': 0.87}
                ]
            })
        else:
            # Real OpenAI integration would go here
            return jsonify({
                'success': True,
                'answer': 'Real OpenAI integration would be active with valid API keys.',
                'mode': 'production'
            })
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search', methods=['POST'])
def search_api():
    """Search API endpoint"""
    try:
        data = request.json
        query = data.get('query', '')
        filters = data.get('filters', {})
        
        # Mock search results
        mock_results = [
            {
                'id': 'doc_001',
                'title': 'Contract Law Overview',
                'content': 'Contract law governs agreements between parties...',
                'score': 0.95,
                'metadata': {
                    'source': 'contract_guide.pdf',
                    'jurisdiction': 'federal',
                    'type': 'contract',
                    'year': 2023
                }
            },
            {
                'id': 'doc_002',
                'title': 'Intellectual Property Rights',
                'content': 'IP rights protect inventions, literary works, and trademarks...',
                'score': 0.87,
                'metadata': {
                    'source': 'ip_law.docx',
                    'jurisdiction': 'international',
                    'type': 'statute',
                    'year': 2022
                }
            },
            {
                'id': 'doc_003',
                'title': 'Case Study: Smith vs Jones',
                'content': 'This case established precedents in contract interpretation...',
                'score': 0.78,
                'metadata': {
                    'source': 'case_study.txt',
                    'jurisdiction': 'state',
                    'type': 'case',
                    'year': 2021
                }
            }
        ]
        
        # Apply filters if provided
        filtered_results = mock_results
        if filters:
            filtered_results = [
                doc for doc in mock_results
                if all(
                    doc['metadata'].get(key) == value
                    for key, value in filters.items()
                    if value  # Only apply if filter has a value
                )
            ]
        
        return jsonify({
            'success': True,
            'query': query,
            'results': filtered_results,
            'count': len(filtered_results),
            'mode': 'mock' if MOCK_MODE else 'production'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/upload', methods=['POST'])
def upload_api():
    """File upload API"""
    if MOCK_MODE:
        return jsonify({
            'success': True,
            'message': 'Mock upload successful',
            'files_processed': 1,
            'mode': 'mock'
        })
    else:
        return jsonify({
            'success': True,
            'message': 'File upload endpoint ready',
            'mode': 'production'
        })

@app.route('/api/documents', methods=['GET'])
def list_documents():
    """List documents API"""
    mock_documents = [
        {'id': 1, 'name': 'contract_law.pdf', 'type': 'pdf', 'size': '2.4 MB', 'chunks': 12},
        {'id': 2, 'name': 'intellectual_property.docx', 'type': 'docx', 'size': '1.8 MB', 'chunks': 8},
        {'id': 3, 'name': 'case_study.txt', 'type': 'txt', 'size': '0.5 MB', 'chunks': 3}
    ]
    
    return jsonify({
        'success': True,
        'documents': mock_documents,
        'total': len(mock_documents),
        'total_chunks': sum(doc['chunks'] for doc in mock_documents)
    })

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')
    
    print("=" * 50)
    print("🚀 LEGAL RAG ASSISTANT")
    print("=" * 50)
    print(f"Mode: {'MOCK (No API keys needed)' if MOCK_MODE else 'PRODUCTION'}")
    print(f"Port: {port}")
    print(f"Host: {host}")
    print("\n📁 Available Pages:")
    print(f"  Home:        http://localhost:{port}")
    print(f"  Chat:        http://localhost:{port}/chat")
    print(f"  Search:      http://localhost:{port}/search")
    print(f"  Upload:      http://localhost:{port}/upload")
    print(f"  Documents:   http://localhost:{port}/documents")
    print(f"  API Health:  http://localhost:{port}/api/health")
    print("\n🔧 API Endpoints:")
    print(f"  POST /api/chat    - Chat with documents")
    print(f"  POST /api/search  - Search documents")
    print(f"  POST /api/upload  - Upload documents")
    print(f"  GET  /api/health  - System health")
    print("=" * 50)
    
    app.run(host=host, port=port, debug=True)