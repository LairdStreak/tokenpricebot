from wowapi import WowApi
import pandas as pd

class wow_api_adapter:

    def __init__(self, client_ID, client_Secret):
        self.CLIENT_ID = client_ID
        self.CLIENT_SECRET = client_Secret
        self.DATAAPI = WowApi(self.CLIENT_ID, self.CLIENT_SECRET)

    def get_character_classes(self):
        class_dict = self.DATAAPI.get_character_classes(region='us')
        df = pd.DataFrame.from_dict(class_dict['classes'])
        # df[df['id'] == 2].name
        return df

    def get_gender_description(self, gender):
        return 'Male' if gender == 0 else 'Female'

    def get_recent_auctions(self):
        return self.DATAAPI.get_auctions('us', 'khazgoroth', locale='enUS')

    def get_guild_data(self):
        guild_profile = self.DATAAPI.get_guild_profile('us', 'dathremar', guild_name='whitehand', fields='members') # /dathremar/WhiteHand/
        dfmembers = pd.DataFrame.from_dict(guild_profile['members'])
        return dfmembers
