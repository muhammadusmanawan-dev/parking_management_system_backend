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
