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

# 向日葵
def Sunflower():
	list = []
	list.insert(0, (-1,-1,0))
	for i in range(n):
		for j in range(n):
			x = get_pos_x()
			y = get_pos_y()
			if (get_ground_type() == Grounds.Grassland):
				till()
			plant(Entities.Sunflower)
			value = measure()
			for k in range(len(list)):
				if (value > list[k][2]):
					list.insert(k, (x, y, value))
					break
			move(North)
		move(East)
	while(True):
		index = 0
		pos = list[index]
		Helper.move_to(pos[0], pos[1])
		#while(can_harvest() == False):
		#	index = index + 1
		#	pos = list[index]
		#	Helper.move_to(pos[0], pos[1])
		list.pop(index)
		harvest()
		plant(Entities.Sunflower)
		if (get_water() < 0.75):
			use_item(Items.Water)
		value = measure()
		for k in range(len(list)):
			if (value > list[k][2]):
				list.insert(k, (pos[0], pos[1], value))
				break
