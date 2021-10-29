from os import read


class FileReader:

    def __init__(self, path: str) -> None:
      self.path = path

    def read(self) -> str:
      try:
        with open(self.path,'r') as f:
          return ''.join(f.readlines())
      except FileNotFoundError:
          return ''
