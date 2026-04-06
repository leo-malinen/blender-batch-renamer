import bpy

class SleekRenamerProperties(bpy.types.PropertyGroup):
    target: bpy.props.EnumProperty(
        name="Target",
        description="Objects to rename",
        items=[('SELECTED', "Selected", "Only selected objects"),
               ('ALL', "All", "All objects in scene")]
    )
    find_str: bpy.props.StringProperty(
        name="Find",
        description="Text to find in the object name",
        default=""
    )
    replace_str: bpy.props.StringProperty(
        name="Replace",
        description="Text to replace the found text with",
        default=""
    )
    prefix: bpy.props.StringProperty(
        name="Prefix",
        description="Text to add to the start of the name",
        default=""
    )
    base_name: bpy.props.StringProperty(
        name="Base Name",
        description="Replace entire name with this (automatically adds numbering)",
        default=""
    )
    suffix: bpy.props.StringProperty(
        name="Suffix",
        description="Text to add to the end of the name",
        default=""
    )
