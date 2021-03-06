class TestCase:
	def __init__(self, name):
		self.name = name

	def run(self):
		method = getattr(self, self.name)
		method()

	def setUp(self):
		pass

	def run(self):
		self.setUp()
		method = getattr(self, self.name)
		method()
		self.tearDown()

	def tearDown(self):
		pass


class WasRun(TestCase):
	def __init__(self, name):
		self.wasRun = None
		TestCase.__init__(self, name)

	def setUp(self):
		self.log = "setUp "

	def testMethod(self):
		self.log = self.log + "testMethod "

	def tearDown(self):
		self.log = self.log + "tearDown "


class TestCaseTest(TestCase):
	def setUp(self):
		self.test = WasRun("testMethod")

	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod tearDown " == test.log)


# test code
if __name__ == '__main__':
	TestCaseTest("testTemplateMethod").run()
