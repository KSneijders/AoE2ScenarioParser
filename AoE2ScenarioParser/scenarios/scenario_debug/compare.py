from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Tuple, Any, List, TextIO

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.helper import typename
from AoE2ScenarioParser.helper.printers import s_print
from AoE2ScenarioParser.helper.string_manipulations import add_tabs, q_str, add_suffix_chars
from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever

if TYPE_CHECKING:
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario


def write_difference_to_file(
        file: TextIO,
        path: List[str],
        reason: str,
        difference: Tuple[Any, Any],
        data: Tuple[Any, Any]
) -> None:
    """
    Write a certain difference between 2 scenarios to a file in the format below
    
    Args:
        file: The debug file to write to
        path: The path where the difference occurred
        reason: The difference type (e.g. different values, different types, different list length etc.)
        difference: A tuple containing the compared values
        data: A tuple containing the data values of the compared retrievers
    """
    val0_type, val1_type = typename(data[0]), typename(data[1])
    max_type_len = max(len(val0_type), len(val1_type))

    if isinstance(data[0], list) and isinstance(data[1], list):
        l0, l1 = len(data[0]), len(data[1])
        val0_str = f"{data[0][0:4]}" + (f" ... (4 / {l0})" if l0 - 4 > 0 else "")
        val1_str = f"{data[1][0:4]}" + (f" ... (4 / {l1})" if l1 - 4 > 0 else "")
    else:
        val0_str = q_str(data[0]).replace('\r', '')
        val1_str = q_str(data[1]).replace('\r', '')

    diff = []
    for i in range(0, len(difference)):
        string = q_str(difference[i]).replace('\n', '\\n').replace('\r', '')
        string = (string[:47] + '...') if len(string) > 50 else string

        diff.append(string)

    file.write('\n\n\n' + '\n'.join([
        ' > '.join(path),
        add_tabs(
            '\n'.join([
                f'{reason} ({diff[0]} vs {diff[1]})',
                f'Values:',
                add_tabs('\n'.join([
                    f'{add_suffix_chars(val0_type, " ", max_type_len)} | {val0_str}',
                    f'{add_suffix_chars(val1_type, " ", max_type_len)} | {val1_str}'
                ]), 1)
            ]), 1)
    ]))


def compare_retrievers(
        output_file: TextIO,
        obj1: Retriever | AoE2FileSection,
        obj2: Retriever | AoE2FileSection,
        path: List[str]
) -> None:
    """
    Compare retriever data and the type of said data with the corresponding retriever data of another scenario.
    Recursively checks retrievers when they contain sections otherwise the retriever's data is verified.
    If data is not the same as the other scenario, it'll be logged to a given TextIO object

    Args:
        output_file: The file to write the inconsistencies (differences) to
        obj1: The source Retriever or FileSection to compare
        obj2: The Retriever or FileSection to compare against
        path: The current path inside the Retrievers and FileSections for logging purposes when differences are found.
    """
    path = path.copy()

    # If it's a file section, go through all retrievers in its map
    if isinstance(obj1, AoE2FileSection):
        retr2_keys = list(obj2.retriever_map.keys())

        for retr_key in obj1.retriever_map.keys():
            retriever1 = obj1.retriever_map[retr_key]

            if retr_key in obj2.retriever_map:
                retriever2 = obj2.retriever_map[retr_key]
                compare_retrievers(output_file, retriever1, retriever2, path + [retr_key])

                retr2_keys.remove(retr_key)
            else:
                write_difference_to_file(
                    output_file, path + [retr_key], "TARGET MISSING RETRIEVER",
                    (typename(retriever1.data), None),
                    (retriever1.data, None)
                )

        for retr2_key in retr2_keys:
            retriever2 = obj2.retriever_map[retr2_key]
            write_difference_to_file(
                output_file, path + [retr2_key], "SOURCE MISSING RETRIEVER",
                (None, typename(retriever2.data)),
                (None, retriever2.data)
            )

        return

    # If it's a retriever, check its data and go through it if necessary (when it's a list)
    # Check if the data types are the same
    if typename(obj1.data) != typename(obj2.data):
        write_difference_to_file(
            output_file, path, "DIFFERENT TYPES",
            (typename(obj1.data), typename(obj2.data)),
            (obj1.data, obj2.data)
        )
    # Check if both are lists (is for both because of previous check)
    elif isinstance(obj1.data, list):
        # Check if the lists are equal in size
        if len(obj1.data) != len(obj2.data):
            write_difference_to_file(
                output_file, path, "DIFFERENT LENGTHS",
                (len(obj1.data), len(obj2.data)),
                (obj1.data, obj2.data),
            )
        elif len(obj1.data) > 0:
            # Assuming a list only contains a single data type, compare the first of both lists
            if typename(obj1.data[0]) != typename(obj2.data[0]):
                write_difference_to_file(
                    output_file, path, "DIFFERENT LIST CONTENT TYPES",
                    (typename(obj1.data[0]), typename(obj2.data[0])),
                    (obj1.data, obj2.data),
                )
            # If the list is a list of AoE2FileSection, go through those recursively
            # We can assume type & length are equal due to earlier checks
            elif isinstance(obj1.data[0], AoE2FileSection):
                for i in range(len(obj1.data)):
                    compare_retrievers(output_file, obj1.data[i], obj2.data[i], path + [obj1.name + f"[{i}]"])
            else:
                # Both lists are empty
                for i in range(len(obj1.data)):
                    if obj1.data[i] != obj2.data[i]:
                        write_difference_to_file(
                            output_file, path + [obj1.name + f"[{i}]"], "DIFFERENT LIST DATA VALUE",
                            (obj1.data[i], obj2.data[i]),
                            (obj1.data[i], obj2.data[i]),
                        )
    # If it's not a list, compare the data directly.
    # This SHOULD only be values like: str, int, float or Enum datasets entries etc. (primitives)
    elif obj1.data != obj2.data:
        write_difference_to_file(
            output_file, path, "DIFFERENT VALUES",
            (obj1.data, obj2.data),
            (obj1.data, obj2.data)
        )


def debug_compare(
        scenario: 'AoE2Scenario',
        other: 'AoE2Scenario',
        filename,
        commit: bool = False,
        *,
        allow_multiple_versions: bool=False,
) -> None:
    """
    Compare two scenario files and report the differences found

    Args:
        scenario: The initial scenario
        other: The scenario to compare it to
        filename: The debug file to write the differences to
        commit: If the scenarios need to commit their manager changes before comparing (Defaults to False)
        allow_multiple_versions:
    """
    if commit:
        for scn in scenario, other:
            if hasattr(scn, '_object_manager'):
                scn.commit()

    s_print(f"Searching for differences between scenarios...")
    if not allow_multiple_versions:
        if other.game_version != scenario.game_version or other.scenario_version != scenario.scenario_version:
            raise ValueError("Scenarios must be from the same game & have the same version.")

    with open(filename, 'w', encoding=settings.MAIN_CHARSET) as output_file:
        for section_key in other.sections.keys():
            file_section1 = scenario.sections[section_key]
            file_section2 = other.sections[section_key]
            compare_retrievers(output_file, file_section1, file_section2, [section_key])

    s_print(f"Searching for differences between scenarios finished successfully.", final=True)
    s_print(f"File successfully written to: '{filename}'", color="magenta", final=True)
