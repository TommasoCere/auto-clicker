import time
import pyautogui

def get_mouse_coordinates():
    while True:
        input("Posiziona il mouse dove vuoi cliccare e premi invio")
        x, y = pyautogui.position()
        print(f"Coordinate x: {x}, y: {y}")
        return x, y
    
def number_of_clicks():
    while True:
        try:
            n = int(input("Inserisci il numero di click: "))
            return n
        except ValueError:
            print("Inserisci un numero intero")
            
def click(x, y, n):
    for i in range(n):
        # singolo click
        pyautogui.leftClick(x, y)
        #pyautogui.click(x, y)
        time.sleep(0.5)
        
def main():
    x, y = get_mouse_coordinates()
    n = number_of_clicks()
    click(x, y, n)
    
if __name__ == "__main__":
    main()