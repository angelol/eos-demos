# EOS MongoDB Importer

This python script can be used to import all data from your EOS smart contract database into MongoDB.

## Usage
In the configuration section of the script, change these parameters to your liking:
```
### Configuration
mongodb_url = "mongodb://localhost/"
mongodb_db_name = "poc"
nodeos_url = 'http://localhost:8888'
BATCH_SIZE = 100
eos_scope = "test"
eos_contract = "test"
tables = ['table1', 'table2']
DROP_DB_ON_EVERY_RUN = False # Turn this on if you want to import multiple times
### End of configuration
```

## Limitations
It currently does not support live tracking of the changes from the chain. If you want to update the state of mongodb, you need to re-run this script again and refetch all data. Don't forget to enable DROP_DB_ON_EVERY_RUN.
