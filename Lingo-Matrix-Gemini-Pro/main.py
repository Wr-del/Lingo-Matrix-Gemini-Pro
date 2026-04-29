import os
from app.core.gemini_client import GeminiMatrixClient

def main():
    print("--- Lingo-Matrix v0.1 (Experimental Gemini 3.1 Pro) ---")
    # 模拟初始化
    client = GeminiMatrixClient(api_key="YOUR_GEMINI_API_KEY")
    print("Status: Connected to Gemini 3.1 Pro Engine")
    print("Ready for Multi-Agent Oral Training Session.")

if __name__ == "__main__":
    main()