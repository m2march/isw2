import unittest
import httplib
import subprocess

host = "127.0.0.1"
port = "8080"

class ServiceTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.p = subprocess.Popen("make start".split(), stdout=None, stdin=None)

  def setUp(self):
        self.conn = httplib.HTTPConnection(host, port)

  def test_strategies(self):
        response = self.conn.request("GET", "/strategies")
        self.assertIsNotNone(response)

  def test_products(self):
        response = self.conn.request("GET", "/products")
        self.assertIsNotNone(response)

  @classmethod
  def tearDownClass(cls):
        cls.p.terminate()



