from __future__ import division
import wpf

from System.Windows import Application, Window
from System.Windows.Controls import Button, Label

clear = True

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'PyCulator.xaml')
        pass

    def Is_Last_Numeric(text):
        if(text[-1].isdigit()):
            return True
        return False

    def Number_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        number_value = getattr(sender, 'Content', 'default')
        global clear
        if (clear or self.bigText.Content == '0'):
            clear = False
            self.bigText.Content = number_value
        else:
            self.bigText.Content += number_value
        pass

    def Plus_Minus_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        global clear
        try:
            num = float(self.bigText.Content)
            self.bigText.Content = str(-1 * num)
        except:
            clear = True
            self.bigText.Content = "INVALID"
        pass

    def Clear_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        self.smallText = self.FindName('Small_Text')
        clear_value = getattr(sender, 'Content', 'default')
        global clear
        if (clear_value == 'CE'):
            clear = True
            self.bigText.Content = '0'
        else:
            clear = True
            self.bigText.Content = '0'
            self.smallText.Content = '0'
        pass

    def Del_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        new_value = self.bigText.Content[:-1]
        self.bigText.Content = new_value
        pass

    def Dot_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        global clear
        if clear:
            clear = False
            self.bigText.Content = '0.'
        else:
            if (self.bigText.Content.find('.') == -1):
                self.bigText.Content += '.'
        pass

    def Basic_Operation_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        self.smallText = self.FindName('Small_Text')
        operation_value = getattr(sender, 'Content', '+')
        if(operation_value == 'X'):
            operation_value = '*'
        global clear
        
        if (self.bigText.Content != 'INVALID'):
            if (self.smallText.Content == '0' or self.smallText.Content == '' or self.smallText.Content == 'Error'):
                if(self.bigText.Content.find('Error') != -1):
                    pass
                else:
                    self.smallText.Content = self.bigText.Content + operation_value
            else:
                try:
                        self.smallText.Content += self.bigText.Content + operation_value
                except:
                    self.smallText.Content = 'Error'
            try:
                self.bigText.Content = str(eval(self.smallText.Content))
            except:
                try:
                    self.bigText.Content = str(eval(self.smallText.Content + '0'))
                except:
                    self.bigText.Content = 'Math Error'
            clear = True
        pass

    def Diva_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        self.smallText = self.FindName('Small_Text')
        global clear
        if (self.bigText.Content != 'INVALID'):
            if (self.smallText.Content == '0'):
                self.smallText.Content = self.bigText.Content + '/'
            else:
                self.smallText.Content += self.bigText.Content + '/'
            try:
                num1 = float(eval(self.smallText.Content))
                num2 = float(self.bigText.Content)
                self.bigText.Content = str(num1 / num2)
            except:
                self.bigText.Content = '0'
            clear = True
        pass

    def Equ_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        self.smallText = self.FindName('Small_Text')
        global clear
        if (self.bigText.Content != 'INVALID'):
            try:
                self.bigText.Content = str(eval(self.smallText.Content + self.bigText.Content))
            except:
                pass
            self.smallText.Content = ''
            clear = True
        pass
    
if __name__ == '__main__':
    print ("test")
    Application().Run(MyWindow())