from app import CHUNK_SIZE

import sqlite3 as sql

import sys

def clear_db():
  try:
    with sql.connect("database.db") as connection:
      cursor = connection.cursor()
      cursor.execute("delete from line_size_map")

      connection.commit
  except:
    connection.rollback()

  finally:
    connection.close()

def process_file(filename):

  clear_db()

  line_index = 1
  bytes_so_far = 0 #maybe don't keep a total, just need last plus new?
  
  try:
    with open(filename, "rb") as file:
      for line in file:
        if line_index % CHUNK_SIZE == 1:
          try:
            with sql.connect("database.db") as connection:
              cursor = connection.cursor()
              cursor.execute("insert into line_size_map (line_num, seek_target) values (?, ?)", (line_index, bytes_so_far))

              connection.commit
          except:
            connection.rollback()
        
          finally:
            connection.close()

        bytes_so_far += len(line)

        line_index += 1
  except FileNotFoundError:
    print('please supply a valid, existing filename')
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    process_file(sys.argv[1])
  else:
    print('please supply a filename')