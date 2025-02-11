import  bpy
from .my_menu import TOPBAR_MT_my_menu

bl_info={
    "name":"レベルエディタ",
    "author":"Masami Tsuzukibashi",
    "version":(1,0),
    "blender":(3,3,1),
    "location":"",
    "description":"レベルエディタ",
    "warning":"",
    "wiki_url":"",
    "tracker_url":"",
    "category":"Object"
}

def draw_menu_manual(self,context):
    self.layout.operator("wm.url_open_preset",text="Manual",icon='HELP')
    
classes=(
    MYADDON_OT_stretch_vertex,
    MYADDON_OT_create_ico_sphere,
    MYADDON_OT_export_scene,
    TOPBAR_MT_my_menu,
    OBJECT_PT_add_file_name,
    MYADDON_OT_add_filename,
    MYADDON_OT_add_collider,
    OBJECT_PT_collider,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    DrawCollider.handle=bpy.types.SpaceView3D.draw_handler_add(DrawCollider.draw_collider,(),"WINDOW","POST_VIEW")
    print("レベルエディタが有効化されました。")
    
def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    for cls in classes:
        bpy.utils.unregister_class(cls)
        bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle,"WINDOW")
    print("レベルエディタが無効化されました。")

if __name__=="__main__":
    register()
