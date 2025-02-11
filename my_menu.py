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


class TOPBAR_MT_my_menu(bpy.types.Menu):
    bl_idname="TOPBAR_MT_my_menu"
    bl_label="Mymenu"
    bl_description="拡張メニュー by ..." 
    def draw(self,context):
        self.layout.operator(MYADDON_OT_stretch_vertex.bl_idname,
            text=MYADDON_OT_stretch_vertex.bl_label)
    
        self.layout.operator(MYADDON_OT_create_ico_sphere.bl_idname,
            text=MYADDON_OT_create_ico_sphere.bl_label)
    
        self.layout.operator(MYADDON_OT_export_scene.bl_idname,
            text=MYADDON_OT_export_scene.bl_label)
    
        self.layout.operator(OBJECT_PT_add_file_name.bl_idname,
            text=OBJECT_PT_add_file_name.bl_label)
    
        self.layout.operator(MYADDON_OT_add_filename.bl_idname,
            text=MYADDON_OT_add_filename.bl_label)
    
        self.layout.operator(DrawCollider.bl_idname,
            text=DrawCollider.bl_label)
    
        self.layout.operator(MYADDON_OT_add_collider.bl_idname,
            text=MYADDON_OT_add_collider.bl_label)
    
        self.layout.operator(OBJECT_PT_collider.bl_idname,
            text=OBJECT_PT_collider.bl_label)
    
    def submenu(self,context):
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)
