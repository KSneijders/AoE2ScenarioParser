from src.objects.aoe2_object import AoE2Object


class TriggerObject(AoE2Object):
    def __init__(self,
                 name,
                 description,
                 description_stid,
                 display_as_objective,
                 short_description,
                 short_description_stid,
                 display_on_screen,
                 description_order,
                 enabled,
                 looping,
                 header,
                 mute_objectives,
                 conditions,
                 condition_order,
                 effects,
                 effect_order,
                 ):

        super().__init__(locals())
