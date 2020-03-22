import random

class Slot_machine():
    """ a simple slot machine """

    def __init__(self, mean):
        """

        :param mean: actual win rate
        mean_estimate: current mean estimate
        N: number of plays a the slot machine
        """
        self.mean = mean
        self.mean_estimate = 0
        self.N = 0
        self.x = 0

    def pull(self):
        """ modeled pull operation in a slot machine """
        self.x = self.mean + random.gauss(0,0.05)
        self.update()
        return self.x

    def update(self):
        """ updates mean estimate and tracks number of pulls """
        self.N += 1
        self.mean_estimate = (1.0 - (1.0 / self.N)) * self.mean_estimate + (1.0 / self.N) * self.x


# exploration is 5%
eps = 0.05

# Instantiated 3 slot machines
sm1 = Slot_machine(0.5)
sm2 = Slot_machine(0.3)
sm3 = Slot_machine(0.1)

all_sm = [sm1, sm2, sm3]

# randomly selection for initial sm
current_best_sm = random.choice(all_sm)

# records actual mean values of pulled slot machines
all_pulls = []

# records random values generated that decide between exploration / exploitation
all_values = []

for _ in range(1000):
    value = random.uniform(0,1)
    all_values.append(value)

    if value < eps:
        random_sm = random.choice(all_sm)
        random_sm.pull()
        if random_sm.mean_estimate > current_best_sm.mean_estimate:
            current_best_sm = random_sm
        all_pulls.append(random_sm.mean)

    else:
        current_best_sm.pull()
        all_pulls.append(current_best_sm.mean)

print(all_values)
print(all_pulls)





