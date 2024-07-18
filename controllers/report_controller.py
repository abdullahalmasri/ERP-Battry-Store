from models.report import Report


class ReportController:
    def __init__(self):
        self.reports = [
            Report(1, "Sales", "2023-07-17",
                   [{"total_sales": 10000, "region": "North America"}, {"total_sales": 2000, "region": "South America"},
                    {"total_sales": 1500, "region": "Middle America"}]),
            Report(2, "Inventory", "2023-07-18", {"total_items": 5000, "warehouse": "Warehouse A"}),
            Report(3, "Performance", "2023-07-19", {"employee_id": 123, "rating": "A"}),
        ]

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
