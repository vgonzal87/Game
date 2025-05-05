import unittest
from die import Die
from game import Game
from analyzer import Analyzer
import numpy as np
import pandas as pd

class DieTestSuite(unittest.TestCase):
	def test_die_init(self):
		die_test = Die(np.array([1]))
		self.assertIsInstance(die_test, Die)
	def test_die_change_weight(self):
		die_test = Die(np.array([1]))
		die_test.change_weight(1,0.5)
		self.assertEqual(die_test.current_state().index[0], 0.5)
	def test_die_roll(self):
		die_test = Die(np.array([1]))
		self.assertEqual(die_test.roll_die(), [1])
	def test_current_state(self):
		die_test = Die(np.array([1]))
		self.assertIsInstance(die_test.current_state(), pd.DataFrame)
		
class GameTestSuite(unittest.TestCase):
	def test_game_init(self):
		die_test = Die(np.array([1]))
		game_test = Game([die_test])
		self.assertIsInstance(game_test, Game)
	def test_game_play(self):
		die_test = Die(np.array([1]))
		game_test = Game([die_test])
		game_test.play(4)
		self.assertEqual(game_test.current_play().shape, (4,1))
	def test_current_play_narrow(self):
		die_test = Die(np.array([1]))
		game_test = Game([die_test])
		game_test.play(4)
		self.assertEqual(len(game_test.current_play("narrow").index.levels), 2)

class AnalyzerTestSuite(unittest.TestCase):
	def test_analyzer_init(self):
		die_test = Die(np.array([1]))
		game_test = Game([die_test])
		analyzer_test = Analyzer(game_test)
		self.assertIsInstance(analyzer_test, Analyzer)
	def test_jackpot(self):
		die_test = Die(np.array([1]))
		game_test = Game([die_test])
		game_test.play(4)
		analyzer_test = Analyzer(game_test)
		self.assertEqual(analyzer_test.jackpot(),4)
	def test_face_counts(self):
		die_test = Die(np.array([1]))
		game_test = Game([die_test])
		game_test.play(4)
		analyzer_test = Analyzer(game_test)
		self.assertEqual(analyzer_test.face_counts()[1].sum(),4)
	def test_combo_count(self):
		die_test = Die(np.array([1]))
		game_test = Game([die_test])
		game_test.play(4)
		analyzer_test = Analyzer(game_test)
		self.assertEqual(analyzer_test.combo_count().shape, (1,1))
	def test_permutation_count(self):
		die_test = Die(np.array([1]))
		game_test = Game([die_test])
		game_test.play(4)
		analyzer_test = Analyzer(game_test)
		self.assertEqual(analyzer_test.permutation_count().iloc[0,0], 4)
	
		
if __name__ == '__main__':
	unittest.main(verbosity=3)