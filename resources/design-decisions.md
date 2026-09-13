# Design Decisions

A running log of design decisions for the library and short notes on how things should
behave.

---

## Linking objects across scenarios

An object is "linked" once it belongs to a scenario. Any non-import function that
receives an object linked to a *different* scenario should error. Import functions are
the exception and are the way to bring in externally linked objects. Add operations link
up any unlinked objects they receive.

This applies to units, triggers, effects, and conditions.

---

## Materializing IDs on link

Unlinked triggers and objects may reference other unlinked triggers and objects. IDs are
materialized at link time: until then reference-derived fields (e.g. `trigger_id`) 
are not yet valid. Inserting one item into a scenario links the whole referenced chain.

So triggers, with activation, or units with garrisoned units will all be linked if any
of them are added.

---

## Removing references in replace functions

Replace functions take a `remove_external_references` argument. When `True` (default),
external references are stripped. This means unit references are removed from triggers
and vice versa. When `False`, references are resolved to their plain IDs
and the objects are left unlinked, so you must call the linking function yourself
afterwards. This allows importing triggers and units and linking them back up later.
