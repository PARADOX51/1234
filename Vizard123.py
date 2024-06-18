import viz
import vizshape
import vizact
import vizcam
import random

viz.go()

spawn_position = [0, 1, -5]

stl_file1 = "C:/Users/nmrom/Downloads/Swanky Juttuli.stl"
stl_file2 = "C:/Users/nmrom/Downloads/Fantabulous Luulia.stl"
tree_file = "C:/Users/nmrom/Downloads/Realistic Pine Tree.stl"

object1 = viz.add(stl_file1)
object1.setScale(0.01, 0.01, 0.01) 
object1.setPosition(spawn_position[0] - 2, spawn_position[1], spawn_position[2]) 
object1.color(viz.RED)

object2 = viz.add(stl_file2)
object2.setScale(0.05, 0.05, 0.05) 
object2.setPosition(spawn_position[0] + 2, spawn_position[1], spawn_position[2])  
object2.color(viz.BLUE)  

floor = vizshape.addPlane(size=(200, 200), axis=vizshape.AXIS_Y, cullFace=False)
floor.setPosition(0, 0, 0)
floor.color(viz.GRAY)

num_trees = 25  
tree_scale = 0.05  
forest_area = 200  

trees = []

for _ in range(num_trees):
    tree = viz.add(tree_file)
    tree.setScale(tree_scale, tree_scale, tree_scale)  
    tree.setPosition(random.uniform(-forest_area, forest_area), 0, random.uniform(-forest_area, forest_area))
    tree.color(viz.GREEN) 
    trees.append(tree)

# Function to change tree color on mouse click
def onMouseDown(e):
    x, y = viz.mouse.getPosition()
    info = viz.pick(x, y)
    if info.valid:
        obj = info.object
        if obj in trees:
            obj.color(random.choice([viz.RED, viz.BLUE, viz.YELLOW, viz.PURPLE, viz.ORANGE, viz.WHITE]))

viz.callback(viz.MOUSEDOWN_EVENT, onMouseDown)

# Set up navigation
navigation = vizcam.WalkNavigate()
navigation.setPosition([0, 1, 0])
navigation.moveScale = 3.0
viz.cam.setHandler(navigation)

viz.MainView.setPosition(0, 1, 5) 

# Hide the mouse cursor for a cleaner view
viz.mouse(viz.OFF)









