from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import FixedLenNTStr, int32, uint32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class AiError(BaseStruct):
    # @formatter:off
    file_name: str   = Retriever(FixedLenNTStr[260], default = "")
    line_number: int = Retriever(int32,              default = -1)
    message: str     = Retriever(FixedLenNTStr[128], default = -1)
    code: str        = Retriever(uint32,             default = 0)
    """
    - 0: ConstantAlreadyDefined
    - 1: FileOpenFailed
    - 2: FileReadFailed
    - 3: InvalidIdentifier
    - 4: InvalidKeyword
    - 5: InvalidPreprocessorDirective
    - 6: ListFull
    - 7: MissingArrow
    - 8: MissingClosingParenthesis
    - 9: MissingClosingQuote
    - 10: MissingEndIf
    - 11: MissingFileName
    - 12: MissingIdentifier
    - 13: MissingKeyword
    - 14: MissingLHS
    - 15: MissingOpeningParenthesis
    - 16: MissingPreprocessorSymbol
    - 17: MissingRHS
    - 18: NoRules
    - 19: PreprocessorNestingTooDeep
    - 20: RuleTooLong
    - 21: StringTableFull
    - 22: UndocumentedError
    - 23: UnexpectedElse
    - 24: UnexpectedEndIf
    - 25: UnexpectedError
    - 26: UnexpectedEOF
    """
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
