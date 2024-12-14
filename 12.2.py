
import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()

class TournamentTest(TestCase):
    def setUpClass(self):
        all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrei = Runner("Андрей", speed=9)
        self.runner_nick = Runner("Ник", speed=3)

    def tearDownClass(self, all_results=None):
        for result in all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results["Usain vs Nick"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_andrei_and_nick(self):
        tournament = Tournament(90, self.runner_andrei, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results["Andrei vs Nick"] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_usain_andrei_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results["Usain vs Andrei vs Nick"] = {place: str(runner) for place, runner in
                                                                 results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    if __name__ == "__main__":
        unittest.main()


