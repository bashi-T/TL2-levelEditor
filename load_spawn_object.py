import bpy

class MYADDON_OT_load_spawn_object(bpy.types.Operator):
    bl_idname="myaddon.myaddon_ot_load_spawn_object"
    bl_label="出現ポイントシンボルImport"
    bl_description="出現ポイントのシンボルをImportします"
    bl_options={"REGISTER","UNDO"}
    prototype_object_name="PrototypePlayerSpawn"
    object_name="PlayerSpawn"

    def execute(self,context):
        return {'FINISHED'}