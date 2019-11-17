# Copyright (c) 2013, masonarmani38@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Sales Person: Link/Sales Person200", "Item:Link/Item:200","Item Name:Data:200","Qty:Float:200","Amount:Currency:200"], []

	item=""
	customer=""
	territory=""

	if filters.get("item"):
		item = """ and soi.item_code = '{}' """.format(filters.get("item"))

	if filters.get("sales"):
		customer = """ and st.sales_person = '{}' """.format(filters.get("sales"))

	if filters.get("territory"):
		territory = """ and so.territory = '{}' """.format(filters.get("territory"))

	data = frappe.db.sql("""select st.sales_person, soi.item_code,soi.item_name,sum(soi.qty),sum(soi.amount) from `tabSales Invoice Item` soi 
		join `tabSales Invoice` so on soi.parent=so.name 
		join `tabCustomer` c on c.name = so.customer
		join `tabSales Team` st on c.name = st.parent 
		where so.docstatus=1 and (so.posting_date between '{}' and '{}') {} {} {} group by soi.item_code""".format(filters.get("from"),filters.get("to"),item,customer,territory),as_list=1 )

	return columns, data
