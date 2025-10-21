"""Solution to Ellen's Alien Game exercise."""

total_aliens_created=0
class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created =0
    health=3
    def __init__(self,x_coordinate,y_coordinate):
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
        Alien.total_aliens_created +=1
    def hit(self):
        self.health -=1
    def is_alive(self):
        if self.health>0:
            return True
        else:
            return False
    def teleport(self,x_coordinate,y_coordinate):
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
    def collision_detection(self,other_object):
        pass
        

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection (alien_start_positions):
    alien_list=[]
    for a in alien_start_positions:
        alien_new = list(a)
        alien=Alien(alien_new[0],alien_new[1])
        alien_list.append(alien)
        
        
    return alien_list
    