########################### DO NOT MODIFY THIS SECTION ##########################
#################################################################################
import sqlite3
from sqlite3 import Error
import csv
#################################################################################

## Change to False to disable Sample
SHOW = False

############### SAMPLE CLASS AND SQL QUERY ###########################
######################################################################
class Sample():
    def sample(self):
        try:
            connection = sqlite3.connect("sample")
            connection.text_factory = str
        except Error as e:
            print("Error occurred: " + str(e))
        print('\033[32m' + "Sample: " + '\033[m')
        
        # Sample Drop table
        connection.execute("DROP TABLE IF EXISTS sample;")
        # Sample Create
        connection.execute("CREATE TABLE sample(id integer, name text);")
        # Sample Insert
        connection.execute("INSERT INTO sample VALUES (?,?)",("1","test_name"))
        connection.commit()
        # Sample Select
        cursor = connection.execute("SELECT * FROM sample;")
        print(cursor.fetchall())

######################################################################

class HW2_sql():
    ############### DO NOT MODIFY THIS SECTION ###########################
    ######################################################################
    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            connection.text_factory = str
        except Error as e:
            print("Error occurred: " + str(e))
    
        return connection

    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            if query == "":
                return "Query Blank"
            else:
                cursor.execute(query)
                connection.commit()
                return "Query executed successfully"
        except Error as e:
            return "Error occurred: " + str(e)
    ######################################################################
    ######################################################################

    # GTusername [0 points]
    def GTusername(self):
        gt_username = "atorres78"
        return gt_username
    
    # Part a.i Create Tables [2 points]
    def part_ai_1(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_ai_1_sql = "CREATE TABLE movies(id INTEGER, title TEXT, score REAL);"
        ######################################################################
        
        return self.execute_query(connection, part_ai_1_sql)

    def part_ai_2(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_ai_2_sql = "CREATE TABLE movie_cast(movie_id INTEGER, cast_id INTEGER, cast_name TEXT, birthday TEXT, popularity REAL);"

        ######################################################################
        
        return self.execute_query(connection, part_ai_2_sql)
    
    # Part a.ii Import Data [2 points]
    def part_aii_1(self,connection,path):
        ############### CREATE IMPORT CODE BELOW ############################
        with open( path, newline='', encoding='utf8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')

            for row in reader:
                
                # id, title, row
                movie = (row[0], row[1], row[2])

                sql = "INSERT INTO movies(id, title, score) VALUES(?,?,?)"
                cur = connection.cursor()
                cur.execute(sql, movie)
                connection.commit()                
       ######################################################################
        
        sql = "SELECT COUNT(id) FROM movies;"
        cursor = connection.execute(sql)
        return cursor.fetchall()[0][0]
    
    def part_aii_2(self,connection, path):
        ############### CREATE IMPORT CODE BELOW ############################
        with open( path, newline='', encoding='utf8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')

            for row in reader:                
                # movie_id, cast_id, cast_name, birthday, popularity
                movie = (row[0], row[1], row[2], row[3], row[4])

                sql = "INSERT INTO movie_cast(movie_id, cast_id, cast_name, birthday, popularity) VALUES(?,?,?,?,?)"
                cur = connection.cursor()
                cur.execute(sql, movie)
                connection.commit()          
        ######################################################################
        
        sql = "SELECT COUNT(cast_id) FROM movie_cast;"
        cursor = connection.execute(sql)
        return cursor.fetchall()[0][0]

    # Part a.iii Vertical Database Partitioning [5 points]
    def part_aiii(self,connection):
        ############### EDIT CREATE TABLE SQL STATEMENT ###################################
        part_aiii_sql = "CREATE TABLE cast_bio(cast_id INTEGER, cast_name TEXT, birthday TEXT);"
        ######################################################################
        
        self.execute_query(connection, part_aiii_sql)
        
        ############### CREATE IMPORT CODE BELOW ############################
        part_aiii_insert_sql = "INSERT INTO cast_bio( cast_id, cast_name, birthday) "\
                               "SELECT DISTINCT cast_id, cast_name, birthday FROM movie_cast;"
        ######################################################################
        
        self.execute_query(connection, part_aiii_insert_sql)
        
        sql = "SELECT COUNT(cast_id) FROM cast_bio;"
        cursor = connection.execute(sql)
        return cursor.fetchall()[0][0]
       

    # Part b Create Indexes [1 points]
    def part_b_1(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_b_1_sql = "CREATE INDEX movie_index "\
                        "ON movies(id);"
        ######################################################################
        return self.execute_query(connection, part_b_1_sql)
    
    def part_b_2(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_b_2_sql = "CREATE INDEX cast_index "\
                       "ON movie_cast(cast_id);"
        ######################################################################
        return self.execute_query(connection, part_b_2_sql)
    
    def part_b_3(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_b_3_sql = "CREATE INDEX cast_bio_index "\
                        "ON cast_bio(cast_id);"
        ######################################################################
        return self.execute_query(connection, part_b_3_sql)
    
    # Part c Calculate a Proportion [3 points]
    def part_c(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_c_sql = 'SELECT '\
                       'printf( "%.2f", (1.0 * count(*) / ' \
                           '(select count(*) from movies)) * 100) '\
                     'FROM movies '\
                     'WHERE title LIKE "%war%" '\
                     'AND score > 50'
        ######################################################################
        cursor = connection.execute(part_c_sql)
        return cursor.fetchall()[0][0]

    # Part d Find the Most Prolific Actors [4 points]
    def part_d(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_d_sql = "SELECT mc.cast_name, count(*) as total "\
                     "FROM movies AS m INNER JOIN movie_cast AS mc ON m.id = mc.movie_id "\
                     "WHERE mc.popularity > 10 "\
                     "GROUP BY mc.cast_id "\
                     "ORDER BY total DESC, mc.cast_name "\
                     "LIMIT 5;"
        ######################################################################
        cursor = connection.execute(part_d_sql)
        return cursor.fetchall()

    # Part e Find the Highest Scoring Movies With the Least Amount of Cast [4 points]
    def part_e(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_e_sql = \
        """
        SELECT m.title, printf( "%.2f", m.score) AS score, count(mc.cast_id) as total
        FROM movies m INNER JOIN movie_cast mc ON m.id = mc.movie_id
        GROUP BY m.title
        ORDER BY m.score DESC, total, m.title
        LIMIT 5;
        """
        XX_part_e_sql = \
        """
        SELECT m.title, printf( "%.2f", m.score) AS score,  count(mc.cast_id) AS total
        FROM 
            ( SELECT id, title, score
              FROM movies
              ORDER BY score DESC
              LIMIT 5 ) m
        INNER JOIN movie_cast mc ON m.id = mc.movie_id
        GROUP BY m.title
        ORDER BY total, m.title;        
        """
        ######################################################################
        cursor = connection.execute(part_e_sql)
        return cursor.fetchall()
    
    # Part f Get High Scoring Actors [4 points]
    def part_f(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_f_sql = 'SELECT mc.cast_id, mc.cast_name, printf( "%.2f",AVG(m.score)) AS average_score '\
                    'FROM movie_cast mc INNER JOIN movies m ON m.id = mc.movie_id '\
                    'WHERE m.score > 25 '\
                    'GROUP BY mc.cast_id '\
                    'HAVING count(m.id) > 2 '\
                    'ORDER BY average_score DESC, mc.cast_name '\
                    'LIMIT 10; '        
        ######################################################################
        cursor = connection.execute(part_f_sql)
        return cursor.fetchall()

    # Part g Creating Views [6 points]
    def part_g(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_g_sql = \
        """        
        CREATE VIEW good_collaboration( 
                                        cast_member_id1, 
                                        cast_member_id2, 
                                        movie_count, 
                                        average_movie_score)
        AS
            SELECT
                mc1.cast_id as actor_a, 
                mc2.cast_id as actor_b,
                count(mc1.movie_id) as casted_together,
                AVG(m.score) as average
            from movie_cast mc1 
            join movie_cast mc2 
                on mc1.movie_id = mc2.movie_id
                and mc1.cast_id < mc2.cast_id
            join movies m
                on mc1.movie_id = m.id
            group by mc1.cast_id, mc2.cast_id
            having casted_together >= 3 AND average >= 40
            order by casted_together desc;
        """
        ######################################################################
        return self.execute_query(connection, part_g_sql)
    
    def part_gi(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_g_i_sql = \
        """
        SELECT id AS cast_id, bio.cast_name as cast_name, printf( "%.2f", AVG(average_movie_score)) AS collaboration_score
        FROM
        (
            SELECT cast_member_id1 AS id, average_movie_score
            FROM good_collaboration g
            UNION ALL
            SELECT cast_member_id2 AS id, average_movie_score
            FROM good_collaboration g
        ) c
        INNER JOIN cast_bio bio ON c.id = bio.cast_id
        GROUP BY ID
        ORDER BY collaboration_score DESC, cast_name
        LIMIT 5;
        """
        ######################################################################
        cursor = connection.execute(part_g_i_sql)
        return cursor.fetchall()
    
    # Part h FTS [4 points]
    def part_h(self,connection,path):
        ############### EDIT SQL STATEMENT ###################################
        part_h_sql = "CREATE VIRTUAL TABLE movie_overview USING fts3(id, overview);"
        ######################################################################
        connection.execute(part_h_sql)
        ############### CREATE IMPORT CODE BELOW ############################
        with open( path, newline='', encoding='utf8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')

            for row in reader:
                
                # id, overview
                movie = (row[0], row[1])

                sql = "INSERT INTO movie_overview(id, overview) VALUES(?,?)"
                cur = connection.cursor()
                cur.execute(sql, movie)
                connection.commit()            
        ######################################################################
        sql = "SELECT COUNT(id) FROM movie_overview;"
        cursor = connection.execute(sql)
        return cursor.fetchall()[0][0]
        
    def part_hi(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_hi_sql = """\
            SELECT count(*)
            FROM movie_overview
            WHERE overview MATCH 'fight';
        """
        ######################################################################
        cursor = connection.execute(part_hi_sql)
        return cursor.fetchall()[0][0]
    
    def part_hii(self,connection):
        ############### EDIT SQL STATEMENT ###################################
        part_hii_sql = """\
            SELECT count(*)
            FROM movie_overview
            WHERE overview MATCH 'space NEAR/5 program';
        """
        ######################################################################
        cursor = connection.execute(part_hii_sql)
        return cursor.fetchall()[0][0]


if __name__ == "__main__":
    
    ########################### DO NOT MODIFY THIS SECTION ##########################
    #################################################################################
    if SHOW == True:
        sample = Sample()
        sample.sample()

    print('\033[32m' + "Q2 Output: " + '\033[m')
    db = HW2_sql()
    try:
        conn = db.create_connection("Q2")
    except:
        print("Database Creation Error")

    try:
        conn.execute("DROP TABLE IF EXISTS movies;")
        conn.execute("DROP TABLE IF EXISTS movie_cast;")
        conn.execute("DROP TABLE IF EXISTS cast_bio;")
        conn.execute("DROP VIEW IF EXISTS good_collaboration;")
        conn.execute("DROP TABLE IF EXISTS movie_overview;")
    except:
        print("Error in Table Drops")

    try:
        print('\033[32m' + "part ai 1: " + '\033[m' + str(db.part_ai_1(conn)))
        print('\033[32m' + "part ai 2: " + '\033[m' + str(db.part_ai_2(conn)))
    except:
         print("Error in Part a.i")

    try:
        print('\033[32m' + "Row count for Movies Table: " + '\033[m' + str(db.part_aii_1(conn,"data/movies.csv")))
        print('\033[32m' + "Row count for Movie Cast Table: " + '\033[m' + str(db.part_aii_2(conn,"data/movie_cast.csv")))
    except:
        print("Error in part a.ii")

    try:
        print('\033[32m' + "Row count for Cast Bio Table: " + '\033[m' + str(db.part_aiii(conn)))
    except:
        print("Error in part a.iii")

    try:
        print('\033[32m' + "part b 1: " + '\033[m' + db.part_b_1(conn))
        print('\033[32m' + "part b 2: " + '\033[m' + db.part_b_2(conn))
        print('\033[32m' + "part b 3: " + '\033[m' + db.part_b_3(conn))
    except:
        print("Error in part b")

    try:
        print('\033[32m' + "part c: " + '\033[m' + str(db.part_c(conn)))
    except:
        print("Error in part c")

    try:
        print('\033[32m' + "part d: " + '\033[m')
        for line in db.part_d(conn):
            print(line[0],line[1])
    except:
        print("Error in part d")

    try:
        print('\033[32m' + "part e: " + '\033[m')
        for line in db.part_e(conn):
            print(line[0],line[1],line[2])
    except:
        print("Error in part e")

    try:
        print('\033[32m' + "part f: " + '\033[m')
        for line in db.part_f(conn):
            print(line[0],line[1],line[2])
    except:
        print("Error in part f")
    
    try:
        print('\033[32m' + "part g: " + '\033[m' + str(db.part_g(conn)))
        print('\033[32m' + "part g.i: " + '\033[m')
        for line in db.part_gi(conn):
            print(line[0],line[1],line[2])
    except:
        print("Error in part g")

    try:   
        print('\033[32m' + "part h.i: " + '\033[m'+ str(db.part_h(conn,"data/movie_overview.csv")))
        print('\033[32m' + "Count h.ii: " + '\033[m' + str(db.part_hi(conn)))
        print('\033[32m' + "Count h.iii: " + '\033[m' + str(db.part_hii(conn)))
    except:
        print("Error in part h")

    conn.close()
    #################################################################################
    #################################################################################
  
