from flask import Flask
from flask import abort

import sqlite3 as sql

import os

application = Flask(__name__)

CHUNK_SIZE = 5000
FILENAME = os.environ.get("FILENAME")

@application.route("/")
def hello():
    return "Hello Salsify!"

# FIRST PASS, very naive
# @application.route("/lines/old/<int:line_num>")
# def get_line_first_version(line_num):
#   line_index = 1
#   with open("test_file.txt", "r") as file:
#     for line in file:
#       if line_index == line_num:
#         return line
#       else:
#         line_index += 1
#
#   abort(413)

@application.route("/lines/<int:line_num>")
def get_line(line_num):
  if line_num < 1:
    abort(413)

  seek_target = 0
  chunk_start = (int((line_num-1)/CHUNK_SIZE) * CHUNK_SIZE) + 1

  try:
    with sql.connect("database.db") as connection:
      cursor = connection.cursor()
      cursor.execute("select seek_target from line_size_map where line_num = ?", (chunk_start,))
      seek_target = cursor.fetchall()[0][0]
  except IndexError:
    abort(413)
  finally:
    connection.close()

  line = iterate_through_file(seek_target, line_num, chunk_start)

  if line is not None:
    return line
  else:
    abort(413)


def iterate_through_file(seek_target, line_num, chunk_start):
  line_index = chunk_start
  with open(FILENAME, "rb") as file:
    file.seek(seek_target)
    for line in file:
      if line_index == line_num:
        return line
      else:
        line_index += 1

  return None

if __name__ == "__main__":
  application.run(host='0.0.0.0')