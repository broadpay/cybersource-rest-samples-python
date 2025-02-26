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

def enroll_with_travel_information():
    clientReferenceInformationCode = "cybs_test"
    clientReferenceInformation = Riskv1decisionsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetailsTotalAmount = "10.99"
    orderInformationAmountDetails = Riskv1authenticationsOrderInformationAmountDetails(
        currency = orderInformationAmountDetailsCurrency,
        total_amount = orderInformationAmountDetailsTotalAmount
    )

    orderInformationBillToAddress1 = "1 Market St"
    orderInformationBillToAddress2 = "Address 2"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToCountry = "US"
    orderInformationBillToLocality = "san francisco"
    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Doe"
    orderInformationBillToPhoneNumber = "4158880000"
    orderInformationBillToEmail = "test@cybs.com"
    orderInformationBillToPostalCode = "94105"
    orderInformationBillTo = Riskv1authenticationsOrderInformationBillTo(
        address1 = orderInformationBillToAddress1,
        address2 = orderInformationBillToAddress2,
        administrative_area = orderInformationBillToAdministrativeArea,
        country = orderInformationBillToCountry,
        locality = orderInformationBillToLocality,
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        phone_number = orderInformationBillToPhoneNumber,
        email = orderInformationBillToEmail,
        postal_code = orderInformationBillToPostalCode
    )

    orderInformation = Riskv1authenticationsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    paymentInformationCardType = "002"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2025"
    paymentInformationCardNumber = "5200340000000015"
    paymentInformationCard = Riskv1authenticationsPaymentInformationCard(
        type = paymentInformationCardType,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear,
        number = paymentInformationCardNumber
    )

    paymentInformation = Riskv1authenticationsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    buyerInformationMobilePhone = 1245789632
    buyerInformation = Riskv1authenticationsBuyerInformation(
        mobile_phone = buyerInformationMobilePhone
    )

    consumerAuthenticationInformationTransactionMode = "MOTO"
    consumerAuthenticationInformation = Riskv1decisionsConsumerAuthenticationInformation(
        transaction_mode = consumerAuthenticationInformationTransactionMode
    )


    travelInformationLegs = []
    travelInformationLegs1 = Riskv1decisionsTravelInformationLegs(
        destination = "DEF",
        carrier_code = "UA",
        departure_date = "2019-01-01"
    )

    travelInformationLegs.append(travelInformationLegs1.__dict__)

    travelInformationLegs2 = Riskv1decisionsTravelInformationLegs(
        destination = "RES",
        carrier_code = "AS",
        departure_date = "2019-02-21"
    )

    travelInformationLegs.append(travelInformationLegs2.__dict__)

    travelInformationNumberOfPassengers = 2

    travelInformationPassengers = []
    travelInformationPassengers1 = Riskv1decisionsTravelInformationPassengers(
        first_name = "Raj",
        last_name = "Charles"
    )

    travelInformationPassengers.append(travelInformationPassengers1.__dict__)

    travelInformationPassengers2 = Riskv1decisionsTravelInformationPassengers(
        first_name = "Potter",
        last_name = "Suhember"
    )

    travelInformationPassengers.append(travelInformationPassengers2.__dict__)

    travelInformation = Riskv1authenticationsTravelInformation(
        legs = travelInformationLegs,
        number_of_passengers = travelInformationNumberOfPassengers,
        passengers = travelInformationPassengers
    )

    requestObj = CheckPayerAuthEnrollmentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        order_information = orderInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        buyer_information = buyerInformation.__dict__,
        consumer_authentication_information = consumerAuthenticationInformation.__dict__,
        travel_information = travelInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PayerAuthenticationApi(client_config)
        return_data, status, body = api_instance.check_payer_auth_enrollment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PayerAuthenticationApi->check_payer_auth_enrollment: %s\n" % e)

if __name__ == "__main__":
    enroll_with_travel_information()
