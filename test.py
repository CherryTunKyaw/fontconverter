# -*- coding: utf-8 -*-
import unittest
import uni2zg

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        zawgyi = u'''မည္သူကိုမၽွ ညႇဥ္းပန္း ႏွိပ္စက္ျခင္း၊'''
        unicode = u'''မည်သူကိုမျှ ညှဉ်းပန်း နှိပ်စက်ခြင်း၊
'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed converting Article One")

    #def test_myanmar_pangram(self):
        #zawgyi  = u'သီဟိုဠ္မွ ဉာဏ္ႀကီးရွဆင္သည္ အာယုဝၯနေဆးၫႊန္းစာကို ဇလြန္ေဈးေဘးဗာဒံပင္ထက္ အဓိ႒ာန္လ်က္ ဂဃနဏဖတ္ခဲ့သည္။'
        #unicode = u'သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် အာယုဝဍ္ဎနဆေးညွှန်းစာကို ဇလွန်ဈေးဘေးဗာဒံပင်ထက် အဓိဋ္ဌာန်လျက် ဂဃနဏဖတ်ခဲ့သည်။'
        #result = zg2uni.convert(zawgyi)
        #self.assertEqual(unicode, result, "Failed converting Myanmar Pangram")

if __name__ == "__main__":
    unittest.main()