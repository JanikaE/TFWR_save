import Helper
n = get_world_size()

# 草\树\萝卜
def Tree():
	dict = {}	
	while(True):
		for i in range(n):
			for j in range(n):
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

