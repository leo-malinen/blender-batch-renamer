# __init__.py
# Batch Rename Helper Add-on
# Contributor(s): Leo Malinen, Aaron Powell (template maker)

bl_info = {
    "name": "Sleek Batch Renamer",
    "author": "Your Name",
    "version": (1, 0, 0),
    "blender": (4, 5, 5),
    "location": "View3D > Sidebar > Renamer",
    "description": "A simplistic, sleek UI for batch renaming objects.",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy

if "bpy" in locals():
    import importlib
    importlib.reload(properties)
    importlib.reload(ui)
else:
    from . import properties
    from . import ui

# --- Operator (The Logic) ---
class OBJECT_OT_sleek_batch_rename(bpy.types.Operator):
    bl_idname = "object.sleek_batch_rename"
    bl_label = "Apply Rename"
    bl_description = "Apply the renaming rules to the targeted objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.sleek_renamer_props
        
        if props.target == 'SELECTED':
            objs = context.selected_objects
        else:
            objs = context.scene.objects
            
        for i, obj in enumerate(objs):
            new_name = obj.name
            
            if props.find_str:
                new_name = new_name.replace(props.find_str, props.replace_str)
                
            if props.base_name:
                new_name = f"{props.base_name}_{i+1:03d}"
                
            new_name = f"{props.prefix}{new_name}{props.suffix}"
            
            obj.name = new_name
            
        self.report({'INFO'}, f"Successfully renamed {len(objs)} objects.")
        return {'FINISHED'}

classes = (
    properties.SleekRenamerProperties,
    OBJECT_OT_sleek_batch_rename,
    ui.VIEW3D_PT_sleek_renamer,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.sleek_renamer_props = bpy.props.PointerProperty(type=properties.SleekRenamerProperties)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.sleek_renamer_props

if __name__ == "__main__":
    register()
