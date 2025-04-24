import bpy
import re

# def populateSearch(self, context):

#     current_nodegroup = context.space_data.edit_tree

#     node_groups = []
#     for node in current_nodegroup.nodes:
#         try:
#             if "Group" in node.name:
#                 node_groups.append((node.name, node.node_tree.name+f" ({node.name})", ""))
#         except AttributeError:
#             pass
    
#     result = tuple(node_groups)
#     return result

class NODE_OT_UNDUPE_NODEGROUPS(bpy.types.Operator):
    bl_idname = "node.undupe"
    bl_label = "Deduplicate node groups"
    bl_options = {'UNDO'}

    # @classmethod
    # def poll(cls, context):
    #     return True if hasattr(context, 'NODE_EDITOR') else False
    
    def execute(self, context):
        node_groups = bpy.data.node_groups

        for group in node_groups:
            unduped_name, *_ = re.split("\.\d+$", group.name) 
            if unduped_name in node_groups and unduped_name != group.name:
                original_size = len(group.nodes)
                dupe_size = len(node_groups[unduped_name].nodes)
        
                if original_size != dupe_size:
                    print(f"Length of {group.name} does not match {node_groups[unduped_name].name}! Skipping remap")
                else:
                    group.user_remap(node_groups[unduped_name])
                    print(f"Remapped {group.name} to {node_groups[unduped_name].name}!")

        else:
            group.name = unduped_name
        
        for group in node_groups:
            if group.use_fake_user == False and group.users == 0:
                print(f"Removed group {group.name}")
                node_groups.remove(group)

        return {'FINISHED'}
        
