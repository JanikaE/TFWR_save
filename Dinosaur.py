import Helper
n = get_world_size()
body = []


def Dinosaur():
	while (True):
		change_hat(Hats.Carrot_Hat)
		Helper.move_to(0,0)
		change_hat(Hats.Dinosaur_Hat)
		body.append((0, 0))

		con = True
		while(con == True):
			next = NextMove()
			body.insert(0, next)
			if next != measure():
				body.pop()

			if next[0] > get_pos_x():
				con = move(East)
			elif next[0] < get_pos_x():
				con = move(West)
			elif next[1] > get_pos_y():
				con = move(North)
			else:
				con = move(South)


def NextMove():
	food_x, food_y = measure()
	food = (food_x, food_y)
	pathToFood = FindPath(body[0], food, body)

	if pathToFood and len(pathToFood) > 1:
		nextMove = pathToFood[1]
		simulateD = SimulateMove(nextMove, body, nextMove == food)

		tail = simulateD[-1]
		pathToTail = FindPath(simulateD[0], tail, simulateD, True)
		if pathToTail and len(pathToTail) > 1:
			return nextMove
		
	tail = body[-1]
	pathToTail = FindPath(body[0], tail, body, True)
	if pathToTail and len(pathToTail) > 1:
		return pathToTail[1]

	return body[0]


def Check(point):
	if point in body:
		return False
	if point[0] < 0 or point[0] >= n or point[1] < 0 or point[1] >= n:
		return False
	return True


def FindPath(start, target, body, ignoreTail):
	queue = []
	prev = {}
	blocked = body.copy()
	if ignoreTail and len(body) > 0:
		blocked = blocked[:-1]
	queue.append(start)
	prev[start] = None
	while len(queue) > 0:
		current = queue.pop(0)
		if current == target:
			break
		for dir in GetMoveDirections(current[0], current[1]):
			next = MoveOne(current, dir)
			if next[0] < 0 or next[0] >= n or next[1] < 0 or next[1] >= n:
				continue
			if next in blocked:
				continue
			if next in prev:
				continue
			prev[next] = current
			queue.append(next)

	if target not in prev:
		return
	
	path = []
	current = target
	while current != start:
		path.append(current)
		current = prev[current]
	path.append(start)
	path.reverse()
	return path


def SimulateMove(newHead, body, eatsFood):
	result = body.copy()
	result.insert(0, newHead)
	if not eatsFood:
		result.pop()
	return result


def GetMoveDirections(x, y):
	move_directions = []
	if y % 2 == 0:
		move_directions.append(East)
	else:
		move_directions.append(West)
	if x % 2 == 0:
		move_directions.append(North)
	else:
		move_directions.append(South)
	return move_directions


def MoveOne(point, direction):
	if direction == East:
		return (point[0] + 1, point[1])
	elif direction == West:
		return (point[0] - 1, point[1])
	elif direction == North:
		return (point[0], point[1] + 1)
	elif direction == South:
		return (point[0], point[1] - 1)