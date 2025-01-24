import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def validate_input(user_input):
    """
    Validates user input to ensure it's not empty or invalid.
    """
    if not user_input or not isinstance(user_input, str):
        logging.warning("Invalid input received.")
        return False
    return True

def create_session(user_id):
    """
    Creates a unique session ID for a user.
    """
    session_id = f"{user_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    logging.info(f"Session created: {session_id}")
    return session_id

def log_interaction(agent, user_input, response):
    """
    Logs interactions between the user and the AI agent.
    """
    logging.info(f"Agent: {agent} | Input: {user_input} | Response: {response}")
