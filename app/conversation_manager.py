class ConversationManager:
    """
    Manages user-agent interactions, maintaining context across turns.
    """
    def __init__(self):
        self.conversations = {}

    def start_conversation(self, user_id, agent):
        """
        Initializes a conversation session.
        """
        if user_id not in self.conversations:
            self.conversations[user_id] = {
                "agent": agent,
                "context": []
            }
            return f"Conversation started with {agent.name}."
        return "Conversation already in progress."

    def handle_input(self, user_id, user_input):
        """
        Handles user input and generates a response from the agent.
        """
        if user_id not in self.conversations:
            return "No active conversation. Start a session first."

        agent = self.conversations[user_id]["agent"]
        context = self.conversations[user_id]["context"]
        context.append(user_input)

        # Generate response using the agent
        response = agent.respond(user_input)
        context.append(response)

        # Maintain only the last 5 exchanges for simplicity
        self.conversations[user_id]["context"] = context[-5:]
        return response

    def end_conversation(self, user_id):
        """
        Ends the conversation session.
        """
        if user_id in self.conversations:
            del self.conversations[user_id]
            return "Conversation ended."
        return "No active conversation to end."


if __name__ == "__main__":
    # Example usage
    from agent_factory import AgentFactory

    manager = ConversationManager()
    user_id = "user123"
    agent = AgentFactory.create_agent("Amara")

    print(manager.start_conversation(user_id, agent))
    print(manager.handle_input(user_id, "How do I ask someone out?"))
    print(manager.end_conversation(user_id))
