from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def users(self, param):
        return Chain('%s/%s' % (self._path, param))


#print(Chain().users('troy').hehe.lala.wawa)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
