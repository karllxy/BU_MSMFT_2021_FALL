class point:
    """a blueprint for objects that represent a rectangular shape
    """
    
    def __init__(self,x,y):#init必须两条横线
        """the rectangle constructor"""
        self.x = x
        self.y = y
        # self.width = init_width
        # self.height = init_height
        
    # def grow(self,dwidth,dheight):
    #     self.width += dwidth
    #     self.height += dheight
    
    # def scale(self,factor):
    #     self.width *= factor
    #     self.height *= factor
    
    #special methods __repr__ string representaiton
    def __repr__(self):
        return f"Point at ({self.x},{self.y})"

    
    #special method: __eq__operator
    def __eq__(self,other):
        """define a special implementation of the  ==operation."""
        
        return self.x == other and self.y == other.y
    
    
    
    
    
    #define the power operator
    def __ipow__(self,e):
        self.x **= e
        self.y **= e
        
        return self
    
    
    
    def __pow__(self,e):
        x = self.x ** e
        y = self.y ** e
        
        return point(x,y)






if __name__ == '__main__':
    
   p1 = point(0,0)
   p2 = point(6,6)
   p3 = point(0,0)
   
   p4 = p1
    