def expect(xDistribution, function):
    expectation = sum({function(key)*value for (key, value) in xDistribution.items()})
    return expectation


def getVariance(xDistribution):
    tempfunct = lambda x: x
    e_x = expect(xDistribution, tempfunct)
    tempDict = {((key - e_x) ** 2): value for (key, value) in xDistribution.items()}
    variance = expect(tempDict, tempfunct)
    return variance


def main():
    xDistributionExample1 = {1: 1 / 5, 2: 2 / 5, 3: 2 / 5}
    functionExample1 = lambda x: x ** 2
    print(expect(xDistributionExample1, functionExample1))
    print(getVariance(xDistributionExample1))

    xDistributionExample2 = {1: 1 / 6, -1 / 2: 1 / 3, 1 / 3: 1 / 4, -1 / 4: 1 / 12, 1 / 5: 1 / 6}
    functionExample2 = lambda x: 1 / x
    print(expect(xDistributionExample2, functionExample2))
    print(getVariance(xDistributionExample2))


if __name__ == '__main__':
    main()

