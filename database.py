import sqlite3
from datetime import datetime, timedelta
from json import dumps, loads
from itertools import chain


def dict_factory(cursor, row):
    save_dict = {}

    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]

    return save_dict

class Users:
    def __init__(self, path) -> None:
        self.path = path
        self.row_factory = dict_factory
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users (
                                userID INT,
                                lang TEXT,
                                nodeAlert INT,
                                haltAlert INT,
                                voteAlert INT)""")

            try:
                cur.execute("select voteAlert from users")
            except sqlite3.OperationalError:
                cur.execute("alter table users add haltAlert INT")
                cur.execute("alter table users add voteAlert INT")
            finally:
                db.commit()

    def user_exists(self, userID):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.row_factory = self.row_factory
            return cur.execute("SELECT * FROM users WHERE userID = ?", (userID,)).fetchone()

    def add_user(self, userID):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (userID, "en", 1, 1, 1))
            db.commit()

    def change_user_settings(self, userID, setting_name, setting_value):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute(f"UPDATE users SET {setting_name} = ? WHERE userID = ?", (setting_value, userID))
            db.commit()
    
    def get_user_settings(self, userID, setting_name):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.row_factory = self.row_factory
            
            data = cur.execute(f"SELECT {setting_name} FROM users WHERE userID = ?", (userID,)).fetchone()
            return data[setting_name]

    def __iter__(self):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.row_factory = self.row_factory
            return iter(cur.execute("SELECT * FROM users").fetchall())


class Nodes:
    def __init__(self, path) -> None:
        self.path = path
        self.row_factory = dict_factory
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS nodes (
                                userID INT, ip TEXT, state TEXT
                                )""")
            try:
                cur.execute("select state from nodes")
            except sqlite3.OperationalError:
                cur.execute("alter table nodes add state TEXT")
            finally:
                db.commit()
    
    def get_user_nodes(self, userID):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.row_factory = self.row_factory
            return cur.execute("SELECT * FROM nodes WHERE userID = ?", (userID,)).fetchall()

    def get_node_state(self, ip, userID):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            data = cur.execute("select state from nodes where userID = ? and ip = ?", (userID, ip)).fetchone()
            return data[0] if data else None

    def set_node_state(self, ip, userID, state):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("update nodes set state = ? where ip = ? and userID = ?", (state, ip, userID)).fetchone()
            db.commit()

    
    def add_user_node(self, userID, ip):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO nodes VALUES (?, ?, ?)", (userID, ip, ""))
            db.commit()
    
    def remove_user_node(self, userID):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("DELETE FROM nodes WHERE userID = ?", (userID,))
            db.commit()
    
    def __iter__(self):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.row_factory = self.row_factory
            return iter(cur.execute("SELECT * from nodes").fetchall())

class NodesUptime:
    def __init__(self, path) -> None:
        self.path = path
        self.row_factory = dict_factory
        with sqlite3.connect(path) as db:
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS nodesUptime (
                                date TEXT,
                                network TEXT,
                                block_height TEXT,
                                addresses TEXT
                                )""")
            db.commit()
    
    def add_addresses(self, network, block_height, addressess):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO nodesUptime VALUES (?, ?, ?, ?)",
                                (datetime.now().isoformat(), network, block_height, dumps(addressess)))
            db.commit()

    def get_last_block_height(self, network):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.row_factory = self.row_factory
            data = cur.execute("SELECT * FROM nodesUptime where network = ?", (network,)).fetchall()
            if not data:
                return None
            return max(data, key=lambda x: datetime.fromisoformat(x["date"]))

    def get_all_addresses(self, network):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.row_factory = self.row_factory
            res = cur.execute("SELECT addresses FROM nodesUptime WHERE network = ?", (network,)).fetchall()
            res = [i["addresses"] for i in res]
            res = [loads(i) for i in res]
            return res # list of lists of addresses
            # return list(chain.from_iterable(res)) # all addresses in one list
    
    def cleanup(self):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            one_day_ago_isoformat = (datetime.now() - timedelta(days=1)).isoformat()
            cur.execute("DELETE FROM nodesUptime WHERE date < ?", (one_day_ago_isoformat,))
            db.commit()


class DiscordNews:
    def __init__(self, path):
        self.path = path
        self.row_factory = dict_factory
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS discordNews (content TEXT)")
            db.commit()

    def get_last_content(self):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            data = cur.execute("select content from discordNews").fetchall()
            return data[-1] if data else None

    def add_content(self, content):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("insert into discordNews values (?)", (content,))
            db.commit()


class Votes:
    def __init__(self, path):
        self.path = path
        self.row_factory = dict_factory
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS votes (vote_id INT)")
            db.commit()

    def get_all_votes(self):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.row_factory = self.row_factory
            data = cur.execute("select vote_id from votes").fetchall()
            return [i['vote_id'] for i in data] if data else list()

    def add_vote(self, vote_id):
        with sqlite3.connect(self.path) as db:
            cur = db.cursor()
            cur.execute("insert into votes values (?)", (vote_id,))
            db.commit()


users = Users("database.db")
nodes = Nodes("database.db")
nodesUptime = NodesUptime("database.db")
discordNews = DiscordNews("database.db")
votes = Votes("database.db")