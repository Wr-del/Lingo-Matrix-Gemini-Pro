# app/agents/partner.py
class DialoguePartner:
    def __init__(self, personality="friendly"):
        self.personality = personality

    def craft_response(self, context, core_feedback):
        """结合教练建议和当前语境生成回复"""
        return "Hey! That's a great point, but have you considered..."