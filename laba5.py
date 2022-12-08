f = open('laba5/test.txt', 'r', encoding = 'utf-8')
print(*f)
import collections
f = open('laba5/test.txt', 'r', encoding = 'utf-8')
def countLiteras():
    results = collections.Counter(f.read())
    return (results)
print(countLiteras())