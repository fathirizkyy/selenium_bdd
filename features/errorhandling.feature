Feature: Error Handling on Locked Out User

    @error
    Scenario: Uji login menggunakan akun yang terkunci
    Given Masuk ke login page
    When Menggunakan username locked_out_user dan password valid
    And Menekan tombol login
    Then Muncul pesan error Epic sadface: Sorry, this user has been locked out