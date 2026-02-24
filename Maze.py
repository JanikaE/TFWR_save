import Helper

def Maze():
	dir = [East, North, West, South]
	while(True):
		Helper.move_to(0, 0)
		if (get_ground_type() == Grounds.Grassland):
			till()
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		index = 0
		while(get_entity_type() != Entities.Treasure):
			index = (index - 1) % 4
			while(can_move(dir[index]) == False):
				index = (index + 1) % 4
			move(dir[index])
		harvest()