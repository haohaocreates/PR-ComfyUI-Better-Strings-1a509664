# import folder_paths
#
#
# class BetterPath:
#
#     def __init__(self):
#         pass
#
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "type": (folder_paths.get_filename_list("."),),
#                 "subtype": ("STRING", {"multiline": True}),
#                 "path": ("STRING", {"multiline": True}),
#             },
#         }
#
#     RETURN_TYPES = ("STRING",)
#     CATEGORY = "Better Things 💡"
#
#     def action(self, string):
#         return (string,)
#
#     FUNCTION = action.__name__
#
