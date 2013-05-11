import unittest
import httplib
import subprocess

host = "http://localhost"
port = "8080"

class ServiceTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    exitCode = subprocess.call("make start".split())
    cls.assertEquals(exitCode, 0)
    if (exitCode == 0):
      httplib.HTTPConnection(host, port)
