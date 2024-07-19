from Stack import Stack

def solveMaze(maze, startX, startY):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    stack = Stack()
    stack.push((startX, startY))
    step = 1
    while not stack.isEmpty():
        x, y = stack.peek()

        if maze[x][y] == 'G':
            return True

        if maze[x][y] == ' ':
            maze[x][y] = step
            step += 1

        moved = False

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if maze[nx][ny] in [' ', 'G']:
                stack.push((nx, ny))
                moved = True
                break

        if not moved:
            stack.pop()

    return False