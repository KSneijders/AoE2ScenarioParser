import json
from pathlib import Path

from definitions import EffectDefinition, LegacyEffectDefinition
from resources.scenario.triggers.effects.definitions import AttributeDefinition

effects_json = (Path(__file__).parent.parent.parent.parent.parent
                / 'AoE2ScenarioParser' / 'versions' / 'DE' / 'v1.56' / 'effects.json')

COMPLETE_PROGRESS = 11
"""Until which ID have the descriptions, refs and defaults been filled."""

effect_attribute_descriptions_file = (Path(__file__).parent / 'effect-attributes.json')
with effect_attribute_descriptions_file.open('r') as f:
    effect_attribute_descriptions: dict[str, str] = json.load(f)

complete_file_path = Path(__file__).parent / 'effect-definitions-complete.json'
with complete_file_path.open('r') as f:
    complete_file_current: list[EffectDefinition] = json.load(f)

result: list[EffectDefinition] = []
with effects_json.open('r') as f:
    legacy_effect_definition: dict[str, LegacyEffectDefinition] = json.load(f)

    for effect_id, effect_definition in legacy_effect_definition.items():
        if effect_id == '-1':  # Skip representation
            continue

        matched_effect = next((effect for effect in complete_file_current if effect['id'] == int(effect_id)), None)
        is_completed_effect = int(effect_id) <= COMPLETE_PROGRESS

        # noinspection PyTypedDict
        types: dict[str, str] = legacy_effect_definition['-1']['attribute_presentation']
        types['area'] = 'Area'
        types['location'] = 'Tile'
        types['string_id'] = 'int'
        types['quantity'] = 'int'
        types['armour_attack_quantity'] = 'int'
        types['ai_script_goal'] = 'int'
        types['item_id'] = 'int'
        types['facet'] = 'int'
        types['facet2'] = 'int'
        types['ai_signal_value'] = 'int'
        types['display_time'] = 'int'
        types['timer'] = 'int'
        types['resource1_quantity'] = 'int'
        types['resource2_quantity'] = 'int'
        types['resource3_quantity'] = 'int'
        types['max_units_affected'] = 'int'
        types['decision_id'] = 'int'
        types['string_id_option1'] = 'int'
        types['string_id_option2'] = 'int'
        types['train_time'] = 'int'
        types['hotkey'] = 'int'
        types['quantity_float'] = 'float'
        types['message_option1'] = 'str'
        types['message_option2'] = 'str'
        types['trigger_id'] = 'Trigger'

        for key, value in types.items():
            if value.endswith('[]'):
                value = f"list[{value[:-2]}]"
                types[key] = value

        attributes_list = effect_definition['attributes']
        if 'effect_type' in attributes_list:
            attributes_list.remove('effect_type')

        attributes: dict[str, str | None] = {attr: attr for attr in attributes_list}

        replacements = {
            'location_x':                'location',
            'location_y':                None,
            'area_x1':                   'area',
            'area_y1':                   None,
            'area_x2':                   None,
            'area_y2':                   None,
            'selected_object_ids':       'selected_objects',
            'trigger_id':                'trigger',
            'tribute_list':              'resource',
            'diplomacy':                 'diplomacy_state',
            'number_of_units_selected':  'num_units_selected',
            'object_list_unit_id':       'object_unit_id',
            'technology':                'technology_id',
            'string_id':                 'str_id',
            'unknown_2':                 'timer',
            'food':                      'legacy_food',
            'wood':                      'legacy_wood',
            'stone':                     'legacy_stone',
            'gold':                      'legacy_gold',
            'force_research_technology': 'force_technology',
            'object_list_unit_id_2':     'object_unit_id2',
            'unknown_3':                 'unused1',
            'timer':                     'timer_id',
            'location_object_reference': 'location_object_ref',
            'unknown_4':                 'unused2',
            'string_id_option1':         'decision_option1_str_id',
            'string_id_option2':         'decision_option2_str_id',
            'local_technology':          'local_technology_id',
            'resource_1':                'resource1',
            'resource_1_quantity':       'resource1_quantity',
            'resource_2':                'resource2',
            'resource_2_quantity':       'resource2_quantity',
            'resource_3':                'resource3',
            'resource_3_quantity':       'resource3_quantity',
        }

        for before, after in replacements.items():
            if before in attributes:
                attributes[before] = after

        attr_definitions = [
            AttributeDefinition(
                name = after,
                ref = next(
                    (attribute['ref'] for attribute in matched_effect['attributes'] if attribute['name'] == after), None
                ) if is_completed_effect else None,
                type = types.get(before) or types.get(after) or '------ UNKNOWN TYPE ------',

                description = next(
                    (attribute['description'] for attribute in matched_effect['attributes'] if attribute['name'] == after), None
                )
                if is_completed_effect
                else effect_attribute_descriptions.get(before) or effect_attribute_descriptions.get(after),

                default = next(
                    (attribute['default'] for attribute in matched_effect['attributes'] if attribute['name'] == after), None
                )
                if is_completed_effect
                else None,
            ) for before, after in attributes.items() if after is not None
        ]

        if is_completed_effect:
            effect_description = matched_effect['description']
        else:
            effect_description = '----- DESCRIPTION TO BE FILLED -----'

        result.append(
            EffectDefinition(
                id = int(effect_id),
                name = effect_definition['name'],
                description = effect_description,
                attributes = attr_definitions
            )
        )

complete_file = Path(__file__).parent / 'effect-definitions-complete.json'
with complete_file.open('w') as f:
    f.write(json.dumps(result, indent = 2))
