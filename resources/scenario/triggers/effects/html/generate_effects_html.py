import json
from pathlib import Path

json_path = Path(__file__).parent.parent / "effect-definitions-complete.json"
out_path = Path(__file__).parent / "effect-definitions.html"

with open(json_path, encoding="utf-8") as f:
    effects = json.load(f)


def desc(value):
    if isinstance(value, list):
        return " ".join(value)
    return value or ""


rows = []
for effect in effects:
    effect_id = effect["id"]
    name = effect["name"]
    description = desc(effect.get("description", ""))
    attributes = effect.get("attributes", [])

    attr_rows = ""
    for attr in attributes:
        attr_name = attr.get("name", "")
        attr_type = attr.get("type", "")
        attr_desc = desc(attr.get("description", ""))
        attr_default = attr.get("default")
        default_str = f'<span class="default">default: {attr_default}</span>' if attr_default is not None else ""
        attr_rows += f"""
        <div class="attr-row">
          <span class="attr-name">{attr_name}</span>
          <span class="attr-type">{attr_type}</span>
          <span class="attr-desc">{attr_desc} {default_str}</span>
        </div>"""

    attrs_html = f'<div class="attrs">{attr_rows}</div>' if attr_rows else '<div class="attrs empty">no attributes</div>'

    rows.append(f"""
  <div class="effect-row">
    <div class="effect-header">
      <span class="effect-id">{effect_id}</span>
      <span class="effect-name">{name}</span>
      <span class="effect-desc">{description}</span>
    </div>
    {attrs_html}
  </div>""")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Effect Definitions</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: system-ui, sans-serif; font-size: 14px; background: #1a1a1a; color: #ccc; padding: 24px; }}
    h1 {{ margin-bottom: 16px; font-size: 20px; color: #eee; }}

    .effect-row {{
      background: #242424;
      border: 1px solid #333;
      border-radius: 6px;
      margin-bottom: 8px;
      overflow: hidden;
    }}

    .effect-header {{
      display: grid;
      grid-template-columns: 36px 260px 1fr;
      gap: 12px;
      align-items: baseline;
      padding: 8px 12px;
      background: #2c2c2c;
      border-bottom: 1px solid #333;
    }}

    .effect-id {{
      font-weight: 600;
      color: #666;
      text-align: right;
    }}

    .effect-name {{
      font-weight: 600;
      font-family: monospace;
      font-size: 13px;
      color: #7aadff;
    }}

    .effect-desc {{
      color: #aaa;
      font-size: 13px;
    }}

    .attrs {{ padding: 4px 12px 6px 12px; }}
    .attrs.empty {{ color: #555; font-style: italic; padding: 6px 48px; }}

    .attr-row {{
      display: grid;
      grid-template-columns: 220px 120px 1fr;
      gap: 12px;
      align-items: baseline;
      padding: 3px 0;
      border-bottom: 1px solid #2e2e2e;
      font-size: 13px;
    }}
    .attr-row:last-child {{ border-bottom: none; }}

    .attr-name {{
      font-family: monospace;
      padding-left: 36px;
      color: #888;
    }}

    .attr-type {{
      color: #5a9a6e;
      font-size: 12px;
    }}

    .attr-desc {{ color: #bbb; }}

    .default {{
      color: #666;
      font-size: 11px;
      margin-left: 6px;
    }}
  </style>
</head>
<body>
  <h1>Effect Definitions ({len(effects)} effects)</h1>
{"".join(rows)}
</body>
</html>
"""

out_path.write_text(html, encoding="utf-8")
print(f"Written to {out_path}")
