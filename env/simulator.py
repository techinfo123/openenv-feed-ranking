import random

def simulate_user(action, state):
    responses = []

    for post in action:
        score = state.interest - state.fatigue

        if score > 0.6:
            responses.append("click")
        elif score > 0.3:
            responses.append("watch")
        else:
            responses.append("skip")

    # user drift
    state.interest += random.uniform(-0.05, 0.05)
    state.fatigue += 0.02

    return responses