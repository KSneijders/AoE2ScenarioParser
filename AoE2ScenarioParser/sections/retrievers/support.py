from __future__ import annotations

default_since = 0
default_until = 100


class Support:
    """
    Object to check for version support.
    """

    # Note to self: \n
    # As long as versions are always 4 chars long, this system works.
    # If they could define the first (or second) 2.x version as: 2.1 and 9 later as: 2.10, this would break.
    # The version is always 4 in length, I assume they'd write it as: '2.01' and not '2.1 ' to fill the 4 chars.

    # If they do write is as '2.1 ', I'd have to compare each number (between dots) separately.
    # So with: (2.1 vs 2.10): (2 vs 2) and (1 vs 10)

    def __init__(self, since: float = default_since, until: float = default_until):
        """
        Used to determine if retriever_object_link should be constructed/committed.

        Args:
            since: Version item introduced
            until: Version item last seen in (before removal)
        """
        self.since = since
        self.until = until

    def supports(self, v: str) -> bool:
        """
        Check if this object is supported by the given scenario version

        Args:
            v: The string representation of the scenario version

        Returns:
            `True`/`False` based on if the object is supported by the given scenario version
        """
        return self.since <= float(v) <= self.until

    def __repr__(self):
        since, until = "", ""
        if self.since > default_since:
            since = f"since: {self.since:.2f}"
        if self.until < default_until:
            until = f"until: {self.until:.2f}"
        s = ', '.join(list(filter(lambda x: x != "", [since, until])))
        return f"supported {s}"
