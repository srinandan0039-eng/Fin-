import random

class FinEnv:
    def __init__(self):
        self.balance = 0
        self.income = 0
        self.expenses = 0
        self.savings = 0
        self.risk = 0

    def reset(self):
        self.balance = random.randint(2000, 10000)
        self.income = random.randint(1000, 5000)
        self.expenses = random.randint(1000, 6000)
        self.savings = random.randint(500, 5000)
        self.risk = random.randint(1, 5)

        return self._get_state()

    def step(self, action):
        reward = 0

        # Random real-life event
        event = random.choice(["none", "expense", "bonus"])

        if event == "expense":
            self.balance -= 500
        elif event == "bonus":
            self.balance += 500

        # Actions
        if action == "cut_expenses":
            self.expenses -= 200
            reward += 1

        elif action == "increase_income":
            self.income += 300
            reward += 1

        elif action == "save_money":
            if self.balance > 500:
                self.savings += 300
                self.balance -= 300
                reward += 1
            else:
                reward -= 1

        elif action == "invest_money":
            if self.balance > 500:
                outcome = random.choice(["profit", "loss"])
                if outcome == "profit":
                    self.balance += 500
                    reward += 2
                else:
                    self.balance -= 400
                    reward -= 1
            else:
                reward -= 1

        else:
            reward -= 1  # invalid action

        # Update balance
        self.balance += self.income - self.expenses

        # Risk adjustment
        if self.expenses > self.income:
            self.risk += 1
            reward -= 1
        else:
            self.risk = max(1, self.risk - 1)

        # Done condition
        done = self.balance <= 0 or self.savings >= 10000

        return self._get_state(), reward, done

    def _get_state(self):
        return {
            "balance": self.balance,
            "income": self.income,
            "expenses": self.expenses,
            "savings": self.savings,
            "risk": self.risk
        }