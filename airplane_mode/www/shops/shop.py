import frappe

no_cache = 1


def get_context(context):
	name = frappe.form_dict.get("shop")
	if not name or not frappe.db.exists("Airport Shop", name):
		raise frappe.DoesNotExistError
	context.shop = frappe.db.get_value(
		"Airport Shop",
		name,
		[
			"name",
			"shop_number",
			"shop_name",
			"shop_type",
			"airport",
			"area",
			"status",
			"rent_amount",
			"contract_expiry_date",
		],
		as_dict=True,
	)
	context.airport = frappe.db.get_value(
		"Airport", context.shop.airport, ["code", "city", "country"], as_dict=True
	)
	return context
