class TestCase:

    def __init__(self):
        self.test_steps = []
        self.test_result = None

    def set_step(self, step, text):
        self.test_steps.append({'step': step, 'text': text})
    
    def delete_step(self, step):
        self.test_steps = [s for s in self.test_steps if s['step'] != step]


    def set_result(self, result):
        self.test_result = result

    def get_test_case(self):
        print("Шаги:") 
        for step in self.test_steps: 
            print(f"{step['step']}: {step['text']}") 
        print(f"Ожидаемый результат: {self.test_result}")    
        

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