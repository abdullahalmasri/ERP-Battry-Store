from models.recycling_process import RecyclingProcess

class RecyclingController:
    def __init__(self):
        self.processes = [
            RecyclingProcess(1, 'BAT123', '2023-01-01', '2023-01-10', 'Completed'),
            RecyclingProcess(2, 'BAT456', '2023-02-01', '2023-02-15', 'In Progress'),
            RecyclingProcess(3, 'BAT789', '2023-03-01', '2023-03-10', 'Planned')
        ]

    def plan_process(self, process):
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
