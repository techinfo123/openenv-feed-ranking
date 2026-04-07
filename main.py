import json
import random
import numpy as np
import os

from env.feed_env import FeedRankingEnv
from agents.random_agent import RandomAgent
from evaluation.grader import evaluate_all_tasks

# ---------------------------
# Environment Variables (required format)
# ---------------------------
API_BASE_URL = os.getenv("API_BASE_URL", "default")
MODEL_NAME = os.getenv("MODEL_NAME", "baseline")
HF_TOKEN = os.getenv("HF_TOKEN")

# ---------------------------
# Reproducibility
# ---------------------------
def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)

set_seed()

# ---------------------------
# Load data
# ---------------------------
with open("data/posts.json", "r") as f:
    posts = json.load(f)

# ---------------------------
# Initialize agent
# ---------------------------
agent = RandomAgent()

# ---------------------------
# Evaluate
# ---------------------------
results = evaluate_all_tasks(agent, posts, FeedRankingEnv)

# ---------------------------
# REQUIRED STRUCTURED OUTPUT
# ---------------------------
print("START")

for task, score in results.items():
    print(f"STEP task={task} score={round(score, 2)}")

print("END")