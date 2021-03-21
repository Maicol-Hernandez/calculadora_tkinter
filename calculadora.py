from calculadora_pro import make_root, make_display, make_label, make_buttons 
 
from calculadora_class import Calculadora

def main(): 
    root = make_root()
    display = make_display(root)
    label = make_label(root)
    buttons = make_buttons(root)
    calculadora = Calculadora(root, label, display, buttons)
    calculadora.inicio()


if __name__ == "__main__":
    main()