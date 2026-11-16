# === Stage 14: Статусы записей ===
# Project: TheaterProps
LIFECYCLE_STATES = ["new", "issued", "returned", "lost", "damaged", "retired"]

ALLOWED_TRANSITIONS = {
    "new": ["issued", "damaged", "retired"],
    "issued": ["returned", "damaged", "lost", "retired"],
    "returned": ["new", "retired"],
    "lost": ["retired"],
    "damaged": ["returned", "retired"],
    "retired": [],
}

def transition(state, action):
    """Return the resulting state after applying an action, or None if invalid."""
    allowed = ALLOWED_TRANSITIONS.get(state, [])
    if action in allowed:
        return action
    return None

def is_valid_transition(state, action):
    """Check whether a given action is a permitted transition from the given state."""
    return action in ALLOWED_TRANSITIONS.get(state, [])

def next_states(state):
    """Return the list of states reachable from the current state."""
    return ALLOWED_TRANSITIONS.get(state, [])
