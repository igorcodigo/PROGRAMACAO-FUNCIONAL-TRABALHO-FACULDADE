def hi_message(nome, inicial):
    def message():
        nonlocal inicial
        inicial += 1
        return f"Olá, {nome}! Esta é minha {inicial}° saudação."
    return message

saudacao_vini = hi_message("Vini", 0)

print(saudacao_vini)

print(saudacao_vini())
print(saudacao_vini())
print(saudacao_vini())

saudacao_ana = hi_message("Ana", 9)

print(saudacao_ana())
print(saudacao_ana())
print(saudacao_ana())
