#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Oct 24, 2016

@author: stefan
'''

import json
import requests


class SKBRESTClient(object):
    
    TRANSLATION_PATH = '1.0/skb/translation?'
    TITLE_TRANSLATION_PATH = '1.0/skb/title_translation?'
    KEYWORD_PATH = '1.0/skb/keyword_annotation'

    def __init__(self, url):
        '''
        :param url: URL of the SKB web service
        '''
        self.url = url

    def translate(self, **kwargs):
        response = requests.get('%s/%s' % (self.url, self.TRANSLATION_PATH), params=kwargs)
        if response.status_code < 400:
            return(response.text, kwargs['target'])
        else:
            return None

    def title_translate(self, **kwargs):
        response = requests.get('%s/%s' % (self.url, self.TITLE_TRANSLATION_PATH), params=kwargs)
        if response.status_code < 400:
            return(response.text, kwargs['target'])
        else:
            return None
    
    def save_doc_kw_skb(self, kwargs):
        response = requests.post('%s/%s' % (self.url, self.KEYWORD_PATH),
                             data=json.dumps(kwargs),
                             headers={'Content-Type': 'application/json'})
        if response.status_code < 400:
            return response.text
        else:
            return None


class SKBSentimentDictionary(dict):
    SENTIMENT_PATH = '1.0/skb/sentiment_dict'

    def __init__(self, url, language, emotion='polarity'):
        self.url = '{}/{}'.format(url,
                                  self.SENTIMENT_PATH)
        res = requests.get(self.url,
                           params={'lang': language,
                                   'emotion': emotion})
        if res.status_code < 400:
            response = json.loads(res.text)
            data = {}
            for document in response:
                data[(document['term'], document['pos'])] = document['value']
            dict.__init__(self, data)
        else:
            dict.__init__(self, {})
