import Helper
n = get_world_size()

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
		if pos[0] == -1:
			break
		Helper.move_to(pos[0], pos[1])
		list.pop(index)
		harvest()
		