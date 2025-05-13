from Cliente import Cliente

if __name__ == "__main__":
    cli = Cliente()

    cli.setNome("Giovana")
    cli.setEnd("Cananeia")
    cli.setRg("57.562.094-8")

    cli.listarCliente()