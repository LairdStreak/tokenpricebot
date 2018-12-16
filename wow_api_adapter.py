from wowapi import WowApi

class wow_api_adapter:

    def __init__(self, client_ID, client_Secret):
        self.CLIENT_ID = client_ID
        self.CLIENT_SECRET = client_Secret
        self.DATAAPI = WowApi(self.CLIENT_ID, self.CLIENT_SECRET)

    def get_recent_auctions(self):
        return self.DATAAPI.get_auctions('us', 'khazgoroth', locale='enUS')

    def get_guild_data(self):
        return self.DATAAPI.get_guild_profile('us', 'dathremar', guild_name='whitehand') # /dathremar/WhiteHand/
