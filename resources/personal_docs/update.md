# States:
- on_construct
- on_commit
- on_update (When data has changed)
- on_refresh (When refresh request came in)

# Actions:
- refresh:
  - SUB->targetor
- set_repeat:
  - retrieve:
    - SUB->targetor
    - SUB->eval
- set_value:
  - retrieve:
    - SUB->targetor
    - SUB->eval

## Sub items:
- targetor
  - target_piece: str (piece_name or "self" (own list))
  - piece_attr_name: str
- eval
  - eval_code: str
  - eval_locals: dict
