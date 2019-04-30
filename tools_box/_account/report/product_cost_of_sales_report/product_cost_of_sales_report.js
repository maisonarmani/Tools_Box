// Copyright (c) 2018, masonarmani38@gmail.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Product Cost Of Sales Report"] = {
	"filters": [
        {
            "fieldname":"from_date",
            "label": __("From"),
            "fieldtype": "Date",
            "width": "80",
            "reqd": 1,
            "default": frappe.datetime.get_today(),
        },
        {
            "fieldname":"to_date",
            "label": __("To"),
            "fieldtype": "Date",
            "width": "80",
            "reqd": 1,
            "default": frappe.datetime.get_today(),
        },
        {
            "fieldname": "warehouse",
            "label": __("Warehouse"),
            "fieldtype": "Link",
            "width": "80",
            "reqd":0,
            "options": "Warehouse"
        }
	]
}
