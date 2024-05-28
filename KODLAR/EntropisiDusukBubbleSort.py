import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Son i öğe zaten sıralı olduğundan, n-i-1'e kadar döngü yaparız
        for j in range(0, n-i-1):
            # Bir sonraki öğeyle karşılaştır ve gerekirse değiştir
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 1 ile 45 arasında rastgele sayılar üreten veri seti oluşturma
random_data = [random.randint(1, 45) for _ in range(1000)]

# Sıralama öncesi veri seti
print("Sıralama öncesi ilk 20 eleman:", random_data[:20])

# Bubble Sort algoritması uygulanıyor
bubble_sort(random_data)

# Sıralama sonrası veri seti
print("Sıralama sonrası ilk 20 eleman:", random_data[:20])
