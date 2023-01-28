'''1

Create a module called hello.py that contains a single function hello. 
his function should accept a single string parameter name print the text Hello {name}! 
to the interactive window with {name} replaced with the function argument.
2. Create a module called main.py that imports the hello function from hello.py and calls the function with your name.
Встановити: Faker, Freeze. Завантажити завдання необхідно на git, необхідно
мати файли config, requirements.
3. Після цього виконати перевірки на ввід користувача, якщо не має запису, його потрібно згенерувати(пароль також).
4.
*Зробити перевірку паролю на коректність
https://www.ibm.com/docs/en/sva/9.0.5?topic=policy-valid-not-valid-password- '''


def hello(name:str) -> str:

    return f'Hello {name}!'