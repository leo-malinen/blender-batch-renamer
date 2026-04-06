import bpy

class VIEW3D_PT_sleek_renamer(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renamer'
    bl_label = "Batch Rename"

    def draw(self, context):
        layout = self.layout
        props = context.scene.sleek_renamer_props
        
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Apply To:", icon='OUTLINER_OB_MESH')
        col.prop(props, "target", text="")
        
        layout.separator()
        
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Search & Replace:", icon='VIEWZOOM')
        col.prop(props, "find_str", text="Find")
        col.prop(props, "replace_str", text="Replace")
        
        layout.separator()
        
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Naming Rules:", icon='ADD')
        col.prop(props, "prefix", text="Prefix")
        col.prop(props, "base_name", text="Base Name")
        col.prop(props, "suffix", text="Suffix")
        
        layout.separator()
        
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.sleek_batch_rename", icon='CHECKMARK')
