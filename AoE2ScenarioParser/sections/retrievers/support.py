from __future__ import annotations


class Support:
    def __init__(self, since: float = 0, until: float = 100):
        """
        Used to determine if retriever_object_link should be constructed/committed.

        Args:
            since (float): Version item introduced
            until (float): Version item last seen in (before removal)
        """
        self.since = since
        self.until = until

    def supports(self, v):
        return self.since <= float(v) <= self.until
