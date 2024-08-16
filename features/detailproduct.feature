Feature: Product Details

    @detail1
    Scenario: Product Details Page
    Given Masukan username dan password
    When Tekan tombol login
    And Masuk dan pilih cek detail produk
    Then Menampilkan deskripsi produk

    @detail
    Scenario: Back to Products from Product Details
    Given Masuk kedalam akun
    When cek detail produk
    And Tekan tombol Back to Products
    Then Kembali ke dalam daftar produk