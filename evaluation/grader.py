def evaluate(env, agent):
    total = 0

    for _ in range(5):
        state = env.reset()
        done = False

        while not done:
            action = agent.act(state, env.posts)
            state, reward, done, _ = env.step(action)
            total += reward

    return total / 5


def evaluate_all_tasks(agent, posts, EnvClass):
    tasks = ["easy", "medium", "hard"]
    results = {}

    for t in tasks:
        env = EnvClass(posts, task=t)
        results[t] = evaluate(env, agent)

    return results