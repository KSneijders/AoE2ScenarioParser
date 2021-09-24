from enum import IntEnum


class GroupBy(IntEnum):
    """
    Enum used to select what way the triggers should be grouped when using the function 'copy_trigger_tree_per_player'.
    Each mode has it's own explanation explained in the corresponding docstring.
    """
    NONE = -1
    """
    Don't group triggers. Add triggers to the end of the list. This could mean the source triggers aren't near the 
    copies. All copies, however, will be grouped like the TRIGGER grouping mechanism - at the end of the list.
    """
    TRIGGER = 0
    """
    Group triggers by trigger. All copies of a trigger will be put directly below the 'source' trigger. 
    Example: If the 'source' trigger has display_index of 3, and another trigger in it's tree has 5. Assuming the 
    triggers were copied for all players, display indexes of the copies from the first trigger would be 4-10. The second
    trigger in the tree would be bumped up to 12 (from 5) and it's copies would use: 13-19. 
    
    Orders the given trigger on top with the child triggers after. Child triggers are ordered in the order they were
    found in (Depth-first).
    """
    PLAYER = 1
    """
    Group triggers by player. Warning: This mode could change some of the intended order of the triggers. All copies of
    the trigger will be put together sorted on player first, then trigger order. 
    Example: If the 'source' trigger has display_index of 3, and another trigger in it's tree has 5. Assuming the 
    triggers were copied for all players, display indexes of the copies from the firs trigger would be: 5, 7, 9, 11, 13,
    15 and 17. The second trigger would have moved to 4 (from 5) and it's copies would occupy slots: 6, 8, 10, 12, 14, 
    16 and 18. This way both PlayerId.ONE (assuming that's the source player) triggers will be together, same goes for 
    all other players. 
    
    In the example above can be seen how the second trigger was moved from 5 to 4. The unrelated trigger in between was
    moved to the end, 19. This might be an unwanted side effect, be aware.
    """
