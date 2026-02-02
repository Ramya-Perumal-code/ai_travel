import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# CONFIGURATION
# Set this to your Koyeb App URL (e.g., https://your-app-name.koyeb.app)
KOYEB_URL = "https://inevitable-catlin-self-learner-ai-337aa463.koyeb.app" # <--- UPDATE THIS
API_KEY = os.getenv("GROQ_API_KEY") 
print(f"🔑 Using API Key: {API_KEY[:5]}...{API_KEY[-5:]}")

def migrate_data():
    dataset_folder = "dataset_json"
    
    if not os.path.exists(dataset_folder):
        print(f"❌ Folder {dataset_folder} not found!")
        return

    print(f"🚀 Starting migration to {KOYEB_URL}...")
    
    files = [f for f in os.listdir(dataset_folder) if f.endswith(".json")]
    
    success_count = 0
    for filename in files:
        print(f"📄 Processing {filename}...", end=" ", flush=True)
        file_path = os.path.join(dataset_folder, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Send to your cloud API
            response = requests.post(
                f"{KOYEB_URL}/api/v1/upload-json",
                params={"api_key": API_KEY},
                json=data
            )
            
            if response.status_code == 200:
                print("✅ Success")
                success_count += 1
            else:
                print(f"❌ Failed ({response.status_code}): {response.text}")
                
        except Exception as e:
            print(f"❌ Error: {e}")

    print(f"\n✨ Done! Migrated {success_count}/{len(files)} files to Cloud RAG.")

if __name__ == "__main__":
    if not API_KEY:
        print("❌ Error: GROQ_API_KEY not found in .env file.")
    else:
        migrate_data()
