import wpf

from System.Windows import Application, Window
from System.Windows.Controls import Button, Label

clear = True

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'PyCulator.xaml')
        pass

    def Number_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        number_value = getattr(sender, 'Content', 'default')
        global clear
        if clear:
            clear = False
            self.bigText.Content = number_value
        else:
            self.bigText.Content += number_value
        pass

    def Plus_Minus_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        try:
            num = int(self.bigText.Content)
            self.bigText.Content = str(-1 * num)
        except:
            self.bigText.Content = "INVALID"
        pass

    def Clear_Click(self, sender, e):
        self.bigText = self.FindName('Big_Text')
        self.smallText = self.FindName('Small_Text')
        clear_value = getattr(sender, 'Content', 'default')
        global clear
        if (clear_value == 'C'):
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
    
if __name__ == '__main__':
    print ("test")
    Application().Run(MyWindow())