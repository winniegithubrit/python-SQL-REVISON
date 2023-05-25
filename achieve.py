import sqlite3
conn = sqlite3.connect("database.db")
CURSOR = conn.cursor()
# CURSOR.execute(""" CREATE TABLE IF NOT EXISTS students(
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT,
#                age INTEGER,
#                course TEXT)
#                """)
# CURSOR.execute(
#   """INSERT INTO students(id,name,age,course) 
#   VALUES(1,"Georginah", 19, "BSC Mathematics and ComputerScience")
        
#   """
# )
# CURSOR.execute(
#   """INSERT INTO students(id,name,age,course)
#   VALUES(2,"Ahmed",22,"BSC ComputerScience")
  
#   """
# )
# CURSOR.execute(
#   """INSERT INTO students(id,name,age,course)
#   VALUES(3,"Wendy",24,"BSC ChemicalScience")
  
#   """
# )
# # CURSOR.execute(
# #   """INSERT INTO students(id,name,age,course)
# #   VALUES(4,"Nathalie",12,"BSC SoftwareEngineering")
  
# #   """
# )
# CURSOR.execute(
#   """INSERT INTO students(id,name,age,course)
#   VALUES(5,"Winter",30,"BSC InfoTech")
  
#   """
# )
CURSOR.execute(
  """DELETE FROM students WHERE rowid = 2
  
  
  """
)

conn.commit()