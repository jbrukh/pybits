from coroutines import coroutine
import heapq
import re
import sys

class SubComparable(object):
	
	def __init__(self, line, pattern):
		self.line = line
		if pattern:
			s = re.search(pattern, line)
			if s:
				self.substr = s.group(0)
			else:
				self.substr = line

	def __lt__(self,other):
		return self.substr.__lt__(other.substr)

	def __repr__(self):
		return "'%s'"%self.line
	
	def __str__(self):
		return self.substr


pattern = None
if len(sys.argv) > 1:
	pattern = sys.argv[1]

h = []
for line in sys.stdin.readlines():
	subline = SubComparable(line.strip(), pattern)
	heapq.heappush(h,subline)
	print h

for i in range(len(h)):
	print heapq.heappop(h)
