import logging

class logGen:
    @staticmethod
    def loggen():
        path = "./logs/Automat.log"  #for terminal execution, otherwise an exception occurs
        #path = "..\\logs\Automation.log" #for the RUN button
        logging.basicConfig(filename=path, force=True,  #force is used to remove handlers and create the log file
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger


#logger=logGen.loggen()
#logger.info("This is my INFO")