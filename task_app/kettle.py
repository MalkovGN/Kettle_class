import time
import random
import configparser
import logging

from .models import LogModel

# Logger settings
console_out = logging.StreamHandler()
log_in_file = logging.FileHandler('kettle_logs.log')
logging.basicConfig(
    handlers=(console_out, log_in_file),
    level=logging.INFO,
    format='%(levelname)s - %(message)s - %(asctime)s - %(name)s',
    datefmt='%m-%d-%Y %H:%M:%S',
    encoding='utf-8',
)

# Settings .ini file parser
config = configparser.ConfigParser()
config.read('task_app/config.ini', encoding='utf-8')


class Kettle:
    def __init__(
            self,
            boiling_time=int(config['Kettle']['boiling_time']),
            boiling_temp=int(config['Kettle']['boiling_temp']),
            water_volume=float(config['Kettle']['water_volume']),
    ):
        self.boiling_time = boiling_time  # Set number of seconds to boil
        self.boiling_temp = boiling_temp  # Set boiling temperature
        self.water_volume = water_volume  # Set the kettle volume
        self.start_temp = random.randint(5, 45)  # Generating the start water temperature

    def check_values(self):
        """
        Checking the kettle volume
        and max boiling temperature
        """
        if self.water_volume > 1.7:  # 1.7 - the value from link in test task file
            logging.info('The kettle cant boiled more than 1.7 litres')
            LogModel(
                message='The kettle cant boiled more than 1.7 litres',
            ).save()
            return True
        if self.boiling_temp > 100:  # 100 - Maximum boiling point
            logging.info('The temperature of water cant be more than 100')
            LogModel(
                message='The temperature of water cant be more than 100',
            ).save()
            return True

    def start_boiling(self):
        if self.check_values():
            return
        logging.info('The kettle is turned on.')
        log = LogModel.objects.create(
            message='The kettle is turned on.\n',
        )
        start_time = 0
        delta = (self.boiling_temp - self.start_temp) / self.boiling_time  # Count the value adding every second
        try:
            while start_time <= self.boiling_time:
                logging.info(f'Now the temperature of water is {round(self.start_temp, 1)}°C')
                message = LogModel.objects.get(pk=log.pk).message  # Get actual message from current log
                LogModel.objects.filter(pk=log.pk).update(
                    message=message + f'Now the temperature of water is {round(self.start_temp, 1)}°C\n'
                )  # Update current log message
                time.sleep(1)
                self.start_temp += delta
                start_time += 1
            message = LogModel.objects.get(pk=log.pk).message
            LogModel.objects.filter(pk=log.pk).update(
                message=message + 'The kettle boiled. Now its turned off',
            )
            logging.info('The kettle boiled. Now its turned off')
        except KeyboardInterrupt:
            message = LogModel.objects.get(pk=log.pk).message
            LogModel.objects.filter(pk=log.pk).update(
                message=message + 'The kettle has been stopped. Now its turned off',
            )
            logging.info('The kettle has been stopped. Now its turned off')
