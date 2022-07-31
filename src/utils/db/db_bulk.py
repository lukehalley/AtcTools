import sys

from src.db.actions.actions_Setup import getCursor


def update_many(dbConnection, data_list=None, mysql_table=None):

    cursor = getCursor(dbConnection=dbConnection)

    query = ""
    valuesToUpdate = []

    amountToUpdate = len(data_list)

    batchSize = 1000

    for data_dict in data_list:

        if not query:
            columns = ', '.join('`{0}`'.format(k) for k in data_dict)
            duplicates = ', '.join('{0}=VALUES({0})'.format(k) for k in data_dict)
            place_holders = ', '.join('%s'.format(k) for k in data_dict)
            query = "INSERT INTO {0} ({1}) VALUES ({2})".format(mysql_table, columns, place_holders)
            query = "{0} ON DUPLICATE KEY UPDATE {1}".format(query, duplicates)

        if data_dict is not None:

            print(data_dict)

            cleanValues = []

            if "route_id" in data_dict:
                cleanValues.append(
                    int(data_dict["route_id"])
                )
            else:
                sys.exit("No Route ID!")

            if "token_in_id" in data_dict:
                cleanValues.append(
                    int(data_dict["token_in_id"])
                )
            else:
                cleanValues.append(None)

            if "token_out_id" in data_dict:
                cleanValues.append(
                    int(data_dict["token_out_id"])
                )
            else:
                cleanValues.append(None)

            v = tuple(cleanValues)

            print(v)

            valuesToUpdate.append(v)

        cursor.executemany(query, valuesToUpdate)

        dbConnection.commit()

        x = 1
        # more logic here



    x = 1

    # cursor.close()
    # dbConnection.close()