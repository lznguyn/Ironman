import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id interger primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null, 'one note', 'C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE')"
# cursor.execute(query)
# con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id interger primary key, name VARCHAR(100), url ARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com')"
cursor.execute(query)
con.commit()