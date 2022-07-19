Feature: Dealer Blackjack
    Scenario: rozdaje karty
        Given na stronie blackjacka
        When wciśnięty przycisk play
        Then zostają poprawnie rozdane karty
        Then webdriver się wyłącza