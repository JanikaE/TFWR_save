import Helper
n = get_world_size()

# 排序_单无人机
def Sort():
	list = []
	list.insert(0, (-1,-1,0))
	for _ in range(n):
		for _ in range(n):
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
		if pos[0] == -1:
			break
		Helper.move_to(pos[0], pos[1])
		list.pop(index)
		harvest()

# 全7_32无人机
def AllSeven_M():
	def Plant():
		for _ in range(n):
			if (get_ground_type() == Grounds.Grassland):
				till()
			while get_water() < 0.75:
				use_item(Items.Water)
			while measure() != 7:
				harvest()
				plant(Entities.Sunflower)
			move(North)
	def Harvest():
		for _ in range(n):
			harvest()
			move(North)
	while True:
		# Plant
		Helper.move_to(0, 0)
		finishList = []
		for _ in range(n-1):
			finishList.append(spawn_drone(Plant))
			move(East)
		Plant()
		for i in range(n-1):
			if (finishList[i] != None):
				wait_for(finishList[i])
		# Harvest
		Helper.move_to(0, 0)
		finishList = []
		for _ in range(n-1):
			finishList.append(spawn_drone(Harvest))
			move(East)
		Harvest()
		for i in range(n-1):
			if (finishList[i] != None):
				wait_for(finishList[i])