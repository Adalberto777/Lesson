import view
import model

def my_func():
    num1 = model.parsing(view.data_in())
    num2 = model.parsing(view.data_in())
    oper = view.data_op()
    result = model.new_parsing(model.calculate(num1, num2, oper))
    print(result)

