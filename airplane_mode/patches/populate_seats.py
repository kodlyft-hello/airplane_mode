import frappe

from airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket import generate_seat


def execute():
	for name in frappe.get_all("Airplane Ticket", filters={"seat": ["is", "not set"]}, pluck="name"):
		frappe.db.set_value("Airplane Ticket", name, "seat", generate_seat(), update_modified=False)
