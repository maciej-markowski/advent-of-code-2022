#!/usr/bin/python

"""
--- Day 11: Monkey in the Middle ---
As you finally start making your way upriver, you realize your pack is much lighter than you remember.
Just then, one of the items from your pack goes flying overhead. Monkeys are playing Keep Away with your missing things!
To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation,
you realize the monkeys operate based on how worried you are about each item.
You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items,
and how the monkey makes decisions based on your worry level. For example:
  <input-test>
Each monkey has several attributes:
  Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
  Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means 
  that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
  Test shows how the monkey uses your worry level to decide where to throw an item next.
  If true shows what happens with an item if the Test was true.
  If false shows what happens with an item if the Test was false.
After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item
causes your worry level to be divided by three and rounded down to the nearest integer.
The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items it is holding
one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn. The process
of each monkey taking a single turn is called a round.
When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that starts a round
with no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items
at the start of its turn, its turn ends.
In the above example, the first round proceeds as follows:
  Monkey 0:
    Monkey inspects an item with a worry level of 79.
      Worry level is multiplied by 19 to 1501.
      Monkey gets bored with item. Worry level is divided by 3 to 500.
      Current worry level is not divisible by 23.
      Item with worry level 500 is thrown to monkey 3.
    Monkey inspects an item with a worry level of 98.
      Worry level is multiplied by 19 to 1862.
      Monkey gets bored with item. Worry level is divided by 3 to 620.
      Current worry level is not divisible by 23.
      Item with worry level 620 is thrown to monkey 3.
(...)
  Monkey 0: 20, 23, 27, 26
  Monkey 1: 2080, 25, 167, 207, 401, 1046
  Monkey 2: 
  Monkey 3: 
Monkeys 2 and 3 aren't holding any items at the end of the round; they both inspected items during the round and threw them all before the round ended.
This process continues for a few more rounds:
After round 2, the monkeys are holding items with these worry levels:
  Monkey 0: 695, 10, 71, 135, 350
  Monkey 1: 43, 49, 58, 55, 362
  Monkey 2: 
  Monkey 3: 
(...)
After round 20, the monkeys are holding items with these worry levels:
  Monkey 0: 10, 12, 14, 26, 34
  Monkey 1: 245, 93, 53, 199, 115
  Monkey 2: 
  Monkey 3: 
Chasing all of the monkeys at once is impossible; you're going to have to focus on the two most active monkeys if you
want any hope of getting your stuff back. Count the total number of times each monkey inspects items over 20 rounds:
  Monkey 0 inspected items 101 times.
  Monkey 1 inspected items 95 times.
  Monkey 2 inspected items 7 times.
  Monkey 3 inspected items 105 times.
In this example, the two most active monkeys inspected items 101 and 105 times. The level of monkey business in this
situation can be found by multiplying these together: 10605.
Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. 
What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
"""

def taskOne() -> None:
  oMonkeys = {}
  with open('input', 'r') as fInputFile:
    while True:
      sLine = fInputFile.readline()
      if not sLine:
        break
      if sLine.startswith('Monkey'):
        _mID = int(sLine.strip()[-2])
        sLine = fInputFile.readline()
        _itm = []
        for i in sLine.strip().split(':')[1].split(','):
          _itm.append(int(i))
        sLine = fInputFile.readline()
        _op = sLine.strip().split('=')[1].strip()
        sLine = fInputFile.readline()
        _divisible_by = int(sLine.strip().split()[-1])
        sLine = fInputFile.readline()
        _if_true = int(sLine.strip().split()[-1])
        sLine = fInputFile.readline()
        _if_false = int(sLine.strip().split()[-1])
        oMonkeys[_mID] = {
                          'items': _itm,
                          'operation': _op,
                          'test': _divisible_by,
                          'if_true': _if_true,
                          'if_false': _if_false,
                          'inspected': 0
                        }
  
  iRounds = 20

  for _ in range(iRounds):
    for i in range(len(oMonkeys)):
      for item in oMonkeys[i]['items'].copy():
        if oMonkeys[i]['operation'].split()[1] == '+':
          worry_level = item + int(oMonkeys[i]['operation'].split()[2])
        elif oMonkeys[i]['operation'].split()[2] == 'old':
          worry_level = item * item
        else:
          worry_level = item * int(oMonkeys[i]['operation'].split()[2])
        worry_level = worry_level // 3
        if worry_level %  oMonkeys[i]['test'] == 0:
          oMonkeys[oMonkeys[i]['if_true']]['items'].append(worry_level)
          oMonkeys[i]['items'].pop(0)
        else:
          oMonkeys[oMonkeys[i]['if_false']]['items'].append(worry_level)
          oMonkeys[i]['items'].pop(0)
        oMonkeys[i]['inspected'] += 1

  iInspections = []
  for i in range(len(oMonkeys)):
    iInspections.append(oMonkeys[i]['inspected'])
  iInspections.sort()

  print("Monkey business is {}".format(str(iInspections[-1] * iInspections[-2])))
 

"""
You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection
didn't damage an item no longer causes your worry level to be divided by three.
Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to
find another way to keep your worry levels manageable.
At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!
Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your
worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?
"""

def taskTwo() -> None:
  oMonkeys = {}
  with open('input', 'r') as fInputFile:
    while True:
      sLine = fInputFile.readline()
      if not sLine:
        break
      if sLine.startswith('Monkey'):
        _mID = int(sLine.strip()[-2])
        sLine = fInputFile.readline()
        _itm = []
        for i in sLine.strip().split(':')[1].split(','):
          _itm.append(int(i))
        sLine = fInputFile.readline()
        _op = sLine.strip().split('=')[1].strip()
        sLine = fInputFile.readline()
        _divisible_by = int(sLine.strip().split()[-1])
        sLine = fInputFile.readline()
        _if_true = int(sLine.strip().split()[-1])
        sLine = fInputFile.readline()
        _if_false = int(sLine.strip().split()[-1])
        oMonkeys[_mID] = {
                          'items': _itm,
                          'operation': _op,
                          'test': _divisible_by,
                          'if_true': _if_true,
                          'if_false': _if_false,
                          'inspected': 0
                        }
  
  iRounds = 10000
  MOD = 1
  for i in range(len(oMonkeys)):
    MOD *= oMonkeys[i]['test']

  for _ in range(iRounds):
    for i in range(len(oMonkeys)):
      for item in oMonkeys[i]['items'].copy():
        if oMonkeys[i]['operation'].split()[1] == '+':
          worry_level = item + int(oMonkeys[i]['operation'].split()[2])
        elif oMonkeys[i]['operation'].split()[2] == 'old':
          worry_level = item * item
        else:
          worry_level = item * int(oMonkeys[i]['operation'].split()[2])
        worry_level = worry_level % MOD
        if worry_level %  oMonkeys[i]['test'] == 0:
          oMonkeys[oMonkeys[i]['if_true']]['items'].append(worry_level)
          oMonkeys[i]['items'].pop(0)
        else:
          oMonkeys[oMonkeys[i]['if_false']]['items'].append(worry_level)
          oMonkeys[i]['items'].pop(0)
        oMonkeys[i]['inspected'] += 1

  iInspections = []
  for i in range(len(oMonkeys)):
    iInspections.append(oMonkeys[i]['inspected'])
  iInspections.sort()

  print("[worry level self decreased] Monkey business is {}".format(str(iInspections[-1] * iInspections[-2])))



if __name__ == '__main__':
  taskOne()
  taskTwo()
