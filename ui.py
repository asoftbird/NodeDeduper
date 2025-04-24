import bpy

class NodeDeduper(bpy.types.Menu):
    bl_label = "NodeDeduper"
    bl_idname = "WINDOW_MT_NodeDeduper"

    def draw(self, context):
        layout = self.layout

        layout.operator("node.undupe", text="Query")

def draw_item(self, context):
    layout = self.layout
    layout.menu(NodeDeduper.bl_idname)