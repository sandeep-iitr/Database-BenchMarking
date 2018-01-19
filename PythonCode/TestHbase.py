#Hbase: 0.9x or greater

# Start the Hbase
# ./start-hase.sh

# Start Thrift Server
# ./hbase thrift start

import happybase
from HBaseUtils import CreateTable

hostName='localhost'
tableName='HBase-Test'

#connection = happybase.Connection('localhost')

# before first use:
#connection.open()

# Create the table, if not already created
CreateTable()


#print(connection.tables())
#connection.close()





