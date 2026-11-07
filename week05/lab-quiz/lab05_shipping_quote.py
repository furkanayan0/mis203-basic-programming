def calculate_subtotal(item_prices):
    """Sepetteki ürünlerin toplam fiyatını hesaplar."""
    return sum(item_prices)

def get_discount_rate(subtotal):
    """100 TL ve üzeri siparişler için %10 (0.10) indirim oranı döndürür."""
    if subtotal >= 100.0:
        return 0.10
    return 0.0

def calculate_shipping_fee(subtotal):
    """50 TL altı siparişlere 15 TL kargo ücreti ekler, üstü için ücretsizdir (0.0)."""
    if subtotal >= 50.0:
        return 0.0
    return 15.0

def calculate_final_total(item_prices):
    """Tüm hesaplamaları birleştirip nihai ödenecek tutarı döndürür."""
    subtotal = calculate_subtotal(item_prices)
    discount_rate = get_discount_rate(subtotal)
    shipping_fee = calculate_shipping_fee(subtotal)
    
    discount_amount = subtotal * discount_rate
    final_total = (subtotal - discount_amount) + shipping_fee
    return final_total

# --- Acceptance Checks: Assert Tests ---
# Sınır değeri (threshold boundary) kontrolü: Tam 100.0 değeri
assert get_discount_rate(100.0) == 0.10, "Hata: 100 sınırı %10 indirim almalı."
# Sınırın hemen altı kontrolü
assert get_discount_rate(99.9) == 0.0, "Hata: 100 altı indirim almamalı."
# Alt toplam hesaplama kontrolü
assert calculate_subtotal([10.0, 20.0, 5.0]) == 35.0, "Hata: Alt toplam yanlış hesaplanıyor."

# --- Sample Orders ---
# Aynı kod kopyalanmadan, fonksiyonlar tekrar kullanılarak iki farklı sipariş hesaplanıyor.

print("--- Order 1 ---")
order1_items = [15.0, 20.0] # Toplam 35 (Kargo eklenecek, indirim yok)
order1_total = calculate_final_total(order1_items)
print(f"Items: {order1_items}")
print(f"Final Total: {order1_total} TL") # 35 + 15 = 50.0 TL

print("\n--- Order 2 ---")
order2_items = [40.0, 50.0, 30.0] # Toplam 120 (Kargo ücretsiz, %10 indirim)
order2_total = calculate_final_total(order2_items)
print(f"Items: {order2_items}")
print(f"Final Total: {order2_total} TL") # 120 - 12 + 0 = 108.0 TL
