def sort_phones(ph
                ):
    
    for i in range(len(ph)):
        min_idx = i

        for j in range(i + 1, len(ph)):
            if ph[j] < ph[min_idx]:
                min_idx = j

        if min_idx != i:
            ph[i], ph[min_idx] = ph[min_idx], ph[i]
    
    return ph

phone_list = [
    "23-45-67",
    "98-01-02", 
    "12-34-56",  
    "78-90-12"
]

print(sort_phones(phone_list))
