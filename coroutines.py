# Thinking about Beazley's examples

def coroutine(func):
	"""
	Decorator that primes a coroutine by calling
	its next() method so that it is ready for send().
	"""
	def wrapper(*args, **kwargs):
		f = func(*args, **kwargs)
		f.next()
		return f
	return wrapper

@coroutine
def reprinter():
	item = (yield)
	print item

@coroutine
def grep(pattern):
	while True:
		line = (yield)
		if pattern in line:
			print line,
