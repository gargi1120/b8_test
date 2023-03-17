from django.test import TestCase

# Create your tests here.
# model ka testing karana hai 

from .models import Product

class ModelTest(TestCase):
    def testProductModel(self):
        product = Product.objects.create(name ="Toycar", price = 800)   # jab product create hota hai to product return  bhi kararata hai
        self.assertEquals(str(product), 'Toycar') #product madhye product cha obj asel str method return karety mhanun str(product) mhanaje Toycar yeil ani doghanch comaparision hoil
        print("IsInstance : ", isinstance(product, Product)) # product ye Product ka instance hona chahiye 
        self.assertTrue(isinstance(product, Product)) #product ye Product class ka instance hona chahiye 