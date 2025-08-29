# Models

Detected core models and extensions in account.

```mermaid
classDiagram
    class account_account
    class account_account_tag
    class account_account_template
    class account_bank_statement
    class account_bank_statement_line
    class account_cash_rounding
    class account_chart_template
    class account_fiscal_position
    class account_fiscal_position_account
    class account_fiscal_position_account_template
    class account_fiscal_position_tax
    class account_fiscal_position_tax_template
    class account_fiscal_position_template
    class account_full_reconcile
    class account_group
    class account_group_template
    class account_incoterms
    class account_journal
    class account_journal_group
    class account_move
    class account_move_line
    class account_partial_reconcile
    class account_payment
    class account_payment_method
    class account_payment_method_line
    class account_payment_term
    class account_payment_term_line
    class account_reconcile_model
    class account_reconcile_model_line
    class account_reconcile_model_line_template
    class account_reconcile_model_partner_mapping
    class account_reconcile_model_template
    class account_report
    class account_report_column
    class account_report_expression
    class account_report_external_value
    class account_report_line
    class account_root
    class account_tax
    class account_tax_group
    class account_tax_repartition_line
    class account_tax_repartition_line_template
    class account_tax_template
    class res_company
    class res_partner
    class res_partner_bank
    class sequence_mixin
    class account_analytic_account
    class account_analytic_applicability
    class account_analytic_distribution_model
    class account_analytic_line
    class account_journal
    class account_move_line
    class analytic_mixin
    class decimal_precision
    class digest_digest
    class ir_actions_report
    class ir_attachment
    class mail_thread
    class product_category
    class product_product
    class product_template
    class res_config_settings
    class res_currency
    class res_groups
    class res_partner
    class res_users
    class account_journal
    res_partner_bank --> account_journal : journal_id (One2many)
    class account_group_template
    account_group_template --> account_group_template : parent_id (Many2one)
    class account_chart_template
    account_group_template --> account_chart_template : chart_template_id (Many2one)
    class res_currency
    account_account_template --> res_currency : currency_id (Many2one)
    class account_tax_template
    account_account_template --> account_tax_template : tax_ids (Many2many)
    class account_chart_template
    account_account_template --> account_chart_template : chart_template_id (Many2one)
    class account_account_tag
    account_account_template --> account_account_tag : tag_ids (Many2many)
    class account_chart_template
    account_chart_template --> account_chart_template : parent_id (Many2one)
    class res_currency
    account_chart_template --> res_currency : currency_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : account_ids (One2many)
    class account_tax_template
    account_chart_template --> account_tax_template : tax_template_ids (One2many)
    class account_account_template
    account_chart_template --> account_account_template : income_currency_exchange_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : expense_currency_exchange_account_id (Many2one)
    class res_country
    account_chart_template --> res_country : country_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : account_journal_suspense_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : account_journal_payment_debit_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : account_journal_payment_credit_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : default_cash_difference_income_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : default_cash_difference_expense_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : default_pos_receivable_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : account_journal_early_pay_discount_loss_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : account_journal_early_pay_discount_gain_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_account_receivable_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_account_payable_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_account_expense_categ_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_account_income_categ_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_account_expense_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_account_income_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_stock_account_input_categ_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_stock_account_output_categ_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_stock_valuation_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_tax_payable_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_tax_receivable_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_advance_tax_payment_account_id (Many2one)
    class account_account_template
    account_chart_template --> account_account_template : property_cash_basis_base_account_id (Many2one)
    class account_chart_template
    account_tax_template --> account_chart_template : chart_template_id (Many2one)
    class account_tax_template
    account_tax_template --> account_tax_template : children_tax_ids (Many2many)
    class account_tax_repartition_line_template
    account_tax_template --> account_tax_repartition_line_template : invoice_repartition_line_ids (One2many)
    class account_tax_repartition_line_template
    account_tax_template --> account_tax_repartition_line_template : refund_repartition_line_ids (One2many)
    class account_tax_group
    account_tax_template --> account_tax_group : tax_group_id (Many2one)
    class account_account_template
    account_tax_template --> account_account_template : cash_basis_transition_account_id (Many2one)
    class account_account_template
    account_tax_repartition_line_template --> account_account_template : account_id (Many2one)
    class account_tax_template
    account_tax_repartition_line_template --> account_tax_template : invoice_tax_id (Many2one)
    class account_tax_template
    account_tax_repartition_line_template --> account_tax_template : refund_tax_id (Many2one)
    class account_account_tag
    account_tax_repartition_line_template --> account_account_tag : tag_ids (Many2many)
    class account_report_expression
    account_tax_repartition_line_template --> account_report_expression : plus_report_expression_ids (Many2many)
    class account_report_expression
    account_tax_repartition_line_template --> account_report_expression : minus_report_expression_ids (Many2many)
    class account_chart_template
    account_fiscal_position_template --> account_chart_template : chart_template_id (Many2one)
    class account_fiscal_position_account_template
    account_fiscal_position_template --> account_fiscal_position_account_template : account_ids (One2many)
    class account_fiscal_position_tax_template
    account_fiscal_position_template --> account_fiscal_position_tax_template : tax_ids (One2many)
    class res_country
    account_fiscal_position_template --> res_country : country_id (Many2one)
    class res_country_group
    account_fiscal_position_template --> res_country_group : country_group_id (Many2one)
    class res_country_state
    account_fiscal_position_template --> res_country_state : state_ids (Many2many)
    class account_fiscal_position_template
    account_fiscal_position_tax_template --> account_fiscal_position_template : position_id (Many2one)
    class account_tax_template
    account_fiscal_position_tax_template --> account_tax_template : tax_src_id (Many2one)
    class account_tax_template
    account_fiscal_position_tax_template --> account_tax_template : tax_dest_id (Many2one)
    class account_fiscal_position_template
    account_fiscal_position_account_template --> account_fiscal_position_template : position_id (Many2one)
    class account_account_template
    account_fiscal_position_account_template --> account_account_template : account_src_id (Many2one)
    class account_account_template
    account_fiscal_position_account_template --> account_account_template : account_dest_id (Many2one)
    class account_chart_template
    account_reconcile_model_template --> account_chart_template : chart_template_id (Many2one)
    class account_journal
    account_reconcile_model_template --> account_journal : match_journal_ids (Many2many)
    class res_partner
    account_reconcile_model_template --> res_partner : match_partner_ids (Many2many)
    class res_partner_category
    account_reconcile_model_template --> res_partner_category : match_partner_category_ids (Many2many)
    class account_reconcile_model_line_template
    account_reconcile_model_template --> account_reconcile_model_line_template : line_ids (One2many)
    class account_reconcile_model_template
    account_reconcile_model_line_template --> account_reconcile_model_template : model_id (Many2one)
    class account_account_template
    account_reconcile_model_line_template --> account_account_template : account_id (Many2one)
    class account_tax_template
    account_reconcile_model_line_template --> account_tax_template : tax_ids (Many2many)
    class account_reconcile_model
    account_reconcile_model_partner_mapping --> account_reconcile_model : model_id (Many2one)
    class res_partner
    account_reconcile_model_partner_mapping --> res_partner : partner_id (Many2one)
    class account_reconcile_model
    account_reconcile_model_line --> account_reconcile_model : model_id (Many2one)
    class account_account
    account_reconcile_model_line --> account_account : account_id (Many2one)
    class account_journal
    account_reconcile_model_line --> account_journal : journal_id (Many2one)
    class account_tax
    account_reconcile_model_line --> account_tax : tax_ids (Many2many)
    class res_company
    account_reconcile_model --> res_company : company_id (Many2one)
    class account_journal
    account_reconcile_model --> account_journal : match_journal_ids (Many2many)
    class res_partner
    account_reconcile_model --> res_partner : match_partner_ids (Many2many)
    class res_partner_category
    account_reconcile_model --> res_partner_category : match_partner_category_ids (Many2many)
    class account_reconcile_model_line
    account_reconcile_model --> account_reconcile_model_line : line_ids (One2many)
    class account_reconcile_model_partner_mapping
    account_reconcile_model --> account_reconcile_model_partner_mapping : partner_mapping_line_ids (One2many)
    class account_move
    account_payment --> account_move : move_id (Many2one)
    class res_partner_bank
    account_payment --> res_partner_bank : available_partner_bank_ids (Many2many)
    class res_partner_bank
    account_payment --> res_partner_bank : partner_bank_id (Many2one)
    class account_payment
    account_payment --> account_payment : paired_internal_transfer_payment_id (Many2one)
    class account_payment_method_line
    account_payment --> account_payment_method_line : payment_method_line_id (Many2one)
    class account_payment_method_line
    account_payment --> account_payment_method_line : available_payment_method_line_ids (Many2many)
    class account_journal
    account_payment --> account_journal : available_journal_ids (Many2many)
    class res_currency
    account_payment --> res_currency : currency_id (Many2one)
    class res_partner
    account_payment --> res_partner : partner_id (Many2one)
    class account_account
    account_payment --> account_account : outstanding_account_id (Many2one)
    class account_account
    account_payment --> account_account : destination_account_id (Many2one)
    class account_journal
    account_payment --> account_journal : destination_journal_id (Many2one)
    class account_move
    account_payment --> account_move : reconciled_invoice_ids (Many2many)
    class account_move
    account_payment --> account_move : reconciled_bill_ids (Many2many)
    class account_bank_statement_line
    account_payment --> account_bank_statement_line : reconciled_statement_line_ids (Many2many)
    class account_payment
    account_move --> account_payment : payment_ids (One2many)
    class res_country
    account_account_tag --> res_country : country_id (Many2one)
    class product_category
    account_analytic_applicability --> product_category : product_categ_id (Many2one)
    class product_product
    account_analytic_line --> product_product : product_id (Many2one)
    class account_account
    account_analytic_line --> account_account : general_account_id (Many2one)
    class account_journal
    account_analytic_line --> account_journal : journal_id (Many2one)
    class account_move_line
    account_analytic_line --> account_move_line : move_line_id (Many2one)
    class account_move
    account_bank_statement_line --> account_move : move_id (Many2one)
    class account_bank_statement
    account_bank_statement_line --> account_bank_statement : statement_id (Many2one)
    class account_payment
    account_bank_statement_line --> account_payment : payment_ids (Many2many)
    class res_partner
    account_bank_statement_line --> res_partner : partner_id (Many2one)
    class res_currency
    account_bank_statement_line --> res_currency : currency_id (Many2one)
    class res_currency
    account_bank_statement_line --> res_currency : foreign_currency_id (Many2one)
    class account_bank_statement_line
    account_move --> account_bank_statement_line : statement_line_ids (One2many)
    class res_currency
    account_account --> res_currency : currency_id (Many2one)
    class account_tax
    account_account --> account_tax : tax_ids (Many2many)
    class res_company
    account_account --> res_company : company_id (Many2one)
    class account_account_tag
    account_account --> account_account_tag : tag_ids (Many2many)
    class account_group
    account_account --> account_group : group_id (Many2one)
    class account_root
    account_account --> account_root : root_id (Many2one)
    class account_journal
    account_account --> account_journal : allowed_journal_ids (Many2many)
    class account_group
    account_group --> account_group : parent_id (Many2one)
    class res_company
    account_group --> res_company : company_id (Many2one)
    class account_root
    account_root --> account_root : parent_id (Many2one)
    class res_company
    account_root --> res_company : company_id (Many2one)
    class res_company
    account_fiscal_position --> res_company : company_id (Many2one)
    class account_fiscal_position_account
    account_fiscal_position --> account_fiscal_position_account : account_ids (One2many)
    class account_fiscal_position_tax
    account_fiscal_position --> account_fiscal_position_tax : tax_ids (One2many)
    class res_country
    account_fiscal_position --> res_country : country_id (Many2one)
    class res_country_group
    account_fiscal_position --> res_country_group : country_group_id (Many2one)
    class res_country_state
    account_fiscal_position --> res_country_state : state_ids (Many2many)
    class account_fiscal_position
    account_fiscal_position_tax --> account_fiscal_position : position_id (Many2one)
    class res_company
    account_fiscal_position_tax --> res_company : company_id (Many2one)
    class account_tax
    account_fiscal_position_tax --> account_tax : tax_src_id (Many2one)
    class account_tax
    account_fiscal_position_tax --> account_tax : tax_dest_id (Many2one)
    class account_fiscal_position
    account_fiscal_position_account --> account_fiscal_position : position_id (Many2one)
    class res_company
    account_fiscal_position_account --> res_company : company_id (Many2one)
    class account_account
    account_fiscal_position_account --> account_account : account_src_id (Many2one)
    class account_account
    account_fiscal_position_account --> account_account : account_dest_id (Many2one)
    class res_currency
    res_partner --> res_currency : currency_id (Many2one)
    class account_account
    res_partner --> account_account : property_account_payable_id (Many2one)
    class account_account
    res_partner --> account_account : property_account_receivable_id (Many2one)
    class account_fiscal_position
    res_partner --> account_fiscal_position : property_account_position_id (Many2one)
    class account_payment_term
    res_partner --> account_payment_term : property_payment_term_id (Many2one)
    class account_payment_term
    res_partner --> account_payment_term : property_supplier_payment_term_id (Many2one)
    class res_company
    res_partner --> res_company : ref_company_ids (One2many)
    class account_move
    res_partner --> account_move : invoice_ids (One2many)
    class account_analytic_account
    res_partner --> account_analytic_account : contract_ids (One2many)
    class res_company
    account_bank_statement --> res_company : company_id (Many2one)
    class res_currency
    account_bank_statement --> res_currency : currency_id (Many2one)
    class account_journal
    account_bank_statement --> account_journal : journal_id (Many2one)
    class account_bank_statement_line
    account_bank_statement --> account_bank_statement_line : line_ids (One2many)
    class ir_attachment
    account_bank_statement --> ir_attachment : attachment_ids (Many2many)
    class product_product
    account_analytic_distribution_model --> product_product : product_id (Many2one)
    class product_category
    account_analytic_distribution_model --> product_category : product_categ_id (Many2one)
    class account_account
    product_category --> account_account : property_account_income_categ_id (Many2one)
    class account_account
    product_category --> account_account : property_account_expense_categ_id (Many2one)
    class account_tax
    product_template --> account_tax : taxes_id (Many2many)
    class account_tax
    product_template --> account_tax : supplier_taxes_id (Many2many)
    class account_account
    product_template --> account_account : property_account_income_id (Many2one)
    class account_account
    product_template --> account_account : property_account_expense_id (Many2one)
    class account_account_tag
    product_template --> account_account_tag : account_tag_ids (Many2many)
    class account_payment_method
    account_payment_method_line --> account_payment_method : payment_method_id (Many2one)
    class account_account
    account_payment_method_line --> account_account : payment_account_id (Many2one)
    class account_journal
    account_payment_method_line --> account_journal : journal_id (Many2one)
    class account_report_line
    account_report --> account_report_line : line_ids (One2many)
    class account_report_column
    account_report --> account_report_column : column_ids (One2many)
    class account_report
    account_report --> account_report : root_report_id (Many2one)
    class account_report
    account_report --> account_report : variant_report_ids (One2many)
    class account_chart_template
    account_report --> account_chart_template : chart_template_id (Many2one)
    class res_country
    account_report --> res_country : country_id (Many2one)
    class account_report_expression
    account_report_line --> account_report_expression : expression_ids (One2many)
    class account_report
    account_report_line --> account_report : report_id (Many2one)
    class account_report_line
    account_report_line --> account_report_line : parent_id (Many2one)
    class account_report_line
    account_report_line --> account_report_line : children_ids (One2many)
    class ir_actions_actions
    account_report_line --> ir_actions_actions : action_id (Many2one)
    class account_report_line
    account_report_expression --> account_report_line : report_line_id (Many2one)
    class account_report
    account_report_column --> account_report : report_id (Many2one)
    class ir_actions_act_window
    account_report_column --> ir_actions_act_window : custom_audit_action_id (Many2one)
    class account_report_expression
    account_report_external_value --> account_report_expression : target_report_expression_id (Many2one)
    class res_company
    account_report_external_value --> res_company : company_id (Many2one)
    class account_fiscal_position
    account_report_external_value --> account_fiscal_position : foreign_vat_fiscal_position_id (Many2one)
    class account_report_line
    account_report_external_value --> account_report_line : carryover_origin_report_line_id (Many2one)
    class account_payment_term_line
    account_payment_term --> account_payment_term_line : line_ids (One2many)
    class res_company
    account_payment_term --> res_company : company_id (Many2one)
    class account_payment_term
    account_payment_term_line --> account_payment_term : payment_id (Many2one)
    class account_account
    account_cash_rounding --> account_account : profit_account_id (Many2one)
    class account_account
    account_cash_rounding --> account_account : loss_account_id (Many2one)
    class res_company
    account_cash_rounding --> res_company : company_id (Many2one)
    class account_move
    account_move_line --> account_move : move_id (Many2one)
    class account_account
    account_move_line --> account_account : account_id (Many2one)
    class res_currency
    account_move_line --> res_currency : currency_id (Many2one)
    class res_partner
    account_move_line --> res_partner : partner_id (Many2one)
    class account_reconcile_model
    account_move_line --> account_reconcile_model : reconcile_model_id (Many2one)
    class account_payment
    account_move_line --> account_payment : payment_id (Many2one)
    class account_bank_statement_line
    account_move_line --> account_bank_statement_line : statement_line_id (Many2one)
    class account_tax
    account_move_line --> account_tax : tax_ids (Many2many)
    class account_tax
    account_move_line --> account_tax : group_tax_id (Many2one)
    class account_tax
    account_move_line --> account_tax : tax_line_id (Many2one)
    class account_tax_repartition_line
    account_move_line --> account_tax_repartition_line : tax_repartition_line_id (Many2one)
    class account_account_tag
    account_move_line --> account_account_tag : tax_tag_ids (Many2many)
    class account_full_reconcile
    account_move_line --> account_full_reconcile : full_reconcile_id (Many2one)
    class account_partial_reconcile
    account_move_line --> account_partial_reconcile : matched_debit_ids (One2many)
    class account_partial_reconcile
    account_move_line --> account_partial_reconcile : matched_credit_ids (One2many)
    class product_product
    account_move_line --> product_product : product_id (Many2one)
    class uom_uom
    account_move_line --> uom_uom : product_uom_id (Many2one)
    class uom_category
    account_move_line --> uom_category : product_uom_category_id (Many2one)
    class account_analytic_line
    account_move_line --> account_analytic_line : analytic_line_ids (One2many)
    class account_account
    account_tax_group --> account_account : property_tax_payable_account_id (Many2one)
    class account_account
    account_tax_group --> account_account : property_tax_receivable_account_id (Many2one)
    class account_account
    account_tax_group --> account_account : property_advance_tax_payment_account_id (Many2one)
    class res_country
    account_tax_group --> res_country : country_id (Many2one)
    class res_company
    account_tax --> res_company : company_id (Many2one)
    class account_tax
    account_tax --> account_tax : children_tax_ids (Many2many)
    class account_tax_group
    account_tax --> account_tax_group : tax_group_id (Many2one)
    class account_account
    account_tax --> account_account : cash_basis_transition_account_id (Many2one)
    class account_tax_repartition_line
    account_tax --> account_tax_repartition_line : invoice_repartition_line_ids (One2many)
    class account_tax_repartition_line
    account_tax --> account_tax_repartition_line : refund_repartition_line_ids (One2many)
    class res_country
    account_tax --> res_country : country_id (Many2one)
    class account_account
    account_tax_repartition_line --> account_account : account_id (Many2one)
    class account_account_tag
    account_tax_repartition_line --> account_account_tag : tag_ids (Many2many)
    class account_tax
    account_tax_repartition_line --> account_tax : invoice_tax_id (Many2one)
    class account_tax
    account_tax_repartition_line --> account_tax : refund_tax_id (Many2one)
    class account_tax
    account_tax_repartition_line --> account_tax : tax_id (Many2one)
    class res_company
    account_tax_repartition_line --> res_company : company_id (Many2one)
    class account_account
    res_company --> account_account : transfer_account_id (Many2one)
    class account_chart_template
    res_company --> account_chart_template : chart_template_id (Many2one)
    class account_account
    res_company --> account_account : default_cash_difference_income_account_id (Many2one)
    class account_account
    res_company --> account_account : default_cash_difference_expense_account_id (Many2one)
    class account_account
    res_company --> account_account : account_journal_suspense_account_id (Many2one)
    class account_account
    res_company --> account_account : account_journal_payment_debit_account_id (Many2one)
    class account_account
    res_company --> account_account : account_journal_payment_credit_account_id (Many2one)
    class account_account
    res_company --> account_account : account_journal_early_pay_discount_gain_account_id (Many2one)
    class account_account
    res_company --> account_account : account_journal_early_pay_discount_loss_account_id (Many2one)
    class account_tax
    res_company --> account_tax : account_sale_tax_id (Many2one)
    class account_tax
    res_company --> account_tax : account_purchase_tax_id (Many2one)
    class account_journal
    res_company --> account_journal : currency_exchange_journal_id (Many2one)
    class account_account
    res_company --> account_account : income_currency_exchange_account_id (Many2one)
    class account_account
    res_company --> account_account : expense_currency_exchange_account_id (Many2one)
    class account_account
    res_company --> account_account : property_stock_account_input_categ_id (Many2one)
    class account_account
    res_company --> account_account : property_stock_account_output_categ_id (Many2one)
    class account_account
    res_company --> account_account : property_stock_valuation_account_id (Many2one)
    class account_journal
    res_company --> account_journal : bank_journal_ids (One2many)
    class account_incoterms
    res_company --> account_incoterms : incoterm_id (Many2one)
    class account_move
    res_company --> account_move : account_opening_move_id (Many2one)
    class account_journal
    res_company --> account_journal : account_opening_journal_id (Many2one)
    class account_account
    res_company --> account_account : account_default_pos_receivable_account_id (Many2one)
    class account_account
    res_company --> account_account : expense_accrual_account_id (Many2one)
    class account_account
    res_company --> account_account : revenue_accrual_account_id (Many2one)
    class account_journal
    res_company --> account_journal : automatic_entry_default_journal_id (Many2one)
    class res_country
    res_company --> res_country : account_fiscal_country_id (Many2one)
    class res_country
    res_company --> res_country : account_enabled_tax_country_ids (Many2many)
    class account_journal
    res_company --> account_journal : tax_cash_basis_journal_id (Many2one)
    class account_account
    res_company --> account_account : account_cash_basis_base_account_id (Many2one)
    class account_fiscal_position
    res_company --> account_fiscal_position : fiscal_position_ids (One2many)
    class res_country
    res_company --> res_country : multi_vat_foreign_country_ids (Many2many)
    class res_company
    account_journal_group --> res_company : company_id (Many2one)
    class account_journal
    account_journal_group --> account_journal : excluded_journal_ids (Many2many)
    class account_account
    account_journal --> account_account : account_control_ids (Many2many)
    class account_account
    account_journal --> account_account : default_account_id (Many2one)
    class account_account
    account_journal --> account_account : suspense_account_id (Many2one)
    class res_currency
    account_journal --> res_currency : currency_id (Many2one)
    class res_company
    account_journal --> res_company : company_id (Many2one)
    class account_payment_method_line
    account_journal --> account_payment_method_line : inbound_payment_method_line_ids (One2many)
    class account_payment_method_line
    account_journal --> account_payment_method_line : outbound_payment_method_line_ids (One2many)
    class account_account
    account_journal --> account_account : profit_account_id (Many2one)
    class account_account
    account_journal --> account_account : loss_account_id (Many2one)
    class res_partner
    account_journal --> res_partner : company_partner_id (Many2one)
    class res_partner_bank
    account_journal --> res_partner_bank : bank_account_id (Many2one)
    class res_bank
    account_journal --> res_bank : bank_id (Many2one)
    class mail_activity_type
    account_journal --> mail_activity_type : sale_activity_type_id (Many2one)
    class res_users
    account_journal --> res_users : sale_activity_user_id (Many2one)
    class mail_alias
    account_journal --> mail_alias : alias_id (Many2one)
    class account_journal_group
    account_journal --> account_journal_group : journal_group_ids (Many2many)
    class ir_sequence
    account_journal --> ir_sequence : secure_sequence_id (Many2one)
    class account_payment_method
    account_journal --> account_payment_method : available_payment_method_ids (Many2many)
    class res_currency
    res_config_settings --> res_currency : currency_id (Many2one)
    class account_journal
    res_config_settings --> account_journal : currency_exchange_journal_id (Many2one)
    class account_account
    res_config_settings --> account_account : income_currency_exchange_account_id (Many2one)
    class account_account
    res_config_settings --> account_account : expense_currency_exchange_account_id (Many2one)
    class account_chart_template
    res_config_settings --> account_chart_template : chart_template_id (Many2one)
    class account_tax
    res_config_settings --> account_tax : sale_tax_id (Many2one)
    class account_tax
    res_config_settings --> account_tax : purchase_tax_id (Many2one)
    class account_account
    res_config_settings --> account_account : account_journal_suspense_account_id (Many2one)
    class account_account
    res_config_settings --> account_account : account_journal_payment_debit_account_id (Many2one)
    class account_account
    res_config_settings --> account_account : account_journal_payment_credit_account_id (Many2one)
    class account_account
    res_config_settings --> account_account : transfer_account_id (Many2one)
    class account_journal
    res_config_settings --> account_journal : tax_cash_basis_journal_id (Many2one)
    class account_account
    res_config_settings --> account_account : account_cash_basis_base_account_id (Many2one)
    class account_incoterms
    res_config_settings --> account_incoterms : incoterm_id (Many2one)
    class account_account
    res_config_settings --> account_account : account_journal_early_pay_discount_loss_account_id (Many2one)
    class account_account
    res_config_settings --> account_account : account_journal_early_pay_discount_gain_account_id (Many2one)
    class account_partial_reconcile
    account_full_reconcile --> account_partial_reconcile : partial_reconcile_ids (One2many)
    class account_move_line
    account_full_reconcile --> account_move_line : reconciled_line_ids (One2many)
    class account_move
    account_full_reconcile --> account_move : exchange_move_id (Many2one)
    class account_move_line
    account_partial_reconcile --> account_move_line : debit_move_id (Many2one)
    class account_move_line
    account_partial_reconcile --> account_move_line : credit_move_id (Many2one)
    class account_full_reconcile
    account_partial_reconcile --> account_full_reconcile : full_reconcile_id (Many2one)
    class account_move
    account_partial_reconcile --> account_move : exchange_move_id (Many2one)
    class res_currency
    account_partial_reconcile --> res_currency : company_currency_id (Many2one)
    class res_currency
    account_partial_reconcile --> res_currency : debit_currency_id (Many2one)
    class res_currency
    account_partial_reconcile --> res_currency : credit_currency_id (Many2one)
    class res_company
    account_partial_reconcile --> res_company : company_id (Many2one)
    class account_journal
    account_move --> account_journal : journal_id (Many2one)
    class res_company
    account_move --> res_company : company_id (Many2one)
    class account_move_line
    account_move --> account_move_line : line_ids (One2many)
    class account_payment
    account_move --> account_payment : payment_id (Many2one)
    class account_bank_statement_line
    account_move --> account_bank_statement_line : statement_line_id (Many2one)
    class account_partial_reconcile
    account_move --> account_partial_reconcile : tax_cash_basis_rec_id (Many2one)
    class account_move
    account_move --> account_move : tax_cash_basis_origin_move_id (Many2one)
    class account_move
    account_move --> account_move : tax_cash_basis_created_move_ids (One2many)
    class account_move
    account_move --> account_move : auto_post_origin_id (Many2one)
    class account_journal
    account_move --> account_journal : suitable_journal_ids (Many2many)
    class ir_attachment
    account_move --> ir_attachment : attachment_ids (One2many)
    class account_move_line
    account_move --> account_move_line : invoice_line_ids (One2many)
    class account_payment_term
    account_move --> account_payment_term : invoice_payment_term_id (Many2one)
    class res_partner
    account_move --> res_partner : partner_id (Many2one)
    class res_partner
    account_move --> res_partner : commercial_partner_id (Many2one)
    class res_partner
    account_move --> res_partner : partner_shipping_id (Many2one)
    class res_partner_bank
    account_move --> res_partner_bank : partner_bank_id (Many2one)
    class account_fiscal_position
    account_move --> account_fiscal_position : fiscal_position_id (Many2one)
    class res_currency
    account_move --> res_currency : currency_id (Many2one)
    class account_move
    account_move --> account_move : reversed_entry_id (Many2one)
    class account_move
    account_move --> account_move : reversal_move_id (One2many)
    class account_move
    account_move --> account_move : invoice_vendor_bill_id (Many2one)
    class res_users
    account_move --> res_users : invoice_user_id (Many2one)
    class account_incoterms
    account_move --> account_incoterms : invoice_incoterm_id (Many2one)
    class account_cash_rounding
    account_move --> account_cash_rounding : invoice_cash_rounding_id (Many2one)
    class res_partner
    account_move --> res_partner : bank_partner_id (Many2one)
    class res_country
    account_move --> res_country : tax_country_id (Many2one)
    class account_move
    account_move --> account_move : duplicated_ref_ids (Many2many)
```

Notes
- Classes show model technical names; fields omitted for brevity.
- Items listed under _inherit are extensions of existing models.
