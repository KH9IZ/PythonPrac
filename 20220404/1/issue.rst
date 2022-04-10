TaskTree
========

.. image:: https://i.ibb.co/SJ8MNKc/tt-logo-black.png
    :width: 100px
    :align: center
    :alt: Альтернативный текст


* Список ToDo в древовидном представлении
* Репозиторий_ 
 

.. code:: python3
    :number-lines:

    t = Task("My plans") # Default status is STATUS.PENDING.
    t.children += (Task("Lifeline plans"), )
    new_t = Task("Make big things", parent=t)
    new_t.parent = t.children[0]
  
Участники
~~~~~~~~~
#. Князев Егор Иванович, 321 группа, `@KH9IZ`_
#. Поклонский Алексей Андреевич, 319/2 группа, `@Prikalel`_
#. Шутков Геннадий Алексеевич, 321 группа, `@gen-gematogen`_

.. _Репозиторий: https://github.com/Chauss-LLC/task_tree_local 
.. _@KH9IZ: https://github.com/KH9IZ
.. _@Prikalel: https://github.com/Prikalel
.. _@gen-gematogen: https://github.com/gen-gematogen
.. _logo: https://github.com/Chauss-LLC/task_tree_local/blob/master/logo_task_tree.svg
