import unittest

from main.block import Block


class BlockTest(unittest.TestCase):
    def test_block_str(self):
        block = Block(0, 1, "{'msg':'hallo'}", "aa==")
        self.assertEqual(str(block), "01{'msg':'hallo'}aa==", "wrong __str__")

    def test_block_hash(self):
        block = Block(0, 1, "{'msg':'hallo'}", "aa==")
        hs = block.hash_block()
        print(hs)
        self.assertIsNotNone(hs, "null hash")


if __name__ == '__main__':
    unittest.main()
