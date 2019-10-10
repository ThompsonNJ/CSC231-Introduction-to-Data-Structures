import unittest
from hashtable import *

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
        self.table.put('390-296-6413', 'John Smith')
        self.table.put('422-634-0074', 'Robert Jones')
        self.table.put('325-975-9795', 'Sam Spade')
        self.assertEqual('John Smith', self.table.get('390-296-6413')[0])
        self.assertEqual('Robert Jones', self.table.get('422-634-0074')[0])
        self.assertEqual('Sam Spade', self.table.get('325-975-9795')[0])

    def test_put_out_of_memory(self):
        table = HashTable(2)
        table.put('390-296-6413', 'John Smith')
        table.put('422-634-0074', 'Robert Jones')

        self.assertEqual(table.size, len(table))
        with self.assertRaises(RuntimeError):
            table.put('325-975-9795', 'Sam Spade')

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
        self.table.put('390-296-6413', 'John Smith')
        self.assertTrue('390-296-6413' in self.table)
        del self.table['390-296-6413']
        self.assertFalse('390-296-6413' in self.table)

    def test_getitem(self):
        self.table.put('390-296-6413', 'John Smith')
        self.assertEqual('John Smith', self.table['390-296-6413'][0])

    def test_setitem(self):
        self.table['390-296-6413'] = 'John Smith'
        self.assertEqual('John Smith', self.table['390-296-6413'][0])

if __name__ == '__main__':
    unittest.main(verbosity=2)

