import unittest

from src.energyhub.setgame.card import Card
from src.energyhub.setgame.set_game_solver import SetGameSolver


class SetGameSolverTests(unittest.TestCase):
    def setUp(self):
        self.solver = SetGameSolver()

    def test_solver_different(self):
        result = self.solver.solve([
            Card({
                "color": "blue",
            }),
            Card({
                "color": "red",
            }),
            Card({
                "color": "purple",
            }),
            Card({
                "color": "yellow",
            })
        ], 3)

        self.assertEqual(4, len(result))

    def test_solver_same(self):
        result = self.solver.solve([
            Card({
                "color": "red",
            }),
            Card({
                "color": "red",
            }),
            Card({
                "color": "red",
            }),
            Card({
                "color": "red",
            })
        ], 3)

        self.assertEqual(4, len(result))

    def test_solver_no_match(self):
        result = self.solver.solve([
            Card({
                "color": "blue",
            }),
            Card({
                "color": "blue",
            }),
            Card({
                "color": "purple",
            }),
            Card({
                "color": "purple",
            })
        ], 3)

        self.assertEqual(0, len(result))

    def test_solver_found(self):
        result = self.solver.solve([
            Card({
                "color": "blue",
                "number": 2,
                "shape": "circle",
                "shading": "none",
                "texture": "smooth"
            }),
            Card({
                "color": "red",
                "number": 3,
                "shape": "circle",
                "shading": "some",
                "texture": "bumpy"
            }),
            Card({
                "color": "purple",
                "number": 4,
                "shape": "circle",
                "shading": "much",
                "texture": "prickly"
            }),
            Card({
                "color": "yellow",
                "number": 3,
                "shape": "circle",
                "shading": "much",
                "texture": "bumpy"
            })
        ], 3)

        self.assertEqual(1, len(result))
        self.assertEqual(3, len(result[0]))

    def test_solver_no_set(self):
        result = self.solver.solve([
            Card({
                "color": "blue",
                "number": 2,
                "shape": "circle",
                "shading": "none"
            }),
            Card({
                "color": "red",
                "number": 3,
                "shape": "square",
                "shading": "some"
            }),
            Card({
                "color": "purple",
                "number": 4,
                "shape": "circle",
                "shading": "much"
            })
        ], 3)

        self.assertEqual(0, len(result))
