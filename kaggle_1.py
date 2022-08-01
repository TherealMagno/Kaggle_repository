


# def run():
#     entrada = input("Escriba un numero para agregar 3 numeros más ")
#     output = int(entrada) + 3 
#     print(output)


# if __name__ == "__main__":
#     run()


def add_three(input_var):
    output_var = input_var + 3
    return output_var


# Run the function with 10 as input
new_number = add_three(10)

# Check that the value is 13, as expected
print(new_number)    