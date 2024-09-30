// material_management/static/src/js/pos_customizations.js
odoo.define('material_management.pos_customizations', function(require){
    "use strict";

    var screens = require('point_of_sale.screens');
    var models = require('point_of_sale.models');
    var PosDB = require('point_of_sale.DB');
    var core = require('web.core');
    var QWeb = core.qweb;

    // 1. Disable Price and Discount Buttons
    screens.ProductScreenWidget.include({
        renderElement: function() {
            this._super();
            this.$('.mode-button[data-mode="price"], .mode-button[data-mode="discount"]').hide();
        }
    });

    // 2. Change +10, +20, +50 to +10,000, +50,000, +100,000
    screens.NumpadWidget.include({
        renderElement: function() {
            this._super();
            this.$('.input-button[data-id="1"]').text('+10,000');
            this.$('.input-button[data-id="2"]').text('+50,000');
            this.$('.input-button[data-id="3"]').text('+100,000');
        }
    });

    // 3. Send Email Receipt Automatically
    var OrderSuper = models.Order;
    models.Order = models.Order.extend({
        finalize: function(){
            OrderSuper.prototype.finalize.apply(this, arguments);
            var self = this;
            var client = this.get_client();
            if (client && client.email) {
                this.pos._send_receipt_by_email(this, client.email).then(function(){
                    self.pos.gui.show_popup('confirm', {
                        'title': 'Email sent',
                        'body': 'Email sudah dikirim / Email sent',
                    });
                }).catch(function(){
                    self.pos.gui.show_popup('error', {
                        'title': 'Error',
                        'body': 'Gagal mengirim email',
                    });
                });
            }
        },
    });

    // Tambahkan method untuk mengirim email
    models.PosModel = models.PosModel.extend({
        _send_receipt_by_email: function(order, email){
            return this.rpc({
                model: 'pos.order',
                method: 'send_receipt_email',
                args: [order.id, email],
            });
        },
    });
});
