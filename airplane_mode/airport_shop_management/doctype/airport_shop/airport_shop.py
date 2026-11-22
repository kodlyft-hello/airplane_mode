# Copyright (c) 2026, Ali Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirportShop(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link
		area: DF.Float
		contract_expiry_date: DF.Date | None
		contract_start_date: DF.Date | None
		rent_amount: DF.Currency
		shop_name: DF.Data
		shop_number: DF.Data
		shop_type: DF.Link | None
		status: DF.Literal["Available", "Occupied"]
		tenant_email: DF.Data | None
		tenant_name: DF.Data | None
		tenant_phone: DF.Data | None
	# end: auto-generated types

	def before_validate(self):
		if not self.rent_amount:
			self.rent_amount = frappe.db.get_single_value("Airport Shop Settings", "default_rent_amount") or 0

	def validate(self):
		self.status = "Occupied" if self.tenant_name else "Available"
		if (
			self.contract_start_date
			and self.contract_expiry_date
			and self.contract_expiry_date < self.contract_start_date
		):
			frappe.throw("Contract Expiry Date cannot be before Contract Start Date.")

	def on_update(self):
		update_airport_shop_counts(self.airport)
		previous = self.get_doc_before_save()
		if previous and previous.airport != self.airport:
			update_airport_shop_counts(previous.airport)

	def after_delete(self):
		update_airport_shop_counts(self.airport)


def update_airport_shop_counts(airport):
	if not airport or not frappe.db.exists("Airport", airport):
		return
	total = frappe.db.count("Airport Shop", {"airport": airport})
	occupied = frappe.db.count("Airport Shop", {"airport": airport, "status": "Occupied"})
	frappe.db.set_value(
		"Airport",
		airport,
		{"total_shops": total, "occupied_shops": occupied, "available_shops": total - occupied},
		update_modified=False,
	)
