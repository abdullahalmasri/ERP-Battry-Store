from models.remanufacturing_process import RemanufacturingProcess

class RemanufacturingController:
    def __init__(self):
        self.processes = [
            RemanufacturingProcess(1, 101, '2024-07-01', '2024-07-10', 'Scheduled'),
            RemanufacturingProcess(2, 102, '2024-07-05', '2024-07-15', 'In Progress'),
            RemanufacturingProcess(3, 103, '2024-06-20', '2024-07-05', 'Completed')
        ]

    def schedule_process(self, process):
        self.processes.append(process)

    def update_process(self, process):
        oldProcess = self.find_process_by_id(process.process_id)
        if oldProcess:
            oldProcess.battery_id = int(process.battery_id)
            oldProcess.start_date = process.start_date
            oldProcess.end_date = process.end_date
            oldProcess.status = process.status

    def find_process_by_id(self, process_id):
        for process in self.processes:
            if process.process_id == process_id:
                return process
        return None
