def move_to(tar_x, tar_y):
	n = get_world_size()
	x = get_pos_x()
	y = get_pos_y()
	if (x > tar_x):
		x = x - n
	if (tar_x - x < n / 2):
		while(get_pos_x() != tar_x):
			move(East)
	else:
		while(get_pos_x() != tar_x):
			move(West)
	if (y > tar_y):
		y = y - n
	if (tar_y - y < n / 2):
		while(get_pos_y() != tar_y):
			move(North)
	else:
		while(get_pos_y() != tar_y):
			move(South)
		
def clear_and_till():
	clear()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			move(North)
		move(East)
		
def copy(list):
	result = []
	for i in range(len(list)):
		item = list[i] 
		result.append(item)
	return result
	
def reverse(list):
	result = []
	n = len(list)
	for i in range(n):
		result.append(list[n - i - 1])
	return result