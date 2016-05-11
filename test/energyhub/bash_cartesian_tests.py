import unittest

from src.energyhub.bashcartesian.bash_cartesian import BashCartesian


class BashCartesianTest(unittest.TestCase):
    def setUp(self):
        self.bashCartesian = BashCartesian()

    def test_nested_expansion(self):
        self.assertEqual(["abijk", "abijl", "acdgijk", "acdgijl", "acegijk", "acegijl", "acfgijk", "acfgijl", "ahijk", "ahijl"], self.bashCartesian.parse("a{b,c{d,e,f}g,h}ij{k,l}"))

    def test_simple_case(self):
        self.assertEqual(["abcdefg"], self.bashCartesian.parse("abcdefg"))

    def test_one_split(self):
        self.assertEqual(["aaaacc", "aabbcc"], self.bashCartesian.parse("aa{aa,bb}cc"))

    def test_single_value_split(self):
        self.assertEqual(["aabb"], self.bashCartesian.parse("aa{bb}"))

    def test_adjacent_splits(self):
        self.assertEqual(["aabbccff", "aabbccee", "aabbddff", "aabbddee"], self.bashCartesian.parse("aa{bb}{cc,dd}{ff,ee}"))

    def test_many_values_splits(self):
        self.assertEqual(["aabb", "aacc", "aadd", "aaee", "aaff"], self.bashCartesian.parse("aa{bb,cc,dd,ee,ff}"))

    def test_splits_beginning(self):
        self.assertEqual(["aacc", "bbcc"], self.bashCartesian.parse("{aa,bb}cc"))
