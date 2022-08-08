import pandas as pd


def update_many(dbConnection, data_list=None, mysql_table=None):

    newDicts = []

    keys = data_list[0].keys()
    for data in data_list:
        if data:
            for key in keys:
                if key not in data:
                    data[key] = None
                else:
                    data[key] = f"{data[key]}"
            newDicts.append(data)

    routeIds = pd.DataFrame(newDicts, columns=['route_id', 'token_in_id', 'token_out_id'])

    routeIds['route_id'] = pd.to_numeric(routeIds['route_id'], downcast='float', errors='raise').astype('Int64')
    routeIds['token_in_id'] = pd.to_numeric(routeIds['token_in_id'], downcast='float', errors='raise').astype('Int64')
    routeIds['token_out_id'] = pd.to_numeric(routeIds['token_out_id'], downcast='float', errors='raise').astype('Int64')

    routes = pd.read_csv(r'data/db/routes_raw_new.csv')

    keysToKeep = ['route_id', 'network_id', 'dex_id', 'token_in_address',
                  'token_out_address', 'route', 'method', 'transaction_hash',
                  'block_number', 'amount_in', 'amount_out', 'tx_timestamp', 'created_at']

    merged = pd.merge(routeIds, routes[keysToKeep], on=['route_id'])

    merged = merged.astype(str)

    merged = merged.where(pd.notnull(merged), None)

    merged = merged.replace("<NA>", r"\N")

    merged = merged.replace("nan", r"\N")

    merged = merged.replace("", r"\N")

    merged['route'] = merged['route'].str.replace(', ', '-')

    order = ['route_id',
             'network_id',
             'dex_id',
             'token_in_id',
             'token_in_address',
             'token_out_id',
             'token_out_address',
             'route',
             'method',
             'transaction_hash',
             'block_number',
             'amount_in',
             'amount_out',
             'tx_timestamp',
             'created_at']

    mergedFinal = merged[order]

    mergedFinal.to_csv("data/db/done/routes_done.csv", index=False)

    x = 1

    # cursor = getCursor(dbConnection=dbConnection)
    #
    # query = ""
    # valuesToUpdate = []
    #
    # amountToUpdate = len(data_list)
    #
    # batchSize = 1000
    #
    # for data_dict in data_list:
    #
    #     if not query:
    #         columns = ', '.join('`{0}`'.format(k) for k in data_dict)
    #         duplicates = ', '.join('{0}=VALUES({0})'.format(k) for k in data_dict)
    #         place_holders = ', '.join('%s'.format(k) for k in data_dict)
    #         query = "INSERT INTO {0} ({1}) VALUES ({2})".format(mysql_table, columns, place_holders)
    #         query = "{0} ON DUPLICATE KEY UPDATE {1}".format(query, duplicates)
    #
    #     if data_dict is not None:
    #
    #         print(data_dict)
    #
    #         cleanValues = []
    #
    #         if "route_id" in data_dict:
    #             cleanValues.append(
    #                 int(data_dict["route_id"])
    #             )
    #         else:
    #             sys.exit("No Route ID!")
    #
    #         if "token_in_id" in data_dict:
    #             cleanValues.append(
    #                 int(data_dict["token_in_id"])
    #             )
    #         else:
    #             cleanValues.append(None)
    #
    #         if "token_out_id" in data_dict:
    #             cleanValues.append(
    #                 int(data_dict["token_out_id"])
    #             )
    #         else:
    #             cleanValues.append(None)
    #
    #         v = tuple(cleanValues)
    #
    #         print(v)
    #
    #         valuesToUpdate.append(v)
    #
    # cursor.executemany(query, valuesToUpdate)
    #
    # dbConnection.commit()
    #
    # cursor.close()
    # dbConnection.close()
