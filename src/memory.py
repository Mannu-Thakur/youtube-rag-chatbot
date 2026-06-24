from dataclasses import dataclass, field


@dataclass
class ConversationMemory:
    turns: list[tuple[str, str]] = field(default_factory=list)
    max_turns: int = 6

    def add_turn(self, user_message: str, assistant_message: str) -> None:
        self.turns.append((user_message, assistant_message))
        self.turns = self.turns[-self.max_turns :]

    def as_text(self) -> str:
        if not self.turns:
            return ""

        lines = []
        for i, (user_message, assistant_message) in enumerate(self.turns, start=1):
            lines.append(f"User {i}: {user_message}")
            lines.append(f"Assistant {i}: {assistant_message}")
        return "\n".join(lines)


def build_retrieval_query(question: str, memory: ConversationMemory) -> str:
    history = memory.as_text().strip()

    if not history:
        return question.strip()

    return (
        "Conversation so far:\n"
        f"{history}\n\n"
        f"Current question:\n{question.strip()}"
    )