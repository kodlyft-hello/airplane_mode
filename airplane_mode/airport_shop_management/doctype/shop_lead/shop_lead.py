# Copyright (c) 2026, Ali Raza and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class ShopLead(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data
		full_name: DF.Data
		message: DF.SmallText | None
		phone: DF.Data | None
		shop: DF.Link | None
		status: DF.Literal["Open", "Contacted", "Converted", "Lost"]
	# end: auto-generated types

	pass
