from models.quality_control import QualityControl


class QualityController:
    def __init__(self):
        self.qcc = [
            QualityControl(1, "B1001", "2024-07-10", "Pass", "None"),
            QualityControl(2, "B1002", "2024-07-11", "Fail", "Overheating issue detected"),
            QualityControl(3, "B1003", "2024-07-12", "Pass", "None")
        ]

    def perform_inspection(self, qc):
        self.qcc.append(qc)

    def update_inspection_results(self, qc_id, results, issues):
        qc = self.find_quality_control_by_id(qc_id)
        if qc:
            qc.results = results
            qc.issues = issues

    def find_quality_control_by_id(self, qc_id):
        for qc in self.qcc:
            if qc.qc_id == qc_id:
                return qc
        return None
