import csv101
import re

class Tbl():

	def __init__(self,s):
		self.Row = {"cells":[], "cooked":[]}
		self.Row["cells"] = self.create_rows(s)
		self.cols = []
		self.oid = None

	def compiler(self,x):
		"return something that can compile strings of type x"
		try: int(x); return int
		except ValueError:
			try: float(x); return  float
			except ValueError: return str

	def string(self,s):
		"read lines from a string"
		for line in s.splitlines(): yield line

	def file(self,fname):
		"read lines from a fie"
		with open(fname) as fs:
			for line in fs: yield line

	def zipped(self,archive,fname):
		"read lines from a zipped file"
		with zipfile.ZipFile(archive) as z:
			with z.open(fname) as f:
				for line in f: yield line

	def rows(self,src, 
		sep=     ",",
		doomed = r'([\n\t\r ]|#.*)'):
		"convert lines into lists, killing whitespace and comments"
		for line in src:
			line = line.strip()
			line = re.sub(doomed, '', line)
			if line:
				yield [l for l in line.split(sep) if l]

	def cells(self, src):
		"convert strings into their right types"
		oks = None
		for n,cells in enumerate(src):
			if n==0:
				yield cells
			else:
				oks = [self.compiler(cell) for cell in cells]
				yield [f(cell) for f,cell in zip(oks,cells)]

	def fromString(self,s):
		"putting it all together"
		for lst in self.cells(self.rows(self.string(s))):
			yield lst
	
	def create_rows(self,s):
		lists = []
		for lst in self.fromString(s):
			lists.append(lst)
		return lists
	
	def filter(self):
		
		rows = self.Rows["cells"]
		columns = self.rows["cells"][0]
		for i,r in enumerate(rows):
			if '?' in r:
				self.rows["cells"].pop(i)
			if len(r) < columns:
				self.rows["cells"][i] = ["E"]
	 
				
				