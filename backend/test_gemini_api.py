"""
Quick test script to verify Gemini API connection
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key loaded: {api_key[:20]}..." if api_key else "❌ No API key found!")

try:
    # Configure the API
    genai.configure(api_key=api_key)
    
    # Test with gemini-2.5-flash model (latest stable)
    print("\n🧪 Testing gemini-2.5-flash model...")
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    response = model.generate_content("Say 'Hello! API is working!' in one sentence.")
    print(f"✅ SUCCESS! Response: {response.text}")
    
except Exception as e:
    print(f"❌ ERROR: {str(e)}")
    print("\n💡 Trying to list available models...")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"  - {m.name}")
    except Exception as e2:
        print(f"❌ Could not list models: {str(e2)}")
