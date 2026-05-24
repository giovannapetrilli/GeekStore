Feature: Compra GeekStore

  Scenario: Compra realizada com sucesso

    Given que existe um produto em estoque

    When o usuário realiza uma compra

    Then a compra deve ser aprovada