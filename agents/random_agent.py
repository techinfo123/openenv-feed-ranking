import random

class RandomAgent:
    def act(self, state, posts):
        return random.sample(posts, 3)