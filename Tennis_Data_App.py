import mysql.connector as sql  # python liberary used to connect the mysql to python
import pandas as pa            # python liberary convert the data as dataframe
import streamlit as st         # python liberary to create interactive web application


st.header("Tennis Competitions And Rank list")         # create title for the table
st.image("C:/Users/nsiva/Downloads/tennish.jpg")       # import imager in web

# Initialize session state for query results
if "query_results" not in st.session_state:        # it make sure that query results key available at initial
    st.session_state["query_results"] = None

# to connect MySQL to python streanlit
def Connect_to_database():
    try:
        return sql.connect(
            host="localhost",
            user="root",  # Add your user
            password="",  # Add your password
            database="tennis_data_api"
        )
    except Exception as e:
        st.error(f"Failed to connect to the database: {e}")
        return None

# Function to execute queries
def Execute_query(query, params=None):
    conn = Connect_to_database()
    if conn is None:
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())              # Execute query from database
        results = cursor.fetchall()                      # return result
        conn.close()
        return results
    except Exception as e:
        st.error(f"Query execution failed: {e}")
        return None

def display_table_content(query):    #Executes the query and displays the table content.
    
    try:
        results = Execute_query(query)
        if results:
            df = pa.DataFrame(results)  # Convert the query results into a DataFrame
            st.dataframe(df)  # Display the DataFrame
        else:
            st.warning("No data available in the table.")
    except Exception as e:
        st.error(f"Error loading table: {e}")


def display_all_tables():  #Displays table names when clicking a table name and shows its content.
    
    tables = {
        "Categories Table": "SELECT * FROM tennis_data_api.categories_table;",
        "Competitions Table": "SELECT * FROM tennis_data_api.competitions_table;",
        "Competitors Ranking Table": "SELECT * FROM tennis_data_api.competitor_ranking_table;",
        "Competitors Table": "SELECT * FROM tennis_data_api.competitors_table;",
        "Complexes Table": "SELECT * FROM tennis_data_api.complexes_table;",
        "Venues Table": "SELECT * FROM tennis_data_api.venues_table;"
    }

    st.subheader("Tennis Competitions Tables")
    
    # Show table names and allow users to select one
    selected_table = st.selectbox("Select a table to view its content:", options=tables.keys())
    
    if selected_table:  # Check if a table is selected
        st.write(f"### {selected_table} Content")
        query = tables[selected_table]
        display_table_content(query)

# Main function
def main():
    # Display all tables at the top
    display_all_tables()

    # Predefined queries dropdown
    st.sidebar.header("Information Request")
    queries = {
        "All Category Id & Name":"""SELECT * FROM tennis_data_api.categories_table;""",
        "All Competition Name & Type":"""SELECT * FROM tennis_data_api.competitions_table;""",
        "Ranks & points":"""SELECT * FROM tennis_data_api.competitor_ranking_table;""",
        "All Competitor Name & Country":"""SELECT * FROM tennis_data_api.competitors_table;""",
        "All Complex Id & Name":"""SELECT * FROM tennis_data_api.complexes_table;""",
        "All Commpetions venue name,country Name and Timezone":"""SELECT * FROM tennis_data_api.venues_table;""",
        "All Competitions Along their Category Name":"""
        SELECT c.category_name,
        comp.competition_name 
        FROM categories_table c 
        JOIN competitions_table comp 
        ON c.category_id = comp.category_id;
        """,
        "The Number Of Competitions In Each Category":"""
        select	c.category_name,
        count(com.competition_name) as number_of_competition 
        from categories_table c 
        join competitions_table com 
        on c.category_id = com.category_id 
        group by c.category_name;
        """,
        "Find all competitions of type 'doubles'":"""
        SELECT competition_id,
        competition_name,category_id,`type`
        from competitions_table
        where `type`='doubles';""",
        "competitions that belong to a specific category (e.g., ITF Men(sr:category:785))":"""
        SELECT competition_id,competition_name,`type`,gender,category_id
        FROM `competitions_table`
        WHERE category_id = 'sr:category:785';""",
        "List all venues along with their associated complex name":
        """SELECT c.venue_id,c.venue_name,comp.complex_name
        FROM venues_table c
        JOIN complexes_table comp
        ON c.complex_id = comp.complex_id;""",
        "Count the number of venues in each complex":"""
        select c.complex_id,c.complex_name,count(com.venue_id) as venue_count
        from complexes_table c
        join venues_table com
        on c.complex_id=com.complex_id
        group by c.complex_id,c.complex_name;""",
        "Get details of venues in a specific country (e.g., Chile)":"""
        select venue_id,venue_name,country_name
        from venues_table
        where country_name ='Chile';""",
        "Identify all venues and their timezones":"""
        select venue_id,venue_name,timezone 
        from venues_table;""",
        "Find complexes that have more than one venue":"""
        SELECT c.complex_id, com.complex_name, COUNT(c.venue_id) AS venue_count
        FROM venues_table c
        JOIN
        complexes_table com
        ON
        c.complex_id = com.complex_id
        GROUP BY
        c.complex_id, com.complex_name
        having	venue_count > 1 ;""",
        "List venues grouped by country":"""
        SELECT   country_name,
        GROUP_CONCAT(venue_name) AS venues
        FROM  venues_table
        GROUP BY country_name;""",
        "Find all venues for a specific complex (e.g., Nacional)":"""
        select	c.complex_name,com.venue_name
        from  complexes_table c
        join  venues_table com
        on   c.complex_id=com.complex_id
        having	complex_name = 'Nacional';""",
        "Get all competitors with their rank and points":"""
        select c.competitor_id,com.`name`,c.`rank`,c.points
        from    competitor_ranking_table c
        join    competitors_table com
        on c.competitor_id=com.competitor_id
        order by `rank` asc;""",
        "Find competitors ranked in the top 5":"""
        select	c.competitor_id,com.`name`,`rank`
        from competitor_ranking_table c
        join competitors_table com
        on c.competitor_id=com.competitor_id
        where `rank` <=5 ;""",
        "List competitors with no rank movement (stable rank)":"""
        select c.competitor_id,com.`name`,movement
        from competitor_ranking_table c
        join competitors_table com
        on c.competitor_id=com.competitor_id
        where movement= '0';""",
        "Get the total points of competitors from a specific country (e.g., Croatia)":"""
        select c.country,
        sum(com.points) as Total_point
        from competitors_table c
        join competitor_ranking_table com
        on c.competitor_id=com.competitor_id
        where country='India'
        group by	c.country;""",
        "Count the number of competitors per country":"""
        select country,
        count(competitor_id) as `Number of competitors`
        from	 competitors_table
        group by country
        order by country asc;""",
        "Find competitors with the highest points in the current week":"""
        select	c.`name`,com.competitor_id,
        max(com.points)as highest_point
        from competitors_table c
        join competitor_ranking_table com
        on c.competitor_id=com.competitor_id
        group by c.`name`,com.competitor_id;""",
        "Top ten Rank list":"""
        SELECT competitor_id, `rank`, points 
        FROM competitor_ranking_table  WHERE `rank` <= 500;"""
    }

    selected_query_title = st.sidebar.selectbox("Choose a Query", list(queries.keys()))      # To display the selected query title
    predefined_query_button = st.sidebar.button("Run Query")                                 

    if predefined_query_button:
        query = queries[selected_query_title]                                    # Execute the selected query and display the result in Table
        try:
            results = Execute_query(query)
            if results:
                query_results = pa.DataFrame(results)
                st.session_state["query_results"] = query_results
                st.write(f"Data Fetched: {selected_query_title}")
                st.dataframe(query_results)
            else:
                st.warning(f"No results returned for query: {selected_query_title}.")   # if not excuted display error
        except Exception as e:
            st.error(f"Error: {e}")

    # Apply filters only if query results exist
    query_results = st.session_state["query_results"] 
    if query_results is not None:
        st.sidebar.header("Apply Filters to Results")

        # Rank slider (if applicable)
        if "rank" in query_results.columns:
            min_rank = int(query_results["rank"].min())
            max_rank = int(query_results["rank"].max())
            rank_min, rank_max = st.sidebar.slider(
                "Filter by Rank",
                min_value=min_rank,
                max_value=max_rank,
                value=(min_rank, max_rank)
            )

            # Filter by rank
            filtered_results = query_results[
                (query_results["rank"] >= rank_min) & (query_results["rank"] <= rank_max)
            ]
            st.write(f"Filtered Results for Rank between {rank_min} and {rank_max}")
            st.dataframe(filtered_results)

        # General column filter
        columns = query_results.columns.tolist()
        selected_column = st.sidebar.selectbox("Choose a Column to Filter", columns)
        filter_value = st.sidebar.text_input(f"Filter Value for {selected_column} (e.g., 'value')")

        if st.sidebar.button("Apply Filter"):
            try:
                filtered_results = query_results[
                    query_results[selected_column].astype(str) == filter_value
                    ]
                st.write(f"Filtered Results for {selected_column} = '{filter_value}'")
                st.dataframe(filtered_results)
            except Exception as e:
                st.error(f"Error: {e}")
    # Feedback Section
    st.subheader("Feedback")

    # Input fields for email and feedback
    email = st.text_input("Your Email ID")
    feedback = st.text_area("Your Feedback or Suggestions")

    # Submit button
    if st.button("Submit Feedback"):
        if email.strip() == "" or feedback.strip() == "":
            st.warning("Please provide both Email ID and Feedback.")
        else:
            # Handle the feedback submission logic (e.g., save to database, send email, etc.)
            st.success("Thank you for your feedback!")
            # Example: Print or process the feedback
            st.write(f"Email: {email}")
            st.write(f"Feedback: {feedback}")

if __name__ == "__main__":
    main()