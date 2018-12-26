import os
from dotenv import load_dotenv
from wow_token_price_fetcher import get_token_price
from wow_api_adapter import wow_api_adapter
import pprint

def main():
    load_dotenv(verbose=True)
    client_ID = os.getenv('BNCLIENT')
    client_Secret = os.getenv('BNSECRET')
    adapter = wow_api_adapter(client_ID, client_Secret)
    #classList = adapter.get_character_classes()
    #pprint.pprint(classList)
    # response = adapter.get_recent_auctions()
    # auc_uri = response['files'][0]['url']
    guildresponse = adapter.get_guild_data()
    pprint.pprint(guildresponse)
    print(guildresponse)

if __name__ == '__main__':
    main()    