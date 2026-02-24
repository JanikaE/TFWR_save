import Helper

def Pumpkin():
	n = 6
	while(True):
		for r in range(2):
			for i in range(n):
				for j in range(n):
					x = get_pos_x()
					y = get_pos_y()
					if (get_ground_type() == Grounds.Grassland):
						till()
					if (get_water() < 0.75):
						use_item(Items.Water)
					plant(Entities.Pumpkin)
					if (j != n - 1):
						if (x % 2 == 0):
							move(North)
						else:
							move(South)
				if (i != n - 1):
					if (r == 0):
						move(East)
					else:
						move(West)
			harvest()
			for i in range(n):
				for j in range(n):
					x = get_pos_x()
					y = get_pos_y()				
					plant(Entities.Pumpkin)
					if (j != n - 1):
						if (y % 2 == 0):
							move(West)
						else:
							move(East)
				if (i != n - 1):
					if (r == 0):
						move(North)
					else:
						move(South)
			harvest()
			
def Pumpkin_F():
	n = 6
	while(True):
		for i in range(n):
			for j in range(n):
				x = get_pos_x()
				y = get_pos_y()
				if (get_ground_type() == Grounds.Grassland):
					till()
				while(get_water() < 0.75):
					use_item(Items.Water)
				while(True):
					plant(Entities.Pumpkin)
					use_item(Items.Fertilizer)
					if (can_harvest() == True):
						break
				if (j != n - 1):
					if (x % 2 == 0):
						move(North)
					else:
						move(South)
			if (i != n - 1):
				move(East)
		harvest()
		Helper.move_to(0,0)