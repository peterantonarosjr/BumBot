import utility
import logging
from supremeBot import Bot

def main():
    logging.basicConfig(format="%(levelname)s: %(asctime)s - %(message)s",
                        datefmt="%I:%M:%S", level=logging.INFO)

    items = {
            "name": "ITEM",
            "colorwayPosition": "COLOR",
            "size": "SIZE"
        }
    billing_info = {
        "fullName": "NAME",
        "email": "EMAIL",
        "phone": "PHONE",
        "address": "ADDRESS",
        "unit": "UNIT",
        "zip": "ZIPCODE",
        "city": "CITY",
        "state": "STATE (2 Letters)",
        "ccNumber": "CCNUMBER",
        "expM": "MONTH (2 Numbers)",
        "expY": "YEAR (4 Numbers)",
        "cvv": "CCV"
    }
    numberOfBuys = 1

    bot = Bot("https://www.supremenewyork.com/shop/all/jackets")
    logging.info("Initialized a bot instance")
    item_index = 0
    while item_index != numberOfBuys:
        item_name = items["name"]
        item_colorway_position = items["colorwayPosition"]
        item_size = items["size"]

        bot.go_to_start_page()
        while bot.is_on_start_page():
            if not bot.select_item(item_name):
                bot.refresh()
        logging.info("Item {} selected".format(item_name))

        if item_colorway_position and bot.select_colorway(item_colorway_position):
            logging.info("Colorway at position {} selected".format(
                item_colorway_position))

        if item_size and bot.select_size(item_size):
            logging.info("Size {} selected".format(item_size))

        if bot.add_to_cart():
            item_index += 1
            logging.info(
                "Item {} successfully added to cart".format(item_name))

    if bot.go_to_checkout():
        logging.info("Proceeded to checkout successfully")

    logging.info("Filling in the checkout form")
    bot.fill_in_checkout_form(billing_info)

    if bot.agree_to_terms():
        logging.info("Agreed to terms")


# Uncomment this block of code to process the payment automatically
    if bot.process_payment():
        logging.info("Payment is processing")


if __name__ == "__main__":
    main()
