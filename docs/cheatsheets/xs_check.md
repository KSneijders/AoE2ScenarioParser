# XS-CHECK

Support for XS has been greatly improved by the library: [XS-Check](https://github.com/Divy1211/xs-check) made by Alian.

When calling `scenario.write_to_file(...)` all XS that is present in the scenario is combined and sent to the XS-Check 
library. After XS-Check has completed its validation steps the output is analyzed and shown back in the console.

By default, the writing process of AoE2ScenarioParser is **not** interrupted, even if an error is found in the XS code.


!!! warning "Only XS from Effects and Conditions is combined"
    Due to the import logic of XS scripts from many different locations depending on the installation
    location of AoE2:DE, the XS script file that is referenced by filename in the `XsManager` is NOT
    added to the XS-Check library! Scripts added through `xs_manager.add_script(...)` and all other 
    xs from effects and conditions is combined.

## Configurations

There are some configuration options for XS Check in AoE2ScenarioParser. Below you can find the most useful ones.
For more configuration options and more info, see the [XS-Check API docs](../api_docs/xs/xs_check.md).

### Enabling / Disabling

Disabling XS Check is very simple, you can do so using: 

```py
scenario.xs_manager.xs_check.enabled = False
```

### Raise on error

If you want an exception to be raised when errors are found in your XS file, you can change the following setting:

```py
scenario.xs_manager.xs_check.raise_on_error = True
```

### Timeout

The default timeout for XS Check is 60 seconds. This should be WAY more than most will ever need, but just in case
your XS Check call takes longer than that. You can adjust it using:

```py
scenario.xs_manager.xs_check.timeout_seconds = 120
```

### Using an alternative binary

If you want to use different binaries than the ones that are shipped with AoE2ScenarioParser, you can set the path
to a different binary on your system. You can do so by using:

```py
scenario.xs_manager.xs_check.path = "your/path/to/a/binary"
```

If the binary is of a version that is not technically supported by AoE2ScenarioParser it'll show an error. If you
want to try the unsupported binary anyway, you can also add the following:

```py
scenario.xs_manager.allow_unsupported_versions = True
```

## Example

Below is an example of a trigger with a Script Call Effect with some invalid XS with the output that will be printed.

```py
scenario = AoE2DEScenario.from_file(...)
trigger_manager = scenario.trigger_manager

trigger = trigger_manager.add_trigger('My Trigger With XS')

trigger.new_effect.script_call(
    message='void func () {'
            '    int a = 3;'
            '    int b = 4;'
            '    return "";'
            '}'
)

scenario.write_to_file(...)
```

```
-------------------------<[ XS-CHECK VALIDATION RESULT ]>-------------------------

xs-check:0.2.1 output: [ Provided by: https://github.com/Divy1211/xs-check/ ]

	[06] Error: SyntaxError
	   ╭─[AoE2ScenarioParser.xs:1:56]
	   │
	 1 │ /*T0E0*/ void func () {    int a = 3;    int b = 4;    return "";}
	   │                                                        ─────┬────  
	   │                                                             ╰────── This function's return type was declared as void
	───╯
	Finished analysing file 'AoE2ScenarioParser.xs'.


XS-Check errors origins:

  ⇒ [Trigger #0] 'My Trigger With XS'
     ↳ [Effect #0] Script Call Effect


Open the file below to view the entire XS file:
	file:///C:/Users/.../AppData/Local/Temp/tmp_3bgcg8p.xs

-------------------------<[ END XS-CHECK VALIDATION RESULT ]>-------------------------
```