import unittest
import business.teams
import business.players

from storage.memory import MemoryStorage


class Tests(unittest.TestCase):

    def test_create_team(self):

        team = business.teams.Team(name="test")
        teambll = business.teams.Business(MemoryStorage())

        result = teambll.create_team(team=team)

        self.assertIsNotNone(result.id)
        self.assertEqual(result.name, team.name)

    def test_assign_players(self):

        team = business.teams.Team(name="test")
        teambll = business.teams.Business(MemoryStorage())

        created_team = teambll.create_team(team=team)

        player = business.players.Player(name="test")
        result = teambll.assign_player(team.id , player.id)

        self.assertEqual(result, True)

    def test_get_team_by_name(self):

        memory = MemoryStorage()
        memory.map["bar"] = business.teams.Team(name="foo")

        teambll = business.teams.Business(memory)

        result = teambll.get_team(name="foo")

        self.assertEqual(result, memory.map["bar"])

    def test_get_team_by_id(self):

        memory = MemoryStorage()
        memory.map["bar"] = business.teams.Team(name="foo")

        teambll = business.teams.Business(memory)

        result = teambll.get_team(id="bar")

        self.assertEqual(result, memory.map["bar"])