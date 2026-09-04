import unittest
from shelltools import split_command
class Tests(unittest.TestCase):
 def test_split(self): self.assertEqual(split_command("echo 'hello world'"),['echo','hello world'])
if __name__=='__main__': unittest.main()
