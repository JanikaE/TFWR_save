import Helper
n = get_world_size()

# 单无人机
def Cactus():
	while True:
		for i in range(n):
			for j in range(n):
				plant(Entities.Cactus)
				move(North)
			move(East)			
		Helper.move_to(0,0)
		# 阶段1：对每行进行排序（奇数行升序，偶数行降序）
		for i in range(n):			
			if i % 2 == 0:
				# 偶数行：从左到右排序（升序）
				for j in range(n-1):	
					single_swapped = False
					Helper.move_to(0, i)
					for k in range(n-j-1):
						if (measure() > measure(East)):
							swap(East)
							single_swapped = True
						move(East)
					if single_swapped == False:
						break
				if single_swapped == False:
					continue
			else:
				# 奇数行：从右到左排序（升序，但方向相反）
				for j in range(n-1):	
					single_swapped = False
					Helper.move_to(n-1, i)
					for k in range(n-j-1):
						if (measure() < measure(West)):
							swap(West)
							single_swapped = True
						move(West)
					if single_swapped == False:
						break
				if single_swapped == False:
					continue			
		# 阶段2：对每列进行排序（从上到下升序）
		for j in range(n):
			for i in range(n-1):
				single_swapped = False
				Helper.move_to(j,0)
				for k in range(n-i-1):
					if (measure() > measure(North)):
						swap(North)
						single_swapped = True
					move(North)
				if single_swapped == False:
					break
			if single_swapped == False:
				continue
		# 收割
		harvest()

# 32无人机
def Cactus_M():
	def Plant_Cactus():
		for i in range(n):
			if (get_ground_type() == Grounds.Grassland):
				till()
			plant(Entities.Cactus)
			move(North)
	def SortRow():
		y = get_pos_y()
		if (y % 2 == 0):
			# 偶数行：从左到右排序（升序）
			for i in range(n-1):
				single_swapped = False
				Helper.move_to(0, y)
				for j in range(n-i-1):
					if (measure() > measure(East)):
						swap(East)
						single_swapped = True
					move(East)
				if single_swapped == False:
					break
		else:
			# 奇数行：从右到左排序（升序，但方向相反）
			for i in range(n-1):
				single_swapped = False
				Helper.move_to(n-1, y)
				for j in range(n-i-1):
					if (measure() < measure(West)):
						swap(West)
						single_swapped = True
					move(West)
				if single_swapped == False:
					break
	def SortColumn():
		x = get_pos_x()
		for i in range(n-1):
			single_swapped = False
			Helper.move_to(x,0)
			for j in range(n-i-1):
				if (measure() > measure(North)):
					swap(North)
					single_swapped = True
				move(North)
			if single_swapped == False:
				break
	while(True):
		# Plant
		Helper.move_to(0,0)
		for i in range(n-1):
			spawn_drone(Plant_Cactus)
			move(East)
		Plant_Cactus()
		# SortRow
		Helper.move_to(0,0)
		finishList = []
		for i in range(n-1):
			finishList.append(spawn_drone(SortRow))
			move(North)
		SortRow()
		for i in range(n-1):
			if (finishList[i] != None):
				wait_for(finishList[i])
		# SortColumn
		Helper.move_to(0,0)
		finishList = []
		for i in range(n-1):
			finishList.append(spawn_drone(SortColumn))
			move(East)
		SortColumn()
		for i in range(n-1):
			if (finishList[i] != None):
				wait_for(finishList[i])
		# Harvest
		harvest()