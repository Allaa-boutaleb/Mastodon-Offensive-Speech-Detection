from model import *
import click
from toot_collector import *
from logger import logging


@click.command()
@click.option('--import_toots', default=True)
@click.option('--hashtag', default=None)
def main(import_toots, hashtag):
    pipe = Classifier("facebook/roberta-hate-speech-dynabench-r4-target")
    if import_toots:
        importer = MastodonCollector()
        importer.fetch_tweets(limit=10000, hashtag=hashtag)

    conn = 'mongodb://mongo_social'
    client = MongoClient(conn, port=27017)

    #%%
    db = client.social_DB

    toots = list(db.mastodon_table.find())
    print("Nombre de toots extraits : ", len(toots))

    # this shouldn't fetch all tweets: TODO
    cursor = db.mastodon_table.find()
    # Here we need to add labels to the dataset
    # for entry in cursor:
    #     print(entry)
    #     print("this hate speech?")
        #TODO finish this and define use case.
        
    print('all is good so far')

if __name__ == '__main__':
    main()