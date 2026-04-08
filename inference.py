from openenv import FinEnv

env = FinEnv()

def run():
    state = env.reset()
    total_reward = 0

    for _ in range(15):
        # Simple intelligent strategy
        if state["expenses"] > state["income"]:
            action = "cut_expenses"
        elif state["balance"] > 2000:
            action = "invest_money"
        elif state["savings"] < 2000:
            action = "save_money"
        else:
            action = "increase_income"

        state, reward, done = env.step(action)
        total_reward += reward

        if done:
            break

    return {
        "final_state": state,
        "total_reward": total_reward
    }

if __name__ == "__main__":
    result = run()
    print(result)