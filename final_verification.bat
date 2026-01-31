@echo off
echo ================================================
echo LEGAL RAG ASSISTANT - FINAL VERIFICATION
echo ================================================
echo.
echo Checking if server is running...
timeout /t 2 /nobreak >nul

echo.
echo 1. Testing Health API with Python...
python -c "
import requests
try:
    r = requests.get('http://localhost:5000/api/health', timeout=5)
    print('✅ Health API: Status', r.status_code)
    data = r.json()
    print('✅ Mode:', data.get('mode', 'unknown'))
    print('✅ Features:', ', '.join(data.get('features', [])))
except Exception as e:
    print('❌ Error:', e)
"

echo.
echo 2. Testing Chat API...
python -c "
import requests
try:
    r = requests.post('http://localhost:5000/api/chat', 
                     json={'query': 'Test question'}, 
                     timeout=5)
    data = r.json()
    print('✅ Chat API: Success', data.get('success', False))
    print('✅ Answer preview:', str(data.get('answer', ''))[:80] + '...')
except Exception as e:
    print('❌ Error:', e)
"

echo.
echo 3. Project Structure Check...
if exist "app.py" (
    echo ✅ app.py found
) else (
    echo ❌ app.py missing
)

if exist "src\web\templates\index.html" (
    echo ✅ HTML templates found
) else (
    echo ❌ HTML templates missing
)

if exist "requirements.txt" (
    echo ✅ requirements.txt found
    python -c "print('   Dependencies:', len(open('requirements.txt').readlines()), 'packages')"
)

echo.
echo 4. Opening browser for manual test...
start http://localhost:5000
timeout /t 2

echo.
echo ================================================
echo ✅ VERIFICATION COMPLETE!
echo ================================================
echo.
echo NEXT STEPS:
echo 1. Open browser to: http://localhost:5000
echo 2. Test all 5 pages manually
echo 3. Take screenshots for submission
echo 4. Push to GitHub repository
echo.
echo For submission, include:
echo - GitHub repository link
echo - Screenshots of working application
echo - Instructions: python app.py
echo.
pause