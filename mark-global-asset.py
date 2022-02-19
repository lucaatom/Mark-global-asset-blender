bl_info = {
    "name": "Mark/clear global asset",
    "blender": (3, 0, 0),
    "category": "Object",
}

import bpy 
import os

class MarkGlobalAsset(bpy.types.Operator):
    """Mark/clear Global Asset"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.mark_global_asset"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Mark/clear Global Asset"         # Display name in the interface.
    bl_options = {'REGISTER'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the 
        mark_global_asset(context)

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.
    
def menu_func(self, context):
    self.layout.operator(MarkGlobalAsset.bl_idname)
    
def draw_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator("object.mark_global_asset", text="Mark/clear Global Asset")

def register():
    bpy.utils.register_class(MarkGlobalAsset)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    bpy.types.VIEW3D_MT_object_context_menu.append(draw_menu)

def unregister():
    bpy.utils.unregister_class(MarkGlobalAsset)
    bpy.types.VIEW3D_MT_object_context_menu.remove(draw_menu)
    

if __name__ == "__main__":
    register()

    
    
def mark_global_asset(context):
    prefs = bpy.context.preferences
    filepaths = prefs.filepaths
    asset_libraries = filepaths.asset_libraries
    assetsPath = asset_libraries[0].path
    
    try:
        bpy.ops.asset.mark()
    except:
        bpy.ops.asset.clear(set_fake_user=False)

    
    blendname = bpy.path.basename(bpy.data.filepath)
    bpy.ops.wm.save_as_mainfile(copy=True, filepath=assetsPath + blendname)


