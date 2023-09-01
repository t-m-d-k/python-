import configparser
config = configparser.ConfigParser()


# Read the configuration file
config.read('example.ini')

# Access configuration values
dev_host = config.get('dev', 'host')
dev_port = config.getint('dev', 'port')
prod_host = config.get('prod', 'host')
prod_port = config.get('prod', 'port')

print(dev_host, dev_port)
print(prod_host , prod_port)