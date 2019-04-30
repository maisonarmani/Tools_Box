# Copyright (c) 2018, masonarmani38@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe

def execute(filters={}):
    columns = get_columns()
    dn = get_delivery_notes(filters)
    cur,sum = "",0
    data = []
    for record in dn:

        if cur == "":
            sum = get_stock_total(filters, record.item_code) # go through stock entry
            cur =  record.item_code

        gl_entry = get_gl_entries(record.dn, record.cost_center)
        if not gl_entry: continue
        sum += gl_entry[0].amt

        # when the item_code changes record it
        if record.item_code != cur:
            data.append((
                record.item_code,record.item_name,record.description, record.cost_center, sum
            ))
            cur,sum = "",0

    return columns, data


def get_stock_total(filters, item_code):
    cur,sum = "",0
    for stock in get_stock_entr(filters,item_code):

        if cur == "":
            cur =  stock.item_code
        gl_entry = get_gl_entries(stock.se, stock.cost_center)

        if not gl_entry:
            continue
            
        sum += gl_entry[0].amt

    return sum


def get_gl_entries(dn, cost_center):
    gl_entries = frappe.db.sql("""
		SELECT debit as amt, cost_center	
		FROM `tabGL Entry` WHERE  account = 'Cost of Goods Sold - GCL' and voucher_no ='{0}' and cost_center='{1}' GROUP BY cost_center 
		ORDER BY posting_date, 	account""".format(dn, cost_center), as_dict=1)

    return gl_entries


def get_delivery_notes(filters):
    # get all gl entry for item using the delivery note that has the item in its item list
    delvry_notes = frappe.db.sql("""SELECT dn.name as dn,i.item_code as item_code, i.item_name, i.description, dni.cost_center, dn.posting_date
     FROM `tabDelivery Note` dn INNER JOIN `tabDelivery Note Item` dni  ON(dn.name = dni.parent)
    RIGHT OUTER JOIN  `tabItem` i  ON(i.name = dni.item_code) WHERE i.is_sales_item =1 {conditions} ORDER BY dni.item_code """
                                 .format(conditions = get_conditions(filters)), as_dict=1)


    return delvry_notes





def get_stock_entr(filters, item):
    # get all gl entry for item using the delivery note that has the item in its item list
    stock_entr = frappe.db.sql("""SELECT se.name as se,i.item_code as item_code, i.item_name, i.description, sei.cost_center,se.posting_date
     FROM `tabStock Entry` se INNER JOIN `tabStock Entry Detail` sei ON(se.name = sei.parent)
    RIGHT OUTER JOIN  `tabItem` i  ON(i.name = sei.item_code) WHERE sei.item_code = '{item}' and  i.is_sales_item =1 {conditions} ORDER BY sei.item_code """
                                 .format(conditions = get_conditions(filters, True), item=item), as_dict=1)


    return stock_entr


def get_conditions(filters, stock_en = False):
    conditions = ""
    if not stock_en:
        code1, code2 = "dn", "dni"
    else:
        code1, code2 = "se", "sei"

    if filters.get("from_date") and filters.get("to_date") :
        conditions += " and {2}.posting_date between DATE('{0}') and DATE('{1}')".format(filters.get("from_date"),filters.get("to_date") , code1)

    if filters.get("cost_center"):
        conditions += " and {1}.cost_center = '{0}'".format(filters.get("cost_center"), code2)


    return  conditions

def get_columns():
    """return columns"""

    columns = [
        _("Item") + ":Link/Item:100",
        _("Item Name") + "::150",
        _("Description") + "::300",
        _("Cost Center") + ":Link/Cost Center:250",
        _("Total Amount") + ":Currency:100"
    ]

    return columns