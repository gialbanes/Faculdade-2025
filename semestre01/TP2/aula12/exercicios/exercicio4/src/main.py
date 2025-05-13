from Produto import Produto

if __name__ == "__main__":
    p = Produto()

    p.setNome("Celular")
    p.setQtd(2)
    p.setValor(1000.00)
    p.calcularTotal()