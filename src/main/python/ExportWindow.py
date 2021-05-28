import os
from datetime import datetime

from pandas import ExcelWriter
from PyQt5.QtWidgets import QFileDialog, QWidget

from ui.PyES4_dataExport import Ui_ExportWindow
from utils_func import adjustWidths, getColWidths


class ExportWindow(QWidget, Ui_ExportWindow):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)

        self.result = parent.result
        self.path = parent.project_path

        if self.path == None:
            self.project_name = "unknown"
        else:
            self.project_name = os.path.splitext(os.path.basename(self.path))[0]

        if "formation_constants" not in self.result:
            self.adjlogb_check_excel.setChecked(False)
            self.adjlogb_check_excel.setEnabled(False)
            self.adjlogb_check_csv.setChecked(False)
            self.adjlogb_check_csv.setEnabled(False)

    def ExcelExport(self):
        """
        Export results to an excel file.
        """
        export_path, _ = QFileDialog.getSaveFileName(
            self, "Pick a Path", "", "Excel (*.xlsx)"
        )

        if export_path:
            export_path = export_path.split(".")[0] + ".xlsx"

            with ExcelWriter(export_path) as writer:
                wb = writer.book

                if self.input_check_excel.isChecked():
                    self.result["species_info"].to_excel(
                        writer, sheet_name="System Info", startrow=3
                    )
                    self.result["comp_info"].to_excel(
                        writer,
                        sheet_name="System Info",
                        na_rep="---",
                        startrow=3,
                        startcol=(self.result["species_info"].shape[1] + 3),
                    )

                    ws = wb["System Info"]
                    ws["A1"] = "File:"
                    ws["A2"] = "Date:"
                    ws.merge_cells("B1:D1")
                    ws.merge_cells("B2:D2")
                    ws["B1"] = self.project_name
                    ws["B2"] = datetime.now()

                if self.distribution_check_excel.isChecked():
                    self.result["distribution"].to_excel(
                        writer, sheet_name="Species Distribution"
                    )

                    ws = wb["Species Distribution"]
                    dist_widths = getColWidths(self.result["distribution"])
                    adjustWidths(ws, dist_widths)

                if self.perc_check_excel.isChecked():
                    self.result["percentages"].to_excel(
                        writer, sheet_name="Percentages"
                    )

                    ws = wb["Percentages"]
                    perc_widths = getColWidths(self.result["percentages"])
                    adjustWidths(ws, perc_widths)

                if self.adjlogb_check_excel.isChecked():
                    self.result["formation_constants"].to_excel(
                        writer,
                        sheet_name="Adjusted Formation Constants",
                        float_format="%.3f",
                    )
                    ws = wb["Adjusted Formation Constants"]
                    logb_width = getColWidths(self.result["formation_constants"])
                    adjustWidths(ws, logb_width)

    def CsvExport(self):
        """
        Export results as csv files.
        """
        folder_path = QFileDialog.getExistingDirectory(self, "Select a Folder")

        if folder_path:
            base_name = os.path.join(folder_path, self.project_name)
            if self.input_check_csv.isChecked():
                self.result["species_info"].to_csv(base_name + "_species.csv")

                self.result["comp_info"].to_csv(base_name + "_comp.csv")

            if self.distribution_check_csv.isChecked():
                self.result["distribution"].to_csv(base_name + "_distribution.csv")

            if self.perc_check_csv.isChecked():
                self.result["percentages"].to_csv(base_name + "_percentages.csv")

            if self.adjlogb_check_csv.isChecked():
                self.result["formation_constants"].to_csv(base_name + "_logb.csv")
