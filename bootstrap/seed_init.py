# bootstrap/seed_init.py

from 00_CORE_EXISTENCE.identity.self_id import SelfIdentity
from 00_CORE_EXISTENCE.heartbeat.clock import SystemClock
from 00_CORE_EXISTENCE.heartbeat.pulse import Pulse

def initialize_seed():
    identity = SelfIdentity()
    clock = SystemClock()
    pulse = Pulse()

    return {
        "identity": identity,
        "clock": clock,
        "pulse": pulse
    }
