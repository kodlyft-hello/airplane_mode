# Copyright (c) 2026, Ali Raza and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Airport(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		available_shops: DF.Int
		city: DF.Data
		code: DF.Data
		country: DF.Link
		occupied_shops: DF.Int
		total_shops: DF.Int
	# end: auto-generated types

	pass
