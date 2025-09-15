from pprint import pprint

class TestCase:
    def __init__(self):
        # по условию: пустой словарь шагов и None в expected result
        self.steps: dict[int, str] = {}
        self.result: str | None = None

    def set_step(self, step_number: int, step_text: str) -> None:
        # добавляем/перезаписываем шаг
        if not isinstance(step_number, int) or step_number <= 0:
            raise ValueError("step_number должен быть положительным целым")
        self.steps[step_number] = step_text

    def delete_step(self, step_number: int) -> None:
        # удаляем, не падая, если шага нет
        self.steps.pop(step_number, None)

    def set_result(self, result: str) -> None:
        self.result = result

    def get_test_case(self) -> None:
        # печать в формате из задания
        data = {
            'Шаги': dict(sorted(self.steps.items())),   # чтобы шли по номеру
            'Ожидаемый результат': self.result
        }
        pprint(data, width=100, sort_dicts=False)

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()