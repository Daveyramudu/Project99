import sqlite3

conn = sqlite3.connect("windows.db")    
c = conn.cursor()


#Creating a Table 
c.execute("""CREATE TABLE plugins(

      num1 integer  , num2 integer, result integer 
  
      
)   
            
""")
conn.commit()
