import bpy
from bpy.types import PropertyGroup
from bpy.props import (
    StringProperty,
    BoolProperty,
    IntProperty,
    PointerProperty
)


class BatchRenameProperties(PropertyGroup):
    base_name: StringProperty(
        name="Base Name",
        description="Base name for objects",
        default="Object"
    )

    use_prefix: BoolProperty(
        name="Use Prefix",
        default=False
    )
    prefix: StringProperty(
        name="Prefix",
        default=""
    )

    use_suffix: BoolProperty(
        name="Use Suffix",
        default=False
    )
    suffix: StringProperty(
        name="Suffix",
        default=""
    )

    use_numbering: BoolProperty(
        name="Use Numbering",
        default=True
    )
    start_number: IntProperty(
        name="Start Number",
        default=1,
        min=0
    )
    padding: IntProperty(
        name="Number Padding",
        default=3,
        min=1,
        max=6
    )


def register():
    bpy.utils.register_class(BatchRenameProperties)
    bpy.types.Scene.batch_rename_props = PointerProperty(type=BatchRenameProperties)


def unregister():
    del bpy.types.Scene.batch_rename_props
    bpy.utils.unregister_class(BatchRenameProperties)
