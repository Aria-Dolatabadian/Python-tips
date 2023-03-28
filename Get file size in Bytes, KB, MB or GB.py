import os
import enum
from pathlib import Path
def get_file_size_in_bytes(file_path):
   size = os.path.getsize(file_path)
   return size
def get_file_size_in_bytes_2(file_path):
   stat_info = os.stat(file_path)
   size = stat_info.st_size
   return size
def get_file_size_in_bytes_3(file_path):
   file_obj = Path(file_path)
   size = file_obj.stat().st_size
   return size
class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4
def convert_unit(size_in_bytes, unit):
   if unit == SIZE_UNIT.KB:
       return size_in_bytes/1024
   elif unit == SIZE_UNIT.MB:
       return size_in_bytes/(1024*1024)
   elif unit == SIZE_UNIT.GB:
       return size_in_bytes/(1024*1024*1024)
   else:
       return size_in_bytes
def get_file_size(file_name, size_type = SIZE_UNIT.BYTES ):
   size = os.path.getsize(file_name)
   return convert_unit(size, size_type)
def main():
   file_path = 'd:\python\diamonds.csv'
   size = get_file_size_in_bytes(file_path)
   print('File size in bytes:', size)
   file_path = 'd:\python\diamonds.csv'
   size = get_file_size(file_path, SIZE_UNIT.KB)
   print('File size in KB is:', size)
   file_path = 'd:\python\diamonds.csv'
   size = get_file_size(file_path, SIZE_UNIT.MB)
   print('File size in MB is:', size)
   file_path = 'd:\python\diamonds.csv'
   size = get_file_size(file_path, SIZE_UNIT.GB)
   print('File size in GB is:', size)
   file_name = 'dummy_file.txt'
if __name__ == '__main__':
      main()
