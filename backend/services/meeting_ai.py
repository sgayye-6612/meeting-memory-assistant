from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage


class MeetingAI:
    def __init__(self):
        self.llm = ChatOllama(
            model="llama3.2",
            temperature=0
        )

    def analyze(self, transcript: str) -> str:
        system_prompt = """
You are a meeting analysis assistant.

Analyze the meeting transcript and return the following sections:

SUMMARY:
A concise summary of the meeting.

IMPORTANT POINTS:
List the most important discussion points.

DECISIONS:
List decisions that were made.

ACTION ITEMS:
List tasks that need to be completed.

OWNERS:
Identify the person responsible for each action item when mentioned.

DEADLINES:
Identify deadlines or target dates when mentioned.

OPEN QUESTIONS:
List questions or issues that remain unresolved.

Only use information explicitly present in the transcript.
Do not invent names, decisions, deadlines, or action items.
"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(
                content=f"Analyze this meeting transcript:\n\n{transcript}"
            )
        ]

        response = self.llm.invoke(messages)

        return response.content