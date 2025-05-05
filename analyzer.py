# analyzer class
from die import Die
from game import Game
import pandas as pd
import numpy as np

class Analyzer():
	"""
	A class to analyze a games die roll results. 
	"""
	def __init__(self, game_obj):
		"""
		Initialize an Analyzer object with a Game object. 
		
		Inputs: A Game object. 
		
		Implications/Outputs: Creates an analyzer object.
		"""
		if isinstance(game_obj, Game) != True:
			raise ValueError("Must be Game object")
		self.game_obj = game_obj
	
	def jackpot(self):
		"""
		Calculates the number of times a where the roll results in all faces being the same.
		
		Inputs: None. 
		
		Implications/Outputs: Outputs the number of jackpots within the game.
		"""
		return (self.game_obj.current_play().nunique(axis=1) == 1).sum()
	
	def face_counts(self):
		"""
		Computes how many times a given face is rolled in each event.
		
		Inputs: None.
		
		Implications/Outputs: Returns a dataframe with the roll number as the index, face values as columns, and count values in the cell.
		"""
		wide_results = self.game_obj.current_play().reset_index()
		narrow_results = wide_results.melt(id_vars = "index", var_name = "die", value_name = "face")
		grouped_results = narrow_results.groupby(["index", "face"]).size().unstack(fill_value = 0)
		grouped_results.index.name = None
		grouped_results.columns.name = None
		return grouped_results
		
	def combo_count(self):
		"""
		Computes the distinct combinations of faces rolled, along with their counts.
		
		Inputs: None.
		
		Implications/Outputs: Returns a dataframe with a MultiIndex of distinct combinations and a column for the associated counts.
		"""
		sorted_results = pd.DataFrame(np.sort(self.game_obj.current_play().values, axis = 1))
		return sorted_results.groupby(list(sorted_results.columns)).size().to_frame(name = "count")
		
	def permutation_count(self):
		"""
		Computes the distinct permutations of faces rolled, along with their counts.
		
		Inputs: None.
		
		Implications/Outputs: Returns a dataframe with a MultiIndex of distinct permutations and a column for the associated counts.
		"""
		results = self.game_obj.current_play()
		return results.groupby(list(results.columns)).size().to_frame(name = "count")
		