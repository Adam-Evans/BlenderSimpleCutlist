import bpy, os

# select all the mesh objects in the scene
objects = bpy.context.scene.objects
for ob in objects:
    ob.select_set(ob.type == "MESH")

# get the current selection
selection = bpy.context.selected_objects

result = ""

# iterate through the selected objects
for sel in selection:
    # get the current object's dimensions; convert from meters to mm, 2dp.
    dims = sel.dimensions
    x = float(round(sel.dimensions.x * 1000, 2))
    y = float(round(sel.dimensions.y * 1000, 2))
    z = float(round(sel.dimensions.z * 1000, 2))
    mat = sel.active_material.name if sel.active_material else "None"

    # write the selected object's name material and dimensions to a string for the file output
    result += "%s , %s, %.02f , %.02f , %.02f\n" % (sel.name, mat, x, y, z)

filename = "/home/adam/Documents/CutList.csv"
# confirm path exists
os.makedirs(os.path.dirname(filename), exist_ok=True)
# open the file to write to
file = open(filename, "w")
# write the data to file
file.write("Name, Mat, Length, Width, Height\n")
file.write(result)
# close the file
file.close()
