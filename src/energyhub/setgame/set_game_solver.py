from typing import List

from src.energyhub.setgame.card import Card


class SetGameSolver:
    def solve(self, cards: List[Card], set_size: int) -> List[List[Card]]:
        found = []

        self._solve(cards, [], set_size, found)

        return found

    def _solve(self, cards_remaining: List[Card], candidate: List[Card], set_size: int, found: List[List[Card]]):
        if len(candidate) < set_size and len(cards_remaining) > 0:
            card = cards_remaining.pop(0)
            copy = cards_remaining.copy()
            self._solve(copy, candidate.copy(), set_size, found)  # skip case

            candidate.append(card)

            if self.is_valid(candidate):
                self._solve(cards_remaining, candidate, set_size, found)
        else:
            if self.is_valid(candidate) and len(candidate) == set_size:
                found.append(candidate.copy())

    def is_valid(self, cards: List[Card]) -> bool:
        if len(cards) < 2:
            return True

        dims = cards[0].dimensions.keys()

        valid = True
        for dim in dims:

            sameness = set()
            for card in cards:
                sameness.add(card.dimensions[dim])

            dim_valid = len(sameness) == 1 or len(sameness) == len(cards)
            valid = valid and dim_valid

        return valid
