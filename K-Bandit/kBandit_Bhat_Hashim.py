import numpy as np
import matplotlib.pyplot as plt
import random
import math

def getSamplar():
    mu = np.random.normal(0, 10)
    sd = abs(np.random.normal(5, 2))
    getSample = lambda: np.random.normal(mu, sd)
    return getSample


def e_greedy(Q, e):
    maximize = [keys for keys, values in Q.items() if values == max(Q.values())]
    if len(maximize) == 1:
        choose = maximize[0]
    elif len(maximize) > 1:
        choose = random.choice(maximize)
    choose2 = random.choice(list(Q.keys()))
    action = random.choices(population=[choose, choose2], weights=[1 - e, e])
    action = action[0]
    return action


def upperConfidenceBound(Q, N, c):
    tempfunc = []
    for i in range(len(Q)):
        if list(N.values())[i] == 0:
            tempfunc.append(math.inf)
        else:
            tempfunc2 = math.sqrt(np.log(i + 1) / list(N.values())[i])
            tempfunc3 = list(Q.values())[i] + c * tempfunc2
            tempfunc.append(tempfunc3)
    tempfunc4 = [i for i, x in enumerate(tempfunc) if x == max(tempfunc)]
    if len(tempfunc4) == 1:
        index = tempfunc4[0]
    elif len(tempfunc4) > 1:
        index = random.choice(tempfunc4)
    action = list(Q.keys())[index]
    return action


def updateQN(action, reward, Q, N):
    New_N = N.copy()
    New_Q = Q.copy()

    tempfunc = N[action]
    dictionary = {action: (int(tempfunc)+1)}
    New_N.update(dictionary)

    new_mean = Q[action] + (reward - Q[action])/(New_N[action])
    if new_mean % 1 == 0:
        new_mean = int(new_mean)
    up_dict2 = {action: new_mean}
    New_Q.update(up_dict2)
    return New_Q, New_N


def decideMultipleSteps(Q, N, policy, bandit, maxSteps):
    actionReward = []
    for i in range(maxSteps):

        action = policy(Q, N)
        reward = bandit(action)
        temp = updateQN(action, reward, Q, N)
        Q = temp[0]
        N = temp[1]
        actionReward.append((action, reward))
    return {'Q': Q, 'N': N, 'actionReward': actionReward}


def plotMeanReward(actionReward, label):
    maxSteps = len(actionReward)
    reward = [reward for (action, reward) in actionReward]
    meanReward = [sum(reward[:(i + 1)]) / (i + 1) for i in range(maxSteps)]
    plt.plot(range(maxSteps), meanReward, linewidth=0.9, label=label)
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')


def main():
    np.random.seed(2020)
    random.seed(2020)
    K = 10
    maxSteps = 1000
    Q = {k: 0 for k in range(K)}
    N = {k: 0 for k in range(K)}
    testBed = {k: getSamplar() for k in range(K)}
    bandit = lambda action: testBed[action]()

    policies = {}
    policies["e-greedy-0.5"] = lambda Q, N: e_greedy(Q, 0.5)
    policies["e-greedy-0.1"] = lambda Q, N: e_greedy(Q, 0.1)
    policies["UCB-2"] = lambda Q, N: upperConfidenceBound(Q, N, 2)
    policies["UCB-20"] = lambda Q, N: upperConfidenceBound(Q, N, 20)

    allResults = {name: decideMultipleSteps(Q, N, policy, bandit, maxSteps) for (name, policy) in policies.items()}

    for name, result in allResults.items():
        plotMeanReward(allResults[name]['actionReward'], label=name)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.show()


if __name__ == '__main__':
    main()
