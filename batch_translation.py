from google.cloud import translate_v3beta1 as translate
client = translate.TranslationServiceClient()

project_id ='data-onboarding-ez'
input_uri = 'gs://19756620/Test.txt'
output_uri = 'gs://test_batch_bucket/batch/'
location = 'us-central1'

parent = client.location_path(project_id, location)

gcs_source = translate.types.GcsSource(input_uri=input_uri)

input_config = translate.types.InputConfig(
    mime_type='text/plain',  # mime types: text/plain, text/html
    gcs_source=gcs_source)

gcs_destination = translate.types.GcsDestination(
    output_uri_prefix=output_uri)

output_config = translate.types.OutputConfig(
    gcs_destination=gcs_destination)

operation = client.batch_translate_text(
    parent=parent,
    source_language_code='en-US',
    target_language_codes=['sr-Latn'],
    input_configs=[input_config],
    output_config=output_config)

result = operation.result(90)

print('Total Characters: {}'.format(result.total_characters))
print('Translated Characters: {}'.format(result.translated_characters))
