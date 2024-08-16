Feature: Sorting

    @Sort
    Scenario: Sort Products by Price (Low to High)
    Given Login dengan akun Valid
    When Masuk kedalam akun
    And Tekan tombol dropdown
    Then Pilih opsi Price low to high

    @Sort
    Scenario: Sort Products by Name (A to Z)
    Given Login dengan akun Valid
    When Masuk kedalam akun
    And Tekan tombol dropdown
    Then Pilih opsi Name A to Z