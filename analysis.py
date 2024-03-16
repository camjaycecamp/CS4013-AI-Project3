# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    """ answerNoise = 0.2 """
    # set noise to 0, reducing massively negative incentives resulting from possible transitions to pitfall states
    answerNoise = 0.0 
    return answerDiscount, answerNoise

"""
    Prefer the close exit (+1), risking the cliff (-10)
"""
def question3a():
    answerDiscount = 0.9 # slightly incentivize pursuing rewards sooner
    answerNoise = 0.0 # provide no incentive to avoid risky behavior
    answerLivingReward = -4.0 # massively disincentivize chasing farther exits or playing for a longer period of time
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

"""
    Prefer the close exit (+1), but avoiding the cliff (-10)
"""
def question3b():
    answerDiscount = 0.4 # heavily encourage pursuing rewards ASAP
    answerNoise = 0.2 # somewhat disincentivize risky moves
    answerLivingReward = -3.0 # heavily disincentivize chasing farther exits or playing for a longer period of time
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

"""
    Prefer the distant exit (+10), risking the cliff (-10)
"""
def question3c():
    answerDiscount = 0.9 # slightly incentivize pursuing rewards sooner
    answerNoise = 0.0 # provide no incentive to avoid risky behavior
    answerLivingReward = 0.0 # provide no incentive to chase closer exits or minimize playtime
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

"""
    Prefer the distant exit (+10), avoiding the cliff (-10)
"""
def question3d():
    answerDiscount = 0.9 # slightly incentivize pursuing rewards sooner
    answerNoise = 0.2 # somewhat disincentivize risky moves
    answerLivingReward = 0.0 # provide no incentive to chase closer exits or minimize playtime
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

"""
    Avoid both exits and the cliff (so an episode should never terminate)
"""
def question3e():
    answerDiscount = 0.0 # completely evaporate any incentive to pursue an exit
    answerNoise = 0.2 # provide no incentive to avoid risky behavior
    answerLivingReward = 1.0 # provide incentive to simply stay alive for as long as possible
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    answerEpsilon = 0.05
    answerLearningRate = 0.8
    answerAlpha = 0.2
    return answerEpsilon, answerAlpha, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))