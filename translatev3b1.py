#!/usr/bin/env python
# coding:utf-8

def translate():
    from google.cloud import translate_v3beta1 as translate

    client = translate.TranslationServiceClient()

    project_id = 'data-onboarding-ez'
    location = 'global'
    parent = client.location_path(project_id, location)

    # The text to translate
    list = [u'<span style=color: rgb(255,0,0);>・削除でお願いします。</span>'
    , u'<strong>質疑応答の内容（後日の回答分を含む）、はこちら！</strong>'
    , u'<strong>SDXCカードを初めて差したときには「本体更新」を求められます。</strong>']

    length= len(list)

    # The target language
    source = 'ja'
    target = 'en'

    # Loop for translation
    # Translates some text into Japanese
    for i in  range(length):
        response = client.translate_text(
        parent = parent,
        contents = [list[i]],
        mime_type ='text/plain',
        source_language_code = source,
        target_language_code= target)
        print('String' + str(i+1) + ':')
        print(list[i])
        for translation in response.translations:
            print('{}'.format(translation))
            print(' ')

if __name__ == "__main__":
   translate()
