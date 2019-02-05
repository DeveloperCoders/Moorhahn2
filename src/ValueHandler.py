class Handler:
	def __init__(self):
		pass

	class memory:
		def __init__(self):
			self.mem =  {}
		def add(self,image,coordinates):
				self.mem[image] = coordinates

		def Up(self,value):
			x = lambda x: x+value
			for i in self.mem:
				self.mem[i] = tuple(map(x,self.mem[i]))
		def Down(self,value):
			x = lambda x: x-value
			for i in self.mem:
				self.mem[i] = tuple(map(x,self.mem[i]))

	 	def set(self,object,coordinates):
			if object in self.mem.keys():
					self.mem[object] = coordinates	
	
			else:
				raise MemoryError("Object not found")
		def delete(self,object):
			del self.mem[object]
