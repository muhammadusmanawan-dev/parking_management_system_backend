from rest_framework.exceptions import APIException

class NoParkingSpotAvailable(APIException):
    status_code = 400
    default_detail = "No parking spot available."
    default_code = "no_parking_spot"


class VehicleTypeMismatch(APIException):
    status_code = 400
    default_detail = "Vehicle type does not match the registered vehicle."
    default_code = "vehicle_type_mismatch"


class TicketAlreadyCompleted(APIException):
    status_code = 400
    default_detail = "This ticket has already been completed."
    default_code = "ticket_already_completed"

class PaymentProviderError(APIException):
    status_code = 502
    default_detail = "Payment provider request failed."
    default_code = "payment_provider_error"

class PaymentAlreadyExists(APIException):
    status_code = 400
    default_detail = "A payment record already exists for this ticket."
    default_code = "payment_already_exists"


class UnsupportedPaymentMethod(APIException):
    status_code = 400
    default_detail = "The selected payment method is not supported."
    default_code = "unsupported_payment_method"


class FareCalculationError(APIException):
    status_code = 400
    default_detail = "Cannot calculate fare for a ticket without a valid exit time."
    default_code = "fare_calculation_error"


class PaymentNotFound(APIException):
    status_code = 400
    default_detail = "The requested payment record was not found."
    default_code = "payment_not_found"
