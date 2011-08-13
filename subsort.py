from coroutines import coroutine
import heapq
import re
import sys

class SubComparable(object):
    """
    Comparator that orders strings by the lexicographical
    order of a subregex.
    """
    def __init__(self, line, pattern):
        self.line = line
        self.substr = None
        if pattern:
            s = re.search(pattern, line)
            if s:
                self.substr = s.group(0)

    def __lt__(self, other):
		if not self.substr:
			return self.line.__lt__(other.line)
		return self.substr.__lt__(other.substr)

    def __repr__(self):
        return self.line
    
pattern = None
if len(sys.argv) > 1:
	pattern = sys.argv[1]

h = []
for line in sys.stdin.readlines():
	subline = SubComparable(line.strip(), pattern)
	heapq.heappush(h,subline)

for i in range(len(h)):
	print heapq.heappop(h)
