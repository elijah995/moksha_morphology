# moksha_morphology

Обработка 1 файла объёмом около 1500 слов 

mokshen_pr-2009.05.28.txt - сам текст

mokshen_pr-2009.05.28.json - исходный файл разметки текста из корпуса

mokshen_pr-2009.05.28_formatted.json - конвертированный в UD-like формат разметки

mokshen_pr-2009.05.28_formatted_in_progress.json - частично обработанный (снята омонимия, добавлены тэги для части исходно неразобранных слов)


модули для обработки:

moksha_converting.py - конвертация из исходной разметки в UD-like формат

moksha_visualizing.py - визуализация UD-like разметки в виде conllu, интерфейс для выбора одного из вариантов разбора слова

moksha_preprocessing.py - обработка UD-like разметки (автоматическое снятие омонимии, автоматическое добавление недостающих разборов)


moksha_demo.ipynb - пример обработки исходного файла

