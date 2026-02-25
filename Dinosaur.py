import Helper
n = get_world_size()

def Dinosaur():
	while (True):
		change_hat(Hats.Carrot_Hat)
		Helper.move_to(0,0)
		change_hat(Hats.Dinosaur_Hat)
		con = True
		while(con == True):
			con = move(East)
			for i in range(n):
				for j in range(n-2):
					if (i % 2 == 0):
						con = move(East)
					else:
						con = move(West)
				if (get_pos_y() == n-1):
					con = move(West)
				else:
					con = move(North)
				if (con == False):
					break
			for i in range(n-1):
				con = move(South)
				if (con == False):
					break