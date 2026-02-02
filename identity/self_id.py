# identity/self_id.py

import uuid
from datetime import datetime

class SelfIdentity:
    """
    Core identity of A7DO.
    This must never reset unless death_protocol is invoked.
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.alive = True

    def as_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "alive": self.alive
        }
