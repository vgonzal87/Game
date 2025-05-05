# die class 

import pandas as pd
import numpy as np
import random

class Die():
	"""
	A class representing a die with N sides/faces and W weights. 
	"""
	def __init__(self, faces):
		"""
		Initialize a Die object with N faces and default weights on each side with value of 1. 
		
		Inputs: The number of faces to be assigned.
		
		Implications/Outputs: Creates a private dataframe where the index contains the weights and the columns contain the values of the faces.
		"""
		if type(faces) != np.ndarray:
			raise TypeError("Input must be numpy array")
		if len(faces) != len(np.unique(faces)):
			raise ValueError("Elements in array must be unique")
		self.faces = faces
		self.weights = np.full(len(faces), 1)
		self.__df_die = pd.DataFrame(columns = ["faces"], index = self.weights, data = self.faces)
	
	def change_weight(self, face_val, new_weight):
		"""
		Change the weight of a specified face.  
		
		Inputs: The value of the face wished to be changed, and value of the new weight.
		
		Implications/Outputs: Adjusts the current weight to the new weight within the index of the private dataframe.
		"""
		if self.__df_die['faces'].dtypes != type(face_val):
			raise IndexError("Input value must be the same as original array")
		try:
			float(new_weight)
		except (ValueError, TypeError):
			raise TypeError("Input must be numeric or castable to numeric")
		self.__df_die.index = self.__df_die.index.where(~(self.__df_die['faces'] == face_val), new_weight)
	
	def roll_die(self, num_rolls = 1):
		"""
		Rolls the die object a specific number of times.   
		
		Inputs: The number of times the dice should be rolled. 
		
		Implications/Outputs: Returns a list containing the results of each roll. 
		"""
		return [random.choices(self.__df_die.values, weights = list(self.__df_die.index))[0][0] for i in range(num_rolls)]	
	
	def current_state(self):
		"""
		Outputs a copy of the private die dataframe showing the current state.     
		
		Inputs: None
		
		Implications/Outputs: Returns a copy of the private die dataframe. 
		"""
		return self.__df_die.copy()

