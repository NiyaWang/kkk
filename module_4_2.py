def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()
inner_function()   # Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

