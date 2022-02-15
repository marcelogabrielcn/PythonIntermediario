def hello():
    return 'Hello World!'


def mestre(func):
    return func()


var = mestre(hello)
print(var)
