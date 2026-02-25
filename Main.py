import Helper 
import Plant
import Pumpkin
import Cactus
import Maze
import Dinosaur
target = "dinosaur"

Helper.move_to(0,0)
if (target == "tree"):
	Plant.Tree()	
if (target == "pumpkin"):
	Pumpkin.Pumpkin_F()
if (target == "pumpkin_f"):
	Pumpkin.Pumpkin_F()
if (target == "cactus"):
	Cactus.Cactus()
if (target == "cactus_m"):
	Cactus.Cactus_M()
if (target == "sunflower"):
	Plant.Sunflower()
if (target == "dinosaur"):
	Dinosaur.Dinosaur()
if (target == "maze"):
	Maze.Maze()