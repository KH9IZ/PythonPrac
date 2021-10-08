def SUB(reduce, deduct):
    if '__sub__' in dir(reduce):
        return reduce - deduct
    return type(reduce)(item for item in reduce if item not in deduct)
print(SUB(*eval(input())))
