import os
from datetime import datetime

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
        self.conn.autocommit = True
        self.table = "guests_new"

    def get_cursor(self):
        self.__init__()
        self.curr = self.conn.cursor()

    def fetchh(self):
        return self.curr.fetchall()

    def get_token(self, number: str, just_token=False):
        if number != "0" and number != "" and number.isdigit():
            self.get_cursor()

            self.curr.execute(f"select * from {self.table} where renum={number};")
            data = self.curr.fetchall()[0]
            print(data)
            if data[5] != "True":
                self.curr.execute(
                    f"update {self.table} set checkin=True where renum={number}"
                )
                self.curr.execute(
                    f"update {self.table} set date='{datetime.now()}' where renum={number}"
                )
                # self.conn.commit()

            self.curr.close()
            self.conn.close()
            if just_token:
                return data[7], str(data[3])

            print(f"{str(data[3])} has {data[7]} tokens")
            return (
                data[7],
                data[1],
                str(data[3]),
                "OK" if str(data[5]) == "True" else "None",
            )
        self.conn.close()
        return "No Name", "No Number", "No Code", "No Checkin"

    def update_token(self, number: str, tokens: int):
        self.get_cursor()
        print("update tokennnnnn")
        # print(number)
        self.curr.execute(
            f"update {self.table} set tokens={tokens} where renum={number}"
        )
        self.conn.commit()
        print(f"{tokens} added to {number}")
        self.curr.close()
        self.conn.close()

    def insert_new(self, name: str, ekleyen: str):
        self.get_cursor()
        print("insert new")
        # print(number)
        self.curr.execute(
            f"INSERT INTO {self.table} (isim,kaydeden) VALUES('{name}','{ekleyen}') returning renum;"
        )
        id = self.curr.fetchall()[0][0]
        self.conn.commit()
        # print(f"{tokens} added to {number}")
        self.curr.close()
        self.conn.close()
        return id

    # generate_qr(person[5])


class person:
    def __init__(self) -> None:
        self.renum = "0"
        self.oldrenum = "0"
        self.token = "0"
        self.name = "None"
        self.checkin = "False"
