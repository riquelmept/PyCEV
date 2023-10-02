words = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'grátis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
for p in words:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')