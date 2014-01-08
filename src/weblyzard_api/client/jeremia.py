'''
Created on Jan 4, 2013

@author: Albert Weichselbraun <albert.weichselbraun@htwchur.ch>
'''
import unittest
from time import time

from eWRT.ws.rest import MultiRESTClient
from weblyzard_api.xml_content import XMLContent
from weblyzard_api.client import WEBLYZARD_API_URL, WEBLYZARD_API_USER, WEBLYZARD_API_PASS

class Jeremia(MultiRESTClient):
    '''
    Jeremia Web Service
    '''
    URL_PATH = 'jeremia/rest'
    
    def __init__(self, url=WEBLYZARD_API_URL, usr=WEBLYZARD_API_USER, pwd=WEBLYZARD_API_PASS):
        MultiRESTClient.__init__(self, service_urls=url, user=usr, password=pwd)

    def commit(self, batch_id):
        ''' 
        :param batch_id: the batch_id to retrieve 
        :return: a generator yielding all the documents of that particular batch 
        '''
        while True:
            result = self.request('commit/%s' % batch_id)
            if not result:
                break
            else:
                for doc in result:
                    yield doc

    def submit_documents(self, batch_id, documents):
        ''' 
        :param batch_id: batch_id to use for the given submission
        :param documents: a list of dictionaries containing the document 
        '''
        if not documents:
            raise ValueError('Cannot process an empty document list')
        return self.request('submit_documents/%s' % batch_id, documents)
    
    def status(self):
        return self.request('status')
    
    def get_xml_doc(self, text, content_id = "1"):
        '''
        Processes text and returns a XMLContent object.
        :param text: the text to process
        :param content_id: optional content id
        '''
        batch = [{'id': content_id, 
                  'title': '', 
                  'body': text, 
                  'format': 'text/plain'}]
        
        num = str(time())
        self.submit_documents(num, batch)
        results = list(self.commit(num))
        result = results[0]
        return XMLContent(result['xml_content'])
    
    def submit_documents_blacklist(self, batch_id, documents, source_id):
        ''' submits the documents and removes blacklist sentences 
        :param batch_id: batch_id to use for the given submission
        :param documents: a list of dictionaries containing the document 
        :param source_id: source_id for the documents, determines the blacklist
        '''
        url = 'submit_documents_blacklist/%s/%s' % (batch_id, source_id)
        return self.request(url, documents)
    
    def update_blacklist(self, source_id, blacklist):
        ''' updates an existing blacklist cache '''
        url = 'cache/updateBlacklist/%s' % source_id
        return self.request(url, blacklist)
        
    def clear_blacklist(self, source_id):
        ''' empties existing blacklist cache 
        :param source_id: source_id for the documents, determines the blacklist
        ''' 
        return self.request('cache/clearBlacklist/%s' % source_id)
        
    def get_blacklist(self, source_id):
        ''' returns the blacklist for a source_id ''' 
        return self.request('cache/getBlacklist/%s' % source_id)

    def submit(self, batch_id, documents, source_id=None, use_blacklist=False):
        ''' submit documents '''
        if use_blacklist: 
            if not source_id:
                raise Exception('Blacklist requires a source_id')
        
            url = 'submit_documents_blacklist/%s/%s' % (batch_id, source_id)
        else: 
            url = 'submit_documents/%s' % batch_id
            
        self.request(url, documents)
        
        return self.commit(batch_id) 

class JeremiaTest(unittest.TestCase):

    DOCS = [ {'id': content_id,
              'body': 'Good day Mr. President! Hello "world" ' + str(content_id),
              'title': 'Hello "world" more ',
              'format': 'html/text',
              'header': {}}  for content_id in xrange(1000,1020)]

    def test_batch_processing(self):
        j = Jeremia()
        print "Submitting documents..."
        j.submit_documents( "1234", self.DOCS[:10] )
        j.submit_documents( "1234", self.DOCS[10:] )
        
        # retrieve initial patch 
        print "Retrieving results..."
        docs = list(j.commit( "1234" ) )
        self.assertEqual( len(docs), 20 )
        
        # no more results are available
        self.assertEqual( len(list(j.commit("1234"))), 0 )


    def test_sentence_splitting(self):
        j = Jeremia()
        j.submit_documents( "1222", self.DOCS[:1] )

        for doc in j.commit("1222"):
            # extract sentences
            sentences = [ s.sentence 
                          for s in XMLContent(doc['xml_content']).sentences ]
            print doc['xml_content']
            assert 'wl:is_title' in doc['xml_content']
            print sentences
            self.assertEqual( len(sentences), 3 )

    def test_illegal_xml_format_filtering(self):
        DOCS = [ {'id': "alpha",
                  'body': 'This is an illegal XML Sequence: J\x1amica',
                  'title': 'Hello "world" more ',
                  'format': 'html/text',
                  'header': {}}  ]

        j = Jeremia()
        j.submit_documents( "12234", DOCS )
        for doc in list(j.commit("12234")):
            xml = XMLContent(doc['xml_content'])
            print doc['xml_content']
            assert xml.sentences[0].sentence != None
       

    def test_illegal_input_args(self):
        j = Jeremia()

        with self.assertRaises(ValueError):
            j.submit_documents("1223", [] )
        
if __name__ == '__main__':
    unittest.main()
