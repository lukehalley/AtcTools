from src.db.actions.actions_Setup import getCursor


def update_many(dbConnection, data_list=None, mysql_table=None):

    cursor = getCursor(dbConnection=dbConnection)

    query = ""
    values = []

    for data_dict in data_list:

        if not query:
            columns = ', '.join('`{0}`'.format(k) for k in data_dict)
            duplicates = ', '.join('{0}=VALUES({0})'.format(k) for k in data_dict)
            place_holders = ', '.join('%s'.format(k) for k in data_dict)
            query = "INSERT INTO {0} ({1}) VALUES ({2})".format(mysql_table, columns, place_holders)
            query = "{0} ON DUPLICATE KEY UPDATE {1}".format(query, duplicates)

        if data_dict is not None:
            v = list(data_dict.values())

            while len(v) < 3:
                v.append(None)

            print(v)
            values.append(v)

    print(query)

    cursor.executemany(query, values)

    dbConnection.commit()
    cursor.close()
    dbConnection.close()