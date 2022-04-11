# coding: utf-8
{
    "name": "Modificaciones a Reportes PDF",
    "version": "1.0",
    "author": "Carlos A. Garcia",
    "category": "Reports",
    # "website": "http://www.*.mx",
    "summary": "Ajustes a reportes PDF",
    "depends": [
        "web",
        "sale",
        "account",
    ],
    "data": [
        "report/external_layout_standard.xml",
        "report/report_sale.xml",
        "report/report_invoice.xml",
    ],
    "installable": True,
    "auto_install": False,
}
