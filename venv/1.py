from math import *

nsDict = {'global': None}
varDict = {}


def create(a, b):
    nsDict[a] = b


def add(a, b):
    varDict[a] = b


def get(prostr, per):
    # x = varDict.get(a)
    # print(x)
    res = False
    for k in varDict:
        if (k == prostr and varDict[k] == per):
            res = True
            print(k)
    if (res == False):
        if (nsDict[prostr] is None):
            print('None')
        else:
            get(nsDict[prostr], per)


kol = int(input())
for i in range(kol):
    cmd, ns, var = input().split()
    if (cmd == 'create'):
        create(str(ns), str(var))
    if (cmd == 'add'):
        add(str(ns), str(var))
    if (cmd == 'get'):
        get(str(ns), str(var))

print(nsDict)
print(varDict)