# Copyright (c) 2026, Ali Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from airplane_mode.airplane_mode.doctype.airplane_flight_crew.airplane_flight_crew import (
			AirplaneFlightCrew,
		)

		airplane: DF.Link
		amended_from: DF.Link | None
		crew_members: DF.Table[AirplaneFlightCrew]
		date_of_departure: DF.Date
		destination_airport: DF.Link
		destination_airport_code: DF.ReadOnly | None
		duration: DF.Duration
		gate_number: DF.Data | None
		is_published: DF.Check
		route: DF.Data | None
		source_airport: DF.Link
		source_airport_code: DF.ReadOnly | None
		status: DF.Literal["Scheduled", "Completed", "Cancelled"]
		time_of_departure: DF.Time
	# end: auto-generated types

	def on_submit(self):
		self.db_set("status", "Completed")

	def on_update(self):
		self.enqueue_gate_number_sync()

	def on_update_after_submit(self):
		self.enqueue_gate_number_sync()

	def enqueue_gate_number_sync(self):
		if not self.has_value_changed("gate_number"):
			return
		frappe.enqueue(
			update_ticket_gate_numbers,
			queue="short",
			enqueue_after_commit=True,
			flight=self.name,
			gate_number=self.gate_number,
		)


def update_ticket_gate_numbers(flight, gate_number):
	frappe.db.set_value("Airplane Ticket", {"flight": flight}, "gate_number", gate_number)


def get_list_context(context=None):
	return {"title": "Flights", "list_template": "templates/includes/list/list.html"}
