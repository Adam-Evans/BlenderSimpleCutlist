Usage: 

Open blender, in a new settings tab open scripting,

type in the console: bpy.utils.user_resource("SCRIPTS", path="modules")

copy the output of this. 

you can use this to add modules to blender using pip install. 

For this, we will need: 

pip install openpyxl --target="{result from above}"
pip install pillow --target="{result from above}"

paste in text from cutlist.py to text editor. Change output directory to whereever you want and run :) 
