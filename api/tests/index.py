from app import app
from datetime import datetime
import unittest, json

class IndexTestCase(unittest.TestCase):
	def setUp(self):
		conn = app.test_client()
		self.resp = conn.get('/')
		self.jsonified = json.loads(self.resp.data)

	def test_200(self):
		self.assertEqual(self.resp.status_code, 200)

	def test_status(self):
		self.assertEqual(self.jsonified['status'], "OK")

	def test_time(self):
		datetimenow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
		resp_time = str(self.jsonified['time'])
		self.assertEqual(resp_time, datetimenow)

	def test_time_utc(self):
		utcdatetimenow = datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
		resp_time = str(self.jsonified['utc_time'])
		self.assertEqual(resp_time, utcdatetimenow)
