import unittest
from app import add,subs,multi

class Testmathfunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,4),7)
    
    def test_subs(self):
        self.assertEqual(subs(3,6),-3)
    
    def test_multi(self):
        self.assertEqual(multi(3,0),0)

if __name__ == '__main__':
    unittest.main()