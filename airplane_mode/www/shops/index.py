import frappe

no_cache = 1


def get_context(context):
	airport = frappe.form_dict.get("airport")
	status = frappe.form_dict.get("status")
	filters = {}
	if airport:
		filters["airport"] = airport
	if status in ("Available", "Occupied"):
		filters["status"] = status
	context.shops = frappe.get_all(
		"Airport Shop",
		filters=filters,
		fields=["name", "shop_number", "shop_name", "shop_type", "airport", "area", "status"],
		order_by="airport asc, shop_number asc",
	)
	context.airports = frappe.get_all(
		"Airport",
		fields=["name", "code", "city", "total_shops", "available_shops", "occupied_shops"],
		filters={"total_shops": [">", 0]},
		order_by="name asc",
	)
	context.selected_airport = airport
	context.selected_status = status
	return context
