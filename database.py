import sqlite3

def create_database():
  connection = sqlite3.connect('database.db')

  connection.execute('DROP TABLE IF EXISTS line_size_map')

  connection.execute('CREATE TABLE line_size_map (line_num INT, seek_target INT)')

  connection.execute('CREATE UNIQUE INDEX idx_line_num ON line_size_map (line_num)')

  connection.commit
  connection.close()

if __name__ == '__main__':
  create_database()