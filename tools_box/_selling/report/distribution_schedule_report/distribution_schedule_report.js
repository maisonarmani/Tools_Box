// Copyright (c) 2016, masonarmani38@gmail.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Distribution Schedule Report"] = {
    "filters": [
        {
            "fieldname": "from",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": "2018-07-01",
            "width": "80",
            "reqd": 1
        },
        {
            "fieldname": "to",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(),
            "reqd": 1
        },
        {
            "fieldname": "customer",
            "label": __("Customer"),
            "fieldtype": "Link",
            "options": "Customer",
              "reqd": 0
        },
        {
            "fieldname": "territory",
            "label": __("Territory"),
            "fieldtype": "Link",
            "options": "Territory",
            "reqd": 0
        },
        {
            "fieldname": "inc_itm_qty",
            "label": __("Include Sales Item & Quantity "),
            "fieldtype": "Check",
            "reqd": 0
        },
    ]
}
