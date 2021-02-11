import MsgBox
from time import time
def r():
	t = time()
	a = MsgBox.message('DTCG', 'dfdgfy', '37')
	print(t - time())
	if a == "Retry":
		r()
	else:
		pass


r()
