import os

import psycopg2


class db:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="173.212.221.185",
            port="5555",
            database="sofos",
            user="belit",
            password="12897",
        )

    def get_cursor(self):
        self.curr = self.conn.cursor()

    def fetchh(self):
        return self.curr.fetchall()

    def get_token(self, number: str):
        if number!='0' and number!=''and number.isdigit():
            self.get_cursor()
            
            self.curr.execute(f"select * from guests where renum={number};")
            data = self.curr.fetchall()[0]
            print(data)
            if data[4]=='False':
                self.curr.execute(f'update guests set checkin=True where renum={number}')
                self.conn.commit()

            self.curr.close()
            return data[6], data[1],str(data[5])
        return 'No Name', 'No Number', 'No Code'
    
    def update_token(self,number:str, tokens:int):
        self.get_cursor()
        self.curr.execute(f'update guests set tokens={tokens} where renum={number}')
        self.conn.commit()
        self.curr.close()

    # generate_qr(person[5])

class person:
    def __init__(self) -> None:
        self.renum = "0"
        self.token="0"
        self.name = "None"

    def info(self):
        return self.renum, self.token
