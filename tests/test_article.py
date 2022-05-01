import unittest
from app.models import Article

class TestArticle(unittest.TestCase):
    """
    Test class to test the behavior of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.articles_object = Article('The Verge','Jay Peters','Block and Blockstream are partnering with Tesla on an open-source, solar-powered Bitcoin mine, the companies announced Friday. Teslas 3.8-megawatt Solar PV array and its 12 megawatt-hour Megapack will power the facility, and construction has started on the p…','Its set to open later this year\r\nIf you buy something from a Verge link, Vox Media may earn a commission. See our ethics statement.\r\nIllustration by Alex Castro / The Verge\r\nBlock and Blockstream, a … [+1336 chars]','2022-04-29T13:15:44Z','https://www.engadget.com/beats-fit-pro-studio-buds-airpods-sale-131544330.html','"https://s.yimg.com/os/creatr-uploaded-images/2022-04/8b62a350-c7b8-11ec-a5af-d26c5ceedf70','Beats Fit Pro are on sale for $180 right now')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.articles_object,Article))

    def test_init(self):
        self.assertEqual(self.articles_object.name,'The Verge')
        self.assertEqual(self.articles_object.name,'The Verge')