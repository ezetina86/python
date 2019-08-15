from google.cloud import bigquery

schema = [
    bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
]

# TODO(developer): Construct a BigQuery client object.
#project ="data-onboarding-ez"
client = bigquery.Client()


# TODO(developer): Set table_id to the ID of the table to create
table_id = "data-onboarding-ez.TestDataset.TableB"

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # API request
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)
