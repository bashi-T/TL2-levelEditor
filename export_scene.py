import  bpy
import  math
import  bpy_extras
import  json

class MYADDON_OT_export_scene(bpy.types.Operator,bpy_extras.io_utils.ExportHelper):
    bl_idname="myaddon.myaddon_ot_export_scene"
    bl_label="シーン出力"
    bl_description="シーン情報をエクスポートします"
    filename_ext=".json"

    def export(self):
        """ファイルに出力"""
        print("シーン情報出力開始...%r"%self.filepath)
        with open(self.filepath,"wt")as file:
            file.write("SCENE\n")
            for object in bpy.context.scene.objects:
                if object.parent:
                    continue

                self.parse_scene_recursive(file,object,0)

    def export_json(self):
        """JSON形式でファイルに出力"""
        json_object_root=dict()
        json_object_root["name"]="scene"
        json_object_root["objects"]=list()

        for object in bpy.context.scene.objects:
            if(object.parent):
                continue
            
            self.parse_scene_recursive_json(json_object_root["objects"],object,0)

        json_text=json.dumps(json_object_root,ensure_ascii=False,cls=json.JSONEncoder,indent=4)
        print(json_text)
        with open(self.filepath,"wt",encoding="utf-8")as file:
            file.write(json_text)

    def parse_scene_recursive_json(self,data_parent,object,level):
        json_object=dict()
        json_object["type"]=object.type
        json_object["name"]=object.name

        trans, rot, scale=object.matrix_local.decompose()
        rot=rot.to_euler()
        rot.x=math.degrees(rot.x)
        rot.y=math.degrees(rot.y)
        rot.z=math.degrees(rot.z)

        transform=dict()
        transform["translation"]=(trans.x,trans.y,trans.z)
        transform["rotation"]=(rot.x,rot.y,rot.z)
        transform["scaling"]=(scale.x,scale.y,scale.z)

        json_object["transform"]=transform

        if"file_name" in object:
            json_object["file_name"]=object["file_name"]

        if"collider" in object:
            collider=dict()
            collider["type"]=object["collider_center"].to_list()
            collider["center"]=object["collider_size"].to_list()
            json_object["collider"]=collider

        if "disabled" in object:
            json_object["disabled"]=object["disabled"]

        data_parent.append(json_object)

        if len(object.children) > 0:
            json_object["children"]=list()
            for child in object.children:
                self.parse_scene_recursive_json(json_object["children"],child,level+1)

    def execute(self,context):
        print("シーン情報をエクスポートします")
        self.export_json()
        self.report({'INFO'},"シーン情報をエクスポートしました")
        print("シーン情報をエクスポートしました")
        return{'FINISHED'}
    
    def write_and_print(self,file,str):
        print(str)
        file.write(str)
        file.write('\n')

    def parse_scene_recursive(self,file,object,level):
        """シーン解析用再帰関数"""
        indent=''
        for i in range(level):
            indent+="\t"
        
        self.write_and_print(file,indent + object.type)
        trans, rot, scale=object.matrix_local.decompose()
        rot=rot.to_euler()
        rot.x=math.degrees(rot.x)
        rot.y=math.degrees(rot.y)
        rot.z=math.degrees(rot.z)
        self.write_and_print(file,indent + "T %f %f %f"%(trans.x,trans.y,trans.z))
        self.write_and_print(file,indent + "R %f %f %f"%(rot.x,rot.y,rot.z))
        self.write_and_print(file,indent + "S %f %f %f"%(scale.x,scale.y,scale.z))
        if"file_name"in object:
            self.write_and_print(file,indent+"N %s"%object["file_name"])
        
        if "collider" in object:
            self.write_and_print(file,indent+"C %s" %object["collider"])
            temp_str=indent+"CC %f %f %f"
            temp_str%=(object["collider_center"][0],object["collider_center"][1],object["collider_center"][2])
            self.write_and_print(file,temp_str)
            temp_str=indent+"CS %f %f %f"
            temp_str%=(object["collider_size"][0],object["collider_size"][1],object["collider_size"][2])
            self.write_and_print(file,temp_str)

            
        self.write_and_print(file,indent+'END')
        self.write_and_print(file,'')

        for child in object.children:
            self.parse_scene_recursive(file,child,level + 1)
