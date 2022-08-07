
import bpy
import mathutils

import math


class CameraIO(object):
    """

    """

    def __init__(self):
        pass

    def get_camera_infos(self):
        active_camera = bpy.context.scene.camera
        camera_matrix = active_camera.matrix_world
        eye_pos = camera_matrix.translation
        look_vec = mathutils.Vector((0, 0, -1))
        look_vec.rotate(camera_matrix.to_3x3())
        up_vec = mathutils.Vector((0, 1, 0))
        up_vec.rotate(camera_matrix.to_3x3())
        return eye_pos, look_vec, up_vec

    def get_props(self):
        camera_props = bpy.context.scene.bitto_camera_props
        return camera_props