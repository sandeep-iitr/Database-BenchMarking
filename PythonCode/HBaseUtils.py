import happybase

hostName='localhost'
tableName='HBase-Test'

# Creating the Table in which we will insert the data
def CreateTable():
    connection = happybase.Connection(hostName)
    connection.open()
    tables = connection.tables()
    if tableName.encode() in tables :
        print('Table', tableName,'already exist')
    else:
        print(tables)
        connection.create_table(
             tableName,
             {
              'cerebral-cortex': dict(),  # use defaults
              }
             )
        print('Table',tableName, 'created')

def InsertData():
    