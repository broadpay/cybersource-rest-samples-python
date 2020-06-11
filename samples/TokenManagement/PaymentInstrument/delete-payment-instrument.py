from CyberSource import *
import os
import json
import time
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

tms_file_path = os.path.join(os.getcwd(), "Samples", "TokenManagement", "PaymentInstrument", "create-payment-instrument-card.py")
create_payment_instrument = SourceFileLoader("module.name", tms_file_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def delete_payment_instrument():
    profileid = "93B32398-AD51-4CC2-A682-EA3E93614EB1"

    api_response = create_payment_instrument.create_payment_instrument_card()
    tokenId = api_response.id

    time.sleep(10)

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentInstrumentApi(client_config)
        return_data, status, body = api_instance.delete_payment_instrument(profileid, tokenId)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentInstrumentApi->delete_payment_instrument: %s\n" % e)

if __name__ == "__main__":
    delete_payment_instrument()
