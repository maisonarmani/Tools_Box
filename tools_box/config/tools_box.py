from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Human Resources"),
            "items": [
                {
                    "type": "doctype",
                    "is_query_report": False,
                    "name": "Staff Requisition Form",
                    "label": "Staff Requisition"
                },
                {
                    "type": "doctype",
                    "is_query_report": False,
                    "name": "Staff Replacement Request Form",
                    "label": "Staff Replacement"
                },
                {
                    "type": "doctype",
                    "is_query_report": False,
                    "name": "Overtime Request",
                    "label": "Overtime Request"
                },
                {
                    "type": "doctype",
                    "is_query_report": False,
                    "name": "Overtime Sheet",
                    "label": "Overtime Sheet"
                },
            ]
        },{
            "label": _("Buying"),
            "items": [
                {
                    "type": "doctype",
                    "is_query_report": False,
                    "name": "Purchase Requisition",
                    "label": "Purchase requisition"
                },
            ]
        },{
            "label": _("Selling"),
            "items": [
                {
                    "type": "doctype",
                    "is_query_report": False,
                    "name": "Authority to Load",
                    "label": "Authority to Load"
                },
                {
                    "type": "doctype",
                    "is_query_report": False,
                    "name": "Call Log",
                    "label": "Call Log"
                },
            ]
        },
    ]
