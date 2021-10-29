import sys
steps = int(sys.argv[1])
for step in range(1,steps+1):
  print(' ' * (steps-step) + '#' * step)
