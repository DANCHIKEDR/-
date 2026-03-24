№ тест-кейса	Входные данные	Ожидаемый результат	Полученный результат
TC-001	42	Успешная обработка числа: original=42, absolute=42, square=1764, cube=74088, is_even=True, type='number'	 СОВПАДАЕТ: original=42, absolute=42, square=1764, cube=74088, is_even=True, type='number'
TC-002	-15.7	Успешная обработка числа: original=-15.7, absolute=15.7, square=246.49, cube=-3869.893, is_even=None, type='number'	 СОВПАДАЕТ: original=-15.7, absolute=15.7, square=246.49, cube=-3869.893, is_even=None, type='number'
TC-003	0	Успешная обработка числа: original=0, absolute=0, square=0, cube=0, is_even=True, type='number'	 СОВПАДАЕТ: original=0, absolute=0, square=0, cube=0, is_even=True, type='number'
TC-004	"Привет, мир!"	Успешная обработка текста: original="Привет, мир!", length=12, uppercase="ПРИВЕТ, МИР!", words_count=2, reversed="!рим ,тевирП", is_palindrome=False	 СОВПАДАЕТ: original="Привет, мир!", length=12, uppercase="ПРИВЕТ, МИР!", words_count=2, reversed="!рим ,тевирП", is_palindrome=False
TC-005	"А роза упала на лапу Азора"	Успешная обработка текста: original="А роза упала на лапу Азора", length=26, is_palindrome=True	 СОВПАДАЕТ: original="А роза упала на лапу Азора", length=26, is_palindrome=True
TC-006	"" (пустая строка)	Успешная обработка текста: original="", length=0, words_count=0, reversed=""	 СОВПАДАЕТ: original="", length=0, words_count=0, reversed=""
TC-007	[1, 2, 3, 4, 5]	Успешная обработка списка: length=5, unique_items=[1,2,3,4,5], sum=15, average=3.0, min=1, max=5	 СОВПАДАЕТ: length=5, unique_items=[1,2,3,4,5], sum=15, average=3.0, min=1, max=5
TC-008	[1, 2, 2, 3, 3, 3]	Успешная обработка списка: length=6, unique_items=[1,2,3], sum=14, average≈2.33	 СОВПАДАЕТ: length=6, unique_items=[1,2,3], sum=14, average=2.3333333333333335
TC-009	[] (пустой список)	Успешная обработка списка: length=0, unique_items=[], sum=0, average=0	 СОВПАДАЕТ: length=0, unique_items=[], sum=0, average=0
TC-010	[1, "текст", 3.5]	Успешная обработка смешанного списка: length=3, без числовой статистики (sum=None)	 СОВПАДАЕТ: length=3, unique_items=[1, 3.5, "текст"], sorted=None, числовая статистика отсутствует
TC-011	True	Успешная обработка логического значения: original=True, as_int=1, as_str="True", negated=False	 СОВПАДАЕТ: original=True, as_int=1, as_str="True", negated=False, type='boolean'
TC-012	False	Успешная обработка логического значения: original=False, as_int=0, as_str="False", negated=True	 СОВПАДАЕТ: original=False, as_int=0, as_str="False", negated=True, type='boolean'
TC-013	"true" (строка)	Успешная обработка как текст: type='text', а не boolean	 СОВПАДАЕТ: обработано как текст, type='text', original="true", length=4, uppercase="TRUE"
TC-014	"123" (строка-число)	Успешная обработка как текст или число в зависимости от логики	 СОВПАДАЕТ (как текст): обработано как текст, type='text', original="123", length=3
TC-015	None	Ошибка: неподдерживаемый тип данных	 СОВПАДАЕТ: возвращен error: 'Неподдерживаемый тип данных: <class 'NoneType'>', type='error'
TC-016	{"ключ": "значение"}	Ошибка: неподдерживаемый тип данных	 СОВПАДАЕТ: возвращен error: 'Неподдерживаемый тип данных: <class 'dict'>', type='error'
TC-017	(1, 2, 3)	Ошибка: неподдерживаемый тип данных	 СОВПАДАЕТ: возвращен error: 'Неподдерживаемый тип данных: <class 'tuple'>', type='error'
TC-018	"exit" (команда)	Выход из программы без обработки данных	 СОВПАДАЕТ: программа завершает работу, данные не обрабатываются
TC-019	"history" (команда)	Вывод истории обработанных данных	 СОВПАДАЕТ: выводится список всех ранее обработанных данных
TC-020	"clear" (команда)	Очистка истории, сообщение об успешной очистке	 СОВПАДАЕТ: история очищена, выводится сообщение "История очищена"
