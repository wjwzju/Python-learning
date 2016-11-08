from operator import itemgetter

c = [('bat', 2), ('mat', 1), ('cat', 3)]
# sorted(c, key=itemgetter(1), reverse=True)
c.sort(key=itemgetter(1,0), reverse=True)

print c
