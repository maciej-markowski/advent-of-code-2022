#!/usr/bin/python

"""

"""

#sInput ='input_test'
sInput = 'input'

def printCave(cave) -> None:
  for i in range(len(cave)):
    _r = ''
    for j in range(len(cave[0])):
      _r += cave[i][j]
    print(_r)
  print('\n\n\n\n\n')


def taskOne() -> None:
  iNormalizeX = 9999
  iMaxY = 0
  iMaxX = 0
  with open(sInput, 'r') as fInputFile:
    while True:
      sLine = fInputFile.readline()
      if not sLine:
        break
      for pair in sLine.split(' -> '):
        _x = int(pair.split(',')[0])
        _y = int(pair.split(',')[1])
        if  _x < iNormalizeX:
          iNormalizeX = _x
        if _y > iMaxY:
          iMaxY = _y
        if _x > iMaxX:
          iMaxX = _x
  iMaxX -= iNormalizeX

  asCave = []
  _r = ['.']
  for _ in range(iMaxX + 1):
    _r.append('.')

  for _ in range(iMaxY + 1):
    asCave.append(_r.copy())

  with open(sInput, 'r') as fInputFile:
    while True:
      sLine = fInputFile.readline()
      if not sLine:
        break
      asPairs = sLine.split(' -> ')
      for i in range(len(asPairs) - 1):
        aStartPoint = [int(asPairs[i].split(',')[0]) - iNormalizeX, int(asPairs[i].split(',')[1])]
        aEndPoint = [int(asPairs[i + 1].split(',')[0]) - iNormalizeX, int(asPairs[i + 1].split(',')[1])]

        if aStartPoint[1] - aEndPoint[1] == 0: # horizontal line
          for i in range(min([aStartPoint[0], aEndPoint[0]]), max([aStartPoint[0], aEndPoint[0]]) + 1):
            asCave[aStartPoint[1]][i] = '#'

        else: # vertical line
          for i in range(min([aStartPoint[1], aEndPoint[1]]), max([aStartPoint[1], aEndPoint[1]]) + 1 ):
            asCave[i][aStartPoint[0]] = '#'

    iStoppedSand = 0
    bInVoid = False
    while True:
      if bInVoid:
        break
      aSandPoint = [500 -iNormalizeX, 0]
      while True:
        aPrevSandPoint = aSandPoint.copy()
        aSandPoint[1] += 1

        if aSandPoint[1] > iMaxY: # we fell out to void
          bInVoid = True
          break
        if asCave[aSandPoint[1]][aSandPoint[0]] == '.': # straigth down is a free space, continue faling
          continue
        # no space directly underneath
        aSandPoint[0] -= 1 # move left
        if asCave[aSandPoint[1]][aSandPoint[0]] == '.': # if we have free space, continue falling
          continue

        # no space on left, let's try right
        aSandPoint[0] += 2
        if aSandPoint[0] < len(asCave[0]) and asCave[aSandPoint[1]][aSandPoint[0]] == '.': # if we're still in range and we have space, continue falling
          continue
        # we're either out of range or at the bottom
        asCave[aPrevSandPoint[1]][aPrevSandPoint[0]] = 'o'
        iStoppedSand += 1
        break

  #printCave(asCave)
  print("Stopped sands before falling into void: {}".format(iStoppedSand))





"""

"""


def redrawCave(cave, i) -> list:
  if i < 0: #expand to left
    for i in range(len(cave) - 1):
      cave[i].insert(0, '.')
    cave[-1].insert(0, '#')
  else:
    for i in range(len(cave) - 1):
      cave[i].append('.')
    cave[-1].append('#')
  return cave


def taskTwo() -> None:
  iNormalizeX = 9999
  iMaxY = 0
  iMaxX = 0
  with open(sInput, 'r') as fInputFile:
    while True:
      sLine = fInputFile.readline()
      if not sLine:
        break
      for pair in sLine.split(' -> '):
        _x = int(pair.split(',')[0])
        _y = int(pair.split(',')[1])
        if  _x < iNormalizeX:
          iNormalizeX = _x
        if _y > iMaxY:
          iMaxY = _y
        if _x > iMaxX:
          iMaxX = _x
  iMaxX -= iNormalizeX

  asCave = []
  _r = ['.']
  for _ in range(iMaxX + 1):
    _r.append('.')

  for _ in range(iMaxY + 2):
    asCave.append(_r.copy())

  _r = ['#']
  for _ in range(iMaxX + 1):
    _r.append('#')
  asCave.append(_r.copy())



  with open(sInput, 'r') as fInputFile:
    while True:
      sLine = fInputFile.readline()
      if not sLine:
        break
      asPairs = sLine.split(' -> ')
      for i in range(len(asPairs) - 1):
        aStartPoint = [int(asPairs[i].split(',')[0]) - iNormalizeX, int(asPairs[i].split(',')[1])]
        aEndPoint = [int(asPairs[i + 1].split(',')[0]) - iNormalizeX, int(asPairs[i + 1].split(',')[1])]

        if aStartPoint[1] - aEndPoint[1] == 0: # horizontal line
          for i in range(min([aStartPoint[0], aEndPoint[0]]), max([aStartPoint[0], aEndPoint[0]]) + 1):
            asCave[aStartPoint[1]][i] = '#'

        else: # vertical line
          for i in range(min([aStartPoint[1], aEndPoint[1]]), max([aStartPoint[1], aEndPoint[1]]) + 1 ):
            asCave[i][aStartPoint[0]] = '#'

    iStoppedSand = 0
    iStartX = 500
    while True:
      aSandPoint = [iStartX -iNormalizeX, 0]
      if  asCave[aSandPoint[1]][aSandPoint[0]] == 'o': # full cave
        break
      while True:
        aPrevSandPoint = aSandPoint.copy()
        aSandPoint[1] += 1
        if asCave[aSandPoint[1]][aSandPoint[0]] == '.': # straigth down is a free space, continue faling
          continue
        # no space directly underneath
        aSandPoint[0] -= 1 # move left
        if aSandPoint[0] < 0:
          asCave = redrawCave(asCave, -1) # due to infinite floor, we redraw the cave adding on left and maintain sand starting point
          aSandPoint[0] = 0
          iStartX += 1
        if asCave[aSandPoint[1]][aSandPoint[0]] == '.': # if we have free space, continue falling
          continue

        # no space on left, let's try right
        aSandPoint[0] += 2
        if  aSandPoint[0] >= len(asCave[0]):
          asCave = redrawCave(asCave, 1) # due to infinite floor, we redraw the cave adding on right
        if asCave[aSandPoint[1]][aSandPoint[0]] == '.': # if we're still in range and we have space, continue falling
          continue

        asCave[aPrevSandPoint[1]][aPrevSandPoint[0]] = 'o'
        iStoppedSand += 1
        break

  #printCave(asCave)
  print("Stopped sands before filling the cave: {}".format(iStoppedSand))




if __name__ == '__main__':
  taskOne()
  taskTwo()
