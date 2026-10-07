from dataclasses import dataclass


@dataclass
class CustomerRequest:
    request_id: int
    customer_name: str
    issue: str
