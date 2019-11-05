import psycopg2

#connexting the database
try :  
    connection = psycopg2.connect(user="kunal",
                                  password="9011525149",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="bikebuddy")

    f=open("users.txt","r")                                     #opening source file
    cursor = connection.cursor()


    my_query="""insert into user1 values(%s,%s,%s);"""           #query to execute 

    for i in range(10) :
        line=f.readline()                                               #reading a line from file
        my_record=line.split(',',3)                                     #tokenizing using  split which returns a list of elements 
        cursor.execute(my_query,my_record);                             #one list is passed at a time for insertion
        connection.commit()
        count=cursor.rowcount
        print('Record Inserrt Successful ,The number of rows in the table are ', count)

#error case
except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)


finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


print('end')