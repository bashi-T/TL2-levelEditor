import  bpy


class OBJECT_PT_add_file_name(bpy.types.Panel):
    """オブジェクトのファイルネームパネル"""
    bl_idname="OBJECT_PT_file_name"
    bl_label="FileName"
    bl_space_type="PROPERTIES"
    bl_region_type="WINDOW"
    bl_context="object"

    def draw(self,context):
        if "file_name"in context.object:
            self.layout.prop(context.object,'["file_name"]',text=self.bl_label)
        else:
            self.layout.operator(MYADDON_OT_add_filename.bl_idname)

class MYADDON_OT_add_filename(bpy.types.Operator):
    bl_idname="myadddon.myaddon_ot_add_filename"
    bl_label="Filename 追加"
    bl_description="['file_name']カスタムプロパティを追加します"
    bl_options={"REGISTER","UNDO"}

    def execute(self,context):
        context.object["file_name"]=""
        return {"FINISHED"}
