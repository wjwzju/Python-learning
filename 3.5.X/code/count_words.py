"""Count words."""
from operator import itemgetter


class Word:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __repr__(self):
        return repr((self.word, self.count))


def numeric_compare(x, y):
    if x[1] < y[1]:
        return -1
    if x[1] > y[1]:
        return 1
    if x[1] == y[1]:
        if x[0] < y[0]:
            return -1
        if x[0] > y[0]:
            return 1
        if x[0] == y[0]:
            return 0


def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s
    words = s.split()
    d = {}
    c = []
    for word in words:
        d[word] = 0
    for word in words:
        d[word] += 1
    for k, v in d.items():
        c.append((k, v))
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    # sorted(c, key=lambda x: x[1], reverse=True)
    # sorted(c, key=lambda x: x[0], reverse=True)
    # c.sort(key=itemgetter(1, 0), reverse=True)
    c.sort(cmp=numeric_compare)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = c[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
