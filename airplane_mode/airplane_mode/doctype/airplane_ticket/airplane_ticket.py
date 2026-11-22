# Copyright (c) 2026, Ali Raza and contributors
# For license information, please see license.txt

import random

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from airplane_mode.airplane_mode.doctype.airplane_ticket_add_on_item.airplane_ticket_add_on_item import (
			AirplaneTicketAddonItem,
		)

		add_ons: DF.Table[AirplaneTicketAddonItem]
		amended_from: DF.Link | None
		departure_date: DF.Date
		departure_time: DF.Time
		destination_airport_code: DF.ReadOnly | None
		duration_of_flight: DF.Duration
		flight: DF.Link
		flight_price: DF.Currency
		passenger: DF.Link
		seat: DF.Data | None
		source_airport_code: DF.ReadOnly | None
		status: DF.Literal["Booked", "Checked-In", "Boarded"]
		total_amount: DF.Currency
	# end: auto-generated types

	def before_insert(self):
		self.seat = generate_seat()

	def validate(self):
		seen = set()
		for add_on in list(self.add_ons):
			if add_on.item in seen:
				self.add_ons.remove(add_on)
			seen.add(add_on.item)
		self.calculate_total_amount()

	def calculate_total_amount(self):
		self.total_amount = (self.flight_price or 0) + sum(add_on.amount or 0 for add_on in self.add_ons)

	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw("Cannot submit ticket that is not in 'Boarded' status.")


def generate_seat():
	return f"{random.randint(1, 99)}{random.choice('ABCDE')}"
