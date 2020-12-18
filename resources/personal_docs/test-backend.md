# Currently:

- Values are read in order of the file.
- Values are put back after editing in reverse order
- `Pieces [-> Structs] -> Retriever`
  - Pieces
    - Top layer of the file: FileHeader, Map, Triggers etc.
    - List of retrievers possibly with structs
  - Struct
    - List of retrievers possibly with structs.
    - Used for repition of retrievers
  - Retriever:
    - Name
    - Datatype
      - Unsigned Int    (u)
      - Signed Int      (i)
      - Static String   (c)
      - Variable String (str)
      - Plain bytes     ()
      - Struct          (Struct Object)
    - 3 Events
      - on_construct: Fires when file is read & constructed. 
      - on_commit: Fires when objects are translated back to retrievers
      - on_refresh: When a refresh command is received
        - Other events can emit a refresh command for other retrievers. For example: When the triggers are put back, three refresh commands will be send. All three times to a number_of_trigger retriever, which appears three times in the file.
      - Events can be used to send repeat commands or to set the current value or the current repeat value. This can be done to define target(s) and an eval string to execute the code.
        - Example: 
```py
- "trigger_data": {
    "on_refresh": RetrieverDependency(
        DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_triggers")
    ),
    "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
    "on_commit": RetrieverDependency(
        DependencyAction.REFRESH, DependencyTarget(
            [
                "self",
                "FileHeaderPiece",
                "OptionsPiece",
            ], [
                "number_of_triggers",
                "trigger_count",
                "number_of_triggers",
            ]
        )
    )
},
"trigger_display_order_array": {
    "on_refresh": RetrieverDependency(
        DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_triggers")
    ),
    "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
},
```
