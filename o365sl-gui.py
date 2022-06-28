from src.o365safelink import safelinkDecode
import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("600x320")
        self.title('o365sl')
        # vars
        self.parsedURL = tk.StringVar()
        self.parsedData = tk.StringVar()
        self.parsedSData = tk.StringVar()
        self.parsedIsReserved = tk.StringVar()
        # entries
        self.labelEntry = tk.Label(self, text='URL Source')
        self.labelEntry.pack()

        self.sourceURLText = tk.Text(self, height=5)
        self.sourceURLText.pack()

        self.decode = tk.Button(self, text='Decode', command=self.decode)
        self.decode.pack()

        self.labelEntry = tk.Label(self, text='Decoded URL')
        self.labelEntry.pack()
        self.parsedURLEntry = tk.Entry(self, textvariable=str(self.parsedURL), justify="left", width=90, state='normal')
        self.parsedURLEntry.pack()

        self.labelEntry = tk.Label(self, text='Decoded Data')
        self.labelEntry.pack()
        self.parsedSDataEntry = tk.Entry(self, textvariable=str(self.parsedData), justify="left", width=90, state='normal')
        self.parsedSDataEntry.pack()
        self.parsedSDataEntry = tk.Entry(self, textvariable=str(self.parsedSData), justify="left", width=90, state='normal')
        self.parsedSDataEntry.pack()
        # buttons

    def decode(self):
        try:
            url = self.sourceURLText.get('1.0', 'end-1c').splitlines()[0]
            data = safelinkDecode(url)
        except:
            data = {
                'url': 'error parsing value', 
                'data': 'error parsing value',
                'sdata': 'error parsing value',
                'reserved': '0'
                }

        self.parsedURL.set(data['url'])
        self.parsedData.set(data['data'])
        self.parsedSData.set(data['sdata'])
        self.parsedIsReserved.set(data['reserved'])

if __name__ == '__main__':
    app = Main()
    app.mainloop()
