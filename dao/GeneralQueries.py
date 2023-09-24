    
from exceptions.exceptions import InvalidTableNameError

class GeneralQueries:
    __legit_table_names = {'BoardGames', 'table2', 'table3', '... insert tables here...',
                           'this is to avoid risk of non expected SQL behavior, for example, SQL Injection'}

    def check_legit_table_names(table_name: str):
        if table_name not in GeneralQueries.__legit_table_names:
            raise InvalidTableNameError(f"'{table_name}' is not a valid table name.")

    @classmethod
    def count_table_elements(cls, connector, table_name: str):
        cls.check_legit_table_names(table_name)
        query = f'SELECT COUNT(*) from {table_name}'
        try:
            connector.mycursor.execute(query)            
            res = connector.mycursor.fetchone() 
            return res[0]
        except Exception as e:
            raise e 
        

    @classmethod
    def get_table_elements(cls, connector, table_name:str):
        cls.check_legit_table_names(table_name)
        try:
            number_elements = cls.count_table_elements(connector, table_name)
        except Exception as e:
            raise e
        if number_elements>0:
            query = f'SELECT * FROM {table_name}'
            try:
                connector.mycursor.execute(query)
                results = connector.mycursor.fetchall()
                return results
            except Exception as e:
                raise e
        else:
            return []
