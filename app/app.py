import json
import random
import gradio as gr

from env.feed_env import FeedRankingEnv
from agents.random_agent import RandomAgent

# Load data
posts = json.load(open("data/posts.json"))

env = FeedRankingEnv(posts, task="hard")
agent = RandomAgent()

def run_demo(task):
    env.task = task
    state = env.reset()
    done = False

    log = []
    total_reward = 0

    while not done:
        action = agent.act(state, env.posts)
        state, reward, done, _ = env.step(action)

        total_reward += reward

        log.append({
            "action": [p["id"] for p in action],
            "reward": round(reward, 2),
            "fatigue": round(state.fatigue, 2)
        })

    return log, round(total_reward, 2)

def format_output(log, total):
    text = "=== Simulation Steps ===\n\n"
    for i, step in enumerate(log):
        text += f"Step {i+1}:\n"
        text += f"  Posts: {step['action']}\n"
        text += f"  Reward: {step['reward']}\n"
        text += f"  Fatigue: {step['fatigue']}\n\n"

    text += f"TOTAL REWARD: {total}\n"
    return text

def run(task):
    log, total = run_demo(task)
    return format_output(log, total)

demo = gr.Interface(
    fn=run,
    inputs=gr.Dropdown(["easy", "medium", "hard"], label="Select Task"),
    outputs="text",
    title="Value-Aware Feed Ranking Environment",
    description="Simulates RL-based feed ranking with engagement, alignment, and toxicity trade-offs."
)

if __name__ == "__main__":
    demo.launch()