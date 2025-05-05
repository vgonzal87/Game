# Game

Metadata (general info):
  Victoria Gonzales 
  DS5100 Final Project 
  May 2025
  Create a monte carlo simulation of a game with die and an analyzer

Synopsis (how to call each class): 
  Call die class
  die_test = Die(np.array([1]))
	Call game class 
  game_test = Game([die_test])
	game_test.play(4)
  Call analyzer class
  analyzer_test = Analyzer(game_test)
API (List of all classes and methods)
  Die class
    Initializer: Die(np.array())
    change_weight()
    roll_die()
    current_state()
  Game class 
    Initializer: Game([List of Die])
    play()
    current_play()
  Analyzer class 
    Initializer: Analyzer(Game_Object)
    jackpot()
    face_counts()
    combo_count()
    permutation_count()
