@echo off
echo ========================================
echo LEGAL RAG ASSISTANT - VERIFICATION
echo ========================================

echo.
echo 1. Checking Python version...
python --version

echo.
echo 2. Checking Flask installation...
python -c "import flask; print('Flask version:', flask.__version__)"

echo.
echo 3. Testing web server...
timeout /t 2 /nobreak >nul
curl -s http://localhost:5000/api/health | python -m json.tool

echo.
echo 4. Checking project structure...
dir /b *.py
echo ---
dir /b src\

echo.
echo 5. Checking dependencies...
pip list | findstr -i "flask openai endee"

echo.
echo ========================================
echo VERIFICATION COMPLETE!
echo ========================================
echo.
echo Access the application at:
echo http://localhost:5000
echo.
echo Pages available:
echo - Home:        http://localhost:5000
echo - Chat:        http://localhost:5000/chat
echo - Search:      http://localhost:5000/search
echo - Upload:      http://localhost:5000/upload
echo - Documents:   http://localhost:5000/documents
echo - API Health:  http://localhost:5000/api/health
echo.
pause