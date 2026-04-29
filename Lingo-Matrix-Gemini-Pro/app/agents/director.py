# app/agents/director.py
class SceneDirector:
    def __init__(self):
        self.scenarios = {
            "business": "A high-stakes salary negotiation for a Senior Dev role.",
            "academic": "Defending a thesis on Artificial Intelligence at MIT.",
            "daily": "Ordering a complex custom coffee in a busy London cafe."
        }

    def get_scene_prompt(self, level="advanced"):
        """根据用户等级动态切换场景难度，体现长链逻辑控制"""
        # 逻辑：如果是高级用户，导演会加入突发状况（如面试官突然刁难）
        prompt = f"Current Scene: {self.scenarios['business']}. Difficulty: {level}."
        return prompt