from Numberlink import *
import time
import math
import random


def randomPolicy():  # define random child selection


class MCTS:
    def __init__(self, timeLimit=None, iterationLimit=None, rolloutPolicy=randomPolicy):
        if timeLimit != None:
        if iterationLimit != None:
            raise ValueError("Cannot have both a time limit and an iteration limit")
           # time taken for each MCTS search in milliseconds
        self.timeLimit = timeLimit
        self.limitType = 'time'
        else:
        if iterationLimit == None:
            raise ValueError("Must have either a time limit or an iteration limit")
           # number of iterations of the search
        if iterationLimit < 1:
            raise ValueError("Iteration limit must be greater than one")
        self.searchLimit = iterationLimit
        self.limitType = 'iterations'
        self.rollout = rolloutPolicy

    def search(self, initialState):
        initialState.reset()
        if self.limitType == 'time':
            timeLimit = time.time() + self.timeLimit / 1000
            while time.time < timeLimit:
                self.mcts(initialState)
        else:
            for i in range(self.searchLimit):
                self.mcts(initialState)
        bestChild = self.bestChild(initialState)

    def mcts(self, state):
        node = self.selection(state)
        expanded_node = self.expansion(node)
        simulationResult = self.simulation(expanded_node)
        self.backpropagation(simulationResult, expanded_node)

    def selection(self, state):
        while !state.isTerminal() and state.inTree:  # looping while picking child with best Upper Confidence Tree value
            return self.getBestChild(state)
        return state

    def expansion(self, state):
        if not state.inTree:
            state.inTree = True
            state.statistics = Numberlink.createNewStatistic()
        return state

    def simulation(self, state):
        while(!state.isTerminal()):
            state = state.getRandomChild()
