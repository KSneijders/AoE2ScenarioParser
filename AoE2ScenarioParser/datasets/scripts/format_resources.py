uncapped = [
    'if', 'a', 'is', 'by', 'of', 'the', 'to', 'per', 'in', 'an', 'for', 'and', 'from','does', 'not', 'also', 'have',
    'this', 'set', 'will'
]

with open('../../../resources/personal_docs/ResourceAttributeDescriptionsV1.3.3.md', 'r') as file:
    state = 0
    state_lines = []
    file = file.read()
    for index, line in enumerate(file.splitlines()):
        if line.strip() == '' or line[0] == '`':
            if state == 1:
                # Add colon if first word is 'unknown' or 'boolean'
                words = state_lines[0].split(' ')
                if words[0].lower() in ['boolean', 'unknown', 'unused']:
                    words[0] = words[0] + ':'
                    state_lines[0] = ' '.join(words)
                if len(state_lines) > 1:  # Combine gathered list
                    if state_lines[0][-1] == ".":
                        state_lines[0] = state_lines[0][:-1]
                    state_lines[0] += ":"
                    state_lines.insert(1, "")
                    print('\n'.join(["\"\"\""] + state_lines + ["\"\"\""]))
                else:  # Print single desc line
                    print("\"\"\"" + state_lines[0] + "\"\"\"")
                state_lines = []
                state = 0
            if line.strip() == '':
                break

            # `-------- Building Limit = 30;`
            # BUILDING_LIMIT = 30
            if line[-2:] == ';`':
                line = line[:-2]
            elif line[-1] == '`':
                line = line[:-1]
                print(line)
                print(index)
                exit()
            splitted = line[1:].split(' = ')
            splitted[0] = splitted[0].replace('--------', '').replace('========', '').replace('~~~~~~~~', '')
            splitted[0] = splitted[0].replace('/', ' or ')
            splitted[0] = splitted[0].replace('(', ' ').replace(')', ' ').replace('  ', ' ').strip()
            if splitted[0][:6].lower() == 'unused':
                splitted[0] = f"UNUSED_RESOURCE_{splitted[1].zfill(3)}"
            print(f"{splitted[0].replace(' ', '_').upper()} = {splitted[1]}")
        elif line.strip()[0] == '<':
            state = 1

            # <BOOLEAN_ALLOW_ENEMY_BUILDING_CONVERSIONS by the source player.>
            # Boolean Allow Enemy Building Conversions by the Source Player:
            replaced_line = line.replace('_', ' ')
            edited_line = replaced_line.strip()[1:-1].split(' ')
            capitalized_line = ' '.join(
                [item.lower() if item.lower() in uncapped else item.capitalize() for item in edited_line]
            )
            state_lines.append(capitalized_line)
        elif line.strip()[:2] == '**':
            state = 1

            # **0: when all techs not researched**
            #     0: When All Techs Not Researched
            replaced_line = line.strip()[:-2].replace('**', '- ')
            state_lines.append(' '.join(
                [item.lower() if item.lower() in uncapped else item.capitalize() for item in replaced_line.split(' ')]
            ))
