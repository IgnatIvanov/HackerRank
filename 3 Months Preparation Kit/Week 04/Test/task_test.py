import unittest


def task(s):    
       
    if len(s) % 2 == 1:
        return -1          
    
    for_change = 0
    _left = s[:len(s) // 2]
    _right = s[len(s) // 2:]
    
    for letter in _left:
        if letter not in _right:
            for_change += 1
        else:
            _right = _right.replace(letter, '1', 1)
    
    return for_change

class TestTask2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task('aaabbb'), 3, "Should be 3")
    def test_2(self):
        self.assertEqual(task('ab'), 1, "Should be 1")
    def test_3(self):
        self.assertEqual(task('abc'), -1, "Should be -1")
    def test_4(self):
        self.assertEqual(task('mnop'), 2, "Should be 2")
    def test_5(self):
        self.assertEqual(task('xyyx'), 0, "Should be 0")
    def test_6(self):
        self.assertEqual(task('xaxbbbxx'), 1, "Should be 1")
    def test_7(self):
        self.assertEqual(task('fdhlvosfpafhalll'), 5, "Should be 5")
if __name__ == '__main__':
    unittest.main()
