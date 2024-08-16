Feature: Fitur login

    @sukses
    Scenario:  Login Valid Credetials
    Given Masuk ke login page
    When Memasukan username dan password valid
    And Menekan tombol login
    Then User berhasil masuk

   @invalidPassword
    Scenario: Login Invalid Password
    Given Masuk ke login page
    When Memasukan password invalid
    And Menekan tombol login
    Then menampilkan pesan Epic sadface: Username and password do not match any user in this service

    @invalidPasswordUsername
    Scenario: Login Invalid username and Password
    Given Masuk ke login page
    When Memasukan username dan password invalid
    And Menekan tombol login
    Then menampilkan pesan Epic sadface: Username and password do not match any user in this service

    @empity
    Scenario: Login Empty Fields
    Given  Masuk ke login page
    When biarkan username dan password kosong
    And Menekan tombol login
    Then Epic sadface: Username is required