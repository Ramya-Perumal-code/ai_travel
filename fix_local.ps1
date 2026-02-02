# 1. Activate existing venv (assuming it was created)
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    .\venv\Scripts\Activate.ps1
} else {
    python -m venv venv
    .\venv\Scripts\Activate.ps1
}

Write-Host "📦 Installing dependencies one by one to catch errors..." -ForegroundColor Cyan

# Install core utilities first
pip install python-dotenv requests pydantic-settings --prefer-binary

# Install LangChain core and community
pip install langchain-core langchain-community --prefer-binary

# Install Qdrant specific
pip install qdrant-client langchain-qdrant --prefer-binary

# Install FastEmbed (might fail on 3.14 if binaries are missing)
pip install fastembed --prefer-binary

Write-Host "`n🔍 Checking installed packages..." -ForegroundColor Yellow
pip list | Select-String "langchain|qdrant|fastembed"

Write-Host "`n✅ Done. Please check if any 'ERROR' occurred above." -ForegroundColor Green
