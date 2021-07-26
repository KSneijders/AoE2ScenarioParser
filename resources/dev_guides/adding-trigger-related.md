### What to do when you want to add a new effect (same goes for Condition):

1. Add the effect to the `EffectId` dataset.
2. Add the effect to the `NewEffectSupport` object.
3. Add the effect to the `effects.json` in the version folder.

### What to do when you want to add a new effect attribute (same goes for Condition):

1. Add the attribute to all effects `default_attributes` in the `effects.json` in the version folder.
2. Add the attribute to all effects `attributes` list that use the attribute. 
3. Increase the `static_value` default in the effects structure in the `structure.json`.
3. Add the attribute to the `empty_attributes` dict in `effects.py`.
4. Add the attribute to all effects that use it in the `EffectId` docs (`effects.py`).
2. Add the attribute to the `_add_effect` function's parameters in `trigger.py` data object.
3. Add the attribute to the proper functions in the `NewEffectSupport` object.
4. Add the attribute to `RetrieverObjectLink` list in the `Effect` data object (Include proper version parameter).
5. Add the attribute to the `Effect` data object constructor parameters and the `self.x` assignment.