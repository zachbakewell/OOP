import InsectClass as i


def main():
    ins_type = i.Insect()

    ins = ins_type.type()

    print('This insect is: ', ins)

    print('This', ins, 'can fly for:', ins_type.get_len_flight())