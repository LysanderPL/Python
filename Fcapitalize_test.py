from Fcapitalize import first_up
import unittest

class Test(unittest.TestCase):
  def test_my_function(self):
    self.assertEqual(first_up("spam spam spam"), "Spam Spam Spam")

  def test_my_function2(self):
    self.assertTrue("Its Not A Test",
    first_up('its not a test'))
       
                        

if __name__ == '__main__':
  unittest.main(exit=False)
        

