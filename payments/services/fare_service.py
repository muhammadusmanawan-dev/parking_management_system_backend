from decimal import Decimal


class FareService:
    HOURLY_RATE = Decimal("100.00")

    @classmethod
    def calculate_fare(cls, ticket):
        if not ticket.exit_time:
            raise ValueError("Ticket must have an exit time.")

        duration = ticket.exit_time - ticket.entry_time
        total_seconds = duration.total_seconds()
        total_hours = total_seconds / 3600
        hours = max(1, int(total_hours))

        if total_hours > hours:
            hours += 1

        return cls.HOURLY_RATE * hours
