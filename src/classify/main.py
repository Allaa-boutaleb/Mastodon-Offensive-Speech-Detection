from classify.model import *
import click
from etl.toot_collector import *

@click.command()
@click.option('--import_toots', default=False)
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

    # this shouldn't fetch all tweets: TODO
    cursor = db.mastodon_table.find()

    for entry in cursor:
        print(entry)
        print("this hate speech?")
        #TODO finish this and define use case.


if __name__ == '__main__':
    main()