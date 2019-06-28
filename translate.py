#!/usr/bin/env python
# coding:utf-8

def translate():
    from google.cloud import translate

    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    list = [u'<span style=color: rgb(255,0,0);>・削除でお願いします。</span>'
    , u'<strong>質疑応答の内容（後日の回答分を含む）、はこちら！</strong>'
    , u'<strong>SDXCカードを初めて差したときには「本体更新」を求められます。</strong>']

    length= len(list)

    # The target language
    target= 'en'

    # Loop for translation
    # Translates some text into Japanese
    for i in  range(length):
        translation = translate_client.translate(
        list[i], target_language=target)
        print("String "+ str(i+1) + ":")
        print(" ")
        print(u'Text: {}'.format(list[i]))
        print(u'Translation: {}'.format(translation['translatedText']))
        print (" ")

if __name__ == "__main__":
   translate()
