from __future__ import annotations

from bfp_rs import BaseStruct, ret, Retriever, RetrieverCombiner, Version
from bfp_rs.combinators import set_
from bfp_rs.types.le import Array, i32


def sync_num_techs():
    return [
        set_(ret(LegacyDisables._num_disabled_techs), i).from_len(ret(LegacyDisables._disabled_tech_ids), i)
        for i in range(16)
    ]


def sync_num_units():
    return [
        set_(ret(LegacyDisables._num_disabled_units), i).from_len(ret(LegacyDisables.disabled_unit_ids), i)
        for i in range(16)
    ]


def sync_num_disabled_buildings_old():
    return [
        set_(ret(LegacyDisables._num_disabled_buildings_old), i)
        .from_len(ret(LegacyDisables._disabled_building_ids_old), i)
        for i in range(16)
    ]


def sync_num_disabled_buildings():
    return [
        set_(ret(LegacyDisables._num_disabled_buildings), i)
        .from_len(ret(LegacyDisables._disabled_building_ids), i)
        for i in range(16)
    ]


class LegacyDisables(BaseStruct):
    # @formatter:off
    _disabled_tech_ids_old: list[list[int]]     = Retriever(Array[16][Array[20][i32]], min_ver = Version(1,  4), max_ver = Version(1, 17), default_factory = lambda _ver: [[-1]*20 for _ in range(16)])
    _num_disabled_techs: list[int]              = Retriever(Array[16][i32],            min_ver = Version(1, 18),                           default_factory = lambda _ver: [0]*16,                       on_write = sync_num_techs)
    _disabled_tech_ids: list[list[int]]         = Retriever(Array[16][Array[30][i32]], min_ver = Version(1, 18),                           default_factory = lambda _ver: [[-1]*30 for _ in range(16)])

    _num_disabled_units: list[int]              = Retriever(Array[16][i32],            min_ver = Version(1, 18),                           default_factory = lambda _ver: [0]*16,                       on_write = sync_num_units)
    disabled_unit_ids: list[list[int]]          = Retriever(Array[16][Array[30][i32]], min_ver = Version(1, 18),                           default_factory = lambda _ver: [[-1]*30 for _ in range(16)])

    _num_disabled_buildings_old: list[int]      = Retriever(Array[16][i32],            min_ver = Version(1, 18), max_ver = Version(1, 24), default_factory = lambda _ver: [0]*16,                       on_write = sync_num_disabled_buildings_old)
    _num_disabled_buildings: list[int]          = Retriever(Array[16][i32],            min_ver = Version(1, 25),                           default_factory = lambda _ver: [0]*16,                       on_write = sync_num_disabled_buildings)
    _disabled_building_ids_old: list[list[int]] = Retriever(Array[16][Array[20][i32]], min_ver = Version(1, 18), max_ver = Version(1, 24), default_factory = lambda _ver: [[-1]*20 for _ in range(16)])
    _disabled_building_ids: list[list[int]]     = Retriever(Array[16][Array[30][i32]], min_ver = Version(1, 25),                           default_factory = lambda _ver: [[-1]*30 for _ in range(16)])

    # references
    disabled_tech_ids: list[list[int]]          = RetrieverCombiner(ret(_disabled_tech_ids_old),     ret(_disabled_tech_ids))
    disabled_building_ids: list[list[int]]      = RetrieverCombiner(ret(_disabled_building_ids_old), ret(_disabled_building_ids))
    # @formatter:on

    def __new__(cls, ver: Version = Version(1, 27), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
