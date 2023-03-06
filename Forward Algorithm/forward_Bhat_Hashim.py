def expect(xDistribution, function):
    fxProduct = [px * function(x) for x, px in xDistribution.items()]
    expectation = sum(fxProduct)
    return expectation


def forward(xT_1Distribution, eT, transitionTable, sensorTable):
    forwardsum = []

    for j in range(len(xT_1Distribution)):
        values_sens = list(sensorTable.keys())[j]
        listvals = list(sensorTable.values())[j]
        out = 0

        for i in range(len(transitionTable)):
            valstransit = list(transitionTable.keys())[i]
            transitkeys = transitionTable.get(valstransit)
            transitsens = transitkeys.get(values_sens)
            out += (list(xT_1Distribution.values())[i] * listvals.get(eT) * transitsens)
        maketuple = tuple([values_sens, out])
        forwardsum.append(maketuple)

    dictsum = dict(forwardsum)
    summation = sum(list(dictsum.values()))
    finalvalue = []
    for t in range(len(dictsum)):
        createtuple = tuple([forwardsum[t][0], forwardsum[t][1] / summation])
        finalvalue.append(createtuple)
    finalvalue = dict(finalvalue)
    return finalvalue


def main():
    pX0 = {0: 0.1, 1: 0.9}
    e = 20
    transitionTable = {0: {0: 0.3, 1: 0.7}, 1: {0: 0.5, 1: 0.5}}
    sensorTable = {0: {0: 0.3, 1: 0.1, 2: 0.6}, 1: {0: 2, 1: 0.7, 2: 0.1}}

    xTDistribution = forward(pX0, e, transitionTable, sensorTable)
    print(xTDistribution)


if __name__ == "__main__":
    main()

