# === Stage 31: Что требует внимания ===
# Project: TheaterProps
from datetime import datetime

class Report:
    def __init__(self, props):
        self.props = props

    def expired(self):
        return [r for r in self.props if r['issued_at'] and r['due_at'] and r['due_at'] < datetime.now().date()]

    def stuck(self):
        return [r for r in self.props if r['status'] == 'issued' and r['returned_at'] is None]

    def incomplete(self):
        return [r for r in self.props if not r.get('item_name') or not r.get('scene')]

    def summary(self):
        return {
            'expired': self.expired(),
            'stuck': self.stuck(),
            'incomplete': self.incomplete(),
        }
