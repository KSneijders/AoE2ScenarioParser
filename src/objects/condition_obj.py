from src.objects.aoe2_object import AoE2Object


class ConditionObject(AoE2Object):
    def __init__(self,
                 cond_type,
                 amount,
                 resource_type,
                 unit_object,
                 next_object,
                 object_list,
                 source_player,
                 tech,
                 timer,
                 area_x1,
                 area_y1,
                 area_x2,
                 area_y2,
                 object_group,
                 object_type,
                 ai_signal,
                 inverted,
                 variable,
                 comparison,
                 target_player
                 ):

        super().__init__(locals())
