class Cell:
	@property
	def state(self):
		return self._state
	@state.setter
	def state(self,value):
		print("-------------")
		if 'alive' in value.lower():
			self._state = 'alive'
		else:
			self._state = 'dead'
	#is_dead属性设置getter方法
	#只有getter方法属性是只读属性
	@property
	def is_dead(self):
		return not self._state.lower=='alive'

	def is_good(self):


c= Cell()
#修改state属性
c.state="Alive"
#访问state属性
print(c.state)
#访问is_dead属性
print(c.is_dead) #如果没有装修器就要显示调用
#c.is_dead="d"
