import json

from AoE2ScenarioParser.datasets.triggers import ConditionType

# @formatter:off
attr_map = {
    #                      New Name,          Typehint,          Default,          Struct Name
    'unit_object':        ['object',         'InfoDatasetBase',       '-1',               'unit_object'],
    'next_object':        ['other_object',   'InfoDatasetBase',       '-1',               'next_object'],
    'area_x1':            ['area',           'Area',                  'Area((-1, -1))',   'area'],
    'quantity':           ['quantity',       'int',                   '0',                'quantity'],
    'inverted':           ['inverted',       'bool',                  'False',            'inverted'],
    'object_list':        ['player',         'Player | PlayerData',   'Player.ONE',       'object_list'],
    'source_player':      ['object_list',    'InfoDatasetBase',       'False',            'source_player'],
    'object_group':       ['object_group',   'ObjectClass | int',     '-1',               'object_group'],
    'object_type':        ['object_type',    'ObjectType | int',      '-1',               'object_type'],
    'object_state':       ['state',          'ObjectState | int',     '-1',               'object_state'],
    'attribute':          ['attribute',      'PlayerAttribute | int', '0',                'attribute'],
    'technology':         ['technology',     'TechInfo',              '-1',               'technology'],
    'timer':              ['time',           'int',                   '10',               'timer'],
    'ai_signal':          ['ai_signal',      'int',                   '0',                'ai_signal'],
    'variable':           ['variable',       'Variable | int',        '0',                'variable'],
    'comparison':         ['comparison',     'Comparison',            'Comparison.EQUAL', 'comparison'],
    'target_player':      ['target_player',  'Player | PlayerData',   'Player.ONE',       'target_player'],
    'unit_ai_action':     ['ai_action',      'UnitAIAction',          'UnitAIAction.ANY', 'unit_ai_action'],
    'timer_id':           ['timer',          'int',                   '-1',               'timer_id'],
    'victory_timer_type': ['victory_timer',  'VictoryTimerType',      '-1',               'victory_timer_type'],
    'xs_function':        ['xs_function',    'str',                   '\'\'',             'xs_function'],
    'include_changeable_weapon_objects': ['include_changeable', 'bool', 'False', 'include_changeable_weapon_objects'],
}
imports = {
    'InfoDatasetBase':     'from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase',
    'Area':                'from AoE2ScenarioParser.objects.support import Area',
    'Player | PlayerData':   'from AoE2ScenarioParser.datasets.player_data import Player\n'
                           'from AoE2ScenarioParser.objects.data_objects.player.player_data import PlayerData',
    'ObjectClass | int':     'from AoE2ScenarioParser.datasets.trigger_data import ObjectClass',
    'ObjectType | int':      'from AoE2ScenarioParser.datasets.trigger_data import ObjectType',
    'ObjectState | int':     'from AoE2ScenarioParser.datasets.trigger_data import ObjectState',
    'PlayerAttribute | int': 'from AoE2ScenarioParser.datasets.trigger_data import PlayerAttribute',
    'Comparison':          'from AoE2ScenarioParser.datasets.trigger_data import Comparison',
    'UnitAIAction':        'from AoE2ScenarioParser.datasets.trigger_data import UnitAIAction',
    'VictoryTimerType':    'from AoE2ScenarioParser.datasets.trigger_data import VictoryTimerType',
    'TechInfo':            'from AoE2ScenarioParser.datasets.techs import TechInfo',
    'Variable | int':        'from AoE2ScenarioParser.sections.bfp.triggers.variable import Variable',
}
# @formatter:on

with open('./versions/DE/v1.49/conditions.json') as file:
    content: dict = json.load(file)

    for id_, dict_ in content.items():
        if int(id_) < 0:  # or int(id_) > 11:
            continue

        name: str = dict_['name']
        name_camel_case: str = (name + '_condition' if name == 'none' else name).lower()

        class_name: str = ''.join(word.title() for word in name_camel_case.split('_'))
        condition_type: ConditionType = ConditionType[name.upper()]

        attrs = list(filter(lambda x: x != 'condition_type', dict_['attributes']))
        print("-----------------------------------------")
        print(class_name, attrs)

        attributes = args = args_doc = ''
        imports_ = set()
        for attr in attrs:
            if attr in ['area_y1', 'area_x2', 'area_y2']:
                continue

            [new_attr, import_, default_, struct_attr] = attr_map[attr]
            imports_.add(import_)

            attributes += f'''\
    {new_attr}: {import_} = RetrieverRef(ConditionStruct._{struct_attr})  # type ignore
    """_____DESCRIBE_EFFECT_ATTR_{struct_attr.upper()}_HERE_____"""
'''
            args += f'''\
        {new_attr}: {import_} = {default_},
'''

            args_doc += f'''\n\t\t\t{new_attr}: _____DESCRIBE_EFFECT_ATTR_{struct_attr.upper()}_HERE_____'''
        # Prepend newline for nice alignment when no attributes present
        if attributes:
            attributes = '\n' + attributes
            args = "\n\t\t" + args.strip()
            args_doc = "\n\n\t\tArgs:\n\t\t\t" + args_doc.strip()

        import_text = ''
        for import_ in (i for i in imports_ if i in imports):
            import_text += imports[import_] + '\n'

        additional = ''
        if 'Area' in imports_:
            additional += f"""\
        if area:
            area = Area.from_value(area)
        """

        # Prepend newline for nice alignment when no attributes present
        if additional:
            additional = additional.strip() + '\n\n\t\t'

        # Conditional imports
        if len(attrs) == 0:
            initial_imports = f'''\
from AoE2ScenarioParser.datasets.triggers import ConditionType
from AoE2ScenarioParser.objects.data_objects.conditions.condition import Condition'''
        else:
            initial_imports = f'''\
from binary_file_parser import RetrieverRef

from AoE2ScenarioParser.datasets.triggers import ConditionType
from AoE2ScenarioParser.sections.bfp.triggers import ConditionStruct
from AoE2ScenarioParser.objects.data_objects.conditions.condition import Condition'''

        file_content = f'''\
{initial_imports}
{import_text}

class {class_name}(Condition):
    _type_ = ConditionType.{condition_type.name}
{attributes}
    def __init__(
        self,{args}
        **kwargs,
    ):
        """
        _____DESCRIBE_CONDITION_HERE_____{args_doc}
        """
        {additional}super().__init__(local_vars = locals(), **kwargs)
        
'''
        print("-----------------------------------------")
        print(file_content.replace('\t', '    '))

        with open(f'./objects/data_objects/conditions/sub_conditions/{name_camel_case.lower()}.py', 'w') as output_file:
            output_file.write(file_content.replace('\t', '    '))
