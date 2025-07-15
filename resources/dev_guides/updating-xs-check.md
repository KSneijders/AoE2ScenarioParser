### Updating XS-Check dependency

1. Download the new `xs-check` and `xs-check.exe` from GitHub and replace the binaries:
   - https://github.com/Divy1211/xs-check/releases/latest
2. Within `AoE2ScenarioParser/objects/support/xs_check.py`:
    1. Update the `version` attribute to the newest version
    2. Update the `is_supported_xs_check_binary()` function to support the newest version

