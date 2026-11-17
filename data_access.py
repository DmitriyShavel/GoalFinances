from config import config
import psycopg2
from psycopg2.extras import DictCursor
class DbFunctions:
    def __init__(self,config=config):
        self.conn = psycopg2.connect(**config)
        self.cursor = self.conn.cursor(cursor_factory=DictCursor)
        
        
    def create_new_account(self,card_name,goal_balance=None):
        sql_insert = 'INSERT INTO accounts(card_name,goal_balance) VALUES (%s,%s)'
        self.cursor.execute(sql_insert,(card_name,goal_balance))
        self.conn.commit()
        
        
    def add_balance(self,account_id,amount,transaction_type = 'Пополнение',description = None):
        sql_insert = 'INSERT INTO transactions(account_id,amount,transaction_type,description) VALUES (%s,%s,%s,%s);'
        self.cursor.execute(sql_insert,(account_id,amount,transaction_type,description))
        sql_update = 'UPDATE accounts SET balance = balance + %s WHERE id = %s'
        self.cursor.execute(sql_update,(amount,account_id))
        self.conn.commit()
    
    def out_balance(self,account_id,amount,transaction_type='Расход',description = None):
        sql_insert = 'INSERT INTO transactions(account_id,amount,transaction_type,description) VALUES (%s,%s,%s,%s);'
        self.cursor.execute(sql_insert,(account_id,amount,transaction_type,description))
        sql_update = 'UPDATE accounts SET balance = balance - %s WHERE id = %s'
        self.cursor.execute(sql_update,(amount,account_id))
        self.conn.commit()
        
        
    def transfer_balance(self,from_account_id,receiver_account_id,amount,transaction_type='Перевод',description = None):
        try:
            sql_insert = 'INSERT INTO TRANSACTIONS(account_id,amount,transaction_type,description) VALUES (%s,%s,%s,%s);'
            self.cursor.execute(sql_insert,(from_account_id,amount,transaction_type,description))
            sql_update = 'UPDATE accounts SET balance = balance - %s WHERE id = %s'
            self.cursor.execute(sql_update,(amount,from_account_id))
            sql_update = 'UPDATE accounts SET balance = balance + %s WHERE id = %s'
            self.cursor.execute(sql_update,(amount,receiver_account_id))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise
    def get_accounts(self):
        sql_select = 'SELECT * FROM accounts ORDER BY id;'
        self.cursor.execute(sql_select)
        data = self.cursor.fetchall()
        return data
    
    
    def get_transactions(self):
        sql_select = '''SELECT accounts.card_name,transactions.transaction_type,transactions.amount,COALESCE(transactions.description,'No comments') as description,transactions.date_time
                        FROM transactions JOIN accounts ON transactions.account_id = accounts.id ORDER BY date_time DESC LIMIT 10;'''
        self.cursor.execute(sql_select)
        data = self.cursor.fetchall()
        return data
    
    
    def close_connection(self):
        self.cursor.close()
        self.conn.close()