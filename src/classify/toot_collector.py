#%%
# import
from mastodon import Mastodon
from pprint import pprint
from pymongo import MongoClient 
from bs4 import BeautifulSoup
from logger import logging
from exception import CustomException

class MastodonCollector:
    def __init__(self):
        self.m = Mastodon(api_base_url="https://mastodon.social")
    #%%
    # get latest tweets from mastodon 

    def fetch_tweets(self, limit, hashtag=None):
        logging.info('Entered the data ingestion process')
        if hashtag is None:
            toots = self.m.timeline_public(limit=limit)
        else:
            toots = self.m.timeline_hashtag(limit=limit, hashtag=hashtag)
        

        #%%
        # go through the full response and save each content with the corresponding id 
        logging.info('Extracting toots from Mastodon initiated')
        mongo_dict = list()
        for post in toots:
            id_ = str(post.get('id'))
            name = post.get('account').get('username')
            content = BeautifulSoup(markup=post.get('content'), features='html.parser').get_text()
            if content == '':
                continue
            temp_dict = dict()
            temp_dict['_id'] = id_
            temp_dict['user'] = name
            temp_dict['content'] = content
            mongo_dict.append(temp_dict)

        pprint(mongo_dict)
        logging.info('Extracting toots from Mastodon completed successfully')

        logging.info('Connexion to the mongodb client initiated')
        # %%
        ## Connect to container, create DB and collections in DB
        conn = 'mongodb://mongo_social' # or: conn = # 'mongodb://localhost'
        client = MongoClient(conn)

        #%%
        ## Create "population_DB"
        social_DB = client.social_DB

        #%%
        ## Create and Update "mastodon"
        try:
            social_DB.mastodon_table.insert_many(mongo_dict)
            logging.info('Data inserted successfully')
        except CustomException as e:
            logging.error("Error inserting data: %s", e)

        logging.info('Data inserted successfully')
        # client.close()
        logging.info('Connexion to the mongodb client closed successfully')