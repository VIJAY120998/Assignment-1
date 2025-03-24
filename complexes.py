# Question in Function Mode
def Complexes_Question_1():
    cursor.execute('''select c.complex_name , v.venue_name from complexes_table c join venues_table v 
on c.complex_id = v.complex_id ; ''')
    Q1 = cursor.fetchall()
    for i in Q1:
        print(i)

def Complexes_Question_2():
    cursor.execute('''select c.complex_name , count(v.venue_id) as No_of_Venue from complexes_table c join venues_table v 
on c.complex_id = v.complex_id group by complex_name;''')
    Q2 = cursor.fetchall()
    for i in Q2:
        print(i)

def Complexes_Question_3():
    cursor.execute('''select venue_name , country_name from venues_table where country_name = 'Chile';''')
    Q3 = cursor.fetchall()
    for i in Q3:
        print(i)

def Complexes_Question_4():
    cursor.execute('''select venue_name , timezone from venues_table;''')
    Q4 = cursor.fetchall()
    for i in Q4:
        print(i)
        
def Complexes_Question_5():
    cursor.execute('''select c.complex_name , count(v.venue_name) as venue_count from complexes_table c join venues_table v 
on c.complex_id = v.complex_id group by c.complex_name having count(venue_name) > 1 ;
''')
    Q5 = cursor.fetchall()
    for i in Q5:
        print(i)
        
def Complexes_Question_6():
    cursor.execute('''SELECT country_name, GROUP_CONCAT(venue_name SEPARATOR ' , ') AS venues 
FROM venues_table GROUP BY country_name;
''')
    Q6 = cursor.fetchall()
    for i in Q6:
        print(i)

def Complexes_Question_7():
    cursor.execute('''select v.venue_name , c.complex_name from complexes_table c join venues_table v 
on c.complex_id = v.complex_id having c.complex_name = 'Nacional';
''')
    Q7 = cursor.fetchall()
    for i in Q7:
        print(i)
        
# Function Calling

Complexes_Question_1()
Complexes_Question_2()
Complexes_Question_3()
Complexes_Question_4()
Complexes_Question_5()
Complexes_Question_6()
Complexes_Question_7()