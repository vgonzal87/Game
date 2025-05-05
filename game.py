# game class 
from die import Die
import pandas as pd
import numpy as np

class Game():
	"""
	A class to simulate a game with one or more dice. 
	"""
	def __init__(self, die_list):
		"""
		Initialize a Game object with a list of Die objects. 
		
		Inputs: A list containing similar dice. 
		
		Implications/Outputs: Creates a game object that can be rolled.
		"""
		self.die_list = die_list
		
	def play(self, num_rolls):
		"""
		Creates a play by rolling the die in the list N times and puts the results into a private dataframe
		
		Inputs: Number of times to roll the dice 
		
		Implications/Outputs: Creates dataframe with the index as the roll number, the columns as the die number, and the values of each roll. 
		"""
		rolls = [i.roll_die(num_rolls) for i in self.die_list]
		self.__play_out = pd.DataFrame(columns = range(num_rolls), index = range(len(self.die_list)), data = rolls)
		self.__play_out = self.__play_out.T
	
	def current_play(self, which_form = "wide"):
		"""
		Outputs a copy of the private game dataframe showing the current play.     
		
		Inputs: "wide" or "narrow" for the format of the dataframe to be outputted
		
		Implications/Outputs: Returns a copy of the private game dataframe in the specified format. 
		"""
		if which_form != "wide" and which_form != "narrow":
			raise ValueError("Must input format wide or narrow")
		if which_form == "wide":
			return self.__play_out.copy()
		if which_form == "narrow":
			return self.__play_out.copy().stack().to_frame(name = "face_rolled")
