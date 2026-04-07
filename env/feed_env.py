from env.state import init_user
from env.simulator import simulate_user
from env.reward import compute_reward

class FeedRankingEnv:
    def __init__(self, posts, task="hard"):
        self.posts = posts
        self.task = task
        self._state = None
        self.step_count = 0

    def reset(self):
        self._state = init_user()
        self.step_count = 0
        return self._state

    def step(self, action):
        responses = simulate_user(action, self._state)
        reward = compute_reward(action, responses, self._state, self.task)

        self._state.history.extend([p["id"] for p in action])
        self.step_count += 1

        done = self.step_count >= 20

        return self._state, reward, done, {}

    def state(self):
        return self._state