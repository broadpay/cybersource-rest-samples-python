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

def get_list_of_files():
    startDate = "2020-03-20"
    endDate = "2020-03-30"
    organizationId = "testrest"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = SecureFileShareApi(client_config)
        return_data, status, body = api_instance.get_file_detail(startDate, endDate, organization_id=organizationId)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling SecureFileShareApi->get_file_detail: %s\n" % e)

if __name__ == "__main__":
    get_list_of_files()
