class method:
	@staticmethod
	def test_3():
		print("staticmethod")

	def __del__(self):
		print("i m done")


s = method()
s.test_3()
f = s
# s = None
# f = method()
# f.test_3()


