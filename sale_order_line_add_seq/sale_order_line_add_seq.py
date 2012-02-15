
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields
from tools.translate import _

#class sale_order_line(osv.osv):
#    
#    _inherit = 'sale.order.line'
#    _columns = {
#                'sequence': fields.integer('Sequence'),
#    }
#sale_order_line()

class account_invoice_line(osv.osv):
    
    _inherit = 'account.invoice.line'
    _columns = {
                'sequence': fields.integer('Sequence'),
    }
account_invoice_line()

class stock_move(osv.osv):
    
    _inherit = 'stock.move'
    _columns = {
                'sequence': fields.integer('Sequence'),
    }
stock_move()