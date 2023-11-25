class Calculator:
    def __init__(self, num_list_1, num_list_2):
        self.num_list_1 = num_list_1
        self.num_list_2 = num_list_2

    def calculate_average(self, lst):
        if not lst:
            return 0
        return sum(lst) / len(lst)

    def compare_average(self):
        sum_1 = self.calculate_average(self.num_list_1)
        sum_2 = self.calculate_average(self.num_list_2)

        if sum_1 > sum_2:
            return 'Первый список имеет большее среднее значение'
        elif sum_1 < sum_2:
            return 'Второй список имеет большее среднее значение'
        else:
            return 'Средние значения равны'
