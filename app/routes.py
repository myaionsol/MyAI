from flask import Blueprint, request, jsonify
from .agents import victor, sage, amara, cash

api = Blueprint('api', __name__)

AGENTS = {
    'victor': victor.get_response,
    'sage': sage.get_response,
    'amara': amara.get_response,
    'cash': cash.get_response,
}

@api.route('/interact/<agent_name>', methods=['POST'])
def interact(agent_name):
    if agent_name not in AGENTS:
        return jsonify({'error': 'Agent not found'}), 404

    user_input = request.json.get('input', '')
    response = AGENTS[agent_name](user_input)
    return jsonify({'response': response})
