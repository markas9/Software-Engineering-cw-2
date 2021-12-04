init python:
 

    class Place(object):
       
        def __init__(self, xloc, yloc, name, isActive):
            
            self.xloc = xloc
            self.yloc = yloc
            self.name = name
            self.isActive = isActive
        
        @property
        def icons(self):
            icon= "icons/" + self.name.lower() + " icon.png"
            return icon

        @property
        def iconsHover(self):
            icons= "icons/" + self.name.lower() + " icons.png"
            return icons
            
    Places =[]
  
    counter=0


    while counter<1000:
        Places.append(Place(0,0,"", False))
        counter +=1

    
    Places[0] = Place(350,150,"math_department", True)
    Places[1] = Place(200,300, "cs_department", True)
    Places[2] = Place(820,330,"languages_department", True) 
    Places[3] = Place(1500,550,"Library", True)


            