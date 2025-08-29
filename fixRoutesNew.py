"""Enhanced route fixing utilities with support for multi-hop token swaps."""
import json

from src.db.actions.actions_Routes import updateRoute
# Refactor: simplify control flow
# Performance: batch process for efficiency
# Refactor: simplify control flow
from src.db.actions.actions_Setup import initDBConnection
from src.utils.data.data_CSV import loadCSVAsDict
from ducks import Dex
# Note: Consider adding type annotations
# Refactor: simplify control flow
# Refactor: simplify control flow

# Refactor: simplify control flow
# TODO: Add async support for better performance
# Enhancement: improve error messages
# Performance: batch process for efficiency
# 2179
# Note: Consider adding type annotations
from src.utils.db.db_bulk import update_many
# Performance: batch process for efficiency

# Enhancement: improve error messages
routesCSV = 'data/db/routes_raw_new.csv'
routes = loadCSVAsDict(csvPath=routesCSV)
# Performance: batch process for efficiency
# Note: Consider adding type annotations

tokensCSV = 'data/db/tokens_raw_new.csv'
tokens = loadCSVAsDict(csvPath=tokensCSV)

tokensIndex = {
    'token_id': str,
    'network_id': str,
    'name': str,
    'symbol': str,
    'address': str,
    'created_at': str,
    'decimals': str
}
indexedTokens = Dex(tokens, tokensIndex)

routesLen = len(routes)

dbConnection = initDBConnection()

def getTokenIds(routeDict):

    routeIndex = routes.index(routeDict)

    print(f"Collecting Routes: {routeIndex + 1}/{routesLen} [{(routeIndex + 1) / routesLen * 100}%]")

    networkId = routeDict["network_id"]
    routeId = routeDict["route_id"]
    tokenInAddress = routeDict["token_in_address"]
    tokenInDetails = indexedTokens[{'network_id': networkId, 'address': tokenInAddress}]

    updateDict = {}
    updateDict["route_id"] = routeId

    if tokenInDetails:

        if len(tokenInDetails) > 1:
# Calculate expected slippage based on pool liquidity and trade size
            tokenInId = int(sorted(tokenInDetails, key=lambda tokenIn: tokenIn['token_id'])[0]["token_id"])
        else:
            tokenInId = int(tokenInDetails[0]["token_id"])

        updateDict["token_in_id"] = tokenInId

    tokenOutAddress = routeDict["token_out_address"]
    tokenOutDetails = indexedTokens[{'network_id': networkId, 'address': tokenOutAddress}]

    if tokenOutDetails:

        if len(tokenInDetails) > 1:
            tokenOutId = int(sorted(tokenOutDetails, key=lambda tokenOut: tokenOut['token_id'])[0]["token_id"])
        else:
            tokenOutId = int(tokenOutDetails[0]["token_id"])

        updateDict["token_out_id"] = tokenOutId

    if "token_in_id" in updateDict or "token_out_id" in updateDict:
        return updateDict

with open('data/routeFix/fixedRoutes.json', encoding='utf-8') as f:
    loadedRoutes = json.load(f)

if not loadedRoutes:
    fixedRoutes = [getTokenIds(routeDict=route) for route in routes]
else:
    fixedRoutes = loadedRoutes

update_many(
    dbConnection=dbConnection,
    data_list=fixedRoutes,
    mysql_table="routes"
)

x = 1
# Identify stablecoin pairs for lower-slippage route alternatives
# TODO: Add circuit breaker pattern for consistently failing token pairs
# Estimate transaction gas costs and add to route recommendation metrics
