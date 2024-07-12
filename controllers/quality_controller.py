from models.quality_control import QualityControl

class QualityController:
    def __init__(self):
        self.quality_controls = []

    def perform_inspection(self, qc):
        self.quality_controls.append(qc)

    def update_inspection_results(self, qc_id, results, issues):
        qc = self.find_quality_control_by_id(qc_id)
        if qc:
            qc.results = results
            qc.issues = issues

    def find_quality_control_by_id(self, qc_id):
        for qc in self.quality_controls:
            if qc.qc_id == qc_id:
                return qc
        return None
