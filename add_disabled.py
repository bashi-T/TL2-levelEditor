import  bpy
import  mathutils
import  copy
import  gpu
import  copy
import  mathutils

class MYADDON_OT_add_disabled(bpy.types.Operator):
    bl_idname="myaddon.myaddon_ot_add_disabled"
    bl_label="無効フラグ追加"
    bl_description="['disabled']カスタムプロパティを追加します。"
    bl_options={"REGISTER","UNDO"}

    def execute(self,context):
        #['collider']カスタムプロパティを追加
        context.object["disabled"]=True
        return {"FINISHED"}

#パネルコライダー
class OBJECT_PT_disabled(bpy.types.Panel):
    bl_idname="OBJECT_PT_disabled"
    bl_label="Disabled"
    bl_space_type="PROPARTIES"
    bl_region_type="WINDOW"
    bl_context="object"

    #サブメニュー描画
    def draw(self,context):
        #パネルに項目を追加
        if "disabled"in context.object:
            #プロパティがあればプロパティを表示
            self.layout.prop(context.object,'["disabled"]',text="disabled")
        else:
            #プロパティがなければプロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_disabled.bl_idname)

class DrawDisable:
    handle=None
    def draw_disabled():
        vertices={"pos":[]}

        indices=[]
        #camera_pos=mathutils.Vector()
        for area in bpy.context.window.screen.areas:
            if area.type !='VIEW_3D':
                continue

            #エディタのカメラを取得
            #region_3d=area.spaces.active.region_3d
            #back_vector=mathutils.Vector((0,0,1))
            #front_direction=region_3d.view_rotation @back_vector
            #view_to_camera=front_direction*region_3d.view_distance

            #camera_pos=region_3d.view_location+view_to_camera
            #print(f"Editoor Camera Location:{camera_pos}")
            break
        print("\n\n############BEGIN LOOP##############DrawObject")
        #現在のシーンのオブジェクトリストを走査
        for object in bpy.context.scene.objects:
            if not "disabled" in object:
                continue
            if not object["disabled"]:
                continue
            if object.type!="MESH":
                continue
            print("DrawObject"+object.name)
            obj_vertices=object.data.vertices.values()

            start_index=len(vertices["pos"])
            for v in obj_vertices:
                #オブジェクトの中心座標をコピー
                pos=copy.copy(v.co)
                pos=object.matrix_world@pos
                #頂点データリストに座標を追加
                vertices['pos'].append(pos)

            edges=object.data.edges
            for e in edges:
                indices.append([start_index+e.vertices[0],start_index+e.vertices[1]])

        #深度テスト有効化
        gpu.state.depth_test_set("LESS")
        #ビルトインのシェーダを取得
        shader=gpu.shader.from_builtin("UNIFORM_COLOR")
        #バッチ作成(引数：シェーダ、トポロジー、頂点データ、インデックスデータ)
        #batch=batch_for_shader(shader,"LINES",vertices,indices=indices)
        #シェーダのパラメータ設定
        color=[0.8,0.0,0.0,1.0]
        shader.bind()
        shader.uniform_float("color",color)
        #描画
        #batch.draw(shader)

