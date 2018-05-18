import importlib

import openpyxl
import openpyxl.styles
import openpyxl.writer.excel


class XLSXRenderer(object):
    XLSX_CONTENT_TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    def __init__(self, info):
        self.suffix = info.type
        self.templates_pkg = info.package.__name__ + ".xlsx"

    def __call__(self, value, system):
        templ_name = system["renderer_name"][:-len(self.suffix)]
        templ_module = importlib.import_module("." + templ_name, self.templates_pkg)
        wb = openpyxl.Workbook()
        ws = wb.active
        if "get_header" in dir(templ_module):
            ws.append(getattr(templ_module, "get_header")(system, value))
            ws.row_dimensions[1].font = openpyxl.styles.Font(bold=True)
        if "iterate_rows" in dir(templ_module):
            for row in getattr(templ_module, "iterate_rows")(system, value):
                ws.append(row)

        request = system.get('request')
        if not request is None:
            response = request.response
            ct = response.content_type
            if ct == response.default_content_type:
                response.content_type = XLSXRenderer.XLSX_CONTENT_TYPE
            response.content_disposition = 'attachment;filename=%s.xlsx' % templ_name

        return openpyxl.writer.excel.save_virtual_workbook(wb)
