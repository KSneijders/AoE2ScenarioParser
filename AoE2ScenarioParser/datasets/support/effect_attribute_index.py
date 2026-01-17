from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class EffectAttributeIndex(_DataSetIntEnums):
    AI_SCRIPT_GOAL = 0
    QUANTITY = 1
    RESOURCE = 2
    DIPLOMACY_STATE = 3
    NUM_UNITS_SELECTED = 4
    LEGACY_SELECTED_OBJECT_REF = 4
    """Before DE, you could only select one unit"""
    LEGACY_LOCATION_OBJECT_REF = 5
    OBJECT_UNIT_ID = 6
    SOURCE_PLAYER = 7
    TARGET_PLAYER = 8
    TECHNOLOGY_ID = 9
    STR_ID = 10
    TIMER = 11
    DISPLAY_TIME = 12
    TRIGGER_ID = 13
    LOCATION_X = 14
    LOCATION_Y = 15
    AREA_X1 = 16
    AREA_Y1 = 17
    AREA_X2 = 18
    AREA_Y2 = 19
    OBJECT_GROUP = 20
    OBJECT_TYPE = 21
    INSTRUCTION_PANEL_POSITION = 22
    ATTACK_STANCE = 23
    TIME_UNIT = 24
    ENABLED = 25
    LEGACY_FOOD = 26
    """Legacy - Previously used in change object/tech cost triggers"""
    LEGACY_WOOD = 27
    """Legacy - Previously used in change object/tech cost triggers"""
    LEGACY_STONE = 28
    """Legacy - Previously used in change object/tech cost triggers"""
    LEGACY_GOLD = 29
    """Legacy - Previously used in change object/tech cost triggers"""
    ITEM_ID = 30
    FLASH_OBJECT = 31
    FORCE_TECHNOLOGY = 32
    VISIBILITY_STATE = 33
    SCROLL = 34
    OPERATION = 35
    OBJECT_UNIT_ID2 = 36
    BUTTON_LOCATION = 37
    AI_SIGNAL_VALUE = 38
    UNUSED1 = 39
    OBJECT_ATTRIBUTES = 40
    VARIABLE = 41
    TIMER_ID = 42
    FACET = 43
    LOCATION_OBJECT_REF = 44
    PLAY_SOUND = 45
    PLAYER_COLOR = 46
    UNUSED2 = 47
    COLOR_MOOD = 48
    RESET_TIMER = 49
    OBJECT_STATE = 50
    ACTION_TYPE = 51
    RESOURCE1 = 52
    RESOURCE1_QUANTITY = 53
    RESOURCE2 = 54
    RESOURCE2_QUANTITY = 55
    RESOURCE3 = 56
    RESOURCE3_QUANTITY = 57
    DECISION_ID = 58
    DECISION_OPTION1_STR_ID = 59
    DECISION_OPTION2_STR_ID = 60
    VARIABLE2 = 61
    MAX_UNITS_AFFECTED = 62
    DISABLE_GARRISON_UNLOAD_SOUND = 63
    HOTKEY = 64
    TRAIN_TIME = 65
    LOCAL_TECHNOLOGY_ID = 66
    DISABLE_SOUND = 67
    OBJECT_GROUP2 = 68
    OBJECT_TYPE2 = 69
    QUANTITY_FLOAT = 70
    FACET2 = 71
    GLOBAL_SOUND = 72
    ISSUE_GROUP_COMMAND = 73
    QUEUE_ACTION = 74
