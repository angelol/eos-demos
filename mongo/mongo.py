import requests, json
from pymongo import MongoClient
from pprint import pprint

### Configuration
mongodb_url = "mongodb://localhost/"
mongodb_db_name = "poc"
nodeos_url = 'http://localhost:8888'
eos_scope = "test"
eos_contract = "test"
tables = ['table1', 'table2']
DROP_DB_ON_EVERY_RUN = False # Turn this on if you want to import multiple times
BATCH_SIZE = 100
### End of configuration

client = MongoClient(mongodb_url)
db=getattr(client, mongodb_db_name)

def main():
    if DROP_DB_ON_EVERY_RUN:
        reset_db()
    for table in tables:
        rows = get_rows(table)
        getattr(db, table).insert_many(rows)

def get_data(table, lower_bound):
    r = requests.post(nodeos_url + '/v1/chain/get_table_rows', data=json.dumps({
        "json": True,
        "scope": eos_scope,
        "code": eos_contract,
        "table": table,
        "limit": BATCH_SIZE,
        "lower_bound": lower_bound,
        })
    )
    return r.json()

def get_rows(table):
    rows = []
    while True:
        r = get_data(table, highest_id(rows) + 1)
        rows.extend(r['rows'])
        if r['more'] == False:
            break
    return rows



def highest_id(rows):
    if not rows:
        return 0
    return max(rows, key=lambda x: x['id'])['id']

def reset_db():
    client.drop_database(mongodb_db_name)

if __name__ == '__main__':
    main()
