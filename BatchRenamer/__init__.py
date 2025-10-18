# __init__.py
# Batch Rename Helper Add-on
# Contributor(s): Aaron Powell, Leo Malinen

bl_info = {
    "name": "Batch Rename Helper",
    "description": "Batch rename selected objects with prefix, suffix, and numbering.",
    "author": "Aaron Powell",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Properties > Render > Batch Rename Helper",
    "warning": "",
    "wiki_url": "http://my.wiki.url",
    "tracker_url": "http://my.bugtracker.url",
    "support": "COMMUNITY",
    "category": "Object"
}

import bpy

# Operator for renaming
class OBJECT_OT_batch_rename(bpy.types.Operator):
    bl_idname = "object.batch_rename"
    bl_label = "Batch Rename Objects"
    bl_description = "Rename selected objects with chosen settings"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        props = scene.batch_rename_props

        selected_objects = context.selected_objects
        if not selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}

        for i, obj in enumerate(selected_objects, start=props.start_number):
            new_name = props.base_name

            if props.use_prefix and props.prefix:
                new_name = f"{props.prefix}_{new_name}"

            if props.use_suffix and props.suffix:
                new_name = f"{new_name}_{props.suffix}"

            if props.use_numbering:
                new_name = f"{new_name}_{i:0{props.padding}d}"

            obj.name = new_name

        return {'FINISHED'}


def register():
    from . import properties
    from . import ui
    properties.register()
    ui.register()
    bpy.utils.register_class(OBJECT_OT_batch_rename)


def unregister():
    from . import properties
    from . import ui
    bpy.utils.unregister_class(OBJECT_OT_batch_rename)
    ui.unregister()
    properties.unregister()


if __name__ == "__main__":
    register()
