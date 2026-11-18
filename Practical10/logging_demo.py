import logging
logging .basicConfig(filename="application.log",level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
logger=logging.getLogger(__name__)

def process_order(order_id,amt):
    logger.info("Processing order %s",order_id)
    if amt<=0:
        logger.error("Order %s has an invalid amount: %s", order_id, amt)
        return False
    if amt<100:
        logger.warning("Order %s is a invalid amount: %s ",order_id,amt)
        logger.debug("Validating order amount for order %s", order_id) 
        logger.info("Order %s processed successfully", order_id)
        return True
process_order("ORD101", 1500)
process_order("ORD102", 50)
process_order("ORD103", -10)
    