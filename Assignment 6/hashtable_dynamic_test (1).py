import unittest
from hashtable_dynamic import *

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.table = HashTable()

    def test_get_not_in_table(self):
        self.assertIsNone(self.table.get('123-123-1234')[0])

    def test_put(self):
        self.table.put('123-123-1234', 'John Doe')

    def test_get_in_table(self):
        self.table.put('123-123-1234', 'John Doe')
        self.assertEqual('John Doe', self.table.get('123-123-1234')[0])

    def test_put_none(self):
        self.table.put('123-123-1234', None)
        self.assertIsNone(self.table.get('123-123-1234')[0])

    def test_put_replace(self):
        self.table.put('123-123-1234', 'John Doe')
        self.assertEqual('John Doe', self.table.get('123-123-1234')[0])
        self.table.put('123-123-1234', 'Jane Smith')
        self.assertEqual('Jane Smith', self.table.get('123-123-1234')[0])

    def test_put_collision(self):
        self.table.put('459-741-0153', 'John Smith')
        self.table.put('222-705-9567', 'Robert Jones')
        self.assertEqual('John Smith', self.table.get('459-741-0153')[0])
        self.assertEqual('Robert Jones', self.table.get('222-705-9567')[0])

    def test_len(self):
        self.assertEqual(0, len(self.table))
        self.table.put('390-296-6413', 'John Smith')
        self.assertEqual(1, len(self.table))
        self.table.put('422-634-0074', 'Robert Jones')
        self.assertEqual(2, len(self.table))

    def test_in(self):
        self.assertFalse('390-296-6413' in self.table)
        self.table.put('390-296-6413', 'John Smith')
        self.assertTrue('390-296-6413' in self.table)

    def test_del_not_in_table(self):
        try:
            del self.table['390-296-6413']
        except Exception:
            self.fail("test_del_not_in_table raised exception")

    def test_del_in_table(self):
        self.table.put('459-741-0153', 'John Smith')
        self.table.put('222-705-9567', 'Robert Jones')

        self.assertTrue('459-741-0153' in self.table)
        del self.table['459-741-0153']
        self.assertFalse('459-741-0153' in self.table)
        self.assertTrue('222-705-9567' in self.table)
        self.assertEqual('Robert Jones', self.table.get('222-705-9567')[0])

    def test_getitem(self):
        self.table.put('390-296-6413', 'John Smith')
        self.assertEqual('John Smith', self.table['390-296-6413'][0])

    def test_setitem(self):
        self.table['390-296-6413'] = 'John Smith'
        self.assertEqual('John Smith', self.table['390-296-6413'][0])


if __name__ == '__main__':
    unittest.main(verbosity=2)

