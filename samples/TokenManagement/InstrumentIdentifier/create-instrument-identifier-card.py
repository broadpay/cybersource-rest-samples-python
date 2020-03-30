from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def create_instrument_identifier_card():
    profileid = "93B32398-AD51-4CC2-A682-EA3E93614EB1"

    cardNumber = "411111111111111"
    card = Tmsv1instrumentidentifiersCard(
        number = cardNumber
    )

    requestObj = CreateInstrumentIdentifierRequest(
        card = card.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InstrumentIdentifierApi(client_config)
        return_data, status, body = api_instance.create_instrument_identifier(profileid, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling InstrumentIdentifierApi->create_instrument_identifier: %s\n" % e)

if __name__ == "__main__":
    create_instrument_identifier_card()
