import unittest
from Q2_SQL import HW2_sql

class Test_Q1(unittest.TestCase):

    def test_part_aii_1(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        qtde = db.part_aii_1(conn,"data/movies.csv")

        self.assertEqual( qtde, 2484)
    
    def test_part_aii_2(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        qtde = db.part_aii_2(conn,"data/movie_cast.csv")

        self.assertEqual( qtde, 23380)       

    def test_part_aiii(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        qtde = db.part_aiii(conn)

        self.assertEqual( qtde, 18938)      

    def test_part_b_1(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        resultado = db.part_b_1(conn)

        self.assertEqual( resultado, 'Query executed successfully' )        

    def test_part_b_2(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        resultado = db.part_b_2(conn)

        self.assertEqual( resultado, 'Query executed successfully' )                      

    def test_part_b_3(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        resultado = db.part_b_3(conn)

        self.assertEqual( resultado, 'Query executed successfully' )  

    def test_part_c(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        resultado = db.part_c(conn)

        self.assertEqual( resultado, '0.08' )      

    def test_part_d(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        resultado = db.part_d(conn)
        check = [('Mark Hamill', 17), ('Harrison Ford', 14), ('Billy Dee Williams', 12), ('Patrick Stewart', 11), ('Samuel L. Jackson', 9)]
        
        self.assertEqual(resultado, check)

    def test_part_e(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        resultado = db.part_e(conn)
        check = (99.392, 'Interstellar', 37)
        print( '******')
        print( resultado )
        
        self.assertEqual( resultado[0], check )

    def test_part_f(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")        

        resultado = db.part_f(conn)
        check = (47698, 'Denis Lawson', '57.56')
        print( '******')
        print( resultado )
        
        self.assertEqual( resultado[0], check )

    def test_part_g(self):
        db = HW2_sql()
        try:
            conn = db.create_connection("Q2")
        except:
            print("Database Creation Error")   

        cursor = conn.cursor()
        cursor.execute("DROP VIEW IF EXISTS good_collaboration;")
        conn.commit()                 

        resultado = db.part_g(conn)

        self.assertEqual(resultado, 'Query executed successfully')
        