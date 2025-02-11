import  bpy

from .my_menu import TOPBAR_MT_my_menu
from .stretch_vertex import MYADDON_OT_stretch_vertex
from .create_ico_sphere import MYADDON_OT_create_ico_sphere
from .export_scene import MYADDON_OT_export_scene
from .add_file_name import OBJECT_PT_add_file_name
from .add_file_name import MYADDON_OT_add_filename
from .add_collider import DrawCollider
from .add_collider import MYADDON_OT_add_collider
from .add_collider import OBJECT_PT_collider
from .add_disabled import OBJECT_PT_disabled
from .add_disabled import MYADDON_OT_add_disabled
from .load_spawn_object import MYADDON_OT_load_spawn_object

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
    TOPBAR_MT_my_menu,
    MYADDON_OT_stretch_vertex,
    MYADDON_OT_create_ico_sphere,
    OBJECT_PT_add_file_name,
    MYADDON_OT_add_filename,
    MYADDON_OT_add_collider,
    OBJECT_PT_collider,
    MYADDON_OT_export_scene,
    MYADDON_OT_add_disabled,
    OBJECT_PT_disabled,
    MYADDON_OT_load_spawn_object,
)

def register():
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    DrawCollider.handle=bpy.types.SpaceView3D.draw_handler_add(DrawCollider.draw_collider,(),"WINDOW","POST_VIEW")
    for cls in classes:
        bpy.utils.register_class(cls)
        print("enabled :"+cls.bl_idname)
    print("レベルエディタが有効化されました。")
    
def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    for cls in classes:
        bpy.utils.unregister_class(cls)
        bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle,"WINDOW")
        print("disabled :"+cls.bl_idname)
    print("レベルエディタが無効化されました。")

if __name__=="__main__":
    register()
