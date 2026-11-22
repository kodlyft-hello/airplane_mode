// Copyright (c) 2026, Ali Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
		frm.add_custom_button(
			__("Assign Seat"),
			() => {
				const dialog = new frappe.ui.Dialog({
					title: __("Select Seat"),
					fields: [
						{
							label: __("Seat Number"),
							fieldname: "seat_number",
							fieldtype: "Data",
							reqd: 1,
						},
					],
					primary_action_label: __("Assign"),
					primary_action(values) {
						frm.set_value("seat", values.seat_number);
						dialog.hide();
					},
				});
				dialog.show();
			},
			__("Actions")
		);
	},
});
