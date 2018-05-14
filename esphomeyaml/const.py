"""Constants used by esphomeyaml."""

MAJOR_VERSION = 1
MINOR_VERSION = 4
PATCH_VERSION = '0'
__short_version__ = '{}.{}'.format(MAJOR_VERSION, MINOR_VERSION)
__version__ = '{}.{}'.format(__short_version__, PATCH_VERSION)

ESP_PLATFORM_ESP32 = 'ESP32'
ESP_PLATFORM_ESP8266 = 'ESP8266'
ESP_PLATFORMS = [ESP_PLATFORM_ESP32, ESP_PLATFORM_ESP8266]

APB_CLOCK_FREQ = 80000000

CONF_ESPHOMEYAML = 'esphomeyaml'
CONF_NAME = 'name'
CONF_PLATFORM = 'platform'
CONF_BOARD = 'board'
CONF_SIMPLIFY = 'simplify'
CONF_USE_BUILD_FLAGS = 'use_build_flags'
CONF_LIBRARY_URI = 'library_uri'
CONF_LOGGER = 'logger'
CONF_WIFI = 'wifi'
CONF_SSID = 'ssid'
CONF_PASSWORD = 'password'
CONF_MANUAL_IP = 'manual_ip'
CONF_STATIC_IP = 'static_ip'
CONF_GATEWAY = 'gateway'
CONF_SUBNET = 'subnet'
CONF_OTA = 'ota'
CONF_MQTT = 'mqtt'
CONF_BROKER = 'broker'
CONF_USERNAME = 'username'
CONF_POWER_SUPPLY = 'power_supply'
CONF_ID = 'id'
CONF_MQTT_ID = 'mqtt_id'
CONF_PIN = 'pin'
CONF_NUMBER = 'number'
CONF_INVERTED = 'inverted'
CONF_I2C = 'i2c'
CONF_SDA = 'sda'
CONF_SCL = 'scl'
CONF_FREQUENCY = 'frequency'
CONF_PCA9685 = 'pca9685'
CONF_PCA9685_ID = 'pca9685_id'
CONF_OUTPUT = 'output'
CONF_CHANNEL = 'channel'
CONF_LIGHT = 'light'
CONF_RED = 'red'
CONF_GREEN = 'green'
CONF_BLUE = 'blue'
CONF_SENSOR = 'sensor'
CONF_TEMPERATURE = 'temperature'
CONF_HUMIDITY = 'humidity'
CONF_MODEL = 'model'
CONF_BINARY_SENSOR = 'binary_sensor'
CONF_DEVICE_CLASS = 'device_class'
CONF_GPIO = 'gpio'
CONF_DHT = 'dht'
CONF_SAFE_MODE = 'safe_mode'
CONF_MODE = 'mode'
CONF_GAMMA_CORRECT = 'gamma_correct'
CONF_RETAIN = 'retain'
CONF_DISCOVERY = 'discovery'
CONF_DISCOVERY_PREFIX = 'discovery_prefix'
CONF_STATE_TOPIC = 'state_topic'
CONF_COMMAND_TOPIC = 'command_topic'
CONF_AVAILABILITY = 'availability'
CONF_TOPIC = 'topic'
CONF_PAYLOAD_AVAILABLE = 'payload_available'
CONF_PAYLOAD_NOT_AVAILABLE = 'payload_not_available'
CONF_DEFAULT_TRANSITION_LENGTH = 'default_transition_length'
CONF_BINARY = 'binary'
CONF_WHITE = 'white'
CONF_RGBW = 'rgbw'
CONF_MAX_POWER = 'max_power'
CONF_BIT_DEPTH = 'bit_depth'
CONF_BAUD_RATE = 'baud_rate'
CONF_LOG_TOPIC = 'log_topic'
CONF_TX_BUFFER_SIZE = 'tx_buffer_size'
CONF_LEVEL = 'level'
CONF_LOGS = 'logs'
CONF_PORT = 'port'
CONF_WILL_MESSAGE = 'will_message'
CONF_BIRTH_MESSAGE = 'birth_message'
CONF_PAYLOAD = 'payload'
CONF_QOS = 'qos'
CONF_DISCOVERY_RETAIN = 'discovery_retain'
CONF_TOPIC_PREFIX = 'topic_prefix'
CONF_HOSTNAME = 'hostname'
CONF_PHASE_BALANCER = 'phase_balancer'
CONF_ADDRESS = 'address'
CONF_ENABLE_TIME = 'enable_time'
CONF_KEEP_ON_TIME = 'keep_on_time'
CONF_DNS1 = 'dns1'
CONF_DNS2 = 'dns2'
CONF_UNIT_OF_MEASUREMENT = 'unit_of_measurement'
CONF_ICON = 'icon'
CONF_ACCURACY_DECIMALS = 'accuracy_decimals'
CONF_EXPIRE_AFTER = 'expire_after'
CONF_FILTERS = 'filters'
CONF_OFFSET = 'offset'
CONF_MULTIPLY = 'multiply'
CONF_FILTER_OUT = 'filter_out'
CONF_FILTER_NAN = 'filter_nan'
CONF_SLIDING_WINDOW_MOVING_AVERAGE = 'sliding_window_moving_average'
CONF_EXPONENTIAL_MOVING_AVERAGE = 'exponential_moving_average'
CONF_WINDOW_SIZE = 'window_size'
CONF_SEND_EVERY = 'send_every'
CONF_ALPHA = 'alpha'
CONF_LAMBDA = 'lambda'
CONF_UPDATE_INTERVAL = 'update_interval'
CONF_PULL_MODE = 'pull_mode'
CONF_COUNT_MODE = 'count_mode'
CONF_RISING_EDGE = 'rising_edge'
CONF_FALLING_EDGE = 'falling_edge'
CONF_INTERNAL_FILTER = 'internal_filter'
CONF_DALLAS_ID = 'dallas_id'
CONF_INDEX = 'index'
CONF_RESOLUTION = 'resolution'
CONF_ATTENUATION = 'attenuation'
CONF_PRESSURE = 'pressure'
CONF_TRIGGER_PIN = 'trigger_pin'
CONF_ECHO_PIN = 'echo_pin'
CONF_TIMEOUT_METER = 'timeout_meter'
CONF_TIMEOUT_TIME = 'timeout_time'
CONF_IR_TRANSMITTER_ID = 'ir_transmitter_id'
CONF_CARRIER_DUTY_PERCENT = 'carrier_duty_percent'
CONF_NEC = 'nec'
CONF_COMMAND = 'command'
CONF_DATA = 'data'
CONF_NBITS = 'nbits'
CONF_LG = 'lg'
CONF_SONY = 'sony'
CONF_PANASONIC = 'panasonic'
CONF_REPEAT = 'repeat'
CONF_TIMES = 'times'
CONF_WAIT_TIME = 'wait_time'
CONF_OSCILLATION_OUTPUT = 'oscillation_output'
CONF_SPEED = 'speed'
CONF_OSCILLATION_STATE_TOPIC = 'oscillation_state_topic'
CONF_OSCILLATION_COMMAND_TOPIC = 'oscillation_command_topic'
CONF_SPEED_STATE_TOPIC = 'speed_state_topic'
CONF_SPEED_COMMAND_TOPIC = 'speed_command_topic'
CONF_LOW = 'low'
CONF_MEDIUM = 'medium'
CONF_HIGH = 'high'
CONF_NUM_ATTEMPTS = 'num_attempts'
CONF_CLIENT_ID = 'client_id'
CONF_RAW = 'raw'
CONF_CARRIER_FREQUENCY = 'carrier_frequency'
CONF_RATE = 'rate'
CONF_ADS1115_ID = 'ads1115_id'
CONF_MULTIPLEXER = 'multiplexer'
CONF_GAIN = 'gain'
CONF_SLEEP_DURATION = 'sleep_duration'
CONF_WAKEUP_PIN = 'wakeup_pin'
CONF_RUN_CYCLES = 'run_cycles'
CONF_RUN_DURATION = 'run_duration'
CONF_AP = 'ap'
CONF_CSS_URL = 'css_url'
CONF_JS_URL = 'js_url'
CONF_SSL_FINGERPRINTS = 'ssl_fingerprints'
CONF_PCF8574 = 'pcf8574'
CONF_PCF8575 = 'pcf8575'
CONF_SCAN = 'scan'
CONF_KEEPALIVE = 'keepalive'
CONF_INTEGRATION_TIME = 'integration_time'
CONF_RECEIVE_TIMEOUT = 'receive_timeout'
CONF_SCAN_INTERVAL = 'scan_interval'
CONF_MAC_ADDRESS = 'mac_address'
CONF_SETUP_MODE = 'setup_mode'
CONF_IIR_FILTER = 'iir_filter'
CONF_MEASUREMENT_DURATION = 'measurement_duration'
CONF_LOW_VOLTAGE_REFERENCE = 'low_voltage_reference'
CONF_HIGH_VOLTAGE_REFERENCE = 'high_voltage_reference'
CONF_VOLTAGE_ATTENUATION = 'voltage_attenuation'
CONF_THRESHOLD = 'threshold'
CONF_OVERSAMPLING = 'oversampling'
CONF_GAS_RESISTANCE = 'gas_resistance'
CONF_NUM_LEDS = 'num_leds'
CONF_MAX_REFRESH_RATE = 'max_refresh_rate'
CONF_CHIPSET = 'chipset'
CONF_DATA_PIN = 'data_pin'
CONF_CLOCK_PIN = 'clock_pin'
CONF_RGB_ORDER = 'rgb_order'
CONF_ACCURACY = 'accuracy'

ESP32_BOARDS = [
    'featheresp32', 'node32s', 'espea32', 'firebeetle32', 'esp32doit-devkit-v1',
    'pocket_32', 'espectro32', 'esp32vn-iot-uno', 'esp320', 'esp-wrover-kit',
    'esp32dev', 'heltec_wifi_kit32', 'heltec_wifi_lora_32', 'hornbill32dev',
    'hornbill32minima', 'intorobot', 'm5stack-core-esp32', 'mhetesp32devkit',
    'mhetesp32minikit', 'nano32', 'microduino-core-esp32', 'nodemcu-32s',
    'quantum', 'esp32-evb', 'esp32-gateway', 'onehorse32dev', 'esp32thing',
    'espino32', 'lolin32', 'wemosbat', 'widora-air', 'nina_w10',
]

ESP8266_BOARDS = [
    'gen4iod', 'huzzah', 'oak', 'espduino', 'espectro', 'espresso_lite_v1',
    'espresso_lite_v2', 'espino', 'esp01', 'esp01_1m', 'esp07', 'esp12e', 'esp8285',
    'esp_wroom_02', 'phoenix_v1', 'phoenix_v2', 'wifinfo', 'heltex_wifi_kit_8',
    'nodemcu', 'nodemcuv2', 'modwifi', 'wio_node', 'sparkfunBlynk', 'thing',
    'thingdev', 'esp210', 'espinotee', 'd1', 'd1_mini', 'd1_mini_lite', 'd1_mini_pro',
]
ESP_BOARDS_FOR_PLATFORM = {
    ESP_PLATFORM_ESP32: ESP32_BOARDS,
    ESP_PLATFORM_ESP8266: ESP8266_BOARDS
}
