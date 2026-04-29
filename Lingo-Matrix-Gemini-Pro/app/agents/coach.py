# app/agents/coach.py
class LanguageCoach:
    def analyze_feedback(self, user_input, model_response):
        """
        利用 Gemini 3.1 Pro 的推理能力进行深层纠错
        思维链 (CoT) 逻辑：
        1. 识别：用户是否使用了 'think' 而不是 'ponder'？
        2. 推理：是因为母语中没有区分这类近义词吗？
        3. 建议：在下一轮对话中潜移默化引导用户使用高级词汇。
        """
        analysis_prompt = f"Analyze user's syntax: '{user_input}'. Detect native language interference."
        return analysis_prompt