# Copyright (c) 2026, Ali Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder.functions import Coalesce, Sum


def execute(filters=None):
	columns = [
		{"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 200},
		{"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 200},
	]
	data = get_data()
	total = sum(row.revenue for row in data)
	chart = {
		"data": {
			"labels": [row.airline for row in data],
			"datasets": [{"values": [row.revenue for row in data]}],
		},
		"type": "donut",
	}
	summary = [{"label": "Total Revenue", "value": total, "datatype": "Currency", "indicator": "Green"}]
	return columns, data, None, chart, summary


def get_data():
	airline = frappe.qb.DocType("Airline")
	airplane = frappe.qb.DocType("Airplane")
	flight = frappe.qb.DocType("Airplane Flight")
	ticket = frappe.qb.DocType("Airplane Ticket")
	revenue = Coalesce(Sum(ticket.total_amount), 0)
	return (
		frappe.qb.from_(airline)
		.left_join(airplane)
		.on(airplane.airline == airline.name)
		.left_join(flight)
		.on(flight.airplane == airplane.name)
		.left_join(ticket)
		.on((ticket.flight == flight.name) & (ticket.docstatus == 1))
		.select(airline.name.as_("airline"), revenue.as_("revenue"))
		.groupby(airline.name)
		.orderby(revenue, order=frappe.qb.desc)
		.run(as_dict=True)
	)
