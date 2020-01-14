## FileHeaderObject
Object that holds values from file header
- Timestamp
- Scenario Instructions?
- Player Count
- Creator

## DataHeaderObject
Object that holds values from data header
- Player names
- Filename

## PlayerObject
Object that holds Array of players
- Every entry player object
	- All directly player related values (from player tab in game)

## MessagesObject
Object that holds all values from messages tab in game

## DiplomacyObject
Object that holds array of players
- Every entry player_diplomacy object
	- All diplomacy related values (diplo stance & allied victory)

## OptionsObject
Object that holds all values from options tab in game

## MapObject
Object that holds all values map related
- Array of tiles 2D
  - Terrain ID
  - Elevation
- Map mood
- Collide and Correct
- width & height

## UnitObject
Object that holds all units
	Array of players
		Every entry is an array of units from that player

## TriggerObject
Object that holds all trigger related values
- Number of triggers
- Array of triggers
- Trigger display order
