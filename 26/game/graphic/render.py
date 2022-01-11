import sys, os

sys.path.append("./../../HWPython26_11_PackageExam03_김태인")

from game.sound.echo import echo_test
def render_test():
  print("render")
  echo_test()
  
if __name__=="__main__":
  print("render")
  echo_test