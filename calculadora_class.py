import re
import math
import tkinter as tk
from typing import List

class Calculadora:
    '''teste'''
    def __init__(
        self,
        root: tk.Tk, 
        label: tk.Label,
        display: tk.Entry,
        buttons: List[List[tk.Button]]
    ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons

    def inicio(self):
        self._config_botones()
        self._config_display()
        self.root.mainloop()
    
    def _config_botones(self):
        botones = self.buttons 
        for row_values in botones:
            for boton in row_values:
                boton_text = boton['text']

                if boton_text == 'C':
                    boton.bind('<Button-1>', self.clear)
                    boton.config(bg='#EA4335', fg='#fff')

                if boton_text in '0123456789.+-/*()^':
                    boton.bind('<Button-1>', self.add_text_to_display)
                
                if boton_text == '=':
                    boton.bind('<Button-1>', self.calcular)
                    boton.config(bg='#113ED5', fg='#fff')


    def _config_display(self):
        self.display.bind('<Return>', self.calcular)
        self.display.bind('<KP_Enter>', self.calcular)
    
    def _fix_text(self, text):
        # reemplace todo lo que no sea 0123456789./*-+^ por nada
        text = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', text)
        # Reemplazar señales repetidas con una sola señal.
        text = re.sub(r'([\.\+\/\-\*\^])\1+', r'\1', text, 0 )
        # Sustituye () o * () por nada
        text = re.sub(r'\*?\(\)', '', text)

        return text

    def clear(self, event=None):
        self.display.delete(0, 'end')
    
    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])
    
    def calcular(self, event=None):
        fixed_text = self._fix_text(self.display.get())
        operaciones = self._get_operaciones(fixed_text)

        try:
            if len(operaciones) == 1:
                result = eval(self._fix_text(operaciones[0]))
            else:
                result = eval(self._fix_text(operaciones[0]))
                for operacion in operaciones[1:]:
                    result = math.pow(result, eval(self._fix_text(operacion)))
        
            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{fixed_text} = {result}')
        
        except OverflowError:
            self.label.config(text='No se puede realizar esta operacioon, sorry!')
        except Exception as e:
            print(e)
            self.label.config(text='Operacion invalidad')    
    
    def _get_operaciones(self, text):
        return re.split(r'\^', text, 0)    
    