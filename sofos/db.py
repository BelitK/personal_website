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

    def get_token(self, number: str, just_token=False):
        if number!='0' and number!=''and number.isdigit():
            self.get_cursor()
            
            self.curr.execute(f"select * from guests where renum={number};")
            data = self.curr.fetchall()[0]
            print(data)
            if data[4]=='False':
                self.curr.execute(f'update guests set checkin=True where renum={number}')
                self.conn.commit()
                
            self.curr.close()
            if just_token:
                return data[6]

            print(f"{str(data[5])} has {data[6]} tokens")
            return data[6], data[1],str(data[5]), 'OK' if str(data[4])=='true' else 'None'
        return 'No Name', 'No Number', 'No Code', 'No Checkin'
    
    def update_token(self,number:str, tokens:int):
        self.get_cursor()
        print("update tokennnnnn")
        print(number)
        self.curr.execute(f'update guests set tokens={tokens} where renum={number}')
        self.conn.commit()
        print(f"{tokens} added to {number}")
        self.curr.close()

    # generate_qr(person[5])

class person:
    def __init__(self) -> None:
        self.renum = "0"
        self.oldrenum="0"
        self.token="0"
        self.name = "None"
        self.checkin='False'

