from unittest import TestCase

def increment_dictionary_values (d, i):

"""
Dicts are mutable within Python, meaning that modifying the dict within the function will change the dict data globally (producing a false result).

To solve this, a temporary copy is created using the dict() method.
"""

    d_temp = dict(d) #Local dict copy created

    for k, v in d_temp.items(): #Function remains as it was previously, but performs its operations on the copy.
        d_temp[k] = v + i
    return d_temp

class TestIncrementDictionaryValues (TestCase):

    def test_increment_dictionary_values (self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)