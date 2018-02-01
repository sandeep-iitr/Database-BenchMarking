import happybase

hostName='localhost'
tableName='HBase-Test'
column_family_name='cerebral-cortex'
column_qualifier_name='acc'

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
              column_family_name: dict(),  # use defaults
              }
             )
        print('Table',tableName, 'created')

def InsertData(data):
    connection = happybase.Connection(hostName)
    connection.open()
    table = connection.table(tableName)
    column_name = '{fam}:{qual}'.format(fam=column_family_name,qual=column_qualifier_name)
    row_key = 'row_key{}'.format(123)
    table.put(row_key, {column_name: data})

def GetData():
    print('Getting a single data by row key.')
    connection = happybase.Connection(hostName)
    connection.open()
    table = connection.table(tableName)
    key = 'row_key123'.encode('utf-8')
    column_name = '{fam}:{qual}'.format(fam=column_family_name,qual=column_qualifier_name)
    row = table.row(key)
    print('\t{}: {}'.format(key, row[column_name.encode('utf-8')]))

