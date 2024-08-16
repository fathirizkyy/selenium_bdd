Feature: fitur cart

    @cart
    Scenario: Add Item
    Given Melakukan Login
    When Memilih produk
    And Menekan tombol add to cart
    Then Menampilkan angka di icon cart

    @cart2
    Scenario: Remove ite
    Given Melakukan login
    When Memilih dan tekan tombol cart
    And Tekan tombol remove
    Then Angka di icon cart berkurang

    @cart
    Scenario: View Cart
    Given Melakukan login
    When Memilih dan tekan tombol cart
    And Tekan icon cart
    Then Menampilkan produk yang ditambah

    @cart
    Scenario: Continue Shopping from Cart
    Given Masuk dan pilih produk
    When Tekan icon dan muncul produk yang ditambah
    And Tekan tombol Continue shopping
    Then Kembali ke daftar produk
