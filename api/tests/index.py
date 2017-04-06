from app import app
from datetime import datetime
import unittest, json

class IndexTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.resp = self.app.get('/')

	def test_200(self):
		self.assertEquals(self.resp.status_code, 200)

	def test_status(self):
		jsonified = json.loads(self.resp.data)
		self.assertEqual(jsonified['status'], "OK")

	def test_time(self):
		datetimenow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
		jsonified = json.loads(self.resp.data)
		resp_time = str(jsonified['time'])
		self.assertEqual(resp_time, datetimenow)

	def test_time_utc(self):
		utcdatetimenow = datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
		jsonified = json.loads(self.resp.data)
		resp_time = str(jsonified['utc_time'])
		self.assertEqual(resp_time, utcdatetimenow)
