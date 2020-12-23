import random

def rotate(hand, turns):
    return (hand + turns) % 3

def copy_opponent_agent(observation, configuration):
    if observation.step > 0:
        return rotate(observation.lastOpponentAction, 2)
    else:
        return random.randint(0,2)
