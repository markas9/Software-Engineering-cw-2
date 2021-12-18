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

    
    Places[0] = Place(330,270,"math_department", True)
    Places[1] = Place(520,600, "cs_department", True)
    Places[2] = Place(825,270,"languages_department", True) 
    Places[3] = Place(1360,300, "art_department", True)
    Places[4] = Place(1170,650,"music_department", True)


            