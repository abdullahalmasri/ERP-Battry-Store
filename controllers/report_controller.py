from models.report import Report

class ReportController:
    def __init__(self):
        self.reports = []

    def generate_report(self, report):
        self.reports.append(report)

    def view_report(self, report_id):
        report = self.find_report_by_id(report_id)
        if report:
            return report.view_report()

    def find_report_by_id(self, report_id):
        for report in self.reports:
            if report.report_id == report_id:
                return report
        return None
