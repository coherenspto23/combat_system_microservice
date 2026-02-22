from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/api/combat/attack', methods=['POST'])
def calculate_attack():
    """
    Calculate combat results based on attacker and defender stats
    
    Expects JSON:
    {
        "attacker": {
            "strength": int,
            "agility": int,
            "weapon_damage": int (optional)
        },
        "defender": {
            "defense": int,
            "armor": int (optional),
            "agility": int,
            "health": int
        }
    }
    
    Returns JSON:
    {
        "damage": int,
        "critical_hit": bool,
        "dodged": bool,
        "message": str,
        "defender_health": int
    }
    """
    data = request.json
    
    attacker = data.get('attacker', {})
    defender = data.get('defender', {})
    
    # Extract attacker stats
    attacker_strength = attacker.get('strength', 5)
    attacker_agility = attacker.get('agility', 5)
    weapon_damage = attacker.get('weapon_damage', 0) # optional if you use items
    
    # Extract defender stats
    defender_defense = defender.get('defense', 5)
    defender_armor = defender.get('armor', 0) # optional if you use armor
    defender_agility = defender.get('agility', 5)
    defender_health = defender.get('health', 100)
    
    # Check for dodge (based on defender's agility)
    dodge_roll = random.randint(1, 100)
    dodged = dodge_roll <= defender_agility
    
    if dodged:
        return jsonify({
            "damage": 0,
            "critical_hit": False,
            "dodged": True,
            "message": "Dodged with quick reflexes!",
            "defender_health": defender_health
        }), 200
    
    # Calculate base damage
    base_damage = (attacker_strength * 2) + weapon_damage - (defender_defense + defender_armor)
    base_damage = max(1, base_damage)  # Minimum 1 damage
    
    # Check for critical hit (based on attacker's agility)
    crit_roll = random.randint(1, 100)
    is_crit = crit_roll <= attacker_agility
    
    if is_crit:
        damage = base_damage * 2
        message = "CRITICAL HIT! Precise strike!"
    else:
        damage = base_damage
        message = "Normal hit"
    
    # Calculate defender's remaining health
    new_health = defender_health - damage
    
    return jsonify({
        "damage": damage,
        "critical_hit": is_crit,
        "dodged": False,
        "message": message,
        "defender_health": new_health
    }), 200


@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if service is running"""
    return jsonify({
        'status': 'healthy',
        'service': 'combat_calculator'
    }), 200


if __name__ == '__main__':
    # print("="*60)
    # print("  COMBAT CALCULATOR MICROSERVICE")
    # print("="*60)
    # print("Running on http://localhost:5004")
    # print("Endpoint: POST /api/combat/attack")
    # print("Health check: GET /api/health")
    # print("="*60)
    app.run(host='0.0.0.0', port=5004, debug=True)