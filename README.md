# Combat Calculator Microservice - Mael, Mason and David

## Communication Contract
We will communicate primarily through Teams.
We will respond to messages within 24 hours, even if it’s just “I see this and have no objections”.
If a team member has been unresponsive, we will check in over email or on Canvas.
We will be polite and willing to listen to each other, and focus on finding solutions to problems instead of arguing.
We will minimize unspoken assumptions about classwork. In particular, we will prioritize communication about our personal intents for completing assignment work and expectations from the other team member.
If a team member is concerned they will not be able to complete their work by the deadline, reach out to team members for help at least 24 hours before the deadline.


# Microservice Description
This microservice is a way to calculate damage done by the player and to the player. The microservice will take in a number of combat related stats such as strength, agility, defense to calulate damage numbers as well as whether a players attack was a critical hit and if they were able to dodge the enemies attack. These numbers are then returned to the client program.


# Requesting Data

I formated in a way that the microservice can recieve it
```python 
    data = {
    "attacker": {
        "strength" : 12,
        "agility": 8,
        "defense": 5,
    },
    "defender": {
        "health": 100,
        "defense": 3,
        "agility": 6,
        "armor": 2
    },
}
```

The data sent must be in a JSON data type. The microservice will require a certain amount of combat related stats, such as strengh (which increases damage), agility (which increases dodge chance and crit chance), defense(which decreases damage taken) as well as a number of optional statistics such as armor or weapon related stats. The example above is a good representation of what the microservice takes.

# Sending the Request through Flask
First you need to start the microservice. Either in a sperate terminal or use a launcher program to boot up all your microservices. Then the data will be sent to the microservice as seen in the example bellow.

```python
    service_url = "http://localhost:5004/api/combat/attack"
    response = requests.post(service_url, json=data)
```


# Recieving the data

```python
    response = requests.post(service_url, json=data)
    print(response.json())
```

Once the numbers have been calculated, the data will be sent back and stored in the response variable. This means the attack/defense will be executed. The print statement makes it easy to know that it worked.

# UML Diagram

<img width="1233" height="737" alt="image" src="https://github.com/user-attachments/assets/700bfa2e-e1e2-4a3f-ace4-f5bdd4c3441a" />
