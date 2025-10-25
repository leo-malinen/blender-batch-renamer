import bpy
from bpy.types import Panel


class OBJECT_PT_batch_rename(Panel):
    bl_label = "Batch Rename Helper"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'render'

    def draw(self, context):
        layout = self.layout
        props = context.scene.batch_rename_props

        layout.prop(props, "base_name")

        col = layout.column(align=True)
        col.prop(props, "use_prefix")
        if props.use_prefix:
            col.prop(props, "prefix")

        col.prop(props, "use_suffix")
        if props.use_suffix:
            col.prop(props, "suffix")

        col.prop(props, "use_numbering")
        if props.use_numbering:
            col.prop(props, "start_number")
            col.prop(props, "padding")

        layout.operator("object.batch_rename", icon="OUTLINER_DATA_FONT")


def register():
    bpy.utils.register_class(OBJECT_PT_batch_rename)


def unregister():
    bpy.utils.unregister_class(OBJECT_PT_batch_rename)
