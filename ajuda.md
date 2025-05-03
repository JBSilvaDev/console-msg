# Códigos de Escape ANSI para Personalização de Terminal

Aqui está uma lista completa dos códigos de escape ANSI que você pode usar para personalizar mensagens no terminal:

## Cores do Texto (Foreground)
- `\033[30m` - Preto
- `\033[31m` - Vermelho
- `\033[32m` - Verde
- `\033[33m` - Amarelo
- `\033[34m` - Azul
- `\033[35m` - Magenta
- `\033[36m` - Ciano
- `\033[37m` - Branco
- `\033[90m` - Cinza escuro (Bright Black)
- `\033[91m` - Vermelho claro (Bright Red)
- `\033[92m` - Verde claro (Bright Green)
- `\033[93m` - Amarelo claro (Bright Yellow)
- `\033[94m` - Azul claro (Bright Blue)
- `\033[95m` - Magenta claro (Bright Magenta)
- `\033[96m` - Ciano claro (Bright Cyan)
- `\033[97m` - Branco brilhante (Bright White)

## Cores de Fundo (Background)
- `\033[40m` - Preto
- `\033[41m` - Vermelho
- `\033[42m` - Verde
- `\033[43m` - Amarelo
- `\033[44m` - Azul
- `\033[45m` - Magenta
- `\033[46m` - Ciano
- `\033[47m` - Branco
- `\033[100m` - Cinza escuro (Bright Black)
- `\033[101m` - Vermelho claro (Bright Red)
- `\033[102m` - Verde claro (Bright Green)
- `\033[103m` - Amarelo claro (Bright Yellow)
- `\033[104m` - Azul claro (Bright Blue)
- `\033[105m` - Magenta claro (Bright Magenta)
- `\033[106m` - Ciano claro (Bright Cyan)
- `\033[107m` - Branco brilhante (Bright White)

## Estilos de Texto
- `\033[0m` - Reset (volta ao padrão)
- `\033[1m` - Negrito
- `\033[2m` - Fraco (dim)
- `\033[3m` - Itálico
- `\033[4m` - Sublinhado
- `\033[5m` - Piscando (lento)
- `\033[6m` - Piscando rápido (não suportado em todos os terminais)
- `\033[7m` - Inverte cores (foreground/background)
- `\033[8m` - Oculto (invisível)
- `\033[9m` - Tachado (riscado)

## Movimento do Cursor
- `\033[nA` - Move o cursor para cima n linhas
- `\033[nB` - Move o cursor para baixo n linhas
- `\033[nC` - Move o cursor para a direita n colunas
- `\033[nD` - Move o cursor para a esquerda n colunas
- `\033[2J` - Limpa a tela inteira
- `\033[K` - Limpa a linha atual
- `\033[s` - Salva a posição do cursor
- `\033[u` - Restaura a posição do cursor

## Exemplo de Uso Combinado
```python
print("\033[1;31;47mTexto em vermelho negrito com fundo branco\033[0m")
print("\033[4;33;44mTexto amarelo sublinhado com fundo azul\033[0m")
print("\033[5;32mTexto verde piscando\033[0m")
```

Lembre-se de sempre usar `\033[0m` no final para resetar as configurações e evitar que os estilos afetem o resto do seu terminal.