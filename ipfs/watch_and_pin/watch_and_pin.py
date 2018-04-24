import ipfsapi, requests, json
from pprint import pprint

### Configuration
nodeos_url = 'http://localhost:8888'
eos_scope = "ipfs"
eos_contract = "ipfs"
tables = [{"name": "blog", "column": "hash"}]
BATCH_SIZE = 100
### End of configuration

api = ipfsapi.connect('127.0.0.1', 5001)

def main():
    for table in tables:
        rows = get_rows(table['name'])
        for row in rows:
            hash = row[table['column']]
            print (hash)
            api.pin_add(hash)




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
        return -1
    return max(rows, key=lambda x: x['id'])['id']


if __name__ == '__main__':
    main()
