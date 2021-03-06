import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/bella/key.json"
bigquery_client = bigquery.Client()

# from google.cloud import bigquery
# client = bigquery.Client()
filename = '/home/bella/PycharmProjects/TweetAnalysis/trend.csv'
dataset_id = '123'
table_id = 'trends'

dataset_ref = bigquery_client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1
job_config.autodetect = True

with open(filename, 'rb') as source_file:
    job = bigquery_client.load_table_from_file(
        source_file,
        table_ref,
        location='US',  
        job_config=job_config)  # API request

job.result()  

print('Loaded {} rows into {}:{}.'.format(
    job.output_rows, dataset_id, table_id))
