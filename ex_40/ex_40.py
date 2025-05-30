import mysql.connector as sqltor # importing mysql connector to connect the mysql with python
mycon = sqltor.connect(host="localhost", user='root', password='2007kabish', database="kabish")  # connecting

if mycon.is_connected() == False: # checking whether it is connected
    print("Error connecting to mysql")
cur = mycon.cursor() # setting a cursor instance
cur.execute('SELECT * FROM USER;') # execute the command in mysql
rows = cur.fetchall() # fetch the executed data from mysql
# order the headings for the table
prompt = input("Enter a search string: ").strip().lower()
print(f"{'EMPID':<6} | {'NAME':<12} | {'AGE':<3} | {'SALARY':<8} | {'MAILID':<18} | {'MOBILE':<12} | {'DEPT':<25} | {'GENDER':<6} | {'BRANCH'}")
print("-" * 130)
found = False # initiate found as false
for row in rows: # to check each row
    match_found = False
    for word in row: # to check each word
        if prompt in str(word).lower():
            match_found = True # if the prompt is in the line return true
            break
    if match_found:
        found = True # display after the match is correct
        print(f"{row[0]:<6} | {row[1]:<12} | {row[2]:<3} | {row[3]:<8} | {row[4]:<18} | {row[5]:<12} | {row[6]:<25} | {row[7]:<6} | {row[8]}")
if not found:
    print("No record found")


mycon.close() # close the opened file