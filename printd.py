from printrun.printcore import printcore
from printrun import gcoder
import time



def printd(path):
  p=printcore('/dev/ttyUSB0', 115200)
  pathV= path[::-1]
  if pathV[0]=='e' and pathV[1]=='d' and pathV[2]=='o' and pathV[3]=='c' and pathV[4]=='g' and pathV[5]=='.':
    pass
  else:
    print('please enter a gcode file')
    return 101
  gcode=[i.strip() for i in open(path)]
  gcode=gcoder.LightGCode(gcode)

  print('gcode ready')

  while not p.online:
    time.sleep(0.1)

  print('starting print')

  p.startprint(gcode)


if __name__ =='__main__':
  printd('')
