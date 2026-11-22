# Copyright (c) 2026, Ali Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import formatdate, get_first_day


class ShopRentPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link | None
		amended_from: DF.Link | None
		amount: DF.Currency
		mode_of_payment: DF.Literal["Cash", "Bank Transfer", "Card", "Cheque"]
		payment_date: DF.Date
		rent_month: DF.Date
		shop: DF.Link
		shop_name: DF.Data | None
		tenant_email: DF.Data | None
		tenant_name: DF.Data | None
	# end: auto-generated types

	def validate(self):
		self.rent_month = get_first_day(self.rent_month)
		if frappe.db.get_value("Airport Shop", self.shop, "status") != "Occupied":
			frappe.throw(f"Shop {self.shop} has no tenant, so there is no rent to collect.")
		duplicate = frappe.db.exists(
			"Shop Rent Payment",
			{"shop": self.shop, "rent_month": self.rent_month, "docstatus": 1, "name": ["!=", self.name]},
		)
		if duplicate:
			frappe.throw(
				f"Rent for {formatdate(self.rent_month, 'MMMM yyyy')} is already collected in {duplicate}."
			)
