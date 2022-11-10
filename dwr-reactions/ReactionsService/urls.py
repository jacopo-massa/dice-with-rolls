# Global URLS for extensibility

GATEWAY_PORT = ':5000/'
HOME_URL = "http://gateway" + GATEWAY_PORT

REGISTER_URL = HOME_URL + "users/create"
LOGIN_URL = HOME_URL + "users/login"
LOGOUT_URL = HOME_URL + "users/logout"
USERS_URL = HOME_URL + "users"

READ_URL = HOME_URL + "stories"
SETTINGS_URL = HOME_URL + "stories/new/settings"
ROLL_URL = HOME_URL + "stories/new/roll"
WRITE_URL = HOME_URL + "stories/new/write"
REACTION_URL = HOME_URL + "stories/{}/react"
LATEST_URL = HOME_URL + "stories/latest"
RANGE_URL = HOME_URL + "stories/range"
RANDOM_URL = HOME_URL + "stories/random"

SEARCH_URL = HOME_URL + "search"

# Database in memory
TEST_DB = 'sqlite:///:memory:'

# Database
DEFAULT_DB = 'sqlite:///reaction-service.db'
