def getSum(a, b):
    return a + b

def mutateData(data):
    checking_words = ['fuck', 'suck']

    if data in checking_words:
        return 'censored'.upper()
    return "The length of {} is {}".format(data, len(data))