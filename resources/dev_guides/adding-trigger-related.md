### What to do when you want to add a new effect (same goes for Condition):

1. Add the effect to the `EffectId` dataset.
2. Add the effect to the `NewEffectSupport` object.
3. Add the effect to the `effects.json` in the version folder.

### What to do when you want to add a new effect attribute (same goes for Condition):

1. Add the attribute to the `default_attributes` for the `None` effect in the `effects.json` in the version folder.
2. Add the attribute to the `default_attributes` for effects that are different from `None` in the `effects.json` in the version folder.
3. Add the attribute to all effects `attributes` list that use the attribute. 
4. Increase the `static_value` default in the effects structure in the `structure.json`.
5. Add the attribute to the `empty_attributes` dict in `effects.py`.
6. Add the attribute to all effects that use it in the `EffectId` docs (`effects.py`).
7. Add the attribute to the proper functions in the `NewEffectSupport` object.
8. Add the attribute to `RetrieverObjectLink` list in the `Effect` data object (Include proper version parameter).
9. Add the attribute to the `Effect` data object constructor parameters and the `self.x` assignment.

### What to do when you want to add an existing attribute to an effect (same goes for Condition):

1. Add the attribute to the effect's `default_attributes` in the `effects.json` in the version folder.
2. Add the attribute to the effect's `attributes` list that use the attribute.
3. Add the attribute to the effect's that use it in the `EffectId` docs (`effects.py`).
4. Add the attribute to the proper functions in the `NewEffectSupport` object.
