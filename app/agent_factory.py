class Agent:
    """
    Base class for AI agents.
    """
    def __init__(self, name, expertise, personality):
        self.name = name
        self.expertise = expertise
        self.personality = personality

    def respond(self, user_input):
        """
        Simulates a response based on the agent's personality and expertise.
        """
        return f"{self.name} ({self.expertise}): {self.personality} response to '{user_input}'."


class AgentFactory:
    """
    Factory for creating AI agents.
    """
    @staticmethod
    def create_agent(agent_type):
        if agent_type == "Victor":
            return Agent(
                name="Victor",
                expertise="Career Strategy",
                personality="Sharp, tactical, and commanding"
            )
        elif agent_type == "Sage":
            return Agent(
                name="Sage",
                expertise="Wellness Coaching",
                personality="Calm, poetic, and wise"
            )
        elif agent_type == "Amara":
            return Agent(
                name="Amara",
                expertise="Love and Relationships",
                personality="Flamboyant, passionate, and romantic"
            )
        elif agent_type == "Cash":
            return Agent(
                name="Cash",
                expertise="Financial Advice",
                personality="Street-smart, charismatic, and practical"
            )
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")


if __name__ == "__main__":
    # Example of using the factory to create agents
    agent = AgentFactory.create_agent("Victor")
    print(agent.respond("How can I negotiate a raise?"))
