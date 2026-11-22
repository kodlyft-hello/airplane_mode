// Copyright (c) 2026, Ali Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airport Shop", {
	setup(frm) {
		frm.set_query("shop_type", () => ({ filters: { enabled: 1 } }));
	},
	async onload(frm) {
		if (frm.is_new() && !frm.doc.rent_amount) {
			const amount = await frappe.db.get_single_value(
				"Airport Shop Settings",
				"default_rent_amount"
			);
			if (amount) frm.set_value("rent_amount", amount);
		}
	},
	refresh(frm) {
		if (!frm.is_new() && frm.doc.status === "Occupied") {
			frm.add_custom_button(__("Collect Rent"), () => {
				frappe.new_doc("Shop Rent Payment", { shop: frm.doc.name });
			});
		}
	},
});
