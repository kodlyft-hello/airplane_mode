frappe.listview_settings["Airplane Ticket"] = {
	get_indicator: function (doc) {
		if (doc.status === "Booked") {
			return [__("Booked"), "grey", "status,=,Booked"];
		} else if (doc.status === "Checked-In") {
			return [__("Checked-In"), "purple", "status,=,Checked-In"];
		} else if (doc.status === "Boarded") {
			return [__("Boarded"), "green", "status,=,Boarded"];
		}
	},
};
