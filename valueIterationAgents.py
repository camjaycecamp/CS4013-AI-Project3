# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        """
            this method handles the recursive iteration of values for all states within
            the MDP until each state reflects its optimal expected utility
        """
        # loop over each value iteration without regard for the iteration itself as a variable
        for _ in range(self.iterations): 
            newval = util.Counter() # temp for updated values
            for state in self.mdp.getStates(): # iterate through each possible state of the current iteration
                if not self.mdp.isTerminal(state): # check if the state is terminal
                    # if state isn't terminal, compute max utility (qval) of all actions in the current state
                    # qval is computed from the qvals of all state-action pairs
                    # actions of state-actions pairs are retrieved directly from the state itself
                    maxval = max([self.computeQValueFromValues(state, action) for action in \
                    self.mdp.getPossibleActions(state)])
                    # max utility of state is updated accordingly before visiting next state in iteration
                    newval[state] = maxval
            self.values = newval # all states are updated to reflect results of current iteration


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        """
            this method finds the qval of an action within a given state, and is used by runValueIteration
            for that exact purpose

            essentially fulfills the qval portion of the value iteration formula, representing the values
            of all possible actions that could occur from a given state with respect to factors like 
            irrationality and immediate reward
        """
        qval = 0 # initialize qval of given action in state
        # iterate over each possible action in the given state (state-action pair)
        for nextState, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            # get imm. reward of performing given action
            reward = self.mdp.getReward(state, action, nextState)
            # find product of transition prob. and sum of imm. reward and discounted value of resulting state
            # add result to aggregation of qvals of all possible actions from given state
            # essentially a functional implementation of qval formula 
            qval += prob * (reward + self.discount * self.values[nextState])
        return qval # return qval of state-action pair to calling method
        # util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        """
            this method finds the best action for a given state to take with respect to the most
            recent value estimates

            essentially fulfills the max portion of the value iteration formula, representing the
            choice of the best value associated with an action within the given state and thus
            selecting that action as the preferred course to take in the set of current value estimates
        """
        # if the given state is terminal, there's nothing to be done here
        if self.mdp.isTerminal(state):
            return None
        # find all possible actions that can be taken from given state
        actions = self.mdp.getPossibleActions(state)
        # find action with highest qval and assign it as best action for given state
        best_action = max(actions, key=lambda action: self.computeQValueFromValues(state, action))
        return best_action # return best possible action for given state to calling method
        # util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


class PrioritizedSweepingValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
