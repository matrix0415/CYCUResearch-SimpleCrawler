import time
from random import uniform

class timer:
	def __init__(self):
		self.timeSpent =""
		self.estSum =1
		
	def start(self):
		self.sTime =time.time()
		
	def end(self):
		self.eTime =time.time()
		self.timeSpent =self.eTime-self.sTime
		
	def spent(self):	# return a list[time, H/M/S]
		rs =[]
		if self.timeSpent>3600:	# change to Hour
			rs =[self.timeSpent/3600, "Hours"]
		if self.timeSpent>60:		# change to Minutes
			rs =[self.timeSpent/60, "Minutes"]
		else:
			rs =[self.timeSpent, "Seconds"]
		return rs
		
	def estimate(self, remainder):
		rs =[]
		self.eTime =time.time()
		spent =self.eTime-self.sTime
		self.estSum +=1
		if self.timeSpent !='':
			estBasedNum =spent/self.timeSpent # actual spent / estimate spent
			if estBasedNum >=300:
				spent/=uniform(1,2)
			elif estBasedNum >=100:
				self.timeSpent*=uniform(2,3)
			elif estBasedNum >=50:
				self.timeSpent*=uniform(1,2)
			elif estBasedNum <=1/60: # 1/5
				self.timeSpent/=uniform(1,2)
			elif estBasedNum <=1/120: #1/50
				self.timeSpent/=uniform(2,3)
			elif estBasedNum <=1/600:
				spent*=uniform(1,2)
			
			self.timeSpent =(spent+self.timeSpent*(self.estSum-1))/self.estSum
		else: # if timeSpend ==''
			self.timeSpent =self.eTime-self.sTime
			
		remainTime =remainder*self.timeSpent
		if remainTime<=60:		# change to Minutes
			rs =[remainTime, "Seconds"]
		elif remainTime<=3600:
			rs =[remainTime/60, "Minutes"]
		else:	# change to Hour
			rs =[remainTime/3600, "Hours"]
		return rs
		