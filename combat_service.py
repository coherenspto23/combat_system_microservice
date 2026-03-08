from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Combat data extracted 
def extract_attacker(data):
    attacker = data.get('attacker', {})
    return {
        'strength': attacker.get('strength', 5),
        'agility': attacker.get('agility', 5),
        'weapon_damage': attacker.get('weapon_damage', 0)
    }

def extract_defender(data):
    defender = data.get('defender', {})
    return {
        'defense': defender.get('defense', 5),
        'armor': defender.get('armor', 0),
        'agility': defender.get('agility', 5),
        'health': defender.get('health', 100)
    }
# Combat moves calculated
def dodge(defender_agility):  
    dodge_roll = random.randint(1, 100)
    dodged = dodge_roll <= defender_agility
    return dodged

def base_damage(attacker_strength, weapon_damage, defender_defense, defender_armor): 
    base_damage = (attacker_strength * 2) + weapon_damage - (defender_defense + defender_armor)
    base_damage = max(1, base_damage)
    return base_damage

def crit(attacker_agility):
    crit_roll = random.randint(1, 100)
    is_crit = crit_roll <= attacker_agility
    return is_crit
def resolve_attack(attacker, defender):
    if dodge(defender['agility']):
        return 0, False, True, "Dodged with quick reflexes!"
    
    is_crit = crit(attacker['agility'])
    damage = base_damage(attacker['strength'], attacker['weapon_damage'], defender['defense'], defender['armor'])
    
    if is_crit:
        damage *= 2
        message = "CRITICAL HIT! Precise strike!"
    else:
        message = "Normal hit"
    
    return damage, is_crit, False, message

# Get data and return it to user
@app.route('/api/combat/attack', methods=['POST'])
def calculate_attack():
    data = request.json
    attacker = extract_attacker(data)
    defender = extract_defender(data)
    damage, is_crit, dodged, message = resolve_attack(attacker, defender)
    
    return jsonify({
        "damage": damage,
        "critical_hit": is_crit,
        "dodged": dodged,
        "message": message,
        "defender_health": defender['health'] - damage
    }), 200

# Shows remaining helth of player
@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if service is running"""
    return jsonify({
        'status': 'healthy',
        'service': 'combat_calculator'
    }), 200


if __name__ == '__main__':
    print("="*60)
    print("  COMBAT CALCULATOR MICROSERVICE")
    print("="*60)
    print("Running on http://localhost:5004")
    print("Endpoint: POST /api/combat/attack")
    print("Health check: GET /api/health")
    print("="*60)
    app.run(host='0.0.0.0', port=5004, debug=True)
