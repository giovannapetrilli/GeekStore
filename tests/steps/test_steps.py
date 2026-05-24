from pytest_bdd import scenarios, given, when, then

scenarios("../features/compra.feature")


@given("que existe um produto em estoque")
def produto_em_estoque():
    pass


@when("o usuário realiza uma compra")
def realizar_compra():
    pass


@then("a compra deve ser aprovada")
def compra_aprovada():
    assert True