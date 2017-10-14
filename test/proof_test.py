import unittest

from main.proof import is_good, do_proof


class ProofTest(unittest.TestCase):
    def test_verify(self):
        self.assertTrue(is_good('yrw6T6596icnddcUTWaxBF4UpiRcX0XF8224'), 'wrong PoW')

    def test_do_proof(self):
        proof = do_proof(0)
        print(proof)
        self.assertIsNotNone(proof, 'invalid proof')


if __name__ == '__main__':
    unittest.main()
