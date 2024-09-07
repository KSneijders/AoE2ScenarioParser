from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class Hotkey(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the blast level values used in the game. Used in the
    'Modify Attribute' effect with the 'HotKey ID' attribute

    Many hotkeys are missing from this file (Like arrow up). The reason for this is explained in the UGC guide:
    https://divy1211.github.io/AoE2DE_UGC_Guide/general/hotkeys/hotkeys/

    **Examples**

    >>> Hotkey.SPACE
    <Hotkey.SPACE: 10101>
    """
    SPACE = 10101
    PAGE_UP = 15000
    LEFT_ARROW = 2312
    RIGHT_ARROW = 19707
    DOWN_ARROW = 19731
    INSERT = 9025
    DELETE = 19602
    ZERO = 99
    ONE = 98
    TWO = 10360
    THREE = 9786
    FOUR = 10362
    FIVE = 9785
    SIX = 213
    SEVEN = 8828
    EIGHT = 9448
    NINE = 9783
    A = 1001
    B = 1005
    C = 1201
    D = 1151
    E = 1007
    F = 4137
    G = 2012
    H = 2407
    I = 1212
    J = 1222
    K = 4141
    L = 1101
    M = 1006
    N = 3001
    O = 214
    P = 1210
    Q = 4169
    R = 1200
    S = 1102
    T = 2016
    U = 1205
    V = 1150
    W = 1008
    X = 1002
    Y = 2008
    Z = 4174
    APPLICATION = 19704
    NUM_ZERO = 19721
    NUM_ONE = 4563
    NUM_FOUR = 19499
    NUM_FIVE = 5558
    NUM_SEVEN = 10069
    NUM_EIGHT = 1011
    NUM_DELETE = 20123
    F3 = 9798
    F4 = 22019
    F7 = 9840
    F8 = 1152
    F15 = 10661
