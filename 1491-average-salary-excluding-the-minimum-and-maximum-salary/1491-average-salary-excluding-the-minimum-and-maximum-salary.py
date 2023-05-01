
class Solution:
    def average(self, salary: List[int]) -> float:
        min_int = 9999999.00000
        max_int = -9999999.00000
        total_sum = 0
        
        for each in salary:
            total_sum += each
            if each < min_int:
                min_int = each
            if each > max_int:
                max_int = each
        
        total_sum -= min_int
        total_sum -= max_int
        
        lst_size = len(salary) - 2
        
        if lst_size > 0:
            avg = total_sum / lst_size
        else:
            avg = 0
        
        return avg
        