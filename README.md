# Zeller Algorithm

Bu proje, Zeller algoritmasını kullanarak verilen bir tarihin haftanın hangi gününe denk geldiğini hesaplar.

## Zeller Algoritması Nedir?

Zeller algoritması, bir tarihin haftanın hangi gününe denk geldiğini hesaplamak için kullanılan matematiksel bir yöntemdir. Christian Zeller tarafından geliştirilmiştir.

## Formül

h = (g + m + y + y/4 + c) % 7

* g → gün
* m → ay kodu
* y → yılın son 2 hanesi
* c → yıl kodu

## Sonuç

* 0 → Pazar
* 1 → Pazartesi
* 2 → Salı
* 3 → Çarşamba
* 4 → Perşembe
* 5 → Cuma
* 6 → Cumartesi

## Not

Bu algoritma **1582 yılından sonraki tarihler** için geçerlidir.
