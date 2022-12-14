#!/usr/bin/python

"""
--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.
You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken
into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation,
b is the next-lowest, and so on up to the highest elevation, z.
Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E).
Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.
You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one
square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at
most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n,
but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your
current square.) For example:
  Sabqponm
  abcryxxl
  accszExk
  acctuvwj
  abdefghi
Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll
need to head toward the e at the bottom. From there, you can spiral around to the goal:
  v..v<<<<
  >v.vv<<^
  .>vv>E^^
  ..v>>>^^
  ..>>>>>^
In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>).
The location that should get the best signal is still E, and . marks unvisited squares.
This path reaches the goal in 31 steps, the fewest possible.
What is the fewest steps required to move from your current position to the location that should get the best signal?
"""


def mapInput() -> list:
  aoMap = []
  # with open('input_test', 'r') as fInputFile:
  with open('input', 'r') as fInputFile:
    while True:
      sLine = fInputFile.readline()
      if not sLine:
        break
      aiLine = []
      for i in range(len(sLine.strip())):
        aiLine.append(ord(sLine.strip()[i]))
      aoMap.append(aiLine.copy())
  return aoMap


def isValid(xSrc, ySrc, xDest, yDest, aoMap, maxX, maxY) -> bool:
  if (0 <= xDest < maxX) and (0 <= yDest < maxY) and (aoMap[xDest][yDest] - aoMap[xSrc][ySrc] <= 1):
      return True
  return False


def findDistance(aoMap, s, e) -> int:
  #possible moves:
  dx = [-1, 0, 0, 1]
  dy = [0, -1, 1, 0]
  x = s[0]
  y = s[1]
  # queue = [startX, startY, distanceFromStart]
  queue = [[x, y, 0]]
  visited = [s]
  maxX = len(aoMap)
  maxY = len(aoMap[0])
  while queue:
    current = queue.pop(0)

    if current[0] == e[0] and current[1] == e[1]:
      return current[2]

    for i in range(len(dx)):
      #get next possible position
      x = current[0] + dx[i]
      y = current[1] + dy[i]
      #validate and check if not already visited
      if isValid(current[0], current[1], x, y, aoMap, maxX, maxY):
        if [x,y] not in visited and [x, y, current[2] + 1] not in queue:
          queue.append([x, y, current[2] + 1])
    visited.append([current[0], current[1]])



def taskOne(aoMap) -> None:
  startingPoint = finishPoint = None
  for x in range(len(aoMap)):
    if startingPoint is not None and finishPoint is not None:
        break
    for y in range(len(aoMap[x])):
      if aoMap[x][y] == ord('S'):
        startingPoint = [x, y]
        aoMap[x][y] = ord('a')
        continue
      if aoMap[x][y] == ord('E'):
        finishPoint = [x, y]
        aoMap[x][y] = ord('z')

  print("Shortest path: {}".format(findDistance(aoMap, startingPoint, finishPoint)))

"""
--- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though;
perhaps you can find a better starting point. To maximize exercise while hiking, the trail should start as low as possible: elevation a.
The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll
need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:
  Sabqponm
  abcryxxl
  accszExk
  acctuvwj
  abdefghi
Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a).
If you start at the bottom-left square, you can reach the goal most quickly:
  ...v<<<<
  ...vv<<^
  ...v>E^^
  .>v>>>^^
  >^>>>>>^
This path reaches the goal in only 29 steps, the fewest possible.
What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
"""

# finding path backwards

def isValid2(xSrc, ySrc, xDest, yDest, aoMap, maxX, maxY) -> bool:
  if (0 <= xDest < maxX) and (0 <= yDest < maxY) and (aoMap[xSrc][ySrc] - aoMap[xDest][yDest]  <= 1):
      return True
  return False


def findDistance2(aoMap, s) -> int:
  #possible moves:
  dx = [-1, 0, 0, 1]
  dy = [0, -1, 1, 0]
  x = s[0]
  y = s[1]
  # queue = [startX, startY, distanceFromStart]
  queue = [[x, y, 0]]
  visited = [s]
  maxX = len(aoMap)
  maxY = len(aoMap[0])
  while queue:
    current = queue.pop(0)

    if aoMap[current[0]][current[1]] == ord('a'):
      return current[2]

    for i in range(len(dx)):
      #get next possible position
      x = current[0] + dx[i]
      y = current[1] + dy[i]
      #validate and check if not already visited
      if isValid2(current[0], current[1], x, y, aoMap, maxX, maxY):
        if [x,y] not in visited and [x, y, current[2] + 1] not in queue:
          queue.append([x, y, current[2] + 1])
    visited.append([current[0], current[1]])



def taskTwo(aoMap) -> None:
  startingPoint = None
  for x in range(len(aoMap)):
    if startingPoint is not None:
      break
    for y in range(len(aoMap[x])):
      if aoMap[x][y] == ord('E'):
        startingPoint = [x, y]
        aoMap[x][y] = ord('z')

  print("Shortest path with better view: {}".format(findDistance2(aoMap, startingPoint)))




if __name__ == '__main__':
  aoMap = mapInput()
  taskOne(aoMap)
  aoMap = mapInput()
  taskTwo(aoMap)
