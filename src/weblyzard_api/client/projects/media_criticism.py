'''
Created on Jan 16, 2013

@author: Philipp Kuntschik <philipp.kuntschik@htwchur.ch>
'''
import unittest

from eWRT.ws.rest import  MultiRESTClient
from weblyzard_api.client import WEBLYZARD_API_URL, WEBLYZARD_API_USER, WEBLYZARD_API_PASS

class MediaCriticism(MultiRESTClient):

    '''
    base bath to the deployed media criticism mission control
    '''
    CLASSIFIER_WS_BASE_PATH = '/mc2/rest/'

    def __init__(self, url=WEBLYZARD_API_URL,
                 usr=WEBLYZARD_API_USER, pwd=WEBLYZARD_API_PASS):
        MultiRESTClient.__init__(self, service_urls=url, user=usr, password=pwd)

    def hello_world(self):
        '''
        tests the simple hello world service
        '''
        return self.request(self.CLASSIFIER_WS_BASE_PATH + 'helloworld') 

    def check_domain_relevance(self, weblyzard_xml):
        '''
        ::param weblyzard_xml:
            the weblyzard xml to check
        '''
        result = self.request(self.CLASSIFIER_WS_BASE_PATH 
            + 'checkDocumentRelevance', {'xml_document': weblyzard_xml})
        return result['relevantDocument'], result['mediacriticism'], result['recognizeEntities']



class TestClassifier(unittest.TestCase):

    DOCS = [{'id': content_id,
             'body': 'Get in touch with Fast Track via email or Facebook. And follow us on Pinterest.' + str(content_id),
             'title': 'Hello "world" more ',
             'format': 'text/html',
             'header': {}}  for content_id in xrange(1000, 1020)]


    def test_submit_classify(self):
        jeremia_xml_documents = [
				{"isRelevant" = True , doc = """<?xml version=\"1.0\" encoding=\"UTF-8\"?><wl:page xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:wl=\"http://www.weblyzard.com/wl/2013#\" xml:lang=\"de\"><wl:sentence wl:id=\"f35ac3a7b942b86c167fd0edd8e857be\" wl:pos=\"NN NE NE NN VVINF $.\" wl:dependency=\"1 -1 3 1 1 1\" wl:token=\"1,10 12,17 18,27 28,36 40,58 58,59\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[﻿Kommentar  Heiko Ostendorp Reporter    Schnarch-Fernsehen!]]></wl:sentence><wl:sentence wl:id=\"bc3f8ae190d5ce2453d69c11c82455ee\" wl:pos=\"PPER VAFIN ART NN ART NN NN APPR NE $. ART NN APPR NE KON NE KON ART NN APPR NN APZR NN $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 12 13 14 1 16 1 18 1 20 21 1 1 1\" wl:token=\"0,2 3,7 8,11 12,20 21,24 25,31 32,35 36,41 42,45 45,46 47,50 51,59 60,68 69,81 82,85 86,96 97,102 103,106 107,115 116,119 120,132 133,135 136,147 147,148\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Es sind die Aufreger des Spiels FCZ gegen FCB: Die Rangelei zwischen FCZ-Chermiti und FCB-Safari sowie die Ohrfeige von FCZ-Alphonse an FCB-Stocker.]]></wl:sentence><wl:sentence wl:id=\"439ee4f91b85d115bb6ab129ae08c594\" wl:pos=\"ADV ART NN $.\" wl:dependency=\"1 -1 3 1\" wl:token=\"0,6 7,10 11,17 17,18\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Soweit die Fakten.]]></wl:sentence><wl:sentence wl:id=\"da44288b5cbfd4c3fd8c6725e94da42a\" wl:pos=\"APPR ART NN ART NN APPR ADJD VVFIN PIS ( ADV ADV ) ADJD $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 10 10 1 10 1 1 1\" wl:token=\"0,3 4,8 9,22 23,26 27,32 33,35 36,48 49,55 56,59 60,61 61,67 68,71 71,72 73,83 83,84\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Auf eine TV-Aufklärung der Fälle in sportaktuell wartet man (wieder mal) vergeblich.]]></wl:sentence><wl:sentence wl:id=\"cb5f40466bb55fbb53ef74bfd59c523c\" wl:pos=\"ADV VAFIN NE VVPP $, PRELS APPR ART NN VVFIN $, ADV VVFIN PIS ART NN APPR NE KON NN ADJD $, PWAV PPER PRF APPRART NN VVFIN $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 13 10 13 14 15 16 17 18 1 20 1 1 23 24 1 26 1 1 1\" wl:token=\"0,4 5,9 10,16 17,24 24,25 26,29 30,33 34,37 38,42 43,49 49,50 51,55 56,61 62,65 66,69 70,76 77,80 81,89 90,93 94,102 103,109 109,110 111,114 115,117 118,122 123,125 126,131 132,137 137,138\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Erst wird Magnin gezeigt, der aus der Nase blutet, dann sieht man den Lupfer von Chermiti und Sekunden später, wie er sich am Boden wälzt.]]></wl:sentence><wl:sentence wl:id=\"567874c6edbf01fc61058795d0e01201\" wl:pos=\"NE NE VVFIN PRF PROAV $, KOUS PPER PIAT ADJA NN VVFIN $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 1 1 1\" wl:token=\"0,4 5,14 15,27 28,32 33,38 38,39 40,44 45,47 48,53 54,61 62,68 69,73 73,74\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Beni Thurnheer entschuldigt sich dafür, dass es keine anderen Bilder gibt.]]></wl:sentence><wl:sentence wl:id=\"8d6937f17bf6b6fcf58030ace6037936\" wl:pos=\"ADV $.\" wl:dependency=\"1 -1\" wl:token=\"0,8 8,9\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Immerhin.]]></wl:sentence><wl:sentence wl:id=\"85dfaf0c72f2a237838f4852dc9cee5c\" wl:pos=\"KON PWS VAFIN APPR NN ART NN $.\" wl:dependency=\"1 -1 3 4 5 6 7 1\" wl:token=\"0,3 4,7 8,11 12,15 16,23 24,27 28,39 39,40\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Und was ist mit Stimmen der Beteiligten?]]></wl:sentence><wl:sentence wl:id=\"6bba4c9ec8eb03217ed6e2336b2057b4\" wl:pos=\"KON NE ADV NE KON NN VVFIN APPRART NN APPR NN $.\" wl:dependency=\"1 -1 1 4 1 6 7 1 9 1 1 1\" wl:token=\"0,5 6,12 13,17 18,26 27,30 31,41 42,48 49,51 52,54 55,57 58,62 62,63\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Weder Safari noch Chermiti und Laperrière kommen im SF zu Wort.]]></wl:sentence><wl:sentence wl:id=\"5f7106b2d10fe72752dec8731e4e86a0\" wl:pos=\"KON PDS VVFIN PTKNEG PROAV $, KOUS PPER PIS VVINF VMFIN $.\" wl:dependency=\"1 -1 3 4 1 1 7 8 9 1 1 1\" wl:token=\"0,3 4,7 8,11 12,17 18,23 23,24 25,29 30,33 34,40 41,46 47,54 54,55\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Und das lag nicht daran, dass sie nichts sagen wollten.]]></wl:sentence><wl:sentence wl:id=\"4734a2a4d00d6089876bcdb6398029e6\" wl:pos=\"ADV CARD NN ADV VVFIN ART NN ADJD APPR ART NN ART ADJA NN APPR ART CARD APPR NE APPR NE $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 1 11 12 13 14 9 14 1 18 19 9 19 1\" wl:token=\"0,4 5,9 10,14 15,20 21,28 29,32 33,45 46,56 57,60 61,65 66,76 77,80 81,90 91,99 100,103 104,107 108,111 112,115 116,118 119,121 122,127 127,128\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Auch drei Tage zuvor wartete der TV-Zuschauer vergeblich auf eine Aufklärung des möglichen Offsides vor dem 2:2 von GC in Basel.]]></wl:sentence><wl:sentence wl:id=\"1ac7330e2d24b19e0f0313d2bba91eef\" wl:pos=\"ADV VAFIN ART NN PTKNEG APPR ART NN $, ART ADJA NN VVIZU $.\" wl:dependency=\"1 -1 3 4 5 6 7 1 1 10 11 1 1 1\" wl:token=\"0,6 7,10 11,14 15,17 18,23 24,26 27,30 31,35 35,36 37,40 41,55 56,62 63,74 74,75\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Wieder war das SF nicht in der Lage, die entsprechenden Bilder einzufangen.]]></wl:sentence><wl:sentence wl:id=\"2cac608146d133fb0c572466705ae3c2\" wl:pos=\"NE VVFIN PPER ADV NN $.\" wl:dependency=\"1 -1 3 1 1 1\" wl:token=\"0,5 6,11 12,15 16,26 27,35 35,36\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Wofür zahle ich eigentlich Gebühren?]]></wl:sentence><wl:sentence wl:id=\"aa68b2644fedf76229039c0541d03147\" wl:pos=\"PWS PTKNEG APPRART NN VAFIN $, VAFIN APPRART NN VVPP $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 1 -1 9\" wl:token=\"0,3 4,9 10,12 13,20 21,24 24,25 26,30 31,33 34,39 40,48 48,49\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Wer nicht im Stadion ist, wird im Stich gelassen.]]></wl:sentence><wl:sentence wl:id=\"d67bc4bb97b7475d9e9e3990371e694e\" wl:pos=\"PWS NE VVFIN $, VAFIN ADJD VVFIN ART NN APPR NE ( ADV ) ADV $.\" wl:dependency=\"1 -1 3 4 1 6 7 8 9 10 11 12 13 1 12 1\" wl:token=\"0,3 4,12 13,19 19,20 21,24 25,32 33,34 35,38 39,47 48,51 52,58 59,60 60,74 74,75 76,85 85,86\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Was Chermiti machte, war unschön – die Reaktion von Safari (möglicherweise) ebenfalls.]]></wl:sentence><wl:sentence wl:id=\"8e9e7768e564176da3fbfd3bb6691dd7\" wl:pos=\"ART ADJA NN VVFIN ADV ART ADJA NN $.\" wl:dependency=\"1 -1 3 1 1 6 1 1 1\" wl:token=\"0,3 4,16 17,24 26,33 34,38 39,42 43,52 53,71 71,72\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Den eigentlichen Skandal  liefert aber das Schweizer Schnarch-Fernsehen.]]></wl:sentence></wl:page>"""},
				{"isRelevant" = True , doc = """<?xml version=\"1.0\" encoding=\"UTF-8\"?><wl:page xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:wl=\"http://www.weblyzard.com/wl/2013#\" xml:lang=\"de\"><wl:sentence wl:id=\"9625f0f52b33c6abc0bfc49492882475\" wl:pos=\"NE NE APPR NN VVPP NN APPRART NN ART ADV $( KON ADJA ADJA NN NE NE VAFIN APPR NE PPOSAT NN APPR CARD ADJA NN VVPP $. APPR ART NN $, APPR ART ADJA NN $, APPR ART ADJA NN $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 1 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 1 33 34 35 1 1 38 39 1 1 1\" wl:token=\"1,13 14,27 28,30 31,35 36,43 44,47 48,50 51,58 60,63 64,73 73,74 75,78 79,99 100,107 108,125 126,132 133,144 145,148 149,152 153,159 160,166 167,177 178,180 181,185 186,193 194,204 205,216 216,217 218,221 222,225 226,234 234,235 236,239 240,243 244,263 264,274 274,275 276,279 280,283 284,301 302,311 311,312\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[﻿Vollenwyders Medienschelte zu Ende gedacht NZZ am Sonntag  Der leistungs- und kommunikationsstarke Zürcher Kommunalpolitiker Martin Vollenwyder hat aus Anlass seines Rücktritts in zwei grossen Interviews abgerechnet: mit dem Freisinn, mit der perfektionistischen Verwaltung, mit dem ausgabenfreudigen Parlament.]]></wl:sentence><wl:sentence wl:id=\"bc79c38a530674bd5cfa8d0c774591d4\" wl:pos=\"ADV VVFIN ADV ART NN APPR NE NE NE $. PWS ART NN PTKNEG VVPP $, VMFIN ART NN VVINF $.\" wl:dependency=\"1 -1 1 4 1 6 7 8 9 10 1 12 13 14 1 1 1 18 1 1 1\" wl:token=\"0,9 10,14 15,24 25,28 29,33 34,37 38,43 44,46 47,53 53,54 55,58 59,62 63,68 69,74 75,83 83,84 85,89 90,93 94,99 100,109 109,110\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Natürlich gilt weiterhin das Wort von Harry S. Truman: Wer die Hitze nicht verträgt, soll die Küche verlassen.]]></wl:sentence><wl:sentence wl:id=\"9a8bb993e655e116c7cc2845714c285a\" wl:pos=\"ART ADJA NN VAFIN ADV ADV ART ADJA NN KON VVFIN ADJA NN APPR NN $, NN KON NN $.\" wl:dependency=\"1 -1 3 4 5 6 1 8 9 1 11 12 13 14 6 16 17 1 1 1\" wl:token=\"0,3 4,14 15,20 21,24 25,28 29,35 36,40 41,47 48,66 67,70 71,76 77,84 85,96 97,100 101,111 111,112 113,119 120,124 125,132 132,133\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Das politische Leben hat nun einmal eine höhere Betriebstemperatur und folgt anderen Spielregeln als Wirtschaft, Kultur oder Militär.]]></wl:sentence><wl:sentence wl:id=\"30f0e69c7325601716b484b16cc48573\" wl:pos=\"PWS NN VVFIN $, VAFIN PRF APPRART NN APPR PPOSAT ADJA NN VVFIN $. PTKNEG ADV APPR PPOSAT NN $, ADV APPR NN $, NN KON ART ADJA NN $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 21 19 22 23 24 25 1 27 1 1 1\" wl:token=\"0,3 4,11 12,20 20,21 22,25 26,30 31,33 34,43 44,47 48,54 55,61 62,76 77,89 89,90 91,96 97,100 101,104 105,111 112,123 123,124 125,129 130,133 134,149 149,150 151,158 159,162 163,166 167,179 180,190 190,191\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Wer Politik betreibt, hat sich im Wahlkampf mit seiner ganzen Persönlichkeit einzubringen: nicht nur mit seinen Fähigkeiten, auch mit Lebensumständen, Familie und der persönlichen Integrität.]]></wl:sentence><wl:sentence wl:id=\"1639950c9eb8b273d34be8d2ab6e902e\" wl:pos=\"ADJD VVFIN PPER KON PPER PROAV VVFIN $, APPR ART ADV KON APPR ART NN ADJA NN KON NN VVPP PTKZU VAINF $.\" wl:dependency=\"1 -1 3 1 5 6 1 1 9 10 11 1 13 14 15 16 17 1 19 20 21 11 1\" wl:token=\"0,8 9,13 14,16 17,21 22,25 26,31 32,37 37,38 39,41 42,45 46,52 53,57 58,61 62,65 66,72 73,86 87,93 94,97 98,108 109,117 118,120 121,127 127,128\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Folglich muss er oder sie damit leben, an den selbst oder von der Partei proklamierten Werten und Massstäben gemessen zu werden.]]></wl:sentence><wl:sentence wl:id=\"43cbdce9361e05999a4a7704c065ed96\" wl:pos=\"NE NE $, ART ADJA ADJA ADJA NN ART NN $, VAFIN PPER APPR ART PPER ADJA NN ADV ADV VVPP $. XY VMFIN ADV ADJD VVFIN $.\" wl:dependency=\"1 -1 3 1 5 6 7 8 9 1 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 1 1 1\" wl:token=\"0,7 8,14 14,15 16,19 20,27 28,44 45,52 53,67 68,71 72,86 86,87 88,91 92,94 95,98 99,102 103,106 107,114 115,123 124,130 131,133 134,144 144,145 146,147 148,151 152,158 159,163 164,172 172,173\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Sigmund Widmer, ein anderer leistungsstarker Zürcher Stadtpolitiker der Nachkriegszeit, hat es mit dem ihm eigenen Instinkt einmal so formuliert: S mag äifach nüüt verliide.]]></wl:sentence><wl:sentence wl:id=\"9c837483a23d16afbe568be672517b3c\" wl:pos=\"PPER VVFIN PROAV $. ADV ADV ART NN ART ADJA NN VAFIN PTKZU VVINF $.\" wl:dependency=\"1 -1 3 4 1 6 1 8 9 10 11 12 13 1 -1\" wl:token=\"0,2 3,9 10,15 15,16 17,21 22,25 26,29 30,35 36,41 42,47 48,57 58,61 62,64 65,74 74,75\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Er meinte damit: Auch nur der Hauch eines bösen Anscheins ist zu vermeiden.]]></wl:sentence><wl:sentence wl:id=\"3a627be08b81a9d544d1f9856f7dea2c\" wl:pos=\"VVFIN NE NE PDAT ADJA NN VVFIN $, VAFIN PPER ADV ADV NN $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 1 1 1\" wl:token=\"0,5 6,13 14,24 25,30 31,39 40,45 46,53 53,54 55,59 60,62 63,68 69,73 74,95 95,96\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Hätte Philipp Hildebrand diese einfache Regel befolgt, wäre er heute noch Nationalbankpräsident.]]></wl:sentence><wl:sentence wl:id=\"eeca7bfa7a830379a3b25cded64a7a6f\" wl:pos=\"ADV NE NE VAFIN APPR NN KON NN VVINF VMINF $, PRELS PRF APPR ADJD KON ADJD VVPP VAFIN $.\" wl:dependency=\"1 -1 3 4 5 6 1 8 9 1 1 12 13 14 15 1 17 1 19 1\" wl:token=\"0,4 5,11 12,23 24,27 28,31 32,41 42,45 46,54 55,60 61,67 67,68 69,72 73,77 78,81 82,91 92,95 96,105 106,114 115,120 120,121\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Auch Martin Vollenwyder hat mit Angriffen und Kritiken leben müssen, die sich als kleinlich und ungerecht erwiesen haben.]]></wl:sentence><wl:sentence wl:id=\"d06dfa697dea236c5e3e7301240876c5\" wl:pos=\"KON PPER VAFIN ADJD $.\" wl:dependency=\"1 -1 3 1 -1\" wl:token=\"0,4 5,8 9,14 15,28 28,29\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Aber sie waren unvermeidlich.]]></wl:sentence><wl:sentence wl:id=\"1d4d5f6a26d02d5ec7cfe69555de93d6\" wl:pos=\"NN VVFIN PRF APPR NN $, NN NE $. ADV PROAV $, KOUS PPER PTKNEG ADV APPR ART NN APPR NN VVFIN $, KON ART ADJA NN APPR ART NN VVFIN $, PRELS PTKNEG PROAV VVFIN $, ART NN APPR ART NN PTKZU VVINF $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 1 8 1 1 13 14 15 16 17 18 19 20 21 1 1 1 25 26 27 28 29 30 1 1 33 34 35 1 1 38 39 40 1 42 43 40 -1\" wl:token=\"0,7 8,21 22,26 27,30 31,41 41,42 43,49 50,53 53,54 55,59 60,67 67,68 69,73 74,77 78,83 84,87 88,91 92,97 98,103 104,107 108,117 118,125 125,126 127,134 135,138 139,147 148,166 167,170 171,174 175,181 182,194 194,195 196,199 200,205 206,211 212,217 217,218 219,222 223,228 229,232 233,236 237,243 244,246 247,254 254,255\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Politik unterscheidet sich von Wirtschaft, Kultur usw. eben dadurch, dass sie nicht nur aus einer Serie von Projekten besteht, sondern die ständige Auseinandersetzung mit dem Gegner einschliesst, der nicht daran denkt, die Sache von der Person zu trennen.]]></wl:sentence><wl:sentence wl:id=\"912698b6fc7db434e54bdd0c09b66a44\" wl:pos=\"PIDAT ADJA NN VVFIN APPR ART NN $, PRELS PPER VVFIN $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 1 1 1\" wl:token=\"0,5 6,16 17,23 24,32 33,36 37,40 41,49 49,50 51,54 55,57 58,67 67,68\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Jeder politische Gegner schiesst mit der Munition, die er vorfindet.]]></wl:sentence><wl:sentence wl:id=\"326aadb759e32643370c0b4e79d04ad6\" wl:pos=\"NE ADJA NN NE NE VAFIN PPER VVINF VMFIN $.\" wl:dependency=\"1 -1 3 4 5 6 7 1 1 1\" wl:token=\"0,12 13,23 24,41 42,47 48,53 54,57 58,60 61,68 69,75 75,76\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Vollenwyders glückloser Nachfolgekandidat Marco Camin hat es erleben müssen.]]></wl:sentence><wl:sentence wl:id=\"5f3cbb928e4ae6d4fa3699ab297d4f84\" wl:pos=\"PPER VAFIN ADJD $, KOUS NE NE ART ADJA NN VVPP VAFIN $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 1 -1\" wl:token=\"0,2 3,6 7,10 10,11 12,16 17,23 24,35 36,41 42,51 52,59 60,71 72,75 75,76\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Es ist gut, dass Martin Vollenwyder einen spontanen Rülpser abgesondert hat.]]></wl:sentence><wl:sentence wl:id=\"e3f2be68b3a0852e9350f87136c13508\" wl:pos=\"APPR ADJA NN VAFIN PPER ADJD VVINF $, PRELS PPER APPR ADJA NN CARD NN ADJD VVPP VAFIN $. ART NN APPR NN VVINF $.\" wl:dependency=\"1 -1 3 4 5 6 7 1 9 10 11 12 13 14 15 16 17 18 19 20 21 22 1 1 1\" wl:token=\"0,3 4,12 13,24 25,29 30,32 33,39 40,43 43,44 45,48 49,51 52,55 56,67 68,82 83,86 87,92 93,104 105,110 111,114 114,115 116,119 120,125 126,128 129,133 134,140 140,141\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Bei nächster Gelegenheit wird er sicher tun, was er als städtischer Finanzminister elf Jahre erfolgreich getan hat: die Dinge zu Ende denken.]]></wl:sentence></wl:page>"""},
				{"isRelevant" = False , doc = """<?xml version=\"1.0\" encoding=\"UTF-8\"?><wl:page xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:wl=\"http://www.weblyzard.com/wl/2013#\" xml:lang=\"de\"><wl:sentence wl:id=\"c22823decb996de492c41461506f385c\" wl:pos=\"ADJD NE NN VVFIN APPR NE NE ART CARD NN CARD NN CARD ADJA NE NE NE $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 12 13 14 15 1 1 1\" wl:token=\"3,13 14,21 22,29 30,35 36,40 41,52 53,59 60,63 65,68 69,74 75,77 78,84 85,89 90,93 94,100 101,109 111,117 117,118\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[﻿  schauplatz Manilas Polizei räumt nach Geiseldrama Fehler ein  153 words 25 August 2010 St. Galler Tagblatt  Manila.]]></wl:sentence><wl:sentence wl:id=\"9805d2681624dee8f4d9d361df20f280\" wl:pos=\"APPR ART ADJA NN ART NN APPR NE APPR CARD ADJA NN APPR NE VAFIN ART ADJA NN NE VVPP $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 1 1 1\" wl:token=\"0,4 5,8 9,17 18,22 23,26 27,39 40,42 43,49 50,53 54,58 59,64 65,74 75,78 79,87 88,91 92,95 96,110 111,122 123,129 130,140 140,141\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Nach dem blutigen Ende des Geiseldramas in Manila mit acht toten Touristen aus Hongkong hat der philippinische Polizeichef Fehler eingeräumt.]]></wl:sentence><wl:sentence wl:id=\"5551783516c3805146506fd43e3f0564\" wl:pos=\"ADV VAFIN ART NN ART ADJA NN VVFIN $, ADV VAFIN ADJA NN APPR ART NN KON ART ADJA NN PTKZU VVINF VAPP $, VVFIN NN NE NE APPRART NN $.\" wl:dependency=\"1 2 -1 4 5 6 7 8 9 10 11 12 13 14 15 16 2 18 19 20 21 22 2 2 25 26 27 28 2 2 2\" wl:token=\"0,4 5,9 10,13 14,21 22,25 26,35 36,53 54,62 62,63 64,71 72,77 78,83 84,90 91,103 104,107 108,126 127,130 131,134 135,146 147,153 154,156 157,165 166,173 173,174 175,180 181,196 197,205 206,214 215,217 218,227 227,228\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Zwar habe die Polizei die richtigen Einsatzleitlinien verfolgt, dennoch seien klare Mängel hinsichtlich der Leistungsfähigkeit und der verwendeten Taktik zu erkennen gewesen, sagte Polizeidirektor Leocadio Santiago am Fernsehen.]]></wl:sentence><wl:sentence wl:id=\"9cb8d8cbe62f604a7c4fb1808dc17796\" wl:pos=\"PDS VMFIN ADV ADV VVPP VAINF $.\" wl:dependency=\"1 -1 1 1 1 1 1\" wl:token=\"0,4 5,10 11,14 15,21 22,31 32,38 38,39\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Dies müsse nun weiter überprüft werden.]]></wl:sentence><wl:sentence wl:id=\"f238694b5abab3ac426e4c18cf9440f3\" wl:pos=\"ART NN VAFIN PRF APPRART NN ART NN VVPP $, KOUS ART ADJA NN VVPP VAFIN $, KOUS ART NN PIDAT NN VVINF VMFIN $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 1 1 1\" wl:token=\"0,3 4,11 12,16 17,21 22,25 26,36 37,40 41,47 48,59 59,60 61,68 69,72 73,83 84,90 91,100 101,105 105,106 107,111 112,115 116,125 126,130 131,138 139,144 145,150 150,151\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Die Polizei habe sich zur Erstürmung des Busses entschieden, nachdem der entkommene Fahrer berichtet habe, dass der Kidnapper alle Geiseln töten wolle.]]></wl:sentence><wl:sentence wl:id=\"9c1d45e4a8cd58971be3b03bda4715df\" wl:pos=\"ART ADJD ADJA ADJA NN VAFIN APPRART NN APPR NE ART NN APPR CARD NN KON CARD NN KON ART NN APPR NE APPR PPOSAT NN VVPP $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 1 20 1 22 23 24 25 1 1 1\" wl:token=\"0,3 4,10 11,22 23,33 34,42 43,48 49,51 52,58 59,61 62,68 69,74 75,87 88,91 92,93 94,106 107,112 113,115 116,125 126,129 130,135 136,147 148,151 152,160 161,163 164,169 170,176 177,185 185,186\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Ein schwer bewaffneter ehemaliger Polizist hatte am Montag in Manila einen Touristenbus mit 4 Philippinern sowie 20 Touristen und einem Reiseleiter aus Hongkong in seine Gewalt gebracht.]]></wl:sentence><wl:sentence wl:id=\"17b1a1b50c7d5c3b51ae3e8394549559\" wl:pos=\"ART APPR ART ADJA NN ADJA NN VMFIN PPOSAT NN APPR ART NN VVINF $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 12 1 1 1\" wl:token=\"0,3 4,9 10,15 16,24 25,39 40,50 51,55 56,62 63,68 69,86 87,89 90,93 94,107 108,117 117,118\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Der wegen eines schweren Fehlverhaltens entlassene Mann wollte seine Wiedereinstellung in den Polizeidienst erreichen.]]></wl:sentence><wl:sentence wl:id=\"4d140f1f6f15d33e6d4ae2aa6910817b\" wl:pos=\"APPR ADJA NN VAFIN PPER ADJD APPR NN VVPP $.\" wl:dependency=\"1 -1 3 4 5 6 7 1 1 1\" wl:token=\"0,4 5,18 19,30 31,36 37,39 40,52 53,56 57,71 72,82 82,83\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Nach zehnstündigem Nervenkrieg wurde er schliesslich von Einsatzkräften erschossen.]]></wl:sentence><wl:sentence wl:id=\"de2dda0a6e7b2d7d80dff5de778daf16\" wl:pos=\"ADV CARD NN APPR NE VVFIN APPRART NN $, CARD ADJA VAFIN VVPP $.\" wl:dependency=\"1 -1 3 4 5 6 7 8 9 10 11 1 1 1\" wl:token=\"0,4 5,9 10,18 19,22 23,31 32,39 40,42 43,53 53,54 55,61 62,69 70,76 77,85 85,86\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[Auch acht Urlauber aus Hongkong starben im Kugelhagel, sieben weitere wurden verletzt.]]></wl:sentence><wl:sentence wl:id=\"616e80c6405c6b66c21c7f87b0c2c661\" wl:pos=\"( NE )\" wl:dependency=\"1 -1 1\" wl:token=\"0,1 1,4 4,5\" wl:sem_orient=\"0.0\" wl:significance=\"0.0\"><![CDATA[(sda)]]></wl:sentence></wl:page>"""},
				]

        # 2. step: send processed document to the classifier
        media_criticism = MediaCriticism()
		for(jeremia_xml_document in jeremia_xml_documents)
			result = media_criticism.check_domain_relevance(jeremia_xml_document)
			print result
			assert result['relevantDocument'] == jeremia_xml_document['isRelevant']
        self.assertTrue(result is not None)

if __name__ == '__main__':
    unittest.main()
