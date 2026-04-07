def compute_reward(action, responses, state, task):

    engagement = sum(
        [1 if r == "click" else 0.5 if r == "watch" else 0 for r in responses]
    )

    value_align = sum([post["caring"] for post in action]) / len(action)
    toxicity = sum([post["toxicity"] for post in action]) / len(action)

    diversity = len(set([p["id"] for p in action])) / len(action)

    if task == "easy":
        return engagement

    elif task == "medium":
        return engagement + 0.1 * diversity - 0.1 * toxicity

    else:  # HARD
        return (
            0.5 * engagement +
            0.2 * value_align +
            0.1 * diversity -
            0.2 * toxicity -
            0.1 * state.fatigue
        )