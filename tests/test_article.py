import unittest
from app.models import Article

class TestArticle(unittest.TestCase):

    def setUp(self):
        self.new_article = Article('Jay Peters','Block and Blockstream are partnering with Tesla on an open-source, solar-powered Bitcoin mine, the companies announced Friday. Teslas 3.8-megawatt Solar PV array and its 12 megawatt-hour Megapack will power the facility, and construction has started on the p…','2022-04-29T13:15:44Z','https://www.engadget.com/beats-fit-pro-studio-buds-airpods-sale-131544330.html','"https://s.yimg.com/os/creatr-uploaded-images/2022-04/8b62a350-c7b8-11ec-a5af-d26c5ceedf70','Beats Fit Pro are on sale for $180 right now')
    def test_init(self):
        self.assertTrue(isinstance(self.new_article,Article))