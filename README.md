# Node deduper
Removes duplicate node groups from a blend file, and remaps all users from duplicates with a higher number to the original node group.
If you clone a node group to make specific adjustments, remember to rename it to indicate a difference, otherwise this addon will remove your cloned node. 

Useful in case of appended node groups that use node groups already in the file you're appending them to.

For example, NodeGroup.003, NodeGroup.002 and NodeGroup.001 will all be remapped to NodeGroup, and then any duplicates with numbers in the name will be removed.

# Usage
Use the Search function to look for "Deduplicate node groups". You can bind this to a hotkey if you like. 
Information on deduplicated node groups will be shown in the System Console.