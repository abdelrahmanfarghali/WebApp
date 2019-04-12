import sqlite3
connection = sqlite3.connect('database.db')
command = """CREATE TABLE iqraa(ptitle,posts,description)"""
cursor = connection.cursor()
cursor.execute(command)
connection.commit()
connection.close()
