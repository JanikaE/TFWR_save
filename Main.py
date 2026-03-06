import Helper 
import Plant
import Pumpkin
import Cactus
import Maze
import Dinosaur
import Sunflower
target = "pumpkin"

Helper.move_to(0,0)
if (target == "tree"):
	Plant.Tree_M()	
if (target == "pumpkin"):
	Pumpkin.Pumpkin_M_Fertilizer()
if (target == "cactus"):
	Cactus.Cactus()
if (target == "cactus_m"):
	Cactus.Cactus_M()
if (target == "sunflower"):
	Sunflower.Sunflower()
if (target == "dinosaur"):
	Dinosaur.Dinosaur()
if (target == "maze"):
	Maze.Maze()