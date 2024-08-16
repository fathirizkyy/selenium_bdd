Feature: Verify Product Quantity in Cart
    @jumlah
    Scenario: Uji bahwa jumlah produk yang benar ditampilkan di keranjang
    Given Melakukan Login
    When Memilih produk
    And Menekan tombol add to cart
    Then Periksa jumlah produk