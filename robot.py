from Tkinter import *

class PJoint: #Prismatic joint (linear)
    def __init__(self,):
		self.lengthmax #Length from previous joint to this one
		self.lengthmin
		self.mass
		
class RJoint: #Revolute joint (angular)
	def __init__(self):
		self.xang #x, y, and z angles relative to previous joint (361 if active angle)
		self.yang
		self.zang
		self.anglemin
		self.anglemax
		self.length #length of arm from previous joint (>=0)
		self.mass #mass of joint plus length of arm from previous joint
		
		
if __name__ == '__main__':
	arm=[]
	arm.append(
	root = Tk()
    	root.wm_withdraw()
	ConWin(root)
	root.mainloop()
