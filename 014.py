larg = float(input('digite a largura da parede: '))
alt = float(input('digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua area de {}m².'.format(larg, alt, area))
print('para pintar a parede você precisará de {}l de tinta'.format(tinta))