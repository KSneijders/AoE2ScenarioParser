from src.objects.aoe2_object import AoE2Object


class ConditionObject(AoE2Object):
    def __init__(self,
                 condition_type,
                 amount_or_quantity,
                 resource_type_or_tribute_list,
                 unit_object,
                 next_object,
                 object_list,
                 player,
                 technology,
                 timer,
                 area_1_x,
                 area_1_y,
                 area_2_x,
                 area_2_y,
                 object_group,
                 object_type,
                 ai_signal,
                 inverted,
                 variable,
                 comparison,
                 target_player
                 ):

        super().__init__(locals())
