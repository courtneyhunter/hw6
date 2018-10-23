import re
import unittest

def sumNums(fileName):
    f = open(fileName)
    sum = 0
    for line in f:
        line = line.rstrip()
        num = re.findall("[0-9]+", line)
        for n in num:
            sum += int(n)

    f.close()
    return sum


def countWord(fileName, word):
    f = open(fileName)
    count = 0
    for line in f:
        line = line.rstrip()
        x = re.findall(r"\b" + word + r"\b", line, re.IGNORECASE)
        count += len(x)
    return count


def listURLs(fileName):
        f = open(fileName)
        url = []
        for line in f:
            line = line.rstrip()
            x = re.findall(r"www." + ".*" + r"." + "...", line)
            for u in x:
                url.append(u)
        return url


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
