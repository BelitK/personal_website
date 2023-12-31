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
        if number!='0' and number!='':
            self.get_cursor()
            
            self.curr.execute(f"select * from guests where renum={number};")
            data = self.curr.fetchall()[0]
            print(data)
            if data[4]=='False':
                self.curr.execute(f'update guests set checkin=True where renum={number}')
                self.conn.commit()

            self.curr.close()
            return data[6]
        return 'No number'
    
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

    def info(self):
        return self.renum, self.token
    

# import pandas as pd
import psycopg2
conn = psycopg2.connect(
            host="173.212.221.185",
            port="5555",
            database="sofos",
            user="belit",
            password="12897",
        )
cur = conn.cursor()
import pandas as pd
data = pd.read_excel('a.xlsx')
data.columns=['isim','davet','telefon','mail','rev']

renum = 10367
id=367
for person in data.iterrows():
    if str(person[1]['isim'])!='nan':
        renum+=1
        id+=1
        print(person[1]['isim'])
        cur.execute(f"insert into guests (id, name, phone, checkin,renum,tokens) values('{str(id)}','{person[1]['isim']}','{str(person[1]['telefon'])}','False','{str(renum)}',0)")
