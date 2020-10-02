from math import sqrt


class Statistics:
    def __init__(self, simulations, value):
        self.simulations = simulations  # number of simulations
        self.value = value  # exploitation term
        self.best_value = value

    def compareTo(self, x):
        if self.value < x.value:
            return -1
        else:
            return 1

    def compareToBest(self, x):
        if self.best_value < x.best_value:
            return -1
        else:
            return 1

    def compare_UCT(self, x, parent_simulations):
        u1 = self.value + sqrt(2 * parent_simulations / self.simulations)  # exploration constant= sqrt(2)
        u1 = x.value + sqrt(2 * parent_simulations / x.simulations)
        if u1 < u2:
            return -1
        else:
            return 1
