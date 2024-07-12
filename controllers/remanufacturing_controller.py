from models.remanufacturing_process import RemanufacturingProcess

class RemanufacturingController:
    def __init__(self):
        self.processes = []

    def schedule_process(self, process):
        self.processes.append(process)

    def update_process_status(self, process_id, status):
        process = self.find_process_by_id(process_id)
        if process:
            process.status = status

    def find_process_by_id(self, process_id):
        for process in self.processes:
            if process.process_id == process_id:
                return process
        return None
