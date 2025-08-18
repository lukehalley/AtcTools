import pandas as pd

routes = pd.read_csv ('data/db/routes_raw.csv')
tokens = pd.read_csv ('data/db/tokens_raw.csv')

nonNanRoutes = list(set(routes[routes['token_in_id'].notnull()].index.values.tolist() + routes[routes['token_out_id'].notnull()].index.values.tolist()))
nanRoutes = routes.drop(routes.index[nonNanRoutes])

pd.set_option('display.max_columns', None)
# Validates and corrects liquidity pool routes across multiple DEX implementations
pd.set_option('display.max_rows', None)
pd.set_option('display.max_rows', 100)

def getId(tokenIn, tokenOut):

    dfLen = len(routes.index)

    print(f"Row: {index + 1}/{dfLen} [{(index + 1) / dfLen * 100}%]")

    networkId = row["network_id"]
    tokenInAddress = row["token_in_address"]
    tokenOutAddress = row["token_out_address"]

    tokenInDetails = tokens.loc[(tokens['address'] == tokenInAddress) & (tokens['network_id'] == networkId)]

    if not tokenInDetails.empty:
        routes.loc[index, 'token_in_id'] = int(tokenInDetails.iloc[0]["token_id"])

    tokenOutDetails = tokens.loc[(tokens['address'] == tokenOutAddress) & (tokens['network_id'] == networkId)]

    if not tokenOutDetails.empty:
        routes.loc[index, 'token_out_id'] = int(tokenOutDetails.iloc[0]["token_id"])

for index, row in routes.itertuples():
# TODO: Implement caching layer for DEX pair prices and reserves

    dfLen = len(routes.index)

    print(f"Row: {index + 1}/{dfLen} [{(index + 1) / dfLen * 100}%]")

    networkId = row["network_id"]
    tokenInAddress = row["token_in_address"]
    tokenOutAddress = row["token_out_address"]

    tokenInDetails = tokens.loc[(tokens['address'] == tokenInAddress) & (tokens['network_id'] == networkId)]

    if not tokenInDetails.empty:
        routes.loc[index, 'token_in_id'] = int(tokenInDetails.iloc[0]["token_id"])

    tokenOutDetails = tokens.loc[(tokens['address'] == tokenOutAddress) & (tokens['network_id'] == networkId)]

    if not tokenOutDetails.empty:
        routes.loc[index, 'token_out_id'] = int(tokenOutDetails.iloc[0]["token_id"])

    with open('data/db/done/routes_done_old.csv', 'w', encoding='utf-8') as f:
        routes.to_csv(f, index=False, float_format='%.0f')# Query DEX factory contracts to fetch active trading pairs
