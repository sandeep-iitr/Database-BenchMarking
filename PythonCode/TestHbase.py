#Hbase: 0.9x or greater

# Start the Hbase
# ./start-hase.sh

# Start Thrift Server
# ./hbase thrift start

import happybase

connection = happybase.Connection('localhost')
# before first use:
connection.open()

print(connection.tables())

connection.close()


