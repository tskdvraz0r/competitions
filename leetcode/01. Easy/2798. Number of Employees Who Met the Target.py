def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
    return len([i for i in hours if i >= target])