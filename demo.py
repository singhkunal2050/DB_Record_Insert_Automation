import psycopg2
connection = psycopg2.connect(user="kunal",
                              password="9011525149",
                              host="127.0.0.1",
                              port="5432",
                              database="bikebuddy")

cursor = connection.cursor()

my_query="""insert into user1 values(%s,%s,%s);"""           #query to execute 
my_record=(105,"apill",751)                                   #tuple in python ()

cursor.execute(my_query,my_record);    

connection.commit()
count=cursor.rowcount
print('Record Inserrt Successful ,The number of rows in the table are ')
print(count)



