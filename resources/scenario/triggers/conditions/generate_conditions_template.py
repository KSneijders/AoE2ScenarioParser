import json
from pathlib import Path

from definitions import AttributeDefinition, ConditionDefinition

conditions_json = (Path(__file__).parent.parent.parent.parent.parent
                   / 'AoE2ScenarioParser' / 'versions' / 'DE' / 'v1.57' / 'conditions.json')

COMPLETE_PROGRESS = -1
"""Until which ID have the descriptions, refs and defaults been filled."""

condition_attribute_descriptions_file = (Path(__file__).parent / 'condition-attributes.json')
with condition_attribute_descriptions_file.open('r') as f:
    condition_attribute_descriptions: dict[str, str] = json.load(f)

complete_file_path = Path(__file__).parent / 'condition-definitions-complete.json'
with complete_file_path.open('r') as f:
    complete_file_current: list[ConditionDefinition] = json.load(f)

result: list[ConditionDefinition] = []
with conditions_json.open('r') as f:
    legacy_condition_definitions: dict[str, dict] = json.load(f)

    base_types: dict[str, str] = dict(legacy_condition_definitions['-1']['attribute_presentation'])
    base_types['area'] = 'Area'
    base_types['quantity'] = 'int'
    base_types['timer'] = 'int'  # still used as 'before' key in replacements lookup
    base_types['trigger_id'] = 'int'
    base_types['ai_signal'] = 'int'
    base_types['timer_id'] = 'int'
    base_types['decision_id'] = 'int'

    for condition_id, condition_definition in legacy_condition_definitions.items():
        if condition_id == '-1':
            continue

        matched_condition = next(
            (c for c in complete_file_current if c['id'] == int(condition_id)), None
        )
        is_completed_condition = int(condition_id) <= COMPLETE_PROGRESS

        local_types = dict(base_types)
        if 'attribute_presentation' in condition_definition:
            local_types.update(condition_definition['attribute_presentation'])

        attributes_list: list[str] = list(condition_definition['attributes'])
        if 'condition_type' in attributes_list:
            attributes_list.remove('condition_type')

        replacements = {
            'attribute':                         'resource',
            'unit_object':                       'primary_unit_ref',
            'next_object':                       'secondary_unit_ref',
            'object_list':                       'object_id',
            'unit_ai_action':                    'unit_action',
            'technology':                        'technology_id',
            'area_x1':                           'area',
            'area_y1':                           None,
            'area_x2':                           None,
            'area_y2':                           None,
            'timer':                             'timer_seconds',
            'variable':                          'variable1_id',
            'object_state':                      'unit_state',
            'include_changeable_weapon_objects': 'include_transformable_units',
            'variable2':                         'variable2_id',
            'local_technology':                  'local_technology_id',
        }

        attributes: dict[str, str | None] = {attr: attr for attr in attributes_list}
        for before, after in replacements.items():
            if before in attributes:
                attributes[before] = after

        default_attributes: dict = condition_definition.get('default_attributes', {})

        attr_definitions: list[AttributeDefinition] = [
            AttributeDefinition(
                name=after,
                ref=(
                    next(
                        (a['ref'] for a in matched_condition['attributes'] if a['name'] == after),
                        None,
                    )
                    if is_completed_condition and matched_condition
                    else None
                ),
                type=local_types.get(before) or local_types.get(after) or '------ UNKNOWN TYPE ------',

                description=(
                    next(
                        (a['description'] for a in matched_condition['attributes'] if a['name'] == after),
                        None,
                    )
                    if is_completed_condition and matched_condition
                    else condition_attribute_descriptions.get(before) or condition_attribute_descriptions.get(after)
                ),

                default=(
                    next(
                        (a['default'] for a in matched_condition['attributes'] if a['name'] == after),
                        None,
                    )
                    if is_completed_condition and matched_condition
                    else None
                ),
            )
            for before, after in attributes.items()
            if after is not None
        ]

        if is_completed_condition and matched_condition:
            condition_description = matched_condition['description']
        else:
            condition_description = '----- DESCRIPTION TO BE FILLED -----'

        result.append(
            ConditionDefinition(
                id=int(condition_id),
                name=condition_definition['name'],
                description=condition_description,
                attributes=attr_definitions,
            )
        )

complete_file = Path(__file__).parent / 'condition-definitions-complete.json'
with complete_file.open('w') as f:
    f.write(json.dumps(result, indent=2))
