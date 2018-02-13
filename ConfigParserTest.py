import configparser

config = configparser.ConfigParser()

config.read('fermenter.cfg')

target = config['temperature']['TargetTemp']

print(target)




