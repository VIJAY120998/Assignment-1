import streamlit as st
import mysql.connector
import pandas as pd

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vijay@120998",
    database="tennis_db"
)
cursor = conn.cursor(dictionary=True)

# Tennis Database as A Title
st.title('Tennis Data Base')

def dynamic_query1():
    query = "SELECT * FROM Competitions_table"
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    st.header('Competitions_table')
    st.dataframe(df)
def dynamic_query2():
    Query1 = "SELECT * FROM categories_table"
    cursor.execute(Query1)
    data = cursor.fetchall()
    df1 = pd.DataFrame(data)
    st.header('Categories_table')
    st.dataframe(df1)
def dynamic_query3():
    Query2 = "select * from complexes_table"
    cursor.execute(Query2)
    data = cursor.fetchall()
    df2 = pd.DataFrame(data)
    st.header('Complexes_table')
    st.dataframe(df2)
def dynamic_query4():
    Query3 = 'select * from venues_table'
    cursor.execute(Query3)
    data = cursor.fetchall()
    df3 = pd.DataFrame(data)
    st.header('Venues_table')
    st.dataframe(df3)
def dynamic_query5():
    Query4 = 'select * from competitor_rankings_table'
    cursor.execute(Query4)
    data = cursor.fetchall()
    df4 = pd.DataFrame(data)
    st.header('Competitor_rankings_table')
    st.dataframe(df4)

def dynamic_query6():
    Query5 = 'select * from competitor_table'
    cursor.execute(Query5)
    data = cursor.fetchall()
    df5 = pd.DataFrame(data)
    st.header('Competitor_table')
    st.dataframe(df5)


selected_table = st.sidebar.selectbox("Select the Table :",["Select",'categories_table','competitions_table','competitor_rankings_table',
'competitor_table','complexes_table','venues_table'])

if st.sidebar.button('Show Data'):
    if selected_table == 'categories_table':
        dynamic_query2()
        
    elif selected_table == 'competitions_table':
        dynamic_query1()
        
    elif selected_table == 'complexes_table':
        dynamic_query3()
        
    elif selected_table == 'venues_table':
        dynamic_query4()
        
    elif selected_table == 'competitor_rankings_table':
        dynamic_query5()
        
    elif selected_table == 'competitor_table':
        dynamic_query6()        
    else:
        st.write("Kindly Select the Table First")


# SQL Queries 
q1 = '1) List all competitions along with their category name'
q2 = '2) Count the number of competitions in each category'
q3 = "3) Find all competitions of type 'doubles'"
q4 = "4) Get competitions that belong to a specific category (e.g., ITF Men)"
q5 = "5) Identify parent competitions and their sub-competitions"
q6 = "6) Analyze the distribution of competition types by category"
q7 = "7) List all competitions with no parent (top-level competitions)"

q8 = '8) List all venues along with their associated complex name'
q9 = "9) Count the number of venues in each complex"
q10 = "10) Get details of venues in a specific country (e.g., Chile)'"
q11 = "11) Identify all venues and their timezones"
q12 = "12) Find complexes that have more than one venue"
q13 = "13) List venues grouped by country"
q14 = "14) Find all venues for a specific complex (e.g., Nacional)"

q15 = "15) Get all competitors with their rank and points."
q16 = "16) Find competitors ranked in the top 5"
q17 = "17) List competitors with no rank movement (stable rank)"
q18 = "18) Get the total points of competitors from a specific country (e.g., Croatia)"
q19 = "19) Count the number of competitors per country"
q20 = "20) Find competitors with the highest points"

def Competition_Question_1():
    cursor.execute('''SELECT competitions_table.competition_name, categories_table.category_name FROM competitions_table JOIN categories_table 
                ON competitions_table.category_id = categories_table.category_id
                ''')
    Q1 = cursor.fetchall()
    data = Q1
    df = pd.DataFrame(data)
    st.dataframe(df)
        
def Competition_Question_2():
    cursor.execute('''select categories_table.category_name , count(competitions_table.competition_name) as competition_count from competitions_table 
    join categories_table on competitions_table.category_id = categories_table.category_id group by categories_table.category_name;''')
    Q2 = cursor.fetchall()
    data = Q2
    df = pd.DataFrame(data)
    st.dataframe(df)

def Competition_Question_3():
    cursor.execute('''select competition_name , type from competitions_table where type = "doubles" ''')
    Q3 = cursor.fetchall()
    data = Q3
    df = pd.DataFrame(data)
    st.dataframe(df)

def Competition_Question_4():
    cursor.execute('''select competitions_table.competition_name , categories_table.category_name from competitions_table join categories_table 
on competitions_table.category_id = categories_table.category_id where categories_table.category_name = 'ITF Men'
''')
    Q4 = cursor.fetchall()
    data = Q4
    df = pd.DataFrame(data)
    st.dataframe(df)

def Competition_Question_5():
    cursor.execute('''select distinct parent_id , count(competition_name) as count from competitions_table group by parent_id''')
    Q5 = cursor.fetchall()
    data = Q5
    df = pd.DataFrame(data)
    st.dataframe(df)

def Competition_Question_6():
    cursor.execute('''select categories_table.category_name , count(competitions_table.competition_name) as competition_count from competitions_table 
    join categories_table on competitions_table.category_id = categories_table.category_id group by categories_table.category_name order by competition_count desc;''')
    Q6 = cursor.fetchall()
    data = Q6
    df = pd.DataFrame(data)
    st.dataframe(df)
        
def Competition_Question_7():
    cursor.execute('''select competition_id , competition_name from competitions_table where parent_id is null''')
    Q7 = cursor.fetchall()
    data = Q7
    df = pd.DataFrame(data)
    st.dataframe(df)
    
def Complexes_Question_1():
    cursor.execute('''select c.complex_name , v.venue_name from complexes_table c join venues_table v 
    on c.complex_id = v.complex_id ; ''')
    Q1 = cursor.fetchall()
    data = Q1
    df = pd.DataFrame(data)
    st.dataframe(df)

def Complexes_Question_2():
    cursor.execute('''select c.complex_name , count(v.venue_id) as No_of_Venue from complexes_table c join venues_table v 
    on c.complex_id = v.complex_id group by complex_name;''')
    Q2 = cursor.fetchall()
    data = Q2
    df = pd.DataFrame(data)
    st.dataframe(df)

def Complexes_Question_3():
    cursor.execute('''select venue_name , country_name from venues_table where country_name = 'Chile';''')
    Q3 = cursor.fetchall()
    data = Q3
    df = pd.DataFrame(data)
    st.dataframe(df)
    
def Complexes_Question_4():
    cursor.execute('''select venue_name , timezone from venues_table;''')
    Q4 = cursor.fetchall()
    data = Q4
    df = pd.DataFrame(data)
    st.dataframe(df)
        
def Complexes_Question_5():
    cursor.execute('''select c.complex_name , count(v.venue_name) as venue_count from complexes_table c join venues_table v 
    on c.complex_id = v.complex_id group by c.complex_name having count(venue_name) > 1 ;
    ''')
    Q5 = cursor.fetchall()
    data = Q5
    df = pd.DataFrame(data)
    st.dataframe(df)
        
def Complexes_Question_6():
    cursor.execute('''SELECT country_name, GROUP_CONCAT(venue_name SEPARATOR ' , ') AS venues 
    FROM venues_table GROUP BY country_name;
    ''')
    Q6 = cursor.fetchall()
    data = Q6
    df = pd.DataFrame(data)
    st.dataframe(df)

def Complexes_Question_7():
    cursor.execute('''select v.venue_name , c.complex_name from complexes_table c join venues_table v 
    on c.complex_id = v.complex_id having c.complex_name = 'Nacional';
    ''')
    Q7 = cursor.fetchall()
    data = Q7
    df = pd.DataFrame(data)
    st.dataframe(df)
    
def Competitor_Question_1():
    cursor.execute('''select competitor_table.name , competitor_rankings_table.`rank` , competitor_rankings_table.points
from competitor_table join competitor_rankings_table on
competitor_table.competitor_id = competitor_rankings_table.competitor_id;''')
    Q1 = cursor.fetchall()
    data = Q1
    df = pd.DataFrame(data)
    st.dataframe(df)
        
def Competitor_Question_2():
    cursor.execute('''select * from competitor_rankings_table order by `rank` limit 5;''')
    Q2 = cursor.fetchall()
    data = Q2
    df = pd.DataFrame(data)
    st.dataframe(df)
        
        
def Competitor_Question_3():
    cursor.execute('''select * from competitor_rankings_table where movement = 0;''')
    Q3 = cursor.fetchall()
    data = Q3
    df = pd.DataFrame(data)
    st.dataframe(df)
        
        
def Competitor_Question_4():
    cursor.execute('''select competitor_table.country , sum(competitor_rankings_table.points) as Total_Points from competitor_table join
competitor_rankings_table on competitor_table.Competitor_id = competitor_rankings_table.Competitor_id 
where competitor_table.country = 'Croatia' group by competitor_table.country;
''')
    Q4 = cursor.fetchall()
    data = Q4
    df = pd.DataFrame(data)
    st.dataframe(df)
        
def Competitor_Question_5():
    cursor.execute('''select competitor_table.country , count(competitor_rankings_table.competitor_id) as No_of_Competitors from competitor_table join
competitor_rankings_table on competitor_table.Competitor_id = competitor_rankings_table.Competitor_id 
group by competitor_table.country;''')
    Q5 = cursor.fetchall()
    data = Q5
    df = pd.DataFrame(data)
    st.dataframe(df)
        
def Competitor_Question_6():
    cursor.execute('''select * , competitor_table.name from competitor_rankings_table join competitor_table
on competitor_table.competitor_id = competitor_rankings_table.competitor_id 
order by points desc limit 5;''')
    Q6  = cursor.fetchall()
    data = Q6
    df = pd.DataFrame(data)
    st.dataframe(df)

st.title("SQL Queries")
select_q = st.selectbox("Select the Question", ["Select",q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20])

if st.button ('Run Queries'):  
    if select_q == q1:
        Competition_Question_1()
    elif select_q == q2:
        Competition_Question_2()
    elif select_q == q3:
        Competition_Question_3()
    elif select_q == q4:
        Competition_Question_4()
    elif select_q == q5:
        Competition_Question_5()
    elif select_q == q6:
        Competition_Question_6()
    elif select_q == q7:
        Competition_Question_7()
    elif select_q == q8:
        Complexes_Question_1()
    elif select_q == q9:
        Complexes_Question_2()
    elif select_q == q10:
        Complexes_Question_3()
    elif select_q == q11:
        Complexes_Question_4()
    elif select_q == q12:
        Complexes_Question_5()
    elif select_q == q13:
        Complexes_Question_6()
    elif select_q == q14:
        Complexes_Question_7()    
    elif select_q == q15:
        Competitor_Question_1()
    elif select_q == q16:
        Competitor_Question_2()
    elif select_q == q17:
        Competitor_Question_3()
    elif select_q == q18:
        Competitor_Question_4()
    elif select_q == q19:
        Competitor_Question_5()
    elif select_q == q20:
        Competitor_Question_6()
    else:
        st.write("Kindly Select the Question")
# Close Connection  
cursor.close()
conn.close()