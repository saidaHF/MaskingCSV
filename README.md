# Saida Masked Project 

### Prerequisites:

- Python 3.9
- For execute this program you need a CSV file with the next structure:
    
|  ID | Nombre | Email | Facturado | Localidad |
| -------- | -------- | -------- |-------- |--------
| 1     | Juan Martinez  | juan@mail.com     | 15000 | Valladolid |
| 2    | Francisco Gomez  | paco@my-mail.com  | 20000 | Salamanca |
| 3    | ...  | ...  | ... | ... |

The program will return a new CSV file with the sensitive data masked 

*For example:*
juan@mail.com -> XXXX@XXXX.XXX
