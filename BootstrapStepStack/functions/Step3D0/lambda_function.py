import logging
import json
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logging.info('Hello From Step3')

    logging.info('event: ')
    logging.info(json.dumps(event))

    logging.info('context: ')
    print(context)

    logging.info('End From Step3')

    return {
        'event': json.dumps(event)
    }
