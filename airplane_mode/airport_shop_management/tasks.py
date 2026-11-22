import frappe
from frappe.utils import fmt_money, formatdate, get_first_day, get_last_day, getdate, today


def send_rent_reminders():
	if not frappe.db.get_single_value("Airport Shop Settings", "enable_rent_reminders"):
		return
	month = get_first_day(today())
	shops = frappe.get_all(
		"Airport Shop",
		filters={"status": "Occupied", "tenant_email": ["is", "set"]},
		fields=[
			"name",
			"shop_name",
			"shop_number",
			"airport",
			"tenant_name",
			"tenant_email",
			"rent_amount",
			"contract_expiry_date",
		],
	)
	for shop in shops:
		if shop.contract_expiry_date and getdate(shop.contract_expiry_date) < month:
			continue
		if frappe.db.exists("Shop Rent Payment", {"shop": shop.name, "rent_month": month, "docstatus": 1}):
			continue
		frappe.sendmail(
			recipients=[shop.tenant_email],
			subject=f"Rent due for {formatdate(month, 'MMMM yyyy')}: {shop.shop_name}",
			template="rent_reminder",
			args={
				"shop": shop,
				"month": formatdate(month, "MMMM yyyy"),
				"due_by": formatdate(get_last_day(month)),
				"amount": fmt_money(shop.rent_amount, currency=frappe.db.get_default("currency")),
			},
			reference_doctype="Airport Shop",
			reference_name=shop.name,
		)
