# switch
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = False

# Redis config
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

# Proxy Pool config
POOL_UPPER_THRESHOLD = 10000

# Api server config
API_HOST = 'localhost'
API_PORT = '8080'

# loop duration
TESTER_CYCLE = 20
GETTER_CYCLE = 20

# Tester config
TEST_URL = [
    'http://www.baidu.com',
]
VALID_STATUS_CODES = [200]
BATCH_TEST_SIZE = 100
