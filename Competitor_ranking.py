# Sql Query's in Function 

def Competitor_Question_1():
    cursor.execute('''select competitor_table.name , competitor_rankings_table.`rank` , competitor_rankings_table.points
from competitor_table join competitor_rankings_table on
competitor_table.competitor_id = competitor_rankings_table.competitor_id;''')
    Q1 = cursor.fetchall()
    for i in Q1:
        print(i)
        
def Competitor_Question_2():
    cursor.execute('''select * from competitor_rankings_table order by `rank` limit 5;''')
    Q2 = cursor.fetchall()
    for i in Q2:
        print(i)
        
        
def Competitor_Question_3():
    cursor.execute('''select * from competitor_rankings_table where movement = 0;''')
    Q3 = cursor.fetchall()
    for i in Q3:
        print(i)
        
        
def Competitor_Question_4():
    cursor.execute('''select competitor_table.country , sum(competitor_rankings_table.points) as Total_Points from competitor_table join
competitor_rankings_table on competitor_table.Competitor_id = competitor_rankings_table.Competitor_id 
where competitor_table.country = 'Croatia' group by competitor_table.country;
''')
    Q4 = cursor.fetchall()
    for i in Q4:
        print(i)
        
def Competitor_Question_5():
    cursor.execute('''select competitor_table.country , count(competitor_rankings_table.competitor_id) as No_of_Competitors from competitor_table join
competitor_rankings_table on competitor_table.Competitor_id = competitor_rankings_table.Competitor_id 
group by competitor_table.country;''')
    Q5 = cursor.fetchall()
    for i in Q5:
        print(i)
        
def Competitor_Question_6():
    cursor.execute('''select * , competitor_table.name from competitor_rankings_table join competitor_table
on competitor_table.competitor_id = competitor_rankings_table.competitor_id 
order by points desc limit 5;''')
    Q6  = cursor.fetchall()
    for i in Q6:
        print(i)
        
Competitor_Question_1()
Competitor_Question_2()
Competitor_Question_3()
Competitor_Question_4()
Competitor_Question_5()
Competitor_Question_6()