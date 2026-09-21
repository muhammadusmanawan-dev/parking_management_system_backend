from decimal import Decimal

class FareService:
    HOURLY_RATE = Decimal("100.00")

    @classmethod
    def calculate_fare(cls, ticket):
        duration = ticket.exit_time - ticket.entry_time

        total_seconds = duration.total_seconds()

        total_hours = total_seconds / 3600

        if total_hours <= 1:
            hours = 1
        else:
            hours = int(total_hours)

            if total_hours > hours:
                hours += 1

        return cls.HOURLY_RATE * hours
    