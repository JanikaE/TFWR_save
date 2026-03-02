import Helper
n = get_world_size()

# 单无人机
def Tree():
	dict = {}	
	while(True):
		for _ in range(n):
			for _ in range(n):
				x = get_pos_x()
				y = get_pos_y()
				if (can_harvest()):
					harvest()
				entity = Entities.Carrot
				if ((x,y) in dict):
					entity = dict[(x,y)]
				if (entity == Entities.Grass and get_ground_type() == Grounds.Soil or entity != Entities.Grass and get_ground_type() == Grounds.Grassland):
					till()
				plant(entity)
				com = get_companion()
				if (com != None):
					dict[com[1]] = com[0]
				move(North)
			move(East)

# 32无人机
def Tree_M():
	def Plant():
		while (True):
			com = get_companion()
			while com == None:
				if get_ground_type() == Grounds.Soil:
					till()
					com = get_companion()
			Helper.move_to(com[1][0], com[1][1])
			if (can_harvest()):
				harvest()
			entity = com[0]
			if (entity == Entities.Grass and get_ground_type() == Grounds.Soil or entity != Entities.Grass and get_ground_type() == Grounds.Grassland):
				till()
			while get_water() < 0.75:
				use_item(Items.Water)
			plant(entity)
	for _ in range(n - 1):
		spawn_drone(Plant)
		move(East)
	Plant()
		