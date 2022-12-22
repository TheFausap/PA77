# SC77

## General info

- 21 bits word
- floating point arithmetic
- integer arithmetic
- string operation
- tagged word
- one generic register R0 at memory address 1
- PC is at memory address 0

| TAG | Description                |
| :-: | :---------------------:    |
| 000 | Integer number             |
| 010 | Floating point number (UN) |
| 001 | Floating point number (N)  |
| 011 | Strings                    |
| 100 | Arithmetic instructions    |
| 101 | Data instructions          |
| 110 | Jump instructions          |
| 111 | Unused memory location     |

### Floating point number (first approach) - NOT IMPLEMENTED

| `TTT` | `S` | `G` | `EEEEEEE` | `DDDDDDDDD` |
| :---: | :-: | :-: | :-------: | :---------: |
| `211` | `1` | `1` | `1111110` | `000000000` |
| `098` | `7` | `6` | `5432109` | `876543210` |

| `TTT` | `S` | `G` | `EEEEEEE` | `DDDDDDDDD` |
| :---: | :-: | :-: | :-------: | :---------: |
| `000` | `0` | `0` | `0000011` | `111111112` |
| `012` | `3` | `4` | `5678901` | `234567890` |

`2**-255 < x < 2**255`

### Floating point number (second approach)

| `TTT` | `EEEEEEEEE` | `DDDDDDDDD` |
| :---: | :---------: | :---------: |
| `211` | `111111110` | `000000000` |
| `098` | `765432109` | `876543210` |

| `TTT` | `EEEEEEEEE` | `DDDDDDDDD` |
| :---: | :---------: | :---------: |
| `000` | `000000011` | `111111112` |
| `012` | `345678901` | `234567890` |

the number is just a pointer to two addresses: one for the exponent, one for the mantissa
represented as integer numbers with sign.
The address is decided randomly by the CPU.

| `TTT` | `EEEEEEEEE` | `DDDDDDDDD` |
| :---: | :---------: | :---------: |
| `211` | `111111110` | `000000000` |
| `098` | `765432109` | `876543210` |

| `TTT` | `EEEEEEEEE` | `DDDDDDDDD` |
| :---: | :---------: | :---------: |
| `000` | `000000011` | `111111112` |
| `012` | `345678901` | `234567890` |

### Integer number

| `TTT` | `S` | `DDDDDDDDDDDDDDDDD` |
| :---: | :-: | :-----------------: |
| `211` | `1` | `11111110000000000` |
| `098` | `7` | `65432109876543210` |

| `TTT` | `S` | `DDDDDDDDDDDDDDDDD` |
| :---: | :-: | :-----------------: |
| `000` | `0` | `00000011111111112` |
| `012` | `3` | `45678901234567890` |

### String element

The element is just a pointer to an address in memory
E is always 0

| `TTT` | `EEEEEEEEE` | `DDDDDDDDD` |
| :---: | :---------: | :---------: |
| `211` | `111111110` | `000000000` |
| `098` | `765432109` | `876543210` |

| `TTT` | `EEEEEEEEE` | `DDDDDDDDD` |
| :---: | :---------: | :---------: |
| `000` | `000000011` | `111111112` |
| `012` | `345678901` | `234567890` |

The strings are encoded using the SQUOZE encoding, plus two flag bits. Each memory location can contain up to 7 chars.

| SQZ | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 000 | spc |  0  |  1  |  2  |  3  |  4  |  5  |  6  |
| 001 |  7  |  8  |  9  |  A  |  B  |  C  |  D  |  E  |
| 010 |  F  |  G  |  H  |  I  |  J  |  K  |  L  |  M  |
| 011 |  N  |  O  |  P  |  Q  |  R  |  S  |  T  |  U  |
| 100 |  V  |  W  |  X  |  Y  |  Z  | = # | / % | ) ] |
| 101 | + & |  -  | ^ @ | < ? | > : |  *  |  /  |  $  |
| 110 |  ,  |  .  |  ;  | ( [ | { } | _ ! | N/A | N/A |
| 111 |  \  | ' " |  `  |  ~  | N/A | N/A | N/A | N/A |

if FF is 00 the above table is applied. If FF is 01 the other possible character is selected or null char. If FF is 10 the small
letter alphabet is used, the other characters remain the same.

## Opcodes list

- LDF AAAA : load the next two words in consecutive memory location starting from AAAA
- LDI AAAA : load the next word into AAAA
- MOV DDDD,SSSS : move one word from SSSS to DDDD. SSSS is zeroed and the previous content of DDDD is destroyed
- CPY DDDD,SSSS : copy one word from SSSS to DDDD. Previous content of DDDD is destroyed
- LDX IIII : load the immediate value IIII into R0
- MVA DDDD,SSSS : move one word from SSSS to DDDD. SSSS is zeroed and the new content in DDDD is (SSSS) AND (DDDD)
- MVO DDDD,SSSS : move one word from SSSS to DDDD. SSSS is zeroed and the new content in DDDD is (SSSS) OR (DDDD)
- MVX DDDD,SSSS : move one word from SSSS to DDDD. SSSS is zeroed and the new content in DDDD is (SSSS) XOR (DDDD)
- NOT AAAA : all bits are inverted at location AAAA
- MVF DDDD,SSSS : move two words at SSSS,SSSS+1 to DDDD,DDDD+1. SSSS is zeroed and the previous content of DDDD is destroyed
- FLD AAAA : load a floating point value (in the next two words, exp and mant) at AAAA. The addresses of the exp and mant are handled automatically by the system
