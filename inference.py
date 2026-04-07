from fastapi import FastAPI
import json
from env.feed_env import FeedRankingEnv
from agents.random_agent import RandomAgent

app = FastAPI()

# Load data
with open("data/posts.json", "r") as f:
    posts = json.load(f)

env = FeedRankingEnv(posts, task="hard")
agent = RandomAgent()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state.__dict__}

@app.post("/step")
def step():
    action = agent.act(env.state(), env.posts)
    state, reward, done, _ = env.step(action)

    return {
        "state": state.__dict__,
        "reward": reward,
        "done": done
    }