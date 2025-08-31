from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32, NtStr, u32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class AiError(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    file_name: str   = Retriever(NtStr[260], default = "")
    line_number: int = Retriever(i32,        default = -1)
    message: str     = Retriever(NtStr[128], default = "")
    code: str        = Retriever(u32,        default = 0)
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
