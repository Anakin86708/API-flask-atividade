from flask.json import JSONEncoder

class Settings(JSONEncoder):
    def __init__(self, eventNotificationsState: bool, onlyFavoriteState: bool, updateFrequencyValue: str):
        self.eventNotificationsState = eventNotificationsState
        self.onlyFavoriteState = onlyFavoriteState
        self.updateFrequencyValue = updateFrequencyValue

    def as_json(self):
        return vars(self)

    def __repr__(self):
        return f'eventNotificationsState: {self.eventNotificationsState}\nonlyFavoriteState: {self.onlyFavoriteState}\nupdateFrequencyValue: {self.updateFrequencyValue}'