def saude(pessoas, d_encontro, d_observacao):
    infected = []
    if any(i > -1 for i in pessoas):
        for j in range(pessoas.count(-1)):
            pessoas[pessoas.index(-1)] = d_encontro

    for i in pessoas:
        if i + 15 > d_observacao:
            infected.append(i)
    return len(infected)


if __name__ == '__main__':
    print(saude(
        [-1, 0, 3, -1, -1],
        3,
        17
    ))
