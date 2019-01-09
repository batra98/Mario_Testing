Analysis of code before refactoring

Report
======

1099 statements analysed.

Statistics by type
------------------

+------------+----------+--------------+--------------+---------------+------------+
| type       | number   | old number   | difference   | %documented   | %badname   |
+============+==========+==============+==============+===============+============+
| module     | 20       | 19           | +1.00        | 0.00          | 0.00       |
+------------+----------+--------------+--------------+---------------+------------+
| class      | 16       | 15           | +1.00        | 0.00          | 31.25      |
+------------+----------+--------------+--------------+---------------+------------+
| method     | 67       | 62           | +5.00        | 31.34         | 0.00       |
+------------+----------+--------------+--------------+---------------+------------+
| function   | 4        | 11           | -7.00        | 0.00          | 0.00       |
+------------+----------+--------------+--------------+---------------+------------+

External dependencies
---------------------

::

    NonBlockingInput (main,main_mario_4)
    big_enemy (main_mario_4)
    bulletclass (main_mario_4)
    cake (main_mario_4)
    clouds (main_mario_4)
    coins (main_mario_4)
    collectable_objects (pistol,cake)
    color (scene,start_screen)
    config (main,small_enemy,coins,main_mario_4,big_enemy)
    ending (main_mario_4)
    flag_1 (main_mario_4)
    main_mario_4 (main)
    mario_player (main_mario_4)
    person (big_enemy,mario_player,small_enemy)
    pistol (main_mario_4)
    poles (main_mario_4)
    scene (main_mario_4)
    small_enemy (main_mario_4)

Raw metrics
-----------

+-------------+----------+---------+------------+--------------+
| type        | number   | %       | previous   | difference   |
+=============+==========+=========+============+==============+
| code        | 1285     | 82.27   | 1298       | -13.00       |
+-------------+----------+---------+------------+--------------+
| docstring   | 17       | 1.09    | 127        | -110.00      |
+-------------+----------+---------+------------+--------------+
| comment     | 9        | 0.58    | 6          | +3.00        |
+-------------+----------+---------+------------+--------------+
| empty       | 251      | 16.07   | 229        | +22.00       |
+-------------+----------+---------+------------+--------------+

Duplication
-----------

+----------------------------+---------+------------+--------------+
|                            | now     | previous   | difference   |
+============================+=========+============+==============+
| nb duplicated lines        | 37      | 8          | +29.00       |
+----------------------------+---------+------------+--------------+
| percent duplicated lines   | 2.429   | 0.493      | +1.94        |
+----------------------------+---------+------------+--------------+

Messages by category
--------------------

+--------------+----------+------------+--------------+
| type         | number   | previous   | difference   |
+==============+==========+============+==============+
| convention   | 765      | 2          | +763.00      |
+--------------+----------+------------+--------------+
| refactor     | 45       | 31         | +14.00       |
+--------------+----------+------------+--------------+
| warning      | 357      | 14         | +343.00      |
+--------------+----------+------------+--------------+
| error        | 7        | 0          | +7.00        |
+--------------+----------+------------+--------------+

% errors / warnings by module
-----------------------------

+-----------------------+---------+-----------+------------+--------------+
| module                | error   | warning   | refactor   | convention   |
+=======================+=========+===========+============+==============+
| collectable\_objects  | 85.71   | 3.08      | 2.22       | 3.01         |
+-----------------------+---------+-----------+------------+--------------+
| NonBlockingInput      | 14.29   | 0.84      | 6.67       | 2.75         |
+-----------------------+---------+-----------+------------+--------------+
| scene                 | 0.00    | 22.13     | 2.22       | 14.64        |
+-----------------------+---------+-----------+------------+--------------+
| start\_screen         | 0.00    | 8.96      | 4.44       | 5.62         |
+-----------------------+---------+-----------+------------+--------------+
| small\_enemy          | 0.00    | 7.84      | 4.44       | 4.71         |
+-----------------------+---------+-----------+------------+--------------+
| big\_enemy            | 0.00    | 7.84      | 4.44       | 4.71         |
+-----------------------+---------+-----------+------------+--------------+
| main                  | 0.00    | 7.56      | 0.00       | 5.75         |
+-----------------------+---------+-----------+------------+--------------+
| flag\_1               | 0.00    | 5.32      | 0.00       | 6.27         |
+-----------------------+---------+-----------+------------+--------------+
| clouds                | 0.00    | 5.32      | 0.00       | 3.53         |
+-----------------------+---------+-----------+------------+--------------+
| main\_mario\_4        | 0.00    | 5.04      | 64.44      | 9.93         |
+-----------------------+---------+-----------+------------+--------------+
| ending                | 0.00    | 4.76      | 0.00       | 5.62         |
+-----------------------+---------+-----------+------------+--------------+
| bulletclass           | 0.00    | 4.76      | 0.00       | 3.14         |
+-----------------------+---------+-----------+------------+--------------+
| person                | 0.00    | 4.20      | 0.00       | 3.14         |
+-----------------------+---------+-----------+------------+--------------+
| coins                 | 0.00    | 3.92      | 6.67       | 4.71         |
+-----------------------+---------+-----------+------------+--------------+
| mario\_player         | 0.00    | 3.08      | 0.00       | 2.61         |
+-----------------------+---------+-----------+------------+--------------+
| poles                 | 0.00    | 1.96      | 2.22       | 2.22         |
+-----------------------+---------+-----------+------------+--------------+
| cake                  | 0.00    | 1.68      | 0.00       | 1.96         |
+-----------------------+---------+-----------+------------+--------------+
| pistol                | 0.00    | 1.68      | 0.00       | 1.83         |
+-----------------------+---------+-----------+------------+--------------+
| color                 | 0.00    | 0.00      | 2.22       | 3.53         |
+-----------------------+---------+-----------+------------+--------------+
| config                | 0.00    | 0.00      | 0.00       | 10.33        |
+-----------------------+---------+-----------+------------+--------------+

Messages
--------

+----------------------------------+---------------+
| message id                       | occurrences   |
+==================================+===============+
| bad-whitespace                   | 403           |
+----------------------------------+---------------+
| mixed-indentation                | 306           |
+----------------------------------+---------------+
| invalid-name                     | 131           |
+----------------------------------+---------------+
| missing-docstring                | 86            |
+----------------------------------+---------------+
| trailing-whitespace              | 55            |
+----------------------------------+---------------+
| line-too-long                    | 44            |
+----------------------------------+---------------+
| too-many-nested-blocks           | 22            |
+----------------------------------+---------------+
| singleton-comparison             | 20            |
+----------------------------------+---------------+
| broad-except                     | 16            |
+----------------------------------+---------------+
| anomalous-backslash-in-string    | 12            |
+----------------------------------+---------------+
| wrong-import-order               | 10            |
+----------------------------------+---------------+
| no-self-use                      | 10            |
+----------------------------------+---------------+
| missing-final-newline            | 10            |
+----------------------------------+---------------+
| unused-variable                  | 8             |
+----------------------------------+---------------+
| unused-import                    | 6             |
+----------------------------------+---------------+
| unused-argument                  | 6             |
+----------------------------------+---------------+
| superfluous-parens               | 6             |
+----------------------------------+---------------+
| too-many-branches                | 3             |
+----------------------------------+---------------+
| undefined-variable               | 2             |
+----------------------------------+---------------+
| too-many-statements              | 2             |
+----------------------------------+---------------+
| too-many-locals                  | 2             |
+----------------------------------+---------------+
| too-many-arguments               | 2             |
+----------------------------------+---------------+
| super-init-not-called            | 2             |
+----------------------------------+---------------+
| no-method-argument               | 2             |
+----------------------------------+---------------+
| no-member                        | 2             |
+----------------------------------+---------------+
| duplicate-code                   | 2             |
+----------------------------------+---------------+
| too-many-return-statements       | 1             |
+----------------------------------+---------------+
| too-few-public-methods           | 1             |
+----------------------------------+---------------+
| import-error                     | 1             |
+----------------------------------+---------------+
| attribute-defined-outside-init   | 1             |
+----------------------------------+---------------+

Global evaluation
-----------------

Your code has been rated at -0.94/10 (previous run: 9.56/10, -10.49)

Analysis after Refactoring the code

Report
======

1057 statements analysed.

Statistics by type
------------------

+------------+----------+--------------+--------------+---------------+------------+
| type       | number   | old number   | difference   | %documented   | %badname   |
+============+==========+==============+==============+===============+============+
| module     | 19       | 19           | =            | 100.00        | 0.00       |
+------------+----------+--------------+--------------+---------------+------------+
| class      | 15       | 15           | =            | 100.00        | 13.33      |
+------------+----------+--------------+--------------+---------------+------------+
| method     | 62       | 62           | =            | 100.00        | 0.00       |
+------------+----------+--------------+--------------+---------------+------------+
| function   | 11       | 11           | =            | 100.00        | 0.00       |
+------------+----------+--------------+--------------+---------------+------------+

External dependencies
---------------------

::

    NonBlockingInput (main,main_mario_4)
    bulletclass (main_mario_4)
    cake (main_mario_4)
    clouds (main_mario_4)
    coins (main_mario_4)
    collectable_objects (cake,pistol)
    color (start_screen,scene)
    config (small_enemy,main,main_mario_4)
    ending (main_mario_4)
    flag_1 (main_mario_4)
    main_mario_4 (main)
    mario_player (main_mario_4)
    person (small_enemy,mario_player)
    pistol (main_mario_4)
    poles (main_mario_4)
    scene (main_mario_4)
    small_enemy (main_mario_4)

Raw metrics
-----------

+-------------+----------+---------+------------+--------------+
| type        | number   | %       | previous   | difference   |
+=============+==========+=========+============+==============+
| code        | 1298     | 78.19   | 1299       | -1.00        |
+-------------+----------+---------+------------+--------------+
| docstring   | 127      | 7.65    | 127        | =            |
+-------------+----------+---------+------------+--------------+
| comment     | 6        | 0.36    | 6          | =            |
+-------------+----------+---------+------------+--------------+
| empty       | 229      | 13.80   | 229        | =            |
+-------------+----------+---------+------------+--------------+

Duplication
-----------

+----------------------------+---------+------------+--------------+
|                            | now     | previous   | difference   |
+============================+=========+============+==============+
| nb duplicated lines        | 8       | 8          | =            |
+----------------------------+---------+------------+--------------+
| percent duplicated lines   | 0.493   | 0.493      | +0.00        |
+----------------------------+---------+------------+--------------+

Messages by category
--------------------

+--------------+----------+------------+--------------+
| type         | number   | previous   | difference   |
+==============+==========+============+==============+
| convention   | 2        | 2          | =            |
+--------------+----------+------------+--------------+
| refactor     | 31       | 31         | =            |
+--------------+----------+------------+--------------+
| warning      | 14       | 14         | =            |
+--------------+----------+------------+--------------+
| error        | 0        | 0          | =            |
+--------------+----------+------------+--------------+

% errors / warnings by module
-----------------------------

+-----------------------+---------+-----------+------------+--------------+
| module                | error   | warning   | refactor   | convention   |
+=======================+=========+===========+============+==============+
| main\_mario\_4        | 0.00    | 78.57     | 87.10      | 0.00         |
+-----------------------+---------+-----------+------------+--------------+
| clouds                | 0.00    | 14.29     | 0.00       | 0.00         |
+-----------------------+---------+-----------+------------+--------------+
| scene                 | 0.00    | 7.14      | 3.23       | 50.00        |
+-----------------------+---------+-----------+------------+--------------+
| start\_screen         | 0.00    | 0.00      | 3.23       | 0.00         |
+-----------------------+---------+-----------+------------+--------------+
| color                 | 0.00    | 0.00      | 3.23       | 0.00         |
+-----------------------+---------+-----------+------------+--------------+
| collectable\_objects  | 0.00    | 0.00      | 3.23       | 0.00         |
+-----------------------+---------+-----------+------------+--------------+
| small\_enemy          | 0.00    | 0.00      | 0.00       | 50.00        |
+-----------------------+---------+-----------+------------+--------------+

Messages
--------

+------------------------------+---------------+
| message id                   | occurrences   |
+==============================+===============+
| too-many-nested-blocks       | 20            |
+------------------------------+---------------+
| broad-except                 | 14            |
+------------------------------+---------------+
| too-many-branches            | 3             |
+------------------------------+---------------+
| too-many-statements          | 2             |
+------------------------------+---------------+
| too-many-locals              | 2             |
+------------------------------+---------------+
| too-many-arguments           | 2             |
+------------------------------+---------------+
| invalid-name                 | 2             |
+------------------------------+---------------+
| too-many-return-statements   | 1             |
+------------------------------+---------------+
| duplicate-code               | 1             |
+------------------------------+---------------+

Global evaluation
-----------------

Your code has been rated at 9.56/10 (previous run: 9.56/10, -0.00)