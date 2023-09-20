    
class GeneralQueries:

    @classmethod
    def count_table_elements(cls, connector, table_name: str):
        query = f'SELECT COUNT(*) from {table_name}'
        try:
            connector.mycursor.execute(query)            
            res = connector.mycursor.fetchone() 
            return res[0]
        except Exception as e:
            raise e 
        

    @classmethod
    def get_table_elements(cls, connector, table_name:str):
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
