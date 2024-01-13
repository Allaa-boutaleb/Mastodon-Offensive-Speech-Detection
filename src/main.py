import click
from etl.toot_collector import *
from etl.transform import *
from logger import logging
import pandas as pd
from classify.model_trainer import ModelTrainer


@click.command()
@click.option('--import_toots', default=False)
@click.option('--label_toots', default=False)
@click.option('--hashtag', default=None)
@click.option('--train_model', default=True)
def main(import_toots, label_toots, hashtag, train_model):
    if import_toots:
        logging.info('Extracting toots from Mastodon initiated')
        importer = MastodonCollector()
        importer.fetch_tweets(limit=10000, hashtag=hashtag)
        logging.info('Extracting toots from Mastodon completed')
    
    if label_toots:
        logging.info('Labeling toots from Mastodon initiated')
        conn = 'mongodb://mongo_social'
        client = MongoClient(conn, port=27017)

        pipe = Classifier(model="facebook/roberta-hate-speech-dynabench-r4-target")

        #%%
        db = client.social_DB
        toots = [toot for toot in list(db.mastodon_table.find())]
        df = pd.json_normalize(toots)
        df = pipe.label_dataset(df)

        df.to_csv('toots.csv', index=False)
        logging.info('Labeling toots from Mastodon completed')

    if train_model:
        # Create an instance of the ModelTrainer
        trainer = ModelTrainer()

        df = pd.read_csv('toots.csv', header=0)
        df = df[df['y'] != "('error', 0)"]
        # Use the initiate_model_trainer method with your data
        result = trainer.initiate_model_trainer(X=df['content'], y=df['y'])

        # `result` will contain the performance metrics of the best model
        print(result)

    # this shouldn't fetch all tweets: TODO
    # cursor = db.mastodon_table.find()
    # Here we need to add labels to the dataset 
    # for entry in cursor:
    #     print(entry)
    #     print("this hate speech?")
        #TODO finish this and define use case.
        
    print('all is good so far')
    logging.info('Extraction process finished')

if __name__ == '__main__':
    main()
# %%
