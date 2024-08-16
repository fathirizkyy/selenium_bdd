Feature: Fitur Checkout

    @out1
    Scenario: Checkout Valid Information
    Given Tambahkan produk ke keranjang dan tekan tombol checkout
    When Isi seluruh form informasi
    And Tekan tombol Finish
    Then Menampilkan pesan THANK YOU FOR YOUR ORDER

    @out
    Scenario: Checkout Missing First Name
    Given Tambahkan produk ke keranjang dan tekan tombol checkout
    When Isi seluruh form informasi kecuali kolom firts name
    And Tekan tombol Continue
    Then Menampilkan allert Error: First Name is required