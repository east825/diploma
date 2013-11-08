Рецензии на литературу
======================

[Brett Cannon][cannon] ["Localized type inference of atomic types in Python"][1]
--------------------------------------------------------------------------------

Дипломная работа [Brett Cannon](http://www.python.org/psf/records/board/history/#brett-cannon)
на тему локального вывода стандартных типов внутри функций. Цель работы
-- повысить быстродействие интерпреторора за счет добавления нескольких новых
инструкций в байт-код, позволяющих миновать процедуру поиска атрибутов
для некотороых стандартных типов и операторов (например, `STORE_SUBSCR` для вызова
`__setitem__` на словаре). Типы выводятся только для локальных переменных
внутри функций, для задания типов аргументов вводятся аннотации в
документирющих комментариях.

Несмотря на то, что досчтичь желаемого повышения быстродействия на >= 5%
автору не удалось, работа интересна по нескольким причинам:

* Имеется небольшой обзор и сравнение использующихся алгоритмов для вывода типов:
Hindley-Milner vs. Cartesian Product. В итоге, как и в других публикациях, для
анализа используется абстракная интерпретация, названная здесь *"iterative type
analysis"*.
* Неплохо расписан процесс вывода для стандарных операторов языка:
ветвелений, циклов и блоков `try/except/finally`.
* В разделе, посвященному тестированию системы, делаются инересные выводы на
счет совместимости примененного подхода и использования ООП в рассматриваемых
проектах: в методах вместо локальных переменных часто используются атрибуты
объекта, их типы никак не аннотруются и не выводятся, и это сводит на нет всю
пользу от остального анализа.
* Данны ссылки на другие интересные проекты и публиакации *(правда довольно
старые)*. Например, на [этот][starkiller]. Стоит взглянуть.


[Alexander Aiken][aiken], Brian R. Murphy ["Static type inference in dynamically typed language"][2]
---------------------------------------------------------------------------------------------------

В работе рассматривается алгоритм вывода типов в функциональном языке [FL][].
Также, как и в прочих работах, для вывода используется абстрактная
интерпретация. Отличием использованного решения является то, что сами типы
трактуются не как множество значений, а как *множество выражений*,
А для интерпретации используются, т.н. *type rewrite rules*.
Сделано это в частности для возможности сравнения типов функций.

Честно говоря, в силу того, что статья написана довольно сжато,
а также из-за обилия специфической математической нотации,
я не понял многие из приведенных правил для вывода.
У авторов есть другие публикации, возможно помогут разобраться в этой.


Alex Holkner, James Harland ["Evaluating the dynamic behaviour of Python applications"][3]
------------------------------------------------------------------------------------------

Работа посвящена исследованию частоты использованию использования
возможностей метапрограммирования в проектах на Python. Предпосылкой для
работы является предположение, что в большинстве программ на Python
возможности вроде добавления атрибутов объектам и классам после их создания,
модификации глобального простраства имен модуля или `exec/eval`
используются только на начальном этапе исполнения, после чего программы ведут
себя во многом идентично приложениям на статически типизированных языках и
могут быть ускорены за счет JIT-компиляции (что используется в RPython).
В работе рассматриваются 24 проекта, для сбора статистики применяется
инструментированный интрепретатор.

Хотя высказанная гипотеза о полном отсутствии использования
метапрограммирования во время работы программы не подтверждается,
проведенные измерения показывают, что 70% из исследованных программ
действительно используют их значительно меньше после этапа инициализации.

В работе также приводится классификация динамических возможностей Python:

1. *Reflection.* Получение и использование информации о программе во время ее
исполнения. К этой категории авторы относят `getattr()`,
использование модуля `inspection`, специальных имен `__file__`,
`__name__` и пр.

2. *Dynamic typing*. Отсутствие аннотаций и статического вывода типов,
все проверки на этапе исполнения. Тут все понятно.

3. *Dynamic objects*. Возможность изменения уже объявленных классов во время
исполнения, добавления/удаление/изменения атрибутов объектов. Мне привычнее
термин monkey patching.

4. *Dynamic code*. Динамическое генерация и исполнение кода программой:
использование `exec()/eval()/compile()`. Сюда же относится `__import__` и,
видимо, `importlib`.

Davine Ancona, Massimo Ancona, Antonio Cuni ["RPython: a step towards reconciling dynamically and statically typed OO languages"][4]
------------------------------------------------------------------------------------------------------------------------------------

TODO

[1]: http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.90.3231#!
[2]: http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.45.4450
[3]: #

[cannon]: http://ca.linkedin.com/in/drbrettcannon
[aiken]: http://theory.stanford.edu/~aiken/publications/publications.html

[FL]: http://en.wikipedia.org/wiki/FL_(programming_language)
[starkiller]: http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.95.3786